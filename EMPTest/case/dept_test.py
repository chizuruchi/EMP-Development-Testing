import pytest
from lib.dept import dept_instance


class Test_dept:
    @pytest.mark.parametrize('id, code, msg, le', [
        (None, 1, "success", 7),
        ("1", 1, "success", 1),
        ("3", 1, "success", 1),
        ("8", 1, "success", 1),
        ("9", 1, "success", None),
        ("1,2", 0, "fail", None)
    ])
    # 部门查询及根据ID查询
    def test_dept_001_006(self, id, code, msg, le):
        response = dept_instance.searchIdDept(id)
        assert response["code"] == code
        assert response["msg"] == msg
        data = (response["data"])
        # 仅返回一个部门的值
        if isinstance(data, dict):
            assert "id" in data
            assert "name" in data
            assert "create_time" in data
            assert "update_time" in data
        # 返回多个部门的值
        elif isinstance(data, list):
            assert len(data) == le
            for dept in data:
                assert "id" in dept
                assert "name" in dept
                assert "create_time" in dept
                assert "update_time" in dept
        # 查询不到该部门
        elif data is None:
            assert data == le

    @pytest.mark.parametrize('body, code, msg, data', [
        ({"name": "审查部"}, 1, "success", None),
        (None, 0, "fail", "missing"),
        ([{"name": "审查部"}, {"name": "伦理部"}], 0, "fail", "JSON parse error"),
        ({"name": "教研部"}, 0, "fail", "Duplicate entry")
    ])
    # 新增部门
    def test_dept_007_010(self, body, code, msg, data):
        response = dept_instance.addDept(body)
        assert response["code"] == code
        assert response["msg"] == msg
        if data is None:
            assert response["data"] is None
        else:
            assert data in response["data"]

    @pytest.mark.parametrize('body, code, msg, data', [
        ({"id": 1, "name": "通讯部"}, 1, "success", None),
        (None, 0, "fail", "missing"),
        ({"id": 1}, 0, "fail", "database"),
        ({"id": 1, "name": ""}, 0, "Please enter the name of the department", None),
        ({"name": "通讯部"}, 0, "Please enter the id of the department", None),
        ({"id": None, "name": "通讯部"}, 0, "Please enter the id of the department", None),
        ({"id": 1,"name": "教研部"}, 0, "fail", "database"),
    ])
    # 修改员工信息
    def test_dept_012_016(self, body, code, msg, data):
        response = dept_instance.updateDept(body)
        assert response["code"] == code
        assert response["msg"] == msg
        if data is None:
            assert response["data"] is None
        else:
            assert data in response["data"]

    @pytest.mark.parametrize('ids, code, msg, data', [
        ("17", 1, "success", None),
        ("7,8", 0, "fail", "Failed"),
        ("11", 0, "No such department", None),
        (None, 0, "fail", "Failed"),
    ])
    # 删除部门
    def test_dept_017_022(self, ids, code, msg, data):
        response = dept_instance.deleteDept(ids)
        assert response["code"] == code
        assert response["msg"] == msg
        if data is None:
            assert response["data"] is None
        else:
            assert data in response["data"]



