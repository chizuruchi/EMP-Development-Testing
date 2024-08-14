package com.example.mybatisdemo.service.impl;

import com.example.mybatisdemo.mapper.EmpMapper;
import com.example.mybatisdemo.pojo.Emp;
import com.example.mybatisdemo.pojo.PageBean;
import com.example.mybatisdemo.service.EmpService;
import com.github.pagehelper.Page;
import com.github.pagehelper.PageHelper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.util.List;

@Service
public class EmpServiceImpl implements EmpService {
    @Autowired
    private EmpMapper empMapper;

    @Override
    public Emp listbyid(Integer id) {
        return empMapper.listId(id);
    }

    @Override
    public PageBean list(Integer page, Integer pagesize) {
        Integer total = empMapper.listCount();
        Integer start = (page-1)*pagesize;
        List<Emp> rows = empMapper.list(start,pagesize);
        return new PageBean(total,rows);
    }

    @Override
    public PageBean listbys(Integer page, Integer pagesize, String name, Short gender, LocalDate begin, LocalDate end) {
        PageHelper.startPage(page, pagesize);  // 用于分页查询
        List<Emp> listemp = empMapper.selectbyname(name, gender, begin, end);
        Page<Emp> p = (Page<Emp>) listemp;
        return new PageBean((int) p.getTotal(), p.getResult());
    }

    @Override
    public void deletebyids(Integer[] ids) {
        empMapper.deleteByIds(ids);
    }

    @Override
    public void insertEmp(Emp emp) {
        empMapper.insertEmp(emp);
    }

    @Override
    public List<Emp> listbyids(Integer[] ids) {
        return empMapper.selectbyids(ids);
    }

    @Override
    public void updatebyid(Emp emp) {
        empMapper.updateEmp(emp);
    }

    @Override
    public Integer selectByUsername(String username) {
        return empMapper.selectByUsername(username);
    }
}
