import unittest
from app import rnd, max_num_in_list

class TestApp(unittest.TestCase):
    # check if max_num_in_list will return right value
    def test_rnd(self):
        self.assertIn(rnd(start=2, end=20), [i for i in range(2, 21)])
    '''
    The randomized result is not deterministic, making it impossible to predict the exact output. 
    However, by defining a specific range, you can ensure that the output 
    will always fall within a predetermined set of values.
    '''
    def test_rnd_check_out_of_range(self):
        self.assertNotIn(rnd(start=2, end=20), [0, 1]+[i for i in range(21, 50)])
    
    
    def test_max_num_in_list1(self):
        self.assertEqual(max_num_in_list([2, 6, 8, 7, -1]), 8, 'return value not the greatest value in max_num_in_list')



if __name__ == '__main__':
    unittest.main()
    
    