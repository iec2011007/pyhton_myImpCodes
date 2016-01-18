import unittest
import numpy as np
from OneHotEncoding import *

class OneHotEncodingTestCases(unittest.TestCase):
    def test_encode(self):
        input1 = np.array([[0,1,1,2], [1,1,0,1]])
        out1 = np.array([[ 1., 0.,  1.,  1.,  0.,  1.,  0.], [ 0., 1.,  1.,  0.,  1.,  0.,  1.]])
        np.testing.assert_allclose(out1, OneHotEncoder().encode(input1))


if __name__ == '__main__':
    unittest.main()