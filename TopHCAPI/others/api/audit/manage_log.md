[back to api overview](../api_overview.md#label_api)
### 管理操作日志相关接口
## /v1/operatelog/list
管理操作日志列表
### 请求类型
GET
### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-|集群uuid
 tenant|string| 否|-|租户uuid；过滤租户
 page_num|int|否|0|显示页码
 page_size|int|否|0|每页显示多少数据
 filter_start_time|int64|否|0|开始时间，时间戳
 filter_end_time|int64|否|0|结束时间，时间戳
 filter_str|string|否|-|过滤主机，资源，动作等字段

### 返回参数

名称|参数类型|描述
---|---|---
logs|object array|列表
total_count|int32|总数量

#### logs对象
名称|参数类型|描述
---|---|---
uuid|string|日志uuid
start_time|int64|开始时间
end_time|int64|结束时间
host_ip|string|主机ip
tenant_uuid|string|操作者所属的租户uuid
tenant_name|string|操作者所属的租户名称
user_uuid|string|操作者uuid
user_name|string|操作者名称
role|string|操作者角色
is_ldap|bool|是否LDAP用户
action_desc|action_desc object|操作动作(接口)描述
obj_tenant_uuid|string|操作对象所属的租户uuid
obj_tenant_name|string|操作对象所属的租户名称
obj_source_type|string|操作对象的所属资源类型
result|int|结果，0为成功
err_info|string|失败英文描述
err_info_cn|string|失败中文描述

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/operatelog/list?tenant=&page_num=0&page_size=20&filter_start_time=1572537600&filter_end_time=1572969600&filter_str=485&cluster_uuid=b088822c-1176-4c79-9df7-5fad80c7fd1d
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
  "data": {
    "total": 1,
    "logs": [
      {
        "uuid": "59ef3384-7c36-4c2c-9011-7d66e2c691c7",
        "ctime": 1572596721171650299,
        "start_time": 1572596719,
        "end_time": 1572596721,
        "cluster_uuid": "b088822c-1176-4c79-9df7-5fad80c7fd1d",
        "cluster_name": "",
        "host_ip": "10.30.12.161",
        "remote_ip": "10.30.1.157",
        "tenant_uuid": "system",
        "tenant_name": "system",
        "user_uuid": "admin-1234567890987654321",
        "user_name": "admin",
        "role": "管理员",
        "is_ldap": false,
        "action_desc": {
          "cn": "内置卷快照创建",
          "en": "InternalVolume Snapshot Create"
        },
        "obj_tenant_uuid": "8b69bb2f-2a6e-4149-9f43-8d2e2b780df1",
        "obj_tenant_name": "billing_15版本测试",
        "obj_source_type": "Volume",
        "obj_uuid": "",
        "obj_name": "485",
        "result": 0,
        "err_info": "",
        "err_info_cn": "",
        "desc": ""
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码
