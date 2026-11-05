"""
Custom exceptions for Coffee Shop Ordering System
"""

class CoffeeShopError(Exception):
    """Base exception for all coffee shop errors."""

    def __init__(self):
        super().__init__()

class OrderError(CoffeeShopError):
    """Base exception for order-related errors."""

    def __init__(self):
        super().__init__()

class InvalidItemError(OrderError):
    """Raised when item doesn't exist on menu."""

    def __init__(self):
        super().__init__()

class InvalidCustomizationError(OrderError):
    """Raised when customization not available."""

    def __init__(self):
        super().__init__()

class PaymentError(CoffeeShopError):
    """Base exception for payment errors."""

    def __init__(self):
        super().__init__()

class InsufficientPointsError(PaymentError):
    """Raised when loyalty points insufficient for redemption."""

    def __init__(self):
        super().__init__()

class InvalidDiscountError(CoffeeShopError):
    """Raised when discount can't be applied."""

    def __init__(self):
        super().__init__()