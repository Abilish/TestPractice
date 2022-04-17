from requests_project.api.base_api import BaseApi


class WeWork(BaseApi):
    def get_token(self, secrete):
        corpid = 'ww390fdd05'
        corpsecret = 'QiKLgg8vuVkzgSJNENZWjA0SqKQTzC'   # 这两处都有删减，在企业微信上看接口文档替换成自己的就可以
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }
        # print(self.send(**data))
        return self.send(data)["access_token"]