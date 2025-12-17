import sys

def bye():
    sys.exit(62)

try:
    bye()
except:
    print('Got it')
    
print('Continuing...') 

# Output:
# Got it
# Continuing...