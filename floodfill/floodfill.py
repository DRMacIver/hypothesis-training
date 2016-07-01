class Image(object):
    """A container class representing a two-dimensional 8-bit image"""

    def __init__(self, width, height, data=None):
        self.width = width
        self.height = height
        self.data = [0] * (width * height)
        if data is not None:
            for i, row in enumerate(data):
                for j, v in enumerate(row):
                    self[j, i] = v

    @property
    def size(self):
        return (self.width, self.height)

    @classmethod
    def from_data(cls, data):
        if not data:
            return Image(0, 0)
        else:
            return Image(len(data[0]), len(data), data)

    def to_data(self):
        return [
            [self[i, j] for i in range(self.width)]
            for j in range(self.height)
        ]

    def __getitem__(self, key):
        x, y = key
        return self.data[self.__index(x, y)]

    def __setitem__(self, key, value):
        if not (0 <= value < 256):
            raise ValueError('Colour out of range ')
        x, y = key
        self.data[self.__index(x, y)] = value

    def __index(self, x, y):
        if x < 0 or x >= self.width:
            raise IndexError('Index x out of range 0 <= %d < %d' % (
                x, self.width
            ))
        if y < 0 or y >= self.height:
            raise IndexError('Index x out of range 0 <= %d < %d' % (
                y, self.height
            ))
        return self.width * y + x

    def __eq__(self, other):
        return isinstance(other, Image) and self.to_data() == other.to_data()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "Image(%r, %r, %r)" % (
            self.width, self.height, self.to_data()
        )

    def copy(self):
        return Image(self.width, self.height, self.to_data())

def flood_fill(image, x, y, replace):
    """Set image[x, y] to colour replace, along with any pixels of the same
    colour that are connected to it."""
    xsize, ysize = image.size
    target_colour = image[x, y]
    queue = [(x, y)]
    while queue:
        i, j = queue.pop()
        if i < 0 or i >= xsize:
            continue
        if j < 0 or j >= xsize:
            continue
        if image[i, j] == target_colour:
            image[i, j] = replace
            queue.append((i - 1, j))
            queue.append((i + 1, j))
            queue.append((i, j - 1))
            queue.append((i, j + 1))
