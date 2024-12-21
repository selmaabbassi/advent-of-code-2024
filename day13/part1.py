from typing import List
from utils.AoC import AoC
import re

class ClawMachine():
    def __init__(self, A:tuple[int,int], B:tuple[int,int], prize:tuple[int,int]):
        self.buttonA = A
        self.buttonB = B
        self.prize = prize
        
    def solve_equation(self):
        Ax, Ay = self.buttonA
        Bx, By = self.buttonB
        Px, Py = self.prize
        
        ##Ax*a+Bx*b=Px => 94a+22b=8400
        ##Ay*a+By*b=Py => 34a+67b=5400
        
        r1 = By*Px #67*8400 = 562 800
        r2 = Bx*Py #22*5400 = 118 800
        
        a1 = By*Ax#67*94 = 6298a
        a2 = Bx*Ay#22*34 = 748a
        
        rr = r1 - r2 #562 800 - 118 800 = 444 000
        aa = a1 - a2 #6298a - 748a = 5550a
        
        a = rr/aa # a = 80
        b = (Px-(Ax*a))/Bx #b = 40
        
        return (a,b)
        
    def print(self):
        Ax, Ay = self.buttonA
        Bx, By = self.buttonB
        Px, Py = self.prize
        print(f"Claw Machines specs: Button A: X+{Ax}, Y+{Ay}, Button B: X+{Bx}, Y+{By}, Prize: X={Px}, Y={Py}")
        
class TokenCalculator():
    def __init__(self, machines: List[ClawMachine]):
        self.machines = machines
        
    def is_prize_attainable(self, a, b):
        #if a > 100 or b > 100:
            #return False
        if a % 1 == 0 and b % 1 == 0:
            return True
        
        return False
            
    def calculate_tokens(self):
        tokens = 0
        
        for machine in self.machines:
            a, b = machine.solve_equation()
            if self.is_prize_attainable(a,b):
                tokens += (a*3) + b
                
        return int(tokens)
        
    def print(self):
        for machine in self.machines:
            machine.print()

def create_claw_machine(puzzle_input:str):
    machine_str = puzzle_input.split("\n")
    test = ",".join(machine_str)
    
    buttonA = re.search("Button A: X\+(\d*), Y\+(\d*)", test).groups()
    buttonB = re.search("Button B: X\+(\d*), Y\+(\d*)", test).groups()
    prize = re.search("Prize: X=(\d*), Y=(\d*)", test).groups()
    
    Bx, By = int(buttonB[0]), int(buttonB[1])
    Ax, Ay = int(buttonA[0]), int(buttonA[1])
    Px, Py = int(prize[0])+10000000000000, int(prize[1])+10000000000000
    
    return ClawMachine((Ax,Ay), (Bx,By), (Px,Py))
    
def parse_input(puzzle_input:str):
    machines_str = puzzle_input.split("\n\n")
    machines: List[ClawMachine] = []
    
    for machine in machines_str:
        machines.append(create_claw_machine(machine))
        
    return machines

if __name__ == '__main__':
    day13 = AoC("day13", "day13.txt")
    input = day13.get_puzzle_input()
    
    machines = parse_input(input)
    tc = TokenCalculator(machines)
    tokens = tc.calculate_tokens()
    
    day13.solve(tokens)