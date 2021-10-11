[back to api overview](../api_overview.md#label_api)
### 集群相关接口
## /v1/cluster/add
#### 功能：添加集群
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 ip|string| 是|-| 要添加的集群的某一个节点的ip
 name|string| 是|-| 集群名称
 desc|string| 否|-| 集群描述信息

### 返回参数
名称|参数类型|描述
---|---|---
 uuid|string|集群uuid
 name|string| 集群名称
 desc|string| 集群描述信息
 ip|string| 集群节点ip

### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/cluster/add
```
Body:
```
{
    "ip": "192.168.201.101",
    "name": "name_192.168.201.101",
    "desc": "第一个集群"
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
      "uuid": "",
      "name": "name_192.168.201.101",
      "desc": "第一个集群"
      "ip": "192.168.201.101"
  }
}
```

#### 异常返回示例

### 状态码


## /v1/cluster/delete
#### 功能：删除集群
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 cluster_uuid|string| 是|-| 集群uuid
 force|bool| 否|false| 是否强制删除

### 返回参数
名称|参数类型|描述 
---|---|---
uuid|string| 集群uuid
name|string| 集群名称


### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/cluster/delete
```
Body:
```
{	
    "cluster_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"，
    "force": true
}
```


#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "name": "cluster_name1"
  }
}
```

#### 异常返回示例

### 状态码


## /v1/cluster/get
#### 功能：获取集群详情
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 cluster_uuid|string| 是|- | 集群uuid

### 返回参数
名称|参数类型|描述 
---|---|---
 cluster_uuid|string| 集群uuid
 name|string| 集群名称
 desc|string| 集群描述信息
 tenants_uuid|[]string| 集群内所有的租户
 candidates|[]object| 集群拓扑节点列表

### 示例

#### 请求示例
```
http://10.30.12.161:9990/v1/cluster/get?cluster_uuid=9505d119-0fa8-4a57-b693-5e8ab7b64466
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
     "cluster_uuid": "9505d119-0fa8-4a57-b693-5e8ab7b64466",
     "name": "cluster_6",
     "desc": "",
     "tenants": [],
     "candidates": [
       "10.30.12.6"
     ],
     "TopoHostNode": [
       {
         "UUID": "21d61a68-b30f-4350-ac38-0dd69231648d",
         "ID": 1,
         "managerNet": {
           "Name": "ens56",
           "Addrs": [
             "10.30.12.137/24"
           ],
           "MTU": 1450,
           "BridgeUUID": "",
           "BridgeName": ""
         },
         "computeNet": null,
         "storageNet": {
           "Name": "ens56",
           "Addrs": [
             "10.30.12.137/24"
           ],
           "MTU": 1450,
           "BridgeUUID": "",
           "BridgeName": ""
         },
         "backupNet": {
           "Name": "ens56",
           "Addrs": [
             "10.30.12.137/24"
           ],
           "MTU": 1450,
           "BridgeUUID": "",
           "BridgeName": ""
         },
         "domain": "491e797f-fd4b-46eb-a76c-4880f2ac4b12",
         "name": "10.30.12.137",
         "IsSystemService": false,
         "services": {
           "UUID": "21d61a68-b30f-4350-ac38-0dd69231648d",
           "manager": null,
           "center": null,
           "usm": null,
           "vsm": null,
           "network": null,
           "hyper": null,
           "agentStatus": 1,
           "hostMode": 0
         }
       },
       {
         "UUID": "2748d997-8162-4ac7-942a-2d56e9c38c49",
         "ID": 0,
         "managerNet": {
           "Name": "eth0",
           "Addrs": [
             "10.30.12.6/24"
           ],
           "MTU": 1500,
           "BridgeUUID": "",
           "BridgeName": ""
         },
         "computeNet": null,
         "storageNet": {
           "Name": "eth0",
           "Addrs": [
             "10.30.12.6/24"
           ],
           "MTU": 1500,
           "BridgeUUID": "",
           "BridgeName": ""
         },
         "backupNet": {
           "Name": "eth0",
           "Addrs": [
             "10.30.12.6/24"
           ],
           "MTU": 1500,
           "BridgeUUID": "",
           "BridgeName": ""
         },
         "domain": "b4d07ddb-5229-4d54-8938-92aa0a5f6686",
         "name": "10.30.12.6",
         "IsSystemService": true,
         "services": {
           "UUID": "2748d997-8162-4ac7-942a-2d56e9c38c49",
           "manager": {
             "enabled": true,
             "mode": 0,
             "status": 0
           },
           "center": {
             "enabled": true,
             "mode": 5,
             "status": 1
           },
           "usm": null,
           "vsm": null,
           "network": null,
           "hyper": null,
           "agentStatus": 1,
           "hostMode": 0
         }
       }
     ]
   }
 }
