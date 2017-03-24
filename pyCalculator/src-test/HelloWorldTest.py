# Inspired by
# https://testing.googleblog.com/2009/11/how-to-get-started-with-tdd.html
# HelloWorldTest.java

import unittest

print( "HelloWorldTest is loaded")

class HelloWorldTest (unittest.TestCase):
    def testHelloWorld(self):
        print ("testHelloWorld called")
        self.assertTrue(True, "Hello")

if __name__ == "__main__":
    unittest.main()
    
