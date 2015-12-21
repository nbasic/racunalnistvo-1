__author__ = 'Nino Bašić <nino.basic@fmf.uni-lj.si>'

import unittest
from verizni_seznam import VerizniSeznamPlus, Vozel


class VerizniSeznamPlusTest(unittest.TestCase):

    def test_init(self):
        s = VerizniSeznamPlus()
        self.assertIsNone(s.zacetek)
        self.assertIsNone(s.konec)

    def test_vstavi_na_konec(self):
        s = VerizniSeznamPlus()
        s.vstavi_na_konec('banana')
        self.assertIsNotNone(s.zacetek)
        self.assertEqual(s.zacetek, s.konec)
        self.assertIsInstance(s.zacetek, Vozel)
        self.assertEqual(s.zacetek.podatek, 'banana')
        self.assertIsNone(s.zacetek.naslednji)
        self.assertIsNone(s.zacetek.prejsnji)

    def test_vstavi_na_konec_2(self):
        s = VerizniSeznamPlus()
        s.vstavi_na_konec('banana')
        s.vstavi_na_konec('jabolko')
        self.assertIsNotNone(s.konec)
        self.assertIsNotNone(s.zacetek)
        self.assertIsInstance(s.zacetek, Vozel)
        self.assertIsInstance(s.konec, Vozel)
        self.assertEqual(s.zacetek.naslednji, s.konec)
        self.assertEqual(s.zacetek, s.konec.prejsnji)
        self.assertIsNone(s.zacetek.prejsnji)
        self.assertIsNone(s.konec.naslednji)
        self.assertEqual(s.zacetek.podatek, 'banana')
        self.assertEqual(s.konec.podatek, 'jabolko')

    def test_vstavi_na_konec_3(self):
        s = VerizniSeznamPlus()
        sadje = ['banana', 'jabolko', 'pomaranča', 'limona', 'kivi', 'hruška', 'kokos']
        s.vstavi_na_konec(sadje[0])
        prev_konec = s.konec
        for i in range(1, len(sadje)):
            s.vstavi_na_konec(sadje[i])
            self.assertIsNone(s.konec.naslednji)
            self.assertEqual(s.konec.prejsnji, prev_konec)
            self.assertEqual(s.konec.prejsnji.podatek, sadje[i-1])
            self.assertEqual(s.konec.podatek, sadje[i])
            prev_konec = s.konec

    def test_init_iter(self):
        sadje = ['banana', 'jabolko', 'pomaranča', 'limona', 'kivi', 'hruška', 'kokos']
        s = VerizniSeznamPlus(sadje[:])
        for x, correct in zip(s, sadje):
            self.assertEqual(x, correct)

    def test_vstavi_na_zacetek(self):
        s = VerizniSeznamPlus()
        s.vstavi_na_zacetek('banana')
        self.assertIsNotNone(s.zacetek)
        self.assertEqual(s.zacetek, s.konec)
        self.assertIsInstance(s.zacetek, Vozel)
        self.assertEqual(s.zacetek.podatek, 'banana')
        self.assertIsNone(s.zacetek.naslednji)
        self.assertIsNone(s.zacetek.prejsnji)

    def test_vstavi_na_zacetek_2(self):
        s = VerizniSeznamPlus()
        s.vstavi_na_zacetek('banana')
        s.vstavi_na_zacetek('jabolko')
        self.assertIsNotNone(s.konec)
        self.assertIsNotNone(s.zacetek)
        self.assertIsInstance(s.zacetek, Vozel)
        self.assertIsInstance(s.konec, Vozel)
        self.assertEqual(s.zacetek.naslednji, s.konec)
        self.assertEqual(s.zacetek, s.konec.prejsnji)
        self.assertIsNone(s.zacetek.prejsnji)
        self.assertIsNone(s.konec.naslednji)
        self.assertEqual(s.zacetek.podatek, 'jabolko')
        self.assertEqual(s.konec.podatek, 'banana')

    def test_vstavi_na_zacetek_3(self):
        s = VerizniSeznamPlus()
        sadje = ['banana', 'jabolko', 'pomaranča', 'limona', 'kivi', 'hruška', 'kokos']
        s.vstavi_na_zacetek(sadje[0])
        prev_zacetek = s.zacetek
        for i in range(1, len(sadje)):
            s.vstavi_na_zacetek(sadje[i])
            self.assertIsNone(s.zacetek.prejsnji)
            self.assertEqual(s.zacetek.naslednji, prev_zacetek)
            self.assertEqual(s.zacetek.naslednji.podatek, sadje[i-1])
            self.assertEqual(s.zacetek.podatek, sadje[i])
            prev_zacetek = s.zacetek

        for x, correct in zip(s, reversed(sadje)):
            self.assertEqual(x, correct)

    def test_podatek_na_zaceteku(self):
        s = VerizniSeznamPlus()
        s.vstavi_na_zacetek('hruška')
        self.assertEqual(s.podatek_na_zacetku(), 'hruška')
        s.vstavi_na_konec('limona')
        self.assertEqual(s.podatek_na_zacetku(), 'hruška')
        s.vstavi_na_zacetek('kokos')
        self.assertEqual(s.podatek_na_zacetku(), 'kokos')
        s.vstavi_na_konec('pomaranča')
        self.assertEqual(s.podatek_na_zacetku(), 'kokos')

    def test_podatek_na_zacetku_2(self):
        s = VerizniSeznamPlus()
        with self.assertRaisesRegexp(IndexError, 'verižni seznam je prazen'):
            s.podatek_na_zacetku()

    def test_podatek_na_koncu(self):
        s = VerizniSeznamPlus()
        s.vstavi_na_konec('hruška')
        self.assertEqual(s.podatek_na_koncu(), 'hruška')
        s.vstavi_na_zacetek('limona')
        self.assertEqual(s.podatek_na_koncu(), 'hruška')
        s.vstavi_na_konec('kokos')
        self.assertEqual(s.podatek_na_koncu(), 'kokos')
        s.vstavi_na_zacetek('pomaranča')
        self.assertEqual(s.podatek_na_koncu(), 'kokos')

    def test_podatek_na_koncu_2(self):
        s = VerizniSeznamPlus()
        with self.assertRaisesRegexp(IndexError, 'verižni seznam je prazen'):
            s.podatek_na_koncu()

    def test_je_prazen(self):
        s = VerizniSeznamPlus()
        self.assertTrue(s.je_prazen())
        s.vstavi_na_konec('hruška')
        self.assertFalse(s.je_prazen())

    def test_sprazni(self):
        sadje = ['banana', 'jabolko', 'pomaranča', 'limona', 'kivi', 'hruška', 'kokos']
        s = VerizniSeznamPlus(sadje[:])
        self.assertFalse(s.je_prazen())
        s.sprazni()
        self.assertTrue(s.je_prazen())
        self.assertIsNone(s.zacetek)
        self.assertIsNone(s.konec)

    def test_je_prazen_2(self):
        s = VerizniSeznamPlus()
        self.assertTrue(s.je_prazen())
        s.vstavi_na_konec('hruška')
        self.assertFalse(s.je_prazen())
        s.zbrisi_konec()
        self.assertTrue(s.je_prazen())
        s.vstavi_na_konec('banana')
        self.assertFalse(s.je_prazen())

    def test_zbrisi_konec(self):
        s = VerizniSeznamPlus()
        s.vstavi_na_konec('banana')
        s.zbrisi_konec()
        self.assertTrue(s.je_prazen())
        self.assertIsNone(s.zacetek)
        self.assertIsNone(s.konec)

    def test_zbrisi_konec_2(self):
        s = VerizniSeznamPlus()
        s.vstavi_na_konec('banana')
        s.vstavi_na_konec('hruška')
        s.zbrisi_konec()
        self.assertFalse(s.je_prazen())
        self.assertIs(s.zacetek, s.konec)
        self.assertEqual(s.zacetek.podatek, 'banana')

    def test_zbrisi_konec_3(self):
        sadje = ['banana', 'jabolko', 'pomaranča', 'limona', 'kivi', 'hruška', 'kokos']
        s = VerizniSeznamPlus(sadje[:])
        while sadje:
            self.assertEqual(s.podatek_na_koncu(), sadje[-1])
            s.zbrisi_konec()
            del sadje[-1]
        self.assertTrue(s.je_prazen())

    def test_zbrisi_zacetek(self):
        s = VerizniSeznamPlus()
        s.vstavi_na_zacetek('jabolko')
        s.zbrisi_zacetek()
        self.assertTrue(s.je_prazen())
        self.assertIsNone(s.zacetek)
        self.assertIsNone(s.konec)

    def test_zbrisi_zacetek_2(self):
        s = VerizniSeznamPlus()
        s.vstavi_na_zacetek('banana')
        s.vstavi_na_zacetek('hruška')
        s.zbrisi_zacetek()
        self.assertFalse(s.je_prazen())
        self.assertIs(s.zacetek, s.konec)
        self.assertEqual(s.zacetek.podatek, 'banana')

    def test_zbrisi_zacetek_3(self):
        sadje = ['banana', 'jabolko', 'pomaranča', 'limona', 'kivi', 'hruška', 'kokos']
        s = VerizniSeznamPlus(sadje[:])
        while sadje:
            self.assertEqual(s.podatek_na_zacetku(), sadje[0])
            s.zbrisi_zacetek()
            del sadje[0]
        self.assertTrue(s.je_prazen())


if __name__ == '__main__':
    unittest.main()
