from enum import Enum
from gamestate import GameState
from game_state_member import GameStateMember
import random
import schedule
import pygame
import os

class Animatronic(GameStateMember):
    def __init__(self, state: GameState, name: str, room, allowed_room_ids: list, ai_level: int):
        GameStateMember.__init__(self, state)
        self.name = name
        self.room = room
        self.room.add_animatronic(self.name)
        self.stall_time = 0 # Animatronic's stalled time, they are unable to move during this period
        self.allowed_room_ids = allowed_room_ids # Rooms this animatronic can move to
        self.ai_level = ai_level

        schedule.every(0.1).seconds.do(self.decrease_stall_time)

    def decrease_stall_time(self):
        if (self.stall_time > 0):
            self.stall_time -= 0.1
        if (self.stall_time < 0):
            self.stall_time = 0
            print(f"{self.name} unstalled!")

    def attempt_movement(self):
        roll = random.randrange(1, 21)
        if roll <= self.ai_level and self.stall_time == 0:
            self.move()

    def get_adjacent_rooms(self):
        return self.room.adjacent_rooms
    
    def generate_next_movement(self) -> str:
        possible_movements = [room for room in self.get_adjacent_rooms() if room in self.allowed_room_ids]
        roll = random.randrange(0, len(possible_movements))
        selected_room = possible_movements[roll]

        if self.room.id == "OL":
            if self.state.office.left_door_closed:
                selected_room = "1B"
            else:
                selected_room = "O"
        elif self.room.id == "OR":
            if self.state.office.right_door_closed:
                selected_room = "1B"
            else:
                selected_room = "O"

        return selected_room

    def move(self):
        next_movement = self.generate_next_movement()
        if next_movement == None:
            return
        new_room = self.state.rooms[next_movement]
        self.transfer_room(new_room)
        self.state.camera.update_camera()
        if new_room.id == "O":
            self.state.end_game(self)

    def transfer_room(self, new_room):
        self.room.remove_animatronic(self.name)
        new_room.add_animatronic(self.name)
        self.room = new_room

class Bonnie(Animatronic):
    def __init__(self, state: GameState, room, ai_level: int):
        Animatronic.__init__(self, state, "Bonnie", room, ["1B", "2A", "2B", "3", "5", "OL", "O"], ai_level)

class Chica(Animatronic):
    def __init__(self, state: GameState, room, ai_level: int):
        Animatronic.__init__(self, state, "Chica", room, ["1B", "4A", "4B", "6", "7", "OR", "O"], ai_level)

class Freddy(Animatronic):
    def __init__(self, state: GameState, room, ai_level: int):
        Animatronic.__init__(self, state, "Freddy", room, [], ai_level)

    def generate_next_movement(self) -> str:
        # Freddy is stalled with the cameras open
        if self.state.camera.open:
            return

        if self.room.id == "1A" and ("Bonnie" in self.room.animatronics or "Chica" in self.room.animatronics):
            return self.room.id
        path = ["1A", "1B", "6", "5", "4A", "4B"]
        index = path.index(self.room.id)
        next_room = path[index + 1 if index < len(path) - 1 else index]

        if self.room.id == "4B" and not self.state.office.right_door_closed:
            return "O"

        return next_room

class FoxyAttackState(Enum):
    HIDDEN = 0
    PEEKING = 1
    LURKING = 2
    RUNNING = 3
    
class Foxy(Animatronic):
    def __init__(self, state: GameState, room, ai_level: int):
        Animatronic.__init__(self, state, "Foxy", room, [], ai_level)
        self.attack_state = FoxyAttackState.HIDDEN
        self.is_running = False
        self.power_penalty = 1
        self.audio_door_pounding = pygame.mixer.Sound(os.path.join("assets", "audio", "knock2.wav"))
        self.audio_running = pygame.mixer.Sound(os.path.join("assets", "audio", "run.wav"))

    def generate_next_movement(self) -> str:
        # Foxy is stalled with the cameras open
        if self.state.camera.open and not self.is_running:
            return

        if self.attack_state.value < FoxyAttackState.LURKING.value:
            self.attack_state = FoxyAttackState(self.attack_state.value + 1)
        elif self.attack_state == FoxyAttackState.LURKING:
            self.attack_state = FoxyAttackState.RUNNING
            self.running()
            self.transfer_room(self.state.rooms["2A"])
        
        return
    
    def running(self):
        print(f"{self.name} is now running")
        schedule.every(25).seconds.do(self.attempt_kill_player)
        self.is_running = True

    def seen_in_west_hall(self):
        pygame.mixer.Sound.play(self.audio_running)
        schedule.every(3).seconds.do(self.attempt_kill_player)

    def attempt_kill_player(self):
        if not self.is_running:
            return schedule.CancelJob
        
        if self.state.office.left_door_closed:
            pygame.mixer.Sound.play(self.audio_door_pounding)
            self.is_running = False
            self.attack_state = FoxyAttackState.PEEKING
            self.state.power -= self.power_penalty
            self.power_penalty += 6
            self.transfer_room(self.state.rooms["1C"])
        else:
            self.state.end_game(self)
        return schedule.CancelJob
    