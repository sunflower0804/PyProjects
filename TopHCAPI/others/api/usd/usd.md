[back to api overview](../api_overview.md#label_api)
### usd(磁盘)相关接口
## /v1/storage/data_disk/list
数据盘列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
host_uuid|string|是|-|主机uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://10.30.10.24:8080/v1/storage/data_disk/list?host_uuid=d13a0be4-22f8-4d2d-82f8-8d43a9076b6a&cluster_uuid=3afdbbfc-e45a-430e-abba-842074a8b035
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
        "Name": "data-d7bff985-3a4a-4641-af7c-27a42dd58405",
        "UUID": "6e21fca5-4cb0-4c58-8d14-e66c927be30f",
        "HostUUID": "d13a0be4-22f8-4d2d-82f8-8d43a9076b6a",
        "Type": "HDD",
        "Device": "/dev/sdg",
        "Status": 1,
        "Usage": 0,
        "info": null,
        "Ctime": 1568948641,
        "GIndex": 8,
        "Capacity": 2000198885931,
        "Port": 60004,
        "Vendor": "",
        "HostIP": "10.30.10.21",
        "CacheDevice": "/dev/sdf",
        "Avail": 1286429208576,
        "Mode": 0
      }
    ],
    "total_count": 1
  }
}
```

#### 异常返回示例

### 状态码



## /v1/storage/physical_disk/list
物理盘列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
host_uuid|string|是|-|主机uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://10.30.10.24:8080/v1/storage/physical_disk/list?host_uuid=d13a0be4-22f8-4d2d-82f8-8d43a9076b6a&cluster_uuid=3afdbbfc-e45a-430e-abba-842074a8b035
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
        "Name": "/dev/sdg",
        "UUID": "",
        "HostUUID": "d13a0be4-22f8-4d2d-82f8-8d43a9076b6a",
        "Type": "HDD",
        "Device": "",
        "Status": 0,
        "Usage": 0,
        "info": null,
        "Ctime": 0,
        "GIndex": 0,
        "Capacity": 2000398934016,
        "Port": 0,
        "Vendor": "SEAGATE",
        "HostIP": "10.30.10.21",
        "CacheDevice": "",
        "Avail": 0,
        "Mode": 0
      }
    ],
    "total_count": 1
  }
}
```

#### 异常返回示例

### 状态码


## /v1/storage/unused/physical_disk/list
未使用的物理盘列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
host_uuid|string|是|-|主机uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://10.30.10.24:8080/v1/storage/unused/physical_disk/list?host_uuid=d13a0be4-22f8-4d2d-82f8-8d43a9076b6a&cluster_uuid=3afdbbfc-e45a-430e-abba-842074a8b035
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
        "type": "HDD",
        "path": "/dev/sdk",
        "is_sys_disk": false
      }
    ],
    "total_count": 1
  }
}
```

#### 异常返回示例

### 状态码



## /v1/storage/data_disk/create
添加数据盘到容量组
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
http://192.168.201.147:9990/v1/storage/data_disk/create
```
Body:
```
{
	"host_uuid": "d13a0be4-22f8-4d2d-82f8-8d43a9076b6a",
	"host_name": "10.30.10.21",
	"devices": [
		{
			"path": "/dev/sdh",
			"type": "HDD"
		}
	],
	"cluster_uuid": "3afdbbfc-e45a-430e-abba-842074a8b035"
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



## /v1/storage/disk/mode/set
磁盘模式设置
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
http://192.168.201.147:9990/v1/storage/disk/mode/set
```
Body:
```
{
	"mode": 3,
	"devices": [
		{
			"uuid": "beb6e3c3-8647-433d-84cf-d404e1ad9346",
			"path": "/dev/sdb"
		}
	],
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


## /v1/storage/cache_disk/mode/set
缓存盘模式设置
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
http://192.168.201.147:9990/v1/storage/cache_disk/mode/set
```
Body:
```
{
	"mode": 3,
	"host_uuid": "d13a0be4-22f8-4d2d-82f8-8d43a9076b6a",
	"devices": [
		{
			"name": "cache-1ff1199f-f6cb-4c9c-b1a0-0babc51a389e",
			"path": "/dev/sdb"
		}
	],
	"cluster_uuid": "3afdbbfc-e45a-430e-abba-842074a8b035"
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


## /v1/storage/data_disk/delete
从容量组移除数据盘
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
http://192.168.201.147:9990/v1/storage/data_disk/delete
```
Body:
```
{
	"usd_uuid": "da46539a-06b9-4595-926d-67d2952f8700",
	"host_name": "192.168.201.188",
	"host_uuid": "07bc76c4-ce06-4383-988d-8dd4ee493012",
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


## /v1/storage/cache_disk/list
缓存盘列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
host_uuid|string|是|-|主机uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.213:8080/v1/storage/cache_disk/list?host_uuid=f6db6e80-642f-4335-8b00-71f84809dfad&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
    "list": [],
    "total_count": 0
  }
}
```

