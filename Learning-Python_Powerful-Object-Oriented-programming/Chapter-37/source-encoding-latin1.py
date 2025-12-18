myStr1 = 'AÄBèC'
myStr2 = 'A\xc4B\xe8C'
myStr3 = 'A\u00c4B\U000000e8C'
myStr4 = 'A' + chr(0xC4) + 'B' + chr(0xE8) + 'C'

import sys, locale
# print('Sys hosting platform: ', sys.platform)   # Sys hosting platform:  darwin
# print('Sys default encoding: ', sys.getdefaultencoding())   # Sys default encoding:  utf-8
# print('Open default encoding:', locale.getpreferredencoding(False))  # Open default encoding: UTF-8

for aStr in (myStr1, myStr2, myStr3, myStr4):
    # print(f'{aStr}, strlen={len(aStr)}', end=', ')  # AÄBèC, strlen=5, AÄBèC, strlen=5, AÄBèC, strlen=5, AÄBèC, strlen=5,
    bytes1 = aStr.encode()          # Default UTF-8
    bytes2 = aStr.encode('latin-1') # Explicit Latin-1
    print(f'byteslen1={len(bytes1)}, byteslen2={len(bytes2)}')  # byteslen1=7, byteslen2=5
                                                                # byteslen1=7, byteslen2=5
                                                                # byteslen1=7, byteslen2=5
                                                                # byteslen1=7, byteslen2=5