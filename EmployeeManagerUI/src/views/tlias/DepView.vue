<template>
  <div>
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
          <!-- 蓝色框 -->
          <div class="container">
            <div class="square"></div>
            <div class="top-font">部门管理</div>
          </div>

          <el-button type="primary" @click="AddFormVisible = true">+新增部门</el-button>
          <el-dialog title="新增部门" :visible.sync="AddFormVisible">
            <el-form :model="AddForm">
              <el-form-item label="* 部门名称" :label-width="formLabelWidth">
                <el-input v-model="AddForm.name" autocomplete="off" placeholder="请输入部门名称，长度为2-10位"></el-input>
              </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button type="primary" @click="AddSubmit">
                保 存
              </el-button>
              <el-button @click="AddFormVisible = false">取 消</el-button>
            </div>
          </el-dialog>

          <el-table :data="tableData" style="width: 100%">
            <el-table-column prop="name" label="名称"> </el-table-column>
            <el-table-column prop="update_time" label="最后操作时间">
              <template slot-scope="scope">
                {{ scope.row.update_time.replace('T', ' ') }}
              </template>
            </el-table-column>
            <el-table-column label="操作">
              <template v-slot="scope">
                <el-row>
                  <el-button type="primary" @click="editRow(scope.row)">编辑</el-button>
                  <el-button type="danger" @click="confirmDelete(scope.row.id)">删除</el-button>
                </el-row>
                <!-- 编辑部门表单 -->
                <el-dialog title="编辑部门" :visible.sync="UpdateFormVisible[scope.row.id]">
                  <el-form :model="UpdateForm">
                    <el-form-item label="部门名称">
                      <el-input v-model="UpdateForm.name" autocomplete="off"></el-input>
                    </el-form-item>
                  </el-form>
                  <div slot="footer" class="dialog-footer">
                    <el-button type="primary" @click="save(scope.row.id, scope.row.name)">保 存</el-button>
                    <el-button @click="closeDialog(scope.row.id)">取 消</el-button>
                  </div>
                </el-dialog>
                <!-- 删除对话框 -->
                <el-dialog title="提示" :visible.sync="deleteDialogVisible[scope.row.id]" width="30%"
                  :before-close="handleClose">
                  <span>您确定要删除该部门吗?</span>
                  <span slot="footer" class="dialog-footer">
                    <el-button type="primary" @click="deleteRow(scope.row.id)">确 定</el-button>
                    <el-button @click="closeDeleteDialog(scope.row.id)">取 消</el-button>
                  </span>
                </el-dialog>

              </template>
            </el-table-column>
          </el-table>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
// 写JavaScript
import Vue from "vue";
import axiosInatance from "../../utils/Axios.ts";
Vue.prototype.$axios = axiosInatance;
export default {
  // vue对象
  data() {
    return {
      tableData: [],
      AddFormVisible: false,
      AddForm: {
        name: "",
      },
      UpdateForm: {
        name: "",
      },
      formLabelWidth: "120px",
      UpdateFormVisible: {},
      deleteDialogVisible: {}, // 用于跟踪删除对话框的可见性
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

    editRow(row) {
      this.UpdateForm = { ...row }; // 将当前行的数据复制到表单中
      this.$set(this.UpdateFormVisible, row.id, true); // 显示当前行的对话框
    },

    save(id, name) {
      // 校验表单输入内容是否符合要求
      if (!this.UpdateForm.name || this.UpdateForm.name.length < 2 || this.UpdateForm.name.length > 10) {
        this.$message.error("请输入部门名称，长度为2-10位");
        return;
      }

      if (name === this.UpdateForm.name) {
        this.$message.error("请更改部门名称");
        return;
      }

      // 使用 axios 发送 PUT 请求
      this.$axios.put('/depts', {
        id: id,
        name: this.UpdateForm.name
      })
        .then(response => {
          if (response.data.code === 1) {
            // 请求成功时弹出成功提示框
            this.$message.success("部门更新成功");
            this.UpdateFormVisible[id] = false; // 关闭对话框
            this.fetchDepts(); // 刷新部门列表
          } else {
            // 请求失败时弹出错误提示框
            this.$message.error(response.data.msg || "部门更新失败");
          }
        })
        .catch(error => {
          console.error("部门更新请求失败", error);
          this.$message.error("部门更新失败，请检查网络或服务器设置");
        });
    },

    closeDialog(id) {
      this.$set(this.UpdateFormVisible, id, false); // 隐藏对话框
    },
    handleClose(done) {
      done();
    },
    confirmDelete(id) {
      this.$set(this.deleteDialogVisible, id, true); // 显示当前行的删除确认对话框
    },

    deleteRow(id) {
      // 删除行的逻辑
      // 使用 axios 发送 DELETE 请求
      this.$axios.delete(`/depts/${id}`)
        .then(response => {
          if (response.data.code === 1) {
            // 请求成功时弹出成功提示框
            this.$message.success("部门删除成功");
            this.$set(this.deleteDialogVisible, id, false); // 关闭当前行的删除确认对话框
            this.fetchDepts(); // 刷新部门列表
          } else {
            // 请求失败时弹出错误提示框
            this.$message.error(response.data.msg || "部门删除失败");
          }
        })
        .catch(error => {
          console.error("部门删除请求失败", error);
          this.$message.error("部门删除失败，请检查网络或服务器设置");
        });
      this.closeDeleteDialog(id); // 删除后关闭对话框
    },

    closeDeleteDialog(id) {
      this.$set(this.deleteDialogVisible, id, false); // 隐藏删除确认对话框
    },

    AddSubmit() {
      // 校验表单输入内容是否符合要求
      if (!this.AddForm.name || this.AddForm.name.length < 2 || this.AddForm.name.length > 10) {
        this.$message.error("请输入部门名称，长度为2-10位");
        return;
      }

      // 使用 axios 发送 POST 请求
      this.$axios.post('/depts', {
        name: this.AddForm.name
      })
        .then(response => {
          if (response.data.code === 1) {
            // 如果请求成功，关闭对话框并刷新部门列表
            this.$message.success("部门新增成功");
            this.AddFormVisible = false;
            this.fetchDepts(); // 假设有一个方法来刷新部门列表
          } else {
            this.$message.error(response.data.msg || "部门新增失败");
          }
        })
        .catch(error => {
          console.error("部门新增请求失败", error);
          this.$message.error("部门新增失败，请检查网络或服务器设置");
        });
    },
    fetchDepts() {
      this.$axios.get("/depts")
        .then((response) => {
          console.log("Response data:", response.data.data);
          this.tableData = response.data.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    this.$axios.get("/depts")
      .then((response) => {
        console.log("Response data:", response.data.data);
        this.tableData = response.data.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

<style>
.no-underline {
  text-decoration: none;
}

;

.top-font {
  font-family: "Helvetica Neue";
  line-height: 1.7;
  font-size: 18px;
  display: flex;
  align-items: center;
  /* 垂直居中对齐文本和方框 */
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
</style>
