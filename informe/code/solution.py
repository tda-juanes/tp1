from collections import namedtuple
import heapq

Demora = namedtuple("Demora", ['s', 'a'])
# overload comparison operators
Demora.__eq__ = lambda self, other: self.a == other.a
Demora.__ne__ = lambda self, other: self.a != other.a
Demora.__le__ = lambda self, other: self.a >= other.a
Demora.__ge__ = lambda self, other: self.a <= other.a
Demora.__lt__ = lambda self, other: self.a > other.a
Demora.__gt__ = lambda self, other: self.a < other.a

def ordenar(datos: list[Demora]):
    """ Requiere que (x < y) <=> (x.a > y.a) """
    heapq.heapify(datos)
    return [heapq.heappop(datos) for _ in range(len(datos))]
