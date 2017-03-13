from is_sorted import is_sorted
from unittest import TestCase


class TestSorted(TestCase):
    def test_sorted(self):
        self.assertEquals(True, is_sorted([1, 2, 3]), "fail")
        self.assertEquals(True, is_sorted([1, 2, 2, 3, 3]), "fail")
        self.assertEquals(True, is_sorted([2, 2, 2, 2]), "fail")
        self.assertEquals(False, is_sorted([1, 4, 3]), "fail")
        self.assertEquals(True, is_sorted([]), "fail")