from requests_project.api.address import Address


class TestAddress:
    def setup(self):
        self.address = Address()

    def test_create(self):
        print(self.address.create("xiaohong", "小红", "15500000000"))

    def test_update(self):
        print(self.address.update("xiaohong", "小红", "15500000002"))

    def test_delete(self):
        print(self.address.delete("xiaohong"))