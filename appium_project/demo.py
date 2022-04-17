from appium import webdriver


desired_caps={
    "platformName": 'Android',
    "platformVerdion": '5.1.1',
    "deviceName": '192.xxx.x.xxx:5555',
    "appPackage" 'com.android.settings'
    "appActivity": 'com.android.settings.Settings'
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.quit()
