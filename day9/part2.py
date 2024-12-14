def calculate_checksum(disk):
    print(f"Calculating checksum...")
    checksum = 0
    for i in range(len(disk)):
        if disk[i] == ".":
            continue
        else:
            checksum += i * int(disk[i])

    return checksum


def rearrange_file_blocks(disk):
    print(f"Rearranging file blocks... ")

    file_block = []
    for i in range(len(disk) - 1, 0, -1):
        val = disk[i]
        if i == 0:
            break
        next_val = disk[i - 1]

        if val != ".":
            val_is_in_file_block = any(val == value for _, value in file_block)
            if len(file_block) == 0 or val_is_in_file_block:
                file_block.append((i, val))

            if val != next_val:  # end of file_block, start checking for free space
                free_space = []
                for j in range(len(disk)):
                    free = disk[j]
                    if j > i or j >= len(disk) - 1:  # no space found for file_block
                        file_block = []
                        free_space = []
                        break
                    next = disk[j + 1]
                    # print(f"Fileblock: {file_block}, size: {len(file_block)}")
                    # print(f"Freespace: {free_space}, size: {len(free_space)}")
                    if free == ".":
                        free_space.append((j, free))

                        if free != next:  # end of empty space
                            if len(free_space) < len(
                                file_block
                            ):  # no free space for file
                                # print(
                                #    f"This free space block {free_space} is not enough for {file_block}"
                                # )
                                free_space = []
                                continue  # continue to find free space...
                            else:  # free space available, do the swap!
                                # print(f"Moving {file_block} to {free_space}")
                                swap(disk, file_block, free_space)
                                file_block = []
                                free_space = []
                                break
                        else:
                            continue  # continue finding free space block

    return disk


def swap(disk, file_block, free_space):
    for i, (old_index, _) in enumerate(file_block):
        new_index, _ = free_space[i]
        disk[new_index], disk[old_index] = disk[old_index], disk[new_index]


def create_disk(puzzle_input):
    print(f"Creating file blocks...")
    disk_map = list(map(int, list(puzzle_input)))
    disk = []

    id = 0
    j = 0
    for i in range(len(disk_map)):
        if disk_map[i] == 0:
            continue
        if j == i:  # even number -> it's a file!
            for _ in range(disk_map[i]):
                disk.append(str(id))
            j += 2
            id += 1
        else:
            for _ in range(disk_map[i]):
                disk.append(".")

    return disk


def main():
    with open("day9.txt", "r") as file:
        puzzle_input = file.read()

    file_blocks = create_disk(puzzle_input)
    rearranged = rearrange_file_blocks(file_blocks)
    checksum = calculate_checksum(rearranged)

    print(f"Filesystem checksum: {checksum}")


if __name__ == "__main__":
    main()
