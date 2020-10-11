import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for name 'name_function.py"""

    def test_fisrt_last_name(self):
        """Do name like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()
