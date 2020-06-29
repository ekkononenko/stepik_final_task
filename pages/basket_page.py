from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Basket link is not found"

    def should_be_empty_baskets_message(self):
        empty_message = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE).text
        assert "Your basket is empty. Continue shopping" == empty_message, \
            f"Basket should be empty, but {empty_message} is presented"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Items are presented in basket, but should not be"
