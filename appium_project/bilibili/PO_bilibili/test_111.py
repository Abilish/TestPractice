from time import sleep

from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.actions.pointer_actions import PointerActions


class TestBiliBili:
    def setup(self):
        desired_caps = {
            "platformName": 'Android',
            "platformVerdion": '5.1.1',
            "deviceName": '192.xxx.x.xxx:5555',
            "appPackage": 'tv.danmaku.bili',
            "appActivity": '.MainActivityV2',
            "noReset": True,
            "dontStopAppOnReset": True,
            "skipDeviceInitialization": True,
            "skipServerInstallation": True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()


    def test_case(self):
        # action = ActionBuilder(self.driver)
        action = PointerActions(self.driver)
        window_rect = self.driver.get_window_rect()  # 获取当前窗口x、y
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        action.pointer_down(button=[x1, y_start])
        action.move_to(x=x1, y=y_end)
        action.pointer_up()
        # action.pointer_action.pointer_down(button=[x1, y_start])



