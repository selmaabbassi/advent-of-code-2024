import sys
from direction import Direction

class PathPredictor:
    direction: Direction = Direction.NORTH
    compass = {
            Direction.NORTH: (-1,0), 
            Direction.EAST: (0,1),
            Direction.SOUTH: (1,0),
            Direction.WEST: (0,-1)
            }
    
    def __init__(self, map):
        self.map = map
        self.start_position = self.find_start_position(map)
        
    def traverse_map(self):
        start_x, start_y = self.start_position
        self.__traverse(start_x, start_y)
        
        return self.__number_of_distinct_traversed_positions(self.map)
        
    def __traverse(self, current_x, current_y):
        next_x, next_y = self.get_next_coordinate(current_x, current_y)
        
        if next_x >= len(self.map) or next_x < 0 or next_y >= len(self.map[current_x]) or next_y < 0:
            self.map[current_x][current_y] = "X"
            return
        
        if self.map[next_x][next_y] == "#":
            self.turn_right()
            self.__traverse(current_x, current_y)
        else:
            self.map[current_x][current_y] = "X"
            self.__traverse(next_x, next_y)
            
    def __number_of_distinct_traversed_positions(self, updated_map):
        counter = 0
        for x in range(len(updated_map)):
            for y in range(len(updated_map[x])):
                if updated_map[x][y] == "X":
                    counter += 1
                    
        return counter
                
    def find_start_position(self, map):
        for x in range(len(map)):
            for y in range(len(map[x])):
                if map[x][y] == "^":
                    return (x,y)
        
    def get_next_coordinate(self, x, y):
        i, j = self.compass.get(self.direction)
        step = 1
        new_x = x + (step * i)
        new_y = y + (step * j)
        return (new_x, new_y)
        
    def turn_right(self):
        next_direction = self.direction.turn_right()
        self.direction = next_direction

def create_map():
    map = []
    with open("day6.txt", "r") as file:
        for line in file:
            map.append(list(line.replace("\n", "")))
    
    return map

def main():
    sys.setrecursionlimit(6000)
    map = create_map()
    path_predictor = PathPredictor(map)
    result = path_predictor.traverse_map()
    
    print(f"The answer is: {result}")

if __name__ == '__main__':
    main()