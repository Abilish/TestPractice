from appium.webdriver.common.appiumby import AppiumBy

from appium_case.bilibili.PO_bilibili.page.authorspace import AuthorSpace
from appium_case.bilibili.PO_bilibili.page.base_page import BasePage


class SearchPage(BasePage):
    def search_action(self):
        self._driver.find_element(AppiumBy.ID, 'tv.danmaku.bili:id/search_src_text').send_keys('天真的和感伤的小说家')
        self._driver.find_element(AppiumBy.XPATH, "(//*[@text='天真的和感伤的小说家'])[2]").click()
        return self

    def goto_authorspace(self):
        '''跳转到up主首页'''
        self._driver.find_element(AppiumBy.ID, "tv.danmaku.bili:id/up_title").click()
        return AuthorSpace(self._driver)

    def other_action(self):
        pass
