import  unittest
from mock import patch
import findyourday.functions 


class TestFunction(unittest.TestCase):        

    def test_find_day(self):
        with patch('__builtin__.raw_input', return_value = '29/12/1974') as _raw_input:
            self.assertEqual(findyourday.functions.find_day(), 'Sunday')


"""
    def test_find_day2(self):
        with patch('__builtin__.raw_input', return_value = 'ewaflh') as _raw_input:
            self.assertEqual(findyourday.functions.find_day(), 'Format error. Date should not include letters. \n')
  
    def test_find_day3(self):
        with patch('__builtin__.raw_input', return_value = '13\\12') as _raw_input:
            self.assertEqual(findyourday.functions.find_day(), 'Format error. Date should follow 01/01/2017 format. Days, months, and years should be separated by forward slashes (/). Do not type backward slashes(\). \n')
    
    def test_find_day4(self):
        with patch('__builtin__.raw_input', return_value = '123456') as _raw_input:
            self.assertEqual(findyourday.functions.find_day(), 'ValueError. Please follow the day/month/year format e.g. 01/01/2017 \n')
"""


if __name__ == '__main__':
    unittest.main()
