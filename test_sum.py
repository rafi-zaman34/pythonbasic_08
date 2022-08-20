#test case 1

import unittest

class unittest(unittest.TestCase):

    def test_sum_tc1(self):
        assert sum([1,1]) == 2, "Should be 2"


    def test_sum_tc2(self):
        assert sum([1,1,1]) == 3, "should be 2"

