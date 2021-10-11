[back to api overview](../api_overview.md#api)


## /v1/network/add/switch
#### 功能： 添加交换机
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
http://localhost:9990/v1/network/add/switch
```
Body:
```	
{
	"tenant": "ed350282-de88-4e2a-98fc-da2029a60138",
	"name": "aaaa",
	"zone_uuid": "64864753-88a2-4020-8627-bf055964b4d8",
	"ip_type": 0,
	"subnet": "10.10.10.10/24",
	"ipv_6_prefix": "",
	"enable_dhcp": true,
	"dhcp": {
		"lease_time": "",
		"router": "",
		"mtu": "",
		"dns_server": ""
	},
	"exclude_ips": "",
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
    "switch_info": {
      "ns": "ed350282-de88-4e2a-98fc-da2029a60138",
      "tenant": "",
      "tenant_name": "",
      "ctime": 1573092187,
      "mtime": 1573092187,
      "uuid": "6c66d043-108e-432c-91eb-2b4a599a60fe",
      "name": "aaaa",
      "ac_ls": null,
      "dns_records": null,
      "load_balancer": null,
      "ls_ext_ids": {
        "SubnetGateway": "10.10.10.1",
        "container_port": "0",
        "dhcp_uuid": "2ae15b0a-e980-450e-8846-d1133f110964",
        "enable_dhcp": "true",
        "gate_mac": "52:56:FF:00:DD:C9",
        "iptype": "0",
        "mtu": "1442",
        "subnet": "10.10.10.0/24",
        "vm_port": "0"
      },
      "ports": null,
      "qos_rules": null,
      "other_config": {
        "subnet": "10.10.10.0/24"
      }
    }
  }
}
```

#### 异常返回示例

### 状态码



## /v1/network/switch/delete/loadbalancer
#### 功能：删除交换机负载均衡器
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 无


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/switch/delete/loadbalancer
```
Body:
```	
{
	"tenant": "ed350282-de88-4e2a-98fc-da2029a60138",
	"switch_uuid": "6c66d043-108e-432c-91eb-2b4a599a60fe",
	"switch_name": "aaaa",
	"load_balancer_uuid": "cb08c860-5e9d-4413-a56d-bb855911f843",
	"load_balancer_name": "fasdfsaf",
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


## /v1/network/del/switch
#### 功能：删除交换机
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 无


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/del/switch
```
Body:
```	
{
	"switch_name": "aaaa",
	"tenant": "ed350282-de88-4e2a-98fc-da2029a60138",
	"switch_uuid": "6c66d043-108e-432c-91eb-2b4a599a60fe",
	"real_delete": false,
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




## /v1/network/switch/add/loadbalancer
#### 功能：交换机添加负载均衡器
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
http://localhost:9990/v1/network/switch/add/loadbalancer
```
Body:
```	
{
	"tenant": "ed350282-de88-4e2a-98fc-da2029a60138",
	"name": "aaaa",
	"protocol": "tcp",
	"vip": "10.10.10.11",
	"ip_port": {
		"10.10.10.12": 5556
	},
	"vipport": 5555,
	"switch_uuid": "894410f2-f770-4615-8a87-7acff8b22ca7",
	"switch_name": "fdsfaf",
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


## /v1/network/switch/add/dns
#### 功能：交換機添加dns
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
http://localhost:9990/v1/network/switch/add/dns
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



## /v1/network/switch/del/dns
#### 功能：刪除交换机dns
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
http://localhost:9990/v1/network/switch/del/dns
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


## /v1/network/switch/service/list
#### 功能：获取交换机服务列表
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
http://localhost:9990/v1/network/switch/service/list
```
Body:
```	
{
	"tenant": "ed350282-de88-4e2a-98fc-da2029a60138",
	"switch_uuid": "53ffd0c2-6612-4e59-8b23-78f108936248",
	"page_num": 0,
	"page_size": 10,
	"service_type": null,
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
    "logical_switch": {
      "ns": "ed350282-de88-4e2a-98fc-da2029a60138",
      "tenant": "ed350282-de88-4e2a-98fc-da2029a60138",
      "tenant_name": "lts",
      "ctime": 1573093094,
      "mtime": 1573093094,
      "uuid": "53ffd0c2-6612-4e59-8b23-78f108936248",
      "name": "aaa",
      "ac_ls": null,
      "dns_records": null,
      "load_balancer": null,
      "ls_ext_ids": {
        "container_port": "0",
        "enable_dhcp": "false",
        "gate_mac": "52:56:FF:10:7B:E0",
        "iptype": "0",
        "subnet": "10.10.20.0/24",
        "vm_port": "0"
      },
      "ports": null,
      "qos_rules": null,
      "other_config": {
        "subnet": "10.10.20.0/24"
      }
    },
    "dhcp": null,
    "acls": null,
    "load_balancers": null
  }
}
```

#### 异常返回示例

### 状态码




## /v1/network/acl/add
功能：交换机添加访问控制规则acl
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid
 switch_uuid|string| 是|""  | 交换机uuid
 security_group_uuid|string| 否|""  | 安全组uuid
 acl|Acl object| 是|""  | acl访问控制器

### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 switch_uuid|string| 交换机uuid
 security_group_uuid|string| 安全组uuid
 acl|Acl object| acl访问控制器
 
### 示例

#### 请求示例
```
http://localhost:9990/v1/network/acl/add
```
Body:
```
{	
    "tenant_uuid": "5c028587-14aa-11e9-b0b9-5256ff003400"
    "swtich_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "acl_info":{
        "priority":50,
        "direction":"to-lport",
        "action":  "allow",
        "protocol":"tcp",
        "port":5050,
        "retome":"192.168.201.56/24",
        "switch_port":8000
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
    "tenant_uuid": "5c028587-14aa-11e9-b0b9-5256ff003400"
    "swtich_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "acl_info":{
        "priority":50,
        "direction":"to-lport",
        "action":  "allow",
        "protocol":"tcp",
        "port":5050,
        "retome":"192.168.201.56/24",
        "switch_port":8000
    }
  }
}
```

#### 异常返回示例

### 状态码




## /v1/network/acl/del
功能：交换机删除acl
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid
 switch_uuid|string| 是|""  | 交换机uuid
 acl_uuid|string| 是|""  | acl的uuid


### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 switch_uuid|string| 交换机uuid
 acl_uuid|string| acl的uuid

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/acl/del
```
Body:
```
{	
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "switch_uuid": "5c028587-14aa-11e9-b0b9-5256ff003400"
    "acl_uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400"
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
    "switch_uuid": "5c028587-14aa-11e9-b0b9-5256ff003400"
    "acl_uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400"
  }
}
```

#### 异常返回示例

### 状态码




## /v1/network/switch/port/list
功能：获取交换机端口列表
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid
 switch_uuid|string| 是|""  | 交换机uuid

### 返回参数
名称|参数类型|描述 
---|---|---
 total_count|int| 总数量
 list|array|交换机端口详情列表
 
 #### list对象
 名称|参数类型|描述 
 ---|---|---
 vm_name|string|虚拟机名称
 vm_uuid|string|虚拟机uuid
 network_card_uuid|string|网卡uuid
 switch_port_uuid|string|交换机端口uuid
 

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/switch/port/list?tenant_uuid=4a7e240b-14aa-11e9-b0b9-5256ff003400&switch_uuid=55b2edab-14aa-11e9-b0b9-5256ff003400
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "total_count":1,
    "list":[
        {
            "vm_name":"vm_aaa",
            "vm_uuid":"4a7e240b-14aa-11e9-b0b9-5256ff003400",
            "net_card_uuid":"1c64fac3-14aa-11e9-b0b9-5256ff003400",
            "switch_port_uuid":"5c028587-14aa-11e9-b0b9-5256ff003400"
        }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/network/switch/dhcp/delete
功能：关闭交换机dhcp
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid
 switch_uuid|string| 是|""  | 交换机uuid
 dhcp_uuid|string| 是|""  | dhcp的uuid

### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 switch_uuid|string| 交换机uuid
 dhcp_uuid|string| dhcp的uuid

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/switch/dhcp/delete
```
Body:
```
{	
    "tenant_uuid": "5c028587-14aa-11e9-b0b9-5256ff003400"
    "switch_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "dhcp_uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400"
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
    "switch_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "dhcp_uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400"
  }
}
```

#### 异常返回示例
### 状态码


## /v1/network/switch/dhcp/modify
#### 功能：更新交换机
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|- | 租户uuid
 switch_uuid|string| 是|- | 交换机uuid
 dhcp_uuid|string| 是|- | dhcp的uuid
 lease_time|int| 否|- | 地址租期
 mtu|int| 否|- | 最大传输单元
 dns_server|string| 否|- | dns服务器ip
 exclude_ips|string| 否|- | dhcp从子网分配地址时禁止使用的ip或ip段
 is_close|string| 否|- | 是否关闭dhcp

### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 swtich_uuid|string| 交换机uuid
 dhcp_uuid|string| dhcp的uuid
 lease_time|int| 地址租期
 mtu|int| 最大传输单元
 dns_server|string| dns服务器ip
 exclude_ip|string| dhcp从子网分配地址时禁止使用的ip或ip段
 is_close | bool | 是否关闭dhcp
 
### 示例

#### 请求示例
```
http://localhost:9990/v1/network/switch/dhcp/modify
```
Body:
```
{	
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
    "swtich_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
    "dhcp_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
    "lease_time": 3600,
    "mtu": 1500,
    "dns_server": "",
    "exclude_ip": "",
    "is_close": false
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
    "swtich_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
    "dhcp_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
    "lease_time": 3600,
    "mtu": 1500,
    "dns_server": "",
    "exclude_ip": "",
    "is_close": false
  }
}
```

#### 异常返回示例
### 状态码





## /v1/network/switch/loadbalancer/update
#### 功能：交换机负载均衡器修改
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
http://localhost:9990/v1/network/switch/loadbalancer/update
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











