```

#### 异常返回示例

### 状态码


## /v1/cluster/list
#### 功能：获取集群列表
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
filter_name|string| 否|- | 过滤集群名称
filter_uuid|string| 否|- | 过滤集群uuid
page_num|int| 否|0| 第几页
page_size|int| 否|0| 每页多少条数据

### 返回参数
名称|参数类型|描述 
---|---|---
 total_count|int| 总数量
 list|array| 集群列表

#### list 对象
名称|参数类型|描述
---|---|---
 cluster_uuid|string| 集群uuid
 cluster_name|string| 集群名称
 ctime|int64| 创建时间


### 示例

#### 请求示例
```
http://10.30.12.161:9990/v1/cluster/list
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "messageCn": "",
  "stack": null,
  "data": {
    "list": [
      {
        "cluster_uuid": "4e6dd97b-e937-4b78-ad3d-10a716bc29a3",
        "cluster_name": "louis",
        "ctime": 0,
        "candidates": null
      },
      {
        "cluster_uuid": "b088822c-1176-4c79-9df7-5fad80c7fd1d",
        "cluster_name": "clster_161_0924",
        "ctime": 0,
        "candidates": null
      }
    ],
    "total_count": 2
  }
}
```

#### 异常返回示例

### 状态码


## /v1/cluster/top
#### 功能：获取集群top
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 cluster_uuid|string| 是|-  | 集群uuid
 count|int| 是|-  | 想要查看的排名的数量

### 返回参数
名称|参数类型|描述 
---|---|---
total_count|int|总数量
cpu_usage_info|[]HostUsageInfo|主机cpu使用排名详情
mem_usage_info|[]HostUsageInfo|主机内存使用排名详情
net_riops_usage_info|[]HostUsageInfo|网卡IOPS接收排名详情
net_wiops_usage_info|[]HostUsageInfo|网卡IOPS发送排名详情
net_rmbps_usage_info|[]HostUsageInfo|网卡速率接收排名详情
net_wmbps_usage_info|[]HostUsageInfo|网卡速率发送排名详情
disk_riops_usage_info|[]HostUsageInfo|磁盘IOPS接收排名详情
disk_wiops_usage_info|[]HostUsageInfo|磁盘IOPS发送排名详情
disk_rspeed_usage_info|[]HostUsageInfo|磁盘速率接收排名详情
disk_wspeed_usage_info|[]HostUsageInfo|磁盘速率发送排名详情
disk_riowait_usage_info|[]HostUsageInfo|磁盘iowait接收排名详情
disk_wiowait_usage_info|[]HostUsageInfo|磁盘iowait发送排名详情

#### HostUsageInfo 对象
名称|参数类型|描述
---|---|---
 host_info|HostInfo object| 主机信息
 cpu_usage|float64|cpu使用率
 mem_usage|float64|内存使用率
 
 net_wiops|uint64|
 net_riops|uint64|
 net_wmbps|uint64|
 net_rmbps|uint64|
 
 disk_riops|uint64|
 disk_wiops|uint64|
 disk_rspeed|uint64|
 disk_wspeed|uint64|
 disk_riowait|uint64|
 disk_wiowait|uint64|
 
#### HostInfo 对象
名称|参数类型|描述
---|---|---
uuid|string|
addr|string|
ctime|int64|
hostname|string |
uptime|int64 |
boot_time|int64 |
procs|int64 |
os|string |
platform|string |
platform_family|string |
platform_version|string |
kernel_version|string |
virtualization_system|string |
virtualization_role|string |
host_id|string | 主机信息
 
### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/cluster/top?cluster_uuid=323-32r-3ref-3wf32&count=3
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
        "total_count": 1,
        "list": [
          {
            "host_info": {
              "uuid": "2ccac5a2-95bb-41d6-b161-4330e371777a",
              "addr": "",
              "ctime": 1545906480,
              "hostname": "TOS-192.168.201.187",
              "uptime": 189312,
              "boot_time": 1545717186,
              "procs": 310,
              "os": "linux",
              "platform": "ubuntu",
              "platform_family": "debian",
              "platform_version": "16.04",
              "kernel_version": "4.14.254",
              "virtualization_system": "kvm",
              "virtualization_role": "host",
              "host_id": ""
            },
            "cpu_usage": 6.3124784557129345,
            "mem_usage": 14.893124758895068,
            "net_wiops": 2,
            "net_riops": 47,
            "net_wmbps": 891,
            "net_rmbps": 4700,
            "disk_riops": 0,
            "disk_wiops": 0,
            "disk_rspeed": 0,
            "disk_wspeed": 272,
            "disk_riowait": 0,
            "disk_wiowait": 46
          },
          ...
        ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/cluster/system/service/storage
#### 功能：获取集群存储信息(融合存储和外置存储)
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid

### 返回参数
名称|参数类型|描述
---|---|---
inner|inner object |融合存储数据
external|external object | 外置存储数据

#### inner对象
名称|参数类型|描述
---|---|---
total_size|uint64|总容量
used|uint64|已使用容量
allocated|uint64|置备容量
pool_count|int32|存储池数量
volume_total_count|int32|存储卷数量
volume_health_count|int32|存储卷健康数量
volume_degrade_count|int32|存储卷降级数量
volume_failed_count|int32|存储卷失效数量
physic_host_total_count|int32|物理主机数量
physic_host_health_count|int32|物理主机健康数量
physic_host_down_count|int32|物理主机宕机数量
cpu_usage|float32|物理主机cup使用率
memory_usage|float32|物理主机内存使用率
capacity_usage|float32|物理主机存储使用率
ssd|int32|固体硬盘数量
hdd|int32|机械硬盘数量
data_dev|int32|数据盘数量
storage_host_total_count|int32|存储主机总数
storage_host_health_count|int32|存储主机健康总数
storage_host_down_count|int32|存储主机宕机总数


#### external 对象
名称|参数类型|描述
---|---|---
total_size|uint64|总容量
used|uint64|已使用容量
pool_count|int32|存储池数量
volume_total_count|int32|存储卷数量


### 示例

#### 请求示例
```
http://10.30.12.52:8080/v1/cluster/system/service/storage?cluster_uuid=667822c9-fec0-43ca-94dc-68ed45becce3
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "messageCn": "",
  "stack": null,
  "data": {
    "inner": {
      "total_size": 214643503104,
      "used": 691019776,
      "allocated": 22548578304,
      "pool_count": 5,
      "volume_total_count": 34,
      "volume_health_count": 34,
      "volume_degrade_count": 0,
      "volume_failed_count": 0,
      "physic_host_total_count": 2,
      "physic_host_health_count": 2,
      "physic_host_down_count": 0,
      "cpu_usage": 0.6072706,
      "memory_usage": 0.07809637,
      "capacity_usage": 0.0032193835,
      "ssd": 0,
      "hdd": 1,
      "data_dev": 1,
      "cache_dev": 0,
      "storage_host_total_count": 0,
      "storage_host_health_count": 0,
      "storage_host_down_count": 0
    },
    "external": {
      "total_size": 0,
      "used": 0,
      "pool_count": 0,
      "volume_total_count": 0
    }
  }
}
```

#### 异常返回示例

### 状态码


## /v1/cluster/system/service/network
功能：系统服务：网络
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 否|- | 集群uuid

### 返回参数
名称|参数类型|描述
---|---|---
 router_summary|[RouterSummary_object](./systemservice.md#RouterSummary_object)| 路由器概览
 switch_summary|[SwitchSummary_object](./systemservice.md#SwitchSummary_object)| 交换机概览
 gateway_summary|[GatewaySummary_object](./systemservice.md#GatewaySummary_object)| 网关概览
 service_summary|[ServiceSummary_object](./systemservice.md#ServiceSummary_object)| 服务概览
 sdn_controller|[Sdncontroller_object](./systemservice.md#Sdncontroller_object)| sdn控制器信息

#### RouterSummary_object
名称|参数类型|描述
---|---|---
router_num|int32|
start_num|int32|
stop_num|int32|

#### SwitchSummary_object
名称|参数类型|描述
---|---|---
switch_num|int32|交换机数量
no_connection|int32|未连接数量
connection|int32|连接数量
otherconfig|map[string]string|其他配置信息

#### GatewaySummary_object
名称|参数类型|描述
---|---|---
gateway_num|int32|网关数量
no_connection|int32|未连接数量
connection|int32|连接数量
other_config|map[string]string|其他配置信息

#### ServiceSummary_object
名称|参数类型|描述
---|---|---
floating_ips_num|int32|
port_mapping_num|int32|端口映射数量
load_balancer_num|int32|负载均衡数量
nats_num|int32|nat数量
security_group_num|int32|安全组数量
security_specification_num|int32|安全规则数量


#### Sdncontroller_object
名称|参数类型|描述
---|---|---
ip_addr|string|ip地址
host_ip|string|主机ip
status|string|状态
other_config|map[string]string|其他配置
cpu_info|[CPUInfo_object](./systemservice.md#CPUInfo_object)|状态
mem_info|[MemInfo_object](./systemservice.md#MemInfo_object)|状态
network_card_info|[NetworkcardInfo_object](./systemservice.md#NetworkcardInfo_object)|状态

#### CPUInfo_object
名称|参数类型|描述
---|---|---
idle|float64|空闲百分比
used|float64|已使用百分比
io_wait|float64|io延时

#### MemInfo_object
名称|参数类型|描述
---|---|---
usage_rate|float64|使用率
total|uint64|总数量
available|uint64|可获得的数量
used|uint64|已使用的数量

#### NetworkcardInfo_object
名称|参数类型|描述
---|---|---
usage_rate|float64|使用率
read_mbps|float64|
write_mbps|float64|
status|float64|状态
mtu|float64| 最大传输单元
loss_packet_num|float64|丢包数量

### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/cluster/system/service/network?cluster_uuid=5c028587-1639-11e9-8b6e-5254fffffffe
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    todo
  }
}
```

