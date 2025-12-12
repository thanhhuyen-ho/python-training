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
