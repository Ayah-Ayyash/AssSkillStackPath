from models.library import Library
from models.book import Book
from models.magazine import Magazine
from models.dvd import DVD

library = Library()

def menu():
    print("\nWelcome to the Library System")
    print("1. View all available items")
    print("2. Search item by title or type")
    print("3. Register as a new user")
    print("4. Borrow an item")
    print("5. Reserve an item")
    print("6. Return an item")
    print("7. Exit and Save")
    return input("Choose an option: ")

while True:
    choice = menu()
    try:
        if choice == "1":
            for item in library.items.values():
                item.display_info()
        elif choice == "2":
            keyword = input("Enter search keyword: ").lower()
            found = False
            for item in library.items.values():
                if keyword in item.title.lower() or keyword == type(item).__name__.lower():
                    item.display_info()
                    found = True
            if not found:
                print("No items found")
        elif choice == "3":
            name = input("Enter your name: ")
            user = library.add_user(name)
            print(f"User registered with ID: {user.user_id}")
        elif choice == "4":
            user_id = input("Enter your user ID: ")
            item_id = input("Enter item ID to borrow: ")
            library.borrow_item(user_id, item_id)
            print("Item borrowed successfully")
        elif choice == "5":
            user_id = input("Enter your user ID: ")
            item_id = input("Enter item ID to reserve: ")
            library.reserve_item(user_id, item_id)
            print("Item reserved successfully")
        elif choice == "6":
            user_id = input("Enter your user ID: ")
            item_id = input("Enter item ID to return: ")
            library.return_item(user_id, item_id)
            print("Item returned successfully")
        elif choice == "7":
            library.save_items()
            library.save_users()
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice")
    except Exception as e:
        print(f"Error: {e}")
