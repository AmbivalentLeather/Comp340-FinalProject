from tree_class import TreeNode

precedence_dict = {
    'PLUS': 1, 'MINUS': 1,
    'TIMES': 2, 'DIVIDE': 2,
    'NUMB': 0,
    'LPAREN': 0, 'RPAREN':0
}

paren_flag = 0


def pratt_parse(lexer_list, p1_precedence):
    global paren_flag
    while lexer_list:

        if len(lexer_list) == 1:
            temp: TreeNode = TreeNode(lexer_list[0])
            lexer_list.pop(0)
            return temp

        p2_precedence = precedence_dict[lexer_list[1][1]]

        # Code to handle parens does not currently work
        # if lexer_list[0][1] == 'LPAREN':
        #     paren_flag = 1
        #     lexer_list.pop(0)
        #     pass
        #
        # if lexer_list[0][1] == 'RPAREN':
        #     paren_flag = 0
        #     lexer_list.pop(0)
        #     pass

        if paren_flag is True:
            p2_precedence += 3

        op_boolean = precedence_dict[lexer_list[1][1]] > 0

        if op_boolean and p1_precedence >= p2_precedence:
            temp: TreeNode = TreeNode(lexer_list[0])
            lexer_list.pop(0)
            return temp

        if precedence_dict[lexer_list[0][1]] > 0:
            left_tree = op
        else:
            left_tree = TreeNode(lexer_list[0])
            lexer_list.pop(0)

        op = TreeNode(lexer_list[0])
        lexer_list.pop(0)
        right_tree = pratt_parse(lexer_list, p2_precedence)

        op.left = left_tree
        op.right = right_tree

    return op
