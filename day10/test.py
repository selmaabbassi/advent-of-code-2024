import unittest

from day10.part1 import HikeTrailFinder
from utils.Grid import Grid

class TestHikeTrailFinder(unittest.TestCase):
    def test_find_trailheads(self):
        """Test find trailheads"""
        grid = Grid("0123\n1234\n8765\n9876")
        map = grid.get_map()
        
        trail_finder = HikeTrailFinder(map)
        start = trail_finder.find_trailheads()
        
        self.assertEqual(start, [((0, 0), "0")])
        
    def test_find_2_trailheads(self):
        """Test find 2 trailheads"""
        grid = Grid("10..9..\n2...8..\n3...7..\n4567654\n...8..3\n...9..2\n.....01")
        map = grid.get_map()
        trail_finder = HikeTrailFinder(map)
        start = trail_finder.find_trailheads()
        
        self.assertEqual(start, [((0, 1), "0"), ((6, 5), "0")])
        
    def test_find_next_position(self):
        """Test find next position"""
        grid = Grid("0123\n1234\n8765\n9876")
        map = grid.get_map()
        
        trail_finder = HikeTrailFinder(map)
        next = trail_finder.get_next_position(((0,0), "0"),(0,1))
        
        self.assertEqual(next, ((0,1),"1"))
        
    def test_find_next_position_yields_none(self):
        """Test find next position"""
        grid = Grid("0523\n9234\n8765\n9876")
        map = grid.get_map()
        
        trail_finder = HikeTrailFinder(map)
        next = trail_finder.get_next_position(((0,0), "0"), (-1, 0))
        
        self.assertIsNone(next)
        
    def test_traverse(self):
        """Test traverse"""
        grid = Grid("0123456789")
        map = grid.get_map()
        
        trail_finder = HikeTrailFinder(map)
        current = ((0,0), "0")
        unique_tops = set()
        result = trail_finder.traverse(current, unique_tops)
        
        self.assertEqual(result, {(0,9)})
        
    def test_traverse_to_two_tops(self):
        """Test traverse"""
        grid = Grid("0123456789\n1234567892")
        map = grid.get_map()
        trail_finder = HikeTrailFinder(map)
        current = ((0,0), "0")
        unique_tops = set()
        trail_finder.traverse(current, unique_tops)
        
        self.assertEqual(unique_tops, {(0, 9),(1, 8)})
        
if __name__ == '__main__':
    unittest.main()