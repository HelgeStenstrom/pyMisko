# Inspired by
# https://testing.googleblog.com/2009/11/how-to-get-started-with-tdd.html
# AllTests.java

import calculator.CalculatorControllerTest as CCT # Heter det så i Python?
import unittest
import HelloWorldTest

def suite():
    s = unittest.TestSuite()
    s.addTest(HelloWorldTest.HelloWorldTest('testHelloWorld'))
    s.addTest(CCT.CalculatorControllerTest('testItShouldInitializeToZero'))
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
    
