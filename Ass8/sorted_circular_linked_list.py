class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SortedCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            return
        current = self.head
        prev = None
        while True:
            if data < current.data:
                break
            prev = current
            current = current.next
            if current == self.head:
                break
        if prev is None:
            last = self.head
            while last.next != self.head:
                last = last.next
            new_node.next = self.head
            self.head = new_node
            last.next = self.head
        else:
            prev.next = new_node
            new_node.next = current
            if current == self.head and data > prev.data:
                pass

    def print_list(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(f"[{current.data}]", end=" -> " if current.next != self.head else "\n")
            current = current.next
            if current == self.head:
                break
