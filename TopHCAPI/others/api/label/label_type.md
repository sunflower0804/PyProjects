[back to api overview](../api_overview.md#label_api)

### 标签类型相关接口
## /v1/label/type/list
标签类型列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-| 租户uuid
 tenant|string| 是|-| 租户uuid
 filter_name|string|否|-|过滤标签名
 page_num|int32|否|0|显示页码
 page_size|int32|否|0|每页显示多少数据
### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.212:8080/v1/label/type/list?tenant=2fd69493-5005-4a2e-9e60-f6923040a48d&filter_name=test1&page_size=10&page_num=0&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
        "name": "test1",
        "label_uuid": "",
        "label_type_uuid": "91acd427-f43f-44d0-986d-4d879a4e8cb8",
        "label_type_name": "",
        "color": "",
        "label_type_color": "#396afc",
        "description": "",
        "reference": 0,
        "reference_object": null,
        "attr": null,
        "create_time": 1573096200,
        "value": null,
        "tenant": "2fd69493-5005-4a2e-9e60-f6923040a48d",
        "tenant_name": "gg_tenant",
        "namespace": "2fd69493-5005-4a2e-9e60-f6923040a48d",
        "labels": [
          {
            "Name": "label1",
            "UUID": "dd0d15cc-ba06-4ce9-9f0b-13744dcef19c",
            "LTypeUUID": "91acd427-f43f-44d0-986d-4d879a4e8cb8",
            "Color": "#396afc",
            "Desc": "",
            "Ref": 0,
            "RefObject": null,
            "Attr": null,
            "Ctime": 1573096221,
            "NsUUID": "2fd69493-5005-4a2e-9e60-f6923040a48d",
            "LTypeName": "test1",
            "Value": [
              "333"
            ]
          }
        ]
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/label/type/add
标签类型添加
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
http://192.168.201.147:9990/v1/label/type/add
```
Body:
```
{
	"tenant": "2fd69493-5005-4a2e-9e60-f6923040a48d",
	"name": "dsfdsf",
	"description": "sfsafd",
	"color": "#396afc",
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


## /v1/label/type/delete
标签类型删除
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
http://192.168.201.147:9990/v1/label/type/delete
```
Body:
```
{
	"tenant": "2fd69493-5005-4a2e-9e60-f6923040a48d",
	"uuid": "8269ff77-9a63-414d-9bba-8412a77ca8f2",
	"label_name": "dsfdsf",
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
    "name": "",
    "uuid": "",
    "description": "",
    "color": "",
    "label_nums": 0,
    "create_time": 0,
    "labels": null,
    "attr": null
  }
}
```

#### 异常返回示例

### 状态码


