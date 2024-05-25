#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_string = roman_string.upper()
    roman_num = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    prev = 0
    for symbol in reversed(roman_string):
        value = roman_num[symbol]
        if value >= prev:
            result += value
            prev = value
        else:
            result -= value
            prev = value
    return result
