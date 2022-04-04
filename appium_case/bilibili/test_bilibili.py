from time import sleep

from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestBiliBili:
    def setup(self):
        desired_caps = {
            "platformName": 'Android',
            "platformVerdion": '5.1.1',
            "deviceName": '192.168.0.101:5555',
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

    def test_search(self):
        self.driver.find_element(AppiumBy.ID, 'tv.danmaku.bili:id/expand_search').click()
        self.driver.find_element(AppiumBy.ID, 'tv.danmaku.bili:id/search_src_text').send_keys('天真的和感伤的小说家')
        self.driver.find_element(AppiumBy.XPATH, "(//*[@text='天真的和感伤的小说家'])[2]").click()
        self.driver.find_element(AppiumBy.ID, "tv.danmaku.bili:id/up_title").click()

        sleep(2)

        # 向下滑动up主主页
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()  # 获取当前窗口x、y
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()

        # 点击屏幕中显示的第二个视频（定位的标题） ，这里不直接定位名字，否则up发布新视频后会很难定位，还要再修改脚本
        # 待改进：不同设备下的resourse-id是可能会变得，用父子关系定位class属性
        self.driver.find_element(AppiumBy.XPATH, "(//*[@resource-id='tv.danmaku.bili:id/title'])[2]").click()

        # 一键三连
        # 思路：先找到点赞按钮的坐标，然后使用TouchAction进行长按操作
        # 1、获取坐标
        sleep(2)  # 先暂用sleep吧，把整个流程跑通了再优化
        like_element = self.driver.find_element(AppiumBy.ID, 'tv.danmaku.bili:id/recommend_icon')
        l_position= like_element.get_attribute("bounds")
        l_position = l_position.replace("][", ',').replace("[", '').replace("]", '').split(',')
        print(l_position)
        x = int((int(l_position[0])+int(l_position[2])) * 0.5)
        y = int((int(l_position[1])+int(l_position[3])) * 0.5)
        print(x, y)        # # action = TouchAction(self.driver)

        # 这两种方法都可以长按：短按+wait/长按，不过TouchAction已被弃用了
        action.long_press(x=x, y=y, duration=2000).release().perform()
        # action.press(x=x, y=y).wait(4000).release().perform()


        # 判断toast，不完整
        aaa = self.driver.find_element(AppiumBy.XPATH, "//*[@class='android.widget.Toast']").text





















