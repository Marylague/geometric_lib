import unittest

class SquareTestCase(unittest.TestCase) :
    
    def test_zero_mul(self):
        
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_1(self):
        
        res = area(5)
        self.assertEqual(res, 25)

    def test_2(self):
        
        res = area(70)
        self.assertEqual(res, 4900)


