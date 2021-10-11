[back to api overview](../api_overview.md#api)
# router

## /v1/network/add/router
#### 功能：添加路由器
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|"" | 租户uuid
 cluster_uuid|string| 是|"" | 集群uuid
 zone_uuid|string| 是|"" | 子集群uuid
 name|string|是|""  | 路由器名称
 enable_ipv_6|bool|否|false  | 是否启动ipv6
 ipv_6_address_mode|int|否|0 | ipv6模式


### 返回参数
名称|参数类型|描述 
---|---|---
 todo
 
### 示例

#### 请求示例
```
http://localhost:9990/v1/network/add/router
```
Body:
```
{
  "tenant_uuid": "3fb91ca3-5034-47ee-bccf-cabf7fd5a3fe",
  "name": "sw1",
  "enable_ipv_6": false,
  "ipv_6_address_mode": null,
  "zone_uuid": "64864753-88a2-4020-8627-bf055964b4d8",
  "cluster_uuid": "42e3b0db-5dce-4893-9421-7ae6fe8ac0ee"
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
    "router_info": {
      "ns": "fafddfdf",
      "ctime": 1573093989,
      "mtime": 1573093989,
      "uuid": "ef4d9eb8-bfd4-4460-82a4-86e09c418df4",
      "enable": true,
      "ext_ids": {
        "ipv6": "true",
        "ipv6_address_mode": "slaac",
        "name": "fafddfdf"
      },
      "lr_lb": null,
      "name": "fafddfdf",
      "nat": null,
      "options": null,
      "ports": null,
      "static_routes": null,
      "port_mappings": null
    }
  }
}
```

#### 异常返回示例

### 状态码


## /v1/network/router/info
#### 功能：获取交换机信息
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant|string| 是|""  | 租户uuid
 router_uuid|string| 是|""  | 路由器的uuid

### 返回参数
名称|参数类型|描述 
---|---|---
todo 

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/router/info
```
Body:
```
{
	"tenant": "ed350282-de88-4e2a-98fc-da2029a60138",
	"router_uuid": "fafddfdf-de88-4e2a-98fc-da2029a60138"
}
```
#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "create_time": 1548139892,
    "update_time": 1548139902,
    "uuid": "244b22a7-ba01-46cf-ae96-715f5c80f30e",
    "enable": true,
    "extra_info": {
      "name": "aaaa"
    },
    "loadbanlance_info": null,
    "name": "aaa_aaaa",
    "nat": null,
    "options": null,
    "ports": null,
    "static_routes": null,
    "port_mappings": null
  }
}
```

#### 异常返回示例

### 状态码

## /v1/network/router/info/list
#### 功能：获取路由器列表
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant|string| 是|""  | 租户uuid
 page_num|int|否|0  | 第几页
 page_size|int|否|0  | 每一个多少条数据
 filter_name|string|否|""  | 要过滤的路由器的名称


### 返回参数
名称|参数类型|描述 
---|---|---
 todo 

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/router/info/list
```
Body:
```
{
	"tenant": "ed350282-de88-4e2a-98fc-da2029a60138",
	"page_num": 0,
	"page_size": 10,
	"filter_name": "",
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
    "total": 1,
    "router_infos": [
      {
        "ns": "ed350282-de88-4e2a-98fc-da2029a60138",
        "tenant": "ed350282-de88-4e2a-98fc-da2029a60138",
        "tenant_name": "lts",
        "ctime": 1573093989,
        "mtime": 1573093989,
        "uuid": "ef4d9eb8-bfd4-4460-82a4-86e09c418df4",
        "enable": true,
        "exit_ids": {
          "ipv6": "true",
          "ipv6_address_mode": "slaac",
          "name": "fafddfdf"
        },
        "lr_lb": null,
        "name": "fafddfdf",
        "nat": null,
        "options": null,
        "ports": null,
        "static_routes": null,
        "forwards": null
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码



## /v1/network/delete/router
#### 功能：删除路由器
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|-  | 租户uuid
 router_uuid|string| 是|-  | 路由器的uuid

### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 router_uuid|string| 路由器的uuid

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/delete/router
```
Body:
```
{	
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
    "router_uuid": "55b2edab-305c-461a-b49d-2f9847f037e1"
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
    "router_uuid": "55b2edab-305c-461a-b49d-2f9847f037e1"
  }
}
```

#### 异常返回示例
### 状态码


## /v1/network/router/delete/loadbalancer
功能：路由器删除负载均衡
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid
 router_uuid|string|是|""  | 路由器的uuid
 load_balancer_uuid|string|是|""  | 负载均衡的uuid


### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string|租户uuid
 router_uuid|string|路由器的uuid
 load_balancer_uuid|string|负载均衡的uuid

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/router/delete/loadbalancer 
```
Body:
```
{	
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
    "router_uuid": "5c028587-1639-11e9-8b6e-5254fffffffe",
    "load_balancer_uuid": "55b2edab-305c-461a-b49d-2f9847f037e1"
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
    "load_balancer_uuid": "55b2edab-305c-461a-b49d-2f9847f037e1"
  }
}
```

#### 异常返回示例

### 状态码

## /v1/network/router/add/loadbalancer
功能：路由器添加负载均衡
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|-  | 租户uuid
 router_uuid|string| 是|-  | 路由器uuid
 load_balancer_name|string| 是|-  | 负载均衡的名字
 vip|string| 是|-  | 虚拟IP（即物理出口ip）
 vip_port|int64| 是|0  | 虚拟ip对应的端口
 target_ip_port|map[string]string| 是|-  | 要进行负载均衡的虚拟机ip组，包括ip和端口
 protocol|string|是|-  | 传输协议 

### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 router_uuid|string| 路由器uuid
 load_balancer_name|string| 负载均衡的名字
 vip|string| 虚拟IP（即物理出口ip）
 vip_port|int64| 虚拟ip对应的端口
 target_ip_port|map[string]string| 要进行负载均衡的虚拟机ip组，包括ip和端口
 protocol|string| 传输协议 

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/router/add/loadbalancer
```
Body:
```
{	
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "router_uuid": "55b2edab-305c-461a-b49d-2f9847f037e1"
    "load_balancer_name": "testname"
    "vip": "192.168.201.3"
    "vip_port": 8000
    "target_ip_port": {
        "192.168.201.56":8080
    }
    "protocol": "tcp"
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
    " load_balancer_name": "testname"
    "vip": "192.168.201.3"
    "vip_port": 8000
    "target_ip_port": {
        "192.168.201.56":8080
    }
    "protocol": "tcp"
  }
}
```

#### 异常返回示例

### 状态码


## /v1/network/disable/router
功能：关闭路由器
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|-  | 租户uuid
 router_uuid|string| 是|-  | 路由器uuid

### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 router_uuid|string| 路由器uuid

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/disable/router
```
Body:
```
{	
    "tenant_uuid": "5c028587-14aa-11e9-b0b9-5256ff003400"
    "router_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "tenant_uuid": "5c028587-14aa-11e9-b0b9-5256ff003400"
    "router_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
  }
}
```

#### 异常返回示例

### 状态码


## /v1/network/router/service/list
#### 功能：
#### 请求类型：

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/router/service/list
```
Body:
```	
{
	"tenant": "ed350282-de88-4e2a-98fc-da2029a60138",
	"router_uuid": "ef4d9eb8-bfd4-4460-82a4-86e09c418df4",
	"page_num": 0,
	"page_size": 10,
	"service_type": 5,
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
    "total_count": 0,
    "router": {
      "ns": "ed350282-de88-4e2a-98fc-da2029a60138",
      "tenant": "ed350282-de88-4e2a-98fc-da2029a60138",
      "tenant_name": "lts",
      "ctime": 1573093989,
      "mtime": 1573093989,
      "uuid": "ef4d9eb8-bfd4-4460-82a4-86e09c418df4",
      "enable": true,
      "ext_ids": {
        "ipv6": "true",
        "ipv6_address_mode": "slaac",
        "name": "fafddfdf"
      },
      "lr_lb": null,
      "name": "fafddfdf",
      "nat": null,
      "options": null,
      "ports": null,
      "static_routes": null,
      "forwards": null
    },
    "for_wards": null,
    "nats": null,
    "fips": null,
    "load_balancers": null,
    "static_routes": null
  }
}
```

#### 异常返回示例

### 状态码


## /v1/network/router/add/forward
功能：路由器添加端口映射
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|-  | 租户uuid
 router_uuid|string| 是|-  | 路由器uuid
 port_mapping|[PortMapping_object](./port_mapping.md#PortMapping_object)| 是|-  | 端口映射
 
 #### PortMapping_object
名称|参数类型|描述 
--- |---|---|--- |---
port_mapping_name|string| 是|-  | 端口映射名称
physical_export_ip|string| 是|-  | 物理出口ip
port|string| 是|-  | 与出口ip对应的端口
vm_ip|string| 是|-  | 虚拟机ip
vm_port|string| 是|-  | 虚拟机端口
protocol|string| 是|""  | 网络传输协议

### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 router_uuid|string| 路由器uuid
 port_mapping|[PortMapping_object](./port_mapping.md#PortMapping_object)| 端口映射
 



### 示例

#### 请求示例
```
http://localhost:9990/v1/network/router/add/forward
```
Body:
```
{	
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "router_uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400"
    "port_mapping": {
        "name":"port_mapping_name",
        "physical_export_ip":"192.168.201.25",
        "port":2550,
        "vm_ip":"192.168.201.168",
        "vm_port":8080,
        "protocol":"tcp"
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
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "router_uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400"
    "port_mapping": {
        "name":"port_mapping_name",
        "physical_export_ip":"192.168.201.25",
        "port":2550,
        "vm_ip":"192.168.201.168",
        "vm_port":8080,
        "protocol":"tcp"
    }
  }
}
```

#### 异常返回示例

### 状态码



## /v1/network/router/del/forward
功能：路由器删除端口映射
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|-  | 租户uuid
 router_uuid|string| 是|-  | 路由器uuid
 port_mapping_uuid|string| 是|-  | 端口映射uuid
 

### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 router_uuid|string| 路由器uuid
 port_mapping_uuid|string| 端口映射uuid
 

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/router/del/forward
```
Body:
```
{	
    "tenant_uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400"
    "router_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "port_mapping_uuid": "5c028587-14aa-11e9-b0b9-5256ff003400"
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "tenant_uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400"
    "router_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "port_mapping_uuid": "5c028587-14aa-11e9-b0b9-5256ff003400"
  }
}
```

#### 异常返回示例
### 状态码



## /v1/network/router/port_mapping/inspect
功能：获取路由器端口映射详情
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid
 router_uuid|string| 是|""  | 租户uuid
 port_mapping_uuid|string| 是|""  | 租户uuid

### 返回参数
名称|参数类型|描述 
---|---|---
create_time|int64|创建时间
update_time|int64|修改时间
port_mapping_uuid|string|uuid
port_mapping_name|string|uuid
vip|string|虚拟ip(物理出口ip)
port|int|与出口ip对应的端口
vm_ip|string|虚拟机ip
vm_port|int|虚拟机端口
protocol|string|传输协议
extra_info|map[string]string|额外信息

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/router/port_mapping/inspect?tenant_uuid=5c028587-1639-11e9-8b6e-5254fffffffe&router_uuid=55b2edab-305c-461a-b49d-2f9847f037e1&port_mapping_uuid=1c64fac3-1324-11e9-b910-5254fffffffd
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "create_time": 1548139892,
    "update_time": 1548139902,
    "port_mapping_uuid": "1c64fac3-1324-11e9-b910-5254fffffffd",
    "port_mapping_name": "testname",
    "vip": "192.168.201.2",
    "port": 8000,
    "vm_ip": "192.168.201.5",
    "vm_port": 8001,
    "protocol": "tcp",
    "extra_info": nil,
  }
}
```

#### 异常返回示例

### 状态码



## /v1/network/router/router/del/eip
#### 功能：路由器删除弹性ip
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid
 router_uuid|string|是|""  |  路由器uuid
 fip_uuid|string|是|""  | fip的uuid


### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 router_uuid|string| 路由器uuid
 fip_uuid|string| fip的uuid

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/router/del/eip
```
Body:
```
{	
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "router_uuid": "1c64fac3-14aa-11e9-b0b9-5256ff003400"
    "fip_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
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
    "router_uuid": "1c64fac3-14aa-11e9-b0b9-5256ff003400"
    "fip_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
  }
}
```

