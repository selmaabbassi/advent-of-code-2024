import os
from functools import lru_cache

script_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(script_dir, 'day11.txt')

@lru_cache(maxsize=None)
def update_stone(stone):
    as_string = str(stone)
    size = len(as_string)
    
    if stone == 0:
        return [1]
    elif size % 2 == 0:
        return [int(as_string[0:size//2]), int(as_string[size//2:])]
    else:
        return [stone*2024]
        
def blink(stones):
    new_map = {}
    
    for stone, occurence in stones.items():
        for new_stone in update_stone(stone):
            new_map[new_stone] = new_map.get(new_stone, 0) + occurence
                
    return new_map

def main():
    with open(file_path, "r") as file:
        puzzle_input = file.read()
        
    initial_stones = list(map(int, puzzle_input.split()))
    print(f"Initial stones: {initial_stones}")
    
    stones = {num: 1 for num in initial_stones}
    
    print(f"Blinking...")
    for i in range(75):
        stones = blink(stones)
        print(f"After {i+1} blinks: {len(stones)} unique stones")
        
    print(f"Calculating number of stones...")
    counter = sum(stones.values())
        
    print(f"Number of stones: {counter}")
if __name__ == "__main__":
    main()