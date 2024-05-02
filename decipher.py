"""
Author: Nicholas Young
Date: 2024-04-30
Class: Comp 340-002
"""
import re

def translate_baby_language(baby_string):
    translation_key = {
        'pee': '+',
        'gah': '-',
        'milk': '*',
        'heh': '/',
        'mama': '(',
        'dada': ')',
        'b': '0',
        'ba': '1',
        'baa': '2',
        'baaa': '3',
        'baaaa': '4',
        'baaaaa': '5',
        'baaaaaa': '6',
        'baaaaaaa': '7',
        'baaaaaaaa': '8',
        'baaaaaaaaa': '9'
    }

    # Clean the string
    baby_string = re.sub(r'\s', '', baby_string)

    # Add an end marker
    baby_string += 'X'

    current_word = ''
    equation = ''
    next_char = ''
    for i in range(len(baby_string)):
        if baby_string[i] == 'X':
            break
        current_word += baby_string[i]
        next_char = baby_string[i+1]
        if current_word[0] == 'b' and next_char == 'a':
            continue
        if current_word in translation_key:
            equation += translation_key[current_word]
            current_word = ''
    return equation