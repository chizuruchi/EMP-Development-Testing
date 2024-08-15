## 项目介绍

本项目基于 **Java** + **Spring Boot** + **MySQL** + **MyBatis** + **Vue** + **Axios** 开发的员工管理系统，主要实现了以下功能：

- 信息查询
- 新增
- 删除
- 修改

测试方面，使用等价类划分、边界值和场景法对上述功能编写测试用例。

## 项目结构

```plaintext
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
│
├─EMPTestAPI
│  ├─case                                   # 测试用例
│  │  ├─login_test.py                       # 登录模块的测试用例
│  │  ├─dept_test.py                        # 部门模块的测试用例
│  │  └─emp_test.py                         # 员工模块的测试用例
│  ├─lib                                    # 测试库
│  │  ├─login.py                            # 登录模块的测试逻辑
│  │  ├─dept.py                             # 部门模块的测试逻辑
│  │  └─emp.py                              # 员工模块的测试逻辑
│  └─cfg.py                                 # 配置文件，包含全局配置
│
├─TestCase.xlsx                             # 测试用例数据文件
