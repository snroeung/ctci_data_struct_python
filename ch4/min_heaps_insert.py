from binary_tree_node_class import BinaryTreeNode

#TODO: implement insert class
        


if __name__ == "__main__":
    root = BinaryTreeNode(4)
    root.left = BinaryTreeNode(50)
    root.right = BinaryTreeNode(7)
    root.left.parent = root.right.parent = root

    root.left.left = BinaryTreeNode(55)
    root.left.right = BinaryTreeNode(90)
    root.left.left.parent = root.left.right.parent = root.left

    root.right.left = BinaryTreeNode(87)
    #add new element to satisfy complete tree property
    root.right.right = BinaryTreeNode(2)
    root.right.left.parent = root.right.right.parent = root.right


