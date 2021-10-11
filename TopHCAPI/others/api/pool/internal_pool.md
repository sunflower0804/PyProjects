[back to api overview](../api_overview.md#label_api)
### 融合存储存储池(内置池)相关接口
## /v1/pool/internal/list
融合存储池列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|否|-|集群uuid,不填默认所有集群
tenant|string|否|-|租户uuid
filter_name|string|否|-|过滤名称
page_num|int|否|0|第几页
page_size|int|否|0|每页数据条数

### 返回参数

名称|参数类型|描述
---|---|---
TotalCount|int|数量
List|object|卷列表
each_range_list_state|object|集群列表,由于可能有多个集群


### List对象
名称|参数类型|描述
---|---|---
tenant|sting|租户uuid
tenant_name|sting|租户名称
namespace|sting|命名空间uuid
name|sting|存储池名称
uuid|sting|存储池uuid
storage_size|uint64|存储池大小
used_size|uint64|已使用大小
available|uint64|可使用大小
create_time|int64|创建时间
volume_num|int|卷数量

### each_range_list_state对象
名称|参数类型|描述
---|---|---
cluster_uuid|sting|集群uuid
cluster_name|sting|集群名称
total_count|sting|集群存储池数量
result|object|获取该集群数据结果


### each_range_list_state对象
名称|参数类型|描述
---|---|---
scode|int|状态码,0表示成功
desc|string|描述
message|string|状态码对应英文描述
message_cn|string|状态码对应中文描述


### 示例

#### 请求示例
```
http://192.168.201.212:8080/v1/pool/internal/list?tenant=&page_num=0&page_size=10&filter_name=gg_pool2&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
    "List": [
      {
        "tenant": "6d40f98e-1a1f-40a4-8bfb-1897036b1255",
        "tenant_name": "TopHC",
        "namespace": "c91c1a95-6dc5-4628-b013-04c5a583c306",
        "name": "Repository",
        "uuid": "189857c3-02f4-4160-97bd-df78d423ef42",
        "storage_size": 0,
        "used_size": 558345748480,
        "available": 0,
        "create_time": 1593583067,
        "volume_num": 2,
        "attr": {
          "ComputeRepository": "ComputeRepository"
        },
        "cluster_uuid": "40898f97-2a97-4fbb-a1b4-e772ecc13689",
        "cluster_name": "cluster_name_113"
      },
      {
        "tenant": "6d40f98e-1a1f-40a4-8bfb-1897036b1255",
        "tenant_name": "TopHC",
        "namespace": "c91c1a95-6dc5-4628-b013-04c5a583c306",
        "name": "TopHC",
        "uuid": "36ed1968-6680-4e94-a823-a914c9ecca2c",
        "storage_size": 21990232555520000,
        "used_size": 12077448036352,
        "available": 21978155107483648,
        "create_time": 1593572017,
        "volume_num": 112,
        "attr": null,
        "cluster_uuid": "40898f97-2a97-4fbb-a1b4-e772ecc13689",
        "cluster_name": "cluster_name_113"
      }
    ],
    "each_range_list_state": [
      {
        "cluster_uuid": "40898f97-2a97-4fbb-a1b4-e772ecc13689",
        "cluster_name": "cluster_name_113",
        "namespace_uuid": "c91c1a95-6dc5-4628-b013-04c5a583c306",
        "result": {
          "scode": 0,
          "desc": "",
          "message": "success",
          "message_cn": "成功",
          "stack": null,
          "data": ""
        },
        "total_count": 2
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码

## /v1/pool/internal/get
存储池详情
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
pool_uuid|string|是|-|池uuid
filter_volume_name|string|否|-|过滤卷名称
volume_list_page_num|int|否|0|第几页
volume_list_page_size|int|否|0|每页数据条数

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.212:8080/v1/pool/internal/get?volume_list_page_num=0&volume_list_page_size=10&tenant=2fd69493-5005-4a2e-9e60-f6923040a48d&pool_uuid=ccb4157d-c6f7-402a-92f3-866c7a17883f&filter_volume_name=&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
    "pool": {
      "tenant": "2fd69493-5005-4a2e-9e60-f6923040a48d",
      "tenant_name": "",
      "namespace": "2fd69493-5005-4a2e-9e60-f6923040a48d",
      "name": "gg_pool2",
      "uuid": "ccb4157d-c6f7-402a-92f3-866c7a17883f",
      "storage_size": 10737418240,
      "used_size": 0,
      "available": 10737418240,
      "create_time": 1573025859,
      "volume_num": 0,
      "volumes": [],
      "filter_volume_num": 0
    }
  }
}
```

#### 异常返回示例

### 状态码


## /v1/pool/internal/delete
存储池删除
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
http://192.168.201.147:9990/v1/pool/internal/delete
```
Body:
```
{
	"tenant": "76373db8-e98d-4ad5-a373-9e9e4cd6048e",
	"pool_uuid": "bee8bf29-b759-4c9d-81a8-a91b75482b10",
	"pool_name": "pool_test",
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
    "pool": {
      "tenant": "",
      "tenant_name": "",
      "namespace": "",
      "name": "",
      "uuid": "",
      "storage_size": 0,
      "used_size": 0,
      "available": 0,
      "create_time": 0,
      "volume_num": 0
    }
  }
}
```

#### 异常返回示例

### 状态码



## /v1/pool/internal/create
存储池添加
### 请求类型
POST

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
pool_name|string|是|-|存储池名称
quota|object|是|-|存储池配额
#### quota对象

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
storage_size|uint64|是|-|存储池配额大小,单位字节

### 返回参数

名称|参数类型|描述
---|---|---
tenant|sting|租户uuid
tenant_name|sting|租户名称
namespace|sting|命名空间uuid
name|sting|存储池名称
uuid|sting|存储池uuid
storage_size|uint64|存储池大小,单位字节
used_size|uint64|已使用大小,单位字节
available|uint64|可使用大小,单位字节
create_time|int64|创建时间
volume_num|int|卷数量


### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/pool/internal/create
```
Body:
```
{
	"tenant": "76373db8-e98d-4ad5-a373-9e9e4cd6048e",
	"pool_name": "pool_test",
	"quota": {
		"storage_size": 21474836480
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
  "data": {
    "pool": {
      "tenant": "76373db8-e98d-4ad5-a373-9e9e4cd6048e",
      "tenant_name": "",
      "namespace": "76373db8-e98d-4ad5-a373-9e9e4cd6048e",
      "name": "pool_test",
      "uuid": "bee8bf29-b759-4c9d-81a8-a91b75482b10",
      "storage_size": 21474836480,
      "used_size": 0,
      "available": 21474836480,
      "create_time": 1573106887,
      "volume_num": 0
    }
  }
}
```

#### 异常返回示例

### 状态码



## /v1/pool/internal/quota/edit
存储池编辑
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
http://192.168.201.147:9990/v1/pool/internal/quota/edit
```
Body:
```
{
	"tenant": "76373db8-e98d-4ad5-a373-9e9e4cd6048e",
	"pool_uuid": "bee8bf29-b759-4c9d-81a8-a91b75482b10",
	"new_pool_name": "pool_test",
	"quota": {
		"storage_size": 10737418240
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



