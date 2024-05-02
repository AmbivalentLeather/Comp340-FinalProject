"""
Author: Nicholas Young
Date: 2024-04-30
Class: Comp 340-002
"""

def evaluate(node):
    if node.token == "NUMB":
        return int(node.value)

    left = evaluate(node.left)
    right = evaluate(node.right)
    match node.token:
        case "MINUS":
            return left - right
        case "DIVIDE":
            return left / right
        case "PLUS":
            return left + right
        case "TIMES":
            return left * right
