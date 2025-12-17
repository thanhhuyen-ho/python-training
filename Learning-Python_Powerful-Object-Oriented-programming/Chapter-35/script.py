class FormatError(Exception):
    def __init__(self, line, file):
        self.line = line
        self.file = file
        
def parser(file):
    raise FormatError(62, file=file)

try:
    parser('code.py')
except FormatError as X:
    print(f"Error at {X.file} #{X.line}")
    
# Output: Error at code.py #62