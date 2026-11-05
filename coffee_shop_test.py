import unittest
from coffee_shop_refactored import MenuItem, Order, Customer, LoyaltyProgram
from coffee_shop_exceptions import *

class TestCoffeeShop(unittest.TestCase):

    
    def setUp(self):
            """Set up test fixtures."""
            
            self.latte = MenuItem("Latte", 4.50, ['small', 'medium', 'large'])
            self.cappuccino = MenuItem("Cappuccino", 4.25, ['small', 'medium', 'large'])
            self.espresso = MenuItem("Espresso", 3.50, ['small', 'medium', 'large'])
            self.americano = MenuItem("Americano", 3.75, ['small', 'medium', 'large'])
            self.mocha = MenuItem("Mocha", 5.00, ['small', 'medium', 'large'])

            self.customer = Customer("Alice", member=True)
                    
            self.loyalty = LoyaltyProgram()

        
    def test_menu_item_pricing_small(self):
        """Test MenuItem calculates small drink price correctly."""
            
        self.latte.calculate_price('small')                
        self.assertEqual(self.latte._price, 4.50)

        self.espresso.calculate_price('small')
        self.assertEqual(self.espresso._price, 3.50)

        self.espresso.calculate_price('medium')
        self.assertEqual(self.espresso._price, 4.55)

        
    def test_menu_item_pricing_invalid_size(self):
        """Test MenuItem raises exception for invalid size."""
            
        with self.assertRaises(InvalidCustomizationError):
                    
            self.latte.calculate_price('extra-large')

        
    def test_order_total_with_multiple_items(self):
        """Test Order calculates total correctly."""
            
        order = Order()
                
        self.assertEqual(order._total_cost(), )

        
    def test_member_discount_applied(self):
        """Test member discount is 10%."""
            
        # Add implementation

        
    def test_loyalty_points_earned(self):
        """Test loyalty points: $1 = 1 point."""
            
        # Add implementation

        
    def test_redeem_points_insufficient(self):
        """Test redeeming with insufficient points raises exception."""
            
        with self.assertRaises(InsufficientPointsError):
                
            self.loyalty.redeem_points(self.customer, points_to_redeem=100)

    
# Add more tests as needed

if __name__ == '__main__':    
    unittest.main()