package com.example.mybatisdemo.utils;

import com.aliyun.oss.ClientException;
import com.aliyun.oss.OSS;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.OSSClientBuilder;
import com.aliyun.oss.OSSException;
import com.aliyun.oss.model.PutObjectRequest;
import com.aliyun.oss.model.PutObjectResult;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;
import org.springframework.web.multipart.MultipartFile;

import java.io.FileInputStream;
import java.io.InputStream;
import java.util.UUID;

@Component
public class Aliossutils {
    // Endpoint以华东1（杭州）为例，其它Region请按实际情况填写。
    @Value("${aliyun.oss.endpoint}")
    private String endpoint;
    // 填写Bucket名称，例如examplebucket。
    @Value("${aliyun.oss.bucketName}")
    private String bucketName;

    public String upload(MultipartFile file) throws Exception {
        if (file == null || file.isEmpty()) {
            throw new IllegalArgumentException("File is empty or null");
        }

        // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
        EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();
        try (InputStream inputStream = file.getInputStream()) {
            // 1.取文件名后缀，并且使用uuid随机生成文件名（避免文件名重复，覆盖掉其他同名文件）
            String originalFilename = file.getOriginalFilename();
            String fileName = UUID.randomUUID().toString() + originalFilename.substring(originalFilename.lastIndexOf('.'));

            // 上传文件到OSS
            OSS ossClient = new OSSClientBuilder().build(endpoint, credentialsProvider);
            ossClient.putObject(bucketName, fileName, inputStream);

            String url = "https://" + bucketName + "." + endpoint + "/" + fileName;
            ossClient.shutdown();
            return url;
        } catch (Exception e) {
            throw new RuntimeException("Failed to upload file", e);
        }
    }
} 