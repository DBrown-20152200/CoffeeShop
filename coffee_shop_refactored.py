"""
Refactored Coffee Shop Ordering System
"""
from coffee_shop_exceptions import *

class MenuItem():
    """The items on the menu and their customisations"""

    #dict of drink sizes and their price multipliers
    drinks_size_multiplier = {"small":1.0,
                            "medium":1.3,
                            "large":1.6
                            }

    def __init__(self, name: str, base_price: float, available_sizes: list):
        """Initialises MenuItem"""

        self._name = name
        self._base_price = base_price
        self._available_sizes = available_sizes
        self._price = 0.00

    def calculate_price (self, size: str):
        """Calculates the item price after all selections are made."""

        if size in self._available_sizes:
            self._price = self._base_price * self.drinks_size_multiplier.get(size)
        else:
            raise InvalidCustomizationError

class Customer():
    """Manages customer information"""

    staff_list = []

    def __init__(self, name: str, member: bool = False):
        self._name = name
        self._is_member = member

class LoyaltyProgram():
    """Manages loyalty points and discounts."""

    loyalty_discount = 0.10
    points_redeem_threshold = 100
    
    loyalty_account_list = {}

    def __init__(self):
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

class Order():
    """Class for creating orders"""

    def __init__(self):
        self._order_number = int()
        self._item_list = []
        self._payment = str()
        self._total_cost = 0.00

    def add_item(self, item: MenuItem):
        self._item_list.append(item)

    def calculate_total_cost(self):
        for items in self._item_list:
            self._total_cost += items._price