package com.example.mybatisdemo.controller;

import com.example.mybatisdemo.pojo.Response;
import com.example.mybatisdemo.utils.Aliossutils;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.util.UUID;

@Slf4j
@RestController
@CrossOrigin(origins = "http://localhost:7000")
@RequestMapping("/upload")
public class uploadController {
//    @PostMapping
//    public Response uploadImg(MultipartFile image){
////        1.取文件名后缀，并且使用uuid随机生成文件名（避免文件名重复，覆盖掉其他同名文件）
//        String filename = image.getOriginalFilename();
//        int index  = filename.lastIndexOf('.');
//        String extName = filename.substring(index);
//        String newFilename = UUID.randomUUID().toString()+extName;
////        2.本地存储接收到的文件
//        try {
//            image.transferTo(new File("E:\\heima\\uploadImage\\" + newFilename));
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//        return new Response<>(1,"success",null);
//    }

    @Autowired
    Aliossutils aliossutils;
    @PostMapping
    public Response uploadImg( @RequestParam("image") MultipartFile image){
        try {
            String fileURL = aliossutils.upload(image);
            return new Response<>(1,"success", fileURL);
        } catch (Exception e) {
            e.printStackTrace();
            return new Response<>(1,"success", e.getMessage());
        }
    }
}
