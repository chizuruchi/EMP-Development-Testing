package com.example.mybatisdemo.controller;

import com.example.mybatisdemo.mapper.EmpMapper;
import com.example.mybatisdemo.pojo.Emp;
import com.example.mybatisdemo.pojo.PageBean;
import com.example.mybatisdemo.pojo.Response;
import com.example.mybatisdemo.service.impl.EmpServiceImpl;
import lombok.extern.slf4j.Slf4j;
import org.apache.ibatis.jdbc.Null;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;

@Slf4j
@CrossOrigin(origins = "http://localhost:7000")
@RestController
@RequestMapping("/emps")
public class EmpController {
    @Autowired
    private EmpServiceImpl empServiceImpl;

    //查询员工
    @GetMapping
    public Response selectbys(@RequestParam(defaultValue = "1") Integer page,
                            @RequestParam(defaultValue = "5") Integer pageSize,
                            @RequestParam(required = false) String name,
                            @RequestParam(required = false) Short gender,
                            @RequestParam(required = false) @DateTimeFormat(iso = DateTimeFormat.ISO.DATE) LocalDate begin,
                            @RequestParam(required = false) @DateTimeFormat(iso = DateTimeFormat.ISO.DATE) LocalDate end) {
        log.info("接收到的参数: page={}, pageSize={}, name={}, gender={}, startTime={}, endTime={}",
                page, pageSize, name, gender, begin, end);
        // 设置默认值
        if (begin != null || end != null){
            if (begin == null) {
                begin = LocalDate.of(1900, 1, 1);
            }
            if (end == null) {
                end = LocalDate.now();
            }
        }
        try{
            PageBean pageBean = empServiceImpl.listbys(page, pageSize, name, gender, begin, end);
            return new Response<>(1, "success", pageBean);
        }catch (Exception e){
            return new Response<>(0, "fail", e);
        }
    }

    //根据ID查询员工
    @GetMapping("/{id}")
    public Response selectbyid(@PathVariable Integer id){
        log.info("接收到的参数: id={}", id);
        try{
            Emp emp = empServiceImpl.listbyid(id);
            return new Response<>(1, "success",emp);
        }catch (Exception e){
            return new Response<>(0, "fail", e);
        }
    }

//    根据username查询数量
    @GetMapping("/username")
    public Response selectByUsername(String username){
        log.info("接收到的参数: username={}", username);
        try{
            Integer uni = empServiceImpl.selectByUsername(username);
            return new Response<>(1, "success",uni);
        }catch (Exception e){
            return  new Response<>(0,"fail",e);
        }
    }

    //删除员工
    @DeleteMapping("/{ids}")
    public Response deletebyids(@PathVariable Integer[] ids){
        log.info("接收到的参数：ids={}", ids);
        try{
            List<Emp> result = empServiceImpl.listbyids(ids);
            if (result.isEmpty()) {
                return new Response<>(0, "not that ids", null);
            } else {
                empServiceImpl.deletebyids(ids);
                return new Response<>(1, "success", null);
            }
        }catch (Exception e){
            return new Response<>(0, "fail", e);
        }
    }

    //新增员工
    @PostMapping
    public Response insertEmp(@RequestBody Emp emp){
        log.info("接收到的参数：emp={}", emp);
        if(emp.getUsername()=="" || !emp.getUsername().matches("^[a-zA-Z0-9]+$")){
            return new Response<>(0, "fail", "Must be a non-empty string containing only letters and numbers");
        }
        if(emp.getName() == "" || !emp.getName().matches("^[\\u4e00-\\u9fa5]+$")){
            return new Response<>(0, "fail", "Must be a non-empty string containing only Chinese characters");
        }
        try{
            LocalDateTime now = LocalDateTime.now();
            emp.setCreate_time(now);
            emp.setUpdate_time(now);
            empServiceImpl.insertEmp(emp);
            return new Response<>(1, "success", null);
        }catch (Exception e){
            return new Response<>(0, "fail", e);
        }
    }

    //修改员工
    @PutMapping
    public Response InsertEmp(@RequestBody Emp emp){
        log.info("接收到的参数：emp={}", emp);
        if(emp.getUsername()=="" || !emp.getUsername().matches("^[a-zA-Z0-9]+$")){
            return new Response<>(0, "fail", "Must be a non-empty string containing only letters and numbers");
        }
        if(emp.getName() == "" || !emp.getName().matches("^[\\u4e00-\\u9fa5]+$")){
            return new Response<>(0, "fail", "Must be a non-empty string containing only Chinese characters");
        }
        try{
            LocalDateTime now = LocalDateTime.now();
            emp.setUpdate_time(now);
            empServiceImpl.updatebyid(emp);
            return new Response<>(1, "success", null);
        }catch (Exception e){
            return new Response<>(0, "fail", e);
        }
    }
}
