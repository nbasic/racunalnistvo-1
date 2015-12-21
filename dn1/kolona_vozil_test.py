__author__ = 'Nino Bašić <nino.basic@fmf.uni-lj.si>'

import unittest
from jadrolinija import KolonaVozil, Vozilo


class KolonaVozilTest(unittest.TestCase):

    def test_init(self):
        kv = KolonaVozil(2000)
        self.assertEqual(kv.max_dolzina, 2000)
        self.assertEqual(kv.zasedenost, 0)

    def test_vkrcaj(self):
        kv = KolonaVozil(1000)

        vozilo1 = Vozilo('NM DK-34J', 425)
        kv.vkrcaj(vozilo1)
        self.assertEqual(kv.zasedenost, 425)

        vozilo2 = Vozilo('LJ N6-03K', 445)
        kv.vkrcaj(vozilo2)
        self.assertEqual(kv.zasedenost, 425 + 10 + 445)

        vozilo3 = Vozilo('KP JB-P20', 385)
        with self.assertRaisesRegexp(ValueError, 'ni dovolj prostora'):
            kv.vkrcaj(vozilo3)

    def test_izkrcaj(self):
        kv = KolonaVozil(1000)

        vozilo1 = Vozilo('NM DK-34J', 425)
        kv.vkrcaj(vozilo1)
        vozilo2 = Vozilo('LJ N6-03K', 445)
        kv.vkrcaj(vozilo2)

        self.assertIs(kv.izkrcaj(), vozilo1)
        self.assertEqual(kv.zasedenost, 425 + 10 + 445)

        with self.assertRaisesRegexp(ValueError, 'ni dovolj prostora'):
            kv.vkrcaj(vozilo1)

        self.assertIs(kv.izkrcaj(), vozilo2)
        self.assertEqual(kv.zasedenost, 0)

        with self.assertRaisesRegexp(ValueError, 'kolona je prazna'):
            kv.izkrcaj()



if __name__ == '__main__':
    unittest.main()
