package com.example.mybatisdemo.controller;

import com.example.mybatisdemo.pojo.Dept;
import com.example.mybatisdemo.pojo.Response;
import com.example.mybatisdemo.service.impl.DeptServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDateTime;
import java.util.List;

@CrossOrigin(origins = "http://localhost:7000")
@RestController
public class DeptController {
    @Autowired
    private DeptServiceImpl deptServiceImpl;

    //部门列表查询
    @GetMapping("/depts")
    public Response<List<Dept>> deptslist(){
        List<Dept> dept = deptServiceImpl.list();

        return new Response<>(1, "success", dept);
    }

    //删除部门
    @DeleteMapping("depts/{id}")
    public Response deptsdel(@PathVariable Integer id){
        if(deptServiceImpl.selectbyid(id) != null){
            deptServiceImpl.del(id);
            return new Response<>(1, "success",null);
        }else{
            return new Response<>(0, "No such department",null);
        }
    }

    //添加部门
    @PostMapping("/depts")
    public Response deptsadd(@RequestBody Dept dept){
        LocalDateTime now = LocalDateTime.now();
        dept.setCreate_time(now);
        dept.setUpdate_time(now);
        deptServiceImpl.insert(dept);
        return new Response<>(1, "success",null);
    }

    //根据ID查询
    @GetMapping("/depts/{id}")
    public Response deptsbyid(@PathVariable Integer id){
        Dept dept = deptServiceImpl.selectbyid(id);
        return new Response<>(1, "success",dept);
    }

    //修改部门
    @PutMapping("/depts")
    public Response deptsmod(@RequestBody Dept dept){
        if(deptServiceImpl.selectbyid(dept.getId()) != null){
            if(dept.getName() != ""){
                deptServiceImpl.update(dept);
                return new Response<>(1, "success",null);
            }else{
                return new Response<>(0, "Please enter the name of the department",null);
            }
        }else{
            return new Response<>(0, "Please enter the id of the department",null);
        }
    }
}
