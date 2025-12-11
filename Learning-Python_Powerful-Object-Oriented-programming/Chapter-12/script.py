# -----------------------------------------
# Chapter 12 — if and match Selections
# -----------------------------------------

print("=== Basic if ===")
if 1:
    print('true')

if not 1:
    print('true')
else:
    print('false')

print("\n=== if / elif / else ===")
os, mode = 'Windows', 'mobile'

if os in ['iOS', 'iPhoneOS']:
    print('macOS')
elif mode == 'mobile' and os != 'Windows':
    print('Linux')
else:
    print('unknown?')

print("\n=== Nested if ===")
os, mode = 'Android', 'mobile'

if mode == 'mobile':
    if os == 'Android':
        print('Linux')
    elif os != 'Windows':
        print('macOS')

print("\n=== Dictionary-based multiple choice ===")
choice = 'Windows'
print({'macos': 2001, 'Linux': 1991, 'Windows': 1985}[choice])

print("\n=== Equivalent if ===")
if choice == 'macos':
    print(2001)
elif choice == 'Linux':
    print(1991)
elif choice == 'Windows':
    print(1985)
else:
    print('Bad choice')

print("\n=== dict.get default ===")
branch = dict(macos=2001, Linux=1991, Windows=1985)
print(branch.get('Windows', 'Bad choice'))
print(branch.get('Solaris', 'Bad choice'))

print("\n=== default with 'in' ===")
choice = 'AmigaOS'
if choice in branch:
    print(branch[choice])
else:
    print('Bad choice')

print("\n=== default with try/except ===")
choice = 'GEM'
try:
    print(branch[choice])
except KeyError:
    print('Bad choice')

print("\n=== Callable dictionary (jump table) ===")
def action():
    print("iOS action")

def default():
    print("default action")

branch = {
    'Android': lambda: print("Android action"),
    'iOS': action,
    'Symbian OS': lambda: print("Symbian action"),
}

choice = 'Android'
branch.get(choice, default)()

# -----------------------------------------
# MATCH STATEMENT EXAMPLES
# -----------------------------------------

print("\n=== Basic match ===")
state = 'go'

match state:
    case 'go':
        print('green')
    case 'stop':
        print('red')
    case _:
        print('yellow')

print("\n=== match with OR, as, variable ===")
state = 'halt'

match state:
    case 'go' | 'proceed' | 'start':
        print('green')
        print('means go')
    case 'stop' | 'halt' as what:
        print('red')
        print('means', what)
    case other:
        print('catchall', other)

print("\n=== match assigning variables ===")
for stmt in ['if', 'while', 'try']:
    match stmt:
        case 'if' | 'match':
            print('logic')
        case 'for' | 'while' as which:
            print('loop')
        case other:
            print('tbd')

print("which =", which)
print("other =", other)

print("\n=== Advanced structural match patterns ===")
# Example 12-1 condensed so it can run for any state value
test_states = [
    1,
    [1, 2, 3],
    [0, 2, 3],
    (1, 2, 3),
    (0, 2, 3),
    dict(a=1, b=2, c=3),
    dict(a=0, b=2, c=3),
    "other"
]

for state in test_states:
    match state:
        case 1 | 2 | 3 as what:
            print("or", what)

        case [1, 2, what]:
            print("list1", what)

        case [0, *what]:
            print("list2", what)

        case {'a': 1, 'b': 2, 'c': what}:
            print("dict1", what)

        case {'a': 0, **what}:
            print("dict2", what)

        case (1, 2, what):
            print("tuple1", what)

        case (0, *what):
            print("tuple2", what)

        case _ as what:
            print("other", what)

print("\n=== Attribute / instance patterns preview ===")

class Emp:
    def __init__(self, name):
        self.name = name

pat = Emp("Pat")
state = pat

match state:
    case pat.name as what:
        print("attr", what)
    case Emp(name=what):
        print("instance", what)

print("\n=== match with guards (if) ===")
state = ((1, 2), 3)
guard1 = True

match state:
    case ((a, 2), b) if guard1:
        print("case1", a, b)
    case (a, 3) as what:
        print("case2", a, what)
    case [a, (3 | 4)] as what if guard1:
        print("case3", a, what)
