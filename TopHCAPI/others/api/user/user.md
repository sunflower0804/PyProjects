[back to api overview](../api_overview.md#label_api)
### 用户相关接口
## /v1/user/list
用户列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
filter_name|string|否|-|过滤名称
page_num|int|否|0|第几页
page_size|int|否|0|每页数据条数
show_tenant_admin|bool|否|false|是否显示租户管理员
filter_no_ldap|bool|否|false|是否过滤不是ldap用户

### 返回参数

名称|参数类型|描述
---|---|---
list|array|用户列表
total_count|int|用户总数
#### list对象
名称|参数类型|描述
---|---|---
uuid|string|用户uuid
name|string|用户名称
email|string|用户邮箱
event_windows_popup_push|object|告警弹窗推送;1为最低级(提示)，4为最高级(紧急)
event_email_push|object|告警邮件推送;1为最低级(提示)，4为最高级(紧急)
phone|string|电话
description|string|描述
create_time|int64|创建时间
tenant|string|租户uuid
role|string|administrator为租户管理员
group|string|所在用户组
policys|array|用户角色uuid
default_cluster|string|默认集群
is_ldap|bool|是否为ldap用户
last_password_modify_time|int64|最近密码修改时间
### 示例

#### 请求示例
```
http://192.168.201.213:8080/v1/user/list?tenant=315aa203-1965-4e89-b493-18f2baffbbf5&page_num=0&page_size=10&filter_name=&show_tenant_admin=true&filter_no_ldap=true&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
    "list": [
      {
        "uuid": "315aa203-1965-4e89-b493-18f2baffbbf5",
        "name": "api-test",
        "email": "fewf@fdf.com",
        "event_windows_popup_push": {
          "push_level": 4,
          "push_enabled": true
        },
        "event_email_push": {
          "push_level": 4,
          "push_enabled": true
        },
        "phone": "",
        "description": "",
        "create_time": 1573111175,
        "tenant": "315aa203-1965-4e89-b493-18f2baffbbf5",
        "role": "administrator",
        "group": "",
        "policys": [
          "315aa203-1965-4e89-b493-18f2baffbbf5"
        ],
        "default_cluster": "",
        "is_ldap": false,
        "last_password_modify_time": 1573111175
      }
    ],
    "total_count": 1
  }
}
```

#### 异常返回示例

### 状态码



## /v1/user/add
用户添加(系统租户system添加的用户为管理员)
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant|string|是|-|租户uuid
user|string|是|-|用户名称
email|string|是|-|邮箱
password|string|是|-|密码
event_windows_popup_push|object|否|-|告警事件弹窗推送设置;不填会默认开启并设置等级
event_email_push|object|否|-|告警事件邮箱推送设置;不填会默认开启并设置等级
### event_windows_popup_push对象
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
push_level|int32|是|-|推送等级;1为最低级(提示)，4为最高级(紧急)
push_enabled|bool|否|false|是否开启推送

### event_email_push对象
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
push_level|int32|是|-|推送等级;1为最低级(提示)，4为最高级(紧急)
push_enabled|bool|否|false|是否开启推送

### 返回参数

名称|参数类型|描述
---|---|---
name|string|创建的用户名称
uuid|string|创建的用户uuid

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/user/add
```
Body:
```
{
  "email": "dsf@fd.com",
  "user": "rrr",
  "password": "21232f297a57a5a743894a0e4a801fc3",
  "event_windows_popup_push": {
    "push_level": 1,
    "push_enabled": true
  },
  "event_email_push": {
    "push_level": 1,
    "push_enabled": false
  },
  "tenant": "system",
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
    "name": "api--test1",
    "uuid": "20aed31c-2319-4bc9-9a66-249272719a90"
  }
}
```

#### 异常返回示例

### 状态码


## /v1/user/delete
用户删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant|string|是|-|租户uuid
user_name|string|是|-|用户名称
user|string|是|-|用户uuid


### 返回参数

名称|参数类型|描述
---|---|---
name|string|删除的用户名称
uuid|string|删除的用户uuid

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/user/delete
```
Body:
```
{
	"user": "20aed31c-2319-4bc9-9a66-249272719a90",
	"tenant": "315aa203-1965-4e89-b493-18f2baffbbf5",
	"user_name": "api--test1",
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
    "uuid": "20aed31c-2319-4bc9-9a66-249272719a90",
    "name": "api--test1"
  }
}
```

#### 异常返回示例

### 状态码


