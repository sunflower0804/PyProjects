[back to api overview](../api_overview.md#label_api)
### 融合存储卷(内置卷)快照相关接口
## /v1/volume/internal/snapshot/list
内置卷快照列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
volume_uuid|string|是|-|卷uuid
tenant|string|是|-|租户uuid
filter_name|string|否|-|过滤名称
### 返回参数

名称|参数类型|描述
---|---|---
list|object array|列表
total_count|int32|总数量
#### list对象
名称|参数类型|描述
---|---|---
name|string|快照名称
uuid|string|快照uuid
volume|string|卷uuid
desc|string|快照描述
status|int32|快照状态,0表示健康
ctime|int64|创建时间
### 示例

#### 请求示例
```
http://192.168.201.213:8080/v1/volume/internal/snapshot/list?tenant=b3c011b0-6e4a-487e-b9af-022f869dc790&filter_name=&volume_uuid=8652dfcb-9c83-4f93-b964-b8c87942869a&cluster_uuid=b8205835-ee82-4aa0-8c8b-6269e85aabd5
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
    "list": [
      {
        "name": "snap2",
        "uuid": "0aebff34-d816-4f4f-858d-ba16205f7293",
        "volume": "e93606cd-5544-48c4-b44c-aa4e82a5f5dd",
        "desc": "快照描述2",
        "status": 0,
        "ctime": 1587520509,
        "attr": {
          "ActiveCreated": "false"
        }
      },
      {
        "name": "snap1",
        "uuid": "71e08fe6-21b5-4d15-bfdf-cd75020b7b94",
        "volume": "e93606cd-5544-48c4-b44c-aa4e82a5f5dd",
        "desc": "快照描述1",
        "status": 0,
        "ctime": 1587520035,
        "attr": {
          "ActiveCreated": "false"
        }
      }
    ],
    "total_count": 2
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/internal/snapshot/create
内置卷快照添加
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
volume_uuid|string|是|-|卷uuid
snapshot_name|string|是|-|快照名称
description|string|否|-|快照描述


### 返回参数

名称|参数类型|描述
---|---|---
uuid|string|新创卷uuid
name|string|新创卷名称

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/snapshot/create
```
Body:
```
{
  "message": "success",
  "message_cn": "成功",
  "scode": 0,
  "desc": "",
  "stack": null,
  "data": {
    "uuid": "71e08fe6-21b5-4d15-bfdf-cd75020b7b94",
    "name": "snap1"
  }
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


## /v1/volume/internal/snapshot/delete
融合存储卷快照删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
snapshot_name|string|否|-|快照名称
snapshot_uuid|string|是|-|快照uuid
volume_uuid|string|是|-|卷uuid


### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/snapshot/delete
```
Body:
```
{
	"tenant": "b3c011b0-6e4a-487e-b9af-022f869dc790",
	"volume_uuid": "8652dfcb-9c83-4f93-b964-b8c87942869a",
	"snapshot_name": "dfdf",
	"snapshot_uuid": "1f5adb32-9cdd-49b2-8688-6363fde8f477",
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



## /v1/volume/internal/snapshot/tree
融合存储卷快照树
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
volume_uuid|string|是|-|卷uuid
tenant|string|是|-|租户uuid

### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://192.168.201.213:8080/v1/volume/internal/snapshot/tree?tenant=b3c011b0-6e4a-487e-b9af-022f869dc790&volume_uuid=8652dfcb-9c83-4f93-b964-b8c87942869a&cluster_uuid=b8205835-ee82-4aa0-8c8b-6269e85aabd5
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
    "tree": {
      "root": "111",
      "nodes": {
        "111": {
          "children": [
            "222"
          ]
        },
        "222": {
          "children": [
            "333",
            "444"
          ]
        },
        "333": {
          "children": []
        },
        "444": {
          "children": [
            "head"
          ]
        },
        "head": {
          "children": []
        }
      }
    }
  }
}
```

#### 异常返回示例

### 状态码

