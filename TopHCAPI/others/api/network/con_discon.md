## /v1/network/connect/router_and_switch
#### 功能：连接路由器和交换机
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|-  | 租户uuid
 router_uuid|string| 是|-  | 路由器uuid
 switch_uuid|string| 是|-  | 交换机uuid

### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 router_uuid|string| 路由器uuid
 switch_uuid|string| 交换机uuid

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/connect/router_and_switch
```
Body:
```
{	
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "router_uuid": "55b2edab-305c-461a-b49d-2f9847f037e1"
    "switch_uuid": "1c64fac3-1324-11e9-b910-5254fffffffd"
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "router_uuid": "55b2edab-305c-461a-b49d-2f9847f037e1"
    "switch_uuid": "1c64fac3-1324-11e9-b910-5254fffffffd"
  }
}
```

#### 异常返回示例

### 状态码




## /v1/network/disconnect/switch_from_router 
功能：断开路由器和交换机
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|-  | 租户uuid
 router_uuid|string| 是|-  | 路由器uuid
 switch_uuid|string| 是|-  | 交换机uuid

### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 router_uuid|string| 路由器uuid
 switch_uuid|string| 交换机uuid
 
### 示例

#### 请求示例
```
http://localhost:9990/v1/network/disconnect/switch_from_router 
```
Body:
```
{	
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "router_uuid": "5c028587-1639-11e9-8b6e-5254fffffffe"
    "switch_uuid": "55b2edab-305c-461a-b49d-2f9847f037e1"
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "router_uuid": "5c028587-1639-11e9-8b6e-5254fffffffe"
    "switch_uuid": "55b2edab-305c-461a-b49d-2f9847f037e1"
  }
}
```

#### 异常返回示例

### 状态码



## /v1/network/connect/router_to_gateway
#### 功能：连接网关和路由器
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|-  | 租户uuid
 router_uuid|string| 是|-  | 路由器uuid
 gateway_uuid|string| 是|-  | 网关uuid


### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 router_uuid|string| 路由器uuid
 gateway_uuid|string| 网关uuid

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/connect/router_to_gateway
```
Body:
```
{	
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
    "router_uuid": "5c028587-1639-11e9-8b6e-5254fffffffe",
    "gateway_uuid": "55b2edab-305c-461a-b49d-2f9847f037e1"
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
    "router_uuid": "5c028587-1639-11e9-8b6e-5254fffffffe",
    "gateway_uuid": "55b2edab-305c-461a-b49d-2f9847f037e1"
  }
}
```

#### 异常返回示例

### 状态码



## /v1/network/disconnect/router_from_gateway
#### 功能：断开网关和路由器
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|-  | 租户uuid
 router_uuid|string| 是|-  | 路由器uuid
 gateway_uuid|string| 是|-  | 网关uuid
    

### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 router_uuid|string| 路由器uuid
 gateway_uuid|string| 网关uuid

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/disconnect/router_from_gateway
```
Body:
```
{	
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
    "gateway_uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400",
    "router_uuid": "5c028587-14aa-11e9-b0b9-5256ff003400"
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
    "gateway_uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400",
    "router_uuid": "5c028587-14aa-11e9-b0b9-5256ff003400"
  }
}
```

#### 异常返回示例
### 状态码


## /v1/network/attach/network/node/to/controller
#### 功能：连接网络节点和控制器
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 cluster_uuid|string| 是|""  | 集群uuid
 controller_ip|string| 是|""  | 控制器ip
 host_ips|[]string| 是|""  | 主机ip


### 返回参数
名称|参数类型|描述 
---|---|---
 cluster_uuid|string| 集群uuid
 controller_ip|string| 控制器ip
 host_ips|[]string| 主机ip

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/attach/network/node/to/controller
```
Body:
```
{	
    "cluster_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "controller_ip": "192.168.201.6"
    "host_ips": [
        "192.168.201.1",
        "192.168.201.2",
        "192.168.201.3"
    ]
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "cluster_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "controller_ip": "192.168.201.6"
    "host_ips": [
        "192.168.201.1",
        "192.168.201.2",
        "192.168.201.3"
    ]
  }
}
```

#### 异常返回示例
### 状态码


## /v1/network/detack/network/node/to/controller
#### 功能：断开网络节点和控制器
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 cluster_uuid|string| 是|""  | 集群uuid
 controller_ip|string| 是|""  | 控制器ip
 host_ips|[]string| 是|""  | 主机ip


### 返回参数
名称|参数类型|描述 
---|---|---
 cluster_uuid|string| 集群uuid
 controller_ip|string| 控制器ip
 host_ips|[]string| 主机ip

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/detack/network/node/to/controller
```
Body:
```
{	
    "cluster_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "controller_ip": "192.168.201.6"
    "host_ips": [
        "192.168.201.1",
        "192.168.201.2",
        "192.168.201.3"
    ]
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "cluster_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "controller_ip": "192.168.201.6"
    "host_ips": [
        "192.168.201.1",
        "192.168.201.2",
        "192.168.201.3"
    ]
  }
}
```
#### 异常返回示例
### 状态码


## /v1/network/connect/switch_and_vm
功能：连接交换机和虚拟机
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid
 switch_uuid|string| 是|""  | 交换机uuid
 mac|string| 是|""  | 虚拟机mac地址

### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 switch_uuid|string| 交换机uuid
 mac|string| 虚拟机mac地址
 
 
### 示例

#### 请求示例
```
http://localhost:9990/v1/network/connect/switch_and_vm
```
Body:
```
{	
    "tenant_uuid": "5c028587-1639-11e9-8b6e-5254fffffffe",
    "switch_uuid": "55b2edab-305c-461a-b49d-2f9847f037e1",
    "mac": " fe80::291c:95cd:52e4:7a07%23"
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "tenant_uuid": "5c028587-1639-11e9-8b6e-5254fffffffe",
    "switch_uuid": "55b2edab-305c-461a-b49d-2f9847f037e1",
    "mac": " fe80::291c:95cd:52e4:7a07%23"
  }
}
```

#### 异常返回示例
### 状态码


## /v1/network/disconnect/vm_from_switch
功能：断开交换机和虚拟机连接
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid
 switch_uuid|string| 是|""  | 交换机uuid
 mac|string| 是|""  | 虚拟机的mac地址

### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 switch_uuid|string| 交换机uuid
 mac|string| 虚拟机的mac地址

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/disconnect/vm_from_switch
```
Body:
```
{	
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "switch_uuid": "5c028587-1639-11e9-8b6e-5254fffffffe"
    "mac": "fe80::291c:95cd:52e4:7a07%23"
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "switch_uuid": "5c028587-1639-11e9-8b6e-5254fffffffe"
    "mac": "fe80::291c:95cd:52e4:7a07%23"
  }
}
```

#### 异常返回示例
### 状态码


