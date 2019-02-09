import unittest
from overlap import isOverlapping

class TestsForOverLap(unittest.TestCase):

    def test_pos_true(self):
        result = isOverlapping((1, 4), (3, 6));
        self.assertEqual(result, True);

    def test_pos_false(self):
        result = isOverlapping((1, 5), (6, 11));
        self.assertEqual(result, False);

    def test_neg_true(self):
        result = isOverlapping((-1, -4), (-2, -6));
        self.assertEqual(result, True);

    def test_neg_false(self):
        result = isOverlapping((-1, -5), (-7, -10));
        self.assertEqual(result, False);

    def test_edging_false(self):
        result = isOverlapping((0, 1), (1, 2));
        self.assertEqual(result, False);

    def test_arbitrary_true(self):
        result = isOverlapping((-1, 2), (0, -2));
        self.assertEqual(result, True);

    def test_arbitrary_false(self):
        result = isOverlapping((-1, -3), (1, 3));
        self.assertEqual(result, False);
        
if __name__ == '__main__':
    unittest.main()