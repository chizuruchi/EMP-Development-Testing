import axios from 'axios';
import Vue from "vue";

// 创建axios实例
const axiosInatance = axios.create({
  baseURL: 'http://127.0.0.1:8080', // api的base URL
  timeout: 5000, // 设置请求超时时间
  responseType: 'json',
  withCredentials: true, // 是否允许带cookie这些
  headers: {
    'Content-Type': 'application/json;charset=utf-8',
  },
});

// 设置请求拦截器，在每个请求中添加 token
axiosInatance.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers['token'] = token;
  }
  return config;
}, error => {
  return Promise.reject(error);
});

// 设置响应拦截器
axiosInatance.interceptors.response.use(
  res => {
    const { code, msg, data } = res.data;

    if (code === 0 && msg === "NOT_LOGIN") {
      // 提示未登录信息
      Vue.prototype.$message({
        message: "未登录，请先登录",
        type: "warning",
      });

      // 跳转到登录页面
      window.location.href = "/";

      // 返回一个被拒绝的Promise，以防止继续处理
      return Promise.reject(new Error("未登录"));
    } else if (code === 1) {
      // 请求成功，返回响应信息
      return res;
    } else {
      // 其他失败情况，抛出错误信息
      return Promise.reject(new Error(msg || '请求失败'));
    }
  },
  (error) => {
    // 处理响应错误
    console.error('响应错误:', error);
    return Promise.reject(error);
  }
);

export default axiosInatance;
