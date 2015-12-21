__author__ = 'nino'

import unittest
from jadrolinija import Vozilo


class VoziloTest(unittest.TestCase):

    def test_something(self):
        v = Vozilo('NM DK-34J', 425)
        self.assertEqual(v.tablica, 'NM DK-34J')
        self.assertEqual(v.dolzina, 425)


if __name__ == '__main__':
    unittest.main()
