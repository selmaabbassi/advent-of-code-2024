from utils.AoC import AoC
import re
from typing import List
import math

#LIMIT = (11,7)
LIMIT = (101,103)

class Robot():
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        
    def move(self):
        pos_x, pos_y = self.position
        vel_x, vel_y = self.velocity
        lim_x, lim_y = LIMIT
        
        new_x = pos_x + vel_x
        new_y = pos_y + vel_y
        
        #out of bounds
        if new_x < 0:
            new_x = lim_x + new_x
        if new_x >= lim_x: 
            new_x = abs(lim_x - new_x)
        if new_y < 0:
            new_y = lim_y + new_y
        if new_y >= lim_y:
            new_y = abs(lim_y - new_y)
            
        self.position = (new_x, new_y)
        
    def is_in_Q1(self):
        pos_x, pos_y = self.position
        lim_x, lim_y = LIMIT
        
        skip_x = math.floor(lim_x/2)
        skip_y = math.floor(lim_y/2)
        
        return pos_x < skip_x and pos_y < skip_y
    
    def is_in_Q2(self):
        pos_x, pos_y = self.position
        lim_x, lim_y = LIMIT
        
        skip_x = math.floor(lim_x/2)
        skip_y = math.floor(lim_y/2)
        
        return pos_x > skip_x and pos_y < skip_y
    
    def is_in_Q3(self):
        pos_x, pos_y = self.position
        lim_x, lim_y = LIMIT
        
        skip_x = math.floor(lim_x/2)
        skip_y = math.floor(lim_y/2)
        
        return pos_x < skip_x and pos_y > skip_y
    
    def is_in_Q4(self):
        pos_x, pos_y = self.position
        lim_x, lim_y = LIMIT
        
        skip_x = math.floor(lim_x/2)
        skip_y = math.floor(lim_y/2)
        
        return pos_x > skip_x and pos_y > skip_y
        
class RobotPredictor():
    def __init__(self, robots: List[Robot]):
        self.robots: List[Robot] = robots
        
    def is_robot(self, position):
        return any(robot.position == position for robot in self.robots)
    
    def to_string(self):
        str = ""
        lim_x, lim_y = LIMIT
        for y in range(lim_y):
            for x in range(lim_x):
                if self.is_robot((x,y)):
                    str+="#"
                else:
                    str+="."
            
            str+="\n"
        
        return str
        
    def predict(self, seconds):
        for _ in range(seconds):
            for robot in self.robots:
                robot.move()
                
        return self.robots
    
    def number_of_robots_after(self, seconds):
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        
        robots: List[Robot] = self.predict(seconds)
        
        for robot in robots:
            if robot.is_in_Q1():
                q1 += 1
            if robot.is_in_Q2():
                q2 += 1
            if robot.is_in_Q3():
                q3 += 1
            if robot.is_in_Q4():
                q4 += 1
                
        return q1*q2*q3*q4

    
def create_robots(puzzle_input):
    robots = []
    
    lines = puzzle_input.split("\n")
    for line in lines:
        g = re.match(r"p=(-?\b\d+\b),(-?\b\d+\b) v=(-?\b\d+\b),(-?\b\d+\b)", line).groups()
        pos_x = int(g[0])
        pos_y = int(g[1])
        vel_x = int(g[2])
        vel_y = int(g[3])
        robots.append(Robot((pos_x,pos_y), (vel_x, vel_y)))
    
    return robots

if __name__ == '__main__':
   day14 =  AoC("day14", "day14.txt")
   puzzle_input = day14.get_puzzle_input()
   robots = create_robots(puzzle_input)
   
   predictor = RobotPredictor(robots)
   result = predictor.number_of_robots_after(100)
   
   day14.solve(result)