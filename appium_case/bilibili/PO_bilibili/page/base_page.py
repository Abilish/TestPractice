from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _black_list = [
        (By.XPATH, "//*[@text='确认']"),
        (By.XPATH, "//*[@text='下次再说']"),
        (By.XPATH, "//*[@text='确定']"),
    ]
    def __init__(self, driver:WebDriver = None):
        self._driver = driver

    def find(self, locator, value:str=None):
        element:WebElement
        # 弹框处理，如果找到了元素就返回，否则捕获异常
        try:
            if isinstance(locator, tuple):
                element = self._driver.find_element(*locator)  # 解元组
            else:
                element = self._driver.find_element(locator, value)
            return element
        except:
            for ele in self._black_list:
                elelist = self._driver.find_elements(*ele)
