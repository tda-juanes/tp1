from collections import namedtuple
import datetime as dt
import heapq

# type(Demora.*) = dt.timedelta
Demora = namedtuple("Demora", ['s', 'a'])

# overload comparison operators
Demora.__eq__ = lambda self, other: self.a == other.a
Demora.__ne__ = lambda self, other: self.a != other.a
Demora.__le__ = lambda self, other: self.a >= other.a
Demora.__ge__ = lambda self, other: self.a <= other.a
Demora.__lt__ = lambda self, other: self.a > other.a
Demora.__gt__ = lambda self, other: self.a < other.a


def ordenar(datos: list[Demora]):
    heapq.heapify(datos)
    return [heapq.heappop(datos) for i in range(len(datos))]


def max_demora(videos):
    total = m = dt.timedelta(0)
    for s, a in videos:
        total += s
        m = max(m, total + a)

    return m
