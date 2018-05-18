import unittest

from test_matchfunc import TestMathFunc
from HtmlTestRunner import  HTMLTestRunner

if __name__  == '__main__':
    suite = unittest.TestSuite()
    tests = [TestMathFunc("test_divide"),TestMathFunc("test_multi"),TestMathFunc("test_add"),TestMathFunc("test_minus")]
    # for i in tests:
    #     suite.addTest(i)
 
   suite.addTests(tests)
   with open('test.html','wb') as f:
        runner = HTMLTestRunner(output='/Users/name/jenk/Jenkins-test/untitled')
        runner.run(suite)
