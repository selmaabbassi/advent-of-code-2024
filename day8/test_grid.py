import unittest

from part1 import Grid

class TestGrid(unittest.TestCase):
    def test_encapsulate_point(self):
        """Test get antinodes given two points"""
        grid = Grid()
        A = (1, 2)
        B = (2, 3)
        P1, P2 = grid.calculate_antinodes(A,B)
        
        print(f"P1: {P1}, P2: {P2}")
        
        self.assertEqual(P2, (3, 4))
        self.assertEqual(P1, (0, 1))
        
        
if __name__ == '__main__':
    unittest.main()