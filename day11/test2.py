import unittest
from day11.part2 import update_stone

class TestDay11Part2(unittest.TestCase):
    def test_update_stone_rule_1(self):
        result = list(update_stone(0))[0]
        
        self.assertEqual(result, 1)
        
    def test_update_stone_rule_2(self):
        result = list(update_stone(12))
        
        self.assertEqual(result[0], 1)
        self.assertEqual(result[1], 2)
        
    def test_update_stone_rule_3(self):
        result = list(update_stone(2))[0]
        
        self.assertEqual(result, 4048)
        
if __name__ == '__main__':
    unittest.main()   