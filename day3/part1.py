import re

if __name__ == "__main__":
    with open("day3.txt", "r") as file:
        data = file.read()

matches = re.findall(r"mul(\(\d*,\d*\))", data)

counter = 0

for match in matches:
    print(match)
    numbers = re.match(r"\((\d*),(\d*)\)", match).groups()
    print(numbers)
    counter += (int(numbers[0]) * int(numbers[1]))

print(f"The answer is: {counter}")
