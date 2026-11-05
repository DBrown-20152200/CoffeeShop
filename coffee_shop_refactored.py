"""
Refactored Coffee Shop Ordering System
"""
from coffee_shop_exceptions import *

class MenuItem():
    """The items on the menu and their customisations."""

    #dict of drink sizes and their price multipliers
    drinks_size_multiplier = {"small":1.0,
                            "medium":1.3,
                            "large":1.6
                            }

    def __init__(self, name: str, base_price: float, available_sizes: list):

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
    """Manages customer information."""

    def __init__(self, name: str, member: bool = False):
        self._name = name
        self._is_member = member

class LoyaltyProgram():
    """Manages loyalty points, discounts and redeeming logic."""

    def __init__(self):
        self._account_list = {}

    def add_member(self, customer: Customer, starting_points: int):
        """Adds a new member to the list and starts their points at 0"""

        if customer._is_member == True:
            self._account_list[customer._name] = starting_points

    def apply_member_discount(self, cart: dict):
        """Applies the 10% member discount to loyalty members."""

        for item in cart:
            cart[item] *= 0.9
        return cart

    def earn_points(self, member_name: str, purchase_cost: float):
        """assigns 1 point for every $1 spent"""

        points_earned = round(purchase_cost)
        self._account_list[member_name] = points_earned

    def redeem_points(self, member_name: str, points_to_redeem: int):
        """Checks if member is eligible for a free small drink."""

        if self._account_list[member_name] >= points_to_redeem:

            self._account_list[member_name] -= points_to_redeem
            total_cost = 0.00

            return total_cost
        else:
            raise InsufficientPointsError
        

class Order():
    """Class for creating orders"""

    def __init__(self, customer:Customer):
        self._item_list = {}
        self._total_cost = float()
        self._customer = customer

    def add_item(self, item: MenuItem, size: str):
        """Adds item and its cost to a cart."""

        item.calculate_price(size)
        self._item_list[f"{size} {item._name}"] = item._price

    def calculate_total_cost(self):
        """Calculates total cost of the order."""

        for item in self._item_list:
            self._total_cost += (self._item_list.get(item))