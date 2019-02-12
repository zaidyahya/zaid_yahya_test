import unittest
from comparator import VersionComparator


class TestsForStrings(unittest.TestCase):

    # -------------------TEST compare-------------------------
    def test1_Forcompare(self):
        strings = VersionComparator('1.3.2', '1.3.1')
        self.assertEqual(strings.compare(), '1.3.2 is greater than 1.3.1')

    def test2_Forcompare(self):
        strings = VersionComparator('-1.2.1', '-1.3.1')
        self.assertNotEqual(strings.compare(), '-1.2.1 is greater than -1.3.1')

    # -------------------TEST Lesser-------------------------
    def test1_ForLesser(self):
        strings = VersionComparator('1.0', '1.3.1')
        self.assertEqual(strings.compare(), '1.0 is lesser than 1.3.1')

    def test2_ForLesser(self):
        strings = VersionComparator('-1.3.1.1', '-1.2.5.8')
        self.assertNotEqual(strings.compare(), '-1.3.1.1 is lesser than -1.2.5.8')

    # ------------TEST Equal---------------------------------
    def test1_ForEqual(self):
        strings = VersionComparator('1.0', '2.3')
        self.assertEqual(strings.compare(), '1.0 is lesser than 2.3')

    def test2_ForEqual(self):
        strings = VersionComparator('1.1.3', '1.1.3')
        self.assertEqual(strings.compare(), '1.1.3 is equal to 1.1.3')

if __name__ == '__main__':
    unittest.main()
