from lexer import tokenize
from parser import pratt_parse
from evaluator import evaluate


def main():
    while True:
        user_input = input(">>> ")
        if user_input == "exit":
            break
        src_list = tokenize(user_input)
        parsed_tree = pratt_parse(src_list, 0)
        result = evaluate(parsed_tree)
        print("The result is: ", result)
    print("Now it is time to exit.")


def testing_pratt_parse():
    temp = "-(-5)"
    src_list = tokenize(temp)
    parsed_tree = pratt_parse(src_list, 0)
    output = evaluate(parsed_tree)
    print_tree(parsed_tree)
    print()
    print("The result is: ", output)
    return


def print_tree(node, depth=0):
    if node is not None:
        print("  " * depth + str(node.value))
        print_tree(node.left, depth + 1)
        print_tree(node.right, depth + 1)


if __name__ == "__main__":
    #main()
    testing_pratt_parse()