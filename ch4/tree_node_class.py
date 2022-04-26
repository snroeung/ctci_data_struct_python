class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def isLeaf(self):
        if self.left == None & self.right == None:
            return True
        else:
            return False
