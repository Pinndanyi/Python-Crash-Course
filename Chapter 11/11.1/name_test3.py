import unittest
from name_function4 import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function能够正确运行"""
    
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        
    def test_first_middle_last(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
    
unittest.main()
    