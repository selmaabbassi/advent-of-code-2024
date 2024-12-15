from utils.Grid import Grid
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(script_dir, 'day10.txt')

class HikeTrailFinder:
    def __init__(self, map: dict):
        self.map = map
        
    def number_of_valid_trails(self):
        counter = 0
        trailheads = self.find_trailheads()
        
        for trailhead in trailheads:
            counter += self.find_unique_tops(trailhead)
                
        return counter
    
    def find_trailheads(self):
        trailheads = []
        for key, value in self.map.items():
            if value == "0":
                trailheads.append((key, value))
                
        return trailheads
    
    def find_unique_tops(self, trailhead):       
        unique_tops = self.traverse(trailhead, set())
        return len(unique_tops)
                
    def traverse(self, current:tuple[tuple[int,int], str], unique_tops: set):
        if current is None:
            return
        
        cur_pos = current[0]
        cur_val = current[1]
        
        if cur_val == "9": #end of trail found!
            unique_tops.add(cur_pos)
            return
        
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        
        for direction in directions:
            next = self.get_next_position(current, direction)
            self.traverse(next, unique_tops)
                
        return unique_tops
    
    def get_next_position(self, current:tuple[tuple[int,int], str], direction:tuple[int,int]):
        cur_val = current[1]
        cx, cy = current[0]
        dx, dy = direction
        
        next_pos = (cx+1*dx, cy+1*dy)
        
        if next_pos in self.map:
            next_val = self.map[next_pos]
            if int(next_val) - int(cur_val) == 1:
                return (next_pos, next_val)
        
def main():
    with open(file_path, "r") as file:
        puzzle_input = file.read()
    
    grid = Grid(puzzle_input)
    map = grid.get_map()
    trail_finder = HikeTrailFinder(map)
    result = trail_finder.number_of_valid_trails()

    print(f"Number of valid hiking trails: {result}")

if __name__ == '__main__':
    main()