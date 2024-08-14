package com.example.mybatisdemo.filter;

import com.alibaba.fastjson.JSONObject;
import com.example.mybatisdemo.pojo.Response;
import com.example.mybatisdemo.utils.JwtUtils;
import lombok.extern.slf4j.Slf4j;

import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@Slf4j
@WebFilter("/*")
public class LoginCheckFilter implements Filter {
    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        Filter.super.init(filterConfig);
        System.out.println("打开过滤器");
    }

    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        HttpServletRequest request = (HttpServletRequest) servletRequest;
        HttpServletResponse response = (HttpServletResponse) servletResponse;

        // 设置 CORS 响应头
        response.setHeader("Access-Control-Allow-Origin", "http://localhost:7000");
        response.setHeader("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS");
        response.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization, token");
        response.setHeader("Access-Control-Allow-Credentials", "true");

        // 处理 OPTIONS 预检请求
        if ("OPTIONS".equalsIgnoreCase(request.getMethod())) {
            response.setStatus(HttpServletResponse.SC_OK);
            return;
        }

        // 1.得到url
        String url = request.getRequestURL().toString();
        log.info("url:{}",url);
        // 2.检查url中是否含有login字样
        if(url.contains("login")){
            filterChain.doFilter(servletRequest,servletResponse);
            return;
        }
        // 3.无jwt直接return
        String token = request.getHeader("token");
        if(token == null || token.isEmpty()){
            log.info("未登录");
            Response<String> not_login = new Response<>(0, "NOT_LOGIN", null);
            // 手动转换为Json格式的字符串，使用fastjson需要提前在pom.xml中添加
            String s = JSONObject.toJSONString(not_login);
            response.getWriter().write(s);
            return;
        }
        // 4.有jwt检查其合法性，不合法return
        try {
            JwtUtils.parseJWT(token);
        }catch (Exception e){
            log.info("jwt不合法");
            Response<String> not_login = new Response<>(0, "NOT_LOGIN", null);
            String s = JSONObject.toJSONString(not_login);
            response.getWriter().write(s);
            return;
        }
        // 5.放行
        filterChain.doFilter(servletRequest,servletResponse);
    }

    @Override
    public void destroy() {
        Filter.super.destroy();
        System.out.println("关闭过滤器");
    }
}
