package com.example.mybatisdemo.mapper;

import com.example.mybatisdemo.pojo.Dept;
import org.apache.ibatis.annotations.*;

import java.util.List;

@Mapper
public interface DeptMapper {
    @Select("select * from dept")
    public List<Dept> list();

    @Delete("delete from dept where id = #{id}")
    public void del(Integer id);

    @Insert("INSERT INTO dept(name, create_time, update_time) VALUES (#{name}, #{create_time}, #{update_time})")
    public int insert(Dept dept);

    @Select("select * from dept where id = #{id}")
    public Dept selectbyid(Integer id);

    @Update("update dept set name = #{name}, update_time= #{update_time} where id =#{id}")
    public void update(Dept dept);
}
