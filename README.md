## 项目简介

本项目是一个基于 **Java**、**Spring Boot**、**MySQL**、**MyBatis**、**Vue** 和 **Axios** 开发的员工管理系统，主要实现了以下功能：

- 信息查询
- 新增部门或员工
- 删除部门或员工
- 修改部门或员工
- 员工头像上传

## 测试策略

在测试方面，本项目采用等价类划分、边界值分析和场景法对上述功能编写测试用例。具体测试实施如下：

1. **自动化测试框架**  
   测试用例的执行采用 `pytest` 作为自动化测试框架。

2. **数据驱动测试**  
   数据驱动测试分为两种方式：
   - 使用 `pytest.mark.parametrize` 装饰器直接在测试函数中进行参数化。
   - 通过 `openpyxl` 和 `pandas` 库从 Excel 文件中动态加载测试数据。

3. **接口自动化测试**  
   使用 `requests` 库发送 HTTP 请求，验证接口的正确性和稳定性。

4. **功能自动化测试**  
   使用 `Selenium` 进行网页的自动化操作，模拟用户行为，测试系统功能的可靠性。


## 项目结构

```plaintext
├─员工管理系统-测试用例.xlsx                 # 测试用例数据文件
│
├─EMPTestAPI                                # 接口自动化测试项目
│  ├─case                                   
│  │  ├─login_test.py                       # 登录模块的测试用例
│  │  ├─dept_test.py                        # 部门模块的测试用例
│  │  └─emp_test.py                         # 员工模块的测试用例
│  ├─lib                                    
│  │  ├─testcase.xlsx                       # 使用excel表存放测试用例输入数据及验证数据
│  │  ├─LoadExceldata.py                    # 加载测试用例输入数据及验证数据
│  │  ├─login.py                            # 登录模块的测试逻辑
│  │  ├─dept.py                             # 部门模块的测试逻辑
│  │  └─emp.py                              # 员工模块的测试逻辑
│  └─cfg.py                                 # 配置文件
│
├─EMPTestUI                                 # 功能自动化测试项目
│  ├─case                                   
│  │  ├─login_test.py                       # 登录模块的测试用例
│  │  ├─dept_test.py                        # 部门模块的测试用例
│  │  └─emp_test.py                         # 员工模块的测试用例
│  ├─lib                                    
│  │  ├─testcase.xlsx                       # 使用excel表存放测试用例输入数据及验证数据
│  │  ├─LoadExceldata.py                    # 加载测试用例输入数据及验证数据
│  │  ├─login.py                            # 登录模块的登录操作
│  │  ├─dept.py                             # 部门模块的增删改查操作
│  │  └─emp.py                              # 员工模块的增删改查操作
│  └─cfg.py                                 # 配置文件
│
├─EmployeeManagerAPI                         # 员工管理系统后端项目
│  └─src
│      ├─main
│      │  ├─java
│      │  │  └─com
│      │  │      └─example
│      │  │          └─mybatisdemo
│      │  │              ├─controller        # 控制器层，处理请求并返回数据
│      │  │              ├─exception         # 自定义异常类和全局异常处理
│      │  │              ├─filter            # 过滤器，用于请求拦截或处理
│      │  │              ├─mapper            # 数据访问层，MyBatis的Mapper接口
│      │  │              ├─pojo              # 实体类，表示数据库中的表结构
│      │  │              ├─service           # 服务层，业务逻辑处理
│      │  │              └─utils             # 工具类，通用的辅助功能
│      │  └─resources
│      │      └─com
│      │          └─example
│      │              └─mybatisdemo
│      │                  ├─mapper          # MyBatis的XML配置文件
│      │                  └─static          
│      └─test
│          └─java                           
│
├─EmployeeManagerUI                          # 员工管理系统前端项目
│  ├─public                                  
│  └─src
│      ├─assets                              
│      ├─components                          # Vue组件
│      ├─router                              # 路由配置
│      ├─utils                               # 工具函数和方法
│      └─views
│          └─tlias                           # 视图组件
│              ├─DepView.vue                 # 部门视图组件
│              ├─EmpView.vue                 # 员工视图组件
│              └─LoginView.vue               # 登录视图组件