#### 异常返回示例

### 状态码

## /v1/cluster/cloud/manage
#### 功能：获取集群云管数据
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid

### 返回参数
名称|参数类型|描述
---|---|---
host_info|host_info array |集群节点列表

#### host_info对象
名称|参数类型|描述
---|---|---
etcd_network_peer_sent_bytes_total|map[string]string|etcd发送网络数据总量
etcd_network_peer_sent_failures_total|map[string]string|etcd发送网络数据失败量
etcd_network_peer_received_bytes_total|map[string]string|etcd接收网络数据总量
etcd_network_peer_round_trip_time_seconds_sum|map[string]string|etcd往返时间总和
etcd_base_info|map[string]string|etcd基本信息
host_spec_spice|host_spec_spice object|主机信息
license_expire_date|int64|集群license到期时间
ip|string|集群节点ip
is_leader|bool|是否是leader
status|int32|节点状态
uuid|string|节点主机uuid


### 示例

#### 请求示例
```
http://10.30.12.52:8080/v1/cluster/cloud/manage?cluster_uuid=667822c9-fec0-43ca-94dc-68ed45becce3
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "messageCn": "",
  "stack": null,
  "data": {
    "host_info": [
      {
        "etcd_network_peer_sent_bytes_total": {
          "937ba95f5d1dd974": ""
        },
        "etcd_network_peer_sent_failures_total": {
          "937ba95f5d1dd974": ""
        },
        "etcd_network_peer_received_bytes_total": {
          "937ba95f5d1dd974": ""
        },
        "etcd_network_peer_round_trip_time_seconds_sum": {
          "937ba95f5d1dd974": ""
        },
        "etcd_base_info": {
          "center_node_health": "1",
          "center_node_unhealth": "0",
          "etcd_cluter_health": "health",
          "etcd_data_dir_disk_capacity": "51699699712",
          "etcd_data_dir_disk_free": "15635509248",
          "etcd_debugging_mvcc_db_total_size_in_bytes": "2.2687744e+07",
          "etcd_disk_backend_commit_duration_seconds_count": "75433",
          "etcd_disk_backend_commit_duration_seconds_sum": "1582.462559973002",
          "etcd_disk_wal_fsync_duration_seconds_count": "277902",
          "etcd_disk_wal_fsync_duration_seconds_sum": "5482.815729355915",
          "etcd_network_client_grpc_received_bytes_total": "1.79243969e+08",
          "etcd_network_client_grpc_sent_bytes_total": "6.90051012e+08",
          "etcd_node_count": "1",
          "etcd_server_leader_changes_seen_total": "1",
          "etcd_server_proposals_applied_total": "598152",
          "etcd_server_proposals_committed_total": "598152",
          "etcd_server_proposals_failed_total": "13",
          "etcd_server_proposals_pending": "0",
          "process_resident_memory_bytes": "1.00876288e+08"
        },
        "host_spec_spice": null,
        "license_expire_date": 1572873658,
        "license_existed": false,
        "ip": "10.30.12.52",
        "is_leader": true,
        "status": 1,
        "uuid": "5a2744dc-b17c-4082-8259-ddb91952e1fa",
        "machine_uuid": ""
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/cluster/compute/service/statistic
#### 功能：获取集群计算服务信息
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid
 filter_machine|string| 否|-|按主机uuid过滤
 filter_name|string| 否|-|按主机名称过滤
 page_num|int| 否|0|页码
 page_size|int| 否|0|每页数据条数

### 返回参数
名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://10.30.12.52:8080/v1/cluster/compute/service/statistic?cluster_uuid=667822c9-fec0-43ca-94dc-68ed45becce3&page_num=0&page_size=5
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "messageCn": "",
  "stack": null,
  "data": {
    "total_count": 2,
    "StateSummaryResult": {
      "total": 5,
      "no_state_count": 0,
      "running_count": 0,
      "blocked_count": 0,
      "paused_count": 0,
      "shutdown_count": 0,
      "shutoff_count": 5,
      "crashed_count": 0,
      "pmsuspend_count": 0,
      "cloning_count": 0,
      "save_count": 0,
      "migrating_count": 0,
      "pending_count": 0,
      "importing_count": 0,
      "unknown_count": 0,
      "restoring_count": 0
    },
    "UsageRatio": {
      "Cpu": {
        "Ratio": 0,
        "Logical": 0,
        "Physical": 8
      },
      "Mem": {
        "Ratio": 0,
        "Logical": 0,
        "Physical": 8362889216
      }
    },
    "HostStatistics": [
      {
        "HostUUID": "55c94054-baa1-4882-b1bf-2825b334c92a",
        "Cpu": {
          "Ratio": 0,
          "Logical": 0,
          "Physical": 8
        },
        "Mem": {
          "Ratio": 0,
          "Logical": 0,
          "Physical": 8362889216
        },
        "LogicalInterface": 0,
        "Status": 1,
        "Name": "10.30.12.41",
        "Label": {
          "555": "666",
          "value3": "value3",
          "测试标签": "fff"
        },
        "DiskCount": 0,
        "Mode": 0,
        "VmCount": 0,
        "Baseline": "Westmere",
        "IOMMUEnabled": false,
        "VFIOEnabled": false
      },
      {
        "HostUUID": "826eabbd-5d6e-4060-bd80-b91db01e22a2",
        "Cpu": {
          "Ratio": 0,
          "Logical": 0,
          "Physical": 0
        },
        "Mem": {
          "Ratio": 0,
          "Logical": 0,
          "Physical": 0
        },
        "LogicalInterface": 0,
        "Status": 1,
        "Name": "10.30.12.68",
        "Label": {
          "111": "222",
          "222": "value",
          "4505": "256",
          "555": "666",
          "label1": "value1",
          "label2": "vlue2",
          "new": "wwww",
          "system::secret": "optional",
          "value3": "value3",
          "测试标签": "fff"
        },
        "DiskCount": 0,
        "Mode": 0,
        "VmCount": 0,
        "Baseline": "Westmere",
        "IOMMUEnabled": false,
        "VFIOEnabled": false
      }
    ],
    "HostSummary": {
      "Total": 2,
      "Healthy": 2,
      "NoInUse": 0
    }
  }
}
```
## /v1/cluster/compute/service/statistic/host
#### 功能：获取集群计算服务主机信息
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid
 machine|string| 是|-|主机uuid


