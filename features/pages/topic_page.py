from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


# Inherits form BasePage
class TopicPage(BasePage):
    TITLE_TOPIC = (By.ID, "firstHeading")
    PANEL_LEFT = (By.ID, "mw-panel")
    FIELD_SEARCH = (By.ID, "searchInput")
    BUTTON_SEARCH = (By.ID, "searchButton")
    LINK_USERNAME = (By.XPATH, "//li[@id='pt-userpage']/a")

    # verify if elements are displayed on the page initially
    def _verify_page(self):
        self.on_this_page(self.BUTTON_SEARCH, self.FIELD_SEARCH)

    def search_for(self, query):
        self.type_in(self.FIELD_SEARCH, query)
        self.click_on(self.BUTTON_SEARCH)

    def get_topic_title(self):
        return self.get_text(self.TITLE_TOPIC)

    def get_username(self):
        return self.get_text(self.LINK_USERNAME)
