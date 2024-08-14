import requests
from cfg import baseurl, proxies, headers
import json
from utils.login import login_instance


class dept:
    def __init__(self):
        self.deptURL = baseurl + "depts/"
        self.token = login_instance.defaultLogin()
        self.headers = headers
        self.headers["token"] = self.token

    def searchDept(self):
        # 部门查询
        response = requests.get(self.deptURL, proxies=proxies, headers=self.headers).json()
        return response

    def searchIdDept(self, id):
        # 根据id查询部门
        if id is not None:
            url = self.deptURL + str(id)
            response = requests.get(url=url, proxies=proxies, headers=self.headers).json()
        else:
            response = requests.get(url=self.deptURL, proxies=proxies, headers=self.headers).json()
        return response

    def addDept(self, data):
        # 添加部门
        response = requests.post(self.deptURL, data=json.dumps(data), proxies=proxies, headers=self.headers).json()
        return response

    def updateDept(self, data):
        # 修改部门
        response = requests.put(self.deptURL, data=json.dumps(data), proxies=proxies, headers=self.headers).json()
        return response

    def deleteDept(self, id):
        # 删除部门
        url = self.deptURL + str(id)
        response = requests.delete(url=url, proxies=proxies, headers=self.headers).json()
        return response


dept_instance = dept()

if __name__ == "__main__":
    print(dept_instance.searchDept())
    print(dept_instance.searchIdDept(1))
    # print(dept_instance.addDept("大不了部"))
    # print(dept_instance.updateDept(11, "好好部"))
    print(dept_instance.deleteDept(11))
