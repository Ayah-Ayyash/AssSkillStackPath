from customer_queue import CustomerQueue

cq = CustomerQueue()

customers = ["Alice", "Bob", "Carol"]

for customer in customers:
    cq.enqueue(customer)

cq.serve_all()
