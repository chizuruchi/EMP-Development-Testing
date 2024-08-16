<template>
  <div>
    <!-- 写html -->
    <!-- 整体布局 -->
    <el-container style="height: 500px; border: 1px solid #eee">
      <!-- 头部部分 -->
      <el-header style="
          font-size: 40px;
          background-color: #eee;
          display: flex;
          align-items: center;
          justify-content: space-between;
        ">
        员工管理系统
        <router-link to="/login">
          <el-button type="primary" icon="el-icon-switch-button" @click="logout">退出登录</el-button>
        </router-link>
      </el-header>
      <el-container>
        <!-- 侧边栏 -->
        <el-aside width="200px">
          <el-menu>
            <router-link to="/dep" class="no-underline">
              <el-menu-item>部门管理</el-menu-item>
            </router-link>
            <router-link to="/emp" class="no-underline">
              <el-menu-item>员工管理</el-menu-item>
            </router-link>
          </el-menu>
        </el-aside>
        <!-- 主体部分 -->
        <el-main>
          <div class="container">
            <div class="square"></div>
            <div class="top-font">员工管理</div>
          </div>

          <!-- 员工查询 -->
          <el-form :inline="true" :model="formInline" class="first-form">
            <el-form-item label="姓名">
              <el-input v-model="formInline.user" placeholder="姓名"></el-input>
            </el-form-item>
            <el-form-item label="性别">
              <el-select v-model="formInline.gender" placeholder="请选择">
                <el-option label="男" value="1"></el-option>
                <el-option label="女" value="2"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="入职日期">
              <el-date-picker v-model="formInline.date" type="daterange" range-separator="至" start-placeholder="开始日期"
                end-placeholder="结束日期" value-format="yyyy-MM-dd">
              </el-date-picker>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="searchSubmit">查询</el-button>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="searchStill">重置</el-button>
            </el-form-item>
          </el-form>

          <!-- 新增员工的弹窗 -->
          <el-button type="primary" @click="AddFormVisible = true">+新增员工</el-button>
          <el-dialog title="新增员工" :visible.sync="AddFormVisible" width="30%">
            <el-form :model="AddForm" inline>
              <el-form-item label="* 用户名 " label-width="80px">
                <el-input v-model="AddForm.username" autocomplete="off" placeholder="请输入用户名，2-20字符，不可重复">
                </el-input>
              </el-form-item>
              <el-form-item label="* 用户姓名" label-width="80px">
                <el-input v-model="AddForm.name" autocomplete="off" placeholder="请输入用户姓名，2-10个字"></el-input>
              </el-form-item>
              <el-form-item label="* 性  别 " label-width="80px">
                <el-select v-model="AddForm.gender" placeholder="请选择">
                  <el-option label="男" value="1"></el-option>
                  <el-option label="女" value="2"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item label="图   像" label-width="80px">
                <el-upload class="avatar-uploader" action="http://127.0.0.1:8080/upload" name="image"
                  :show-file-list="false" :on-success="handleAvatarSuccess" :before-upload="beforeAvatarUpload"
                  :on-error="handleUploadError" :headers="uploadHeaders">
                  <img v-if="imageUrl" :src="imageUrl" class="avatar">
                  <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                </el-upload>
              </el-form-item>
              <el-form-item label="职   位" label-width="80px">
                <el-select v-model="AddForm.job" placeholder="请选择">
                  <el-option label="班主任" value="1"></el-option>
                  <el-option label="讲师" value="2"></el-option>
                  <el-option label="学工主管" value="3"></el-option>
                  <el-option label="教研主管" value="4"></el-option>
                  <el-option label="咨询师" value="5"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item label=" 入职日期" label-width="80px">
                <el-date-picker v-model="AddForm.entrydate" type="date" placeholder="选择日期"
                  value-format="yyyy-MM-dd"></el-date-picker>
              </el-form-item>
              <el-form-item label=" 归属部门" label-width="80px">
                <el-select v-model="AddForm.dept_id" placeholder="请选择">
                  <!-- 使用v-for循环deptData数组，为每个部门生成一个el-option -->
                  <el-option v-for="dept in departmentsList" :key="dept.id" :label="dept.name" :value="dept.id">
                  </el-option>
                </el-select>
              </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button @click="cancelSubmit">取消</el-button>
              <el-button type="primary" @click="submitForm(AddForm)">提交</el-button>
            </div>
          </el-dialog>

          <!-- 表格 -->
          <el-table :data="tableData" style="width: 100%">
            <el-table-column type="selection" width="55"></el-table-column>
            <el-table-column prop="name" label="姓名" width="110">
            </el-table-column>
            <el-table-column label="图像" prop="image" width="130">
              <template slot-scope="scope">
                <img :src="scope.row.image" alt="图像" style="width: 50px; height: 50px" />
              </template>
            </el-table-column>
            <el-table-column label="性别" prop="gender" width="110">
              <template slot-scope="scope">
                {{ scope.row.gender == 1 ? "男" : "女" }}
              </template>
            </el-table-column>
            <el-table-column prop="job" label="职位" width="110">
              <template slot-scope="scope">
                <!-- 使用映射对象将数字转换为文字 -->
                {{ jobTitlesMap && jobTitlesMap[scope.row.job] ? jobTitlesMap[scope.row.job] : "未知职位" }}
              </template>
            </el-table-column>
            <el-table-column prop="dept_id" label="所属部门" width="110">
              <template slot-scope="scope">
                <!-- 使用映射对象将数字转换为文字 -->
                {{ deptData[scope.row.dept_id] || "未知部门" }}
              </template>
            </el-table-column>
            <el-table-column prop="entrydate" label="入职日期" width="130">
            </el-table-column>
            <el-table-column prop="update_time" label="最后操作时间" width="210">
              <template slot-scope="scope">
                {{ scope.row.update_time.replace('T', ' ') }}
              </template>
            </el-table-column>
            <el-table-column label="操作">
              <template slot-scope="scope">
                <el-row>
                  <el-button type="primary" @click="handleEdit(scope.row)">编辑</el-button>
                  <el-button type="danger" @click="confirmDelete(scope.row.id)">删除</el-button>
                  <!-- 删除对话框 -->
                  <el-dialog title="提示" :visible.sync="deleteDialogVisible[scope.row.id]" width="30%"
                    :before-close="handleClose">
                    <span>您确定要删除该员工吗?</span>
                    <span slot="footer" class="dialog-footer">
                      <el-button type="primary" @click="deleteRow(scope.row.id)">确 定</el-button>
                      <el-button @click="closeDeleteDialog(scope.row.id)">取 消</el-button>
                    </span>
                  </el-dialog>
                </el-row>
              </template>
            </el-table-column>
          </el-table>

          <!-- 编辑员工的弹窗 -->
          <el-dialog title="编辑员工" :visible.sync="EditFormVisible" width="30%">
            <el-form :model="EditForm" inline>
              <el-form-item label="* 用户姓名" label-width="80px">
                <el-input v-model="EditForm.name" autocomplete="off" placeholder="请输入用户姓名，2-10个字"></el-input>
              </el-form-item>
              <el-form-item label="* 性  别 " label-width="80px">
                <el-select v-model="EditForm.gender" placeholder="请选择">
                  <el-option v-for="(t, i) of genderTitles" :key="i" :label="t.label" :value="t.value"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item label="图   像" label-width="80px">
                <el-upload class="avatar-uploader" action="http://127.0.0.1:8080/upload" name="image"
                  :show-file-list="false" :on-success="handleAvatarSuccess" :before-upload="beforeAvatarUpload"
                  :headers="uploadHeaders">
                  <img v-if="EditForm.image" :src="EditForm.image" class="avatar">
                  <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                </el-upload>
              </el-form-item>
              <el-form-item label="职   位" label-width="80px">
                <el-select v-model="EditForm.job" placeholder="请选择">
                  <el-option v-for="(t, i) of jobTitles" :key="i" :label="t.label" :value="t.value"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item label=" 入职日期" label-width="80px">
                <el-date-picker v-model="EditForm.entrydate" type="date" placeholder="选择日期"
                  value-format="yyyy-MM-dd"></el-date-picker>
              </el-form-item>
              <el-form-item label=" 归属部门" label-width="80px">
                <el-select v-model="EditForm.dept_id" placeholder="请选择">
                  <el-option v-for="dept in departmentsList" :key="dept.id" :label="dept.name" :value="dept.id">
                  </el-option>
                </el-select>
              </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button @click="EditFormVisible = false">取消</el-button>
              <el-button type="primary" @click="submitForm(EditForm)">提交</el-button>
            </div>
          </el-dialog>

          <div class="row">
            <div>共 {{ totalRecords }} 条记录</div>
            <div class="block">
              <el-pagination layout="prev, pager, next" :total="totalRecords" :page-size="5" :current-page="currentPage"
                @current-change="handlePageChange">
              </el-pagination>
            </div>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import Vue from "vue";
