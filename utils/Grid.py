from typing import List
from utils.Direction import Direction

class Grid:
    def __init__(self, puzzle_input: str):
        self.map: dict = {}
        self.__create_map(puzzle_input)
                
    def __create_map(self, puzzle_input: str):  
        data = []
        
        lines = puzzle_input.split("\n")
        for line in lines:
            data.append(list(line.strip()))
            
        self.map = self.from_2D_array_to_grid(data)
                
    def from_2D_array_to_grid(self, data):
        map = {}
        
        for x in range(len(data)):
            for y in range(len(data[x])):
                map[(x,y)] = data[x][y]
                
        return map
    
    def get_map(self):
        return self.map
    
    def get_directions(self):
        return [direction.value for direction in Direction]
        
    def print(self):
        print(self.map)
