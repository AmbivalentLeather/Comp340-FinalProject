"""
Author: Nicholas Young
Date: 2024-04-30
Class: Comp 340-002
"""

def translate(ch: str):
    match ch:
        case '(':
            return 'LPAREN'
        case ')':
            return 'RPAREN'
        case '+':
            return 'PLUS'
        case '-':
            return 'MINUS'
        case '*':
            return 'TIMES'
        case '/':
            return 'DIVIDE'
        case _:
            if ch.isnumeric():
                return 'NUMB'


def tokenize(src: str):
    src_list: list[list] = []
    for i in range(len(src)):
        if src[i] == ' ':
            continue

        token = translate(src[i])
        if len(src_list) > 0 and token == 'NUMB' and src_list[-1][1] == 'NUMB':
            src_list[-1][0] = src_list[-1][0] + src[i]
        else:
            src_list.append([src[i], token])

    return src_list
