import requests
from cfg import baseurl, proxies, headers
import json


class login:
    def __init__(self):
        self.token = ""
        self.loginURL = baseurl + "login"

    def userLogin(self, data):
        response = requests.post(self.loginURL, data=json.dumps(data), proxies=proxies, headers=headers).json()
        return response

    # 返回使用默认账户登录的token
    def defaultLogin(self):
        data = {
            "username": "jinyong",
            "password": "123456"
        }
        response = requests.post(self.loginURL, data=json.dumps(data), proxies=proxies, headers=headers)
        response = response.json()
        return response["data"]


login_instance = login()

if __name__=='__main__':
    # print(login_instance.userLogin("jinyong", "123456"))
    print(login_instance.defaultLogin())