#### 异常返回示例

### 状态码


## /v1/network/router/add/eip
#### 功能：路由器添加弹性ip
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid
 router_uuid|string|是|""  | 路由器uuid
 out_ip|string|是|""  | 物理出口ip
 inside_subnet|string|是|""  | 子网网段内某个ip地址
 

### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 router_uuid|string| 路由器uuid
 out_ip|string| 物理出口ip
 inside_subnet|string| 子网网段内某个ip地址


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/router/add/eip
```
Body:
```
{	
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "router_uuid": "1c64fac3-14aa-11e9-b0b9-5256ff003400"
    "out_ip": "192.168.201.198"
    "inside_subnet": "192.168.1.2"
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
    "router_uuid": "1c64fac3-14aa-11e9-b0b9-5256ff003400"
    "out_ip": "192.168.201.198"
    "inside_subnet": "192.168.1.2"
  }
}
```

#### 异常返回示例

### 状态码


## /v1/network/router/nat/create
功能：路由器添加nat
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|-  | 租户uuid
 router_uuid|string| 是|-  | 路由器uuid
 out_ip|string|是|-  | 物理出口ip
 inside_subnet|string|是|-  | 逻辑子网网段


### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string|  租户uuid
 router_uuid|string|  路由器uuid
 out_ip|string | 物理出口ip
 inside_subnet|string |逻辑子网网段

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/router/nat/create
```
Body:
```
{	
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "router_uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400"
    "out_ip": "192.168.201.168"
    "inside_subnet": "192.168.1.104/24"
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
    "router_uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400"
    "out_ip": "192.168.201.168"
    "inside_subnet": "192.168.1.104/24"
  }
}
```

