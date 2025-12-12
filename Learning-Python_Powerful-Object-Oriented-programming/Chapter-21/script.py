"""
Chapter 21: The Benchmarking Interlude
"""

print("\n=== Example 1: Simplistic timing function ===")    
import time

from sqlalchemy import func
def timer(func, *args):
    start = time.perf_counter()
    for i in range(100_000):
        func(*args)
    return time.perf_counter() - start



print("\n=== Example 2: Benchmarking Functions ===")
import time
timer = time.perf_counter
def once(func, *pargs, **kargs): 
    """
    Time to run func(...) once.
    Returns (elapsed-time, result).
    """
    start = timer()
    result = func(*pargs, **kargs)
    elapsed = timer() - start
    return elapsed, result

def total(reps, func, *pargs, **kargs):
    """
    Total time to run func(...) reps times. 
    Returns (total-time, last-result).
    """
    total = 0
    for i in range(reps):
        time, result = once(func, *pargs, **kargs)
        total += time
    return total, result

def bestof(reps, func, *pargs, **kargs):
    """
    Best time among reps runs of func(...).
    Returns (best-time, best-time-result).
    """
    return min(once(func, *pargs, **kargs) for i in range(reps))

def bestoftotal(reps1, reps2, func, *pargs, **kargs): 
    """
    Best total time among reps1 runs of [reps2 runs of func(...)]. 
    Returns (best-total-time, best-total-time-last-result).
    """
    return min(total(reps2, func, *pargs, **kargs) for i in range(reps1))


print("\n=== Example 3: Using the timer functions ===")
from timer_runner import runner 

repslist = list(range(10_000))

def F(x): return x

def forLoop(): 
    res = []
    for x in repslist: res.append(F(x))
    return res

def listComp():
    return [F(x) for x in repslist]

def mapCall():
    return list(map(F, repslist))

def genExpr():
    return list(F(x) for x in repslist)

def genFunc():
    def gen():
        for x in repslist: yield F(x)
        
    return list(gen())

runner(forLoop, listComp, mapCall, genExpr, genFunc)


print("\n=== Example 4: Function Gotchas ===")
def selector(): 
    global X    # Force X to be global (everywhere in function)
    print(X)
    X = 88
    
# selector()  # Outputs: NameError

X = 99
def selector():
    import __main__     # Import enclosing module
    print(__main__.X)   # Qualify to get to global version of name
    X = 88              # Unqualified X classified as local
    print(X)            # Prints local version of name
    
selector()
