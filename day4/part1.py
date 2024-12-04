def is_xmas(lines, i, j, i_length, j_length):
    directions = [
        (-1, 0), (1, 0),  # up, down
        (0, -1), (0, 1),  # left, right
        (-1, -1), (-1, 1),  # up-left, up-right
        (1, -1), (1, 1)   # down-left, down-right
    ]

    counter = 0

    for direction in directions:
        step = 1
        concatenated_string = lines[i][j] #start with "X"
        
        while step <= 3:
            x = i + step * direction[0] #next x-coordinate
            y = j + step * direction[1] #next y-coordinate
            
            # Check if the position is out of bounds
            if x < 0 or x > i_length or y < 0 or y > j_length:
                break
            else:
                concatenated_string += lines[x][y]
                
            step += 1

        #print(f"Concat string: {concatenated_string}")
        if concatenated_string == "XMAS":
            counter += 1
        else:
            continue

    return counter


def find_nr_of_words(lines):
    counter = 0

    i_length = len(lines) - 1
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            j_length = len(lines[i]) - 1
            if lines[i][j] == "X":
                counter += is_xmas(lines, i, j, i_length, j_length)

    return counter

if __name__ == "__main__":
    lines = []

    with open("day4.txt", "r") as file:
        for line in file:
            l = list(line.strip())
            lines.append(l)

count = find_nr_of_words(lines)
print(f"Number of XMAS words: {count}")
