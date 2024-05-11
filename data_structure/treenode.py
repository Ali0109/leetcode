class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursively(data, self.root)

    def _insert_recursively(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursively(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursively(data, node.right)
        else:
            pass

    def inorder_traversal(self, node):
        if node:
            print(f"2 {node.data}")
            self.inorder_traversal(node.left)
            print(f"3 {node.data}")
            print(node.data, end=" ")
            print(f"4 {node.data}")
            self.inorder_traversal(node.right)
            print(f"5 {node.data}")


binary_tree = BinaryTree()
binary_tree.insert(5)
binary_tree.insert(3)
binary_tree.insert(7)
binary_tree.insert(1)
binary_tree.insert(4)

print("Inorder traversal:")
binary_tree.inorder_traversal(binary_tree.root)
