from models.library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, item_id, title, author, issue):
        super().__init__(item_id, title, author)
        self.issue = issue

    def display_info(self):
        status = "Available" if self.available else "Borrowed"
        print(f"Magazine ID: {self.item_id}, Title: {self.title}, Author: {self.author}, Issue: {self.issue}, Status: {status}")