### 返回参数
名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://10.30.12.52:8080/v1/cluster/compute/service/statistic/host?cluster_uuid=667822c9-fec0-43ca-94dc-68ed45becce3&page_num=0&page_size=5
```

#### 正常返回示例
```
```

#### 异常返回示例

### 状态码

## /v1/cluster/chassis/list
#### 功能：获取集群chassis列表
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid
 page_num|int| 否|""  | 第几页
 page_size|int| 否|""  | 每页数量
 filt_host_name|string| 否|""  | 过滤主机名
 filter_ip|string| 是|""  | 过滤ip

### 返回参数
名称|参数类型|描述
---|---|---
total_count|int|总数量
list|ChassisInfo array| chassis列表

#### ChassisInfo 对象
名称|参数类型|描述
---|---|---
other_config|map[string]string|其他配置信息
chassis|Chassis object|
encap|Encap object|

#### Chassis 对象
名称|参数类型|描述
---|---|---
chassis_uuid|string|
encaps|[]string|
extra_info|[]string|额外信息
host_name|string|主机名称
chassis_name|string|
nb_cfg|uint32|
vtep_logical_switches|[]string|


#### Encap 对象
名称|参数类型|描述
---|---|---
chassis_uuid|string|
chassis_name|string|
chassis_ip|string|
options|map[string]string|可选项
type|string|类型

### 示例

#### 请求示例                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   +
```
http://192.168.201.57:9990/v1/cluster/chassis/list?cluster_uuid=55b2edab-305c-461a-b49d-2f9847f037e1&page_num=&page_size&filter_ip=&filter_host_name
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


## /v1/cluster/inspection
集群一键检测启动
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-|集群uuid
 cluster_name|string|是|-|集群名称
 check_system|bool|否|false|是否检测系统
 check_network|bool|否|false|是否检测网络
 check_hardware|bool|否|false|是否检测硬件


### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://10.30.12.52:8080/v1/cluster/inspection
```

Body:
```
{
	"cluster_name": "clster_52_0905",
	"check_system": true,
	"check_network": true,
	"check_hardware": true,
	"cluster_uuid": "667822c9-fec0-43ca-94dc-68ed45becce3"
}
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "messageCn": "",
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
    "normal": 0,
    "alarm": 0,
    "fault": 0,
    "score": 0,
    "system": null,
    "network": null,
    "hardware": null,
    "state": 0,
    "finishedPercent": 0,
    "checking": ""
  }
}
```

#### 异常返回示例

### 状态码


## /v1/cluster/inspection/progress
#### 功能：集群一键检测进度情况
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-| 集群uuid

### 返回参数
名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/cluster/host/statistic/inspect?cluster_uuid=1c64fac3-1324-11e9-b910-5254fffffffd&host=192.168.201.25
```

#### 正常返回示例
```

```

#### 异常返回示例

### 状态码



