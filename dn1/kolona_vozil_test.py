__author__ = 'Nino Bašić <nino.basic@fmf.uni-lj.si>'

import unittest
from jadrolinija import KolonaVozil


class KolonaVozilTest(unittest.TestCase):

    def test_init(self):
        kv = KolonaVozil(2000)
        self.assertEqual(kv.max_dolzina, 2000)
        self.assertEqual(kv.zasedenost, 0)


if __name__ == '__main__':
    unittest.main()
