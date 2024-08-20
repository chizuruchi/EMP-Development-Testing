import pytest
from selenium.common import NoSuchElementException

from lib.dept import dept_ui
from lib.login import login_ui
from selenium.webdriver.common.by import By
import time

class Test_dept:
    def setup_method(self, method):
        dept_ui.EntryDept()

    @pytest.mark.parametrize('deptName, text', [
        ('审查部', ''),
        ("人事部", '部门新增失败'),
        ("人", '请输入部门名称，长度为2-10位'),
        ("abcde甲乙丙丁戊a", '请输入部门名称，长度为2-10位'),
        ("", '请输入部门名称，长度为2-10位')
    ])
    def test_UI_dept_001_005(self, deptName, text):
        dept_ui.AddDept(deptName)
        # 查找保存按钮，并点击
        login_ui.wd.find_element(By.XPATH, '//button/span[text()=" 保 存 "]')
        if text != "":
            time.sleep(0.5)
            # 查找提示信息元素
            element = login_ui.wd.find_element(By.CSS_SELECTOR, 'p.el-message__content')
            expect_text = element.text
            assert text in expect_text
        else:
            xpath_expression = f'//tbody/tr/td[@class="el-table_2_column_10  "]/div[text()="{deptName}"]'

            # 找到测试部门那一行
            dept_name_ele = login_ui.wd.find_element(By.XPATH, xpath_expression)

            assert dept_name_ele is not None

    @pytest.mark.parametrize('testName, deptName, text', [
        ("人事部", "伦理部", ""),
        ("咨询部", "咨询部", "请更改部门名称"),
        ("研发部", "伦", "请输入部门名称，长度为2-10位"),
        ("就业部", "ab126###@@!", '请输入部门名称，长度为2-10位')
    ])
    def test_UI_dept_007_010(self, testName, deptName, text):
        dept_ui.UpdateDept(testName, deptName)
        # 查找保存按钮，并点击
        login_ui.wd.find_element(By.XPATH, '//button/span[text()="保 存"]').click()
        if text != "":
            time.sleep(0.5)
            # 查找提示信息元素
            element = login_ui.wd.find_element(By.CSS_SELECTOR, 'p.el-message__content')
            expect_text = element.text
            assert text in expect_text
        else:
            xpath_expression = f'//tbody/tr/td[@class="el-table_2_column_10  "]/div[text()="{deptName}"]'

            # 找到测试部门那一行
            dept_name_ele = login_ui.wd.find_element(By.XPATH, xpath_expression)

            assert dept_name_ele is not None

    @pytest.mark.parametrize('testName, text', [
        ("通讯部", "1"),
        ("通讯部", "0")
    ])
    def test_UI_dept_011_012(self, testName, text):
        dept_ui.DeleteDept(testName)
        xpath_expression = f'//tbody/tr/td[@class="el-table_2_column_10  "]/div[text()="{testName}"]'
        if text == "1":
            login_ui.wd.find_element(By.XPATH, '//button/span[text()="确 定"]').click()

            try:
                # 尝试查找测试部门的是否存在
                login_ui.wd.find_element(By.XPATH, xpath_expression)
                assert False, f"Element with department name '{testName}' was found, but it should not exist."
            except NoSuchElementException:
                assert True
        elif text == "0":
            login_ui.wd.find_element(By.XPATH, '//button/span[text()="取 消"]').click()

            # 找到测试部门那一行
            dept_name_ele = login_ui.wd.find_element(By.XPATH, xpath_expression)

            assert dept_name_ele is not None

