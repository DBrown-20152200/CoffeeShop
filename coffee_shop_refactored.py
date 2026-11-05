"""
Refactored Coffee Shop Ordering System
"""
from coffee_shop_exceptions import *

class MenuItem():
    """The items on the menu and their customisations"""

    #dict of drink sizes and their price multipliers
    drinks_sizes = {"small":1.0,
                   "medium":1.3,
                   "large":1.6
                   }

    #list of the drink sizes as strings
    available_sizes = []
    for key in drinks_sizes:
        available_sizes.append(key)

    #list of drinks on the menu and their prices
    drinks_menu = {"latte":4.50,
                    "cappucino":4.25,
                    "esspresso":3.50,
                    "americano":3.75,
                    "mocha":5.00
                    }

    #user friendly version of drinks_menu
    drinks_menu_priced = drinks_menu
    for item in drinks_menu:
        drinks_menu_priced[item] = f"${drinks_menu[item]}"

    #list of milks and their prices
    milk_prices = {"oat":0.50,
                   "almond":0.50,
                   "whole":0.00,
                   "skim":0.00,
                   "none":0.00
                   }

    def __init__(self):
        """Initialises MenuItem"""

        #lets customer choose a drink from the menu
        print(f"\n Drinks Menu: {MenuItem.drinks_menu}")
        self._drink = input("Drink selection: ").strip().lower()
        if self._drink not in MenuItem.drinks_menu:
            raise InvalidItemError

        #lets customer choose drink size
        print(f"Available sizes: {"/".join(self.available_sizes)}")
        self._size = input("Select drink size: ").strip().lower()
        if self._size not in MenuItem.drinks_sizes:
            raise InvalidCustomizationError

        #lets customer customise milk choice
        print(f"Available milk choices: {MenuItem.milk_prices}")
        self._milk = input("Select milk choice: ").strip().lower()

        self._price = 0.00

    def calculate_price (self):
        """Calculates the item price after all selections are made."""

        self._price = (self.drinks_menu.get(self._drink) * 
                        self.drinks_sizes.get(self._size) +
                        self.milk_prices.get(self._milk))

class LoyaltyProgram():
    """Manages loyalty points and discounts."""

    loyalty_discount = 0.10
    points_redeem_threshold = 100
    
    loyalty_account_list = {}

    def __init__(self, name: str):

        self._name = name
        self._points_total = 0

    def __str__(self):
        return "View Loyalty Accounts"

    def add_account(loyalty_account: LoyaltyProgram):
        LoyaltyProgram.loyalty_account_list[
            loyalty_account._account_number] = loyalty_account

    def verify_account(loyalty_account: LoyaltyProgram):
        if loyalty_account._account_number not in LoyaltyProgram.loyalty_account_list:
            LoyaltyProgram.add_account(loyalty_account)

    def points_balance (loyalty_account: LoyaltyProgram):
        return loyalty_account._points_total

    def redeem_free_drink(loyalty_account: LoyaltyProgram):
        if loyalty_account.points_balance >= LoyaltyProgram.points_redeem_threshold:
            loyalty_account._points_total -= 100

class Customer():
    """Manages customer information"""

    staff_list = []

    def __init__(self, name: str):
        self._name = name
        self._loyalty_account = None
        self._is_staff = False

    def enter_loyalty_account(self, loyalty_account: LoyaltyProgram):
        LoyaltyProgram.verify_account(loyalty_account)
        self._loyalty_account = loyalty_account

    def verify_staff_member(customer: Customer):
        if customer._name in Customer.staff_list:
            customer._is_staff = True
        else:
            customer._is_staff = False        

class Payment():
    """Manages payment type and amount"""

    payment_type_list = ["cash",
                         "card",
                         "points",
                         "staff discount"
                        ]

    def __init__(self, total_price: float, method: str, amount_paid: float):
        self._total_price = total_price 
        self._payment_method = method
        self._payment_amount = amount_paid

        if self._payment_method not in self.payment_type_list:
            raise PaymentError
        else:
            self._total_price -= self._payment_amount

class Order():
    """Class for creating orders"""

    def __init__(self):
        self._order_number = int()
        self._customer = str()
        self._item_list = []
        self._payment = str()
        self._total_cost = 0.00

    def add_item(self, item: MenuItem):
        self._item_list.append(item)

    def calculate_total_cost(self):
        for items in self._item_list:
            self._total_cost += items._price

    def __str__(self):
        return "Take Order"

class StaffOrder(Order):
    def __str__(self):
        return "Staff order"

class DailyReport():
    def __str__(self):
        return "Daily Report"

def verify_input(input_message):
    try:
        input_message = int(input_message)
        return input_message
    except:
        raise CoffeeShopError
        
def main_menu():
    """Displays the main menu to allow function selection"""

    main_menu_options = {1:Order(),
                         2:StaffOrder(),
                         3:DailyReport(),
                         4:LoyaltyProgram(),
                         5:"Reset Daily Counters",
                         6:"Exit"}

    print("\n======= Coffee Shop POS =======\n")

    for key in main_menu_options:
        print(f"\n{key}:{main_menu_options[key]}")
    print("\n===============================")

    choice = verify_input(input("Choice: ").strip())

    #creates objects based on user input
    if choice in main_menu_options:
        choice = main_menu_options[choice]
    else:
        raise CoffeeShopError

if __name__ == "__main__":
    main_menu()