import pytest
from lib.LoadExceldata import LoadSearchData, LoadAddData
from lib.emp import emp_instance
import cv2
from io import BytesIO
import requests
import numpy as np


search_testData = LoadSearchData("searchemp")

# total为查询到符合条件的记录总数量，row为返回的记录数量
@pytest.mark.parametrize('testcase, params, code, msg, total, row', search_testData)
# 员工列表查询
def test_emp001_027(testcase, params, code, msg, total, row):
    print(params)
    response = emp_instance.searchEmp(params)
    assert response["code"] == code
    assert response["msg"] == msg
    if code != 0:
        assert response["data"]["total"] == total
        assert len(response["data"]["rows"]) == row


@pytest.mark.parametrize('testcase, id, code, msg, data', [
    ("emp_028", "1", 1, "success", 1),
    ("emp_029", "50", 1, "success", None),
    ("emp_030", "18,19", 0, "fail", None),
    ("emp_031", "b", 0, "fail", None),
])
# 根据ID查询员工信息
def test_emp_028_031(testcase, id, code, msg, data):
    response = emp_instance.searchIdEmp(id)
    assert response["code"] == code
    assert response["msg"] == msg
    if code == 1:
        if data is None:
            assert response["data"] == data
        else:
            assert response["data"]["id"] == data


add_testData = LoadAddData("addemp")


# total为查询到符合条件的记录总数量，row为返回的记录数量
@pytest.mark.parametrize('testcase, body, code, msg, data', add_testData)
# 添加员工
def test_emp_032_54(testcase, body, code, msg, data):
    response = emp_instance.addEmp(body)
    assert response["code"] == code
    assert response["msg"] == msg
    print(response["data"])


update_testData = LoadAddData("updateemp")
@pytest.mark.parametrize('testcase, body, code, msg, data', update_testData)
# 修改员工
def test_emp_055_133(testcase, body, code, msg, data):
    response = emp_instance.updateEmp(body)
    assert response["code"] == code
    assert response["msg"] == msg
    if code:
        actual_data = emp_instance.searchIdEmp(body["data"]["id"])

        # 遍历 body 中的所有键值对，检查它们是否与 actual_data 中的对应值一致
        for key, value in body.items():
            assert actual_data[key] == value, f"Expected {key} to be {value}, but got {actual_data[key]} instead."


@pytest.mark.parametrize('testcase, ids, code, msg', [
    ("emp_134", "32", 1, "success"),
    ("emp_135", "15,16", 1, "success"),
    ("emp_136", "50", 0, "fail"),
    ("emp_137", "10,51", 0, "fail"),
    ("emp_138", "a", 0, "fail"),
])
# 删除员工
def test_emp_134_138(testcase, ids, code, msg):
    response = emp_instance.deleteEmp(ids)
    assert response["code"] == code
    assert response["msg"] == fail
    if code:
        assert emp_instance.searchIdEmp(body["id"]) is None


@pytest.mark.parametrize('testcase, file, code, msg', [
    ("emp_139", r"C:\Users\chizuru\Desktop\test.jpg", 1, "success"),
    ("emp_140", r"test.txt", 1, "success"),
    ("emp_141", r"test1.jpg", 0, "fail"),
    ("emp_142", None, 0, "fail"),
    ("emp_143", "test2.jpg", 0, "fail"),
])
def test_emp_139_143(testcase, file, code, msg):
    response = emp_instance.uploadImg(file)
    assert response["code"] == code
    assert response["msg"] == msg
    if code:
        actual_image = cv2.imread(file)

        # 下载并读取服务器返回的图片
        response_image = requests.get(response["data"])
        image_stream = BytesIO(response_image.content)
        expect_image = cv2.imdecode(np.frombuffer(image_stream.read(), np.uint8), cv2.IMREAD_COLOR)

        # 使用 numpy 进行图像数组比较
        assert np.array_equal(actual_image, expect_image)


