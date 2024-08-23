import copy
import time

from selenium.webdriver.common.by import By
from lib.login import login_ui
from cfg import *


class EMP_UI:
    def __init__(self):
        login_ui.login()

    def SearchEmp(self, name="", gender="", start="", end=""):
        # 点击重置按钮
        login_ui.wd.find_element(By.XPATH, "//span[text()= '重置']").click()

        if name != "":
            login_ui.wd.find_element(By.CSS_SELECTOR, 'input[placeholder="姓名"]').send_keys(name)

        if gender != "":
            # 点击下拉框
            login_ui.wd.find_element(By.CSS_SELECTOR, 'div.el-input.el-input--suffix > input.el-input__inner').click()
            # 选择选项
            option_path = f'//li/span[contains(text(), "{gender}")]'
            login_ui.wd.find_element(By.XPATH, option_path).click()

        now_year = copy.deepcopy(year)
        now_month = copy.deepcopy(month)

        def selectYearMonth(exp_year, exp_month):
            # 选择年份
            if exp_year < now_year:
                for i in range(exp_year, now_year):
                    # 点击前一年按钮
                    login_ui.wd.find_element(By.CSS_SELECTOR, ".el-date-range-picker__header>.el-icon-d-arrow-left").click()
            elif exp_year > now_year:
                for i in range(now_year, exp_year):
                    # 点击后一年按钮
                    login_ui.wd.find_element(By.CSS_SELECTOR, ".el-date-range-picker__header>.el-icon-d-arrow-right").click()

            # 选择月份
            if exp_month < now_month:
                for i in range(exp_month, now_month):
                    # 点击前一月按钮
                    login_ui.wd.find_element(By.CSS_SELECTOR, ".el-date-range-picker__header>.el-icon-arrow-left").click()
            elif exp_month > now_month:
                for i in range(now_month, exp_month):
                    # 点击后一月按钮
                    login_ui.wd.find_element(By.CSS_SELECTOR, ".el-date-range-picker__header>.el-icon-arrow-right").click()

        if start != "" or end != "":
            # 定位并点击“开始日期”输入框
            start_date_input = login_ui.wd.find_element(By.CSS_SELECTOR, 'input[placeholder="开始日期"]')
            start_date_input.click()

            # 选择开始日期及结束日期
            selectYearMonth(exp_year=int(start[:4]), exp_month=int(start[5:7]))
            now_year = int(start[:4])
            now_month = int(start[5:7])

            # 选择日期
            day_path = f"//div[contains(@class,'is-left')]//td[contains(@class,'available')]//span[text()={start[-2:]}]"
            login_ui.wd.find_element(By.XPATH, day_path).click()

            selectYearMonth(exp_year=int(end[:4]), exp_month=int(end[5:7])-1)

            # 选择日期
            day_path = f"//div[contains(@class,'is-right')]//td[contains(@class,'available')]//span[text()={end[-2:]}]"
            login_ui.wd.find_element(By.XPATH, day_path).click()

        # 点击查询按钮
        login_ui.wd.find_element(By.XPATH, "//span[text()= '查询']").click()

    def AddEmp(self, emp_data):
        # 点击新增员工按钮
        login_ui.wd.find_element(By.XPATH, "//button/span[text()='+新增员工']").click()

        if "username" in emp_data:
            login_ui.wd.find_element(By.XPATH, "//div[@class='el-input']/input[@placeholder='请输入用户名，2-20字符，不可重复']")\
                .send_keys(emp_data["username"])

        if "name" in emp_data:
            login_ui.wd.find_element(By.XPATH, "//div[@class='el-input']/input[@placeholder='请输入用户姓名，2-10个字']")\
                .send_keys(emp_data["name"])

        if "gender" in emp_data:
            gender_label = login_ui.wd.find_element(By.XPATH, "//label[contains(text(), '性  别')]")
            # 找到与 <label> 相邻的选择框的输入框
            gender_select_box = gender_label.find_element(By.XPATH,
                                                          "./following-sibling::div//input[@class='el-input__inner']")
            # 点击选择框以展开下拉选项
            gender_select_box.click()
            # 选择选项
            if emp_data["gender"] == "女":
                login_ui.wd.find_elements(By.XPATH, "//li[@class='el-select-dropdown__item']/span[text()='女']")[1].click()
            else:
                login_ui.wd.find_elements(By.XPATH, "//li[@class='el-select-dropdown__item']/span[text()='男']")[1].click()

        if "image" in emp_data:
            login_ui.wd.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(emp_data["image"])
            time.sleep(1)

        if "job" in emp_data:
            job_label = login_ui.wd.find_element(By.XPATH, "//label[contains(text(), '职   位')]")
            # 找到与 <label> 相邻的选择框的输入框
            gender_select_box = job_label.find_element(By.XPATH,
                                                        "./following-sibling::div//input[@class='el-input__inner']")
            # 点击选择框以展开下拉选项
            gender_select_box.click()

            job_path = f"""//span[text()='{emp_data["job"]}']"""

            login_ui.wd.find_element(By.XPATH, job_path).click()

        if "dept_id" in emp_data:
            dept_label = login_ui.wd.find_element(By.XPATH, "//label[contains(text(), ' 归属部门')]")
            # 找到与 <label> 相邻的选择框的输入框
            gender_select_box = dept_label.find_element(By.XPATH,
                                                       "./following-sibling::div//input[@class='el-input__inner']")
            # 点击选择框以展开下拉选项
            gender_select_box.click()

            job_path = f"""//span[text()='{emp_data["dept_id"]}']"""

            login_ui.wd.find_element(By.XPATH, job_path).click()

        if "entrydate" in emp_data:
            login_ui.wd.find_element(By.XPATH, '//input[@placeholder="选择日期"]').click()

            now_year = copy.deepcopy(year)
            now_month = copy.deepcopy(month)

            exp_year = int(emp_data["entrydate"][:4])
            exp_month = int(emp_data["entrydate"][5:7])
            exp_day = int(emp_data["entrydate"][-2:])

            # 选择年份
            if exp_year < now_year:
                for i in range(exp_year, now_year):
                    # 点击前一年按钮
                    login_ui.wd.find_element(By.XPATH, '//button[@aria-label="前一年"]').click()
            elif exp_year > now_year:
                for i in range(now_year, exp_year):
                    # 点击后一年按钮
                    login_ui.wd.find_element(By.XPATH, '//button[@aria-label="后一年"]').click()

            # 选择月份
            if exp_month < now_month:
                for i in range(exp_month, now_month):
                    # 点击前一月按钮
                    login_ui.wd.find_element(By.XPATH, '//button[@aria-label="上个月"]').click()
            elif exp_month > now_month:
                for i in range(now_month, exp_month):
                    # 点击后一月按钮
                    login_ui.wd.find_element(By.XPATH, '//button[@aria-label="下个月"]').click()

            # 选择日期
            day_path = f"//td[contains(@class,'available')]//span[text()={exp_day}]"
            login_ui.wd.find_element(By.XPATH, day_path).click()

    def UpdateEmp(self, emp_data):
        xpath_expression = f"""//div[text()='{emp_data["name"]}']"""

        # 找到测试员工那一行
        dept_name_ele = login_ui.wd.find_element(By.XPATH, xpath_expression)
        dept_ele = dept_name_ele.find_element(By.XPATH, './ancestor::tr')
        # 找到测试员工的编辑按钮
        confirm_button = dept_ele.find_element(By.XPATH,
                                               './/button[contains(@class, "el-button--primary")]/span[text()="编辑"]/..')
        # 点击编辑按钮
        confirm_button.click()

        if "name" in emp_data:
            login_ui.wd.find_elements(By.XPATH, "//div[@class='el-input']/input[@placeholder='请输入用户姓名，2-10个字']")[1] \
                .send_keys(emp_data["name"])

        if "gender" in emp_data:
            gender_label = login_ui.wd.find_elements(By.XPATH, "//label[contains(text(), '性  别')]")[1]
            # 找到与 <label> 相邻的选择框的输入框
            gender_select_box = gender_label.find_element(By.XPATH,
                                                          "./following-sibling::div//input[@class='el-input__inner']")
            # 点击选择框以展开下拉选项
            gender_select_box.click()
            # 选择选项
            if emp_data["gender"] == "女":
                login_ui.wd.find_elements(By.XPATH, "//li[@class='el-select-dropdown__item']/span[text()='女']")[
                    1].click()
            else:
                login_ui.wd.find_elements(By.XPATH, "//li[@class='el-select-dropdown__item']/span[text()='男']")[
                    1].click()

        if "image" in emp_data:
            login_ui.wd.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(emp_data["image"])
            time.sleep(1)

        if "job" in emp_data:
            job_label = login_ui.wd.find_elements(By.XPATH, "//label[contains(text(), '职   位')]")[1]
            # 找到与 <label> 相邻的选择框的输入框
            gender_select_box = job_label.find_element(By.XPATH,
                                                       "./following-sibling::div//input[@class='el-input__inner']")
            # 点击选择框以展开下拉选项
            gender_select_box.click()

            job_path = f"""//span[text()='{emp_data["job"]}']"""

            login_ui.wd.find_element(By.XPATH, job_path).click()

        if "dept_id" in emp_data:
            dept_label = login_ui.wd.find_elements(By.XPATH, "//label[contains(text(), ' 归属部门')]")[1]
            # 找到与 <label> 相邻的选择框的输入框
            gender_select_box = dept_label.find_element(By.XPATH,
                                                        "./following-sibling::div//input[@class='el-input__inner']")
            # 点击选择框以展开下拉选项
            gender_select_box.click()

            job_path = f"""//span[text()='{emp_data["dept_id"]}']"""

            login_ui.wd.find_element(By.XPATH, job_path).click()

        if "entrydate" in emp_data:
            login_ui.wd.find_elements(By.XPATH, '//input[@placeholder="选择日期"]')[1].click()

            now_year = copy.deepcopy(year)
            now_month = copy.deepcopy(month)

            exp_year = int(emp_data["entrydate"][:4])
            exp_month = int(emp_data["entrydate"][5:7])
            exp_day = int(emp_data["entrydate"][-2:])

            # 选择年份
            if exp_year < now_year:
                for i in range(exp_year, now_year):
                    # 点击前一年按钮
                    login_ui.wd.find_element(By.XPATH, '//button[@aria-label="前一年"]').click()
            elif exp_year > now_year:
                for i in range(now_year, exp_year):
                    # 点击后一年按钮
                    login_ui.wd.find_element(By.XPATH, '//button[@aria-label="后一年"]').click()

            # 选择月份
            if exp_month < now_month:
                for i in range(exp_month, now_month):
                    # 点击前一月按钮
                    login_ui.wd.find_element(By.XPATH, '//button[@aria-label="上个月"]').click()
            elif exp_month > now_month:
                for i in range(now_month, exp_month):
                    # 点击后一月按钮
                    login_ui.wd.find_element(By.XPATH, '//button[@aria-label="下个月"]').click()

            # 选择日期
            day_path = f"//td[contains(@class,'available')]//span[text()={exp_day}]"
            login_ui.wd.find_element(By.XPATH, day_path).click()

    def DeleteEmp(self, emp_data):
        xpath_expression = f"""//div[text()='{emp_data["name"]}']"""

        # 找到测试员工那一行
        dept_name_ele = login_ui.wd.find_element(By.XPATH, xpath_expression)
        dept_ele = dept_name_ele.find_element(By.XPATH, './ancestor::tr')
        # 找到测试员工的编辑按钮
        confirm_button = dept_ele.find_element(By.XPATH,
                                               './/button[contains(@class, "el-button el-button--danger")]/span[text()="删除"]/..')
        # 点击删除按钮
        confirm_button.click()

        # 点击确认按钮
        login_ui.wd.find_element(By.XPATH, """//div[@aria-label="提示"]//span[text()='确 定']""").click()


emp_ui = EMP_UI()
