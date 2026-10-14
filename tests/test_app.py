import pathlib
import unittest

PROJECT = pathlib.Path(__file__).resolve().parents[1]
HTML_FILE = PROJECT / "site" / "index.html"


class FoodDeliveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = HTML_FILE.read_text(encoding="utf-8")

    def test_page_title(self):
        self.assertIn("<title>Food Delivery App</title>", self.html)

    def test_restaurants(self):
        self.assertIn("Pizza Palace", self.html)
        self.assertIn("Burger House", self.html)

    def test_menu_prices(self):
        self.assertIn("₹199", self.html)
        self.assertIn("₹99", self.html)

    def test_cart(self):
        self.assertIn('id="items"', self.html)
        self.assertIn('id="total"', self.html)

    def test_order_function(self):
        self.assertIn("function placeOrder()", self.html)

    def test_add_item_function(self):
        self.assertIn("function addItem(", self.html)


if __name__ == "__main__":
    unittest.main()