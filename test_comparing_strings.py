import unittest
import comparing_strings as cs


class TestComparingStrings(unittest.TestCase):
    def test_are_similar(self):
        self.assertTrue(cs.are_similar("abc", "ABC"))
        self.assertTrue(cs.are_similar("abc", "ABCd"))
        self.assertTrue(cs.are_similar("aBDc", "ABC"))
        self.assertTrue(cs.are_similar("abc", "ac"))
        self.assertFalse(cs.are_similar("abc", "def"))
        self.assertFalse(cs.are_similar("aBDc", "ABCe"))
        self.assertTrue(cs.are_similar("abcde", "ABC", max_edit_dist=2))
        self.assertTrue(cs.are_similar("abdec", "ABC", max_edit_dist=2))
        self.assertTrue(cs.are_similar("123", 123))

    def test_longest_subsequence(self):
        self.assertEqual(cs.longest_subsequence("ABAZDC", "BACBAD"), "ABAD")
        self.assertEqual(cs.longest_subsequence("AGGTAB", "GXTAYB"), "GTAB")
        self.assertEqual(cs.longest_subsequence("aaaa", "aa"), "aa")


if __name__ == '__main__':
    unittest.main()
