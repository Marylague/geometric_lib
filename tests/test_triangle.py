import unittest

class TriangleTestCase(unittest.TestCase) :
    
    def test_zero_mul(self):
        
        res = area(0, 5)
        self.assertEqual(res, 0)
    
    def test_1(self):
        
        res = area(5, 2)
        self.assertEqual(res, 5)

    def test_2(self):
        
        res = area(70, 4)
        self.assertEqual(res, 140)


