class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def display_info(self):
        print(f"Product: {self.name}, Price: ${self.price:.2f}")


class Drink(Product):
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = int(volume)

    def display_info(self):
        super().display_info()
        print(f"Volume: {self.volume}ml")


class Snack(Product):
    def __init__(self, name, price, calories):
        super().__init__(name, price)
        self.calories = int(calories)

    def display_info(self):
        super().display_info()
        print(f"Calories: {self.calories}")


class Candy(Product):
    def __init__(self, name, price, flavor):
        super().__init__(name, price)
        self.flavor = flavor

    def display_info(self):
        super().display_info()
        print(f"Flavor: {self.flavor}")


def create_product(line):
    parts = line.strip().split(",")
    p_type, name, price, attr = parts

    if p_type == "Drink":
        return Drink(name, price, attr)
    elif p_type == "Snack":
        return Snack(name, price, attr)
    elif p_type == "Candy":
        return Candy(name, price, attr)


# def load_products(filename):
#     products = []
#     with open(filename, "r") as file:
#         for line in file:
#             product = create_product(line)
#             products.append(product)
#     return products


# def vending_machine():
#     products = load_products("products.txt")

#     print("Welcome to the Python Vending Machine!\n")
#     print("Please select what you want:")
#     for i, product in enumerate(products, start=1):
#         print(f"{i}. {product.__class__.__name__} - {product.name}")

#     choice = int(input("\n> "))
#     if 1 <= choice <= len(products):
#         print("\nProduct Information:")
#         products[choice - 1].display_info()
#     else:
#         print("Invalid choice.")

def load_products(filename):
    products = []
    with open(filename, "r") as file:
        for line in file:
            product = create_product(line)
            products.append(product)
    return products


def vending_machine():
    products = load_products(r"E:\AssSkillStackPath\Ass5\products.txt")

    print("Welcome to the Python Vending Machine!\n")
    print("Please select what you want:")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product.__class__.__name__} - {product.name}")

    choice = int(input("\n> "))
    if 1 <= choice <= len(products):
        print("\nProduct Information:")
        products[choice - 1].display_info()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    vending_machine()
