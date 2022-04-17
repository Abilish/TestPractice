import pytest

from appium_project.bilibili.PO_bilibili.page.app import App
from hamcrest import *
import yaml


class TestAddcontact:
    def setup(self):
        # 初始化app
        self.app = App()
        self.main = self.app.start().main()

    def test_addcontact(self):
        '''测试一键三连功能'''
        videopage = self.main.goto_searchpage().search_action().goto_authorspace().\
            down_page().click_on_video().triple()
        assert '三连推荐成功' in videopage.get_toast()

class TestComment:
    def setup(self):
        # 初始化app
        self.app = App()
        self.main = self.app.start().main()

    @pytest.mark.parametrize("comment", yaml.safe_load(open("../datas/comment.yaml", encoding='UTF-8')))
    def test_comment(self, comment):
        '''测试评论功能'''
        input_comment = self.main.goto_searchpage().search_action().goto_authorspace().\
            down_page().click_on_video().comments_v()
        for c in comment:
            input_comment = input_comment.comments_v(comment)
            result_c = '发送成功'
            assert_that(result_c, equal_to(input_comment.get_toast()), '判断评论是否发送成功')
        # assert '发送成功' in comment.get_toast()



