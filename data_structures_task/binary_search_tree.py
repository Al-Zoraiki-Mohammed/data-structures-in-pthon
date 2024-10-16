"""Implementation of Binary Search Tree data structure form scratch"""


class TreeNode:
    """Represents a node in a binary search tree (BST) 
    with a key value and left and right child links.
"""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """Representing a binary search tree (BST) data structure."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """ insert(key): Inserts an element with the given key into the BST."""
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        return node

    def lookup(self, key):
        """lookup(key): Finds an element by its key and returns a link to it (node)."""
        return self._lookup_recursive(self.root, key)

    def _lookup_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._lookup_recursive(node.left, key)
        return self._lookup_recursive(node.right, key)

    def delete(self, key):
        """delete(key): Deletes an element by its key from the BST."""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_node = self._find_min(node.right)
            node.key = min_node.key
            node.right = self._delete_recursive(node.right, min_node.key)
        return node

    @staticmethod
    def _find_min(node):
        while node.left is not None:
            node = node.left
        return node

    def inorder_traversal(self):
        """Performs an inorder traversal of the BST,
           returning the elements in sorted order.
           """
        return self._inorder_traversal_recursive(self.root)

    def _inorder_traversal_recursive(self, node):
        if node is None:
            return ''
        result = self._inorder_traversal_recursive(node.left)
        result += ' ' + str(node.key) + ' '
        result += self._inorder_traversal_recursive(node.right)
        return result.strip()


if __name__ == "__main__":
    bst = BinarySearchTree()
    print("inserting 4,2,0,3,1 to the BST ")
    bst.insert(4)
    bst.insert(2)
    bst.insert(0)
    bst.insert(3)
    bst.insert(1)

    print("Inorder Traversal :", bst.inorder_traversal())

    # inserting 9,5,8,6,7 to the BST
    print("inserting 9,5,8,6,7 to the BST")
    bst.insert(9)
    bst.insert(5)
    bst.insert(8)
    bst.insert(6)
    bst.insert(7)

    print("Inorder Traversal:", bst.inorder_traversal())

    print(f"Lookup 7: value {bst.lookup(7).key} link/node: {bst.lookup(7)}")
    bst.delete(6)
    print("Inorder Traversal after deletion of 6:", bst.inorder_traversal())
