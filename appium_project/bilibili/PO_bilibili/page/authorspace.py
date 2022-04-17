from time import sleep

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

from appium_project.bilibili.PO_bilibili.page.base_page import BasePage
from appium_project.bilibili.PO_bilibili.page.videodetails import VideoDetails


class AuthorSpace(BasePage):
    def down_page(self):
        sleep(2)

        # 向下滑动up主主页
        action = TouchAction(self._driver)
        window_rect = self._driver.get_window_rect()  # 获取当前窗口x、y
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()
        return self

    def click_on_video(self):
        self.find(AppiumBy.XPATH, "(//*[@resource-id='tv.danmaku.bili:id/title'])[2]").click()
        return VideoDetails(self._driver)
