class Node:
    value = None
    parent = None
    left = None
    right = None

    def __init__(self, val):
        self.value = val

    def get_value(self):
        return self.value

    def get_parent(self):
        return self.parent

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


class BST:
    root = None

    def __init__(self, a):

        self.root = Node(a[0])

        for value in a[1:]:
            self.insert(value)

    def insert(self, value: int):

        if self.root is None:
            self.root = Node(value)
            return

        current_node = self.root

        new_node = Node(value)

        while new_node.parent is None:

            # right node, parent right NIL
            if value >= current_node.get_value() and current_node.get_right() is None:

                current_node.right = new_node
                new_node.parent = current_node
                current_node = self.root
            # left node, parent left NIL
            elif value <= current_node.get_value() and current_node.get_left() is None:
                current_node.left = new_node
                new_node.parent = current_node
                current_node = self.root

                # navigate into right node, start new iteration
            elif value >= current_node.get_value():
                current_node = current_node.right

                # navigate into left node, start new iteration
            else:
                current_node = current_node.left

    def in_order_traversal(self) -> list:

        array = []

        if self.root is not None:
            self.in_order(self.root, array)

        return array

    def in_order(self, node, array: list) -> list:

        if node.left is None and node.right is None:
            pass
        elif node.left is not None:
            self.in_order(node.left, array)

        array.append(node.value)

        if node.right is not None:
            self.in_order(node.right, array)

        return array

    @staticmethod
    def find_min(node=root) -> Node:

        current_node = node

        while current_node.left is not None:
            current_node = current_node.left

        return current_node

    @staticmethod
    def find_max(node=root) -> Node:

        current_node = node

        while current_node.right is not None:
            current_node = current_node.right

        return current_node

    # returns node with value if found. if not found,
    #  returns node of would-be parent to value as tuple with (node, False)
    # if node is found, returns (node, True) tuple, y value indicating it found the specified value.
    def search(self, value: int) -> tuple:
        # current_node starts at root of tree
        # returns None if root does not exist.
        if self.root is None:
            return None, false

        current_node = self.root
        while True:
            # current_node is equal to value, node is found.
            if current_node == value:
                return current_node, True
            # Value is smaller than current_node, go to left child
            elif current_node.value > value and current_node.left is not None:
                current_node = current_node.left
                # value is larger than current_node, go to right child
            elif current_node.value < value and current_node.right is not None:
                current_node = current_node.right
            # the value is not in the tree, return parent_node
            else:
                return current_node, False

    def find_larger(self, value: int) -> Node or None:

        current_node = self.search(value)[0]

        # current_node is actual value in tree:
        if value == current_node.value:

            # if right subtree exists, next_larger is
            # the minimum of right subtree
            if current_node.right is not None:
                return self.find_min(current_node.right)
            # else, iterate up parents until current node is left child
            # return parent_node, which is next_larger in this case.
            else:
                # if parent is None, next larger does not exist.
                while current_node.parent is not None:

                    if current_node.parent.left == current_node:
                        return current_node.parent
                    else:
                        # move up one tree-level
                        current_node = current_node.parent
                        # next larger does not exist, return None
                return None

                # current_node is parent node to would-be value in tree:

        else:

            # if parent node is larger than value, it is the next-larger:

            if current_node.value > value:
                return current_node

            # otherwise, iterate up parents until current node is left child
            else:
                # if parent is None, next larger does not exist.
                while current_node.parent is not None:

                    if current_node.parent.left == current_node:
                        return current_node.parent
                    else:
                        # move up one tree-level
                        current_node = current_node.parent
                        # next larger does not exist, return None
                return None

    def find_smaller(self, value: int) -> Node or None:
        current_node = self.search(value)[0]

        # current_node is actual value in tree:
        if value == current_node.value:

            # if left subtree exists, next_smaller is
            # the maximum of left subtree
            if current_node.left is not None:
                return self.find_max(current_node.left)
            # else, iterate up parents until current node is right child
            # return parent_node, which is next_smaller in this case.
            else:
                # if parent is None, next smaller does not exist.
                while current_node.parent is not None:

                    if current_node.parent.right == current_node:
                        return current_node.parent
                    else:
                        # move up one tree-level
                        current_node = current_node.parent
                        # next smaller does not exist, return None
                return None

                # current_node is parent node to would-be value in tree:

        else:
            # if parent node is smaller than value, it is the next-smaller:

            if current_node.value < value:
                return current_node

            # otherwise, iterate up parents until current node is right child
            else:
                # if parent is None, next larger does not exist.
                while current_node.parent is not None:

                    if current_node.parent.right == current_node:
                        return current_node.parent
                    else:
                        # move up one tree-level
                        current_node = current_node.parent
                        # next larger does not exist, return None
                return None

    def delete(self, value: int) -> bool:

        current_node = self.search(value)[0]
        # value/node does not exist, return False
        if self.root is None or value != current_node.value:
            return False

        # if you're a leaf, we take you out:
        if current_node.left is None and current_node.right is None:

            # if its the last node, which is root.
            if current_node == self.root:
                self.root = None

            # node is left child:
            elif current_node.parent.left == current_node:
                current_node.parent.left = None
                current_node.parent = None
            # node is right child:
            else:
                current_node.parent.right = None
                current_node.parent = None

        # if you have two subtrees, we find next larger and replace its value with your node, and delete next-larger
        elif current_node.left is not None and current_node.right is not None:
            replacer = self.find_larger(current_node.value)
            new_val = replacer.value
            self.delete(replacer.value)
            current_node.value = new_val  # this is always a leaf

        # else: there is one subtree or node, make the parent of the node being deleted now point at that
        # node/ start of subtree instead.
        # will also work when deleting current root

        else:
            # the node being deleted is the root, when it has one subtree.
            if current_node == self.root:

                # the only subtree is the left child
                if current_node.left is not None:

                    self.root = current_node.left
                    self.root.parent = None
                    # the only subtree is the right child
                else:
                    self.root = current_node.right
                    self.root.parent = None

            # node being deleted is left child:
            elif current_node.parent.left == current_node:

                # existing subtree/node is left child, replacer
                if current_node.left is not None:
                    current_node.parent.left = current_node.left
                    current_node.left.parent = current_node.parent

                # existing subtree(node is right child, replacer
                else:
                    current_node.parent.left = current_node.right
                    current_node.right.parent = current_node.parent
            # node being deleted is right child

            else:

                # existing subtree/node is left child, replacer
                if current_node.left is not None:
                    current_node.parent.right = current_node.left
                    current_node.left.parent = current_node.parent

                # existing subtree(node is right child, replacer
                else:
                    current_node.parent.right = current_node.right
                    current_node.left.parent = current_node.parent

        return True
