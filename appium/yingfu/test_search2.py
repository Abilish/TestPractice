from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


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

    def test_search(self):
        self.driver.find_element(MobileBy.ID, 'tv.danmaku.bili:id/expand_search').click()
        self.driver.find_element(MobileBy.ID, 'tv.danmaku.bili:id/search_src_text').send_keys('天真的和感伤的小说家')
        self.driver.find_element(MobileBy.XPATH, "(//*[@text='天真的和感伤的小说家'])[2]").click()