## /v1/cluster/inspection/stop
集群一键检测停止
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-|集群uuid
 cluster_name|string|是|-|集群名称

### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/cluster/inspection/stop
```

Body:
```
{
	"cluster_name": "clster_161_0924",
	"cluster_uuid": "b088822c-1176-4c79-9df7-5fad80c7fd1d"
}
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "messageCn": "",
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
    "normal": 0,
    "alarm": 0,
    "fault": 0,
    "score": 0,
    "system": null,
    "network": null,
    "hardware": null,
    "state": 0,
    "finishedPercent": 0,
    "checking": ""
  }
}
```

#### 异常返回示例

### 状态码



## /v1/cluster/compute/service/drsconfig/get
#### 功能：集群获取计算服务DRS和DPM配置
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid

### 返回参数
名称|参数类型|描述
---|---|---
config|config object |配置信息


#### config对象
名称|参数类型|描述
---|---|---
DRS|DRS object | DRS配置信息
DPM|DPM object | DPM配置信息

#### DRS对象
名称|参数类型|描述
---|---|---
Enabled|bool| DRS是否开启
MaxStep|int32| 单次触发迁移上限（台）
MaxConcurrentMigration|int32| 迁移执行并发数
MaxHostConcurrentMigration|int32| 单主机迁移执行并发数
ThresholdLevel|int32| 触发阈值等级,1-5对应(最保守，保守，普通，激进，最激进)
MinBenefitLevel|int32| 迁移阈值等级,1-5对应(最保守，保守，普通，激进，最激进)

#### DPM对象
名称|参数类型|描述
---|---|---
Enabled|bool| DPM是否开启
HighThreshold|float64| 高阈值；资源使用率（0~100%）。有主机高于该阈值并持续一定时间，将可能触发唤醒主机操作。
LowThreshold|float64| 低阈值；资源使用率（0~100%）。所有主机均低于该阈值并持续较长一段时间，将可能触发主机休眠操作。
### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/cluster/compute/service/drsconfig/get?cluster_uuid=b088822c-1176-4c79-9df7-5fad80c7fd1d
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "messageCn": "",
  "stack": null,
  "data": {
    "config": {
      "DRS": {
        "Enabled": true,
        "MaxStep": 4,
        "MaxConcurrentMigration": 4,
        "MaxHostConcurrentMigration": 2,
        "ThresholdLevel": 3,
        "MinBenefitLevel": 3
      },
      "DPM": {
        "Enabled": false,
        "HighThreshold": 0.8,
        "LowThreshold": 0.45
      }
    }
  }
}
```

#### 异常返回示例

### 状态码



## /v1/cluster/compute/service/drsconfig/update
#### 功能：集群获取计算服务DRS和DPM配置
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid
 cluster_name|string| 否|-|集群名称，操作日志记录使用
 config|config object |是|配置信息

### 返回参数
名称|参数类型|描述
---|---|---
config|config object |配置信息


#### config对象
名称|参数类型|描述
---|---|---
DRS|DRS object | DRS配置信息
DPM|DPM object | DPM配置信息

#### DRS对象
名称|参数类型|描述
---|---|---
Enabled|bool| DRS是否开启
MaxStep|int32| 单次触发迁移上限（台）
MaxConcurrentMigration|int32| 迁移执行并发数
MaxHostConcurrentMigration|int32| 单主机迁移执行并发数
ThresholdLevel|int32| 触发阈值等级,1-5对应(最保守，保守，普通，激进，最激进)
MinBenefitLevel|int32| 迁移阈值等级,1-5对应(最保守，保守，普通，激进，最激进)

#### DPM对象
名称|参数类型|描述
---|---|---
Enabled|bool| DPM是否开启
HighThreshold|float64| 高阈值；资源使用率（0~100%）。有主机高于该阈值并持续一定时间，将可能触发唤醒主机操作。
LowThreshold|float64| 低阈值；资源使用率（0~100%）。所有主机均低于该阈值并持续较长一段时间，将可能触发主机休眠操作。
### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/cluster/compute/service/drsconfig/update
```
Body:
```
{
	"cluster_name": "clster_161_0924",
	"config": {
		"DRS": {
			"Enabled": false,
			"MaxStep": 4,
			"ThresholdLevel": 1,
			"MinBenefitLevel": 3,
			"MaxConcurrentMigration": 4,
			"MaxHostConcurrentMigration": 2
		}
	},
	"cluster_uuid": "b088822c-1176-4c79-9df7-5fad80c7fd1d"
}
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "messageCn": "",
  "stack": null,
  "data": {
    "config": {
      "DRS": {
        "Enabled": false,
        "MaxStep": 4,
        "MaxConcurrentMigration": 4,
        "MaxHostConcurrentMigration": 2,
        "ThresholdLevel": 1,
        "MinBenefitLevel": 3
      },
      "DPM": {
        "Enabled": false,
        "HighThreshold": 0.8,
        "LowThreshold": 0.45
      }
    }
  }
}
```

#### 异常返回示例

### 状态码


## /v1/cluster/deploy/storage_service/vm
#### 功能：部署存储服务虚拟机
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid
 vm_type|string| 是|-|服务类型，可填参数:GST(接入服务)
 manage_cidr|string| 是|-|管理网络
 manage_gateway|string| 是|-|管理网关
 storage_cidr|string| 是|-|存储网络
 storage_gateway|string| 是|-|存储网关

### 返回参数
名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/cluster/deploy/storage_service/vm
```
Body:
```
{
	"manage_cidr": "1.1.1.1/1",
	"storage_cidr": "1.1.1.1/1",
	"vm_type": "GST",
	"storage_gateway": "1.1.1.1",
	"manage_gateway": "1.1.1.1",
	"cluster_uuid": "b088822c-1176-4c79-9df7-5fad80c7fd1d"
}
```

#### 正常返回示例
```
```

#### 异常返回示例

### 状态码


## /v1/cluster/storage_service/vm/list
#### 功能：存储服务虚拟机列表
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid
 filter_ip|string| 否|-|过滤ip
 page_num|int| 否|0|第几页
 page_size|int| 否|0|每页显示条数

