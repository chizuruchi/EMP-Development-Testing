<template>
  <div class="login-page">
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span class="login-title">员工管理后台系统</span>
      </div>
      <div class="login-form">
        <el-form :model="form" :rules="loginRules" ref="loginForm">
          <el-form-item prop="userName">
            <el-input type="text" v-model="form.userName" auto-complete="off" placeholder="请输入用户名">
              <template slot="prepend">
                <i style="font-size: 20px" class="el-icon-user"></i>
              </template>
            </el-input>
          </el-form-item>
          <el-form-item prop="passWord">
            <el-input type="password" v-model="form.passWord" auto-complete="off" placeholder="请输入密码">
              <template slot="prepend">
                <i style="font-size: 20px" class="el-icon-key"></i>
              </template>
            </el-input>
          </el-form-item>
          <el-form-item>
            <el-button style="width: 100%" type="primary" @click="handleLogin" :loading="loading">登录</el-button>
          </el-form-item>
        </el-form>
      </div>
    </el-card>
  </div>
</template>


<script>
import Vue from "vue";
import axiosInatance from "../../utils/Axios.ts";
Vue.prototype.$axios = axiosInatance;
export default {
  name: "UserLogin", // 改为多词名称
  data() {
    return {
      form: { // Declare the form object
        userName: '',
        passWord: '',
      },
      loginRules: { // Example rules, adjust as needed
        userName: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
        ],
        passWord: [
          { required: true, message: '请输入密码', trigger: 'blur' },
        ],
      },
      loading: false,
    };
  },
  methods: {
    handleLogin() {
      this.$refs.loginForm
        .validate()
        .then(() => {
          this.loading = true;

          // 发送登录请求
          this.$axios.post('/login', {
            username: this.form.userName,
            password: this.form.passWord,
          })
            .then(response => {
              if (response.data.code === 1) {  // 检查是否登录成功
                // 假设响应中包含 token
                const token = response.data.data;
                console.log("token:",token);

                // 将 token 存储在 localStorage 中
                localStorage.setItem('token', token);

                // 设置 Axios 请求头以便后续请求带上 token
                // this.$axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
                this.$axios.defaults.headers.common['token'] = token;

                // 重定向到员工管理页面
                this.$router.push("/emp");
              } else {
                // 登录失败处理
                this.$message({
                  message: response.data.msg || "登录失败，请检查用户名或密码。",
                  type: "error",
                });
              }
            })
            .catch(error => {
              this.$message({
                message: "登录失败，请检查网络或稍后再试。",
                type: "error",
              });
              console.error("登录错误:", error);
            })
            .finally(() => {
              this.loading = false;
            });
        })
        .catch(() => {
          this.$message({
            message: "输入错误！",
            type: "warning",
          });
        });
    }
  },
};
</script>

<style scoped>
.login-page {
  background-image: linear-gradient(180deg, #2af598 0%, #009efd 100%);
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-title {
  font-size: 20px;
}

.box-card {
  width: 375px;
}
</style>