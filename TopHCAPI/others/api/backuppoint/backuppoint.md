[back to api overview](../api_overview.md#label_api)

### 备份点相关接口
## /v1/volume/internal/backuppoint/add
备份点添加
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-|集群uuid
 tenant|string|是|-|租户uuid
 zone_uuid|string|是|-|资源池uuid
 name|string|是|-|备份点名称
 btype|string|是|-|备份点类型
 ip|string|是|-|主机IP
 root_dir|string|是|-|备份点根目录
 sub_dir|string|否|-|备份点子目录
 pass_word|string|否|-|如需加密，则需要填写

### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/volume/internal/backuppoint/add
```

Body:
```
{
	"tenant": "8b69bb2f-2a6e-4149-9f43-8d2e2b780df1",
	"name": "nfs_type",
	"btype": "nfs",
	"ip": "10.30.12.165",
	"root_dir": "/exports/eaee0463-d336-419e-aff1-29609f1e8af2/data",
	"pass_word": "",
	"env": {},
	"sub_dir": "zhanghailiang",
	"cluster_uuid": "b088822c-1176-4c79-9df7-5fad80c7fd1d"
}
```

#### 正常返回示例
```
{
  "message": "success",
  "message_cn": "成功",
  "scode": 0,
  "desc": "",
  "stack": null,
  "data": {
    "uuid": "",
    "name": ""
  }
}
```

#### 异常返回示例

### 状态码

## v1/volume/internal/backuppoint/delete
备份点删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-|集群uuid
 uuid|string|是|-|备份点uuid
 tenant|string|否|-|备份点所属租户名称，用于记录操作日志
 backup_point_name|string|否|-|备份点名称，用于记录操作日志

### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/volume/internal/backuppoint/delete
```

Body:
```
{
	"tenant": "fa81a25f-7dfa-41aa-8273-eb9e455d4d36",
	"uuid": "a5bc6ddc-55c9-4715-967e-73723bfa6fac",
	"backup_point_name": "rer",
	"cluster_uuid": "b088822c-1176-4c79-9df7-5fad80c7fd1d"
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
  "data": {}
}
```

#### 异常返回示例

### 状态码


## v1/volume/internal/backuppoint/update
备份点更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-|集群uuid
 tenant_uuid|string|是|-|租户uuid
 backup_point_uuid|string|是|-|备份点uuid
 backup_point_name|string|是|-|备份点名称
 ip|string|是|-|主机IP
 root_directory|string|是|-|备份点根目录
 sub_dir|string|是|-|备份点子目录

### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/volume/internal/backuppoint/update
```

Body:
```
{
	"tenant_uuid": "8b69bb2f-2a6e-4149-9f43-8d2e2b780df1",
	"backup_point_uuid": "d2ac682b-8243-4870-b352-70db99b3a1c2",
	"backup_point_name": "nfs_type_1",
	"ip": "10.30.12.165",
	"root_directory": "/exports/eaee0463-d336-419e-aff1-29609f1e8af2/data",
	"environment": {},
	"sub_dir": "zhanghailiang",
	"cluster_uuid": "b088822c-1176-4c79-9df7-5fad80c7fd1d"
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
  "data": {}
}
```

#### 异常返回示例

### 状态码


## /v1/volume/internal/backuppoint/list
备份点列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-|集群uuid
 tenant|string|否|-|租户uuid
 page_num|int32|否|0|显示页码
 page_size|int32|否|0|每页显示多少数据
 filter_name|string|否|-|过滤名称

### 返回参数

名称|参数类型|描述
---|---|---
list|object array|列表
total_count|int32|总数量

#### list对象
名称|参数类型|描述
---|---|---
tenant|string|租户uuid
tenant_name|string|租户名称
Name|string|备份点名称
UUID|string|备份点uuid
BType|string|备份点类型
NsUUID|string|命名空间uuid
indentify|indentify object|备份点相关信息
Ctime|int64|创建时间
Mtime|int64|修改时间
Bpstate|string|备份点状态

#### indentify对象
名称|参数类型|描述
---|---|---
IP|string|主机IP
PORT|string|主机端口
RootDir|string|根目录
SubDir|string|子目录
Dest|string|描述
Pwd|string|密码
### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/volume/internal/backuppoint/list?tenant=8b69bb2f-2a6e-4149-9f43-8d2e2b780df1&page_num=0&page_size=10&filter_name=&cluster_uuid=b088822c-1176-4c79-9df7-5fad80c7fd1d
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
    "total_count": 1,
    "list": [
      {
        "tenant": "8b69bb2f-2a6e-4149-9f43-8d2e2b780df1",
        "tenant_name": "billing_15版本测试",
        "Name": "nfs_type_1",
        "UUID": "d2ac682b-8243-4870-b352-70db99b3a1c2",
        "BType": "nfs",
        "NsUUID": "8b69bb2f-2a6e-4149-9f43-8d2e2b780df1",
        "Ref": 0,
        "indentify": {
          "IP": "10.30.12.165",
          "PORT": "",
          "RootDir": "/exports/eaee0463-d336-419e-aff1-29609f1e8af2/data",
          "SubDir": "",
          "Dest": "",
          "Env": null,
          "Pwd": ""
        },
        "Ctime": 1572831538,
        "Mtime": 1572832135,
        "Bpstate": "healthy"
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码