### 返回参数
名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/cluster/storage_service/vm/list？cluster_uuid=35c9ge4-34vxg4tg-4454wdgfs-f4435f34
```

#### 正常返回示例
```
```

#### 异常返回示例

### 状态码


## /v1/cluster/storage_service/vm/delete
#### 功能：删除存储服务虚拟机
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid
 force|bool|否|false|是否强制删除
 uuid|string| 是|-|虚拟机(主机)uuid
 name|string| 否|-|虚拟机(主机)名称，记录操作日志使用

### 返回参数
名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/cluster/storage_service/vm/delete
```
Body:
```
{
	"cluster_uuid": "",
	"force": false,
	"uuid": "",
	"name": "",
}
```

#### 正常返回示例
```
```

#### 异常返回示例

### 状态码


## /v1/cluster/deploy/cvm
#### 功能：添加云管服务
#### 请求类型：POST

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid
 MachineUUID|string| 是|-|宿主机uuid
 Networks|Networks array|是|-|ip网络，切片里填一个元素即可

### Networks对象
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
Addr|string| 是|-|IP地址
Gateway|string| 是|-|网关

### 返回参数
名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/cluster/deploy/cvm
```
Body:
```
{
	"Networks": [
		{
			"Addr": "1.1.1.1/1",
			"Gateway": "1.1.1.1"
		}
	],
	"MachineUUID": "964094de-17c1-4eb8-9edd-9aaa41dbad80",
	"cluster_uuid": "b088822c-1176-4c79-9df7-5fad80c7fd1d"
}
```

#### 正常返回示例
```
```

#### 异常返回示例

### 状态码


## /v1/cluster/delete/cvm
#### 功能：删除云管服务
#### 请求类型：POST

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid
 MachineUUID|string| 是|-|cvm主机uuid
 center_candidate_ip|string|否|-|cvm主机ip，用于记录操作日志

### 返回参数
名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/cluster/delete/cvm
```
Body:
```
{
	"MachineUUID": "964094de-17c1-4eb8-9edd-9aaa41dbad80",
	"center_candidate_ip": "10.30.12.11",
	"cluster_uuid": "b088822c-1176-4c79-9df7-5fad80c7fd1d"
}
```

#### 正常返回示例
```
```

#### 异常返回示例

### 状态码


## /v1/cluster/data/snapshot/save
#### 功能：集群元数据快照添加
#### 请求类型：POST

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid
 ip|string| 是|-|center集群节点IP

### 返回参数
名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/cluster/data/snapshot/save
```
Body:
```
{
	"ip": "10.30.10.24",
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
  "data": {
    "meta_data": {
      "status": {
        "code": 0,
        "message": "",
        "messageCn": "",
        "stack": null,
        "desc": "",
        "UUID": ""
      },
      "Snapshot": null,
      "DaemonState": "",
      "SnapshotConfig": null
    }
  }
}
```

#### 异常返回示例

### 状态码



## /v1/cluster/data/snapshot/delete
#### 功能：集群元数据快照删除
#### 请求类型：POST

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid
 ip|string| 是|-|center集群节点IP
 file_name|string| 是|-|元数据文件名

### 返回参数
名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/cluster/data/snapshot/delete
```
Body:
```
{
	"ip": "10.30.10.24",
	"file_name": "snapshot1572936234.db",
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
  "data": {
    "meta_data": {
      "status": {
        "code": 0,
        "message": "",
        "messageCn": "",
        "stack": null,
        "desc": "",
        "UUID": ""
      },
      "Snapshot": null,
      "DaemonState": "",
      "SnapshotConfig": null
    }
  }
}
```

#### 异常返回示例

### 状态码

## /v1/cluster/data/snapshot/list
#### 功能：集群元数据快照列表
#### 请求类型：GET

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid
 ip|string| 是|-|center集群节点IP
 file_name|string|否|-|过滤元数据文件名

### 返回参数
名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.10.25:8080/v1/cluster/data/snapshot/list?ip=10.30.10.24&cluster_uuid=3afdbbfc-e45a-430e-abba-842074a8b035
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
    "meta_data": {
      "status": {
        "code": 0,
        "message": "",
        "messageCn": "",
        "stack": null,
        "desc": "",
        "UUID": ""
      },
      "Snapshot": [
        "snapshot1572928633.db",
        "snapshot1572930374.db",
        "snapshot1572932229.db",
        "snapshot1572932235.db",
        "snapshot1572933977.db",
        "snapshot1572935831.db",
        "snapshot1572935839.db"
      ],
      "DaemonState": "",
      "SnapshotConfig": null
    }
  }
}
```

#### 异常返回示例

### 状态码


## /v1/cluster/data/daemon/state
#### 功能：集群元数据守护进程状态
#### 请求类型：GET

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid
 ip|string| 是|-|center集群节点IP

### 返回参数
名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.10.25:8080/v1/cluster/data/daemon/state?ip=10.30.10.23&cluster_uuid=3afdbbfc-e45a-430e-abba-842074a8b035
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
    "meta_data": {
      "status": {
        "code": 0,
        "message": "",
        "messageCn": "",
        "stack": null,
        "desc": "",
        "UUID": ""
      },
      "Snapshot": null,
      "DaemonState": "running",
      "SnapshotConfig": null
    }
  }
}
```

#### 异常返回示例

### 状态码



## /v1/cluster/data/daemon/start
#### 功能：启动集群元数据守护进程状态
#### 请求类型：POST

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid
 ip|string| 是|-|center集群节点IP

