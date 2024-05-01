def evaluate(node):
    if type(node) is None:
        return None
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
