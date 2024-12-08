import sys
import copy
from part1 import create_map, PathPredictor

def create_new_possible_map(x, y, original_map):
    original_map[x][y] = "#"
    

def main():
    sys.setrecursionlimit(15000)
    map = create_map()
    
    counter = 0
    
    for x in range(len(map)):
        for y in range(len(map[x])):
            tmp_map = copy.deepcopy(map)
            if tmp_map[x][y] == "^" or tmp_map[x][y] == "#":
                continue
            else:
                tmp_map[x][y] = "#"
                   
            path_predictor = PathPredictor(tmp_map)
            start_x, start_y = path_predictor.start_position
            visited = {}
            counter += path_predictor.is_infinite_loop(start_x, start_y, visited)
    
    print(f"The answer is: {counter}")

if __name__ == '__main__':
    main()