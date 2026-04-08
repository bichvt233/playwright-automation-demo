import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from test_data.users import STANDARD_USER, LOCKED_OUT_USER, INVALID_USER

def test_successful_login(page: Page):
    """Test login with valid credentials"""
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    
    login_page.navigate()
    login_page.login(STANDARD_USER["username"], STANDARD_USER["password"])
    
    assert inventory_page.is_loaded()
    assert inventory_page.get_product_count() == 6

def test_invalid_login(page: Page):
    """Test login with invalid credentials"""
    login_page = LoginPage(page)
    
    login_page.navigate()
    login_page.login(INVALID_USER["username"], INVALID_USER["password"])
    
    assert "Epic sadface" in login_page.get_error_message()

def test_locked_out_user(page: Page):
    """Test login with locked out user"""
    login_page = LoginPage(page)
    
    login_page.navigate()
    login_page.login(LOCKED_OUT_USER["username"], LOCKED_OUT_USER["password"])
    
    assert "locked out" in login_page.get_error_message()