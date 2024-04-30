from tree_class import TreeNode

precedence_dict = {
    'PLUS': 1, 'MINUS': 1,
    'TIMES': 2, 'DIVIDE': 2,
    'NUMB': 0,
    'LPAREN': -1, 'RPAREN': -1
}


def pratt_parse(lexer_list, p1_precedence):
    while lexer_list:
        # Base case, if there's only one element, return it
        if len(lexer_list) == 1:
            temp: TreeNode = TreeNode(lexer_list[0])
            lexer_list.pop(0)
            return temp

        p2_precedence = precedence_dict[lexer_list[1][1]]
        op_boolean = precedence_dict[lexer_list[1][1]] > 0

        # If our first element is a PAREN
        if precedence_dict[lexer_list[0][1]] == -1:
            lexer_list.pop(0)
            return pratt_parse(lexer_list, p2_precedence)

        # If our next element is a PAREN -- NOTE: THIS IS LOGICALLY INCORRECT BUT WORKS IN TEST CASES
        # Does not work for "-(-5)"
        if p2_precedence == -1:
            temp: TreeNode = TreeNode(lexer_list[0])
            lexer_list.pop(0)   # Pop num
            lexer_list.pop(0)   # Pop rparen
            return temp

        # If op, and p1 >= p2, return TreeNode
        if op_boolean and p1_precedence >= p2_precedence:
            temp: TreeNode = TreeNode(lexer_list[0])
            lexer_list.pop(0)
            return temp

        neg_flag = False
        # left_tree
        if precedence_dict[lexer_list[0][1]] > 0:
            if lexer_list[0][1] == 'MINUS':
                neg_flag = True
                left_tree = TreeNode(lexer_list[0])
                lexer_list.pop(0)
            else:
                left_tree = op
                p2_precedence = precedence_dict[lexer_list[0][1]]
        else:
            left_tree = TreeNode(lexer_list[0])
            lexer_list.pop(0)

        if left_tree.token == 'LPAREN':
            p2_precedence = precedence_dict[lexer_list[1][1]]
            return pratt_parse(lexer_list, 0)

        if neg_flag == True:
            op = left_tree
            left_tree = TreeNode(['0', 'NUMB'])
            right_tree = pratt_parse(lexer_list, 4)
        else:
            op = TreeNode(lexer_list[0])
            lexer_list.pop(0)
            right_tree = pratt_parse(lexer_list, p2_precedence)

        # Set op.left and op.right accordingly
        op.left = left_tree
        op.right = right_tree

        # Here we test to see if the future op is lower precedence than the current op.
        # If that is true, we check if both op.left and op.right are 'NUMB' types.
        # If that is true, we return op.
        some_test = False   # We predefine some_test as False so we can check it in the second condition below
        if len(lexer_list) >= 1:
            some_test = p2_precedence > precedence_dict[lexer_list[0][1]]
        if op.left.token == 'NUMB' and op.right.token == 'NUMB' and some_test:
            return op

    return op
