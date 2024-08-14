package com.example.mybatisdemo.utils;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;

import java.util.Date;
import java.util.Map;

public class JwtUtils {
    private static String signKey = "empDept";
    private static Long expire = 3600000L;

    // 生成jwt
    public static String generateJWT(Map<String,Object> claims){
        String jwt = Jwts.builder()
                .addClaims(claims)    // 自定义内容（载荷）
                .signWith(SignatureAlgorithm.HS256, signKey)  // 签名算法
                .setExpiration(new Date(System.currentTimeMillis()+expire))  // 有效期
                .compact();
        return jwt;
    }

    // 解析jwt
    public static Claims parseJWT(String jwt){
        Claims claims = Jwts.parser()
                .setSigningKey(signKey)
                .parseClaimsJws(jwt).getBody();
        return claims;
    }
}
