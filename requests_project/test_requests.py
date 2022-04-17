import random
import re
import pytest
import requests
from filelock import FileLock

from requests_project.api.wework import WeWork


@pytest.fixture(scope="session")  # fixture会把函数变成可传的变量
def test_token():
    # 保证只访问一次，所著的内容只会访问一次，只有第一个文件解锁后，后面的session才会执行
    while FileLock("session.lock"):
        corpid = 'ww390fdd050d533652'
        corpsecret = 'QiKLgg8vuVkzgSJNENZWjA0SqKQTzCybssFk5ZL89Yo'
        res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
        print(res.text)
        return res.json()["access_token"]

def test_get(userid, test_token):
    USERID = 'zhangsan2'
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token}&userid={userid}")
    return res.json()


def test_create(userid, name, mobile, department, test_token):
    date = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": department,
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token}",
                        json=date)
    return res.json()


def test_update(userid, name, mobile, test_token):
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token}",
                        json=data)
    return res.json()


def test_delete(userid, test_token):
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token}&userid={userid}")
    return res.json()


def test_create_data():
    '''正常的参数化，用于数据生成'''
    # # 1.采用时间种子生成的随机数
    # data = [(str(random.randint(0, 999999)),
    #          "zhangsan",
    #          str(random.randint(13800000000, 13899999999)),
    #          1
    #          ) for x in range(10)]  # 列表生成器
    # # 不可使用并发，使用时间种子，如果并行那么会发生错误，时间相同造成重复

    # 2. 思路二，可用并发
    data = [("ww123fff" + str(x), "zhangsan", "138%08d" % x, 1) for x in range(10)]
    return data


# @pytest.mark.parametrize("userid, name, mobile, department", [('xiaolan', '小兰', '13500000000', 1)])
@pytest.mark.parametrize("userid, name, mobile, department", test_create_data())
def test_all(userid, name, mobile, department, test_token):
    try:
        assert 0 == test_create(userid, name, mobile, department, test_token)["errcode"]
    except AssertionError as e:
        if "mobile existed" in e.__str__():
            # __str__内置变量，print打印操作一般会调用__str__，
            # __repr__可能会打印非常详细的信息，__str__只会打印异常信息
            re_userid = re.findall(":(.*)'$", e.__str__())[0]
            if re_userid.endswith("'") or re_userid.endswith('"'):
                re_userid = re_userid[:-1]
            assert "deleted" == test_delete(userid, test_token)['errmsg']
            assert 60111 == test_get(re_userid, test_token)['errcode']
            assert 0 == test_create(userid, name, mobile, department, test_token)["errcode"]

    assert name == test_get(userid, test_token)["name"]
    assert "updated" == test_update(userid, "xxxxxxx", mobile, test_token)["errmsg"]
    assert "xxxxxxx" == test_get(userid, test_token)['name']
    assert "deleted" == test_delete(userid, test_token)['errmsg']
    assert 60111 == test_get(userid, test_token)['errcode']


def test_session():
    s = requests.Session()
    s.params = {
        "access_token": WeWork().get_token('QiKLgg8vuVkzgSJNENZWjA0SqKQTzCy')  # 去掉了一部分我的token，填入自己的token就行
    }

    res = s.get("https://qyapi.weixin.qq.com/cgi-bin/user/get?userid=xiaohong")
    print(res.json())