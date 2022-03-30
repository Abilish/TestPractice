from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
# 简单的一个demo
desired_caps={
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

driver.find_element(By.ID, 'com.olg.olg:id/tvMainSearch').click()
# driver.find_element(MobileBy.ID, 'com.olg.olg:id/tvMainSearch').click()  # appium在selenium的By上扩展的MobileBy方法
driver.find_element(By.ID, 'com.olg.olg:id/et_search').send_keys('BABA')
driver.back()

driver.quit()
