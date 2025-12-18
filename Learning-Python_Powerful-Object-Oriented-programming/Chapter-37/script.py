# Examples: Character Representations
print(ord('a')) # 97
print(chr(97))   # a
print(hex(97))  # 0x61
print(0b0111_1111)  # 127

print(chr(196)) # Ä
print(ord('Ä'))  # 196
print(hex(ord('Ä')))  # 0xc4
print(bin(ord('Ä')))  # 0b11000100   

print([f'{c} is {ord(c)} and {hex(ord(c))}' for c in 'aÄ '])    # ['a is 97 and 0x61', 'Ä is 196 and 0xc4', '  is 32 and 0x20']


# Examples: Character Encodings
print(len('a'.encode('ASCII')))  # 1
print(len('a'.encode('UTF-8')))  # 1
print(len('Ä'.encode('UTF-8'))) # 2

print('a'.encode('ASCII'))  # b'a'
print('a'.encode('UTF-8'))  # b'a'
print('a'.encode('Latin-1'))  # b'a'
print('Ä'.encode('UTF-8'))  # b'\xc3\x84'


# Examples: Literals and Basic Properties
B = b'code'
S = 'hack'
print(type(B), type(S))  # <class 'bytes'> <class 'str'>

print(B, S)  # b'code' hack
B2 = B"""
xxxx
yyyy
"""

print(B2)  # b'xxxx\nyyyy\n'
print(b'A\nB\rC', br'A\nB\rC', rb'A\nB\rC') # b'A\nB\rC' b'A\\nB\\rC' b'A\\nB\\rC'

print(B[0], S[0])  # 99 h
print(B[1:], S[1:])  # b'ode' ack
print(list(B), list(S))  # [99, 111, 100, 101] ['h', 'a', 'c', 'k']

# B[0] = 'x'  # TypeError: 'bytes' object does not support item assignment
# S[0] = 'x'  # TypeError: 'str' object does not support item assignment


# Examples: String Type Conversion
# 'hack' + b'code'  # TypeError: can only concatenate str (not "bytes") to str
S = 'hack'
print(S.encode())   # b'hack'
print(bytes(S, encoding='ascii'))   # b'hack'

B = b'code'
print(B.decode())   # code
print(str(B, encoding='ascii'))     # code

print(S.encode('ascii') + B)   # b'hackcode'
print(S + B.decode('ascii'))    # hackcode

# print(bytes(S))  # TypeError: string argument without an encoding
print(str(B))   #b'code'
print(len(str(B)))  # 7
print(len(str(B, encoding='ascii')))    # 4

import sys, locale
print(sys.platform)     # darwin
print(sys.getdefaultencoding())  # utf-8
print(locale.getpreferredencoding(False))   # UTF-8


# Examples: Coding Unicode Strings in Python
print(ord('X'))  # 88
print(chr(88))  # X
S = 'XYZ'   
print(len(S))   # 3

print(S.encode('ascii'))    # b'XYZ'
print(S.encode('latin-1'))  # b'XYZ'
print(S.encode('utf-8'))    # b'XYZ'


# UTF-16 and UTF-32 (with BOM)
print(S.encode('utf-16'))           # b'\xff\xfeX\x00Y\x00Z\x00'
print(S.encode('utf-32'))           # b'\xff\xfe\x00\x00X\x00\x00\x00...'

# Hex and Unicode Escapes
S = '\xc4\xe8'
print(S)                            # 'Äè'
S = '\u00c4\u00e8'
print(S)                            # 'Äè'
print(len(S))                       # 2

# Encoding non-ASCII
# S.encode('ascii')                 # UnicodeEncodeError
print(S.encode('latin-1'))          # b'\xc4\xe8'
print(S.encode('utf-8'))            # b'\xc3\x84\xc3\xa8'

# Manual Decoding
B = b'\xc4\xe8'
print(B.decode('latin-1'))          # 'Äè'
B = b'\xc3\x84\xc3\xa8'
print(B.decode('utf-8'))            # 'Äè'

# Mixing Unicodes
S = 'A\u00c4B\U000000e8C'
print(S)                            # 'AÄBèC'
print(S.encode('latin-1'))          # b'A\xc4B\xe8C'
print(S.encode('utf-8'))            # b'A\xc3\x84B\xc3\xa8C'
print(S.encode('cp500'))            # EBCDIC encoding example
print(S.encode('cp850'))            # DOS encoding example

