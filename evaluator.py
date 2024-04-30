def evaluate(node):
    if node.left is None or node.right is None:
        return int(node.value)

    left = evaluate(node.left)
    right = evaluate(node.right)
    match node.value:
        case "-":
            return left - right
        case "/":
            return left / right
        case "+":
            return left + right
        case "*":
            return left * right
