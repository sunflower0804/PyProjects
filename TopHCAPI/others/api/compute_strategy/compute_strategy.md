[back to api overview](../api_overview.md#label_api)
### 虚拟机策略相关接口
## /v1/strategy/add
虚拟机策略添加(开关机策略,cdp策略,备份策略)
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
http://192.168.201.211:8080/v1/strategy/add
```
Body:
```
{
	"name": "开机策略",
	"desc": "描述",
	"type": 1,
	"enabled": true,
	"params": {
		"vm_power": {
			"next_start_time": 1584633600,
			"next_shutoff_time": 0
		}
	},
	"period": "daily",
	"expire_time": 1584633600,
	"objects": [],
	"cluster_uuid": "e12b4f57-e3f0-4f93-83da-76ce1eda8595"
}
```

#### 正常返回示例
```
{
  "message": "",
  "message_cn": "",
  "scode": 0,
  "desc": "",
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
    "total": 0,
    "infos": [
      {
        "uuid": "b87f776e-9349-4cf9-8b82-1445e4efbb8b",
        "name": "开机策略",
        "desc": "描述",
        "type": 1,
        "params": {
          "vm_power": {
            "next_start_time": 1584633600,
            "next_shutoff_time": 0
          }
        },
        "enabled": true,
        "enabled_string": "启用",
        "period": "daily",
        "expire_time": 1584633600
      }
    ],
    "objects": []
  }
}
```

#### 异常返回示例

### 状态码


## /v1/strategy/delete
虚拟机策略删除(开关机策略,cdp策略,备份策略)
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
http://192.168.201.211:8080/v1/strategy/delete
```
Body:
```
{
	"uuid": "b87f776e-9349-4cf9-8b82-1445e4efbb8b",
	"cluster_uuid": "e12b4f57-e3f0-4f93-83da-76ce1eda8595"
}
```

#### 正常返回示例
```
{
  "message": "",
  "message_cn": "",
  "scode": 0,
  "desc": "",
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
    "total": 0,
    "infos": [
      {
        "uuid": "b87f776e-9349-4cf9-8b82-1445e4efbb8b",
        "name": "开机策略",
        "desc": "描述",
        "type": 1,
        "params": {
          "vm_power": {
            "next_start_time": 0,
            "next_shutoff_time": 0
          }
        },
        "enabled": true,
        "enabled_string": "启用",
        "period": "daily",
        "expire_time": 1584633600
      }
    ],
    "objects": []
  }
}
```

#### 异常返回示例

### 状态码