# Bytes literals vs Str literals logic
# B = b'A\u00C4B\U000000E8C'        # SyntaxWarning (Unicode escapes don't work in bytes)
B = b'A\xC4B\xE8C'                  # Hex escapes work in bytes
print(B)                            # b'A\xc4B\xe8C'
print(B.decode('latin-1'))          # 'AÄBèC'

# "Converting" Encodings
S = 'AÄBèC'
T = S.encode('cp500')               # Convert to EBCDIC bytes
U = T.decode('cp500')               # Convert back to Unicode str
print(U.encode())                   # Back to UTF-8 bytes


# Examples: Using Byte Strings (Methods & Ops)
# Attributes comparison
print(sorted(set(dir('abc')) - set(dir(b'abc')))) # unique to str
print(sorted(set(dir(b'abc')) - set(dir('abc')))) # unique to bytes

B = b'code'
print(B.find(b'od'))                # 1
print(B.replace(b'od', b'XY'))      # b'cXYe'

# Sequence Ops
print(B[0])                         # 99
print(chr(B[0]))                    # 'c'
print(list(B))                      # [99, 111, 100, 101]
print(b'A\x42C\xFF\x63')            # b'ABC\xffc' (Mix of ASCII and hex)
print(B + b'lmn')                   # b'codelmn'
print(B * 4)                        # b'codecodecodecode'

# Formatting
print(b'a %s string' % b'fine')     # b'a fine string' (Only % works for bytes)
# b'a {} string'.format(b'fine')    # AttributeError
# f'a {kind} string'                # f-strings are str only


# Examples: Bytearray Objects
B = b'code'
C = bytearray(B)
print(C)                            # bytearray(b'code')
print(C[0])                         # 99

# Mutability
C[0] = ord('x')                     # Must assign integer
C[1] = b'Y'[0]                      # Assign integer from bytes
print(C)                            # bytearray(b'xYde')

# Methods
C.append(ord('M'))
C.extend(b'NO')
print(C)                            # bytearray(b'xYdeMNO')
print(C + b'!#')                    # bytearray(b'xYdeMNO!#')

# Other ways to make bytes
print(bytes([1, 2, 3, 4]))          # b'\x01\x02\x03\x04'
print(bytes('abc', 'ascii'))        # b'abc'
print(bytes(range(97, 100)))        # b'abc'



# Examples: Text and Binary Modes
open('temp.txt', 'w').write('abc\n')
open('temp.txt', 'r').read()
open('temp.txt', 'rb').read()

open('temp.bin', 'wb').write(b'abc\n')
open('temp.bin', 'r').read()
open('temp.bin', 'rb').read()

open('temp.bin', 'wb').write(b'a\x00c')
open('temp.bin', 'r').read()
open('temp.bin', 'rb').read()

BA = bytearray(b'\x01\x02\x03')
open('temp.bin', 'wb').write(BA)
open('temp.bin', 'r').read()
open('temp.bin', 'rb').read()

open('temp.txt', 'w').write('abc\n')
# open('temp.txt', 'w').write(b'abc\n')   # TypeError: write() argument must be str, not bytes
open('temp.bin', 'wb').write(b'abc\n')
# open('temp.bin', 'wb').write('abc\n')   # TypeError: write() argument must be str, not bytes


import os
import sys
import re
import struct
import pickle
import json
from unicodedata import normalize

# Examples: Basic text file writing and reading
file = open('temp.txt', 'w')
size = file.write('abc\n')   # Returns the number of characters written
file.close()

text = open('temp.txt').read()
print(f"Content read: {repr(text)}") # 'abc\n'

print("\n[Text vs Binary Mode Reading]")
open('temp.txt', 'w').write('abc\n')

print(f"Text mode read:   {repr(open('temp.txt', 'r').read())}")

print(f"Binary mode read: {open('temp.txt', 'rb').read()}")

print("\n[Binary File Writing]")
open('temp.bin', 'wb').write(b'abc\n')

print(f"Read bin as text: {repr(open('temp.bin', 'r').read())}")
print(f"Read bin as bin:  {open('temp.bin', 'rb').read()}")

print("\n[Null Bytes]")
open('temp.bin', 'wb').write(b'a\x00c')
print(f"Text mode with null: {repr(open('temp.bin', 'r').read())}")
print(f"Binary mode:         {open('temp.bin', 'rb').read()}")

print("\n[Bytearray]")
BA = bytearray(b'\x01\x02\x03')
open('temp.bin', 'wb').write(BA)
print(f"Read back: {open('temp.bin', 'rb').read()}")


# Examples: type mismatch errors
try:
    print("Trying to write bytes to text file...")
    open('temp.txt', 'w').write(b'abc\n')
