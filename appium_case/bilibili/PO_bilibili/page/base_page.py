from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
import logging


class BasePage:
    logging.basicConfig(level=logging.INFO)
    _black_list = [
        (By.XPATH, "//*[@text='确认']"),  # 优化：文字+弹框属性定位
        (By.XPATH, "//*[@text='下次再说']"),
        (By.XPATH, "//*[@text='确定']"),
    ]
    _max_num = 3
    _error_num = 0

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value: str = None):   # 元素找到之后，点击之前如果出现弹框？无法处理
        logging.info(locator)
        logging.info(value)
        element: WebElement
        # 弹框处理，如果找到了元素就返回，否则找到弹框就捕获异常
        try:
            # element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(locator, value)
            if isinstance(locator, tuple):
                element = self._driver.find_element(*locator)  # 解元组
            else:
                element = self._driver.find_element(locator, value)
            self._error_num = 0       # 找到后将错误数量归零，否则下一次查找会继续使用上一个错误的次数
            self._driver.implicitly_wait(10)  # 查找到之后再将隐式等待设置回初始值
            return element
        except Exception as e:
            self._driver.implicitly_wait(1)  # 加快查找速度
            if self._error_num > self._max_num:
                raise e
            self._error_num += 1
            for ele in self._black_list:
                logging.info(ele)
                elelist = self._driver.find_elements(*ele)  # 找不到也不会抛异常
                if len(elelist) > 0:
                    elelist[0].click()
                    return self.find(locator, value)  # 自己调用自己通过设置次数来避免死循环
            raise e

    def find_and_get_text(self, locator, value: str = None):  # 元素找到之后，点击之前出现弹框的处理办法
        element_text: WebElement
        # 弹框处理，如果找到了元素就返回，否则找到弹框就捕获异常
        try:
            # element_text = self._driver.find_element(*locator).text if isinstance(locator, tuple) else self._driver.find_element(locator, value)
            if isinstance(locator, tuple):
                element_text = self._driver.find_element(*locator).text  # 解元组
            else:
                element_text = self._driver.find_element(locator, value)
            self._error_num = 0  # 找到后将错误数量归零，否则下一次查找会继续使用上一个错误的次数
            self._driver.implicitly_wait(10)  # 查找到之后再将隐式等待设置回初始值
            return element_text
        except Exception as e:
            self._driver.implicitly_wait(1)  # 加快查找速度
            if self._error_num > self._max_num:
                raise e
            self._error_num += 1
            for ele in self._black_list:
                elelist = self._driver.find_elements(*ele)  # 找不到也不会抛异常
                if len(elelist) > 0:
                    elelist[0].click()
                    return self.find_and_get_text(locator, value)  # 自己调用自己通过设置次数来避免死循环
            raise e
