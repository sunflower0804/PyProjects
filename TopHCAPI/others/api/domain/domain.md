[back to api overview](../api_overview.md#label_api)

### 域相关接口
## /v1/domain/list
域列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 filter_name|string|否|-|按名称过滤
 filter_no_system|bool|否|false|是否过滤掉系统域
 page_num|int|否|0|第几页
 page_size|int|否|0|每页条数
### 返回参数

名称|参数类型|描述
---|---|---
List|array|列表
TotalCount|int|总数

### List对象

名称|参数类型|描述
---|---|---
name|string|域名称
uuid|string|域uuid
hosts_num|int|主机数量

### 示例

#### 请求示例
```
http://192.168.201.212:8080/v1/domain/list?page=0&number=8&filter_no_system=true&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
    "List": [
      {
        "name": "dom187191",
        "uuid": "90a9c3c9-f3e7-4179-89bf-5e5a20a1ae17",
        "hosts_num": 0
      },
      {
        "name": "dom186190",
        "uuid": "35eb616c-7f1b-4ff6-bf58-586e0114f988",
        "hosts_num": 0
      }
    ],
    "TotalCount": 2
  }
}
```

#### 异常返回示例

### 状态码



## /v1/domain/add
域添加
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-| 集群uuid
name|string|是|-|域名称

### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://10.30.10.23:8080/v1/domain/add
```

Body:
```
{
	"name": "test",
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


## /v1/domain/delete
域删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-| 集群uuid
name|string|是|-|域名称
domain_uuid|string|是|-|域uuid

### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://10.30.10.23:8080/v1/domain/delete
```

Body:
```
{
	"name": "test",
	"domain_uuid": "387ac7ad-d510-4195-859d-8a25dc22b6b9",
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
