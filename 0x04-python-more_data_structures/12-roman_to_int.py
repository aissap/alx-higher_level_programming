#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    rom_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    prev_value = 0

    for i in roman_string[::-1]:
        if rom_values[i] >= prev_value:
            result += rom_values[i]
        else:
            result -= rom_values[i]
        prev_value = rom_values[i]

    return result
