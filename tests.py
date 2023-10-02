import os
import sys
import unittest
from main import main, ordenar, Demora

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
            Demora(123456789, 2),
            Demora(2, 20),
            Demora(42, 1),
            Demora(1024, 4),
        ]
        sol = [
            Demora(2, 20),
            Demora(1024, 4),
            Demora(123456789, 2),
            Demora(42, 1),
        ]
        self.assertEqual(ordenar(demoras), sol)


    def test_process_file(self):
        demoras = [
            Demora(123456789, 2),
            Demora(2, 20),
            Demora(42, 1),
            Demora(1024, 4),
        ]
        sol = [
            Demora(2, 20),
            Demora(1024, 4),
            Demora(123456789, 2),
            Demora(42, 1),
        ]
        expected_output = '\n'.join( map(str, sol) ) + '\n'

        input_filename = 'test_process_file_in.tmp'
        output_filename = 'test_process_file_out.tmp'
        with open(input_filename, 'w+') as input_file, \
            open(output_filename, 'w+') as output_file, \
            open('/dev/null', 'w+') as devnull:

            # write demoras to input file
            print('s,a', file=input_file)
            for demora in demoras:
                print(demora, file=input_file)
            input_file.seek(0)
            # run main which writes sorted list to stdout
            sys.stdin = input_file
            sys.stdout = output_file
            sys.stderr = devnull
            main()
            output_file.seek(0)
            self.assertEqual(output_file.read(), expected_output)
        os.remove(input_filename)
        os.remove(output_filename)
