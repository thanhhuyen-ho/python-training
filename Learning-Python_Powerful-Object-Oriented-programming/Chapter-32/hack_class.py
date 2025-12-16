class Hack:
    numInstances = 0

    def __init__(self):
        Hack.numInstances += 1

    def printNumInstances(cls):
        print('Number of instances:', cls.numInstances)

    printNumInstances = classmethod(printNumInstances)
