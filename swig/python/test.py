#!/usr/bin/env python

import string, unittest

from _distance import *

class DistanceTest(unittest.TestCase):
    """A simple and incomplete test case for the distance functions"""

    def testLD(self):
        str1 = "hello my name is jose"
        str2 = "hello m yname is jose"
        str3 = "hlelo my name is jose"

        self.assertEquals(levenshtein_d(str1, len(str1), str2, len(str2)), 2)
        self.assertEquals(levenshtein_d(str1, len(str1), str3, len(str3)), 2)

    def testHD(self):
        str1 = "hello my name is jose"
        str2 = "hello m yname is jose"
        str3 = "hlelo my name is jose"
        self.assertEquals(hamming_d(str1, len(str1), str2, len(str2)), 2)
        self.assertEquals(hamming_d(str1, len(str1), str3, len(str3)), 2)

    def testDD(self):
        str1 = "hello my name is jose"
        str2 = "hello m yname is jose"
        str3 = "hlelo my name is jose"
        self.assertEquals(damerau_d(str1, len(str1), str2, len(str2)), 0)
        self.assertEquals(damerau_d(str1, len(str1), str3, len(str3)), 0)


if __name__ == '__main__':
    # When this module is executed from the command-line, run all its tests
    unittest.main()
