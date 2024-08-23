import pytest
from selenium.webdriver.common.by import By

import cv2
from io import BytesIO
import requests
import numpy as np

from lib.emp import emp_ui
from lib.login import login_ui
from lib.LoadExceldata import *

search_testData = LoadSearchData("searchemp")
add_testData = LoadExcelData("addemp")
update_testData = LoadExcelData("updateemp")


class Test_emp:
    # 查询员工
    @pytest.mark.parametrize('testcase, emp_data, total, row', search_testData)
    def test_UI_emp_001_007(self, testcase, emp_data, total, row):
        emp_ui.SearchEmp(emp_data["name"], emp_data["gender"], emp_data["start"], emp_data["end"])

        # 判断查询结果的总数量
        total_text = login_ui.wd.find_element(By.XPATH, '//div[@class="row"]/div').text
        assert str(total) in total_text

        # 判断第一页结果的查询数量
        expected_row = len(login_ui.wd.find_elements(By.XPATH, '//tbody/tr'))
        assert expected_row == row

    # 新增员工文件上传
    @pytest.mark.parametrize('testcase, image, data', [
        ("UI_emp_008", {"image": r"C:\Users\chizuru\Desktop\test.jpg"}, ""),
        ("UI_emp_010", {"image": r"C:\Users\chizuru\Desktop\test.txt"}, "文件格式需为jpg，png"),
        ("UI_emp_012", {"image": r"C:\Users\chizuru\Desktop\test1.jpg"}, "文件大小为2M以下"),
    ])
    def test_UI_emp_008_010_012(self, testcase, image, data):
        emp_ui.AddEmp(image)
        login_ui.wd.find_element(By.XPATH, "//button/span[text()='提交']").click()
        if data != "":
            warm_text = login_ui.wd.find_element(By.CSS_SELECTOR, 'p.el-message__content')
            assert warm_text == data
        else:
            # 将回显的图像与原有的图像进行比较
            actual_image = cv2.imread(image["image"])

            image_src = login_ui.wd.find_element(By.XPATH, '//div[@class="el-form-item"]//img').get_attribute('src')

            # 下载并读取服务器返回的图片
            response_image = requests.get(image_src)
            image_stream = BytesIO(response_image.content)
            expect_image = cv2.imdecode(np.frombuffer(image_stream.read(), np.uint8), cv2.IMREAD_COLOR)
            assert np.array_equal(actual_image, expect_image)

    # 新增员工
    @pytest.mark.parametrize('testcase, emp_data, data', add_testData)
    def test_UI_emp_008_010(self, testcase, emp_data, data):
        emp_ui.AddEmp(emp_data)
        login_ui.wd.find_element(By.XPATH, "//button/span[text()='提交']").click()
        # 查找第一行信息
        name = login_ui.wd.find_element(By.XPATH, '//td[@class="el-table_1_column_2  "]/div').text
        image = login_ui.wd.find_element(By.XPATH, '//td[@class="el-table_1_column_3  "]/div/img').get_attribute("src")
        gender = login_ui.wd.find_element(By.XPATH, '//td[@class="el-table_1_column_4  "]/div').text
        job = login_ui.wd.find_element(By.XPATH, '//td[@class="el-table_1_column_5  "]/div').text
        dept = login_ui.wd.find_element(By.XPATH, '//td[@class="el-table_1_column_6  "]/div').text
        entrydate = login_ui.wd.find_element(By.XPATH, '//td[@class="el-table_1_column_7  "]/div').text
        if emp_data["name"] in emp_data:
            assert name == emp_data["name"]
        if emp_data["img"] in emp_data:
            # 将回显的图像与原有的图像进行比较
            actual_image = cv2.imread(emp_data["img"])

            response_image = requests.get(image)
            image_stream = BytesIO(response_image.content)
            expect_image = cv2.imdecode(np.frombuffer(image_stream.read(), np.uint8), cv2.IMREAD_COLOR)
            assert np.array_equal(actual_image, expect_image)
        if emp_data["gender"] in emp_data:
            assert gender == emp_data["gender"]
        if emp_data["job"] in emp_data:
            assert job == emp_data["job"]
        if emp_data["dept_id"] in emp_data:
            assert dept == emp_data["dept_id"]
        if emp_data["entrydate"] == emp_data:
            assert entrydate == emp_data["entrydate"]

    @pytest.mark.parametrize('testcase, emp_data, data', update_testData)
    def test_UI_emp_007_011(self, testcase, emp_data, data):
        emp_ui.UpdateEmp(emp_data)
        login_ui.wd.find_element(By.XPATH, "//button/span[text()='提交']").click()
        # 查找第一行信息
        name = login_ui.wd.find_element(By.XPATH, '//td[@class="el-table_1_column_2  "]/div').text
        image = login_ui.wd.find_element(By.XPATH, '//td[@class="el-table_1_column_3  "]/div/img').get_attribute("src")
        gender = login_ui.wd.find_element(By.XPATH, '//td[@class="el-table_1_column_4  "]/div').text
        job = login_ui.wd.find_element(By.XPATH, '//td[@class="el-table_1_column_5  "]/div').text
        dept = login_ui.wd.find_element(By.XPATH, '//td[@class="el-table_1_column_6  "]/div').text
        entrydate = login_ui.wd.find_element(By.XPATH, '//td[@class="el-table_1_column_7  "]/div').text
        if emp_data["name"] in emp_data:
            assert name == emp_data["name"]
        if emp_data["img"] in emp_data:
            # 将回显的图像与原有的图像进行比较
            actual_image = cv2.imread(emp_data["img"])

            response_image = requests.get(image)
            image_stream = BytesIO(response_image.content)
            expect_image = cv2.imdecode(np.frombuffer(image_stream.read(), np.uint8), cv2.IMREAD_COLOR)
            assert np.array_equal(actual_image, expect_image)
        if emp_data["gender"] in emp_data:
            assert gender == emp_data["gender"]
        if emp_data["job"] in emp_data:
            assert job == emp_data["job"]
        if emp_data["dept_id"] in emp_data:
            assert dept == emp_data["dept_id"]
        if emp_data["entrydate"] == emp_data:
            assert entrydate == emp_data["entrydate"]



