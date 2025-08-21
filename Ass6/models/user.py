class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_items = []

    def borrow_item(self, item):
        self.borrowed_items.append(item.item_id)
        item.available = False

    def return_item(self, item):
        if item.item_id in self.borrowed_items:
            self.borrowed_items.remove(item.item_id)
            item.available = True
