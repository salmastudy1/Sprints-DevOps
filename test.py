import sprints
import unittest

class TestSum(unittest.TestCase):
  
  def testFunc(self):
        average, maximum = sprints.MyFunc(4.8, 10,  11, 6, 13, 9.4)
        self.assertEqual(average, 8)
        self.assertEqual(maximum, 9.4)

  def testAllStrings(self):
        result1, result2 = sprints.MyFunc("string1" , "string2")
        self.assertEqual(result1, 0)
        self.assertEqual(result2, 0)
        
  def testNoEvenInt(self):
        result1, maximum = sprints.MyFunc(11, 10.2, 23, 30.1)
        self.assertEqual(result1, "No even integers")
        self.assertEqual(maximum, 30.1)      

  def testNoFloats(self):
        average, result1 = sprints.MyFunc(12, 14, 10)
        self.assertEqual(average, 12)
        self.assertEqual(result1, "No floats")    
  
  def testAllOddInt(self):
        result1, result2 = sprints.MyFunc(7, 31, 15)
        self.assertEqual(result1, "No even integers")
        self.assertEqual(result2, "No floats")
        
if __name__ == '__main__':
    unittest.main()
