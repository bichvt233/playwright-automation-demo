from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.page_title = page.locator("span.title")
        self.product_items = page.locator(".inventory_item")
    
    def is_loaded(self) -> bool:
        return self.page_title.is_visible()
    
    def get_product_count(self) -> int:
        return self.product_items.count()