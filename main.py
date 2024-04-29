from lexer import tokenize
from parser import pratt_parse
from evaluator import evaluate


def print_pratt_parse():
    while True:
        user_input = input("Input: ")
        src_list = tokenize(user_input)
        # [['10', 'NUMB'], ['*', 'TIMES'], ['3', 'NUMB'], ['/', 'DIVIDE'], ['40', 'NUMB'], ['+', 'PLUS'], ['1', 'NUMB']]
        parsed_tree = pratt_parse(src_list, 0)
        x = evaluate(parsed_tree)
        return x

"""
def print_tree(node, depth=0):
    if node is not None:
        print("  " * depth + str(node.value))
        print_tree(node.left, depth + 1)
        print_tree(node.right, depth + 1)
"""

output = print_pratt_parse()
print(output)

