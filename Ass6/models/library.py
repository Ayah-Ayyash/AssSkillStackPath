import json
from models.book import Book
from models.magazine import Magazine
from models.dvd import DVD
from models.user import User
from exceptions.custom_exceptions import ItemNotFoundError, UserNotFoundError, ItemNotAvailableError

class Library:
    def __init__(self, items_file="items.json", users_file="users.json"):
        self.items_file = items_file
        self.users_file = users_file
        self.items = {}
        self.users = {}
        self.load_items()
        self.load_users()

    def load_items(self):
        try:
            with open(self.items_file, "r") as f:
                data = json.load(f)
            for d in data:
                if d["type"] == "Book":
                    self.items[d["item_id"]] = Book(d["item_id"], d["title"], d["author"], d["genre"])
                elif d["type"] == "Magazine":
                    self.items[d["item_id"]] = Magazine(d["item_id"], d["title"], d["author"], d["issue"])
                elif d["type"] == "DVD":
                    self.items[d["item_id"]] = DVD(d["item_id"], d["title"], d["author"], d["duration"])
        except FileNotFoundError:
            self.items = {}

    def load_users(self):
        try:
            with open(self.users_file, "r") as f:
                data = json.load(f)
            for d in data:
                user = User(d["user_id"], d["name"])
                user.borrowed_items = d.get("borrowed_items", [])
                self.users[d["user_id"]] = user
        except FileNotFoundError:
            self.users = {}

    def save_items(self):
        data = []
        for item in self.items.values():
            item_type = type(item).__name__
            d = {"item_id": item.item_id, "title": item.title, "author": item.author, "type": item_type}
            if item_type == "Book":
                d["genre"] = item.genre
            elif item_type == "Magazine":
                d["issue"] = item.issue
            elif item_type == "DVD":
                d["duration"] = item.duration
            data.append(d)
        with open(self.items_file, "w") as f:
            json.dump(data, f, indent=4)

    def save_users(self):
        data = []
        for user in self.users.values():
            d = {"user_id": user.user_id, "name": user.name, "borrowed_items": user.borrowed_items}
            data.append(d)
        with open(self.users_file, "w") as f:
            json.dump(data, f, indent=4)

    def add_user(self, name):
        user_id = str(len(self.users) + 1)
        user = User(user_id, name)
        self.users[user_id] = user
        return user

    def add_item(self, item):
        self.items[item.item_id] = item

    def borrow_item(self, user_id, item_id):
        if user_id not in self.users:
            raise UserNotFoundError(f"User {user_id} not found")
        if item_id not in self.items:
            raise ItemNotFoundError(f"Item {item_id} not found")
        item = self.items[item_id]
        user = self.users[user_id]
        if not item.available:
            raise ItemNotAvailableError(f"{item.title} is not available")
        user.borrow_item(item)

    def return_item(self, user_id, item_id):
        if user_id not in self.users:
            raise UserNotFoundError(f"User {user_id} not found")
        if item_id not in self.items:
            raise ItemNotFoundError(f"Item {item_id} not found")
        item = self.items[item_id]
        user = self.users[user_id]
        user.return_item(item)

    def reserve_item(self, user_id, item_id):
        if user_id not in self.users:
            raise UserNotFoundError(f"User {user_id} not found")
        if item_id not in self.items:
            raise ItemNotFoundError(f"Item {item_id} not found")
        item = self.items[item_id]
        user = self.users[user_id]
        if hasattr(item, "reserve"):
            item.reserve(user)
        else:
            raise ItemNotAvailableError(f"{item.title} cannot be reserved")
