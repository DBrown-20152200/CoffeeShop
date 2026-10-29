"""
Refactored Coffee Shop Ordering System
"""
from coffee_shop_exceptions import *

class MenuItem():
    """A class of the drinks on the menu"""

    drinks_sizes = {"small":1.0,
                   "medium":1.3,
                   "large":1.6}

    drinks_menu = {"latte":4.50,
                    "cappucino":4.25,
                    "esspresso":3.50,
                    "americano":3.75,
                    "mocha":5.00}

    milk_prices = {"oat":0.50,
                   "almond":0.50,
                   "whole":0.00,
                   "skim":0.00,
                   "none":0.00}

    def __init__(self, drink: str, size: str, milk: str):        
        self._drink = drink
        self._size = size
        self._milk = milk
        self._price = 0.00

        if drink not in self.drinks_menu:
            raise InvalidItemError

        if size not in self.drinks_sizes:
            raise InvalidCustomizationError

        if milk not in self.milk_prices:
            raise InvalidCustomizationError

    def calculate_price (menu_item: MenuItem):
        """Calculates the item price after all selections are made."""
        menu_item._price = MenuItem.drinks_menu.get(menu_item._drink)
        menu_item._price *= MenuItem.drinks_sizes.get(menu_item._size)
        menu_item._price += MenuItem.milk_prices.get(menu_item._milk)

class LoyaltyProgram():
    """Manages loyalty points and discounts."""

    loyalty_discount = 0.10
    points_redeem_threshold = 100
    
    loyalty_account_list = {}

    def __init__(self, account_number: int, name: str, phone_number: int, email: str):
        self._account_number = account_number
        self._name = name
        self._phone_number = phone_number
        self._email = email
        self._points_total = 0

    def add_account(loyalty_account: LoyaltyProgram):
        LoyaltyProgram.loyalty_account_list[loyalty_account._account_number] = loyalty_account

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

    def __init__(self, base_price: float, extras_price: float, total_price: float):
        self._base_price = base_price
        self._extras_price = extras_price
        self._total_price = total_price

class CashPayment(Payment):
    def __init__(self, base_price: float, extras_price: float, total_price: float, amount_paid: float):
        super().__init__(base_price, extras_price, total_price)
        self._amount_paid = amount_paid

class Order():
    def __init__(self, order_number: int, customer: Customer, item_list: list[MenuItem], payment: Payment):
        self._order_number = order_number
        self._customer = customer
        self._item_list = item_list
        self._payment = payment