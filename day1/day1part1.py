if __name__ == "__main__":
    list_one = []
    list_two = []

    with open("day1.txt", "r") as file:
        for line in file:
            split = line.split("   ")
            list_one.append(int(split[0]))
            list_two.append(int(split[1]))

    print(f"List 1: {list_one}")
    print(f"List 2: {list_two}")

    list_one.sort()
    list_two.sort()

    print(f"List 1 sorted: {list_one}")
    print(f"List 2 sorted: {list_two}")

    total_distance = 0
    for i in range(len(list_one)):
        diff = abs(list_two[i] - list_one[i])
        total_distance += diff

    print(f"The total distance between left and right list is: {total_distance}")
