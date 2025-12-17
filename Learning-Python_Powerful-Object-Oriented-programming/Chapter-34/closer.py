class MyError(Exception):
    pass

def stuff(file):
    file.write('hello?')
    # raise MyError()

if __name__ == '__main__':
    file = open('temp.txt', 'w')
    try:
        stuff(file)
    finally:
        file.close()
    print('Am I Reached?')
    
# Output: Traceback (most recent call last):
#   File "closer.py", line 11, in <module>
#     stuff(file)
#   File "closer.py", line 6, in stuff
#     raise MyError()
# __main__.MyError
# (The file is properly closed despite the exception)

# When disable raise MyError(), output:
# Am I Reached? 
