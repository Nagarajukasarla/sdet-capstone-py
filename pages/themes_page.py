from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class ThemesPage:

    def __init__(self, driver):
        self.driver = driver

    # locators
    search_box = (By.XPATH, "//input[@placeholder='Search themes']")
    theme_title = (By.XPATH, "//main//h1")

    def open_site(self):
        self.driver.get("https://wordpress.org/themes/")

    # search themes
    def search_theme(self, theme):

        search = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(self.search_box)
        )

        search.clear()
        search.send_keys(theme)
        search.send_keys(Keys.ENTER)

    def get_theme_title(self):

        WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(self.theme_title)
        )

        element = self.driver.find_element(*self.theme_title)

        title = element.text

        return "results" in title.lower()