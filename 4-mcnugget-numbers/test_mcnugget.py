from unittest import TestCase
#from file we're testing import function/class/whaterver

from mcNugget import solution

class TestNugget(TestCase):
    def test_solution(self):
        #assuming the correct output is [1,2,3,4,5,6,7,8,9,10]
        output = solution()
        self.assertEqual(output, [1,2,3,4,5,6,7,8,9,10])