## /v1/user/password/modify
用户密码修改
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant|string|是|-|租户uuid
user_name|string|是|-|用户名称
user|string|是|-|用户uuid
old_password|string|是|-|用户旧密码
new_password|string|是|-|用户新密码


### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/user/password/modify
```
Body:
```
{
  "user": "0365f87a-b5fb-4e38-b7b1-51a13a9211da",
  "old_password": "21232f297a57a5a743894a0e4a801fc3",
  "new_password": "21232f297a57a5a743894a0e4a801fc3",
  "user_name": "zhl",
  "tenant": "system",
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


## /v1/user/password/set
用户密码设置
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant|string|是|-|租户uuid
user_name|string|是|-|用户名称
user|string|是|-|用户uuid
new_password|string|是|-|用户新密码


### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/user/password/set
```
Body:
```
{
	"user": "315aa203-1965-4e89-b493-18f2baffbbf5",
	"tenant": "315aa203-1965-4e89-b493-18f2baffbbf5",
	"new_password": "21232f297a57a5a743894a0e4a801fc3",
	"user_name": "api-test"
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
    "tenant": "",
    "name": "",
    "uuid": ""
  }
}
```

#### 异常返回示例

### 状态码


## /v1/user/password/reset
用户密码重置
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant|string|是|-|租户uuid
user_name|string|是|-|用户名称
user|string|是|-|用户uuid


### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/user/password/reset
```
Body:
```
{
	"user_uuid": "315aa203-1965-4e89-b493-18f2baffbbf5",
	"tenant": "315aa203-1965-4e89-b493-18f2baffbbf5",
	"user_name": "api-test",
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
  }
}
```

#### 异常返回示例

### 状态码

## /v1/user/email/modify
修改用户邮箱
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant|string|是|-|租户uuid
user_name|string|是|-|用户名称
user|string|是|-|用户uuid
email|string|是|-|用户邮箱


### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/user/email/modify
```
Body:
```
{
	"user": "315aa203-1965-4e89-b493-18f2baffbbf5",
	"email": "dsfd@fdfd.co",
	"tenant": "315aa203-1965-4e89-b493-18f2baffbbf5",
	"user_name": "api-test"
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



## /v1/user/event_level/modify
管理员告警设置
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant|string|是|-|租户uuid
user_name|string|是|-|用户名称
user|string|是|-|用户uuid
event_windows_popup_push|object|否|-|告警事件弹窗推送设置;不填会默认开启并设置等级
event_email_push|object|否|-|告警事件邮箱推送设置;不填会默认开启并设置等级
### event_windows_popup_push对象
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
push_level|int32|是|-|推送等级;1为最低级(提示)，4为最高级(紧急)
push_enabled|bool|否|false|是否开启推送

### event_email_push对象
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
push_level|int32|是|-|推送等级;1为最低级(提示)，4为最高级(紧急)
push_enabled|bool|否|false|是否开启推送

### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/user/event_level/modify
```
Body:
```
{
	"tenant": "system",
	"user": "69347874-085a-4b91-ab47-559bce0a2bac",
	"user_name": "zhl",
	"event_windows_popup_push": {
		"push_level": 2,
		"push_enabled": true
	},
	"event_email_push": {
		"push_level": 1,
		"push_enabled": false
	},
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



### /v1/user/cluster/allow/list
集群列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
filter_name|string|否|-|过滤集群名称
page_num|int|否|0|第几页
page_size|int|否|0|每页数据条数

### 返回参数

名称|参数类型|描述
---|---|---
total_count|int|集群总数
list|array|列表

### list对象
名称|参数类型|描述
---|---|---
name|string|集群名称
uuid|string|集群uuid
desc|string|集群描述
create_time|int64|创建时间
master_address|string|集群master节点ip
is_stop|bool|集群是否停止使用
is_stop|bool|集群是否健康
### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/user/cluster/allow/list?page_num=0&page_size=10&filte_rname=1113&username=zhl&cluster_uuid=185d4703-f815-47ef-94b7-1ae7ae0fc204
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
        "name": "cluster_2020_0820",
        "uuid": "7015835c-56a6-4773-937c-1dbcbe5dfba5",
        "desc": "",
        "create_time": 1597925922,
        "master_address": "10.30.10.68",
        "is_stop": false,
        "is_health": true
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/user/cluster/set/default
用户(调用当前接口的用户)设置默认操作集群
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid


### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/user/cluster/set/default
```
Body:
```
{
	"cluster_uuid": "4e6dd97b-e937-4b78-ad3d-10a716bc29a3"
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

