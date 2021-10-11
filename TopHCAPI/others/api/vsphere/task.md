
##  /v1/vsphere/task/root_recent/list
#### 功能：获取整个vsphere集群下的最近任务
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
vsphere_uuid |string|是|-|vsphere集群uuid
filter_name|string|否|- |过滤字符串
page_num | int|否|0 |翻页偏移量
page_size | int|否|0 |每页的限制数量
reference | string|否|- |数据中心reference

### 返回参数
名称|参数类型|描述
---|---|---
key|string|任务key值
task_reference|string|任务reference
name|string|任务名称
entity|string|虚拟机id
target|string|目标虚拟机
status|string|状态
progress|int32|进度
detail|string|详情
user|string|用户
create_time|int64|创建时间
start_time|int64|开始时间
finish_time|int64|完成时间
message|string|任务信息
task|struct|任务详情

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
      "key": "task-3074",
      "task_reference": "Task:task-3074",
      "name": "重新配置虚拟机",
      "entity": "VirtualMachine:vm-119",
      "target": "ActiveDirectory",
      "status": "success",
      "progress": 0,
      "detail": "",
      "user": "VSPHERE.LOCAL\\Administrator",
      "create_time": 1630323687,
      "start_time": 1630323687,
      "finish_time": 1630323688,
      "message": "",
      "task": {
        "Key": "task-3074",
        "Task": {
          "Type": "Task",
          "Value": "task-3074"
        },
        "Description": null,
        "Name": "ReconfigVM_Task",
        "DescriptionId": "VirtualMachine.reconfigure",
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
        "QueueTime": "2021-08-30T11:41:27.79623Z",
        "StartTime": "2021-08-30T11:41:27.799549Z",
        "CompleteTime": "2021-08-30T11:41:28.051857Z",
        "EventChainId": 244413,
        "ChangeTag": "",
        "ParentTaskKey": "",
        "RootTaskKey": "",
        "ActivationId": ""
      }
    },
    {
      "key": "task-3073",
      "task_reference": "Task:task-3073",
      "name": "恢复快照",
      "entity": "VirtualMachine:vm-664",
      "target": "Stabilitywi10",
      "status": "success",
      "progress": 0,
      "detail": "",
      "user": "VSPHERE.LOCAL\\Administrator",
      "create_time": 1630323635,
      "start_time": 1630323635,
      "finish_time": 1630323667,
      "message": "",
      "task": {
        "Key": "task-3073",
        "Task": {
          "Type": "Task",
          "Value": "task-3073"
        },
        "Description": null,
        "Name": "RevertToSnapshot_Task",
        "DescriptionId": "vm.Snapshot.revert",
        "Entity": {
          "Type": "VirtualMachine",
          "Value": "vm-664"
        },
        "EntityName": "Stabilitywi10",
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
        "QueueTime": "2021-08-30T11:40:35.097611Z",
        "StartTime": "2021-08-30T11:40:35.101601Z",
        "CompleteTime": "2021-08-30T11:41:07.370567Z",
        "EventChainId": 244399,
        "ChangeTag": "",
        "ParentTaskKey": "",
        "RootTaskKey": "",
        "ActivationId": ""
      }
    },
    {
      "key": "task-3071",
      "task_reference": "Task:task-3071",
      "name": "移除快照",
      "entity": "VirtualMachine:vm-664",
      "target": "Stabilitywi10",
      "status": "success",
      "progress": 0,
      "detail": "",
      "user": "VSPHERE.LOCAL\\Administrator",
      "create_time": 1630323634,
      "start_time": 1630323634,
      "finish_time": 1630323663,
      "message": "",
      "task": {
        "Key": "task-3071",
        "Task": {
          "Type": "Task",
          "Value": "task-3071"
        },
        "Description": null,
        "Name": "RemoveSnapshot_Task",
        "DescriptionId": "vm.Snapshot.remove",
        "Entity": {
          "Type": "VirtualMachine",
          "Value": "vm-664"
        },
        "EntityName": "Stabilitywi10",
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
        "QueueTime": "2021-08-30T11:40:34.765437Z",
        "StartTime": "2021-08-30T11:40:34.776468Z",
        "CompleteTime": "2021-08-30T11:41:03.668794Z",
        "EventChainId": 244389,
        "ChangeTag": "",
        "ParentTaskKey": "",
        "RootTaskKey": "",
        "ActivationId": ""
      }
    },
    }
  ]
}
```

#### 异常返回示例

### 状态码


##  /v1/vsphere/task/root/list
#### 功能：获取整个vsphere集群下的任务
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
List|struct array|任务列表

### List 对象
key|string|任务key值
task_reference|string|任务reference
name|string|任务名称
entity|string|虚拟机id
target|string|目标虚拟机
status|string|状态
progress|int32|进度
detail|string|详情
user|string|用户
create_time|int64|创建时间
start_time|int64|开始时间
finish_time|int64|完成时间
message|string|任务信息
task|struct|任务详情

### 示例

#### 请求示例
```
http://10.30.12.184:8080/v1/vsphere/task/root/list?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&page_num=0&page_size=10&filter_name=&cluster_uuid=52601d51-7b60-4e16-8c77-cedf08056c91
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
    "total_count": 100,
    "list": [
      {
              "key": "task-3247",
              "task_reference": "Task:task-3247",
              "name": "重新配置虚拟机",
              "entity": "VirtualMachine:vm-120",
              "target": "windowsserver2008R2",
              "status": "success",
              "progress": 0,
              "detail": "",
              "user": "VSPHERE.LOCAL\\Administrator",
              "create_time": 1630389276,
              "start_time": 1630389276,
              "finish_time": 1630389276,
              "message": "",
              "task": {
                "Key": "task-3247",
                "Task": {
                  "Type": "Task",
                  "Value": "task-3247"
                },
                "Description": null,
                "Name": "ReconfigVM_Task",
                "DescriptionId": "VirtualMachine.reconfigure",
                "Entity": {
                  "Type": "VirtualMachine",
                  "Value": "vm-120"
                },
                "EntityName": "windowsserver2008R2",
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
                "QueueTime": "2021-08-31T05:54:36.499Z",
                "StartTime": "2021-08-31T05:54:36.508Z",
                "CompleteTime": "2021-08-31T05:54:36.713999Z",
                "EventChainId": 258101,
                "ChangeTag": "",
                "ParentTaskKey": "",
                "RootTaskKey": "",
                "ActivationId": ""
              }
            }
          ]
        }
      }
