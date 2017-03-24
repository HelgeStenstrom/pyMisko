# Inspired by
# https://testing.googleblog.com/2009/11/how-to-get-started-with-tdd.html
# AllTests.java


from calculator.CalculatorControllerTest import *
from HelloWorldTest import *

import unittest


def suite():
    s = unittest.TestSuite()

    # I would rather add the whole class with its tests; addTests.
    s.addTest(HelloWorldTest('testHelloWorld'))
    s.addTest(CalculatorControllerTest('testItShouldInitializeToZero'))
    return s

class AllTests:
    def main(self):
        res = unittest.TestResult()
        theSuite = suite()
        theSuite.run(res)
        


if __name__ == '__main__':
    AllTests().main()

    print ("Before unittest.main()")
    unittest.main()
    
