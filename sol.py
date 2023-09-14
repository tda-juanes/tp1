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
        print("Ingresar en cada linea un entrenamiento con el formato 's,i', terminar lista con crln+d\n(la primer linea es ignorada)")
    try:
        sys.stdin.readline() # skip headers
        videos = [Demora(*map(int, line.split(','))) for line in sys.stdin]
        orden_optimo = ordenar(videos)
        if len(orden_optimo) > 100:
            print('El orden optimo es muy largo para mostrarlo completo, mostrando principio y final:')
            print('\n'.join( map(str, orden_optimo[:10]) ))
            print('...')
            print('\n'.join( map(str, orden_optimo[-10:]) ))
        else:
            print('Orden optimo:')
            print('\n'.join( map(str, orden_optimo) ))
        print(f'Tiempo optimo: {max_demora(orden_optimo)}')
    except TypeError:
        print('Invalid input: Expected 2 comma separated arguments per line', file=sys.stderr)
    except ValueError:
        print('Invalid input: Arguments must be valid integers', file=sys.stderr)


if __name__ == '__main__':
    main()
