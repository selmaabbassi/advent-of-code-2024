def is_xmas(lines, i, j, i_length, j_length):
    directions = [
        (-1, -1), (-1, 1),  # up-left, up-right
        (1, -1), (1, 1)   # down-left, down-right
    ]

    is_out_of_bounds = False
    
    for direction in directions:
        x = i + 1 * direction[0] #next x-coordinate
        y = j + 1 * direction[1] #next y-coordinate
            
        # Check if the position is out of bounds
        if x < 0 or x > i_length or y < 0 or y > j_length:
            is_out_of_bounds = True
            break;

    if is_out_of_bounds == False:
        up_left = lines[i-1][j-1]
        up_right = lines[i-1][j+1]
        down_left = lines[i+1][j-1]
        down_right = lines[i+1][j+1]

        if (up_left == "M" and down_right == "S" or up_left == "S" and down_right == "M") and (up_right == "M" and down_left == "S" or up_right == "S" and down_left == "M"):
            return 1
        else:
            return 0
    else:
        return 0
        


def find_nr_of_words(lines):
    counter = 0

    i_length = len(lines) - 1
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            j_length = len(lines[i]) - 1
            if lines[i][j] == "A":
                counter += is_xmas(lines, i, j, i_length, j_length)

    return counter

if __name__ == "__main__":
    lines = []

    with open("day4.txt", "r") as file:
        for line in file:
            l = list(line.strip())
            lines.append(l)

count = find_nr_of_words(lines)
print(f"Number of X-MAS words: {count}")
