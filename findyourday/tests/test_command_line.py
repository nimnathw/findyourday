import unittest
from findyourday.command_line import main


class TestCmd(unittest.TestCase):
    def test_basic(self):
       main()

if __name__ == "__main__":
    unittest.main()
