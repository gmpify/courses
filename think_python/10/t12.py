import unittest

import e12

class E12Test(unittest.TestCase):
    def test_create_interlock(self):
        self.assertEqual(e12.create_interlock("show", "cold"), "schooled")

if __name__ == "__main__":
    unittest.main()
