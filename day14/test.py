import unittest

from day14.part1 import Robot

class TestDay14(unittest.TestCase):
    def test_move_robot(self):
        """Test move robot"""
        robot = Robot((2,4), (2,-3))
        
        for _ in range(5):
            robot.move()
        
        pos = robot.position
        
        self.assertEqual(pos, (1,3))
        
    def test_is_in_quadrant(self):
        """Test robot is in quadrant"""
        robot_x = Robot((5,1), (1,1))
        robot_y = Robot((1,3), (1,1))
        robot = Robot((4,2), (1,1))
        
        res_x = robot_x.is_in_Q1()
        res_y = robot_y.is_in_Q1()
        res = robot.is_in_Q1()
        
        self.assertFalse(res_x)
        self.assertFalse(res_y)
        self.assertTrue(res)
        
if __name__ == '__main__':
    unittest.main()