import axiosInatance from "../../utils/Axios.ts";
Vue.prototype.$axios = axiosInatance;
export default {
  // 写JavaScript
  data() {
    return {
      tableData: [],  // 储存表格数据
      totalRecords: 0,  // 数据库中员工数量
      currentPage: 1,  // 当前页码

      genderTitles: [
        { label: "男", value: 1 },
        { label: "女", value: 2 }
      ],
      jobTitles: [
        { label: "班主任", value: 1 },
        { label: "讲师", value: 2 },
        { label: "学工主管", value: 3 },
        { label: "教研主管", value: 4 },
        { label: "咨询师", value: 5 }
      ],

      // 查询表单数据
      formInline: {
        user: "",
        gender: "",
        date: [],
      },

      // 新增表单数据
      AddForm: {
        name: "",
        username: "",
        gender: "",
        image: "",
        dept_id: "",
        job: "",
        entryData: ""
      },

      EditForm: {}, // 编辑表单的数据

      deptData: {}, // 部门数据映射对象
      departmentsList: [], // 原始部门列表
      AddFormVisible: false,  // 控制新增弹窗的显示
      EditFormVisible: false, // 控制编辑弹窗的显示
      deleteDialogVisible: {}, // 用于跟踪删除对话框的可见性

      imageUrl: '',  // 保存上传图片的路径
      originalImage: '' // 保存编辑表单中原有的图像路径
    };
  },
  methods: {
    // 登出
    logout() {
      // 将token的值存为空字符串
      localStorage.setItem('token', '');

      // 设置 Axios 请求头以便后续请求带上 token
      this.$axios.defaults.headers.common['token'] = '';
    },

    // 获取部门数据
    fetchDeptData() {
      this.$axios.get("/depts")
        .then((response) => {
          this.departmentsList = response.data.data;
          const departments = response.data.data; // 获取到的部门数组
          const deptMap = {};
          departments.forEach(dept => {
            deptMap[dept.id] = dept.name; // 使用部门的 id 作为键，部门的 name 作为值
          });
          this.deptData = deptMap;
          console.log("Dept data:", this.deptData);
        })
        .catch((error) => {
          console.error("Error fetching department data:", error);
        });
    },

    // 查询重置
    searchStill() {
      this.formInline = {
        user: "",
        gender: "",
        date: [],
      };
      this.fetchData();
    },

    // 查询表单提交
    searchSubmit(pageNumber = 1) {
      let [begin, end] = [null, null];

      if (this.formInline.date) {
        console.log("formInline.date:", this.formInline.date);

        [begin, end] = this.formInline.date;

        console.log("前begin, end:", begin, end);
      }

      if(typeof pageNumber != 'number'){
        pageNumber = 1;
      }

      // 构建查询参数对象
      const params = {
        name: this.formInline.user,
        gender: this.formInline.gender, // 使用上面设置的性别数字值
        begin: begin || '', // 确保即使没有选择日期也有默认值
        end: end || '', // 确保即使没有选择日期也有默认值
        page: pageNumber,
        pageSize: 5
      };

      console.log("后begin, end:", begin, end);

      this.tableData = [];

      // 使用axios发送GET请求
      this.$axios.get('/emps', { params })
        .then(response => {
          // 处理响应数据
          console.log(response.data);
          // 这里可以处理你的员工列表数据
          console.log("response.data.data.rows：", response.data.data.rows);
          this.tableData = response.data.data.rows;

          this.totalRecords = response.data.data.total;
          console.log("tableData:", this.tableData);
        })
        .catch(error => {
          // 处理错误情况
          console.error('Error during employee query:', error);
        });
    },

    // 员工分页查询--获取页码
    handlePageChange(page) {
      if (typeof page === 'number') {
        this.searchSubmit(page); // 页码改变时获取相应数据
      } else {
        console.error('无效的页码:', page);
      }
    },

    // 图片上传失败的处理函数
    handleUploadError(err) {
      this.$message.error(`图片上传失败: ${err.message}`);
    },

    // 图片上传后存储图片url
    handleAvatarSuccess(response) {
      // 假设服务器返回的数据中包含上传后的图片 URL
      // 在这里你可以处理服务器返回的数据
      console.log('Upload Success:', response);
      // 示例：将图片 URL 保存到 imageUrl 中
      this.imageUrl = response.data;
      this.EditForm.image = this.imageUrl;
      console.log('imageUrl:', this.imageUrl);
    },

    // 图片上传前处理
    beforeAvatarUpload(file) {
      console.log("file:", file);
      const isImage = file.type === 'image/jpeg' || file.type === 'image/png' || file.type === 'image/jpg';
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isImage) {
        this.$message.error('上传头像图片只能是 PNG, JPG, 或 JPEG 格式!');
      }
      if (!isLt2M) {
        this.$message.error('上传头像图片大小不能超过 2MB!');
      }
      return isImage && isLt2M;
    },

    // 取消新增员工
    cancelSubmit() {
      this.AddFormVisible = false;
      this.imageUrl = '';
      this.AddForm = {
        name: "",
        username: "",
        gender: "",
        image: "",
        dept_id: "",
        job: "",
        entryData: ""
      };
    },

    //  编辑员工前处理
    handleEdit(row) {
      console.log("赋值前的行数据:", row);
      // 点击编辑按钮时，使用当前选中的行数据（为了编辑员工中的数据回显用的）
      this.$nextTick(() => {
        this.EditForm = { ...row }; // 复制行数据
        this.originalImage = row.image;
        this.EditFormVisible = true;
        console.log("赋值后的 EditForm:", this.EditForm);
      });
    },

    // 单个员工删除
    confirmDelete(id) {
      this.$set(this.deleteDialogVisible, id, true); // 显示当前行的删除确认对话框
    },
    deleteRow(id) {
      // 构建请求路径，使用模板字符串将 id 传入路径
      const url = `/emps/${id}`;

      // 发送 DELETE 请求
      this.$axios.delete(url)
        .then(response => {
          // 请求成功后的处理逻辑
          // 例如更新表格数据，移除已删除的行
          this.fetchData();

          if (response.data.code == 1) {
            // 显示成功消息
            this.$message({
              message: '删除成功',
              type: 'success'
            });
          } else {
            this.$message(response.data.data);
          }

          // 删除后关闭对话框
          this.closeDeleteDialog(id);
        })
        .catch(error => {
          // 请求失败后的处理逻辑
          console.error('删除错误:', error);

          // 显示错误消息
          this.$message({
            message: '删除失败，请稍后再试',
            type: 'error'
          });
        });
    },
    closeDeleteDialog(id) {
      this.$set(this.deleteDialogVisible, id, false); // 隐藏删除确认对话框
    },
    handleClose(done) {
      done();
    },

    // 新增员工表单及编辑员工表单提交
    submitForm(Form) {
      console.log("Form:", Form);
      // 验证用户名
      if (!Form.username) {
        this.$message.error('用户名是必填项');
        return;
      } else if (Form.username.length < 2 || Form.username.length > 20) {
        this.$message.error('用户名长度必须在2到20个字符之间');
        return;
      } else if (!/^[a-zA-Z0-9]+$/.test(Form.username)) {
        this.$message.error('用户名只能包含字母和数字');
        return;
      }

      // 验证员工姓名
      if (!Form.name) {
        this.$message.error('用户姓名是必填项');
        return;
      } else if (Form.name.length < 2 || Form.name.length > 10) {
        this.$message.error('用户姓名长度必须在2到10个字符之间');
        return;
      } else if (!/^[\u4e00-\u9fa5]+$/.test(Form.name)) {
        this.$message.error('用户姓名只能包含汉字');
        return;
      }

      // 验证性别
      if (!Form.gender) {
        this.$message.error('性别是必填项');
        return;
      }

      // 图像
      // this.imageUrl是新上传图片的url，而this.originalImage是原来图像的url
      if (this.imageUrl) {
        Form.image = this.imageUrl;
      } else {
        Form.image = this.originalImage;
      }

      // 
      // 进行唯一性验证，假设有一个函数 checkUsernameUnique 进行异步验证
      if (Object.prototype.hasOwnProperty.call(Form, 'id')) {
        this.$axios.put('/emps', Form)
          .then(response => {
            this.$message.success('提交成功', response);
            this.EditFormVisible = false;
            this.fetchData();
          })
          .catch(error => {
            this.$message.error('提交失败: ' + error.message);
          });

      } else {
        // 
        this.checkUsernameUnique(Form.username).then(isUnique => {
          if (!isUnique) {
            this.$message.error('当前用户名已存在，请重新输入');
            return;
          }

          // 验证通过，提交表单数据
          this.$axios.post('/emps', Form)
            .then(response => {
              this.$message.success('提交成功', response);
              this.cancelSubmit();
              this.fetchData();
            })
            .catch(error => {
              this.$message.error('提交失败: ' + error.message);
            });
        });
      }
    },

    // 检查Username是否重复
    checkUsernameUnique(username) {
      return new Promise((resolve, reject) => {
        this.$axios.get("/emps/username", { params: { username } })
          .then(response => {
            if (response.data && response.data.data === 0) {
              resolve(true); // 用户名唯一
            } else {
              resolve(false); // 用户名已存在
            }
          })
          .catch(error => {
            console.error('检查用户名唯一性时出错:', error);
            reject(error); // 请求失败
          });
      });
    },

    // 刷新数据
    fetchData() {
      this.$axios.get("/emps")
        .then((response) => {
          console.log("Response data:", response.data.data);
          this.tableData = response.data.data.rows;
          console.log("rows:", this.tableData);
          this.totalRecords = response.data.data.total;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  computed: {
    jobTitlesMap() {
      return this.jobTitles.reduce((map, job) => {
        map[job.value] = job.label;
        return map;
      }, {});
    },

    uploadHeaders() {
      return {
        token: `${localStorage.getItem('token')}`,
      };
    },
  },
  mounted() {
    this.searchSubmit(); // 组件挂载时获取初始数据
    this.fetchDeptData(); // 在组件创建时获取部门数据
  },
};
</script>

<style>
.no-underline {
  text-decoration: none;
}

.square {
  width: 6px;
  /* 长方形的宽度 */
  height: 30px;
  /* 长方形的高度 */
  background-color: rgb(2, 167, 240);
  /* 长方形的背景颜色 */
  display: inline-block;
  vertical-align: top;
  /* 垂直顶部对齐 */
}

.top-font {
  font-family: "Helvetica Neue";
  line-height: 30px;
  /* 调整行高以与长方形顶部对齐 */
  font-size: 18px;
  color: rgb(2, 167, 240);
  display: inline-block;
  vertical-align: top;
  /* 垂直顶部对齐 */
  margin-left: 7px;
  /* 与长方形之间的间距 */
}

.container {
  margin-bottom: 10px;
  /* 容器的下边距 */
}

.el-form:not(.first-form) {
  display: flex;
  flex-direction: column;
}

.el-form:not(.first-form) .el-form-item {
  margin-bottom: 20px;
  /* 根据需要调整间距 */
}

.el-form:not(.first-form) .el-form-item .el-input {
  width: 300px;
}

.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.avatar-uploader .el-upload:hover {
  border-color: #409EFF;
}

.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 100px;
  height: 100px;
  line-height: 100px;
  text-align: center;
}

.avatar {
  width: 100px;
  height: 100px;
  display: block;
}

.row {
  display: flex;
  justify-content: flex-start;
  /* 第一个元素在行的开始位置 */
  margin-top: 20px;
}

.block {
  margin-right: 0;
  /* 确保没有右边距 */
  margin-left: 350px;
  /* 向左增加外边距 */
}
</style>
