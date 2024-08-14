import requests
from cfg import baseurl, proxies, headers
import json
from utils.login import login_instance
import mimetypes
import os
import math


class emp:
    def __init__(self):
        self.epmURL = baseurl + "emps/"
        self.token = login_instance.defaultLogin()
        self.headers = headers
        self.headers["token"] = self.token

    def searchEmp(self, params):
        # 查询员工
        if isinstance(params, float):
            response = requests.get(url=self.epmURL, proxies=proxies, headers=self.headers).json()
        else:
            url = self.epmURL + params
            response = requests.get(url=url, proxies=proxies, headers=self.headers).json()
        return response

    def searchIdEmp(self, id):
        # 根据id查询员工
        url = self.epmURL + str(id)
        response = requests.get(url=url, proxies=proxies, headers=self.headers).json()
        return response

    def addEmp(self, data):
        # 添加员工
        response = requests.post(url=self.epmURL, data=json.dumps(data), proxies=proxies, headers=self.headers).json()
        return response

    def updateEmp(self, data):
        # 更新员工
        response = requests.put(url=self.epmURL, data=json.dumps(data), proxies=proxies, headers=self.headers).json()
        return response

    def deleteEmp(self, ids):
        # 根据id删除员工
        url = self.epmURL + str(ids)
        response = requests.delete(url=url, proxies=proxies, headers=self.headers)
        return response

    def uploadImg(self, file_path):
        uploadURL = baseurl + "upload"

        headers = {
            "token": self.token
        }

        # 从文件路径中提取文件名
        file_name = os.path.basename(file_path)

        print(f"Uploading {file_name} to {uploadURL}")

        # 使用 `with` 确保文件在使用完毕后关闭
        with open(file_path, 'rb') as file:
            files = {
                'image': (file_name, file, 'image/jpeg')
            }
            response = requests.post(url=uploadURL, proxies=proxies, headers=headers, files=files).json()

        return response


emp_instance = emp()

if __name__ == "__main__":
    params = '{"page":1}'

    print(emp_instance.searchEmp(params))
    # print(emp_instance.uploadImg(r"C:\Users\chizuru\Desktop\test.jpg"))

