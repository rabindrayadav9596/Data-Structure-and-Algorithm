class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None


# inserting elements in BST


    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)

        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)

        else:
            print("Value is already presenet in BST")

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True

        else:
            return None

    def _find(self, data, cur_node):
        if data == cur_node.data:
            return True
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        elif data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)

    def inorder_print(self):
        if self.root:
            self._inorder_print(self.root)

    def _inorder_print(self, cur_node):
        if cur_node:
            self._inorder_print(cur_node.left)
            print(str(cur_node.data))
            self._inorder_print(cur_node.right)


bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)


print(bst.inorder_print())
# print(bst.find(10))
