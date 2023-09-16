import unittest
from main import ordenar, Demora

class TestOrdenarDemora(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(ordenar([]), [])


    def test_one(self):
        demoras = [Demora(5, 17)]
        self.assertEqual(ordenar(demoras[:]), demoras)


    def test_sorted(self):
        demoras = [
            Demora(2, 108),
            Demora(20, 23),
            Demora(1, 21),
            Demora(4, 17),
            Demora(100, 7),
            Demora(32, 3),
            Demora(5, 1),
        ]
        self.assertEqual(ordenar(demoras[:]), demoras)


    def test_dont_sort_scaloni(self):
        demoras = [
            Demora(2, 1),
            Demora(20, 1),
            Demora(1, 1),
            Demora(4, 1),
        ]
        self.assertEqual(ordenar(demoras[:]), demoras)


    def test_sort_ayudante(self):
        demoras = [
            Demora(1, 2),
            Demora(1, 20),
            Demora(1, 1),
            Demora(1, 4),
        ]
        sol = [
            Demora(1, 20),
            Demora(1, 4),
            Demora(1, 2),
            Demora(1, 1),
        ]
        self.assertEqual(ordenar(demoras), sol)


    def test_sort_ayudante_ignore_scaloni(self):
        demoras = [
            Demora(1e14, 2),
            Demora(2, 20),
            Demora(42, 1),
            Demora(1024, 4),
        ]
        sol = [
            Demora(2, 20),
            Demora(1024, 4),
            Demora(1e14, 2),
            Demora(42, 1),
        ]
        self.assertEqual(ordenar(demoras), sol)
