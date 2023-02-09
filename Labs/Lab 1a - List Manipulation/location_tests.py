# CPE 202 Location Class Test Cases, Lab 1a - List Manipulation

import unittest
from location import *

class TestLocation(unittest.TestCase):

    def test_repr(self) -> None:
        loc = Location('SLO', 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    def test_init(self) -> None:
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc.name, "SLO")
        self.assertEqual(loc.lat, 35.3)
        self.assertEqual(loc.lon, -120.7)

    def test_eq(self) -> None:
        loc1 = Location("London", 23.6, 83.3)
        loc2 = Location("Rome", 34.5, 11.1)
        loc3 = Location("London", 23.6, 83.3)
        loc4 = Location("Berlin", 123.3, -43.0)
        self.assertNotEqual(loc1, loc2)
        self.assertNotEqual(loc2, loc3)
        self.assertNotEqual(loc2, loc4)
        self.assertEqual(loc1, loc3)
        self.assertTrue(loc1 == loc3)
        self.assertTrue(loc1.__eq__(loc3))

    def test_eq_not_location(self) -> None:
        loc = Location("Paris", 93.2, 11.2)
        self.assertFalse(loc.__eq__(None))
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
