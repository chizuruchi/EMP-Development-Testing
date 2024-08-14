package com.example.mybatisdemo.controller;

import com.example.mybatisdemo.mapper.EmpMapper;
import com.example.mybatisdemo.pojo.Emp;
import com.example.mybatisdemo.pojo.Response;
import com.example.mybatisdemo.utils.JwtUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@CrossOrigin(origins = "http://localhost:7000")
@RestController
public class signController {
    @Autowired
    EmpMapper empMapper;
    @PostMapping("/login")
    public Response signbyPassword(@RequestBody Emp emp){
        Integer id = emp.getId();
        String username = emp.getUsername();
        String password = emp.getPassword();
        // 1.检查用户名和密码是否正确
        Integer result = empMapper.signbyPassword(username, password);
        // 2.正确的时候，返回jwt令牌
        if (result != 0){
            Map<String, Object> claims = new HashMap<>();
            claims.put("id",id);
            claims.put("username",username);
            String jwt = JwtUtils.generateJWT(claims);
            return new Response<>(1,"success",jwt);
        }else{
        // 3.错误的时候，返回错误信息
            return new Response<>(0,"login failed",null);
        }
    }
}
