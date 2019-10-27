from selenium.webdriver.common.by import By

from features.pages.topic_page import TopicPage


# Inherits from TopicPage
class MainPage(TopicPage):
    BANNER_TOP = (By.ID, "mp-topbanner")

    def _verify_page(self):
        self.on_this_page(self.BANNER_TOP)
