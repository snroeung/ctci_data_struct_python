from tree_node_class import TreeNode


def inOrderTraversal(node):
    if node:
        inOrderTraversal(node.left)
        print(node.data)
        inOrderTraversal(node.right)


def preOrderTraversal(node):
    if node:
        print(node.data)
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)


def postOrderTraversal(node):
    if node:
        postOrderTraversal(node.left)
        postOrderTraversal(node.right)
        print(node.data)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Inorder traversal of binary tree: ")
    inOrderTraversal(root)

    print("\nPreorder traversal of binary tree: ")
    preOrderTraversal(root)

    print("\nPostorder traversal of binary tree: ")
    postOrderTraversal(root)
