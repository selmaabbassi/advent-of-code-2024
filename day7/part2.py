import itertools
from typing import List

class Equation:
    def __init__(self, solution, numbers):
         self.solution = solution
         self.numbers = numbers
    
    def is_valid(self):
        combinations = self.get_combinations()
    
        for combination in combinations:
            result = self.numbers[0]
            expression = f"{self.numbers[0]}"

            for i, operator in enumerate(combination):
                expression += f" {operator} {self.numbers[i+1]}"
                if operator == '||':
                    result = int(str(result)+str(self.numbers[i+1]))
                if operator == '+':
                    result += self.numbers[i+1]
                elif operator == '*':
                    result *= self.numbers[i+1]

            if result == self.solution:
                #print(f"Valid equation: {self.solution}={expression}, result={result}")
                return True
            else:
                #print(f"Invalid equation: {self.solution}={expression}, result={result}")
                continue
    
        return False

    def get_combinations(self):
        operators = ['*', '+', '||']
        return [list(combinations) for combinations in itertools.product(operators, repeat=len(self.numbers) - 1)]

def parse_file():
    equations :List[Equation] = []
    
    with open("day7.txt", "r") as file:
        for line in file:
            l = line.replace("\n", "")
            t = l.split(":")
            solution = int(t[0])
            numbers = list(map(int, t[1].strip().split(" ")))
            equations.append(Equation(solution, numbers))
            
    return equations

def main():
    equations: List[Equation] = parse_file()
    
    counter = 0
    
    for equation in equations:
        if equation.is_valid():
            counter += equation.solution
            
    print(f"Total calibration result: {counter}")

if __name__ == '__main__':
    main()