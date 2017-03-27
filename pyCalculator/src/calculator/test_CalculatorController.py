# Inspired by
# https://testing.googleblog.com/2009/11/how-to-get-started-with-tdd.html
# CalculatorControllerTest.java

import calculator
import unittest

print("CalculatorControllerTest is loaded")

class CalculatorControllerTest (unittest.TestCase):
    def testItShouldInitializeToZero (self):
        model = calculator.CalculatorModel()
        controller = CalculatorController(model)
        controller.push('C')
        self.assertEquals("0.", model.getDisplay())
        


if __name__ == '__main__':
    unittest.main()
    
