class Set(list):
    def __init__(self, value=[]):
        list.__init__(self)
        for x in value:
            if x not in self:
                self.append(x)

    def intersect(self, other):
        return Set([x for x in self if x in other])

    def union(self, other):
        res = Set(self)
        for x in other:
            if x not in res:
                res.append(x)
        return res

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return f'Set({list(self)})'
