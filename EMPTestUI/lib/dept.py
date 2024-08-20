from lib.login import login_ui
from selenium.webdriver.common.by import By


class DEPT_UI:
    def EntryDept(self):
        login_ui.login()
        login_ui.wd.find_element(By.CLASS_NAME, 'el-menu-item').click()

    def AddDept(self, deptName):
        # 点击添加部门按钮
        login_ui.wd.find_element(By.CSS_SELECTOR, '.el-main>.el-button').click()
        # 填入部门信息
        login_ui.wd.find_element(By.TAG_NAME, 'input').send_keys(deptName)
        login_ui.wd.find_element(By.CSS_SELECTOR, '.dialog-footer>button').click()

    def UpdateDept(self, testname, deptName):
        xpath_expression = f'//tbody/tr/td[@class="el-table_2_column_10  "]/div[text()="{testname}"]'

        # 找到测试部门那一行
        dept_name_ele = login_ui.wd.find_element(By.XPATH, xpath_expression)
        dept_ele = dept_name_ele.find_element(By.XPATH, './ancestor::tr')
        # 找到测试部门的编辑按钮
        confirm_button = dept_ele.find_element(By.XPATH,
                                               './/button[contains(@class, "el-button--primary")]/span[text()="编辑"]/..')
        # 点击编辑按钮
        confirm_button.click()

        # 找到编辑表单中的输入框
        input_ele = login_ui.wd.find_element(By.XPATH, '//input')
        input_ele.clear()
        input_ele.send_keys(deptName)

    def DeleteDept(self, testname):
        xpath_expression = f'//tbody/tr/td[@class="el-table_2_column_10  "]/div[text()="{testname}"]'

        # 找到测试部门那一行
        dept_name_ele = login_ui.wd.find_element(By.XPATH, xpath_expression)
        dept_ele = dept_name_ele.find_element(By.XPATH, './ancestor::tr')
        # 找到测试部门的删除按钮
        confirm_button = dept_ele.find_element(By.XPATH,
                                               './/button[contains(@class, "el-button--danger")]/span[text()="删除"]/..')
        # 点击删除按钮
        confirm_button.click()


dept_ui = DEPT_UI()
