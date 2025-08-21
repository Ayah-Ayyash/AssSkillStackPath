from bst import BST, is_balanced

bst = BST()
values = [10, 5, 15, 2, 7, 12, 17]

for val in values:
    bst.insert(val)

print("Minimum value in BST:", bst.findMin())
print("Maximum value in BST:", bst.findMax())

print("Is the BST balanced?", is_balanced(bst.root))
