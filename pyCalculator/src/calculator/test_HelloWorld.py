# Inspired by
# https://testing.googleblog.com/2009/11/how-to-get-started-with-tdd.html
# HelloWorldTest.java

import unittest

class HelloWorldTest (unittest.TestCase):
    def testHelloWorld(self):
        self.assertTrue(True, "Hello would be written if not True")

if __name__ == "__main__":
    unittest.main()
    
