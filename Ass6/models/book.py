from models.library_item import LibraryItem

class Reservable:
    def reserve(self, user):
        pass

class Book(LibraryItem, Reservable):
    def __init__(self, item_id, title, author, genre):
        super().__init__(item_id, title, author)
        self.genre = genre
        self.reserved_by = None

    def display_info(self):
        status = "Available" if self.available else "Borrowed"
        reserved = f", Reserved by {self.reserved_by}" if self.reserved_by else ""
        print(f"Book ID: {self.item_id}, Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Status: {status}{reserved}")

    def reserve(self, user):
        if self.reserved_by:
            from exceptions.custom_exceptions import ItemNotAvailableError
            raise ItemNotAvailableError(f"{self.title} is already reserved")
        self.reserved_by = user.user_id
