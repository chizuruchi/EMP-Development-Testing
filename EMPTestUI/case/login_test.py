import pytest
import time
from selenium.webdriver.common.by import By
from lib.login import login_ui
from cfg import *


class Test_login:

    @pytest.mark.parametrize('username, password, text', [
        ("jinyong", "123456", ""),
        ("jinyon", "123456", "登录失败"),
        ("jinyong", "123456!", "登录失败"),
        ("", "123456", "请输入用户名和密码"),
        ("jinyong", "", "请输入用户名和密码")
    ])
    def test_UI_login_001_005(self, username, password, text):
        login_ui.login(username, password)
        if text != "":
            time.sleep(0.5)
            element = login_ui.wd.find_element(By.CSS_SELECTOR, 'p.el-message__content')
            expect_text = element.text
            assert text in expect_text
        else:
            login_ui.wd.find_element(By.CLASS_NAME, 'el-menu-item').click()
            element = login_ui.wd.find_element(By.CSS_SELECTOR, '.top-font')
            assert element.text == "部门管理"

    def test_UI_login_006(self):
        login_ui.wd.get(deptURL)
        element = login_ui.wd.find_element(By.CSS_SELECTOR, 'p.el-message__content')
        assert element.text == "未登录，请先登录"

    def test_UI_login_007(self):
        login_ui.login()
        # 点击退出登录按钮
        login_ui.wd.find_element(By.CSS_SELECTOR, '.el-button').click()
        login_ui.wd.get(deptURL)
        element = login_ui.wd.find_element(By.CSS_SELECTOR, 'p.el-message__content')
        assert element.text == "未登录，请先登录"