## /v1/strategy/get
虚拟机策略查看(开关机策略,cdp策略,备份策略)
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
http://192.168.201.211:8080/v1/strategy/get
```
Body:
```
{
	"uuid": "8bc53cf8-e0df-4088-be35-e54f54818fa4",
	"paging": {
		"page_size": 10,
		"page_number": 0
	},
	"filter": {
		"fuzzy": null,
		"name": null
	},
	"cluster_uuid": "e12b4f57-e3f0-4f93-83da-76ce1eda8595"
}
```

#### 正常返回示例
```
{
  "message": "",
  "message_cn": "",
  "scode": 0,
  "desc": "",
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
    "total": 2,
    "infos": [
      {
        "uuid": "8bc53cf8-e0df-4088-be35-e54f54818fa4",
        "name": "dfdf",
        "desc": "dfsdf",
        "type": 1,
        "params": {
          "vm_power": {
            "next_start_time": 1584611520,
            "next_shutoff_time": 0
          }
        },
        "enabled": false,
        "enabled_string": "停用",
        "period": "daily",
        "expire_time": 1584524825
      }
    ],
    "objects": [
      {
        "uuid": "2e670a09-7969-462d-93f2-f8e5f1ab6e84",
        "strategy": "8bc53cf8-e0df-4088-be35-e54f54818fa4",
        "strategy_name": "dfdf",
        "cluster_type": 1,
        "cluster_uuid": "e12b4f57-e3f0-4f93-83da-76ce1eda8595",
        "cluster_name": "cluster_10_30_12_89",
        "object_type": 1,
        "object_id": "f2e64500-fa40-4e5e-8de4-1dcfa3a40640",
        "object_name": "vm_1",
        "exec_results": null
      },
      {
        "uuid": "796bc7b6-0abf-4085-82ab-1434f20e8884",
        "strategy": "8bc53cf8-e0df-4088-be35-e54f54818fa4",
        "strategy_name": "dfdf",
        "cluster_type": 1,
        "cluster_uuid": "e12b4f57-e3f0-4f93-83da-76ce1eda8595",
        "cluster_name": "cluster_10_30_12_89",
        "object_type": 1,
        "object_id": "f68cd9a2-e820-473b-b81c-603d66cb5763",
        "object_name": "vm_2",
        "exec_results": null
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码



## /v1/strategy/list
虚拟机策略列表(开关机策略,cdp策略,备份策略)
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
http://192.168.201.211:8080/v1/strategy/list
```
Body:
```
{
	"paging": {
		"page_size": 10,
		"page_number": 0
	},
	"filter": {
		"fuzzy": null,
		"name": null,
		"type": 1
	},
	"cluster_uuid": "98323d75-61ce-47f9-8b4d-d83b27ad0469"
}
```

#### 正常返回示例
```
{
  "message": "",
  "message_cn": "",
  "scode": 0,
  "desc": "",
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
    "total": 2,
    "infos": [
      {
        "uuid": "baec0dd9-1def-4b79-9290-604d6d424211",
        "name": "gggggg",
        "desc": "...",
        "type": 1,
        "params": {
          "vm_power": {
            "next_start_time": 1584547200,
            "next_shutoff_time": 0
          }
        },
        "enabled": false,
        "enabled_string": "停用",
        "period": "daily",
        "expire_time": 1583942400
      },
      {
        "uuid": "f0763ec1-19b4-4592-a302-06e29d4b29ba",
        "name": "test1",
        "desc": "",
        "type": 1,
        "params": {
          "vm_power": {
            "next_start_time": 1584587400,
            "next_shutoff_time": 0
          }
        },
        "enabled": false,
        "enabled_string": "停用",
        "period": "daily",
        "expire_time": 1584374400
      }
    ],
    "objects": null
  }
}
```

#### 异常返回示例

### 状态码


## /v1/strategy/edit
虚拟机策略编辑(开关机策略,cdp策略,备份策略)
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
http://192.168.201.211:8080/v1/strategy/edit
```
Body:
```
{
	"uuid": "8bc53cf8-e0df-4088-be35-e54f54818fa4",
	"name": "dfdf",
	"desc": "dfsdf",
	"type": 1,
	"enabled": true,
	"params": {
		"vm_power": {
			"next_start_time": 0,
			"next_shutoff_time": 1584633600
		}
	},
	"period": "daily",
	"expire_time": 1584524825,
	"objects": [
		{
			"cluster_type": 1,
			"cluster_uuid": "e12b4f57-e3f0-4f93-83da-76ce1eda8595",
			"object_type": 1,
			"object_id": "f68cd9a2-e820-473b-b81c-603d66cb5763"
		},
		{
			"cluster_type": 1,
			"cluster_uuid": "e12b4f57-e3f0-4f93-83da-76ce1eda8595",
			"object_type": 1,
			"object_id": "f2e64500-fa40-4e5e-8de4-1dcfa3a40640"
		}
	],
	"cluster_uuid": "e12b4f57-e3f0-4f93-83da-76ce1eda8595"
}
```

#### 正常返回示例
```
{
  "message": "",
  "message_cn": "",
  "scode": 0,
  "desc": "",
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
    "total": 0,
    "infos": [
      {
        "uuid": "8bc53cf8-e0df-4088-be35-e54f54818fa4",
        "name": "dfdf",
        "desc": "dfsdf",
        "type": 1,
        "params": {
          "vm_power": {
            "next_start_time": 0,
            "next_shutoff_time": 1584633600
          }
        },
        "enabled": true,
        "enabled_string": "启用",
        "period": "daily",
        "expire_time": 1584524825
      }
    ],
    "objects": null
  }
}
```

#### 异常返回示例

### 状态码



## /v1/strategy/enable
虚拟机策略启动和停止(开关机策略,cdp策略,备份策略)
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
uuid|string|是|-|策略uuid
enabled|bool|否|false|是否开启

### 返回参数

名称|参数类型|描述
---|---|---
TODO
### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/strategy/enable
```
Body:
```
{
	"uuid": "8bc53cf8-e0df-4088-be35-e54f54818fa4",
	"enabled": true,
	"cluster_uuid": "e12b4f57-e3f0-4f93-83da-76ce1eda8595"
}
```

#### 正常返回示例
```
{
  "message": "",
  "message_cn": "",
  "scode": 0,
  "desc": "",
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
    "total": 0,
    "infos": [
      {
        "uuid": "8bc53cf8-e0df-4088-be35-e54f54818fa4",
        "name": "dfdf",
        "desc": "dfsdf",
        "type": 1,
        "params": {
          "vm_power": {
            "next_start_time": 0,
            "next_shutoff_time": 1584633600
          }
        },
        "enabled": true,
        "enabled_string": "启用",
        "period": "daily",
        "expire_time": 1584524825
      }
    ],
    "objects": null
  }
}
```

#### 异常返回示例

### 状态码
