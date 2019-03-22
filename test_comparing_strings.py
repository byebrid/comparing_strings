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


if __name__ == '__main__':
    unittest.main()
