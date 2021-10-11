[back to api overview](../api_overview.md#label_api)

### ntp服务相关接口
## /v1/ntp/server/add
ntp时间源添加
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
http://192.168.201.147:9990/v1/ntp/server/add
```
Body:
```
{
	"addrs": [
		"10.30.12.77"
	],
	"sync_period": 64,
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
    "status": [
      {
        "addr": "192.168.201.212",
        "loaded": "loaded",
        "status": "active",
        "time_stamp": 1573098164
      }
    ],
    "servers": [
      "10.30.12.77"
    ]
  }
}
```

#### 异常返回示例

### 状态码

## /v1/ntp/server/delete
ntp时间源删除
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
http://192.168.201.147:9990/v1/ntp/server/delete
```
Body:
```
{
    "cluster_uuid":"232671ca-d1e7-44ea-9278-a7c2d5920fa7"
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
    "status": [
      {
        "addr": "192.168.201.212",
        "loaded": "loaded",
        "status": "active",
        "time_stamp": 1573100134
      }
    ],
    "servers": null
  }
}
```

#### 异常返回示例

### 状态码

## /v1/ntp/server/list
ntp时间源列表
### 请求类型
GET

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
http://192.168.201.212:8080/v1/ntp/server/list?cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
    "addrs": [
      "10.30.12.77"
    ],
    "sync_period": 64,
    "date_source_status": [
      {
        "ip": "10.30.12.77",
        "status": true
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/ntp/zone/list
主时区列表
### 请求类型
GET

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
http://192.168.201.212:8080/v1/ntp/zone/list?cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
      "Africa",
      "America",
      "Antarctica",
      "Arctic",
      "Asia",
      "Atlantic",
      "Australia",
      "Brazil",
      "Canada",
      "Chile",
      "Etc",
      "Europe",
      "Indian",
      "Mexico",
      "Pacific",
      "SystemV",
      "US",
      "posix",
      "right"
    ],
    "total_count": 19
  }
}
```

#### 异常返回示例

### 状态码

## /v1/ntp/zone/country/list
次时区列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
zone|string|是|-|主时区

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.212:8080/v1/ntp/zone/country/list?zone=Atlantic&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
      "Azores",
      "Bermuda",
      "Canary",
      "Cape_Verde",
      "Faeroe",
      "Faroe",
      "Jan_Mayen",
      "Madeira",
      "Reykjavik",
      "South_Georgia",
      "St_Helena",
      "Stanley"
    ],
    "total_count": 12
  }
}
```

#### 异常返回示例

### 状态码



## /v1/ntp/zone/country/save
时区设置
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
http://192.168.201.147:9990/v1/ntp/zone/country/save
```
Body:
```
{
	"zone": "Atlantic",
	"country": "Azores",
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


## /v1/ntp/zone/country/current
当前时区获取
### 请求类型
GET

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
http://192.168.201.212:8080/v1/ntp/zone/country/current?cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
    "zone": "Asia",
    "country": "Chongqing"
  }
}
```

#### 异常返回示例

### 状态码


## /v1/ntp/system/current/time
当前时间获取
### 请求类型
GET

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
http://192.168.201.212:8080/v1/ntp/system/current/time?cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
    "time": 1573100124
  }
}
```

#### 异常返回示例

### 状态码



## /v1/ntp/force/time/sync
强制时间同步
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
http://192.168.201.147:9990/v1/ntp/force/time/sync
```
Body:
```
{
    "cluster_uuid":"232671ca-d1e7-44ea-9278-a7c2d5920fa7"
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