except TypeError as e:
    print(f"Error caught: {e}")

try:
    print("Trying to write str to binary file...")
    open('temp.bin', 'wb').write('abc\n')
except TypeError as e:
    print(f"Error caught: {e}")


# Examples: UNICODE FILES (ENCODING) unicode files (encoding)
print("\n[UTF-8]")
file = open('uni.txt', 'w', encoding='utf8')
file.write(' 2 hÄck ')
file.close()

text = open('uni.txt', 'r', encoding='utf8').read()
print(f"Decoded text: {text}")
print(f"Code points:  {[ord(c) for c in text]}")

raw = open('uni.txt', 'rb').read()
print(f"Raw bytes:    {raw}")

print("\n[Encoding Errors]")
try:
    open('uni.txt', 'r', encoding='ascii').read()
except UnicodeDecodeError as e:
    print(f"ASCII Read Error: {e}")

try:
    open('ascii.txt', 'w', encoding='ascii').write(' 2 hÄck ')
except UnicodeEncodeError as e:
    print(f"ASCII Write Error: {e}")

print("\n[UTF-16]")
open('uni2.txt', 'w', encoding='utf16').write(' 2 hÄck ')
print(f"Read UTF-16: {open('uni2.txt', 'r', encoding='utf16').read()}")
print(f"Raw UTF-16:  {open('uni2.txt', 'rb').read()}")


# Examples: Other string tools
S = ' is the fastest way to !'
B = b'Python is the fastest way to pizza!'

match_str = re.match('(.*) the (.*) way (.*)', S).groups()
print(f"Str match:   {match_str}")

match_bytes = re.match(b'(.*) the (.*) way (.*)', B).groups()
print(f"Bytes match: {match_bytes}")


packed_data = struct.pack('>i4sh', 7, b'code', 8)
print(f"Packed:   {packed_data}")

unpacked_vals = struct.unpack('>i4sh', packed_data)
print(f"Unpacked: {unpacked_vals}")

data_list = ['code', 4, ' ']
print(f"Pickle dump: {pickle.dumps(data_list)}")

with open('temp.pkl', 'wb') as f:
    pickle.dump(data_list, f)

with open('temp.pkl', 'rb') as f:
    loaded_pickle = pickle.load(f)
print(f"Pickle load: {loaded_pickle}")

vals = ['code', {'app': (' ', None, 1.23, 99)}]

json_str = json.dumps(vals)
print(f"JSON string: {json_str}")

with open('data.json', 'w', encoding='utf8') as f:
    json.dump(vals, f)

with open('data.json', 'r', encoding='utf8') as f:
    loaded_json = json.load(f)
print(f"JSON load:   {loaded_json}")


# Examples: Filenames and the Filesystem
print(f"Filesystem encoding: {sys.getfilesystemencoding()}")
name1 = 'hÄck 1' # str

open(name1, 'w', encoding='utf8').write('text1')
print(f"Created file: {name1}")

print(f"os.listdir('.'):  {os.listdir('.')}")


# Examples: BOM (Byte Order Marker)
open('temp_nobom.txt', 'w', encoding='utf-8').write('code')
print(f"No BOM raw: {open('temp_nobom.txt', 'rb').read()}")

open('temp_bom.txt', 'w', encoding='utf-8-sig').write('code')
raw_bom = open('temp_bom.txt', 'rb').read()
print(f"With BOM raw: {raw_bom} (Note hex ef bb bf)")

print(f"Read 'utf-8':     {repr(open('temp_bom.txt', 'r', encoding='utf-8').read())}")

print(f"Read 'utf-8-sig': {repr(open('temp_bom.txt', 'r', encoding='utf-8-sig').read())}")


# Examples: Unicode Normalization
L = '\u00F1'          # NFC: ñ (composed form)
M = '\u006E\u0303'    # NFD: n + ~ (decomposed form)

print(f"Char L: {L}, Char M: {M}")
print(f"L == M? {L == M} (Different code points)")
print(f"Len L: {len(L)}, Len M: {len(M)}")

norm_L = normalize('NFC', L)
norm_M = normalize('NFC', M)
print(f"Normalized compare: {norm_L == norm_M}")


files_to_remove = [
    'temp.txt', 'temp.bin', 'uni.txt', 'uni2.txt', 
    'data.bin', 'temp.pkl', 'data.json', 'hÄck 1',
    'temp_nobom.txt', 'temp_bom.txt'
]
for f in files_to_remove:
    if os.path.exists(f):
        os.remove(f)
print("Cleanup complete.")