from sorted_circular_linked_list import SortedCircularLinkedList

scll = SortedCircularLinkedList()
data_items = [7, 3, 9, 1, 4]

for item in data_items:
    scll.insert(item)
    scll.print_list()
