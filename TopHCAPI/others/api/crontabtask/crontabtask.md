[back to api overview](../api_overview.md#label_api)

### 定时任务相关接口
## /v1/crontabtask/list
任务列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 tenant|string|否|-| 租户uuid
 filter_name|string|否|-|按名称过滤
 filter_task_type|int|否|0|按任务类型过滤
 page_num|int|否|0|第几页
 page_size|int|否|0|每页条数
### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.212:8080/v1/crontabtask/list?tenant=2fd69493-5005-4a2e-9e60-f6923040a48d&filter_name=&filter_task_type=0&page_size=10&page_num=0&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
        "tenant": "9e14dd59-1aaa-4d51-947f-9154aa49e969",
        "tenant_name": "manager",
        "namespace": "9e14dd59-1aaa-4d51-947f-9154aa49e969",
        "uuid": "c817a8aa-3ea9-4772-ba54-bce5076a6795",
        "compute_uuid": "2a9ea059-45b1-446d-86e8-6f2d4007fb3d",
        "compute_name": "api-test",
        "backup_point_uuid": "d2a76be2-859d-4aa8-8fd8-e11acc885330",
        "backup_point_name": "manager备份点",
        "name": "back1",
        "description": "",
        "create_time": 1573030786,
        "status": 0,
        "disks": [
          {
            "target_device": "sda",
            "backup_uuid": "42223920-d9f0-4714-9e73-c97519dd69a7",
            "capacity": 1073741824
          }
        ]
      }
    ],
    "total_count": 1
  }
}
```

#### 异常返回示例

### 状态码


## /v1/crontabtask/add
添加任务
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
http://10.30.10.23:8080/v1/crontabtask/add
```

Body:
```
{
	"tenant": "2fd69493-5005-4a2e-9e60-f6923040a48d",
	"task_name": "222",
	"task_duration": 86400,
	"task_id": 6,
	"object_uuid": "10c1efec-b0bd-49ff-9500-b44794580b9c",
	"backup_point_uuid": "73803fea-8eff-4772-be15-dcebff1cdab0",
	"specific_execute_time": 1573038659,
	"limit_executed_time": 86400,
	"task_type": 0,
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


## /v1/crontabtask/delete
删除任务
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
http://10.30.10.23:8080/v1/crontabtask/delete
```

Body:
```
{
	"tenant": "2fd69493-5005-4a2e-9e60-f6923040a48d",
	"task_uuid": "428e1e7d-3e2c-41b0-a301-66fe85c2f405",
	"task_name": "222",
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


## /v1/crontabtask/edit
编辑任务
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
http://10.30.10.23:8080/v1/crontabtask/edit
```

Body:
```
{
	"tenant": "2fd69493-5005-4a2e-9e60-f6923040a48d",
	"task_name": "gg_centos_lv_backup_yask1",
	"task_duration": 3600,
	"task_description": "",
	"object_uuid": "76650c41-75e2-423f-9958-f452bdddd22a",
	"specific_execute_time": 1573034181,
	"limit_executed_time": 86400,
	"task_uuid": "37351657-de4c-4fa2-8094-01e264f9efc8",
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


## /v1/crontabtask/start
任务启动
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
http://10.30.10.23:8080/v1/crontabtask/start
```

Body:
```
{
	"tenant": "2fd69493-5005-4a2e-9e60-f6923040a48d",
	"task_uuid": "37351657-de4c-4fa2-8094-01e264f9efc8",
	"task_name": "gg_centos_lv_backup_yask1",
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

## /v1/crontabtask/stop
任务停止
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
http://10.30.10.23:8080/v1/crontabtask/stop
```

Body:
```
{
	"tenant": "2fd69493-5005-4a2e-9e60-f6923040a48d",
	"task_uuid": "37351657-de4c-4fa2-8094-01e264f9efc8",
	"task_name": "gg_centos_lv_backup_yask1",
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
