from typing import Set, List
from utils.AoC import AoC
from utils.Grid import Grid, Direction
    
class GardenPlot():
    def __init__(self, plant_type):
        self.plant_type = plant_type
        self.plot = {}
        
    def append_to_plot(self, coordinate, value):
        self.plot.update({coordinate: value})
        
    def get_plant_type(self):
        return self.plant_type
    
    def get_area(self):
        return len(self.plot)
    
    def get_perimeter(self):
        perimeter = 0
        coordinates = set(self.plot.keys())
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for x,y in coordinates:
            for dx,dy in directions:
                neighbor = (x+dx, y+dy)
                if neighbor not in coordinates:
                    perimeter +=1
                    
        return perimeter
    
    def get_sides(self):
        sides = 0
        
        coordinates = set(self.plot.keys())
        
        for x, y in coordinates:
            #print(f"{self.get_plant_type()}:({x},{y})")
            left = self.__get_neighbor(x,y,Direction.LEFT)
            right = self.__get_neighbor(x,y,Direction.RIGHT)
            up = self.__get_neighbor(x,y,Direction.UP)
            down = self.__get_neighbor(x,y,Direction.DOWN)
            
            #print(f"left: {left}, right: {right}, up: {up}, down: {down}")
            if right not in coordinates and up not in coordinates:
                sides+=1
            if right not in coordinates and down not in coordinates:
                sides+=1
            if left not in coordinates and up not in coordinates:
                sides+=1
            if left not in coordinates and down not in coordinates:
                sides+=1
            
            if right in coordinates and up in coordinates:
                up_right = self.__get_neighbor(x,y, Direction.UP_RIGHT)
                if up_right not in coordinates:
                    sides+=1
                    
            if right in coordinates and down in coordinates:
                down_right = self.__get_neighbor(x,y, Direction.DOWN_RIGHT)
                if down_right not in coordinates:
                    sides+=1
                    
            if left in coordinates and up in coordinates:
                up_left = self.__get_neighbor(x,y, Direction.UP_LEFT)
                if up_left not in coordinates:
                    sides+=1
                    
            if left in coordinates and down in coordinates:
                down_left = self.__get_neighbor(x,y,Direction.DOWN_LEFT)
                if down_left not in coordinates:
                    sides+=1
                
        return sides
            
    
    def __get_neighbor(self, x,y, direction: Direction):
        dx, dy = direction.value
        return (x+dx, y+dy)

    def print(self):
        print(self.plot)
    
class GardenPlotFinder:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.garden: dict = grid.get_map()
    
    def find_garden_plots(self):
        visited: Set[tuple[int,int]] = set()
        garden_plots: List[GardenPlot] = []
        
        for plant in self.garden.items():
            coordinate, target_value = plant
            if coordinate not in visited:
                garden_plot = GardenPlot(target_value)
                self.__deep_first_search(self.garden, plant, target_value, visited, garden_plot)
                garden_plots.append(garden_plot)
                
        return garden_plots
    
    def get_neighbors(self, plant:tuple[tuple[int,int], str]):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        coordinate, _ = plant
        x, y = coordinate
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            if (nx,ny) in self.garden.keys():
                neighbors.append(((nx,ny), self.garden[(nx,ny)]))
                
        return neighbors
        
    def __deep_first_search(self, grid:dict, plant:tuple[tuple[int,int], str], target_value:str, visited: Set[tuple[int,int]], garden_plot: GardenPlot):
        coordinate, value = plant
        
        if coordinate in visited or grid[coordinate] != target_value:
            return garden_plot
        
        visited.add(coordinate)
        garden_plot.append_to_plot(coordinate, value)
        
        neighbors = self.get_neighbors(plant)
        for neighbor in neighbors:
            self.__deep_first_search(grid, neighbor, target_value, visited, garden_plot)

if __name__ == '__main__':
    day12 = AoC("day12", "day12.txt")
    grid = day12.to_grid()
    
    gpf = GardenPlotFinder(grid)
    garden_plots = gpf.find_garden_plots()
    
    result = 0
    
    for plot in garden_plots:
        #print(f"Plant {plot.get_plant_type()}: Area ({plot.get_area()}), Sides ({plot.get_sides()})")
        area = plot.get_area()
        perimeter = plot.get_perimeter()
        side = plot.get_sides()
        
        result += area*side
        
    day12.solve(result)