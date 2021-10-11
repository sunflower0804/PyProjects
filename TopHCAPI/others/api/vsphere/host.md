##  /v1/vsphere/host/inspect
#### 功能：主机详情
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
FaultTolerance|struct|容错
FullName|string|全称
Mo|struct|主机详情

### 示例

#### 请求示例
```
http://10.30.12.184:8080/v1/vsphere/host/inspect?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&
host_reference=HostSystem:host-9&cluster_uuid=52601d51-7b60-4e16-8c77-cedf08056c91
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
    "vendor": "Dell Inc.",
    "model": "PowerEdge R730",
    "cpuMhz": 2300,
    "processor": "Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz",
    "cpuThreads": 20,
    "networkIfs": 4,
    "cpu_info": {
      "cpuPkgs": 1,
      "cpuCores": 10,
      "cpuThreads": 20
    },
    "network_info": {
      "host_name": "esxi4011",
      "network": "1个网络",
      "physics_adapter": 4
    },
    "datastore_num": "7个数据存储",
    "hyperThreading": "",
    "logicalProcessors": 0,
    "vmotionEnabled": false,
    "managementServerIP": "10.30.40.10",
    "faultTolerance": {
      "faultToleranceSupported": false,
      "faultToleranceEnabled": false
    },
    ......
     }
    }
```

#### 异常返回示例

### 状态码


##  /v1/vsphere/host/vm/list
#### 功能：主机下的虚拟机列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 vsphere_uuid |string|是|-|vsphere集群uuid
filter_name|string|否|- |过滤字符串
page_num | int|否|0 |翻页偏移量
page_size | int|否|0 |每页的限制数量
host_reference|string|是|- |主机Reference

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
http://10.30.12.184:8080/v1/vsphere/host/vm/list?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&host_reference=HostSystem:host-9&
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
    "total_count": 14,
    "list": [
      {
        "name": "ActiveDirectory",
        "reference": "VirtualMachine:vm-119",
        "overallStatus": "green",
        "powerState": "poweredOn",
        "cpu_num": 4,
        "memory_size_mb": 8192,
        "create_time": 0,
        "guest_os": "Microsoft Windows Server 2008 R2 (64 位)",
        "host": "10.30.40.11",
        "host_connection_state": "connected",
        "guestMemUsage": 81,
        "annotation": "",
        "alarmActionsEnabled": true,
        "folder_reference": "Folder:group-v3",
        "host_reference": "HostSystem:host-9"
      },
      ]
        }
      }
```

#### 异常返回示例

### 状态码


##  /v1/vsphere/host/vm_template/list
#### 功能：主机下的虚拟机模板列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
vsphere_uuid |string|是|-|vsphere集群uuid
filter_name|string|否|- |过滤字符串
page_num | int|否|0 |翻页偏移量
page_size | int|否|0 |每页的限制数量
host_reference|string|主机reference

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
http://10.30.12.184:8080/v1/vsphere/host/vm_template/list?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&host_reference=HostSystem:host-9&filter_name=&
page_size=10&page_num=0&cluster_uuid=52601d51-7b60-4e16-8c77-cedf08056c91
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


##  /v1/vsphere/host/datastore/list
#### 功能：主机下的数据存储列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
vsphere_uuid |string|是|-|vsphere集群uuid
filter_name|string|否|- |过滤字符串
page_num | int|否|0 |翻页偏移量
page_size | int|否|0 |每页的限制数量
host_reference|string|主机reference

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
http://10.30.12.184:8080/v1/vsphere/host/datastore/list?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&host_reference=HostSystem:host-9&filter_name=&
page_size=10&page_num=0&cluster_uuid=52601d51-7b60-4e16-8c77-cedf08056c91
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
        "name": "DataStore-HDD2",
        "datastore_reference": "Datastore:datastore-25",
        "overallStatus": "green",
        "url": "ds:///vmfs/volumes/5fac9d78-a46e89c2-20a3-ecf4bbdb8284/",
        "device": "DataStore-HDD2",
        "driverType": "NonSSD",
        "type": "VMFS",
        "lastUpdateTime": 1630395404,
        "alarmActionsEnabled": true,
        "hosts": 1,
        "vms": 9,
        "cpuTotal": 0,
        "cpuFree": 0,
        "cpuUsage": 0,
        "memTotal": 0,
        "memFree": 0,
        "memUsage": 0,
        "diskTotal": 2000112582656,
        "diskFree": 1510742163456,
        "diskUsage": 489370419200
      },
       ]
        }
      }
```

#### 异常返回示例

### 状态码


##  /v1/vsphere/host/network/list
#### 功能：主机下的网络列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
vsphere_uuid |string|是|-|vsphere集群uuid
filter_name|string|否|- |过滤字符串
page_num | int|否|0 |翻页偏移量
page_size | int|否|0 |每页的限制数量
host_reference|string|主机reference

### 返回参数
名称|参数类型|描述
---|---|---
TotalCount|int|总数
List|struct array|虚拟机列表

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
http://10.30.12.184:8080/v1/vsphere/host/network/list?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&host_reference=HostSystem:host-9&filter_name=&page_size=10&
page_num=0&cluster_uuid=52601d51-7b60-4e16-8c77-cedf08056c91
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
        "vms": 15,
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


##  /v1/vsphere/host/recent_tasks/list
#### 功能：获取vsphere指定主机当前的任务
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
vsphere_uuid |string|是|-|vsphere集群uuid

### 返回参数
名称|参数类型|描述
---|---|---
name|string|任务名称
target|string|目标主机
description|string|描述
user|string|用户
entityName|string|实体名称
cancelled|bool|已取消
cancelable|bool|可取消
queueTime|int64|队列时间
startTime|int64|开始事件
completeTime|int64|完成时间
state|string|状态
error|string|错误信息

### 示例

#### 请求示例
```
http://10.30.12.184:8080/v1/vsphere/task/root_recent/list?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&cluster_uuid=52601d51-7b60-4e16-8c77-cedf08056c91
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
  "data": [
    {
      "key": "task-3275",
      "task_reference": "Task:task-3275",
      "name": "SetScreenResolution",
      "entity": "VirtualMachine:vm-119",
      "target": "ActiveDirectory",
      "status": "success",
      "progress": 0,
      "detail": "",
      "user": "VSPHERE.LOCAL\\Administrator",
      "create_time": 1630396630,
      "start_time": 1630396630,
      "finish_time": 1630396631,
      "message": "",
      "task": {
        "Key": "task-3275",
        "Task": {
          "Type": "Task",
          "Value": "task-3275"
        },
        "Description": null,
        "Name": "SetScreenResolution",
        "DescriptionId": "VirtualMachine.setScreenResolution",
        "Entity": {
          "Type": "VirtualMachine",
          "Value": "vm-119"
        },
        "EntityName": "ActiveDirectory",
        "Locked": null,
        "State": "success",
        "Cancelled": false,
        "Cancelable": false,
        "Error": null,
        "Result": null,
        "Progress": 0,
        "Reason": {
          "UserName": "VSPHERE.LOCAL\\Administrator"
        },
        "QueueTime": "2021-08-31T07:57:10.416024Z",
        "StartTime": "2021-08-31T07:57:10.42206Z",
        "CompleteTime": "2021-08-31T07:57:11.753522Z",
        "EventChainId": 260572,
        "ChangeTag": "",
        "ParentTaskKey": "",
        "RootTaskKey": "",
        "ActivationId": ""
      }
    },
    ]
    }
```

#### 异常返回示例

### 状态码

