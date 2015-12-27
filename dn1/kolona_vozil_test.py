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
        with self.assertRaisesRegex(ValueError, 'ni dovolj prostora'):
            kv.vkrcaj(vozilo3)

    def test_izkrcaj(self):
        kv = KolonaVozil(1000)

        vozilo1 = Vozilo('NM DK-34J', 425)
        kv.vkrcaj(vozilo1)
        vozilo2 = Vozilo('LJ N6-03K', 445)
        kv.vkrcaj(vozilo2)

        self.assertIs(kv.izkrcaj(), vozilo1)
        self.assertEqual(kv.zasedenost, 425 + 10 + 445)

        with self.assertRaisesRegex(ValueError, 'ni dovolj prostora'):
            kv.vkrcaj(vozilo1)

        self.assertIs(kv.izkrcaj(), vozilo2)
        self.assertEqual(kv.zasedenost, 0)

        with self.assertRaisesRegex(ValueError, 'kolona je prazna'):
            kv.izkrcaj()

    def test_dovolj_prostora(self):
        kv = KolonaVozil(1000)

        vozilo1 = Vozilo('NM DK-34J', 425)
        self.assertTrue(kv.dovolj_prostora(vozilo1))
        kv.vkrcaj(vozilo1)

        vozilo2 = Vozilo('LJ N6-03K', 445)
        self.assertTrue(kv.dovolj_prostora(vozilo2))
        kv.vkrcaj(vozilo2)

        vozilo3 = Vozilo('KP JB-P20', 385)
        self.assertFalse(kv.dovolj_prostora(vozilo3))

    def test_inspekcija(self):
        kv = KolonaVozil(1500)
        self.assertEqual(kv.inspekcija(), [])

        kv.vkrcaj(Vozilo('NM DK-34J', 425))
        self.assertEqual(kv.inspekcija(), ['NM DK-34J'])

        kv.vkrcaj(Vozilo('LJ N6-03K', 445))
        kv.vkrcaj(Vozilo('KP JB-P20', 385))
        self.assertEqual(kv.inspekcija(), ['NM DK-34J', 'LJ N6-03K', 'KP JB-P20'])


if __name__ == '__main__':
    unittest.main()
