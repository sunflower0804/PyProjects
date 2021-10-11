# overview

## /v1/cluster/overview/operation
#### 功能：运营概览
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 cluster_uuid|string| 否|- | 集群uuid 
 tenant_uuid|string| 否|-  | 租户uuid

### 返回参数
名称|参数类型|描述 
---|---|---
cluster|[cluster_object](overview.md#cluster_object) |集群信息
ticket|Ticket object | 工单信息
tenant|Tenant object | 租户信息
billing|Billing object| 计费信息

#### cluster_object
名称|参数类型|描述
---|---|---
cluster_name|string|  集群名称

#### Ticket 对象
名称|参数类型|描述
---|---|---
unprocessed|int|未处理工单数量

#### Tenant 对象
名称|参数类型|描述
---|---|---
tenant_num|int|租户数量
user_group_num|int|用户组数量
user_num|int|用户数量
tenant_policy_num|int|租户策略数量

#### Billing 对象
名称|参数类型|描述
---|---|---
cpu_fee|float64|cpu花费
mem_fee|float64|内存花费
disk_fee|float64|磁盘花费


### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/cluster/overview/operation?cluster_uuid=5c028587-1639-11e9-8b6e-5254fffffffe&tennat_uuid=55b2edab-305c-461a-b49d-2f9847f037e1
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
        "cluster": {
          "cluster_name": "testname"
        },
        "ticket": {
          "unprocessed": 3
        },
        "tenant": {
          "tenant_num": 1,
          "user_group_num": 0,
          "user_num": 8,
          "tenant_policy_num": 0
        },
        "billing": null
  }
}
```

#### 异常返回示例
### 状态码

## /v1/cluster/overview/compute
#### 功能：计算概览
#### 请求类型：

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 cluster_uuid|string| 否|- | 集群uuid 
 tenant_uuid|string| 否|-  | 租户uuid

### 返回参数
名称|参数类型|描述
---|---|---
total|int32| 
no_state_count|int32| 
running_count|int32| 
blocked_count|int32| 
paused_count|int32| 
shutdown_count|int32| 
shutoff_count|int32| 
crashed_count|int32| 
power_manager_suspend_count|int32| 
cloning_count|int32| 
save_count|int32| 
migrating_count|int32| 
pending_count|int32| 
importing_count|int32| 
unknown_count|int32| 


### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/cluster/overview/compute?cluster_uuid=5c028587-1639-11e9-8b6e-5254fffffffe&tennat_uuid=55b2edab-305c-461a-b49d-2f9847f037e1
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "total": 1,
    "no_state_count": 1,
    "running_count": 1,
    "blocked_count": 1,
    "paused_count": 1,
    "shutdown_count": 1,
    "shutoff_count": 1,
    "crashed_count": 1,
    "power_manager_suspend_count": 1,
    "cloning_count": 1,
    "save_count": 1,
    "migrating_count": 1,
    "pending_count": 1,
    "importing_count": 1,
    "unknown_count": 1,
  }
}
```

#### 异常返回示例

### 状态码



## /v1/cluster/overview/qos
#### 功能：配额概览
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 cluster_uuid|string| 否|- | 集群uuid 
 tenant_uuid|string| 否|-  | 租户uuid

### 返回参数
名称|参数类型|描述 
---|---|---
cpu_info|Qos object| cpu使用概览
memory_info|Qos object| 内存使用概览
disk_info|Qos object| 磁盘使用概览

#### Qos 对象
名称|参数类型|描述
---|---|---
qos_used|uint64|已经使用的数量
qos_total|uint64|总数量
qos_over|uint64|超出的数量


### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/cluster/overview/qos?cluster_uuid=5c028587-1639-11e9-8b6e-5254fffffffe&tennat_uuid=55b2edab-305c-461a-b49d-2f9847f037e1
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "cpu_info":{
        "qos_used":2,
        "qos_total":10,
        "qos_over":0,
    },
    "memory_info":{
        "qos_used":2,
        "qos_total":10,
        "qos_over":0,
    },
    "disk_info":{
        "qos_used":2,
        "qos_total":10,
        "qos_over":0,
    }
  }
}
```

#### 异常返回示例

### 状态码




## /v1/cluster/overview/storage
#### 功能：存储概览
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 cluster_uuid|string| 否|- | 集群uuid 
 tenant_uuid|string| 否|-  | 租户uuid

### 返回参数
名称|参数类型|描述 
---|---|---
inner|Inner object|内部池概览
external|External object|外部池概览

#### Inner 对象
名称|参数类型|描述
---|---|---
total_size|uint64|
used|uint64|
allocated|uint64|
pool_count|int32|
volume_total_count|int32|
volume_health_count|int32|
volume_degrade_count|int32|
volume_failed_count|int32|
physic_host_total_count|int32|
physic_host_health_count|int32|
physic_host_down_count|int32|
cpu_usage|float32|
memory_usage|float32|
capacity_usage|float32|
ssd|int32|
hdd|int32|
data_dev|int32|
cache_dev|int32|

#### External 对象
名称|参数类型|描述
---|---|---
total_size|uint64|
used|uint64|
pool_count|int32|
volume_total_count|int32|


### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/cluster/overview/storage?cluster_uuid=5c028587-1639-11e9-8b6e-5254fffffffe&tennat_uuid=55b2edab-305c-461a-b49d-2f9847f037e1
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "inner": {
        "total_size": 1,
        "used": 1,
        "allocated": 1,
        "pool_count": 1,
        "volume_total_count": 1,
        "volume_health_count": 1,
        "volume_degrade_count": 1,
        "volume_failed_count": 1,
        "physic_host_total_count": 1,
        "physic_host_health_count": 1,
        "physic_host_down_count": 1,
        "cpu_usage": 1,
        "memory_usage": 1,
        "capacity_usage": 1,
        "ssd": 1,
        "hdd": 1,
        "data_dev": 1,
        "cache_dev": 1,
     },
     "external":{
        "total_size": 1,
        "used": 1,
        "pool_count": 1,
        "volume_total_count": 1,
     }
  }
}
```
#### 异常返回示例
### 状态码



## /v1/cluster/overview/network
#### 功能：网络概览
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 cluster_uuid|string| 否|- | 集群uuid 
 tenant_uuid|string| 否|-  | 租户uuid

### 返回参数
名称|参数类型|描述 
---|---|---
switch_num|int32|交换机数量
router_num|int32|路由器数量
gateway_num|int32|网关数量
vip_num|int32|虚拟ip数量
security_group_num|int32|安全组数量
acl_num|int32|acl数量

### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/cluster/overview/network?cluster_uuid=5c028587-1639-11e9-8b6e-5254fffffffe&tennat_uuid=55b2edab-305c-461a-b49d-2f9847f037e1
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "switch_num":1,
    "router_num":1,
    "gateway_num":1,
    "vip_num":1,
    "security_group_num":1,
    "acl_num":1
  }
}
```

#### 异常返回示例

### 状态码


