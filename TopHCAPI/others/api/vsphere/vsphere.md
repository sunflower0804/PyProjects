

## /v1/vsphere/vcluster/create
#### 功能：添加vsphere集群
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 Name     |string |是|- |集群名称
 Host     |string |是|- |集群ip
 User     |string |是|- |用户名
 Password |string |是|- |密码
 Comment  |string |否|“”|注释

### 返回参数
名称|参数类型|描述
---|---|---
vsphere_uuid |string|vsphere集群uuid
VCenterHost|string|vsphere集群主机
VcenterVersion|string|vsphere版本

### 示例

#### 请求示例
```
http://10.30.12.184:8080/v1/vsphere/vcluster/create
```
Body:
```
{
    "name": "镇定",
    "host": "10.30.40.10",
    "user": "administrator@vsphere.local",
    "password": "TopHCS@6666",
    "comment": "",
    "cluster_uuid": "52601d51-7b60-4e16-8c77-cedf08056c91"
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
    "VCenterHost": "10.30.40.10",
    "VcenterVersion": "6.7.3",
    "vsphere_uuid": "e0fd06e7-b891-4fca-ad56-e36981bee2a3"
  }
}
```

#### 异常返回示例

### 状态码


## /v1/vsphere/vcluster/delete
#### 功能：删除vsphere集群
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 vsphere_uuid |string|否|-|vsphere集群uuid

### 返回参数
名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://10.30.12.184:8080/v1/vsphere/vcluster/delete
```
Body:
```
{
    "ClusterUuid": "e0fd06e7-b891-4fca-ad56-e36981bee2a3",
    "TenantUuid": "system",
    "vsphere_uuid": "e0fd06e7-b891-4fca-ad56-e36981bee2a3"
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
  "data": ""
}
```

#### 异常返回示例

### 状态码


##  /v1/vsphere/vcluster/start
#### 功能：vsphere资源集群启动
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
vsphere_uuid |string|否·|-|vsphere集群uuid

### 返回参数
名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://10.30.12.184:8080/v1/vsphere/vcluster/start
```
Body:
```
{
    "ClusterUuid": "e0fd06e7-b891-4fca-ad56-e36981bee2a3",
    "TenantUuid": "system",
    "vsphere_uuid": "e0fd06e7-b891-4fca-ad56-e36981bee2a3"
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
  "data": ""
}
```

#### 异常返回示例

### 状态码


#### 异常返回示例

### 状态码


##  /v1/vsphere/vcluster/stop
#### 功能：vsphere资源集群启动
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
vsphere_uuid |string|是|-|vsphere集群uuid

