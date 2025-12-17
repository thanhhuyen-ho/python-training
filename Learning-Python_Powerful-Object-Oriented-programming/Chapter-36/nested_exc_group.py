def action3():
    raise ExceptionGroup('Nest*', [IndexError(1), TypeError(2), SyntaxError(3)])

def action2(): 
    try:
        action3()
    except* IndexError:
        print('Got IE')
        
def action1(): 
    try:
        action2()
    except* TypeError:
        print('Got TE')
        
if __name__ == '__main__': action1()

# Output:
# Got IE
# Got TE
# + Exception Group Traceback (most recent call last): ...etc...
# | ExceptionGroup: Nest* (1 sub-exception) 
# +-+---------------- 1 ----------------
#  | SyntaxError: 3 
#  +------------------------------------