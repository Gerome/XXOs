from unittest import TestCase
from NoughtCross import NoughtCross


class NoughtCrossTests(TestCase):

    def test_NoughtCrossShouldHoldItsType(self):
        nought = NoughtCross('O')
        cross = NoughtCross('X')

        self.assertEqual('O', nought.type)
        self.assertEqual('X', cross.type)

    def test_NoughtCrossShouldDisregardLetterCasing(self):
        nought = NoughtCross('o')
        cross = NoughtCross('x')

        self.assertEqual('O', nought.type)
        self.assertEqual('X', cross.type)

'''
Test List
-Z
-O
-M
-B
-I
-E


'''