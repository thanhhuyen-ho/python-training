# ============================================================
# CHAPTER 10 — A QUICK EXAMPLE: INTERACTIVE LOOPS
# ============================================================


print("\n=== Simple Interactive Loop ===\n")

# Basic read/evaluate/print loop
while True:
    reply = input('Enter text:')
    if reply == 'stop': 
        break
    print(reply.upper())


print("\n=== Assignment Expression Version (Python 3.8+) ===\n")

# Same loop using := (walrus operator)
# Uncomment to run
# while (reply := input('Enter text:')) != 'stop':
#     print(reply.upper())


print("\n=== Doing Math on User Inputs ===\n")

# Squaring numbers entered by the user
while True:
    reply = input('Enter text:')
    if reply == 'stop':
        break
    print(int(reply) ** 2)
print('Bye')


print("\n=== Handling Errors by Testing Inputs (isdigit) ===\n")

# Prevent int() crash by checking isdigit
while True:
    reply = input('Enter text:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        print(int(reply) ** 2)
print('Bye')


print("\n=== Handling Errors with try/except ===\n")

# Handling conversion failures with try
while True:
    reply = input('Enter text:')
    if reply == 'stop':
        break
    try:
        num = int(reply)
    except:
        print('Bad!' * 8)
    else:
        print(num ** 2)
print('Bye')


print("\n=== More Compact try/except Version ===\n")

# Shorter version: convert inside try
while True:
    reply = input('Enter text:')
    if reply == 'stop':
        break
    try:
        print(int(reply) ** 2)
    except:
        print('Bad!' * 8)
print('Bye')


print("\n=== Supporting Floating-Point Numbers ===\n")

# Accept float inputs using try
while True:
    reply = input('Enter text:')
    if reply == 'stop':
        break
    try:
        print(float(reply) ** 2)
    except:
        print('Bad!' * 8)
print('Bye')


print("\n=== Nested Logic (Three Levels Deep) ===\n")

# Nested if inside loop and else
while True:
    reply = input('Enter text:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        num = int(reply)
        if num < 20:
            print('low')
        else:
            print(num ** 2)
print('Bye')
