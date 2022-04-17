# 用于获取标签
import pytest
import requests

from requests_project.api.base_api import BaseApi
from requests_project.api.wework import WeWork


class Address(BaseApi):
    def __init__(self):
        secrete = 'QiKLgg8vuVkzgSJNENZWjA0SqK'
        self.token = WeWork().get_token(secrete)

    # @pytest.fixture(scope="session")  # fixture会把函数变成可传的变量
    # def get_token(self):
    #     corpid = 'ww390fdd050d533652'
    #     corpsecret = 'QiKLgg8vuVkzgSJNENZWjA0SqKQTzCybssFk5ZL89Yo'
    #     data = {
    #         "method": "get",
    #         "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
    #         "params": {
    #             "corpid": corpid,
    #             "corpsecret": corpsecret
    #         }
    #     }
    #     # print(self.send(**data))
    #     return self.send(data)["access_token"]
    #     # 为什么要进行解析，解字典呢？


    def create(self, userid, name, mobile):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {
                "access_token": self.token
            },
            "json": {
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": [1],
            }
        }
        return self.send(data)


    def update(self, userid, name, mobile):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "params": {
                "access_token": self.token
            },
            "json": {
                "userid": userid,
                "name": name,
                "mobile": mobile,
            }
        }
        return self.send(data)

    def delete(self, userid):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params": {
                "access_token": self.token,
                "userid": userid
            }
        }
        return self.send(data)













