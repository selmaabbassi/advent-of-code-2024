from utils.AoC import AoC
import os
from day14.part1 import Robot, create_robots, RobotPredictor
from sklearn.cluster import DBSCAN
import numpy as np

class EasterEggFinder(RobotPredictor):
    def __init__(self, robots):
        super().__init__(robots)
        
    def db_scan(self, robots):
        coordinates = [robot.position for robot in robots]
        points = np.array(coordinates)
        
        max_distance = 1.5
        min_samples = 8
        dbscan = DBSCAN(eps=max_distance, min_samples=min_samples)
        labels = dbscan.fit_predict(points)
        
        clusters = {}
        for label, coord in zip(labels, coordinates):
            if label not in clusters:
                clusters[label] = []
            clusters[label].append(coord)

        #print("Clusters:")
        for cluster, points in clusters.items():
            #print(f"Cluster {cluster}: {points}")
            if cluster != -1:
                print(f"Cluster found!")
                return True
            
        return False

    def move_robots(self):
        counter = 1
        
        for _ in range(10000):
            print(f"Iteration {counter}...")
            robots = self.predict(1)
            if(self.db_scan(robots)):
                self.save_to_file(counter)
            counter+=1
        
    def save_to_file(self, counter):
        print(f"Saving {counter} to file...")
        data = self.to_string()
        directory = "day14/output"
        filename = str(counter)+".txt"
        file_path = os.path.join(directory, filename)
        
        with open(file_path, "w") as file:
            file.write(data)
    

if __name__ == '__main__':
   day14 =  AoC("day14", "day14.txt")
   puzzle_input = day14.get_puzzle_input()
   robots = create_robots(puzzle_input)
   
   predictor = EasterEggFinder(robots)
   predictor.move_robots()
   
   day14.solve(6355)
   
   """
   #...................................................................................................#
........................#...................................#........................................
....................#..........#.............................................................#.....#.
.....................................................................................................
....................................................#............#.........#.................#.......
.....................#.............#.......................#.........................................
.........................................................#......................#....................
.....................#...............................................................................
......................#.......................................................#......................
..............#..........#............#...........................................#........#....#....
........................................................................#.....................#......
...................................................#..............#..................................
.................................#.....#.............................................................
..................................#..................................................................
................#.......................#...........................................#................
....#................................................................................................
.....................................................................................................
.................................................................#...................................
...................................................................................#.................
...................................................#.................................................
...............................................................................................#.....
.........................................................................#...........................
....................#................#...............................................................
..........#..........................................................................................
.................................................................#..........................#........
..................................#..................................................................
.....................................................................................................
.....................................................................................................
...#...........................................................................................#.....
#...............................................................#......................#.............
......................................................................#.........#....................
.....................................................................................................
.#..............................................#............#.......................................
......................................................#..............................................
....................................................#.#...............#..............................
...................................#...................#.............................................
......................#.................................................#............................
...........................#....................................................................#....
.....................................................................................................
..#..................................................................................................
.....................................................................................................
.............#.......................................................................................
........#.......................................................................#....................
..........................................................................................#..........
.............................................#.......................#...............................
...................................................#......................................#..........
.......#..............................#..........................................#...................
.............#.....................#................#................................................
.....................................................................................................
..........#..........................................................................................
............................................#....................#...............#...................
........................................#................#.......................................#...
...........................#..................#...................#..................................
...................................#.................................................................
........................................#............................................................
.............#................................#........###############################...............
..................................#....................#.............................#...............
.......................................................#.............................#...............
.......................................................#.............................#...............
.......................................................#.............................#...............
.......................................................#..............#..............#...............
#......................................................#.............###.............#...............
........#..............................................#............#####............#...............
...........#................#....................#.....#...........#######...........#...............
...........#...........................................#..........#########..........#....#..........
.............................................#.........#............#####............#...............
.......................................................#...........#######...........#...............
.......................................................#..........#########..........#...............
....................#........................#.........#.........###########.........#...............
.......................................................#........#############........#...............
.......................................................#..........#########..........#...............
.......................................................#.........###########.........#...............
.......................................................#........#############........#...............
.......................................................#.......###############.......#.....#.........
.......................................................#......#################......#..............#
.......................................................#........#############........#...............
.................#.....................................#.......###############.......#....#..........
........................................#..............#......#################......#...............
.......................................................#.....###################.....#....#..........
.......................................................#....#####################....#..............#
................#..............#.......................#.............###.............#...............
..............................................#........#.............###.............#...............
...................#...................................#.............###.............#...............
...................................#...................#.............................#...............
.......................................................#.............................#.....#.........
.........#.#...........................................#.............................#...............
....................#..................................#.............................#.#.............
.......................................................###############################...............
..#..................................................................................................
..........................#....................................................................#.....
.....................................#............................#...#..............................
#....................................................................................................
...................................................#............................................#....
........................................................#............................................
.....................................................................................................
...............................#.....................................................................
..#...........#.#.....................#..............................................................
............................................#........................................................
.................................#...................................................................
..............#........#.............................................................................
......................##.............................................................................
.....................................................................................................
................................#....................................................................
   """