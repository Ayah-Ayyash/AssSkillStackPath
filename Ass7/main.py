from linked_list import LinkedList

ll = LinkedList()
data_items = [1, 2, 3, 4, 5]

for item in data_items:
    ll.append(item)

print("Original Linked List:")
ll.print_list()

ll.reverse()

print("Reversed Linked List:")
ll.print_list()