### 返回参数
名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://10.30.12.184:8080/v1/vsphere/vcluster/stop
```
Body:
```
{
    "ClusterUuid": "e0fd06e7-b891-4fca-ad56-e36981bee2a3",
    "TenantUuid": "system",
    "vsphere_uuid": "e0fd06e7-b891-4fca-ad56-e36981bee2a3"
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
  "data": ""
}
```

#### 异常返回示例

### 状态码


##  /v1/vsphere/vcluster/list
#### 功能：vsphere集群列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 vsphere_uuid |string|是|-|vsphere集群uuid
 filter_name|string|否|- |过滤字符串
 page_num | int|否|0 |翻页偏移量
 page_size | int|否|0 |每页的限制数量

### 返回参数
名称|参数类型|描述
---|---|---
TotalCount|int|总数
List|struct array|集群列表

### List 对象
---|---|---
name     |string |集群名称
host     |string |集群ip
user     |string |用户名
Comment  |string |注释
uuid     |string |集群
createDate     |int64 |创建时间
state     |string |状态
vcenter_version     |string |vsphere版本
is_stop     |bool |是否被启用


### 示例

#### 请求示例
```
http://10.30.12.184:8080/v1/vsphere/vcluster/list?filter_name=&page_num=0&page_size=10&cluster_uuid=52601d51-7b60-4e16-8c77-cedf08056c91
```
Body:
```

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
    "total_count": 1,
    "list": [
      {
        "name": "镇定",
        "host": "10.30.40.10",
        "uuid": "e0fd06e7-b891-4fca-ad56-e36981bee2a3",
        "comment": "",
        "user": "administrator@vsphere.local",
        "createDate": 1630310822,
        "state": "健康",
        "reason": "",
        "vcenter_version": "6.7.3",
        "is_stop": false
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


##  /v1/vsphere/vcluster/host/list
#### 功能：vsphere集群下的主机列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 vsphere_uuid |string|是|-|vsphere集群uuid
 filter_name|string|否|- |过滤字符串
 page_num | int|否|0 |翻页偏移量
 page_size | int|否|0 |每页的限制数量

### 返回参数
名称|参数类型|描述
---|---|---
name|string|主机名称
reference|string|主机reference
vm_num|int|云服务器数
template_num|int|模板数
overallStatus|string|总体状态
connectionState|string|连接状态
runningTime|float64|运行时间
boot_time|int64|启动事件
alarmActionsEnabled|bool|是否告警

### 示例

#### 请求示例
```
http://10.30.12.184:8080/v1/vsphere/vcluster/host/list?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&filter_name=&
page_size=10&page_num=0
```
Body:
```

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
    "total_count": 1,
    "list": [
      {
        "name": "10.30.40.11",
        "reference": "HostSystem:host-9",
        "vm_num": 13,
        "template_num": 1,
        "overallStatus": "red",
        "connectionState": "connected",
        "runningTime": 284.76010027656196,
        "boot_time": 1629287873,
        "lastTimeExitStandByMode": "none",
        "alarmActionsEnabled": true,
        "cpuTotal": 23000,
        "cpuFree": 21837,
        "cpuUsage": 1163,
        "memTotal": 51441324032,
        "memFree": 3641987072,
        "memUsage": 47799336960,
        "diskTotal": 0,
        "diskFree": 0,
        "diskUsage": 0
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


##  /v1/vsphere/vcluster/vm/list
#### 功能：vsphere集群下的虚拟机列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 vsphere_uuid |string|是|-|vsphere集群uuid
 filter_name|string|否|- |过滤字符串
 page_num | int|否|0 |翻页偏移量
 page_size | int|否|0 |每页的限制数量

### 返回参数
名称|参数类型|描述
---|---|---
TotalCount|int|总数
List|struct array|虚拟机列表

### List 对象
name|string|主机名称
reference|string|主机reference
overallStatus|string|总体状态
powerState|string|是否启动
cpu_num|int32|cpu核数
memory_size_mb|int32|内存大小
create_time|int64|创建时间
guest_os|string|操作系统
host|string|宿主机ip
host_connection_state|string|宿主机连接状态
guestMemUsage|int64|内存使用率
alarmActionsEnabled|bool|是否告警
host_reference|string|主机reference

### 示例

#### 请求示例
```
http://10.30.12.184:8080/v1/vsphere/vcluster/vm/list?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&
filter_type=vm&filter_name=&page_size=10&page_num=0&cluster_uuid=52601d51-7b60-4e16-8c77-cedf08056c91
```
Body:
```

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
    "total_count": 13,
    "list": [
     {
            "name": "test",
            "reference": "VirtualMachine:vm-676",
            "overallStatus": "green",
            "powerState": "poweredOn",
            "cpu_num": 2,
            "memory_size_mb": 4096,
            "create_time": 0,
            "guest_os": "Other (32-bit)",
            "host": "10.30.40.11",
            "host_connection_state": "connected",
            "guestMemUsage": 122,
            "annotation": "",
            "alarmActionsEnabled": true,
            "folder_reference": "Folder:group-v3",
            "host_reference": "HostSystem:host-9"
          }
        ]
      }
    }