### 返回参数
名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/cluster/data/daemon/start
```
Body:
```
{
	"ip": "10.30.10.24",
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
  "data": {
    "meta_data": {
      "status": {
        "code": 0,
        "message": "",
        "messageCn": "",
        "stack": null,
        "desc": "",
        "UUID": ""
      },
      "Snapshot": null,
      "DaemonState": "",
      "SnapshotConfig": null
    }
  }
}
```

#### 异常返回示例

### 状态码


## /v1/cluster/data/daemon/stop
#### 功能：启动集群元数据守护进程状态
#### 请求类型：POST

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid
 ip|string| 是|-|center集群节点IP

### 返回参数
名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/cluster/data/daemon/stop
```
Body:
```
{
	"ip": "10.30.10.24",
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
  "data": {
    "meta_data": {
      "status": {
        "code": 0,
        "message": "",
        "messageCn": "",
        "stack": null,
        "desc": "",
        "UUID": ""
      },
      "Snapshot": null,
      "DaemonState": "",
      "SnapshotConfig": null
    }
  }
}
```

#### 异常返回示例

### 状态码


## /v1/cluster/data/snapshot/config/inspect
#### 功能：元数据备份策略详情
#### 请求类型：GET

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid
 ip|string| 是|-|center集群节点IP

### 返回参数
名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.10.25:8080/v1/cluster/data/snapshot/config/inspect?ip=10.30.10.25&cluster_uuid=3afdbbfc-e45a-430e-abba-842074a8b035
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
    "meta_data": {
      "status": {
        "code": 0,
        "message": "",
        "messageCn": "",
        "stack": null,
        "desc": "",
        "UUID": ""
      },
      "Snapshot": null,
      "DaemonState": "",
      "SnapshotConfig": {
        "duration": 3600,
        "MTime": 1568947728,
        "DisplayOption": "hour"
      }
    }
  }
}
```

#### 异常返回示例

### 状态码



## /v1/cluster/data/snapshot/config/update
#### 功能：元数据备份策略设置
#### 请求类型：POST

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid
 ip|string| 是|-|center集群节点IP
 display_option|string| 是|-|hour,day,week可选
 duration|int64| 是|-|多久备份一次，单位为秒

### 返回参数
名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.10.25:8080/v1/cluster/data/snapshot/config/update
```
Body:
```
{
	"ip": "10.30.10.25",
	"duration": 86400,
	"display_option": "day",
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
  "data": {
    "meta_data": {
      "status": {
        "code": 0,
        "message": "",
        "messageCn": "",
        "stack": null,
        "desc": "",
        "UUID": ""
      },
      "Snapshot": null,
      "DaemonState": "",
      "SnapshotConfig": null
    }
  }
}
```

#### 异常返回示例

### 状态码


## /v1/cluster/get/global/config
#### 功能：获取集群全局配置
#### 请求类型：GET

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid

### 返回参数
名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.10.25:8080/v1/cluster/get/global/config?cluster_uuid=4f43254f-3rwf342r-325r32f32-32ref3r
```
#### 正常返回示例
```
```

#### 异常返回示例

### 状态码


## /v1/cluster/set/global/config
#### 功能：设置集群全局配置
#### 请求类型：POST

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid
 StorOverAllocationThreshold|float32| 是|-|存储使用上限
 CPUOverAllocationThreshold|float32| 是|-|cpu使用上限
 MemOverAllocationThreshold|float32| 是|-|内存使用上限
 USDOverAllocationThreshold|float32| 是|-|数据盘使用上限

### 返回参数
名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.10.25:8080/v1/cluster/set/global/config
```
Body:
```
{
	"ip": "10.30.10.25",
	"StorOverAllocationThreshold": 0.7,
	"CPUOverAllocationThreshold": 0.8
}
```

#### 正常返回示例
```
```

#### 异常返回示例

### 状态码


## /v1/cluster/host/task/progress
#### 功能：主机任务进度查询
#### 请求类型：GET

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid
 host_uuid|string| 是|-|主机uuid

### 返回参数
名称|参数类型|描述
---|---|---
progress|float64|进度(0-1直接)
### 示例

#### 请求示例
```
http://10.30.10.25:8080/v1/cluster/host/task/progress?cluster_uuid=4354-35rw
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
  "progress":0.7
  }
}
```

#### 异常返回示例

### 状态码



## /v1/cluster/hardware_resources/inspect
#### 功能：集群硬件资源详情
#### 请求类型：GET

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid
 tenant_uuid|string| 否|-|租户uuid
 storage_status|bool| 否|false|是否获取存储状态
 storage_top|bool| 否|false|是否获取存储top
 cpu_status|bool| 否|false|是否获取cpu状态
 cpu_top|bool| 否|false|是否获取cpu top
 memory_status|bool| 否|false|是否获取内存状态
 memory_top|bool| 否|false|是否获取内存 top
 network_status|bool| 否|false|是否获取网络状态
 network_top|bool| 否|false|是否获取网络 top
 vsm_status|bool| 否|false|是否获取vsm状态
 io_status|bool| 否|false|是否获取io状态
 start_time|int64| 否|0|开始时间
 end_time|int64| 否|0|结束时间
 duration|int64| 否|0|
 count|int32| 否|0|