#### 异常返回示例

### 状态码


## /v1/storage/cache_disk/inspect
缓存盘详情
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
host_uuid|string|是|-|主机uuid
attached_cache_usd_path|string|是|-|盘符

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://10.30.10.24:8080/v1/storage/cache_disk/inspect?host_uuid=d13a0be4-22f8-4d2d-82f8-8d43a9076b6a&attached_cache_usd_path=%2Fdev%2Fsdc&cluster_uuid=3afdbbfc-e45a-430e-abba-842074a8b035
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
        "Name": "",
        "UUID": "",
        "HostUUID": "",
        "Type": "",
        "Device": "",
        "Status": 0,
        "Usage": 0,
        "info": {
          "status": {
            "code": 0,
            "message": "",
            "messageCn": "",
            "stack": null,
            "desc": "",
            "UUID": ""
          },
          "device": "/dev/sdc",
          "cacheMode": "writearound",
          "dirtyData": "0.0k",
          "sequentialCutoff": "4.0M",
          "writebackPercent": "0",
          "writebackIdleDurationMsecs": "5000",
          "writebackRunning": "1",
          "readahead": "0.0k",
          "writeBcakUnconditionalTime": "23:00:00-06:00:00",
          "statsFiveMinute": {
            "bypassed": "167.4M",
            "cacheBypassHits": "1192",
            "cacheBypassMisses": "1610",
            "cacheHitRatio": "81",
            "cacheHits": "3078",
            "cacheMissCollisions": "5",
            "cacheMisses": "677",
            "cacheReadaheads": "0"
          },
          "statsHour": {
            "bypassed": "1.0G",
            "cacheBypassHits": "7912",
            "cacheBypassMisses": "10082",
            "cacheHitRatio": "93",
            "cacheHits": "120380",
            "cacheMissCollisions": "26",
            "cacheMisses": "8669",
            "cacheReadaheads": "0"
          },
          "statsDay": {
            "bypassed": "5.1G",
            "cacheBypassHits": "26370",
            "cacheBypassMisses": "46128",
            "cacheHitRatio": "87",
            "cacheHits": "1011114",
            "cacheMissCollisions": "390",
            "cacheMisses": "141638",
            "cacheReadaheads": "0"
          },
          "statsTotal": {
            "bypassed": "26.8G",
            "cacheBypassHits": "141793",
            "cacheBypassMisses": "592331",
            "cacheHitRatio": "77",
            "cacheHits": "2201591",
            "cacheMissCollisions": "1465",
            "cacheMisses": "647505",
            "cacheReadaheads": "0"
          }
        },
        "Ctime": 0,
        "GIndex": 0,
        "Capacity": 0,
        "Port": 0,
        "Vendor": "",
        "HostIP": "",
        "CacheDevice": "",
        "Avail": 0,
        "Mode": 0
      }
    ],
    "total_count": 0
  }
}
```

#### 异常返回示例

### 状态码



## /v1/storage/cache_disk/create/attach/disk
缓存盘创建和绑定磁盘（物理盘和数据盘）
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
http://192.168.201.147:9990/v1/storage/cache_disk/create/attach/disk
```
Body:
```
{
	"host_uuid": "d13a0be4-22f8-4d2d-82f8-8d43a9076b6a",
	"host_name": "10.30.10.21",
	"physical_device": "/dev/sda",
	"usd_devices": [
		{
			"path": "/dev/sdc",
			"type": "HDD"
		}
	],
	"cluster_uuid": "3afdbbfc-e45a-430e-abba-842074a8b035"
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


## /v1/storage/cache_disk/delete
缓存盘卸载
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
http://192.168.201.147:9990/v1/storage/cache_disk/delete
```
Body:
```
{
	"host_uuid": "d13a0be4-22f8-4d2d-82f8-8d43a9076b6a",
	"host_name": "10.30.10.21",
	"cache_device_paths": [
		"/dev/sdf"
	],
	"cluster_uuid": "3afdbbfc-e45a-430e-abba-842074a8b035"
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


## /v1/storage/cache_disk/detach/data_disk
缓存盘卸载数据盘
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
http://192.168.201.147:9990/v1/storage/cache_disk/detach/data_disk
```
Body:
```
{
	"host_uuid": "d13a0be4-22f8-4d2d-82f8-8d43a9076b6a",
	"host_name": "10.30.10.21",
	"usd_paths": [
		{
			"UUID": "6e21fca5-4cb0-4c58-8d14-e66c927be30f",
			"Path": "/dev/sdg"
		}
	],
	"cache_device_path": "/dev/sdf",
	"cluster_uuid": "3afdbbfc-e45a-430e-abba-842074a8b035"
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


## /v1/storage/cache_disk/attach/disk
缓存盘添加数据盘
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
http://192.168.201.147:9990/v1/storage/cache_disk/attach/disk
```
Body:
```
{
	"host_uuid": "d13a0be4-22f8-4d2d-82f8-8d43a9076b6a",
	"host_name": "10.30.10.21",
	"devices": [
		{
			"path": "/dev/sdc",
			"type": "HDD"
		}
	],
	"cache_device_path": "/dev/sdf",
	"cluster_uuid": "3afdbbfc-e45a-430e-abba-842074a8b035"
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


## /v1/storage/unused/data_disk/list
未使用的数据盘列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
host_uuid|string|是|-|主机uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.213:8080/v1/storage/unused/data_disk/list?host_uuid=f6db6e80-642f-4335-8b00-71f84809dfad&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
    "devices": [
      {
        "uuid": "",
        "name": "",
        "path": "/dev/sdd",
        "capacity": 0,
        "type": "HDD",
        "Status": 1
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码

## /v1/storage/unused/disk/list
未使用磁盘列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
host_uuid|string|是|-|主机uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.213:8080/v1/storage/unused/disk/list?host_uuid=f6db6e80-642f-4335-8b00-71f84809dfad&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
    "devices": [
      {
        "uuid": "",
        "name": "",
        "path": "/dev/sdd",
        "capacity": 0,
        "type": "HDD",
        "Status": 1
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码




## /v1/storage/cache_disk/parameter/update
缓存盘设置
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
http://192.168.201.147:9990/v1/storage/cache_disk/parameter/update
```
Body:
```
{
	"host_uuid": "02eeee3b-1d79-474c-8fb0-7b08e8edca09",
	"host_name": "10.30.10.20",
	"attached_cache_usd_path": "/dev/sde",
	"cache_mode": "writeback",
	"sequential_cutoff": "4.0M",
	"write_back_percent": "1",
	"write_back_idle_duration_msecs": "5000",
	"write_back_running": "1",
	"read_ahead": "0.0k",
	"write_back_unconditional_time": "",
	"cluster_uuid": "3afdbbfc-e45a-430e-abba-842074a8b035"
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

