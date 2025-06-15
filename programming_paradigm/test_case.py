
import unittest
def sqrt(x):
    result = x*0.5
    return result

class Test_Sqrt(unittest.TestCase):
    def test_sqrt(self):
        result = (49)
        self.assertEqual(result, 7)
if __name__ == "__main__":
  unittest.main()


