from typing import List

class Grid:
    def __init__(self, puzzle_input: str):
        self.map: dict = {}
        self.__create_map(puzzle_input)
        
    def __create_map(self, puzzle_input: str):  
        data = []
        
        lines = puzzle_input.split("\n")
        for line in lines:
            data.append(list(line.strip()))
            
        for x in range(len(data)):
            for y in range(len(data[x])):
                self.map[(x,y)] = data[x][y]
                
    def get_map(self):
        return self.map
        
    def print(self):
        print(self.map)
