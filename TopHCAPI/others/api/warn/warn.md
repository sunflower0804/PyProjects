[back to api overview](../api_overview.md#label_api)
### 告警相关接口
## /v1/warn/event/list
告警信息列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
page_num | int| 否|0|页数
page_size|int|否|0|页码
cluster_uuid|string|是| |集群uuid
tenant|string|是| |租户uuid
filterReadStatus|int|否|0|过滤读取状态，0:全部, 1:已读, 2:未读 

### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/warn/event/list
```
Body:
```
{
"page_num":0,
"page_size":15,
"filterReadStatus":2,
"cluster_uuid":"db456c26-c352-4ce6-a2cb-4dbd2568137a"
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
    "TotalCount": 2,
    "Infos": [
      {
             "UUID": "44071502-8c1c-48df-86db-7672d239fabb",
             "Action": "CPU告警",
             "NodeIP": "10.30.12.76",
             "Level": 4,
             "ObjectType": "系统",
             "Object": "主机(10.30.12.76)/CPU",
             "Message": "主机(10.30.12.76)CPU已占用0.999917,超过阈值0.900000/建议[请尽快检查并降低该主机CPU使用率，否则可能会影响使用]",
             "Ctime": 1609314183,
             "Read": false,
             "ActionID": 1,
             "cluster_uuid": "db456c26-c352-4ce6-a2cb-4dbd2568137a",
             "cluster_name": "cluster_10_30_12_76",
             "cluster_mode": ""
           },
           {
             "UUID": "a80f3bd5-5632-4a33-8276-c3b21e4fa678",
             "Action": "CPU告警",
             "NodeIP": "10.30.12.76",
             "Level": 4,
             "ObjectType": "系统",
             "Object": "主机(10.30.12.76)/CPU",
             "Message": "主机(10.30.12.76)CPU已占用0.986720,超过阈值0.900000/建议[请尽快检查并降低该主机CPU使用率，否则可能会影响使用]",
             "Ctime": 1609310521,
             "Read": false,
             "ActionID": 1,
             "cluster_uuid": "db456c26-c352-4ce6-a2cb-4dbd2568137a",
             "cluster_name": "cluster_10_30_12_76",
             "cluster_mode": ""
           },
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/warn/event/delete
告警信息删除
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
http://192.168.201.147:9990/v1/warn/event/delete
```
Body:
```
{
	"UUID": [
		"b4a79c7d-1c66-472c-9397-42b0ad4a004f"
	],
	"cluster_uuid": "b8205835-ee82-4aa0-8c8b-6269e85aabd5"
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


## /v1/warn/set/read
告警信息设置已读
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---



### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/warn/set/read
```
Body:
```
{
	"UUID": [
		"9e3178c9-c5ad-4ac1-b2b6-7f076c36863e",
		"e7725d3f-a200-4c5a-b81e-d13850cc2829",
		"a7b71ffa-669f-4f79-bcc9-2e76c45933c3",
		"cf8bcb2e-2a58-4b2f-8b8d-e1a0e25f99aa"
	],
	"cluster_uuid": "b8205835-ee82-4aa0-8c8b-6269e85aabd5"
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
    "status": {
      "code": 0,
      "message": "",
      "messageCn": "",
      "stack": null,
      "desc": "",
      "UUID": ""
    },
    "TotalCount": 0,
    "Infos": null
  }
}
```

#### 异常返回示例

### 状态码


