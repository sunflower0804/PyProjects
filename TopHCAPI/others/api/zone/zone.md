[back to api overview](../api_overview.md#label_api)
### 子集群相关接口
## /v1/zone/list
子集群列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
filter_name|string|否|-|过滤子集群名称
page_num|int|否|0|第几页
page_size|int|否|0|每页数量

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/zone/list?page_num=0&page_size=0&filter_name=&cluster_uuid=98323d75-61ce-47f9-8b4d-d83b27ad0469
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
    "total_count": 2,
    "list": [
      {
        "Name": "子集群191",
        "UUID": "c12cf7ea-829a-4b26-a8ad-ceaec7ed1736",
        "Domains": null,
        "Labels": null,
        "Func": [
          "Storage",
          "Compute",
          "Container"
        ],
        "Ctime": 1583485993,
        "RelatedZone": null,
        "Role": "master",
        "zonePolicy": null,
        "Status": 1,
        "RelatedZoneName": null,
        "Statistic": {
          "CpuUsed": 0.04730977020209994,
          "CpuTotal": 17.599968,
          "CpuUsage": 0.002688060012501156,
          "MemUsed": 664416256,
          "MemTotal": 6245687296,
          "MemUsage": 0.10638000663682283,
          "USDSizeUsed": 30279000064,
          "USDSizeTotal": 64393043968,
          "USDSIzeUsage": 0.47022159845475064,
          "HostCount": 1,
          "HostHealth": 1,
          "HostDown": 0,
          "VmCount": 0,
          "VmRunning": 0,
          "VmStopped": 0
        }
      },
      {
        "Name": "default",
        "UUID": "866982bd-73a8-4eb6-be60-8e227835c38b",
        "Domains": null,
        "Labels": null,
        "Func": [
          "Storage",
          "Compute",
          "Container"
        ],
        "Ctime": 1583485588,
        "RelatedZone": null,
        "Role": "master",
        "zonePolicy": null,
        "Status": 1,
        "RelatedZoneName": null,
        "Statistic": {
          "CpuUsed": 4.74816514311884,
          "CpuTotal": 48.399912,
          "CpuUsage": 0.09810276397029068,
          "MemUsed": 11053486080,
          "MemTotal": 17775046656,
          "MemUsage": 0.6218541247130215,
          "USDSizeUsed": 179531354112,
          "USDSizeTotal": 246839996416,
          "USDSIzeUsage": 0.7273187356940137,
          "HostCount": 3,
          "HostHealth": 2,
          "HostDown": 1,
          "VmCount": 17,
          "VmRunning": 10,
          "VmStopped": 7
        }
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/zone/inspect
子集群详情
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
zone_uuid|string|是|-|子集群uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/zone/inspect?cluster_uuid=98323d75-61ce-47f9-8b4d-d83b27ad0469&zone_uuid=1438f191-dc1e-4c2b-8f76-8ac782eb3d06
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
		"Name": "子集群190",
		"UUID": "1438f191-dc1e-4c2b-8f76-8ac782eb3d06",
		"Domains": null,
		"Labels": null,
		"Func": [
			"Storage",
			"Compute",
			"Container"
		],
		"Ctime": 1583486056,
		"RelatedZone": null,
		"Role": "master",
		"zonePolicy": null,
		"Status": 1,
		"RelatedZoneName": null,
		"Statistic": {
			"CpuUsed": 0.9814762323345894,
			"CpuTotal": 17.599968,
			"CpuUsage": 0.05576579641136787,
			"MemUsed": 2849275904,
			"MemTotal": 7302660096,
			"MemUsage": 0.39016959115496536,
			"USDSizeUsed": 23087095808,
			"USDSizeTotal": 64393043968,
			"USDSIzeUsage": 0.3585340028260364,
			"HostCount": 1,
			"HostHealth": 1,
			"HostDown": 0,
			"VmCount": 3,
			"VmRunning": 2,
			"VmStopped": 1
		}
	}
}
```

#### 异常返回示例

### 状态码



## /v1/zone/create
子集群添加
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
zone_name|string|是|-|子集群名称
zone_name|[]string|否|-|子集群功能类型,可选；目前有：Storage, Compute, Container，分别为存储，计算，容器


### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/zone/create
```
Body:
```
{
	"cluster_uuid":"98323d75-61ce-47f9-8b4d-d83b27ad0469",
	"zone_name":"zone_name1",
	"zone_function":["Storage"]
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


## /v1/zone/delete
子集群删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
zone_uuid|string|是|-|子集群uuid


### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/zone/delete
```
Body:
```
{
	"cluster_uuid":"98323d75-61ce-47f9-8b4d-d83b27ad0469",
	"zone_uuid":"e11813c1-6e4b-4e48-9236-3595922592b7"
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
	"data": {}
}
```

#### 异常返回示例

### 状态码


## /v1/zone/function/assign
分配子集群功能
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
zone_uuid|string|是|-|子集群uuid
zone_name|string|是|-|子集群名称,审计日志使用
zone_function|[]string|是|-|子集群功能类型,可选；目前有：Storage, Compute, Container，分别为存储，计算，容器


### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/zone/function/assign
```
Body:
```
{
	"zone_name": "子集群190",
	"zone_uuid": "1438f191-dc1e-4c2b-8f76-8ac782eb3d06",
	"zone_function": [
		"Storage"
	],
	"cluster_uuid": "98323d75-61ce-47f9-8b4d-d83b27ad0469"
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
	"data": {}
}
```

#### 异常返回示例

### 状态码


## /v1/zone/function/unassign
取消分配子集群功能
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
zone_uuid|string|是|-|子集群uuid
zone_name|string|是|-|子集群名称,审计日志使用
zone_function|[]string|是|-|子集群功能类型,可选；目前有：Storage, Compute, Container，分别为存储，计算，容器


### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/zone/function/unassign
```
Body:
```
{
	"zone_name": "子集群190",
	"zone_uuid": "1438f191-dc1e-4c2b-8f76-8ac782eb3d06",
	"zone_function": [
		"Storage"
	],
	"cluster_uuid": "98323d75-61ce-47f9-8b4d-d83b27ad0469"
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
	"data": {}
}
```

#### 异常返回示例

### 状态码


## /v1/zone/related_zone/add
添加延伸子集群
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
zone_uuid|string|是|-|子集群uuid
zone_name|string|是|-|子集群名称,审计日志使用
related_zone|[]string|是|-|延伸子集群uuid


### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/zone/related_zone/add
```
Body:
```
{
	"zone_name": "子集群190",
	"zone_uuid": "1438f191-dc1e-4c2b-8f76-8ac782eb3d06",
	"related_zone": [
		"c12cf7ea-829a-4b26-a8ad-ceaec7ed1736"
	],
	"cluster_uuid": "98323d75-61ce-47f9-8b4d-d83b27ad0469"
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
	"data": {}
}
```

#### 异常返回示例

### 状态码


## /v1/zone/related_zone/delete
删除延伸子集群
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
zone_uuid|string|是|-|子集群uuid
zone_name|string|是|-|子集群名称,审计日志使用
related_zone|[]string|是|-|延伸子集群uuid


### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/zone/related_zone/delete
```
Body:
```
{
	"zone_name": "子集群190",
	"zone_uuid": "1438f191-dc1e-4c2b-8f76-8ac782eb3d06",
	"related_zone": [
		"c12cf7ea-829a-4b26-a8ad-ceaec7ed1736"
	],
	"cluster_uuid": "98323d75-61ce-47f9-8b4d-d83b27ad0469"
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
	"data": {}
}
```

#### 异常返回示例

### 状态码



## /v1/zone/policy/update
更新子集群策略(是否自动接管)
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
zone_uuid|string|是|-|子集群uuid
zone_name|string|是|-|子集群名称,审计日志使用
policy|policy object|是|-|策略

#### policy对象
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
MasterTakeOver|bool|否|false|是否自动接管

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/zone/policy/update
```
Body:
```
{
	"zone_name": "子集群190",
	"zone_uuid": "1438f191-dc1e-4c2b-8f76-8ac782eb3d06",
	"policy": {
		"MasterTakeOver": false
	},
	"cluster_uuid": "98323d75-61ce-47f9-8b4d-d83b27ad0469"
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
	"data": {}
}
```

#### 异常返回示例

### 状态码



## /v1/zone/statistic/get
获取子集群统计信息
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/zone/statistic/get?cluster_uuid=98323d75-61ce-47f9-8b4d-d83b27ad0469
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
    "Name": "",
    "UUID": "",
    "Domains": null,
    "Labels": null,
    "Func": null,
    "Ctime": 0,
    "RelatedZone": null,
    "Role": "",
    "zonePolicy": null,
    "Status": 0,
    "RelatedZoneName": null,
    "Statistic": {
      "CpuUsed": 15.787582775479283,
      "CpuTotal": 83.59984800000001,
      "CpuUsage": 0.1888470272754477,
      "MemUsed": 14893461504,
      "MemTotal": 31323394048,
      "MemUsage": 0.4754740652043404,
      "USDSizeUsed": 234898653184,
      "USDSizeTotal": 375626084352,
      "USDSIzeUsage": 0.6253523463079735,
      "HostCount": 5,
      "HostHealth": 4,
      "HostDown": 1,
      "VmCount": 20,
      "VmRunning": 12,
      "VmStopped": 8
    }
  }
}
```

#### 异常返回示例

### 状态码