```

#### 异常返回示例

### 状态码


##  /v1/vsphere/vcluster/vm_template/list
#### 功能：vsphere集群下的模板列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 vsphere_uuid |string|是|-|vsphere集群uuid
 filter_name|string|否|- |过滤字符串
 page_num | int|否|0 |翻页偏移量
 page_size | int|否|0 |每页的限制数量

### 返回参数
名称|参数类型|描述
---|---|---
TotalCount|int|总数
List|struct array|虚拟机模板列表

### List 对象
name|string|主机名称
reference|string|主机reference
overallStatus|string|总体状态
powerState|string|是否启动
cpu_num|int32|cpu核数
memory_size_mb|int32|内存大小
create_time|int64|创建时间
guest_os|string|操作系统
host|string|宿主机ip
host_connection_state|string|宿主机连接状态
guestMemUsage|int64|内存使用率
alarmActionsEnabled|bool|是否告警
host_reference|string|主机reference

### 示例

#### 请求示例
```
http://10.30.12.184:8080/v1/vsphere/vcluster/vm_template/list?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&
filter_name=&page_size=10&page_num=0&cluster_uuid=52601d51-7b60-4e16-8c77-cedf08056c91
```
Body:
```

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
    "total_count": 1,
    "list": [
      {
        "name": "scsi",
        "reference": "VirtualMachine:vm-675",
        "overallStatus": "green",
        "powerState": "poweredOff",
        "cpu_num": 2,
        "memory_size_mb": 4096,
        "create_time": 0,
        "guest_os": "Other (32-bit)",
        "host": "10.30.40.11",
        "host_connection_state": "connected",
        "guestMemUsage": 0,
        "annotation": "",
        "alarmActionsEnabled": true,
        "folder_reference": "Folder:group-v3",
        "host_reference": "HostSystem:host-9"
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


##  /v1/vsphere/vcluster/datastore/list
#### 功能：vsphere集群下的数据存储列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 vsphere_uuid |string|是|-|vsphere集群uuid
 filter_name|string|否|- |过滤字符串
 page_num | int|否|0 |翻页偏移量
 page_size | int|否|0 |每页的限制数量

### 返回参数
名称|参数类型|描述
---|---|---
TotalCount|int|总数
List|struct array|数据存储列表

### List 对象
name|string|数据存储名称
datastore_reference|string|数据存储reference
overallStatus|string|总体状态
url|string|数据存储实际地址
device|string设备名称
driverType|string|设备类型
type|string|数据存储类型
lastUpdateTime|int64|最后一次更新时间
alarmActionsEnabled|bool|是否告警
hosts|int|主机个数
vms|int|虚拟机个数

### 示例

#### 请求示例
```
http://10.30.12.184:8080/v1/vsphere/vcluster/datastore/list?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&
filter_name=&page_size=10&page_num=0&cluster_uuid=52601d51-7b60-4e16-8c77-cedf08056c91
```
Body:
```

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
    "total_count": 7,
    "list": [
    {
            "name": "datastore1",
            "datastore_reference": "Datastore:datastore-10",
            "overallStatus": "green",
            "url": "ds:///vmfs/volumes/61136b40-36766e53-3c76-98039b4696f0/",
            "device": "datastore1",
            "driverType": "SSD",
            "type": "VMFS",
            "lastUpdateTime": 1630314092,
            "alarmActionsEnabled": true,
            "hosts": 1,
            "vms": 1,
            "cpuTotal": 0,
            "cpuFree": 0,
            "cpuUsage": 0,
            "memTotal": 0,
            "memFree": 0,
            "memUsage": 0,
            "diskTotal": 504121786368,
            "diskFree": 466366758912,
            "diskUsage": 37755027456
          }
        ]
      }
    }
```

#### 异常返回示例

### 状态码


##  /v1/vsphere/vcluster/network/list
#### 功能：vsphere集群下的网络列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
vsphere_uuid |string|是|-|vsphere集群uuid
filter_name|string|否|- |过滤字符串
page_num | int|否|0 |翻页偏移量
page_size | int|否|0 |每页的限制数量

### 返回参数
名称|参数类型|描述
---|---|---
TotalCount|int|总数
List|struct array|网络列表

### List 对象
Name|string|网络名称
NetworkReference|string|网络Reference
OverallStatus|string|总体状态
Hosts|int|主机数
Vms|int|虚拟机数
AlarmActionsEnabled|bool|是否告警
Pool|struct|池信息
NetWorkType|string|网络类型
VsphereClient|string|vsphere客户端

### 示例

#### 请求示例
```
http://10.30.12.184:8080/v1/vsphere/vcluster/network/list?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&
filter_name=&page_size=10&page_num=0&cluster_uuid=52601d51-7b60-4e16-8c77-cedf08056c91
```
Body:
```

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
    "total_count": 1,
    "list": [
      {
        "name": "VM Network",
        "network_reference": "Network:network-11",
        "overallStatus": "green",
        "hosts": 1,
        "vms": 14,
        "alarmActionsEnabled": true,
        "pool": {
          "name": "VM Network",
          "accessible": true,
          "ipPoolName": "",
          "IpPoolId": 0
        },
        "self": {
          "Type": "Network",
          "Value": "network-11"
        },
        "net_work_type": "Standard network",
        "vsphere_client": "10.30.40.10"
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


##  /v1/vsphere/vcluster/dashboard
#### 功能：vsphere集群概览
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
vsphere_uuid |string|是|-|vsphere集群uuid

### 返回参数
名称|参数类型|描述
---|---|---
datastore|map[string]int64|数据存储
host|map[string]int|主机
memory|map[string]int64|内存
cpu|map[string]int64|CPU
vm|map[string]int|虚拟机
vm_template|map[string]int|虚拟机模板
alarm|map[string]int|告警

### 示例

#### 请求示例
```
http://10.30.12.184:8080/v1/vsphere/vcluster/dashboard?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&cluster_uuid=52601d51-7b60-4e16-8c77-cedf08056c91
```
Body:
```

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
    "datastore": {
      "diskCapacity": 9256459829248,
      "diskFree": 8200730443776,
      "diskUsed": 1055729385472
    },
    "host": {
      "connected": 1,
      "disconnected": 0,
      "notResponding": 0,
      "total_count": 1
    },
    "memory": {
      "memCapacity": 51441324032,
      "memFree": 3694415872,
      "memUsed": 47746908160
    },
    "cpu": {
      "cpuCapacity": 23000,
      "cpuFree": 22296,
      "cpuUsed": 704
    },
    "vm": {
      "poweredOff": 4,
      "poweredOn": 9,
      "suspended": 0,
      "total_count": 13
    },
    "vm_template": {
      "total_count": 1
    },
    "alarm": {
      "confirm": 3,
      "total_count": 4,
      "unconfirmed": 1
    }
  }
}
```

#### 异常返回示例

### 状态码