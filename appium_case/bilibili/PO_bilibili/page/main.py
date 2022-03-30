from appium.webdriver.common.appiumby import AppiumBy

from appium_case.bilibili.PO_bilibili.page.base_page import BasePage
from appium_case.bilibili.PO_bilibili.page.search_page import SearchPage


class Main(BasePage):
    def goto_searchpage(self):
        '''“搜索”页面'''
        self._driver.find_element(AppiumBy.ID, 'tv.danmaku.bili:id/expand_search').click()
        return SearchPage(self._driver)

    def goto_dynamic(self):
        '''”动态“页面'''
        pass

    def goto_clubno(self):
        '''“会员购”页面'''
        pass

    def goto_my(self):
        '''”我的“页面'''
        pass

