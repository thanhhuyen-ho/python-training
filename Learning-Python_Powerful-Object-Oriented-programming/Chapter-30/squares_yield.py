class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2

S = Squares(1, 3)
for i in S:
    for j in S:
        print(f'{i}:{j}', end=' ')
# 1:1 1:4 1:9 2:1 2:4 2:9 3:1 3:4 3:9