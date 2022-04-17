from requests_project.api.address import Address
import allure


@allure.feature("用户功能点报告")
class TestAddress:
    def setup(self):
        self.address = Address()

    @allure.story("获取token")
    def test_token(self):
        '''一个会失败的测试用例，用来练习生成测试报告'''
        print(self.address.get_token())

    @allure.story("创建用户")
    def test_create(self):
        print(self.address.create("xiaohong", "小红", "15500000000"))

        with allure.step("创建用户"):
            allure.attach("创建用户1", "我也不知道写什么好1")
            allure.attach("创建用户2", "我也不知道写什么好2")
            allure.attach("创建用户3", "我也不知道写什么好3")

    @allure.story("更新用户信息")
    def test_update(self):
        print(self.address.update("xiaohong", "小红", "15500000002"))

    @allure.story("删除用户")
    def test_delete(self):
        print(self.address.delete("xiaohong"))


# 将函数作为一个步骤，调用此函数时，报告中输出一个步骤，步骤名称通常时函数名，这样的函数通常称为步骤函数
@allure.step("用户登录")
def login(user, passwd):
    if user == "crisimple" and passwd == "123456":
        print(user, passwd)
        print("登录成功")
    else:
        print(user, passwd)
        print("登录失败，请重新尝试")