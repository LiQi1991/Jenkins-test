import unittest
from test.matchfunc import *

class TestMathFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("start")

    @classmethod
    def tearDownClass(cls):
        print ("finish")

    def test_add(self):
        self.assertEqual(3,add(1,2))
        self.assertNotEqual(3,add(2,2))

    def test_minus(self):
        self.assertEqual(1,minus(3,2))

    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, multi(2, 3))

    @unittest.skip("I don't want to run this case.")
    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(6, 2))

