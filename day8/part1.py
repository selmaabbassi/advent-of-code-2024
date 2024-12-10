import math
from typing import List

class Grid: 
    def __init__(self, grid = {}):
        self.grid = grid
        
    def calculate_antinodes(self, A, B):
        Ax, Ay = A
        Bx, By = B

        P1 = (2*Ax-Bx, 2*Ay-By)
        P2 = (2*Bx-Ax, 2*By-Ay)
        
        return [P1, P2]
    
    def find_antinodes(self):
        visited = set()
        antinodes = set()
        
        for a, value in self.grid.items():
            visited.add(a)
            if value != ".":
                coordinates_with_value = [k for k, v in self.grid.items() if v == value and k not in visited]
                
                for b in coordinates_with_value:
                    antinodes.update([antinode for antinode in self.calculate_antinodes(a,b) if antinode in self.grid])
                
        return antinodes
    
    def calculate_antinodes_part_2(self, A, B):
        Ax, Ay = A
        Bx, By = B
        
        dx = Ax-Bx
        dy = Ay-By
        
        points = set()
        for i in range(-50, 50):
            P1 = (Ax+dx*i,Ay+dy*i)
            if P1 in self.grid:
                points.add(P1)
        
        return points
    
    def find_antinodes_part_2(self):
        visited = set()
        antinodes = set()
        
        for a, value in self.grid.items():
            visited.add(a)
            if value != ".":
                coordinates_with_value = [k for k, v in self.grid.items() if v == value and k not in visited]
                for b in coordinates_with_value:
                    antinodes.update(self.calculate_antinodes_part_2(a,b))
                
        return antinodes

def parse_grid(filename):
    grid = {}
    data = []
    
    with open(filename, "r") as file:
        for line in file:
            chars = list(line.strip())
            data.append(chars)
            
    for x in range(len(data)):
        for y in range(len(data[x])):
            grid[(x,y)] = data[x][y]
            
    return grid
    
def main():
    grid = Grid(parse_grid("day8.txt"))
    antinodes = grid.find_antinodes()
    
    print(f"Unique antinodes is: {len(antinodes)}")

if __name__ == '__main__':
    main()