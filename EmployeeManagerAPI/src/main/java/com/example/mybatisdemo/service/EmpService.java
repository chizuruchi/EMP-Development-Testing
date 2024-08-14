package com.example.mybatisdemo.service;

import com.example.mybatisdemo.pojo.Emp;
import com.example.mybatisdemo.pojo.PageBean;

import java.time.LocalDate;
import java.util.List;

public interface EmpService {
    PageBean list(Integer page, Integer pagesize);
    Emp listbyid(Integer id);
    List<Emp> listbyids(Integer[] ids);
    PageBean listbys(Integer page, Integer pagesize, String name, Short gender, LocalDate begin, LocalDate end);
    void deletebyids(Integer[] ids);
    void insertEmp(Emp emp);
    void updatebyid(Emp emp);
    Integer selectByUsername(String username);
}
