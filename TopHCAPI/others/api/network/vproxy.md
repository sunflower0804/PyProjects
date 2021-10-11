## /v1/network/load/balancer/create
#### 功能：添加负载均衡器
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-  | 集群uuid
 tenant|string| 是|-  | 租户uuid
 load_balancer|object| 是|- | 负载均衡器参数

### load_balancer对象
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
 name| string| 是| - | 负载均衡器名称
 frontend_ip| string| 是| - | 负载均衡器ip
 zone_uuid| string| 否| - | 资源池uuid
 relate_vm| string| 是| - | 绑定虚拟机的uuid

### 返回参数
名称|参数类型|描述
---|---|---
//todo

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/load/balancer/create
```
Body:
```
{
    "cluster_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"，
    "tenant": "4a7e240b-14aa-11e9-b0b9-5256ff003400"，
    "load_balancer": {
        "frontend_ip": "10.30.10.10",
        "relate_vm": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
        "name": "name",
    }
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
  }
}
```
#### 异常返回示例
### 状态码



## /v1/network/load/balancer/delete
#### 功能：删除负载均衡器
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-  | 集群uuid
 tenant|string| 是|-  | 租户uuid
 load_balancer|object| 是|- | 负载均衡器参数

### load_balancer对象
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
 uuid| string| 是| - | 负载均衡器uuid


### 返回参数
名称|参数类型|描述
---|---|---
//todo

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/load/balancer/delete
```
Body:
```
{
    "cluster_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"，
    "tenant": "4a7e240b-14aa-11e9-b0b9-5256ff003400"，
    "load_balancer": {
        "uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
    }
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
  }
}
```
#### 异常返回示例
### 状态码


## /v1/network/load/balancer/list
#### 功能：负载均衡器列表
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-  | 集群uuid
 tenant|string| 否|-  | 过滤租户uuid
 filter_name| string| 否|- | 过滤负载均衡器名称
 page_num | int32| 否|- | 显示页码
 page_size| int32| 否|- | 每页多少数据

### 返回参数
名称|参数类型|描述
---|---|---
//todo

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/load/balancer/list?cluster_uuid=4a7e240b-14aa-11e9-b0b9-5256ff003400&tenant=4a7e240b-14aa-11e9-b0b9-5256ff003400&filter_name=111
```

#### 正常返回示例
```
//todo
```
#### 异常返回示例
### 状态码


## /v1/network/load/balancer/get
#### 功能：负载均衡器详情
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-  | 集群uuid
 uuid |string | 是|- | 负载均衡器uuid

### 返回参数
名称|参数类型|描述
---|---|---
//todo

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/load/balancer/get?cluster_uuid=4a7e240b-14aa-11e9-b0b9-5256ff003400&uuid=4a7e240b-14aa-11e9-b0b9-5256ff003400
```

#### 正常返回示例
```
//todo
```
#### 异常返回示例
### 状态码



## /v1/network/listener/create
#### 功能：添加监听器
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-  | 集群uuid
 tenant|string| 是|-  | 租户uuid
 listener|object| 是|- | 监听器参数

### listener
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
 name| string| 是| - | 监听器名称
 frontend_port| uint32| 是| - | 监听端口
 backend_port| uint32| 是| - | 后端服务器端口
 relate_lb| string| 是| - | 绑定负载均衡器的uuid

### 返回参数
名称|参数类型|描述
---|---|---
//todo

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/listener/create
```
Body:
```
{
    "cluster_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"，
    "tenant": "4a7e240b-14aa-11e9-b0b9-5256ff003400"，
    "listener": {
        "frontend_port": 80,
        "backend_port": 8080,
        "name": "listener",
        "relate_lb": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
    }
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
  }
}
```
#### 异常返回示例
### 状态码


## /v1/network/listener/delete
#### 功能：删除添监听器
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-  | 集群uuid
 tenant|string| 是|-  | 租户uuid
 listener|object| 是|- | 监听器参数

### listener
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
 uuid| string| 是| - | 监听器uuid


### 返回参数
名称|参数类型|描述
---|---|---
//todo

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/listener/delete
```
Body:
```
{
    "cluster_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"，
    "tenant": "4a7e240b-14aa-11e9-b0b9-5256ff003400"，
    "listener": {
        "uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
    }
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
  }
}
```
#### 异常返回示例
### 状态码


