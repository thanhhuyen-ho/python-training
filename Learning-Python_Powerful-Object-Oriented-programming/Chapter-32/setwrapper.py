class Set:
    def __init__(self, value=[]):
        self.data = []
        for x in value:
            self.add(x)

    def intersect(self, other):
        res = []
        for x in self.data:
            if x in other.data:
                res.append(x)
        return Set(res)

    def union(self, other):
        res = self.data[:]
        for x in other.data:
            if x not in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        res = self.data[:]
        for x in value:
            if x not in res:
                res.append(x)
        return Set(res)

    def add(self, value):
        if value not in self.data:
            self.data.append(value)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return f'Set({self.data})'
