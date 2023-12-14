import pygame
import schedule
from gamestate import GameState
from animatronic import Bonnie, Chica, Freddy, Foxy, Animatronic
from camera_toggle_button import CameraToggleButton
from office import Office
from camera import Camera
from clock import Clock
from text import Text
import room
import sys


class OfficeGameState(GameState):

    def initialize(self):
        GameState.initialize(self)
        self.office = Office(self, pygame.Rect(0, 0, 1920, 1080))
        self.add_object("office", self.office)
        self.add_object("camera_toggle", CameraToggleButton(self, pygame.Rect(350, 970, 950, 75)), 4)

        self.hour = 0
        self.power = 100

        self.rooms = {
            "1A": room.ShowStage(self),
            "1B": room.DiningArea(self),
            "1C": room.PirateCove(self),
            "2A": room.WestHall(self),
            "2B": room.WestHallCorner(self),
            "3": room.SupplyCloset(self),
            "4A": room.EastHall(self),
            "4B": room.EastHallCorner(self),
            "5": room.Backstage(self),
            "6": room.Kitchen(self),
            "7": room.Restrooms(self),
            "O": room.Room(self, "O", room.room_names["O"], ["OL", "OR"]),
            "OL": room.OfficeLeftDoor(self),
            "OR": room.OfficeRightDoor(self)
        }

        show_stage = self.rooms["1A"]
        pirate_cove = self.rooms["1C"]

        self.animatronics = {
            "Bonnie": Bonnie(self, show_stage, 20),
            "Chica": Chica(self, show_stage, 20),
            "Freddy": Freddy(self, show_stage, 20),
            "Foxy": Foxy(self, pirate_cove, 20)
        }

        self.camera = Camera(self, pygame.Rect(0, 0, 1920, 1080), show_stage)
        self.clock = Clock(self, pygame.Rect(100, 100, 100, 100), 0)

        schedule.every(3.02).seconds.do(self.animatronics["Freddy"].attempt_movement)
        schedule.every(4.97).seconds.do(self.animatronics["Bonnie"].attempt_movement)
        schedule.every(4.98).seconds.do(self.animatronics["Chica"].attempt_movement)
        schedule.every(5.01).seconds.do(self.animatronics["Foxy"].attempt_movement)

        schedule.every(90).seconds.do(self.increment_hour)
        schedule.every(0.1).seconds.do(self.decrement_power_one_hundred_ms)
        schedule.every(1).seconds.do(self.update_power_text)

        self.power_text = Text(self, pygame.Rect(20, 925, 300, 75), pygame.font.Font('freesansbold.ttf', 32), f"Power: {round(self.power)}%", (255, 255, 255))
        self.add_object("power_text", self.power_text, 5)

    def get_power_usage(self, ms):
        power_decrease_interval = 10.0
        if self.game.night == 2 or self.game.night == 3:
            power_decrease_interval = 9.0
        elif self.game.night == 4:
            power_decrease_interval = 8.0
        elif self.game.night >= 5:
            power_decrease_interval = 7.6

        power_drainage_per_second = 1 / power_decrease_interval
        power_drainage_per_second *= self.power_usage_multiplier()
        return (power_drainage_per_second / 1000) * ms
    
    def decrement_power_one_hundred_ms(self):
        self.power -= self.get_power_usage(100)

    def power_usage_multiplier(self) -> int:
        multiplier = 1
        if self.camera.open:
            multiplier += 1
        if self.office.left_door_closed:
            multiplier += 1
        if self.office.right_door_closed:
            multiplier += 1
        if self.office.left_light_on:
            multiplier += 1
        elif self.office.right_light_on:
            multiplier += 1
        return multiplier
    
    def update_power_text(self):
        self.power_text.change_string(f"Power: {round(self.power)}%")

    def decrement_power(self):
        self.power -= self.get_power_usage_one_hundred_ms()
        self.update_power_text()

    def increment_hour(self):
        self.hour += 1
        self.clock.set_hour(self.hour)
        if (self.hour == 6):
            print(f"You win with {self.power}% power remaining")
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    def end_game(self, animatronic):
        print(f"{animatronic.name} reached the office. Game over!")
        pygame.display.quit()
        pygame.quit()
        sys.exit()

    def exit(self):
        GameState.exit(self)

    def toggle_camera(self):
        self.camera.toggle_camera()
        self.office.deactivate_lights()