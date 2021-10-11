##  /v1/vsphere/datacenter/list
#### 功能：获取vsphere数据中心列表
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
reference|string|数据中心Reference
name|string|数据中心名称
hosts|int|主机数
vms|int|虚拟机数
vm_template|int|虚拟机模板
clusters|int|集群数
networks|int|网络数
datastores|int|数据存储数
datastore|map<string,int64>|存储使用情况
memory|map<string,int64>|内存使用情况
cpu|map<string,int64>|cpu使用情况

### 示例

#### 请求示例
```
http://10.30.12.184:8080/v1/vsphere/datacenter/list?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&
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
        "reference": "Datacenter:datacenter-2",
        "name": "TopSecDC",
        "hosts": 1,
        "vms": 13,
        "vm_template": 1,
        "clusters": 0,
        "networks": 1,
        "datastores": 7,
        "datastore": {
          "diskCapacity": 9256459829248,
          "diskFree": 8201450815488,
          "diskUsed": 1055009013760
        },
        "memory": {
          "memCapacity": 51441324032,
          "memFree": 3628355584,
          "memUsed": 47812968448
        },
        "cpu": {
          "cpuCapacity": 23000,
          "cpuFree": 22039,
          "cpuUsed": 961
        }
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


##  /v1/vsphere/datacenter/hosts/list
#### 功能：获取vsphere指定数据中心的主机概览
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
vsphere_uuid |string|是|-|vsphere集群uuid
filter_name|string|否|- |过滤字符串
page_num | int|否|0 |翻页偏移量
page_size | int|否|0 |每页的限制数量
datacenter_reference|string|是|- |数据中心Reference

### 返回参数
名称|参数类型|描述
---|---|---
TotalCount|int|总数
List|struct array|虚拟机列表

### List 对象
Name| string| 主机名称
Reference| string| 主机Reference
VmNum| int | 虚拟机数量
TemplateNum| int| 模板数量
OverallStatus| string| 总体状态
RunningTime| float64| 运行时间
BootTime| int64|启动时间
AlarmActionsEnabled| bool|是否告警
CpuTotal| int64| cpu总核数
CpuFree| int64| cpu空闲
CpuUsage| int64| cpu使用
MemTotal| int64| 内存总数
MemFree| int64| 内存空闲
MemUsage| int64| 内存使用
DiskTotal| int64| 磁盘总数
DiskFree| int64| 磁盘空闲
DiskUsage| int64| 磁盘使用

### 示例

#### 请求示例
```
http://10.30.12.184:8080/v1/vsphere/datacenter/hosts/list?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&datacenter_reference=Datacenter:datacenter-2&
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
        "name": "10.30.40.11",
        "reference": "HostSystem:host-9",
        "vm_num": 13,
        "template_num": 1,
        "overallStatus": "red",
        "connectionState": "connected",
        "runningTime": 287.2898906752364,
        "boot_time": 1629287873,
        "lastTimeExitStandByMode": "none",
        "alarmActionsEnabled": true,
        "cpuTotal": 23000,
        "cpuFree": 22360,
        "cpuUsage": 640,
        "memTotal": 51441324032,
        "memFree": 3630452736,
        "memUsage": 47810871296,
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


##  /v1/vsphere/datacenter/vms/list
#### 功能：获取vsphere指定数据中的虚拟机概览
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
vsphere_uuid |string|是|-|vsphere集群uuid
filter_name|string|否|- |过滤字符串
page_num | int|否|0 |翻页偏移量
page_size | int|否|0 |每页的限制数量
datacenter_reference|string|是|- |数据中心Reference

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
http://10.30.12.184:8080/v1/vsphere/datacenter/vms/list?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&datacenter_reference=Datacenter:datacenter-2&
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
            "guestMemUsage": 40,
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


##  /v1/vsphere/datacenter/vm_templates/list
#### 功能：获取vsphere指定数据中心的模板概览
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
vsphere_uuid |string|是|-|vsphere集群uuid
filter_name|string|否|- |过滤字符串
page_num | int|否|0 |翻页偏移量
page_size | int|否|0 |每页的限制数量
datacenter_reference|string|是|- |数据中心Reference

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
http://10.30.12.184:8080/v1/vsphere/datacenter/vm_templates/list?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&datacenter_reference=Datacenter:datacenter-2&
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


##  /v1/vsphere/datacenter/networks/list
#### 功能：获取vsphere指定数据中心网络概览
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 vsphere_uuid |string|是|-|vsphere集群uuid
filter_name|string|否|- |过滤字符串
page_num | int|否|0 |翻页偏移量
page_size | int|否|0 |每页的限制数量
datacenter_reference|string|是|- |数据中心Reference

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
http://10.30.12.184:8080/v1/vsphere/datacenter/networks/list?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&datacenter_reference=Datacenter:datacenter-2&
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

##  /v1/vsphere/datacenter/datastores/list
#### 功能：获取vsphere指定的数据中心的datastore概览
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
vsphere_uuid |string|是|-|vsphere集群uuid
filter_name|string|否|- |过滤字符串
page_num | int|否|0 |翻页偏移量
page_size | int|否|0 |每页的限制数量
datacenter_reference|string|是|- |数据中心Reference

### 返回参数
名称|参数类型|描述
---|---|---
TotalCount|int|总数
List|struct array|虚拟机列表

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
http://10.30.12.184:8080/v1/vsphere/datacenter/datastores/list?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&datacenter_reference=Datacenter:datacenter-2&
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
            "lastUpdateTime": 1630323126,
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
            "diskFree": 466349981696,
            "diskUsage": 37771804672
          }
        ]
      }
    }
```

#### 异常返回示例

### 状态码
