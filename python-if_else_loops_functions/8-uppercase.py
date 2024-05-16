#!/usr/bin/python3
def uppercase(str):
    result = ""
    for ch in str:
        if 96 < ord(ch) < 123:
            result += chr(ord(ch) - 32)
        else:
            result += ch
    print(result)
    print()
