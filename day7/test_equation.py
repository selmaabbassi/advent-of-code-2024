import unittest

from part1 import Equation

class TestMain(unittest.TestCase):
    def test_get_combinations(self):
        """Test combinations given list of numbers"""
        eq = Equation(0, numbers = [1,2,3])
        combinations = eq.get_combinations()
        
        self.assertEqual(combinations, [['*', '*'], ['*', '+'], ['+', '*'], ['+', '+']])
        
    def test_get_combinations_again(self):
        """Test combinations given list of numbers"""
        eq = Equation(0, numbers = [1,2])
        combinations = eq.get_combinations()
        
        self.assertEqual(combinations, [['*'],['+']])
        
    def test_is_valid_equation_true(self):
        """Test example equation is valid"""
        eq = Equation(190, [10,19])
        is_valid = eq.is_valid()
        
        self.assertTrue(is_valid)
        
    def test_is_valid_equation_false(self):
        """Test example equation is valid"""
        eq = Equation(161011, [16,10,13])
        is_valid = eq.is_valid()
        
        self.assertFalse(is_valid)
    
    def test_is_valid_equation_left_to_right(self):
        """Test example equation is valid"""
        eq = Equation(292, [11,6,16,20])
        is_valid = eq.is_valid()
        
        self.assertTrue(is_valid)
        
    def test_is_valid_equation_another_example(self):
        """Test example equation is valid"""
        eq = Equation(4926689152, [20, 1, 1, 8, 2, 4, 532, 5, 4, 531])
        is_valid = eq.is_valid()
        
        self.assertFalse(is_valid)
        
if __name__ == '__main__':
    unittest.main()