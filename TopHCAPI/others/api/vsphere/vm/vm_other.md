
##  /v1/vsphere/vm/datastore/list
#### 功能：虚拟机数据存储列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
vsphere_uuid |string|是|-|vsphere集群uuid
filter_name|string|否|- |过滤字符串
page_num | int|否|0 |翻页偏移量
page_size | int|否|0 |每页的限制数量
vm_reference|string|是|- |虚拟机Reference

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
http://10.30.12.184:8080/v1/vsphere/vm/datastore/list?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&vm_reference=VirtualMachine:vm-119&filter_name=&page_size=10&
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
        "name": "DataStore-HDD2",
        "datastore_reference": "Datastore:datastore-25",
        "overallStatus": "green",
        "url": "ds:///vmfs/volumes/5fac9d78-a46e89c2-20a3-ecf4bbdb8284/",
        "device": "DataStore-HDD2",
        "driverType": "NonSSD",
        "type": "VMFS",
        "lastUpdateTime": 1630397205,
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
        "diskFree": 1510719094784,
        "diskUsage": 489393487872
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


##  /v1/vsphere/vm/network/list
#### 功能：虚拟机网络列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
vsphere_uuid |string|是|-|vsphere集群uuid
filter_name|string|否|- |过滤字符串
page_num | int|否|0 |翻页偏移量
page_size | int|否|0 |每页的限制数量
vm_reference|string|是|- |虚拟机Reference

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
http://10.30.12.184:8080/v1/vsphere/vm/network/list?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&vm_reference=VirtualMachine:vm-119&filter_name=&page_size=10&
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


