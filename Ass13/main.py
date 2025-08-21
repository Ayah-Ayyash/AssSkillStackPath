from max_heap import MaxHeap

heap = MaxHeap()
numbers = [15, 10, 20, 17, 8, 25]

for num in numbers:
    heap.insert(num)
    print("Heap after inserting", num, ":", heap)

print("\nPopping elements in descending order:")
while True:
    val = heap.pop()
    if val is None:
        break
    print(val, end=" ")
print()
