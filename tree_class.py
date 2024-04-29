class TreeNode:
    def __init__(self, src_token):
        self.value = src_token[0]
        self.token = src_token[1]
        self.left = None
        self.right = None
