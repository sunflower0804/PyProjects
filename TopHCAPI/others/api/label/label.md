[back to api overview](../api_overview.md#label_api)

### 标签相关接口
## /v1/label/list
标签列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-| 租户uuid
 tenant|string| 是|-| 租户uuid
 label_type_uuid|string| 是|-| 标签类型uuid
 filter_name|string|否|-|过滤标签名
 page_num|int32|否|0|显示页码
 page_size|int32|否|0|每页显示多少数据
### 返回参数

名称|参数类型|描述
---|---|---
list|object array|列表
total_count|int32|总数量
#### list对象
名称|参数类型|描述
---|---|---
label_name|string|标签名
label_uuid|string|标签uuid
label_type_uuid|string|标签类型uuid
label_description|string|标签描述
label_color|string|标签颜色
label_create_time|int64|标签创建时间
name_space_uuid|string|命名空间uuid

### 示例

#### 请求示例
```
http://192.168.201.212:8080/v1/label/list?tenant=2fd69493-5005-4a2e-9e60-f6923040a48d&label_type_uuid=28851a6e-b408-437d-a877-4f0f9c7bd4a0&page_num=0&filter_name=&page_size=10&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
        "name": "sssada",
        "label_uuid": "f3c74170-872e-4c01-8f8f-fe7130e12518",
        "label_type_uuid": "28851a6e-b408-437d-a877-4f0f9c7bd4a0",
        "label_type_name": "gg_label_style2",
        "color": "#396afc",
        "label_type_color": "",
        "description": "dafa",
        "reference": 0,
        "reference_object": [],
        "attr": {},
        "create_time": 1572955454,
        "value": [
          "dasdas"
        ],
        "tenant": "2fd69493-5005-4a2e-9e60-f6923040a48d",
        "tenant_name": "gg_tenant",
        "namespace": "2fd69493-5005-4a2e-9e60-f6923040a48d",
        "labels": null
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码



## /v1/label/add
标签添加
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
http://192.168.201.147:9990/v1/label/add
```
Body:
```
{
	"tenant": "2fd69493-5005-4a2e-9e60-f6923040a48d",
	"name": "label111",
	"description": "desc",
	"color": "#396afc",
	"label_type_uuid": "28851a6e-b408-437d-a877-4f0f9c7bd4a0",
	"value": [
		"222"
	],
	"ltype": "gg_label_style2",
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


## /v1/label/delete
标签删除
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
http://192.168.201.147:9990/v1/label/delete
```
Body:
```
{
	"tenant": "2fd69493-5005-4a2e-9e60-f6923040a48d",
	"uuid": "f3c74170-872e-4c01-8f8f-fe7130e12518",
	"label_name": "sssada",
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
    "label_uuid": "",
    "label_type_uuid": "",
    "label_type_name": "",
    "color": "",
    "label_type_color": "",
    "description": "",
    "reference": 0,
    "reference_object": null,
    "attr": null,
    "create_time": 0,
    "value": null,
    "tenant": "",
    "tenant_name": "",
    "namespace": "",
    "labels": null
  }
}
```

#### 异常返回示例

### 状态码


## /v1/label/update
标签编辑
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
http://192.168.201.147:9990/v1/label/update
```
Body:
```
{
	"tenant": "2fd69493-5005-4a2e-9e60-f6923040a48d",
	"uuid": "88e4dc48-354d-4110-b637-e278d888518f",
	"description": "desc",
	"color": "#396afc",
	"value": [
		"2223"
	],
	"reference": 0,
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


## /v1/label/host/list
主机获取已使用和未使用标签列表
### 请求类型
GET

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
http://192.168.201.212:8080/v1/label/host/list?tenant=2fd69493-5005-4a2e-9e60-f6923040a48d&domain_uuid=90a9c3c9-f3e7-4179-89bf-5e5a20a1ae17&host_uuid=6040ac60-6c0d-46f6-9af6-90e522e41fe9&host_name=192.168.201.187&filter_label_key=&page_num=0&page_size=5&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
    "used_list": [],
    "unused_list": [
      {
        "key": "system::secret",
        "used_values": [],
        "all_values": [
          "force",
          "optional",
          "disable"
        ]
      },
      {
        "key": "label111",
        "used_values": [],
        "all_values": [
          "2223"
        ]
      },
      {
        "key": "label1",
        "used_values": [],
        "all_values": [
          "333"
        ]
      },
      {
        "key": "gg_label_2",
        "used_values": [],
        "all_values": [
          "1111"
        ]
      },
      {
        "key": "gg_label1",
        "used_values": [],
        "all_values": [
          "123"
        ]
      }
    ],
    "used_label_total_count": 0,
    "unused_label_total_count": 7
  }
}
```

#### 异常返回示例

### 状态码

## /v1/label/list/host
绑定标签的主机列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant|string|是|-|租户uuid
cluster_uuid|string|是|-|集群uuid
filter_name|string|否|-|过滤宿主机名称
page_num|int32|否|0|显示页码
page_size|int32|否|0|每页显示多少数据
label_uuid|string|是|-|标签uuid


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://10.30.12.219:8080/v1/label/list/host?tenant=c7af6cd8-82b1-46a9-a7db-1293609c22ef&cluster_uuid=c123a9ab-1699-482e-aa69-60b68d2d6c7d&filter_name=&page_size=8&page_num=0&label_uuid=0a501af1-3afa-4278-acf8-21a8cee639ce
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
        "host_type": [
          "usm",
          "vsm",
          "hyper"
        ],
        "host_uuid": "24ee9e0d-f51f-4ff5-908b-795195bf3d52",
        "host_name": "10.30.12.218",
        "labels": {
          "yys": "yy"
        },
        "label_num": 1,
        "agent_status": 1,
        "host_mode": 0,
        "domain_name": "domain"
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码

## /v1/label/list/disk
绑定标签的磁盘列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant|string|是|-|租户uuid
cluster_uuid|string|是|-|集群uuid
filter_name|string|否|-|过滤宿主机名称
page_num|int32|否|0|显示页码
page_size|int32|否|0|每页显示多少数据
label_uuid|string|是|-|标签uuid


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://10.30.12.219:8080/v1/label/list/disk?tenant=c7af6cd8-82b1-46a9-a7db-1293609c22ef&cluster_uuid=c123a9ab-1699-482e-aa69-60b68d2d6c7d&filter_name=&page_size=8&page_num=0&label_uuid=0a501af1-3afa-4278-acf8-21a8cee639ce
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
        "disk_type": "HDD",
        "capacity": 107374182400,
        "hosy_uuid": "",
        "host_name": "10.30.12.218",
        "disk_uuid": "4126e835-8767-410e-9444-a98ade6e3434",
        "disk_name": "/dev/sdb",
        "labels": {
          "yys": "yy"
        },
        "label_num": 1
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码
