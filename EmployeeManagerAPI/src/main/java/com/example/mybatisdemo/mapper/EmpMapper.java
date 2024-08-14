package com.example.mybatisdemo.mapper;

import com.example.mybatisdemo.pojo.Emp;
import org.apache.ibatis.annotations.*;

import java.time.LocalDate;
import java.util.List;

@Mapper
public interface EmpMapper {

    @Select("select count(*) from emp")
    Integer listCount();

    @Select("select * from emp limit #{start},#{pagesize}")
    List<Emp> list(@Param("start") Integer start, @Param("pagesize") Integer pagesize);

    @Select("select * from emp where id = #{id}")
    Emp listId(int id);

    @Delete("delete from emp where id = #{id}")
    void deleteId(int id);

//    @Insert("INSERT INTO emp(username, password, name, gender, image, job, entrydate,dept_id, create_time, update_time) VALUES\n" +
//            "    (#{username},#{password},#{name},#{gender},#{image},#{job},#{entrydate},#{dept_id},#{create_time},#{update_time})")
    int insertEmp(Emp emp);

    List<Emp> selectbyname(@Param("name") String name,
                                  @Param("gender") Short gender,
                                  @Param("startTime") LocalDate startTime,
                                  @Param("endTime") LocalDate endTime);

    void updateEmp(Emp emp);

    void deleteByIds(Integer[] ids);

    List<Emp> selectbyids(Integer[] ids);

    @Select("select count(*)  from emp where username = #{username} and password = #{password}")
    Integer signbyPassword(@Param("username") String username, @Param("password")String password);

    @Select("select count(*) from emp where username = #{username} ")
    Integer selectByUsername(String username);
}