```

#### 异常返回示例

### 状态码


##  /v1/vsphere/task/resource/list
#### 功能：获取vsphere指定资源的任务列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
vsphere_uuid |string|是|-|vsphere集群uuid
filter_name|string|否|- |过滤字符串
page_num | int|否|0 |翻页偏移量
page_size | int|否|0 |每页的限制数量
reference|string|是|- |(主机、数据中心、数据存储、虚拟机)reference

### 返回参数
名称|参数类型|描述
---|---|---
TotalCount|int|总数
List|struct array|任务列表

### List 对象
key|string|任务key值
task_reference|string|任务reference
name|string|任务名称
entity|string|虚拟机id
target|string|目标虚拟机
status|string|状态
progress|int32|进度
detail|string|详情
user|string|用户
create_time|int64|创建时间
start_time|int64|开始时间
finish_time|int64|完成时间
message|string|任务信息
task|struct|任务详情

### 示例

#### 请求示例
```
http://10.30.12.184:8080/v1/vsphere/task/resource/list?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&page_num=0&reference=VirtualMachine:vm-119&
page_size=10&filter_name=&cluster_uuid=52601d51-7b60-4e16-8c77-cedf08056c91
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
    "total_count": 10,
    "list": [
      {
        "key": "task-3276",
        "task_reference": "Task:task-3276",
        "name": "检查新通知",
        "entity": "Folder:group-d1",
        "target": "Datacenters",
        "status": "success",
        "progress": 0,
        "detail": "",
        "user": "",
        "create_time": 1630397701,
        "start_time": 1630397702,
        "finish_time": 1630397882,
        "message": "",
        "task": {
          "Key": "task-3276",
          "Task": {
            "Type": "Task",
            "Value": "task-3276"
          },
          "Description": null,
          "Name": "",
          "DescriptionId": "com.vmware.vcIntegrity.CheckNotificationTask",
          "Entity": {
            "Type": "Folder",
            "Value": "group-d1"
          },
          "EntityName": "Datacenters",
          "Locked": null,
          "State": "success",
          "Cancelled": false,
          "Cancelable": true,
          "Error": null,
          "Result": null,
          "Progress": 0,
          "Reason": {
            "Name": "VMware vSphere Update Manager Check Notification",
            "ScheduledTask": {
              "Type": "ScheduledTask",
              "Value": "schedule-2"
            }
          },
          "QueueTime": "2021-08-31T08:15:01.673Z",
          "StartTime": "2021-08-31T08:15:02.710999Z",
          "CompleteTime": "2021-08-31T08:18:02.790999Z",
          "EventChainId": 261116,
          "ChangeTag": "",
          "ParentTaskKey": "",
          "RootTaskKey": "",
          "ActivationId": ""
        }
      },]
        }
      }
```

#### 异常返回示例

### 状态码