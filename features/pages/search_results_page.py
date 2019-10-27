from selenium.webdriver.common.by import By

from features.pages.topic_page import TopicPage


# Inherits from TopicPage
class SearchResultsPage(TopicPage):
    FIELD_SEARCH = (By.XPATH, "//*[@id='searchText']/input")

    def _verify_page(self):
        self.on_this_page(self.FIELD_SEARCH)
