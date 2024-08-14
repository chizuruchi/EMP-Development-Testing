package com.example.mybatisdemo.service.impl;
import com.example.mybatisdemo.mapper.DeptMapper;
import com.example.mybatisdemo.pojo.Dept;
import com.example.mybatisdemo.service.DeptService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Service
public class DeptServiceImpl implements DeptService {
    @Autowired
    private DeptMapper deptMapper;
    @Override
    public List<Dept> list(){
        return deptMapper.list();
    }

    @Override
    public void del(Integer id) {
        deptMapper.del(id);
    }

    @Override
    public void insert(Dept dept) {
        deptMapper.insert(dept);
    }

    @Override
    public Dept selectbyid(Integer id) {
        return deptMapper.selectbyid(id);
    }

    @Override
    public void update(Dept dept) {
        LocalDateTime now = LocalDateTime.now();
        dept.setUpdate_time(now);
        deptMapper.update(dept);
    }
}
