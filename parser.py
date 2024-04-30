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

        if op_boolean is False and p2_precedence == -1:
            temp: TreeNode = TreeNode(lexer_list[0])
            lexer_list.pop(0)   # Pop num
            lexer_list.pop(0)   # Pop rparen
            return temp

        # If op, and p1 >= p2, return TreeNode
        if op_boolean and p1_precedence >= p2_precedence:
            temp: TreeNode = TreeNode(lexer_list[0])
            lexer_list.pop(0)
            return temp

        # left_tree
        if precedence_dict[lexer_list[0][1]] > 0:
            left_tree = op
        else:
            left_tree = TreeNode(lexer_list[0])
            lexer_list.pop(0)

        if left_tree.value == '(':
            return pratt_parse(lexer_list, 0)
        op = TreeNode(lexer_list[0])
        lexer_list.pop(0)
        right_tree = pratt_parse(lexer_list, p2_precedence)

        # Set op.left and op.right accordingly
        op.left = left_tree
        op.right = right_tree

    return op
