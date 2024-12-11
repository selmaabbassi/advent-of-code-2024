import unittest

from part1 import create_file_blocks, rearrange_file_blocks, calculate_checksum

class TestCreateFileBlocks(unittest.TestCase):
    def test_create_file_blocks_1(self):
        """Test create file blocks"""
        file_blocks = create_file_blocks("123")
        string = ''.join(file_blocks)
        
        self.assertEqual(string, "0..111")
        
    def test_create_file_blocks_2(self):
        """Test create file blocks"""
        file_blocks = create_file_blocks("12345")
        string = ''.join(file_blocks)
        
        self.assertEqual(string, "0..111....22222")
        
    def test_create_file_blocks_3(self):
        """Test create file blocks"""
        file_blocks = create_file_blocks("2333133121414131402")
        string = ''.join(file_blocks)
        
        self.assertEqual(string, "00...111...2...333.44.5555.6666.777.888899")
        
class TestMoveFileBlocks(unittest.TestCase):
    def test_move_file_blocks_1(self):
        fb = rearrange_file_blocks(['0', '.', '.', '1', '1', '1'])
        string = ''.join(fb)
    
        self.assertEqual(string, "0111")
        
    def test_move_file_blocks_2(self):
        fb = rearrange_file_blocks(['0', '.', '.', '1', '1', '1', '.', '.', '.', '.', '2', '2', '2', '2', '2'])
        string = ''.join(fb)
    
        self.assertEqual(string, "022111222")
        
    def test_move_file_blocks_3(self):
        fb = rearrange_file_blocks(['0', '0', '.', '.', '.', '1', '1', '1', '.', '.', '.', '2', '.', '.', '.', '3', '3', '3', '.', '4', '4', '.', '5', '5', '5', '5', '.', '6', '6', '6', '6', '.', '7', '7', '7', '.', '8', '8', '8', '8', '9', '9'])
        string = ''.join(fb)
    
        self.assertEqual(string, "0099811188827773336446555566")
        
if __name__ == '__main__':
    unittest.main()