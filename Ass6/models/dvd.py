from models.library_item import LibraryItem
from models.book import Reservable
from exceptions.custom_exceptions import ItemNotAvailableError

class DVD(LibraryItem, Reservable):
    def __init__(self, item_id, title, author, duration):
        super().__init__(item_id, title, author)
        self.duration = duration
        self.reserved_by = None

    def display_info(self):
        status = "Available" if self.available else "Borrowed"
        reserved = f", Reserved by {self.reserved_by}" if self.reserved_by else ""
        print(f"DVD ID: {self.item_id}, Title: {self.title}, Author: {self.author}, Duration: {self.duration} mins, Status: {status}{reserved}")

    def reserve(self, user):
        if self.reserved_by:
            raise ItemNotAvailableError(f"{self.title} is already reserved")
        self.reserved_by = user.user_id
