import math
from array import array


class Vector2D:
    """
    An example in FluentPython

    """

    type_code = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __len__(self):
        return

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.type_code)]) +
                bytes(array(self.type_code, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def angle(self):
        return math.atan2(self.x, self.y)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):  #  极坐标标识
            fmt_spec = fmt_spec[:-1]
            coord = (abs(self), self.angle())
            out_fmt = '<{}, {}>'
        else:
            coord = self
            out_fmt = '({}, {})'

        component = (format(c, fmt_spec)for c in coord)
        return out_fmt.format(*component)

    @classmethod
    def frombyte(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:].cast(typecode))
        return cls(*memv)


v1 = Vector2D(3, 4)
print('print(v1)', v1, format(v1, '0.4fp'), hash(v1), set([v1]))
x, y = v1
print('x:', x, 'y:', y)

v2 = Vector2D(3, 4)
print(v1 == v2, v1.__dict__)







