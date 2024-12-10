import sys
from part1 import Grid, parse_grid

def main():
    #sys.setrecursionlimit(20000)
    grid = Grid(parse_grid("day8.txt"))
    antinodes = grid.find_antinodes_part_2()
    
    print(f"Unique antinodes is: {len(antinodes)}")

if __name__ == '__main__':
    main()