from enum import Enum

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    
    def turn_right(self, step=1):
        next_direction = (self.value + step) % len(Direction)
        return Direction(next_direction)
    
    def turn_left(self, step=1):
        next_direction = (self.value - step) % len(Direction)
        return Direction(next_direction)