### 返回参数
名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/cluster/hardware_resources/inspect?tenant_uuid=&storage_status=true&cpu_status=true&memory_status=true&network_status=true&storage_top=true&cpu_top=true&memory_top=true&network_top=true&io_status=true&duration=60&start_time=1572936541&end_time=1572940141&count=60&vsm_status=true&moduleName=all&cluster_uuid=b088822c-1176-4c79-9df7-5fad80c7fd1d
```

#### 正常返回示例
```
```

#### 异常返回示例

### 状态码



## /v1/cluster/detail_status/inspect
#### 功能：集群相关数据详情
#### 请求类型：GET

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid
 tenant_uuid|string| 否|-|租户uuid
 vm_status|bool| 否|false|是否获取虚拟机状态
 vm_top|bool| 否|false|是否获取虚拟机top
 storage_status|bool| 否|false|是否获取存储状态
 storage_iops_top|bool| 否|false|是否获取存储iops top
 storage_mbps_top|bool| 否|false|是否获取存储mbps top
 storage_pool_top|bool| 否|false|是否获取存储池 top
 container_status|bool| 否|false|是否获取容器状态
 container_top|bool| 否|false|是否获取容器拓扑
 network_equipment_status|bool| 否|false|是否获取网络设备状态
 security_network_element_status|bool| 否|false|是否获取安全网络设备状态
 tenant_status|bool| 否|false|是否获取租户状态


### 返回参数
名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/cluster/detail_status/inspect?tenant_uuid=&vm_status=true&storage_status=true&container_status=true&network_equipment_status=true&security_network_element_status=true&tenant_status=true&vm_top=true&storage_iops_top=true&storage_mbps_top=true&storage_pool_top=true&container_top=true&moduleName=all&cluster_uuid=b088822c-1176-4c79-9df7-5fad80c7fd1d```
```
#### 正常返回示例
```
```

#### 异常返回示例

### 状态码


## /v1/cluster/overall_status/inspect
#### 功能：集群总体状况详情
#### 请求类型：GET

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid
 tenant_uuid|string| 否|-|租户uuid
 manager_cloud_status|bool| 否|false|
 compute_status|bool| 否|false|是否获取虚拟机状态
 storage_status|bool| 否|false|是否获取存储状态
 network_status|bool| 否|false|是否获取网络状态
 cloud_manage_status|bool| 否|false|


### 返回参数
名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/cluster/overall_status/inspect?manager_cloud_status=true&compute_status=true&storage_status=true&network_status=true&cloud_manage_status=true&cluster_uuid=b088822c-1176-4c79-9df7-5fad80c7fd1d
```
#### 正常返回示例
```
```

#### 异常返回示例

### 状态码



## /v1/cluster/vmserver/service/get
#### 功能：查看租户网络是否打开
#### 请求类型：GET

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid
 tenant|string| 否|-|租户uuid


### 返回参数
名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/cluster/vmserver/service/get?tenant=8b69bb2f-2a6e-4149-9f43-8d2e2b780df1&cluster_uuid=b088822c-1176-4c79-9df7-5fad80c7fd1d#### 正常返回示例
```
#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "messageCn": "",
  "stack": null,
  "data": {
    "network_vm_list": []
  }
}
```

#### 异常返回示例

### 状态码



## /v1/cluster/all_cluster/topology
#### 功能：查看集群网络拓扑图
#### 请求类型：POST

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string| 是|-|集群uuid
 height| int32| 是| 550|拓扑图高度
 width| int32| 是| 760|拓扑图宽度

### 返回参数
名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/cluster/all_cluster/topology
```

Body：
```
{
 "width":760,
 "height":550,
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
    "info": {
      "232671ca-d1e7-44ea-9278-a7c2d5920fa7": {
        "ClusterName": "cluster_name_37",
        "HostIFacesInfo": {
          "10.30.12.120/24": {
            "IFacesInfo": {
              "10.30.12.120/24": {
                "SysName": "",
                "IP": "10.30.12.120/24",
                "Mac": "",
                "IFaceName": "",
                "Health": true,
                "Port": ""
              }
            },
            "CoordinateX": 381,
            "CoordinateY": 161,
            "Hosts": [
              {
                "Type": "nvm",
                "UUID": "af7fc298-3e15-4055-af28-8cb23883416b",
                "ClusterUUID": "",
                "DomainUUID": "",
                "Name": "GNW1629684227",
                "CoordinateX": 336,
                "CoordinateY": 170
              },
              {
                "Type": "GPE",
                "UUID": "5428047c-e311-433e-ad62-095cb5df3a23",
                "ClusterUUID": "",
                "DomainUUID": "",
                "Name": "GPE1629169898",
                "CoordinateX": 432,
                "CoordinateY": 156
              },
              {
                "Type": "cvm",
                "UUID": "48d37075-2961-4dd2-8719-a33e371447ae",
                "ClusterUUID": "",
                "DomainUUID": "",
                "Name": "LCM48d37075-2961-4dd2-8719-a33e371447ae",
                "CoordinateX": 309,
                "CoordinateY": 122
              }
            ],
            "SecVirtMachine": [
              {
                "SecurityVmServer": "",
                "VmSeverUUID": "5428047c-e311-433e-ad62-095cb5df3a23",
                "SecurityType": "GPE",
                "Namespace": "c6363c58-a48f-45e4-aa99-55642023770a",
                "VMName": "GPE1629169898",
                "CoordinateX": 432,
                "CoordinateY": 156
              },
              {
                "SecurityVmServer": "",
                "VmSeverUUID": "ccb7cafd-c27b-46de-a27f-9c419b173560",
                "SecurityType": "GTVR",
                "Namespace": "cadb1027-3a5b-4012-97d3-8092feca912c",
                "VMName": "虚拟路由器",
                "CoordinateX": 367,
                "CoordinateY": 74
              }
            ],
            "VirtMachine": [
              {
                "Type": "GUS",
                "Name": "zhangqi",
                "UUID": "aedae191-43c7-40a7-9c50-5632237de982",
                "Nsuuid": "cadb1027-3a5b-4012-97d3-8092feca912c",
                "CoordinateX": 383,
                "CoordinateY": 185
              },
              {
                "Type": "GUS",
                "Name": "2222",
                "UUID": "c67e4b18-383f-4f90-b8b9-67b3c255b985",
                "Nsuuid": "cadb1027-3a5b-4012-97d3-8092feca912c",
                "CoordinateX": 375,
                "CoordinateY": 237
              }
            ]
          }
        }
      }
    }
  }
}
```

#### 异常返回示例

### 状态码


## /v1/cluster/overview/inspect
#### 功能：查看集群大屏显示
#### 请求类型：GRT

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 start_time| int64| 否| 0|开始时间
 end_time| int64| 否| 0|结束时间
 duration| int64| 否| 0|
 count| int32| 否| 0|
 cluster_uuid| string| 是| - | 集群uuid

### 返回参数
名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/cluster/overview/inspect?start_time=1629953706&end_time=1629957306&duration=60&cluster_uuid=49bb08f9-1c60-49ee-85d6-6fde276895c5
```

#### 正常返回示例
```

```

#### 异常返回示例

### 状态码