
class AbstractCollection(object):

    def __init__(self, sourceCollection = None):
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self._size += 3

    def __len__(self):
        return self._size

    def __lr__(self):
        return self._size


a = AbstractCollection([2, 3, 4])
# a = [2, 3, 4]
print(a.__len__())
