class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total(self):
        return sum(item.price for item in self.items)

class Restaurant:
    def __init__(self):
        self.menu = []
        self.orders = []

    def add_menu_item(self, item):
        self.menu.append(item)

    def add_order(self, order):
        self.orders.append(order)

    def list_orders(self):
        for idx, order in enumerate(self.orders, 1):
            print(f"Order {idx}:")
            for item in order.items:
                print(f"- {item.name} (${item.price})")
            print(f"Total: ${order.total()}\n")

def main():
    restaurant = Restaurant()

    while True:
        print("Welcome to the Restaurant Management System!")
        print("Choose an option:")
        print("1. Add menu item")
        print("2. View menu")
        print("3. Create new order")
        print("4. List all orders")
        print("5. Exit")
        choice = input("> ")

        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            category = input("Enter item category: ")
            item = MenuItem(name, price, category)
            restaurant.add_menu_item(item)
            print("Menu item added successfully.\n")

        elif choice == "2":
            print("Menu:")
            for idx, item in enumerate(restaurant.menu, 1):
                print(f"{idx}. {item.name} (${item.price}) [{item.category}]")
            print()

        elif choice == "3":
            if not restaurant.menu:
                print("No menu items available.\n")
                continue
            print("Enter item numbers for the order separated by commas (e.g., 1,2):")
            input_numbers = input()
            indices = [int(x.strip()) - 1 for x in input_numbers.split(",")]
            order = Order()
            for i in indices:
                if 0 <= i < len(restaurant.menu):
                    order.add_item(restaurant.menu[i])
            restaurant.add_order(order)
            print("Order created and added successfully.\n")

        elif choice == "4":
            if not restaurant.orders:
                print("No orders have been placed yet.\n")
            else:
                restaurant.list_orders()

        elif choice == "5":
            print("Thank you for using the Restaurant Management System!")
            break

        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
