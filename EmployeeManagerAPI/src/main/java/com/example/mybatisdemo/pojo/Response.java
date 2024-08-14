package com.example.mybatisdemo.pojo;


import lombok.Data;


@Data
public class Response<T> {
    private int code;
    private String msg;
    private T data; // 将数据类型改为泛型 T

    public Response(int code, String message, T data) {
        this.code = code;
        this.msg = message;
        this.data = data;
    }
}
