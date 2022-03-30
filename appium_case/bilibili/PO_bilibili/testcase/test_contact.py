from appium_case.bilibili.PO_bilibili.page.app import App


class TestContact:
    def setup(self):
        # 初始化app
        self.app = App()
        self.main = self.app.start().main()

    def test_addcontact(self):
        videopage = self.main.goto_searchpage().search_action().goto_authorspace().\
            down_page().click_on_video().triple()
        assert '三连推荐成功' in videopage.get_toast()

