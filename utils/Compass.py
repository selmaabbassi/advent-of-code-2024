from enum import Enum

class Compass(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    
    def turn_right(self, step=1):
        next_direction = (self.value + step) % len(Compass)
        return Compass(next_direction)
    
    def turn_left(self, step=1):
        next_direction = (self.value - step) % len(Compass)
        return Compass(next_direction)
