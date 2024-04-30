from lexer import tokenize
from parser import pratt_parse
from evaluator import evaluate


def print_pratt_parse():
    while True:
        user_input = input(">>> ")
        if user_input == "exit":
           break
        src_list = tokenize(user_input)
        parsed_tree = pratt_parse(src_list, 0)
        output = evaluate(parsed_tree)
        # print_tree(parsed_tree)
        print("The result is: ", output)
    return

def testing_pratt_parse():
    #while True:
    #user_input = input(">>> ")
    # 23 * ((1 + 5) * 33)
    temp = "5 - 13 / 21 + 21 * 6"
    #if user_input == "exit":
    #   break
    src_list = tokenize(temp)
    parsed_tree = pratt_parse(src_list, 0)
    output = evaluate(parsed_tree)
    # print_tree(parsed_tree)
    print("The result is: ", output)
    return

def print_tree(node, depth=0):
    if node is not None:
        print("  " * depth + str(node.value))
        print_tree(node.left, depth + 1)
        print_tree(node.right, depth + 1)


print_pratt_parse()
