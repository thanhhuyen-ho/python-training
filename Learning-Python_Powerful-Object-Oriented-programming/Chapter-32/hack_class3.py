class Hack:
    numInstances = 0

    def count(cls):
        cls.numInstances += 1

    count = classmethod(count)

    def __init__(self):
        self.count()

class Sub(Hack):
    numInstances = 0


class Other(Hack):
    numInstances = 0
