class CustomerQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, customer_name):
        self.queue.append(customer_name)
        print(f"Arriving: {customer_name}")

    def dequeue(self):
        if self.queue:
            customer = self.queue.pop(0)
            print(f"Serving: {customer}")
        else:
            print("All customers served.")

    def serve_all(self):
        while self.queue:
            self.dequeue()
        if not self.queue:
            print("All customers served.")
