import unittest
import math

class CircleTestCase(unittest.TestCase) :
    
    def test_zero_mul(self):
        
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_1(self):
        
        res = area(5)
        self.assertEqual(res, 5 * math.pi)

    def test_2(self):
        
        res = area(98)
        self.assertEqual(res, 98 * math.pi)


