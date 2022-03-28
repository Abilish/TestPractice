from appium import webdriver


class TestYingFu:
    def setup_class(self):
        desired_caps = {
            "platformName": 'Android',
            "platformVerdion": '5.1.1',
            "deviceName": '192.xxx.x.xxx:5555',
            "appPackage": 'com.olg.olg',
            "appActivity": 'com.olg.olg.ui.guide.StartActivity',
            "noReset": True,
            "dontStopAppOnReset": True,
            "skipDeviceInitialization": True
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.implicitly_wait(10)

    def teardown_class(self):
        self.driver.quit()

    def setup(self):
        pass

    def teardown(self):
        pass