#### 异常返回示例

### 状态码




## /v1/network/router/nat/delete
功能：路由器删除nat
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|-  | 租户uuid
 router_uuid|string| 是|-  | 路由器的uuid
 nat_uuid|string|是|-  | nat的uuid


### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 router_uuid|string| 路由器的uuid
 nat_uuid|string| snat的uuid

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/router/nat/delete
```
Body:
```
{	
    "tenant_uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400",
    "router_uuid": "5c028587-14aa-11e9-b0b9-5256ff003400",
    "nat_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "tenant_uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400",
    "router_uuid": "5c028587-14aa-11e9-b0b9-5256ff003400",
    "nat_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
  }
}
```

#### 异常返回示例

### 状态码


## /v1/network/router/nat/update
#### 功能：路由器nat修改
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant|string| 是|-  | 租户uuid
 router_uuid|string| 是|-  | 路由器的uuid
 nat_uuid|string|是 |- | nat的uuid
 inside_subnet|是 |- | 修改后的目的逻辑子网网段

### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/router/nat/update
```
Body:
```	
{
	"cluster_uuid": "49bb08f9-1c60-49ee-85d6-6fde276895c5",
	"tenant": "92126fa9-7d35-4d7a-ad32-3cfce63b8305",
	"router_uuid": "fe73de52-7c2d-42d6-992a-da25344b1a54",
	"router_name": "route",
	"nat_uuid": "c25a6801-f987-465a-a472-9a8153b744de",
	"inside_subnet": "192.168.12.0/24"
}
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码


## /v1/network/router/static_route/create
#### 功能： 路由器静态路由添加
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant|string| 是|-  | 租户uuid
 router_uuid|string| 是|-  | 路由器的uuid
 nat_uuid|string|是 |- | nat的uuid
 ip_prefix| string|是 |- | 目的网络
 next_hop| string|是 |- | 下一跳地址
 policy| string|是 |dst-dst | 下一跳地址

### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/router/static_route/create
```
Body:
```	
{
	"cluster_uuid": "49bb08f9-1c60-49ee-85d6-6fde276895c5",
	"tenant": "92126fa9-7d35-4d7a-ad32-3cfce63b8305",
	"router_uuid": "fe73de52-7c2d-42d6-992a-da25344b1a54",
	"router_name": "route",
	"ip_prefix": "10.30.10.0/24",
	"next_hop": "10.30.192.1",
	"policy": "dst-dst"
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


## /v1/network/router/static_route/delete
#### 功能：租户路由器静态路由删除
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant|string| 是|-  | 租户uuid
 router_uuid|string| 是|-  | 路由器的uuid
 nat_uuid|string|是 |- | nat的uuid
 route_uuid| string|是 |- | 静态路由uuid

### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/router/static_route/delete
```
Body:
{
	"cluster_uuid": "49bb08f9-1c60-49ee-85d6-6fde276895c5",
	"tenant": "92126fa9-7d35-4d7a-ad32-3cfce63b8305",
	"router_uuid": "fe73de52-7c2d-42d6-992a-da25344b1a54",
	"router_name": "route",
	"route_uuid": "c25a6801-f987-465a-a472-9a8153b744de"
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

## /v1/network/router/static_route/update
#### 功能：租户路由器静态路由更新
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
  tenant|string| 是|-  | 租户uuid
  router_uuid|string| 是|-  | 路由器的uuid
  nat_uuid|string|是 |- | nat的uuid
  ip_prefix| string|是 |- | 目的网络
  next_hop| string|是 |- | 下一跳地址
  policy| string|是 |dst-dst | 下一跳地址


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/router/static_route/update
```
Body:
```	
```
{
	"cluster_uuid": "49bb08f9-1c60-49ee-85d6-6fde276895c5",
	"tenant": "92126fa9-7d35-4d7a-ad32-3cfce63b8305",
	"router_uuid": "fe73de52-7c2d-42d6-992a-da25344b1a54",
	"router_name": "route",
	"ip_prefix": "10.30.10.0/24",
	"next_hop": "10.30.192.1",
	"policy": "dst-dst"
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


## /v1/network/vm/delete
#### 功能：网络虚拟机删除
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 addr| string |是 | -| 网络虚拟机ip
 enable| bool |是 | -| 网络虚拟机是否开启


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/vm/delete
```
Body:
```	
{
    "cluster_uuid": "",
    "addr": "10.30.10.10/24",
    "enable": "true"
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





## /v1/network/port_mirror/create
#### 功能：添加端口映射
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/port_mirror/create
```
Body:
```	
todo
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码


## /v1/network/port_mirror/delete
#### 功能:端口映射删除
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/port_mirror/delete
```
Body:
```	
todo
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码


## /v1/network/port_mirror/inspect
#### 功能：获取端口映射
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/port_mirror/inspect
```
Body:
```	
todo
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码


## /v1/network/port_mirror/list
#### 功能：获取端口映射列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/port_mirror/list?page_num=0&page_size=10&zone_uuid=8dbde5bf-d9e2-472c-8c47-f58deeca3a6c&cluster_uuid=49bb08f9-1c60-49ee-85d6-6fde276895c5
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
    "total_count": 0,
    "list": [],
    "each_range_list_state": [
      {
        "cluster_uuid": "49bb08f9-1c60-49ee-85d6-6fde276895c5",
        "cluster_name": "cluster_10_30_100_24",
        "cluster_mode": "",
        "result": {
          "scode": 0,
          "desc": "",
          "message": "success",
          "message_cn": "成功",
          "stack": null,
          "data": ""
        },
        "total_count": 0
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/network/bridge_port/list
#### 功能：获取网桥端口列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/bridge_port/list?host_ip=10.30.100.21&bridge_name=mirror&cluster_uuid=49bb08f9-1c60-49ee-85d6-6fde276895c5
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
    "total_count": 0,
    "list": [],
    "each_range_list_state": [
      {
        "cluster_uuid": "49bb08f9-1c60-49ee-85d6-6fde276895c5",
        "cluster_name": "cluster_10_30_100_24",
        "cluster_mode": "",
        "result": {
          "scode": 0,
          "desc": "",
          "message": "success",
          "message_cn": "成功",
          "stack": null,
          "data": ""
        },
        "total_count": 0
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码

## /v1/network/router/loadbalancer/update
#### 功能：路由器负载均衡器修改
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/router/loadbalancer/update
```
Body:
```	
todo
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码



## /v1/network/router/port_mapping/update
#### 功能：路由器端口映射修改
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/router/port_mapping/update
```
Body:
```	
todo
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码

## /v1/network/enable/router
#### 功能：启动路由器
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|-  | 租户uuid
 router_uuid|string| 是|-  | 路由器uuid

### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 router_uuid|string| 路由器uuid

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/enable/router
```
Body:
```
{	
    "tenant_uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400"
    "router_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "tenant_uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400"
    "router_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
  }
}
```

#### 异常返回示例

### 状态码












