# Inspired by
# https://testing.googleblog.com/2009/11/how-to-get-started-with-tdd.html
# CalculatorControllerTest.java

import CalculatorController as c
import CalculatorModel as m
import unittest

print("CalculatorControllerTest is loaded")

class CalculatorControllerTest (unittest.TestCase):
    def testItShouldInitializeToZero (self):
        model = m.CalculatorModel()
        controller = c.CalculatorController(model)
        controller.push('C')
        self.assertEqual("0.", model.getDisplay())
        


if __name__ == '__main__':
    unittest.main()
    
