import unittest

from day10.part1 import HikeTrailFinder
from utils.Grid import Grid

class TestHikeTrailFinder(unittest.TestCase):
    def test_traverse_to_two_tops(self):
        """Test traverse to same top with different trails"""
        grid = Grid("012300000\n123456789")
        map = grid.get_map()
        trail_finder = HikeTrailFinder(map)
        current = ((0,0), "0")
        tops = []
        trail_finder.traverse_part2(current, tops)
        
        self.assertEqual(tops, [(1, 8), (1, 8), (1, 8), (1, 8)])
        
if __name__ == '__main__':
    unittest.main()