[back to api overview](../api_overview.md#api)

# user websocket
* [/v1/user/connection](user.md#/v1/user/connection)
* [/v1/user/console](user.md#/v1/user/console)



## /v1/user/connection
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
token|string|是|-|用户token




名称|参数类型|描述 
---|---|---
version|string|版本号

#### 请求示例
```
http://192.168.201.212:8080/v1/user/connection
```

#### 正常返回示例
{
  "status_code": 0,
  "message_en": "",
  "message_cn": "",
  "data": null
}
#### 异常返回示例

### 状态码


## /v1/user/console
连接虚拟机终端
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
token|string|是|-|用户token
tenant_uuid|string|是|-|租户uuid
vm_uuid|string|是|-|虚拟机uuid


### 返回参数

名称|参数类型|描述 
---|---|---
leader|string|主节点
candidates|string array|成员列表
ready|bool|是否正常

### 示例

#### 请求示例
```
http://192.168.201.212:9990/v1/user/console
```

#### 正常返回示例
{
  "status_code": 0,
  "message_en": "",
  "message_cn": "",
  "data": null
}

#### 异常返回示例

### 状态码




