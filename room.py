from game_state_member import GameStateMember
from gamestate import GameState
from animatronic import FoxyAttackState

class Room(GameStateMember):
    def __init__(self, state: GameState, id: str, name: str, adjacent_rooms: list):
        self.state = state
        self.id = id
        self.name = name
        self.adjacent_rooms = adjacent_rooms
        self.animatronics = []
        self.textures = {
            "empty": "12.png",
            "bonnie": "12.png",
            "chica": "12.png",
            "freddy": "12.png",
            "foxy": "12.png"
        }

    def get_texture(self) -> str:
        if len(self.animatronics) == 0:
            return self.textures["empty"]
        elif "Bonnie" in self.animatronics:
            return self.textures["bonnie"]
        elif "Chica" in self.animatronics:
            return self.textures["chica"]
        elif "Freddy" in self.animatronics:
            return self.textures["freddy"]
        elif "Foxy" in self.animatronics:
            return self.textures["foxy"]

    def add_animatronic(self, animatronic_name: str):
        self.animatronics.append(animatronic_name)

    def remove_animatronic(self, animatronic_name: str):
        if animatronic_name in self.animatronics:
            self.animatronics.remove(animatronic_name)

room_names = {
    "1A": "Show Stage",
    "1B": "Dining Area",
    "1C": "Pirate Cove",
    "2A": "West Hall",
    "2B": "W. Hall Corner",
    "3": "Supply Closet",
    "4A": "East Hall",
    "4B": "E. Hall Corner",
    "5": "Backstage",
    "6": "Kitchen",
    "7": "Restrooms",
    "O": "Office",
    "OL": "Left Door",
    "OR": "Right Door"
}

class ShowStage(Room):
    def __init__(self, state: GameState):
        Room.__init__(self, state, "1A", room_names["1A"], ["1B"])
        self.textures["all"] = "19.png"
        self.textures["missing_bonnie"] = "68.png"
        self.textures["missing_chica"] = "223.png"
        self.textures["freddy"] = "224.png"
        self.textures["freddy2"] = "355.png"
        self.textures["empty"] = "484.png"

    def get_texture(self) -> str:
        if "Freddy" in self.animatronics:
            if "Bonnie" in self.animatronics and "Chica" in self.animatronics:
                return self.textures["all"]
            elif "Bonnie" in self.animatronics:
                return self.textures["missing_chica"]
            elif "Chica" in self.animatronics:
                return self.textures["missing_bonnie"]
            else:
                return self.textures["freddy"]
        else:
            return self.textures["empty"]

class DiningArea(Room):
    def __init__(self, state: GameState):
        Room.__init__(self, state, "1B", room_names["1B"], ["5", "1C", "7", "6", "2A", "4A"])
        self.textures["empty"] = "48.png"
        self.textures["bonnie"] = "90.png"
        self.textures["bonnie2"] = "120.png"
        self.textures["chica"] = "215.png"
        self.textures["chica2"] = "222.png"
        self.textures["freddy"] = "492.png"

class PirateCove(Room):
    def __init__(self, state: GameState):
        Room.__init__(self, state, "1C", room_names["1C"], ["1B"])
        self.textures["hidden"] = "66.png"
        self.textures["peeking"] = "211.png"
        self.textures["lurking"] = "338.png"
        self.textures["running"] = "240.png"
    
    def get_texture(self) -> str:
        attack_state = self.state.animatronics["Foxy"].attack_state

        if attack_state == FoxyAttackState.HIDDEN:
            return self.textures["hidden"]
        if attack_state == FoxyAttackState.PEEKING:
            return self.textures["peeking"]
        if attack_state == FoxyAttackState.LURKING:
            return self.textures["lurking"]
        if attack_state == FoxyAttackState.RUNNING:
            return self.textures["running"]


class WestHall(Room):
    def __init__(self, state: GameState):
        Room.__init__(self, state, "2A", room_names["2A"], ["3", "2B", "OL"])
        self.textures["empty"] = "44.png"
        self.textures["bonnie"] = "206.png"
        self.textures["foxy"] = "306.png"

class WestHallCorner(Room):
    def __init__(self, state: GameState):
        Room.__init__(self, state, "2B", room_names["2B"], ["2A", "OL"])
        self.textures["empty"] = "0.png"
        self.textures["empty_scary"] = "540.png"
        self.textures["empty_scary2"] = "571.png"
        self.textures["bonnie"] = "188.png"

class SupplyCloset(Room):
    def __init__(self, state: GameState):
        Room.__init__(self, state, "3", room_names["3"], ["2A"])
        self.textures["empty"] = "62.png"
        self.textures["bonnie"] = "190.png"
        self.textures["empty_scary"] = "354.png"

class EastHall(Room):
    def __init__(self, state: GameState):
        Room.__init__(self, state, "4A", room_names["4A"], ["4B", "OR"])
        self.textures["chica2"] = "221.png"
        self.textures["chica"] = "226.png"
        self.textures["empty"] = "67.png"
        self.textures["freddy"] = "487.png"

class EastHallCorner(Room):
    def __init__(self, state: GameState):
        Room.__init__(self, state, "4B", room_names["4B"], ["4A", "OR"])
        self.textures["empty"] = "49.png"
        self.textures["chica"] = "220.png"
        self.textures["freddy"] = "486.png"

class Backstage(Room):
    def __init__(self, state: GameState):
        Room.__init__(self, state, "5", room_names["5"], ["1B"])
        self.textures["empty"] = "83.png"
        self.textures["bonnie"] = "205.png"
        self.textures["dead"] = "358.png"

class Kitchen(Room):
    def __init__(self, state: GameState):
        Room.__init__(self, state, "6", room_names["6"], ["1B"])

class Restrooms(Room):
    def __init__(self, state: GameState):
        Room.__init__(self, state, "7", room_names["7"], ["1B"])
        self.textures["empty"] = "41.png"
        self.textures["chica"] = "217.png"
        self.textures["chica2"] = "219.png"
        self.textures["freddy"] = "494.png"

class OfficeLeftDoor(Room):
    def __init__(self, state: GameState):
        Room.__init__(self, state, "OL", room_names["OL"], ["2A", "2B"])

class OfficeRightDoor(Room):
    def __init__(self, state: GameState):
        Room.__init__(self, state, "OR", room_names["OR"], ["4A", "4B"])


