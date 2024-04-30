from tree_class import TreeNode

precedence_dict = {
    'PLUS': 1, 'MINUS': 1,
    'TIMES': 2, 'DIVIDE': 2,
    'NUMB': 0,
    'LPAREN': 0, 'RPAREN': 0
}


def pratt_parse(lexer_list, p1_precedence):
    while lexer_list:
        neg_flag = False
        # Base case, if there's only one element, return it
        if len(lexer_list) == 1:
            temp: TreeNode = TreeNode(lexer_list[0])
            lexer_list.pop(0)
            return temp

        p2_precedence = precedence_dict[lexer_list[1][1]]
        op_boolean = precedence_dict[lexer_list[1][1]] > 0

        # If op, and p1 >= p2, return TreeNode
        if op_boolean and p1_precedence >= p2_precedence:
            temp: TreeNode = TreeNode(lexer_list[0])
            lexer_list.pop(0)
            return temp

        # left_tree
        if precedence_dict[lexer_list[0][1]] > 0:
            # If first element is operator, set left_tree = op
            if lexer_list[0][0] == '-':
                neg_flag = True
            if op_boolean:
                left_tree = op
        else:
            # Else, set left_tree = TreeNode(first list element)
            left_tree = TreeNode(lexer_list[0])
            lexer_list.pop(0)

        if neg_flag:
            left_tree = TreeNode(['0', 'NUMB'])
            op = TreeNode(lexer_list[0])
            lexer_list.pop(0)
            right_tree = pratt_parse(lexer_list, 4)
        op = TreeNode(lexer_list[0])
        lexer_list.pop(0)
        right_tree = pratt_parse(lexer_list, p2_precedence)

        # Set op.left and op.right accordingly
        op.left = left_tree
        op.right = right_tree

    return op
