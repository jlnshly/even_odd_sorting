class IntegerHandling:
    """Class for handling raw even and odd integers"""

    def __init__(self, raw_integers: list):
        self._integers = []
        self.integers = raw_integers

    @property
    def integers(self):
        """Returns list of integers"""
        return self._integers

    @integers.setter
    def integers(self, value):
        """Sets list of integers"""
        sorted_integers = sorted(list(set([int(x) for x in value])))
        self._integers = sorted_integers

    def filter_using_parity(self, parity: str="even"):
        """Filtering even and odd integers by parity"""
        remainder = 0 if parity == "even" else 1
        return [i for i in self._integers if i % 2 == remainder]

