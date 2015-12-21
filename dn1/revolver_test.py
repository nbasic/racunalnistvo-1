__author__ = 'Nino Bašić <nino.basic@fmf.uni-lj.si>'

import unittest
from revolver import Revolver


class RevolverTest(unittest.TestCase):

    def test_iter(self):
        r = Revolver([[1], [20, 10], [300, 200, 100]])
        self.assertIs(r, iter(r))

    def test_revolver_1(self):
        r = Revolver([[1], [20, 10], [300, 200, 100]])
        vrstni_red = [1, 10, 100, 20, 200, 300]
        for x in vrstni_red:
            self.assertEqual(x, next(r))
        with self.assertRaises(StopIteration):
            next(r)

    def test_revolver_2(self):
        r = Revolver([[1], [2], [3], [4], [5]])
        vrstni_red = [1, 2, 3, 4, 5]
        for x in vrstni_red:
            self.assertEqual(x, next(r))
        with self.assertRaises(StopIteration):
            next(r)

    def test_revolver_3(self):
        r = Revolver([[], [10, 20], [], [], []])
        vrstni_red = [20, 10]
        for x in vrstni_red:
            self.assertEqual(x, next(r))
        with self.assertRaises(StopIteration):
            next(r)

    def test_revolver_4(self):
        r = Revolver([[], [], [], [], []])
        with self.assertRaises(StopIteration):
            next(r)

    def test_revolver_5(self):
        r = Revolver([[10, 20, 30, 40, 50, 60, 70]])
        vrstni_red = [70, 60, 50, 40, 30, 20, 10]
        for x in vrstni_red:
            self.assertEqual(x, next(r))
        with self.assertRaises(StopIteration):
            next(r)

    def test_revolver_6(self):
        r = Revolver([[10, 20, 30], [], [400, 500, 600], [], [2000, 3000, 4000]])
        vrstni_red = [30, 600, 4000, 20, 500, 3000, 10, 400, 2000]
        for x in vrstni_red:
            self.assertEqual(x, next(r))
        with self.assertRaises(StopIteration):
            next(r)


if __name__ == '__main__':
    unittest.main()
