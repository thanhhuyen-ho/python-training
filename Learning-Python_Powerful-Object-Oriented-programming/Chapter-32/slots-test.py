import time

class SlotClass:
    __slots__ = ['x']

class DictClass:
    pass

N = 10_000_000

s = SlotClass()
d = DictClass()

t1 = time.time()
for i in range(N):
    s.x = i
print('Slots:', time.time() - t1)

t2 = time.time()
for i in range(N):
    d.x = i
print('Dict:', time.time() - t2)
