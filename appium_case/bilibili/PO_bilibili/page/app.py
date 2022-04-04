from appium import webdriver

from appium_case.bilibili.PO_bilibili.page.base_page import BasePage
from appium_case.bilibili.PO_bilibili.page.main import Main


class App(BasePage):
    def start(self):
        if self._driver == None:
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
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        else:
            self._driver.launch_app()
            # self.driver.start_activity(app_package= , app_activity= )
            # start该方法也能启动，但需要提供包名等，lunch会自动搜索已存在的app_package和app_activity

        self._driver.implicitly_wait(6)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        return Main(self._driver)