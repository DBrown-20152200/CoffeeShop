"""
Refactored Coffee Shop Ordering System
"""

class MenuItem():
    def __init__(self, name: str, size: str, milk: str, cream: bool):        
        self._name = name
        self._size = size
        self._milk = milk
        self._cream = cream

class LoyaltyProgram():
    def __init__(self, account_number: int, points_total: int, phone_number: int, email: str):
        self._account_number = account_number
        self._points_total = points_total
        self._phone_number = phone_number
        self._email = email

class Customer():
    def __init__(self, name: str, loyalty_account: LoyaltyProgram, staff_status: bool):
        self._name = name
        self._loyalty_account = loyalty_account
        self._is_staff = staff_status

class Payment():
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