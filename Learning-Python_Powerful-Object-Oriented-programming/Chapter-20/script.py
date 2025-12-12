"""
Chapter 20: Comprehensions and Generations
"""

print("\n=== Example 1: Basic List Comprehensions ===")
# Manual results collection
res = []
for x in 'text':
    res.append(ord(x))

# Apply function to iterable
res = list(map(ord, 'text'))

# List comprehension
res = [ord(x) for x in 'text']
print(res)


print("\n=== Example 2: List Comprehensions and Matrixes ===")
M = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]
N = [[2, 2, 2], 
     [3, 3, 3], 
     [4, 4, 4]]

print(M[1])        # Outputs: [4, 5, 6]
print(M[1][2])    # Outputs: 6
print([row[1] for row in M])  # Outputs: [2, 5, 8]
print([M[row][1] for row in (0, 1, 2)])  # Outputs: [2, 5, 8]


print("\n=== Example 3: Generator Functions and Expressions ===")
def both(N):
    for i in range(N): yield i
    for i in map(lambda x: x ** 2, range(N)): yield i
    
print(list(both(5)))  # Outputs: [0, 1, 2, 3, 4, 0, 1, 4, 9, 16]

line = 'aa bbb c'
print(''.join(map(str.upper, filter(lambda x: len(x) > 1, line.split()))))  # Outputs: 'AABBB'


print("\n=== Example 4: Scrambling Sequences ===")
L, S = [1, 2, 3], 'code'

for i in range(len(S)):
    S = S[1:] + S[:1]
    print(S, end=' ')   # Outputs: odec deco ecod code

for i in range(len(L)):
    L = L[1:] + L[:1]
    print(L, end=' ')   # Outputs: [2, 3, 1] [3, 1, 2] [1, 2, 3]
    

print("\n\n=== Example 5: mymap-lists ===")
def mymap(func, *seqs): 
    res = []
    for args in zip(*seqs): 
        res.append(func(*args))
    return res

print(mymap(abs, [-2, -1, 0, 1, 2]))
print(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))


print("\n=== Example 6: Emulating zip and map ===")
zip([1,2],[3,4]) #Outputs: (1,3), (2,4)
map(pow, [1,2,3], [2,3,4]) #Outputs: 1,8,81


print("\n=== Example 7: Using * to Unpack Argument Lists ===")
import time, asyncio 
def now():
    return time.strftime('[%H:%M:%S]') # Local time, as hour:minute:second

async def producer(label):  # await requires async
    await asyncio.sleep(2)  # Call nonblocking/awaitable sleep
    return f'All done, {label}, {now()}'  # Result of await expression

async def main():
    print('Start =>', now())
    task1 = asyncio.create_task(producer(f'async task 1'))
    task2 = asyncio.create_task(producer(f'async task 2'))
    task3 = asyncio.create_task(producer(f'async task 3'))
    print(await task1)
    print(await task2)

asyncio.run(main())





