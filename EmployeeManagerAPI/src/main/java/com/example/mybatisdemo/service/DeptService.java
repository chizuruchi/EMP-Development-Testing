package com.example.mybatisdemo.service;

import com.example.mybatisdemo.pojo.Dept;

import java.util.List;

public interface DeptService {
    public List<Dept> list();
    public void del(Integer id);
    public void insert(Dept dept);
    public Dept selectbyid(Integer id);
    public void update(Dept dept);
}
