package com.example.mybatisdemo.exception;

import com.example.mybatisdemo.pojo.Response;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice
public class GobalException {
    @ExceptionHandler(Exception.class)
    public Response ex(Exception e){
        return new Response<>(0,"fail",e.getMessage());
    }
}
