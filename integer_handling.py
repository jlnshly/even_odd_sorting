class IntegerHandling:
    #Class for handling raw even and odd integers

    def __int__(self, raw_integers: list):
        self._integers = []
        self.integers = raw_integers

    def integers(self):
        return self._integers

    def integer(self, value):
        sorted_integers = sorted(list(set([int(x) for x in value])))
        self._integers = sorted_integers

    def filter_parity_integers(self, parity: str = "even"): -> list[int]:
        remainder = 0 if parity == "even" else 1
        return [n for n ]

