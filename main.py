from collections import namedtuple
import heapq
import sys


# type(Demora.*) = int
Demora = namedtuple("Demora", ['s', 'a'])
Demora.__repr__ = lambda self: f'{self.s},{self.a}'

# overload comparison operators
Demora.__eq__ = lambda self, other: self.a == other.a
Demora.__ne__ = lambda self, other: self.a != other.a
Demora.__le__ = lambda self, other: self.a >= other.a
Demora.__ge__ = lambda self, other: self.a <= other.a
Demora.__lt__ = lambda self, other: self.a > other.a
Demora.__gt__ = lambda self, other: self.a < other.a


def ordenar(datos: list[Demora]):
    heapq.heapify(datos)
    return [heapq.heappop(datos) for _ in range(len(datos))]


def max_demora(videos):
    total = m = 0
    for s, a in videos:
        total += s
        m = max(m, total + a)

    return m


def main():
    if sys.stdin.isatty():
        print("Ingresar un entrenamiento por linea con el formato 's,a'", file=sys.stderr)
    else:
        sys.stdin.readline() # skip headers

    try:
        videos = [Demora(*map(int, line.split(','))) for line in sys.stdin]
        orden_optimo = ordenar(videos)
    except TypeError:
        print('Invalid input: Expected 2 comma separated arguments per line', file=sys.stderr)
    except ValueError:
        print('Invalid input: Arguments must be valid integers', file=sys.stderr)
    else:
        print('\n'.join( map(str, orden_optimo) ))
        print(f'Tiempo optimo: {max_demora(orden_optimo)}', file=sys.stderr)


if __name__ == '__main__':
    main()
