

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for name 'name_function.py"""

    def _get_formatted_name(first, middle, last):
        """Generate a neatly formatted full name."""
        full_name = f"{first} {middle} {last}"
        return full_name.title()

if __name__ == '__main__':
    unittest.main()
