from utils.login import login_instance
import pytest
from cfg import headers
from lib.dept import dept_instance

class Test_login:
    @pytest.mark.parametrize('body', [
        ({'username': "jinyon", 'password': "123456"}),
        ({'username': "jinyong", 'password': "123456!"}),
        ({'password': "123456"}),
        ({'username': "jinyong"}),
        ({'username': "", 'password': "123456"}),
        ({'username': "jinyong", 'password': ""}),
        ({'username': "jinyong", 'password': "' OR '1'='1"}),
        ({'username': "jinyong", 'password': "'; DROP TABLE users;--"}),
        ({'username': "jinyong", 'password': "' OR 1=1 --"}),
    ])
    def test_login002_008(self, body):
        response = login_instance.userLogin(body)

        assert response["code"] == 0
        assert response["msg"] == "login failed"

    def test_login001_009(self):
        data = {
            "username": "jinyong",
            "password": "123456"
        }
        response1 = login_instance.userLogin(data)
        assert response1["code"] == 1
        assert response1["msg"] == "success"

        headers["token"] = response1["data"]

        response2 = dept_instance.searchDept()
        assert response2["code"] == 1
        assert response2["msg"] == "success"
        for dept in response2["data"]:
            assert "id" in dept
            assert "name" in dept
            assert "create_time" in dept
            assert "update_time" in dept

    @pytest.mark.parametrize('jwt', [
        ("yJhbGciOiJIUzI1NiJ9.eyJpZCI6bnVsbCwidXNlcm5hbWUiOiJqaW55b25nIiwiZXhwIjoxNzIzMzcwNzU4fQ.Hv11G3IuYQxgSPdeKykSDvTcvk0yWha9TzG8JtxKSNk"),
        (""),
        (None)
    ])
    def test_login010_012(self, jwt):
        if jwt is not None:
            headers["token"] = jwt
        else:
            headers.pop("token", None)

        response = dept_instance.searchDept()
        assert response["code"] == 0
        assert response["msg"] == "NOT_LOGIN"
