import unittest

from part1 import PathPredictor

class TestMain(unittest.TestCase):
    def test_find_starting_position(self):
        """Test finding start position"""
        map = [["X","X","X"], 
               ["X","^","X"]]
        path_predictor = PathPredictor(map)
        start_position = path_predictor.find_start_position(map)
        
        self.assertEqual(start_position, (1,1))
        
    def test_get_next_coordinate_when_north(self):
        """Test get next coordinate when facing North"""
        map = [["X","next","X"], 
               ["X","start","X"]]
        path_predictor = PathPredictor(map)
        next_coordinate = path_predictor.get_next_coordinate(1,1)
        
        self.assertEqual(next_coordinate, (0,1))
        self.assertEqual(map[next_coordinate[0]][next_coordinate[1]], "next")
        
    def test_get_next_coordinate_when_east(self):
        """Test get next coordinate when facing East"""
        map = [["X","X","X"], 
               ["X","start","next"]]
        path_predictor = PathPredictor(map)
        path_predictor.turn_right()
        next_coordinate = path_predictor.get_next_coordinate(1,1)
        
        self.assertEqual(next_coordinate, (1,2))
        self.assertEqual(map[next_coordinate[0]][next_coordinate[1]], "next")
        
    def test_get_next_coordinate_when_south(self):
        """Test get next coordinate when facing South"""
        map = [["X","start","X"], 
               ["X","next","X"]]
        path_predictor = PathPredictor(map)
        path_predictor.turn_right()
        path_predictor.turn_right()
        next_coordinate = path_predictor.get_next_coordinate(0,1)
        
        self.assertEqual(next_coordinate, (1,1))
        self.assertEqual(map[next_coordinate[0]][next_coordinate[1]], "next")
        
    def test_get_next_coordinate_when_west(self):
        """Test get next coordinate when facing West"""
        map = [["next","start","X"], 
               ["X","X","X"]]
        path_predictor = PathPredictor(map)
        path_predictor.turn_right()
        path_predictor.turn_right()
        path_predictor.turn_right()
        next_coordinate = path_predictor.get_next_coordinate(0,1)
        
        self.assertEqual(next_coordinate, (0,0))
        self.assertEqual(map[next_coordinate[0]][next_coordinate[1]], "next")
        
    def test_traverse(self):
        """Test traversing map"""
        map = [[".","#","."], 
               [".",".","."],
               [".","^","."]]
        path_predictor = PathPredictor(map)
        counter = path_predictor.traverse_map()
        
        self.assertEqual(counter, 3)
        
if __name__ == '__main__':
    unittest.main()
