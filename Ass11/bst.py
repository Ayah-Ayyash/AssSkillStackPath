class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return
        current = self.root
        while True:
            if data < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(data)
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(data)
                    break

    def findMin(self):
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.data

    def findMax(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.data

def is_balanced(node):
    def check(node):
        if not node:
            return 0, True
        left_height, left_balanced = check(node.left)
        right_height, right_balanced = check(node.right)
        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        return max(left_height, right_height) + 1, balanced
    _, result = check(node)
    return result
