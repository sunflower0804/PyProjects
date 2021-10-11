[back to api overview](../api_overview.md#api)


# /v1/authentication/login
用户登陆
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant|string| 是|-| 租户名，系统租户名为system
 user|string|是|-|用户名
 password|string|是|-|用户密码,
 

### 返回参数

名称|参数类型|描述 
---|---|---
user_role|string|角色
token|string|登陆token
user_uuid|string|用户uuid
user_name|string|用户名
ldap_enabled|bool|所在租户是否开启了ldap
tenant_uuid|string|租户uuid
default_cluster_uuid|string|用户默认集群uuid
is_deploy_mode|bool|系统当前是否处于部署模式

### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/authentication/login
```
Body:
```
{	
    "tenant": "system",
    "user": "admin",
    "password": "21232f297a57a5a743894a0e4a801fc3"
    
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
       "user_role": "administrator",
       "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJoaGgiLCJ0ZW5hbnQiOiI0YTdlMjQwYi0xNGFhLTExZTktYjBiOS01MjU2ZmYwMDM0MDAiLCJ1c2VyX3V1aWQiOiI0YTdlMjQwYi0xNGFhLTExZTktYjBiOS01MjU2ZmYwMDM0MDAiLCJyb2xlIjoiYWRtaW5pc3RyYXRvciIsImV4cCI6MTU0NzQwNjU0MCwiaWF0IjoxNTQ3MTA2NTQwfQ.7gTOb26ZxA22fJBuP0WLNammEcrvd-EVWsOpnJBeBHY",
       "user_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
       "user_name": "hhh",
       "ldap_enabled": 0,
       "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
       "default_cluster_uuid": "",
       "is_deploy_mode": false
  }
}
```

#### 异常返回示例

### 状态码

# /v1/authentication/logout
用户登出
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---

 

### 返回参数

名称|参数类型|描述 
---|---|---
user_uuid|string|用户uuid
user_name|string|用户名
tenant_uuid|string|租户uuid

### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/authentication/logout
```
Body:
```
{	
 
}
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "messageCn": "",
  "stack": null,
  "data": ""
}
```

#### 异常返回示例

### 状态码