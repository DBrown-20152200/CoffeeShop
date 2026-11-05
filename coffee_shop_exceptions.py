"""
Custom exceptions for Coffee Shop Ordering System
"""

class CoffeeShopError(Exception):
    """Base exception for all coffee shop errors."""
    def __init__(self):
        message = "Error, please try again."
        super().__init__(message)

class OrderError(CoffeeShopError):
    """Base exception for order-related errors."""
    pass

class InvalidItemError(OrderError):
    """Raised when item doesn't exist on menu."""
    def __init__(self):
        message = "Item is not in the menu"
        super().__init__(message)

class InvalidCustomizationError(OrderError):
    """Raised when customization not available."""
    pass

class PaymentError(CoffeeShopError):
    """Base exception for payment errors."""
    pass

class InsufficientPointsError(PaymentError):
    """Raised when loyalty points insufficient for redemption."""
    pass

class InvalidDiscountError(PaymentError):
    """Raised when discount can't be applied."""
    pass