## /v1/network/listener/list
#### 功能：监听器列表
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-  | 集群uuid
 tenant|string | 否|-  | 过滤租户uuid
 balancer_uuid |string | 否|- | 负载均衡器uuid
 filter_name |string | 否|- | 过滤监听器name
 page_num | int32| 否|- | 显示页码
 page_size| int32| 否|- | 每页多少数据

### 返回参数
名称|参数类型|描述
---|---|---
//todo

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/listener/list?cluster_uuid=4a7e240b-14aa-11e9-b0b9-5256ff003400&balancer_uuid=4a7e240b-14aa-11e9-b0b9-5256ff003400&filter_name=111&tenant=
```

#### 正常返回示例
```
//todo
```
#### 异常返回示例
### 状态码


## /v1/network/listener/get
#### 功能：监听器列表
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-  | 集群uuid
 uuid|string | 是|-  | 监听器uuid


### 返回参数
名称|参数类型|描述
---|---|---
//todo

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/load/listener/get?cluster_uuid=4a7e240b-14aa-11e9-b0b9-5256ff003400&uuid=4a7e240b-14aa-11e9-b0b9-5256ff003400
```

#### 正常返回示例
```
//todo
```
#### 异常返回示例
### 状态码


## /v1/network/backend/server/create
#### 功能：添加后端服务器
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-  | 集群uuid
 tenant|string| 是|-  | 租户uuid
 backend_server|object| 是|- | 后端服务器参数

### backend_server对象
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
 name| string| 是| - | 后端服务器名称
 relate_vm| uint32| 是| - | 绑定虚拟机uuid
 relate_listener| string| 是| - | 绑定监听器的uuid
 backend_ip| string| 是| - | 后端服务器Ip

### 返回参数
名称|参数类型|描述
---|---|---
//todo

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/backend/server/create
```
Body:
```
{
    "cluster_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"，
    "tenant": "4a7e240b-14aa-11e9-b0b9-5256ff003400"，
    "backend_server对象": {
        "relate_listener": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
        "backend_ip": "10.30.11.25",
        "relate_vm": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
        "name": "server",
    }
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
  }
}
```
#### 异常返回示例
### 状态码



## /v1/network/backend/server/delete
#### 功能：删除后端服务器
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-  | 集群uuid
 tenant|string| 否|-  | 租户uuid
 backend_server|object| 是|- | 后端服务器参数

### backend_server对象
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
 uuid| string| 是| - | 后端服务器uuid

### 返回参数
名称|参数类型|描述
---|---|---
//todo

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/backend/server/delete
```
Body:
```
{
    "cluster_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"，
    "tenant": "4a7e240b-14aa-11e9-b0b9-5256ff003400"，
    "backend_server对象": {
        "uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
    }
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
  }
}
```
#### 异常返回示例
### 状态码



## /v1/network/backend/server/list
#### 功能：后端服务器列表
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-  | 集群uuid
 tenant|string| 否|-  | 租户uuid
 listener_uuid| string| 否|- |过滤监听器uuid

### 返回参数
名称|参数类型|描述
---|---|---
//todo

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/backend/server/list?cluster_uuid=4a7e240b-14aa-11e9-b0b9-5256ff003400&listener_uuid=4a7e240b-14aa-11e9-b0b9-5256ff003400
```

#### 正常返回示例
```
//todo
```
#### 异常返回示例
### 状态码


## /v1/network/backend/server/get
#### 功能：后端服务器列表
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-  | 集群uuid
 tenant|string| 否|-  | 租户uuid
 uuid| string| 是|- | 后端服务器uuid

### 返回参数
名称|参数类型|描述
---|---|---
//todo

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/backend/server/get?cluster_uuid=4a7e240b-14aa-11e9-b0b9-5256ff003400&uuid=4a7e240b-14aa-11e9-b0b9-5256ff003400
```

#### 正常返回示例
```
//todo
```
#### 异常返回示例
### 状态码