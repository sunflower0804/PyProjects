[back to api overview](../api_overview.md#label_api)
### 用户组相关接口
## /v1/usergroup/user/list
用户组用户列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant_uuid|string|是|-|租户uuid
group_uuid|string|否|-|
filter_complex|string|否|-|
filter_local|bool|否|false|
page_num|int|否|0|第几页
page_size|int|否|0|每页数据条数

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.213:8080/v1/usergroup/user/list?tenant_uuid=315aa203-1965-4e89-b493-18f2baffbbf5&group_uuid=e835d378-f6ca-40d8-85a2-accbcb97b841&filter_complex=&page_size=10&page_num=0&filter_local=true&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
```


#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "total_count": 1,
    "list": [
      {
        "bind_role": "",
        "group_name": "group1",
        "group_role": "租户管理员",
        "name": "user1",
        "uuid": "64a474fd-7391-4b98-89f4-85e4f6d78589",
        "create_time": 1573122291,
        "resource_version": 0,
        "kind": "User",
        "tenant": "315aa203-1965-4e89-b493-18f2baffbbf5",
        "password": "21232f297a57a5a743894a0e4a801fc3",
        "event_windows_popup_push": {
          "push_level": 4,
          "push_enabled": true
        },
        "event_email_push": {
          "push_level": 4,
          "push_enabled": true
        },
        "email": "1efd@fd.com",
        "phone": "",
        "description": "",
        "role": "normalUser",
        "group": "e835d378-f6ca-40d8-85a2-accbcb97b841",
        "default_cluster_uuid": "c5793204-f4ed-44ae-977a-63609adf2dcd",
        "latest_used_tenants": [],
        "is_ldap": false,
        "bind_policies": [],
        "login_fail_has_retry_times": 0,
        "last_login_time": 0,
        "last_password_modify_time": 1573122291
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码



## /v1/usergroup/create
用户组添加
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TODO


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/usergroup/create
```
Body:
```
{
	"tenant_uuid": "315aa203-1965-4e89-b493-18f2baffbbf5",
	"group_name": "group2",
	"role_uuid": "315aa203-1965-4e89-b493-18f2baffbbf5",
	"description": "",
	"cluster_uuid": "c5793204-f4ed-44ae-977a-63609adf2dcd"
}
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "usergroup_uuid": "72cff15f-ff2c-472e-a624-8d72eea7f5ae"
  }
}
```

#### 异常返回示例

### 状态码


## /v1/usergroup/delete
用户组删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TODO


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/usergroup/delete
```
Body:
```
{
	"tenant_uuid": "315aa203-1965-4e89-b493-18f2baffbbf5",
	"group_uuid": "f9e03447-5078-4032-9395-9521e4d1be11",
	"group_name": "group3",
	"cluster_uuid": "c5793204-f4ed-44ae-977a-63609adf2dcd"
}
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {}
}
```

#### 异常返回示例

### 状态码


## /v1/usergroup/update
用户组编辑
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TODO


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/usergroup/update
```
Body:
```
{
	"parent_group_uuid": "e835d378-f6ca-40d8-85a2-accbcb97b841",
	"tenant_uuid": "315aa203-1965-4e89-b493-18f2baffbbf5",
	"group_uuid": "72cff15f-ff2c-472e-a624-8d72eea7f5ae",
	"group_name": "group2",
	"role_uuid": "315aa203-1965-4e89-b493-18f2baffbbf5",
	"description": "",
	"cluster_uuid": "c5793204-f4ed-44ae-977a-63609adf2dcd"
}
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {}
}
```

#### 异常返回示例

### 状态码


## /v1/usergroup/structure/inspect
用户组结构详情
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-|集群uuid
 tenant_uuid|string|是|-|租户uuid


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.213:8080/v1/usergroup/structure/inspect?tenant_uuid=315aa203-1965-4e89-b493-18f2baffbbf5&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "Structure": [
      {
        "name": "group1",
        "uuid": "e835d378-f6ca-40d8-85a2-accbcb97b841",
        "create_time": 1573119305,
        "resource_version": 0,
        "kind": "UserGroup",
        "tenant": "315aa203-1965-4e89-b493-18f2baffbbf5",
        "level": "1",
        "description": "",
        "parent": "",
        "role_list": [
          {
            "uuid": "315aa203-1965-4e89-b493-18f2baffbbf5",
            "name": "租户管理员"
          }
        ],
        "parent_list": [],
        "children": [
          {
            "name": "group2",
            "uuid": "72cff15f-ff2c-472e-a624-8d72eea7f5ae",
            "create_time": 1573122471,
            "resource_version": 0,
            "kind": "UserGroup",
            "tenant": "315aa203-1965-4e89-b493-18f2baffbbf5",
            "level": "2",
            "description": "",
            "parent": "e835d378-f6ca-40d8-85a2-accbcb97b841",
            "role_list": [
              {
                "uuid": "315aa203-1965-4e89-b493-18f2baffbbf5",
                "name": "租户管理员"
              }
            ],
            "parent_list": [
              {
                "level": 1,
                "uuid": "e835d378-f6ca-40d8-85a2-accbcb97b841",
                "name": "group1"
              }
            ],
            "children": []
          }
        ]
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/usergroup/user/add
用户组绑定用户
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TODO


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/usergroup/user/add
```
Body:
```
{
	"tenant_uuid": "315aa203-1965-4e89-b493-18f2baffbbf5",
	"user_uuid": "027561e8-109f-494d-8332-3192eeb0ddc2",
	"group_uuid": "e835d378-f6ca-40d8-85a2-accbcb97b841",
	"group_name": "user11",
	"cluster_uuid": "c5793204-f4ed-44ae-977a-63609adf2dcd"
}
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {}
}
```

#### 异常返回示例

### 状态码

## /v1/usergroup/user/delete
用户组解绑用户
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TODO


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/usergroup/user/delete
```
Body:
```
{
	"tenant_uuid": "315aa203-1965-4e89-b493-18f2baffbbf5",
	"user_uuid": "22580334-7231-4b8b-8a32-24d813c5d5e6",
	"group_uuid": "e835d378-f6ca-40d8-85a2-accbcb97b841",
	"group_name": "777",
	"cluster_uuid": "c5793204-f4ed-44ae-977a-63609adf2dcd"
}
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {}
}
```

#### 异常返回示例

### 状态码

