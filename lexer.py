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

    # It could be helpful to add an "End of string" character for us to use in the parser later

    return src_list
