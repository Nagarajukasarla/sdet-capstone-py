from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class WordPressPage:

    def __init__(self, driver):
        self.driver = driver

    headerNav = (By.XPATH, "//ul[@aria-label='Main']") 
    download_extend = (By.XPATH, "./li[4]") #considering header as context
    themes = (By.XPATH, "//ul[@aria-label='Main']//a[contains(@href,'themes')]") #considering header as context


    def open_site(self):
        self.driver.get("https://wordpress.org/")

    def get_title(self):
        return self.driver.title

    def hover_download_extend(self):
        header = self.driver.find_element(*self.headerNav)
        element = header.find_element(*self.download_extend)

        ActionChains(self.driver).move_to_element(element).perform()

    def click_themes(self):
        header = self.driver.find_element(*self.headerNav)
        header.find_element(*self.download_extend).click()
        header.find_element(*self.themes).click()
