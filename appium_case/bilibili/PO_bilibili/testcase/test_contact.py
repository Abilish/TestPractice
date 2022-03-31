from appium_case.bilibili.PO_bilibili.page.app import App
from hamcrest import *


class TestContact:
    def setup(self):
        # 初始化app
        self.app = App()
        self.main = self.app.start().main()

    def test_addcontact(self):
        '''测试一键三连功能'''
        videopage = self.main.goto_searchpage().search_action().goto_authorspace().\
            down_page().click_on_video().triple()
        assert '三连推荐成功' in videopage.get_toast()

    def test_comment(self):
        comment = self.main.goto_searchpage().search_action().goto_authorspace().\
            down_page().click_on_video().comments()
        # resault = '发送成功'
        # assert_that(resault, equal_to(comment.get_toast()), '判断评论是否发送成功')
        assert '发送成功' in comment.get_toast()



