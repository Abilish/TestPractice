from time import sleep

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

from appium_case.bilibili.PO_bilibili.page.base_page import BasePage


class VideoDetails(BasePage):
    def triple(self):
        '''一键三连'''
        # 一键三连
        # 思路：先找到点赞按钮的坐标，然后使用TouchAction进行长按操作
        # 1、获取坐标
        sleep(2)  # 先暂用sleep吧，把整个流程跑通了再优化
        like_element = self.find(AppiumBy.ID, 'tv.danmaku.bili:id/recommend_icon')
        l_position= like_element.get_attribute("bounds")
        l_position = l_position.replace("][", ',').replace("[", '').replace("]", '').split(',')
        print(l_position)
        x = int((int(l_position[0])+int(l_position[2])) * 0.5)
        y = int((int(l_position[1])+int(l_position[3])) * 0.5)
        action = TouchAction(self._driver)

        # 这两种方法都可以长按：短按+wait/长按，不过TouchAction已被弃用了
        action.long_press(x=x, y=y, duration=2000).release().perform()
        # action.press(x=x, y=y).wait(4000).release().perform()

        return self

    def get_toast(self):
        '''toast验证一键三连是否成功'''
        return self.find(AppiumBy.XPATH, "//*[@class='android.widget.Toast']").text
        # return 'toast'

    def comments(self, comment):
        '''评论视频'''
        self.find(AppiumBy.ID, "tv.danmaku.bili:id/tab_sub_title").click()
        self.find(AppiumBy.ID, "tv.danmaku.bili:id/input").click()
        # self.find(AppiumBy.ID, "tv.danmaku.bili:id/edit").send_keys('举头望明月，低头两片瓦')
        self.find(AppiumBy.ID, "tv.danmaku.bili:id/edit").send_keys(f'{comment}')
        self.find(AppiumBy.ACCESSIBILITY_ID, '发布，按钮').click()
        return self

    def full_screen(self):
        '''全屏观看视频'''
        return self

    def send_barrage(self):
        '''发送弹幕'''
        return self

    # def back_to_main(self):
    #     self._driver.back()
