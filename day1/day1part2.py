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

    similarity_score = 0
    for i in range(len(list_one)):
        multiplier = list_two.count(list_one[i])
        similarity_score += list_one[i] * multiplier

    print(f"The similarity score of left and right list is: {similarity_score}")
