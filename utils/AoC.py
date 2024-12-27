from abc import ABC, abstractmethod
from utils.Grid import Grid
import os

class AoC:
    
    def __init__(self, directory, filename):
        self.day = directory
        self.file_path = os.path.join(directory, filename)
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f"File '{self.file_path}' does not exist.")
        
    def get_puzzle_input(self):
        with open(self.file_path, "r") as file:
            puzzle_input = file.read()
            
        return puzzle_input
    
    def to_grid(self):
        input = self.get_puzzle_input()
        return Grid(input)
    
    def to_2D_array(self):
        arr = []
        with open(self.file_path, "r") as file:
            for line in file:
                arr.append(list(line.strip()))
                
        return arr
    
    @abstractmethod
    def solve(self, result):
        """Method that must be implemented by subclasses."""
        print(f"The answer to {self.day} is: {result}")
        pass
            
            