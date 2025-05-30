# The shopping cart exercise
## About

This repository contains basic code of a shopping cart system
## Original task


### Create a Python program that simulates a simple shopping cart system. Consider the following classes:
    
    Product:
        Attributes: name (string), price (float).
        Methods:
            Constructor to initialize attributes.
            display_info(): Prints the product’s name and price.
    ShoppingCart:
        Attribute: items (dictionary storing products and their quantities).
        # hint: Use this format  {product.name: {"product": product, "quantity": quantity}}
        Methods:
            add_product(product, quantity): Adds a product to the cart or increases its quantity.
            remove_product(product, quantity): Reduces the quantity or removes the product.
            calculate_total(): Returns the total cost of all items in the cart.
            display_cart(): Prints all items, quantities, and the total cost.
### Test your results:
```python
# Test the implementation
# Create products
apple = Product("Apple", 0.99)
banana = Product("Banana", 0.59)
milk = Product("Milk", 3.49)
# Create cart
cart = ShoppingCart()
# Add items
cart.add_product(apple, 3)
cart.add_product(banana)
cart.add_product(milk, 2)
cart.display_cart()

# Remove items
cart.remove_product(apple, 1)
cart.remove_product(banana)
cart.display_cart()
# Try to remove a product not in the cart
cart.remove_product(milk, 5)  # Removes all milk
cart.display_cart()
```

## New task

### We need to create an upgraded shopping cart system that considers, in addition to the previous code (`original_solution.py`), the following:

* This system will be used as a python package by our client that will import it as package in the backend of a web service
* Introduce sub types of products (Food, Cleaning, Drinks)
    Food:
        Milk, Bread, Eggs, Bananas, Chicken Breast

    Cleaning Products:
        Dish Soap, Laundry Detergent

    Drinks:
        Bottled Water, Soda, Orange Juice

* These sub types should have the following:
    Food should have additional methods to get expiration date, if it is organic or not, and calories content.
    Cleaning should have additional methods to know if it is safe for children or not.
    Drinks should indicate expiration date, sugar content, and if is tin can, plastic or glass bottle.
* Products sub types should be specified in a PRODUCT_TYPES dictionary.
* Handle the error in case the product is not in the list of available products.
* If a product is added wrongly, do not let the program stop. Use try-except blocks.
* Every Shopping cart should correspond to a user. If the user has a "membership", add 1 fidelity point to the FIDELITY_POINTS dictionary, and print an additional message "Welcome  back, thanks for being a member!". You can use a decorator to print that message.
* Do not forget to annotate your code with docstrings and type hints.

You have to follow this folder structure:


### This concepts may be new:
* Decorators
* Type hints
* Try-except blocks
* Patterns

```bash
solution_shopping_cart/
├── __init__.py
├── constants.py
├── decorators.py
├── models/
   ├── cart.py
   ├── product.py

```
```python
# solution_shopping_cart/__init__.py
from .models.cart import ShoppingCart
from .models.product import Product, Food, CleaningProduct, Drink
from .constants import PRODUCT_TYPES
from .decorators import membership_check

# solution_shopping_cart/constants.py
PRODUCT_TYPES = {
    "Food": ["Milk", "Bread", "Eggs", "Bananas", "Chicken Breast"],
    "Cleaning": ["Dish Soap", "Laundry Detergent"],
    "Drinks": ["Bottled Water", "Soda", "Orange Juice"]
}

FIDELITY_POINTS = {}

# solution_shopping_cart/decorators.py
def membership_check(func):
    """Decorator to add fidelity points for members."""
    def wrapper(self, *args, **kwargs):
        if self.user_membership:
            FIDELITY_POINTS[self.user] = FIDELITY_POINTS.get(self.user, 0) + 1
            print("Welcome back, thanks for being a member!")
        return func(self, *args, **kwargs)
    return wrapper

# solution_shopping_cart/models/product.py
class Product:
    """Base class for all products."""
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    def display_info(self) -> None:
        print(f"Product: {self.name}, Price: ${self.price:.2f}")

class Food(Product):
    """Food subclass."""
    def __init__(self, name: str, price: float, expiration_date: str, organic: bool, calories: int):
        super().__init__(name, price)
        self.expiration_date = expiration_date
        self.organic = organic
        self.calories = calories
    
    def get_expiration_date(self) -> str:
        return self.expiration_date

class CleaningProduct(Product):
    """Cleaning product subclass."""
    def __init__(self, name: str, price: float, safe_for_children: bool):
        super().__init__(name, price)
        self.safe_for_children = safe_for_children
    
    def is_safe_for_children(self) -> bool:
        return self.safe_for_children

class Drink(Product):
    """Drink subclass."""
    def __init__(self, name: str, price: float, expiration_date: str, sugar_content: int, container_type: str):
        super().__init__(name, price)
        self.expiration_date = expiration_date
        self.sugar_content = sugar_content
        self.container_type = container_type
    
    def get_expiration_date(self) -> str:
        return self.expiration_date

# solution_shopping_cart/models/cart.py
class ShoppingCart:
    """Shopping Cart class."""
    def __init__(self, user: str, user_membership: bool = False):
        self.user = user
        self.user_membership = user_membership
        self.items = {}
    
    @membership_check
    def add_product(self, product: Product, quantity: int = 1) -> None:
        """Adds a product to the cart or increases its quantity."""
        try:
            if product.name in self.items:
                self.items[product.name]["quantity"] += quantity
            else:
                self.items[product.name] = {"product": product, "quantity": quantity}
        except Exception as e:
            print(f"Error adding product: {e}")
    
    def remove_product(self, product: Product, quantity: int = 1) -> None:
        """Reduces the quantity or removes the product."""
        try:
            if product.name in self.items:
                if self.items[product.name]["quantity"] > quantity:
                    self.items[product.name]["quantity"] -= quantity
                else:
                    del self.items[product.name]
            else:
                print("Product not found in cart.")
        except Exception as e:
            print(f"Error removing product: {e}")
    
    def calculate_total(self) -> float:
        """Returns the total cost of all items in the cart."""
        return sum(item["product"].price * item["quantity"] for item in self.items.values())
    
    def display_cart(self) -> None:
        """Prints all items, quantities, and the total cost."""
        print(f"Shopping Cart for {self.user}:")
        for item in self.items.values():
            print(f"{item['product'].name} - {item['quantity']} x ${item['product'].price:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")

```

## Instructions

To run system, execute this:

```shell
python run.py
```


## Contributors
Gustavo Larrea

