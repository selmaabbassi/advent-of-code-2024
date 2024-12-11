def calculate_checksum(file_blocks):
    print(f"Calculating checksum...")
    checksum = 0
    for i in range(len(file_blocks)):
        checksum += i * int(file_blocks[i])
        
    return checksum

def rearrange_file_blocks(file_blocks):
    print(f"Rearranging file blocks... ")
    
    while True:
        try:
            index = file_blocks.index(".")
        except ValueError: #no more free space left in the list!
            return file_blocks
        
        tail = file_blocks.pop()
        if tail == ".": #ignore trailing free space
            continue
        else:
            file_blocks[index] = tail

def create_file_blocks(puzzle_input):
    print(f"Creating file blocks...")
    disk_map = list(map(int, list(puzzle_input)))
    file_blocks = []
    
    id = 0
    j = 0
    for i in range(len(disk_map)):
        if disk_map[i] == 0:
            continue
        if j == i: #even number -> it's a file!
            for _ in range(disk_map[i]):
                file_blocks.append(str(id))
            j+=2
            id+=1
        else:
            for _ in range(disk_map[i]):
                file_blocks.append(".")
        
    return file_blocks

def main():
    with open("day9.txt", "r") as file:
        puzzle_input = file.read()
        
    file_blocks = create_file_blocks(puzzle_input)
    rearranged = rearrange_file_blocks(file_blocks)
    checksum = calculate_checksum(rearranged)
    
    print(f"Filesystem checksum: {checksum}")

if __name__ == '__main__':
    main()