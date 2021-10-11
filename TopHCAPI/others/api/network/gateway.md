[back to api overview](../api_overview.md#api)

# gateway



## /v1/network/gateway/info
#### 功能：获取网关详情
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid
 gateway_uuid|string|是|""  | 网关uuid
 
### 返回参数
名称|参数类型|描述 
---|---|---
create_time|int64|创建时间
update_time|int64|修改时间
uuid|string|交换机的uuid
name|string|交换机的名称
ls_ext_ids |[]string|
ports|map[string]string|网关额外信息,包括出口ip、网关名字等信息
other_config|[]string| 其他配置信息

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/gateway/info
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
        "create_time": 0,
        "update_time": 0,
        "uuid": "4129fbff-4715-418f-9fb5-7634327d8696",
        "name": "aaa_my_gate_way",
        "acls": null,
        "dns_records": null,
        "load_balancer": null,
        "ls_exit_ids": {
          "Out_IP": "192.168.1.1/24",
          "gateway": "5c5eaf11-0688-4ff1-a9ea-4e23a7441728",
          "name": "my_gate_way"
        },
        "ports": null,
        "qos_rules": null,
        "other_config": null,
  }
}
```

#### 异常返回示例
### 状态码



## /v1/network/gateway/info/list
#### 功能：获取网关列表
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|-  | 租户uuid
 page_num|int| 否|-  | 第几页 
 page_size|int| 否|-  | 每一页大小 
 filter_name|string| 否|-  | 要查看的网关的名称

### 返回参数
名称|参数类型|描述 
---|---|---
total_count|int|满足条件的网关的数量
list|array|网关列表

#### list对象
名称|参数类型|描述 
---|---|---
create_time|int64|创建时间
update_time|int64|修改时间
uuid|string|交换机的uuid
name|string|交换机的名称
ls_ext_ids |[]string|
ports|map[string]string|网关额外信息,包括出口ip、网关名字等信息
other_config|[]string| 其他配置信息

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/gateway/info/list?tenant_uuid=4a7e240b-14aa-11e9-b0b9-5256ff003400&page_num=0&page_size=10&filter_name=testname&filter_uuid=anblfd
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
        "create_time": 1548139892,
        "update_time": 1548139902,
        "uuid": "4129fbff-4715-418f-9fb5-7634327d8696",
        "name": "aaa_my_gate_way",
        "acls": null,
        "dns_records": null,
        "load_balancer": null,
        "ls_exit_ids": {
          "Out_IP": "192.168.1.1/24",
          "gateway": "5c5eaf11-0688-4ff1-a9ea-4e23a7441728",
          "name": "my_gate_way"
        },
        "ports": null,
        "qos_rules": null,
        "other_config": null,
    }
   ]
  }
}
```

#### 异常返回示例

### 状态码



## /v1/network/gateway/create
功能：添加网关
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|-  | 租户uuid
 gateway_name|string|是|-  | 网关的名称
 out_ip|string|是|- | 出口ip

### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 gateway_name|string| 网关的名称
 out_ip|string| 出口ip

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/switch/create
```
Body:
```
{
  "tenant_uuid": "3fb91ca3-5034-47ee-bccf-cabf7fd5a3fe",
  "name": "gateway1",
  "ip_type": 0,
  "network_name": "manage",
  "zone_uuid": "64864753-88a2-4020-8627-bf055964b4d8",
  "out_ipv_4": "111.111.111.111/24",
  "enable_vlan": false,
  "cluster_uuid": "42e3b0db-5dce-4893-9421-7ae6fe8ac0ee"
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
    "gate_way_info": {
      "ns": "3fb91ca3-5034-47ee-bccf-cabf7fd5a3fe",
      "ctime": 1586856501,
      "mtime": 1586856501,
      "uuid": "fc3c22b0-2b43-4846-afaf-1b0f5b876168",
      "name": "gateway1",
      "ac_ls": null,
      "dns_records": null,
      "load_balancer": null,
      "ls_ext_ids": {
        "IPtype": "0",
        "Out_IPv4": "111.111.111.111/24",
        "gateway": "5b222621-f726-4fa4-a413-31507ba43071",
        "name": "gateway1",
        "vlan": "false",
        "zone": "64864753-88a2-4020-8627-bf055964b4d8",
        "zone_name": "default"
      },
      "ports": null,
      "qos_rules": null,
      "other_config": null,
      "out_ip": "",
      "zone_uuid": "64864753-88a2-4020-8627-bf055964b4d8",
      "zone_name": "default"
    }
  }
}
```

#### 异常返回示例

### 状态码




## /v1/network/gateway/delete
#### 功能：删除网关
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|-  | 租户uuid
 gateway_uuid|string| 是|-  | 网关uuid

### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 gateway_uuid|string| 网关uuid

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/gateway/delete
```
Body:
```
{	
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "gateway_uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400"
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
    "gateway_uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400"
  }
}
```
#### 异常返回示例
### 状态码


## /v1/network/gateway/unrelated/list
#### 功能：获取游离的网关列表
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
http://localhost:9990/v1/network/
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










