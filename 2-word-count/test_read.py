from unittest import TestCase
import read

class testRead(TestCase):
    def testWordStats(self):
        self.assertEqual(read.word_stats("article.txt", 15), [('the', 268), ('and', 143), ('to', 133), ('a', 120), ('of', 112), ('in', 90), ('that', 63), ('is', 56), ('for', 44), ('baker', 44)])
