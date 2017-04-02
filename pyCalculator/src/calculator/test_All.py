# Inspired by
# https://testing.googleblog.com/2009/11/how-to-get-started-with-tdd.html
# AllTests.java

import test_HelloWorld
import test_CalculatorController


import unittest


def suite():
    s = unittest.TestSuite()

    # I would rather add the whole class with its tests; addTests.
    s.addTest(test_HelloWorld.HelloWorldTest('testHelloWorld'))
    s.addTest(test_CalculatorController.CalculatorControllerTest('testItShouldInitializeToZero'))
    return s

class AllTests:
    def main(self):
        res = unittest.TestResult()
        theSuite = suite()
        print("AllTests.main() is run")
        theSuite.run(res)
        


if __name__ == '__main__':
    AllTests().main()

    print ("Before unittest.main()")
    um = unittest.main
    # help(um)
    #print(dir(um))
    um(suite())
    print ("End of test_All.py") 
