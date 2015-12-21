__author__ = 'Nino Bašić <nino.basic@fmf.uni-lj.si>'

import unittest
from jadrolinija import Trajekt, Vozilo, KolonaVozil


class TrajektTest(unittest.TestCase):

    def test_init(self):
        t = Trajekt(2000)
        self.assertEqual(t.stanje, 0)
        self.assertEqual(t.leva_kolona.max_dolzina, 2000)
        self.assertEqual(t.desna_kolona.max_dolzina, 2000)
        self.assertIsInstance(t.leva_kolona, KolonaVozil)
        self.assertIsInstance(t.desna_kolona, KolonaVozil)

    def test_vkrcaj_inspekcija(self):
        t = Trajekt(2000)
        vozila = [
            Vozilo('NM DK-34J', 425),
            Vozilo('LJ N6-03K', 445),
            Vozilo('KP JB-P20', 385),
            Vozilo('MB E8-Y2K', 490),
        ]
        with self.assertRaisesRegexp(ValueError, 'vhodna loputa je zaprta'):
            t.vkrcaj(vozila[0])

        t.stanje = 1  # "Na roke" popravimo stanje.
        for v in vozila:
            t.vkrcaj(v)

        self.assertEqual(t.leva_kolona.inspekcija(), ['NM DK-34J', 'KP JB-P20'])
        self.assertEqual(t.desna_kolona.inspekcija(), ['LJ N6-03K', 'MB E8-Y2K'])

    def test_vkrcaj_2(self):
        t = Trajekt(820)
        t.stanje = 1  # "Na roke" popravimo stanje.
        vozila = [
            Vozilo('NM DK-34J', 425),
            Vozilo('LJ N6-03K', 445),
            Vozilo('KP JB-P20', 385),
        ]
        for v in vozila:
            t.vkrcaj(v)
        with self.assertRaisesRegexp(ValueError, 'ni dovolj prostora'):
            t.vkrcaj(Vozilo('MB E8-Y2K', 490))

    def test_izkrcaj(self):
        t = Trajekt(1000)
        vozila = [
            Vozilo('NM DK-34J', 425),
            Vozilo('LJ N6-03K', 445),
            Vozilo('KP JB-P20', 385),
            Vozilo('MB E8-Y2K', 490),
        ]
        t.stanje = 1  # "Na roke" popravimo stanje.
        for v in vozila:
            t.vkrcaj(v)

        with self.assertRaisesRegexp(ValueError, 'izhodna loputa je zaprta'):
            t.izkrcaj()

    def test_izkrcaj_2(self):
        t = Trajekt(1000)
        vozila = [
            Vozilo('NM DK-34J', 425),
            Vozilo('LJ N6-03K', 445),
            Vozilo('KP JB-P20', 385),
            Vozilo('MB E8-Y2K', 490),
        ]
        t.stanje = 1  # "Na roke" popravimo stanje.
        for v in vozila:
            t.vkrcaj(v)

        t.stanje = -1  # "Na roke" popravimo stanje.
        self.assertIs(t.izkrcaj(), vozila[0])
        self.assertIs(t.izkrcaj(), vozila[1])
        self.assertIs(t.izkrcaj(), vozila[2])
        self.assertIs(t.izkrcaj(), vozila[3])

    def test_izkrcaj_3(self):
        t = Trajekt(1000)
        vozila = [
            Vozilo('LJ N6-03K', 445),
            Vozilo('KP JB-P20', 385),
            Vozilo('NM DK-34J', 425),
            Vozilo('MB E8-Y2K', 490),
        ]
        t.stanje = 1  # "Na roke" popravimo stanje.
        for v in vozila:
            t.vkrcaj(v)

        t.stanje = -1  # "Na roke" popravimo stanje.
        self.assertIs(t.izkrcaj(), vozila[0])
        self.assertIs(t.izkrcaj(), vozila[1])
        self.assertIs(t.izkrcaj(), vozila[2])
        self.assertIs(t.izkrcaj(), vozila[3])

    def test_dovolj_prostora(self):
        t = Trajekt(1000)
        vozila = [
            Vozilo('LJ N6-03K', 445),
            Vozilo('KP JB-P20', 385),
            Vozilo('NM DK-34J', 425),
        ]
        t.stanje = 1  # "Na roke" popravimo stanje.
        for v in vozila:
            t.vkrcaj(v)
        self.assertTrue(t.dovolj_prostora(Vozilo('MB E8-Y2K', 490)))

        t.vkrcaj(Vozilo('MB E8-Y2K', 490))
        self.assertFalse(t.dovolj_prostora(Vozilo('GO 3B-N6J', 285)))

    def test_izkrcaj_vse(self):
        t = Trajekt(1000)
        vozila = [
            Vozilo('LJ N6-03K', 445),
            Vozilo('KP JB-P20', 385),
            Vozilo('NM DK-34J', 425),
            Vozilo('MB E8-Y2K', 490),
        ]
        t.stanje = 1  # "Na roke" popravimo stanje.
        for v in vozila:
            t.vkrcaj(v)

        with self.assertRaisesRegexp(ValueError, 'izhodna loputa je zaprta'):
            t.izkrcaj_vse()

        t.stanje = -1  # "Na roke" popravimo stanje.
        self.assertEqual([v.tablica for v in t.izkrcaj_vse()],
                         ['LJ N6-03K', 'KP JB-P20', 'NM DK-34J', 'MB E8-Y2K'])

    def test_zacni_pokret(self):
        t = Trajekt(2000)
        self.assertEqual(t.stanje, 0)

        t.zacni_vkrcanje()
        self.assertEqual(t.stanje, 1)

        t.zacni_izkrcanje()
        self.assertEqual(t.stanje, -1)

        t.pokret()
        self.assertEqual(t.stanje, 0)

if __name__ == '__main__':
    unittest.main()
