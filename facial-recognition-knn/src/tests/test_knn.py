import unittest
import numpy as np
from src.knn import findknn
from src.accuracy import accuracy

class KNNTest(unittest.TestCase):
    def test_findknn(self):
        # Your test cases here
        pass

class AccuracyTest(unittest.TestCase):
    def test_accuracy(self):
        # Your test cases here
        self.assertAlmostEqual(accuracy([1, 2, 1, 2], [1, 2, 1, 1]), 0.75)

if __name__ == '__main__':
    unittest.main()

