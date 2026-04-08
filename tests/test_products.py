from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from test_data.users import STANDARD_USER

def test_product_count(page: Page):
    """Test that 6 products are displayed"""
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    
    login_page.navigate()
    login_page.login(STANDARD_USER["username"], STANDARD_USER["password"])

    assert inventory_page.is_loaded()
    assert inventory_page.get_product_count() == 6