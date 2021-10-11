

## /v1/network/security/group/add
#### 功能：添加安全组
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid
 security_group_name|string| 是|""  | 安全组名称

### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 security_group_name|string| 安全组名称

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/security/group/add
```
Body:
```
{	
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "name": "testname"
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "name": "testname"
  }
}
```

#### 异常返回示例

### 状态码



## /v1/network/security/group/del
功能：删除安全组
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|-  | 租户uuid
 security_group_uuid|string| 是|-  | 安全组uuid


### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 security_group_uuid|string| 安全组uuid


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/security/group/del
```
Body:
```
{	
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "security_group_uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400"
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "security_group_uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400"
  }
}
```

#### 异常返回示例

### 状态码





## /v1/network/security/acl/list
功能：获取安全组acl规则列表
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|-  | 租户uuid
 security_group_uuid|string| 是|-  | 安全组uuid
 page_num|int| 否|-  | 第几页
 page_size|int| 否|-  | 每一页的数目
 
### 返回参数
名称|参数类型|描述 
---|---|---
total_count|int|总数量
list|array|acl信息列表

#### list对象
名称|参数类型|描述
---|---|---
 priority|int|  优先级
 direction|string| 入口或出口
 action|string| 允许动作或者拒绝动作
 protocol|string| 协议类型
 port|int| acl端口
 remote|string| 远程地址，地址集或cidr
 switch_port|int| 交换机端口

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/security/acl/list?tenant_uuid=5c028587-305c-461a-b49d-2f9847f037e1&security_group_uuid=55b2edab-305c-461a-b49d-2f9847f037e1
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
   "total_count":10,
   "list":[
        {
          "priority":50,
          "direction":"to-lport",
          "action":  "allow",
          "protocol":"tcp",
          "port":5050,
          "retome":"192.168.201.56/24",
          "switch_port":8000
       }
   ]
  }
}
```

#### 异常返回示例
### 状态码


## /v1/network/security/info/list
功能：获取安全组列表
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid
 page_num|int| 否|-  | 第几页
 page_size|string| 否|-  | 每一页的数量
 filter_name|string| 否|""  | 要过滤的安全组的名称

### 返回参数
名称|参数类型|描述 
---|---|---
total_count|int|安全组数量
list|array|安全组列表

#### list对象
名称|参数类型|描述 
---|---|---
create_time|int64|创建时间
update_time|int64|修改时间
security_group_uuid|string|uuid
security_group_name|string|安全组名称
ext_ids|map[string]string|安全组额外信息

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/security/info/list?tenant_uud=1c64fac3-1324-11e9-b910-5254fffffffd
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "total_count": 1,
    "list":[
        {
            "create_time":1548139892,
            "update_time":1548139902,
            "uuid":"4a7e240b-14aa-11e9-b0b9-5256ff003400",
            "name":"testname",
            "ext_ids" :nil
        }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/network/security/group/template_rule/create
#### 功能：创建安全组模板
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/security/group/template_rule/create
```
Body:
```	
todo
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码


## /v1/network/security/group/template_rule/delete 
#### 功能：删除安全组模板
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/security/group/template_rule/delete 
```
Body:
```	
todo
```
#### 正常返回示例
```
tood
```

#### 异常返回示例

### 状态码



## /v1/network/security/group/link/create
#### 功能: 创建an'quan'xu
#### 请求类型：

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/security/group/link/create
```
Body:
```	
todo
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码



## /v1/network/security/group/link/delete 
#### 功能： 删除安全组连接实例
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/security/group/link/delete 
```
Body:
```	
todo
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码


## /v1/network/link/networked/list 
#### 功能：获取网络连接实例列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/link/networked/list 
```
Body:
```	
todo
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码


## /v1/network/switch/ip_pool/inspect
#### 功能：获取ip池详情
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/switch/ip_pool/inspect
```
Body:
```	
todo
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码

## /v1/network/float_container/list
#### 功能：获取游离的容器列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/float_container/list
```
Body:
```	
todo
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码







