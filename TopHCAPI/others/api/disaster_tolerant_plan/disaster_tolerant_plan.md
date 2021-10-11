[back to api overview](../api_overview.md#label_api)
### 异地容灾相关接口
## /v1/disaster_tolerant_plan/add
添加异地容灾计划
### 请求类型
POST

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
---|---|---|---|---
name|string|是|-|容灾计划名称
master_cluster|string|是|-|主站点集群uuid
slave_cluster|string|是|-|备站点集群uuid
rpo|int64|是|-|容灾rpo
dtp_type|string|是|-|容灾类型
local_backup_duration|int64|是|-|本地备份时间
recover_point_reserve_duration|int64|是|-|恢复点保留时间（与恢复点保留数量2选1）
recover_point_reserve_count|int64|是|-|恢复点保留数量（与恢复点保留时间2选1）
compression|bool|是|-|是否压缩传输
enable|bool|是|-|策略是否启用
ProtectedVm|[]DisasterTolerantPlanVm|否|-|容灾保护对象数组
storage_medium|string|是|-|存储介质

### DisasterTolerantPlanVm 对象
名称 | 参数类型 | 是否必填 | 默认值 | 描述
---|---|---|---|---
master_side_uuid|string|是|-|容灾对象在主站点uuid
name|string|是|-|容灾对象名称
recovery_priority|string|是|-|恢复优先级
host_uuid|string|否|-|主机uuid
path|string|否|-|导入路径
ova_path|string|否|-|ova文件路径
tenant|string|否|-|租户uuid
snapshot_name|string|否|-|快照名

### 返回参数

名称|参数类型|描述
---|---|---
total_count|int64|容灾计划总数
infos|[]DisasterTolerantPlanInfo|容灾计划数组

### DisasterTolerantPlanInfo 对象
名称|参数类型|描述
---|---|---
name|string|容灾计划名称
uuid|string|容灾计划uuid
master_cluster|string|容灾计划主站点集群uuid
master_cluster_name|string|容灾计划主站点集群名称
slave_cluster|string|容灾计划备站点集群uuid
slave_cluster_name|string|容灾计划备站点集群名称
protected_vm|[]DisasterTolerantPlanVm|容灾计划保护对象数组
rpo|int64|容灾rpo
local_backup_duration|int64|本地备份时间
recover_point_reserve_duration|int64|恢复点保留时间
enable|bool|是否启用容灾计划
Compression|bool|是否压缩传输
next_execute_time|int64|下一次容灾计划执行时间
ctime|int64|容灾计划创建时间
mtime|int64|容灾计划修改时间
dtp_type|string|容灾类型
datacenter_reference|string|vsphere集群数据中心标识
host_reference|string|vsphere集群主机标识
vm_path_name|string|容灾对象路径名称

### DisasterTolerantPlanVm 对象
名称|参数类型|描述
---|---|---
uuid|string|容灾对象uuid
disaster_tolerant_plan|string|容灾对象所属容灾计划uuid
name|string|容灾对象名称
master_side_uuid|string|容灾对象在主站点的uuid
slave_side_uuid|string|容灾对象在备站点的uuid
running_cluster|string|容灾对象运行站点
procedure|int32|容灾对象状态
last_backup_time|int64|最近一次备份时间
recovery_priority|string|恢复优先级
ctime|int64|创建时间
dtp_type|string|容灾类型
master_side_last_snap|string|容灾对象主站点最新容灾快照名
slave_side_last_snap|string|容灾对象备站点最新容灾快照名

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/disaster_tolerant_plan/add
```
Body:
```
{
	"name": "计划1",
	"master_cluster": "5ea15037-7a21-4233-8c69-b8112156c474",
	"slave_cluster": "b62e7f1b-28c2-4fa7-9226-63231bbd84ea",
	"rpo": 3600,
	"dtp_type": "hci",
	"local_backup_duration": 1800,
	"recover_point_reserve_duration": 2592000,
	"compression": true,
	"enable": true,
	"protected_vm": [
		{
			"master_side_uuid": "d3514d6f-4b92-488e-8f33-6ae1ad7ce5ba",
			"name": "vm2",
			"recovery_priority": "middle"
		}
	],
	"storage_medium": "HDD",
	"cluster_uuid": "5ea15037-7a21-4233-8c69-b8112156c474"
}
```

#### 返回示例
```
{
  "message": "",
  "message_cn": "",
  "scode": 0,
  "desc": "",
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
    "total_count": 1,
    "infos": [
      {
        "name": "计划1",
        "uuid": "28215d7b-6e3e-487d-a7bc-11804b876dda",
        "master_cluster": "5ea15037-7a21-4233-8c69-b8112156c474",
        "master_cluster_name": "cluster_name_213",
        "slave_cluster": "b62e7f1b-28c2-4fa7-9226-63231bbd84ea",
        "slave_cluster_name": "cluster_name_212",
        "protected_vm": [
          {
            "uuid": "ec914c7f-f3c4-4c7d-9bbb-5cc4abea5080",
            "disaster_tolerant_plan": "28215d7b-6e3e-487d-a7bc-11804b876dda",
            "name": "",
            "master_side_uuid": "d3514d6f-4b92-488e-8f33-6ae1ad7ce5ba",
            "slave_side_uuid": "b1603bf2-9777-40a5-8208-62cf5a2d4be7",
            "running_cluster": "5ea15037-7a21-4233-8c69-b8112156c474",
            "procedure": 0,
            "last_backup_time": 0,
            "recovery_priority": "middle",
            "ctime": 1584598413,
            "dtp_type": "",
            "master_side_last_snap": "",
            "slave_side_last_snap": ""
          }
        ],
        "rpo": 3600,
        "local_backup_duration": 1800,
        "recover_point_reserve_duration": 2592000,
        "enable": true,
        "Compression": true,
        "next_execute_time": 1584600213,
        "ctime": 1584598413,
        "mtime": 1584598413,
        "dtp_type": "hci",
        "datacenter_reference": "",
        "host_reference": "",
        "vm_path_name": ""
      }
    ]
  }
}
```

## /v1/disaster_tolerant_plan/get
获取异地容灾计划
### 请求类型
POST

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
---|---|---|---|---
uuid|string|是|-|容灾计划uuid

### 返回参数

名称|参数类型|描述
---|---|---
total_count|int64|容灾计划总数
infos|[]DisasterTolerantPlanInfo|容灾计划数组

### DisasterTolerantPlanInfo 对象
名称|参数类型|描述
---|---|---
name|string|容灾计划名称
uuid|string|容灾计划uuid
master_cluster|string|容灾计划主站点集群uuid
master_cluster_name|string|容灾计划主站点集群名称
slave_cluster|string|容灾计划备站点集群uuid
slave_cluster_name|string|容灾计划备站点集群名称
protected_vm|[]DisasterTolerantPlanVm|容灾计划保护对象
rpo|int64|容灾rpo
local_backup_duration|int64|本地备份时间
recover_point_reserve_duration|int64|恢复点保留时间
enable|bool|是否启用容灾计划
Compression|bool|是否压缩传输
next_execute_time|int64|下一次容灾计划执行时间
ctime|int64|容灾计划创建时间
mtime|int64|容灾计划修改时间
dtp_type|string|容灾类型
datacenter_reference|string|vsphere集群数据中心标识
host_reference|string|vsphere集群主机标识
vm_path_name|string|容灾对象路径名称

### DisasterTolerantPlanVm 对象
名称|参数类型|描述
---|---|---
uuid|string|容灾对象uuid
disaster_tolerant_plan|string|容灾对象所属容灾计划uuid
name|string|容灾对象名称
master_side_uuid|string|容灾对象在主站点的uuid
slave_side_uuid|string|容灾对象在备站点的uuid
running_cluster|string|容灾对象运行站点
procedure|int32|容灾对象状态
last_backup_time|int64|最近一次备份时间
recovery_priority|string|恢复优先级
ctime|int64|创建时间
dtp_type|string|容灾类型
master_side_last_snap|string|容灾对象主站点最新容灾快照名
slave_side_last_snap|string|容灾对象备站点最新容灾快照名

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/disaster_tolerant_plan/get?uuid=28215d7b-6e3e-487d-a7bc-11804b876dda
```

#### 返回示例
```
{
  "message": "",
  "message_cn": "",
  "scode": 0,
  "desc": "",
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
    "total_count": 1,
    "infos": [
      {
        "name": "计划1",
        "uuid": "28215d7b-6e3e-487d-a7bc-11804b876dda",
        "master_cluster": "5ea15037-7a21-4233-8c69-b8112156c474",
        "master_cluster_name": "cluster_name_213",
        "slave_cluster": "b62e7f1b-28c2-4fa7-9226-63231bbd84ea",
        "slave_cluster_name": "cluster_name_212",
        "protected_vm": [
          {
            "uuid": "ec914c7f-f3c4-4c7d-9bbb-5cc4abea5080",
            "disaster_tolerant_plan": "28215d7b-6e3e-487d-a7bc-11804b876dda",
            "name": "",
            "master_side_uuid": "d3514d6f-4b92-488e-8f33-6ae1ad7ce5ba",
            "slave_side_uuid": "b1603bf2-9777-40a5-8208-62cf5a2d4be7",
            "running_cluster": "5ea15037-7a21-4233-8c69-b8112156c474",
            "procedure": 0,
            "last_backup_time": 0,
            "recovery_priority": "middle",
            "ctime": 1584598413,
            "dtp_type": "",
            "master_side_last_snap": "",
            "slave_side_last_snap": ""
          }
        ],
        "rpo": 3600,
        "local_backup_duration": 1800,
        "recover_point_reserve_duration": 2592000,
        "enable": true,
        "Compression": true,
        "next_execute_time": 1584600213,
        "ctime": 1584598413,
        "mtime": 1584598413,
        "dtp_type": "hci",
        "datacenter_reference": "",
        "host_reference": "",
        "vm_path_name": ""
      }
    ]
  }
}
```

## /v1/disaster_tolerant_plan/delete
删除异地容灾计划
### 请求类型
POST

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
uuid|string|是|-|容灾计划uuid

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/disaster_tolerant_plan/delete
```
Body:
```
{
	"uuid": "28215d7b-6e3e-487d-a7bc-11804b876dda"
}
```

#### 返回示例
```
{
  "message": "",
  "message_cn": "",
  "scode": 0,
  "desc": "",
  "stack": null,
  "data": {
    "status": {
      "code": 0,
      "message": "",
      "messageCn": "",
      "stack": null,
      "desc": "",
      "UUID": ""
    }
   }
}
```

## /v1/disaster_tolerant_plan/list
异地容灾计划列表
### 请求类型
POST

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
master_cluster|string|否|-|容灾计划主站点集群uuid
filter_types|[]string|否|-|想要查询的容灾类型数组
fuzzy|string|否|-|过滤关键字
number|int32|否|-|页码
page|int32|否|-|页长

### 返回参数

名称|参数类型|描述
---|---|---
total_count|int64|容灾计划总数
infos|[]DisasterTolerantPlanInfo|容灾计划数组

### DisasterTolerantPlanInfo 对象
名称|参数类型|描述
---|---|---
name|string|容灾计划名称
uuid|string|容灾计划uuid
master_cluster|string|容灾计划主站点集群uuid
master_cluster_name|string|容灾计划主站点集群名称
slave_cluster|string|容灾计划备站点集群uuid
slave_cluster_name|string|容灾计划备站点集群名称
protected_vm|[]DisasterTolerantPlanVm|容灾计划保护对象
rpo|int64|容灾rpo
local_backup_duration|int64|本地备份时间
recover_point_reserve_duration|int64|恢复点保留时间
enable|bool|是否启用容灾计划
Compression|bool|是否压缩传输
next_execute_time|int64|下一次容灾计划执行时间
ctime|int64|容灾计划创建时间
mtime|int64|容灾计划修改时间
dtp_type|string|容灾类型
datacenter_reference|string|vsphere集群数据中心标识
host_reference|string|vsphere集群主机标识
vm_path_name|string|容灾对象路径名称

### DisasterTolerantPlanVm 对象
名称|参数类型|描述
---|---|---
uuid|string|容灾对象uuid
disaster_tolerant_plan|string|容灾对象所属容灾计划uuid
name|string|容灾对象名称
master_side_uuid|string|容灾对象在主站点的uuid
slave_side_uuid|string|容灾对象在备站点的uuid
running_cluster|string|容灾对象运行站点
procedure|int32|容灾对象状态
last_backup_time|int64|最近一次备份时间
recovery_priority|string|恢复优先级
ctime|int64|创建时间
dtp_type|string|容灾类型
master_side_last_snap|string|容灾对象主站点最新容灾快照名
slave_side_last_snap|string|容灾对象备站点最新容灾快照名

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/disaster_tolerant_plan/list
```
Body:
```
{
	"page": 0,
	"number": 10,
	"filter_types": [
		"hci"
	],
	"fuzzy": "",
	"cluster_uuid": "5ea15037-7a21-4233-8c69-b8112156c474"
}
```

#### 返回示例
```
{
  "message": "",
  "message_cn": "",
  "scode": 0,
  "desc": "",
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
    "total_count": 2,
    "infos": [
      {
        "name": "计划1",
        "uuid": "28215d7b-6e3e-487d-a7bc-11804b876dda",
        "master_cluster": "5ea15037-7a21-4233-8c69-b8112156c474",
        "master_cluster_name": "cluster_name_213",
        "slave_cluster": "b62e7f1b-28c2-4fa7-9226-63231bbd84ea",
        "slave_cluster_name": "cluster_name_212",
        "protected_vm": [
          {
            "uuid": "ec914c7f-f3c4-4c7d-9bbb-5cc4abea5080",
            "disaster_tolerant_plan": "28215d7b-6e3e-487d-a7bc-11804b876dda",
            "name": "",
            "master_side_uuid": "d3514d6f-4b92-488e-8f33-6ae1ad7ce5ba",
            "slave_side_uuid": "b1603bf2-9777-40a5-8208-62cf5a2d4be7",
            "running_cluster": "5ea15037-7a21-4233-8c69-b8112156c474",
            "procedure": 0,
            "last_backup_time": 0,
            "recovery_priority": "middle",
            "ctime": 1584598413,
            "dtp_type": "",
            "master_side_last_snap": "",
            "slave_side_last_snap": ""
          }
        ],
        "rpo": 3600,
        "local_backup_duration": 1800,
        "recover_point_reserve_duration": 2592000,
        "enable": true,
        "Compression": true,
        "next_execute_time": 1584600213,
        "ctime": 1584598413,
        "mtime": 1584598413,
        "dtp_type": "hci",
        "datacenter_reference": "",
        "host_reference": "",
        "vm_path_name": ""
      },
      {
        "name": "plan1",
        "uuid": "de77ec92-ab63-4a7e-97dc-6c4e9ec667cf",
        "master_cluster": "b62e7f1b-28c2-4fa7-9226-63231bbd84ea",
        "master_cluster_name": "cluster_name_212",
        "slave_cluster": "5ea15037-7a21-4233-8c69-b8112156c474",
        "slave_cluster_name": "cluster_name_213",
        "protected_vm": [
          {
            "uuid": "0399fca1-fc60-43c8-beb5-c8330bfd65e6",
            "disaster_tolerant_plan": "de77ec92-ab63-4a7e-97dc-6c4e9ec667cf",
            "name": "",
            "master_side_uuid": "3448a0dd-db8f-4ed5-a882-48096ab5367b",
            "slave_side_uuid": "27aba45e-c713-45a9-bc14-c879990b5898",
            "running_cluster": "b62e7f1b-28c2-4fa7-9226-63231bbd84ea",
            "procedure": 0,
            "last_backup_time": 0,
            "recovery_priority": "middle",
            "ctime": 1584590276,
            "dtp_type": "",
            "master_side_last_snap": "",
            "slave_side_last_snap": ""
          }
        ],
        "rpo": 3600,
        "local_backup_duration": 600,
        "recover_point_reserve_duration": 2592000,
        "enable": true,
        "Compression": true,
        "next_execute_time": 1584599276,
        "ctime": 1584590276,
        "mtime": 1584590276,
        "dtp_type": "hci",
        "datacenter_reference": "",
        "host_reference": "",
        "vm_path_name": ""
      }
    ]
  }
}
```

## /v1/disaster_tolerant_plan/edit
异地容灾计划编辑
### 请求类型
POST

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
uuid|string|是|-|容灾计划uuid
name|string|否|-|容灾计划名称
rpo|int64|否|-|容灾rpo
local_backup_duration|int64|否|-|本地备份时间
recover_point_reserve_duration|int64|否|-|恢复点保留时间
recover_point_reserve_count|int64|否|-|恢复点保留数量
compression|bool|否|-|是否压缩传输
enable|bool|否|-|是否启用容灾策略
dtp_type|string|否|-|容灾类型
storage_medium|string|否|-|存储介质
protected_vm|[]DisasterTolerantPlanVm|否|-|容灾保护对象

### DisasterTolerantPlanVm 对象
名称 | 参数类型 | 是否必填 | 默认值 | 描述
---|---|---|---|---
master_side_uuid|string|是|-|容灾对象在主站点uuid
name|string|是|-|容灾对象名称
recovery_priority|string|是|-|恢复优先级
host_uuid|string|否|-|主机uuid
path|string|否|-|导入路径
ova_path|string|否|-|ova文件路径
tenant|string|否|-|租户uuid
snapshot_name|string|否|-|快照名

### 返回参数

名称|参数类型|描述
---|---|---
total_count|int64|容灾计划总数
infos|[]DisasterTolerantPlanInfo|容灾计划数组

### DisasterTolerantPlanInfo 对象
名称|参数类型|描述
---|---|---
name|string|容灾计划名称
uuid|string|容灾计划uuid
master_cluster|string|容灾计划主站点集群uuid
master_cluster_name|string|容灾计划主站点集群名称
slave_cluster|string|容灾计划备站点集群uuid
slave_cluster_name|string|容灾计划备站点集群名称
protected_vm|[]DisasterTolerantPlanVm|容灾计划保护对象
rpo|int64|容灾rpo
local_backup_duration|int64|本地备份时间
recover_point_reserve_duration|int64|恢复点保留时间
enable|bool|是否启用容灾计划
Compression|bool|是否压缩传输
next_execute_time|int64|下一次容灾计划执行时间
ctime|int64|容灾计划创建时间
mtime|int64|容灾计划修改时间
dtp_type|string|容灾类型
datacenter_reference|string|vsphere集群数据中心标识
host_reference|string|vsphere集群主机标识
vm_path_name|string|容灾对象路径名称

### DisasterTolerantPlanVm 对象
名称|参数类型|描述
---|---|---
uuid|string|容灾对象uuid
disaster_tolerant_plan|string|容灾对象所属容灾计划uuid
name|string|容灾对象名称
master_side_uuid|string|容灾对象在主站点的uuid
slave_side_uuid|string|容灾对象在备站点的uuid
running_cluster|string|容灾对象运行站点
procedure|int32|容灾对象状态
last_backup_time|int64|最近一次备份时间
recovery_priority|string|恢复优先级
ctime|int64|创建时间
dtp_type|string|容灾类型
master_side_last_snap|string|容灾对象主站点最新容灾快照名
slave_side_last_snap|string|容灾对象备站点最新容灾快照名

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/disaster_tolerant_plan/edit
```
Body:
```
{
	"uuid": "28215d7b-6e3e-487d-a7bc-11804b876dda",
	"name": "计划12",
	"master_cluster": "cluster_name_213",
	"slave_cluster": "cluster_name_212",
	"rpo": 3600,
	"local_backup_duration": 1800,
	"recover_point_reserve_duration": 2592000,
	"compression": true,
	"enable": true,
	"protected_vm": [
		{
			"uuid": "ec914c7f-f3c4-4c7d-9bbb-5cc4abea5080",
			"disaster_tolerant_plan": "28215d7b-6e3e-487d-a7bc-11804b876dda",
			"name": "",
			"master_side_uuid": "d3514d6f-4b92-488e-8f33-6ae1ad7ce5ba",
			"slave_side_uuid": "b1603bf2-9777-40a5-8208-62cf5a2d4be7",
			"running_cluster": "5ea15037-7a21-4233-8c69-b8112156c474",
			"procedure": 0,
			"last_backup_time": 0,
			"recovery_priority": "middle",
			"ctime": 1584598413,
			"dtp_type": "",
			"master_side_last_snap": "",
			"slave_side_last_snap": ""
		}
	],
	"cluster_uuid": "5ea15037-7a21-4233-8c69-b8112156c474"
}
```

#### 返回示例
```
{
  "message": "",
  "message_cn": "",
  "scode": 0,
  "desc": "",
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
    "total_count": 1,
    "infos": [
      {
        "name": "计划12",
        "uuid": "28215d7b-6e3e-487d-a7bc-11804b876dda",
        "master_cluster": "5ea15037-7a21-4233-8c69-b8112156c474",
        "master_cluster_name": "cluster_name_213",
        "slave_cluster": "b62e7f1b-28c2-4fa7-9226-63231bbd84ea",
        "slave_cluster_name": "cluster_name_212",
        "protected_vm": [
          {
            "uuid": "ec914c7f-f3c4-4c7d-9bbb-5cc4abea5080",
            "disaster_tolerant_plan": "28215d7b-6e3e-487d-a7bc-11804b876dda",
            "name": "",
            "master_side_uuid": "d3514d6f-4b92-488e-8f33-6ae1ad7ce5ba",
            "slave_side_uuid": "b1603bf2-9777-40a5-8208-62cf5a2d4be7",
            "running_cluster": "5ea15037-7a21-4233-8c69-b8112156c474",
            "procedure": 0,
            "last_backup_time": 0,
            "recovery_priority": "middle",
            "ctime": 1584598413,
            "dtp_type": "",
            "master_side_last_snap": "",
            "slave_side_last_snap": ""
          }
        ],
        "rpo": 3600,
        "local_backup_duration": 1800,
        "recover_point_reserve_duration": 2592000,
        "enable": true,
        "Compression": true,
        "next_execute_time": 1584600213,
        "ctime": 1584598413,
        "mtime": 1584599057,
        "dtp_type": "hci",
        "datacenter_reference": "",
        "host_reference": "",
        "vm_path_name": ""
      }
    ]
  }
}
```

## /v1/disaster_tolerant_plan/mastercluster/backup/list
容灾对象主站点数据列表
### 请求类型
POST

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
master_cluster|string|否|-|容灾计划主站点集群uuid
plan_uuid|string|否|-|容灾计划uuid
vm_uuid|[]string|否|-|容灾虚拟机在主站点的uuid数组
filter_types|[]string|否|-|容灾类型数组
fuzzy|string|否|-|过滤关键字
number|int32|否|-|页码
page|int32|否|-|页长

### 返回参数

名称|参数类型|描述
---|---|---
total_count|int32|总数
vms|[]DisasterTolerantMasterClusterVmInfo|容灾主站点集群虚拟机信息数组

### DisasterTolerantMasterClusterVmInfo 对象
名称|参数类型|描述
---|---|---
name|string|容灾对象名称
uuid|string|容灾对象uuid
backup_size|int64|容灾对象备份大小
backup_count|int32|容灾对象备份数量
last_backup_time|int64|最后一次备份时间
belong_cluster|string|容灾对象所属集群uuid
belong_cluster_name|string|容灾对象所属集群名称
disater_tolerant_plan|string|容灾计划uuid
disaster_tolerant_plan_name|string|容灾计划名称
procedure|int32|容灾对象状态
ctime|int64|容灾对象创建时间
dtp_type|string|容灾类型

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/disaster_tolerant_plan/mastercluster/backup/list
```
Body:
```
{
	"master_cluster": "",
	"plan_uuid": "",
	"vm_uuid": [],
	"page": 0,
	"number": 10,
	"filter_types": [
		"hci"
	],
	"fuzzy": null,
	"cluster_uuid": "5ea15037-7a21-4233-8c69-b8112156c474"
}
```

#### 返回示例
```
{
  "message": "",
  "message_cn": "",
  "scode": 0,
  "desc": "",
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
    "total_count": 2,
    "vms": [
      {
        "name": "vm2",
        "uuid": "d3514d6f-4b92-488e-8f33-6ae1ad7ce5ba",
        "backup_size": 0,
        "backup_count": 0,
        "last_backup_time": 0,
        "belong_cluster": "5ea15037-7a21-4233-8c69-b8112156c474",
        "belong_cluster_name": "cluster_name_213",
        "disater_tolerant_plan": "28215d7b-6e3e-487d-a7bc-11804b876dda",
        "disaster_tolerant_plan_name": "计划12",
        "procedure": 0,
        "ctime": 1584598413,
        "dtp_type": "hci"
      },
      {
        "name": "test-子",
        "uuid": "3448a0dd-db8f-4ed5-a882-48096ab5367b",
        "backup_size": 0,
        "backup_count": 0,
        "last_backup_time": 0,
        "belong_cluster": "b62e7f1b-28c2-4fa7-9226-63231bbd84ea",
        "belong_cluster_name": "cluster_name_212",
        "disater_tolerant_plan": "de77ec92-ab63-4a7e-97dc-6c4e9ec667cf",
        "disaster_tolerant_plan_name": "plan1",
        "procedure": 0,
        "ctime": 1584590276,
        "dtp_type": "hci"
      }
    ]
  }
}
```

## /v1/disaster_tolerant_plan/slavecluster/backup/list
容灾对象备站点数据列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
slave_cluster|string|否|-|容灾计划备站点集群uuid
plan_uuid|string|否|-|容灾计划uuid
vm_uuid|[]string|否|-|容灾虚拟机在主站点的uuid数组
filter_types|[]string|否|-|容灾类型数组
fuzzy|string|否|-|过滤关键字
number|int32|否|-|页码
page|int32|否|-|页长

### 返回参数

名称|参数类型|描述
---|---|---
total_count|int32|总数
vms|[]DisasterTolerantSlaveClusterVmInfo|容灾备站点集群虚拟机信息数组

### DisasterTolerantSlaveClusterVmInfo 对象
名称|参数类型|描述
---|---|---
name|string|容灾对象名称
uuid|string|容灾对象uuid
backup_size|int64|容灾对象备份大小
backup_count|int32|容灾对象备份数量
sync_data_delta_size|int64|数据同步增量大小
master_cluster|string|容灾计划主站点集群uuid
master_cluster_name|string|容灾计划主站点集群名称
slave_cluster|string|容灾计划备站点集群uuid
slave_cluster_name|string|容灾计划备站点集群名称
disater_tolerant_plan|string|容灾计划uuid
disaster_tolerant_plan_name|string|容灾计划名称
running_cluster|string|容灾对象运行集群uuid
running_cluster_name|string|容灾对象运行集群名称
last_backup_time|int64|最后一次备份时间
next_execute_plan_time|int64|下一次备份执行时间
recovery_priority|string|恢复优先级
procedure|int32|容灾对象状态
ctime|int64|容灾对象创建时间
dtp_type|string|容灾类型

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/disaster_tolerant_plan/slavecluster/backup/list
```
Body:
```
{
	"slave_cluster": "",
	"plan_uuid": "",
	"page": 0,
	"number": 10,
	"filter_types": [
		"hci"
	],
	"fuzzy": "",
	"cluster_uuid": "5ea15037-7a21-4233-8c69-b8112156c474"
}
```

#### 返回示例
```
{
  "message": "",
  "message_cn": "",
  "scode": 0,
  "desc": "",
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
    "total_count": 2,
    "vms": [
      {
        "name": "vm2",
        "uuid": "b1603bf2-9777-40a5-8208-62cf5a2d4be7",
        "backup_size": 0,
        "backup_count": 0,
        "sync_data_delta_size": 0,
        "master_cluster": "5ea15037-7a21-4233-8c69-b8112156c474",
        "master_cluster_name": "cluster_name_213",
        "slave_cluster": "b62e7f1b-28c2-4fa7-9226-63231bbd84ea",
        "slave_cluster_name": "cluster_name_212",
        "disater_tolerant_plan": "28215d7b-6e3e-487d-a7bc-11804b876dda",
        "disaster_tolerant_plan_name": "计划12",
        "running_cluster": "5ea15037-7a21-4233-8c69-b8112156c474",
        "running_cluster_name": "cluster_name_213",
        "last_backup_time": 0,
        "next_execute_plan_time": 1584600213,
        "recovery_priority": "middle",
        "procedure": 0,
        "ctime": 1584598413,
        "dtp_type": "hci"
      },
      {
        "name": "test-子",
        "uuid": "27aba45e-c713-45a9-bc14-c879990b5898",
        "backup_size": 1872396288,
        "backup_count": 1,
        "sync_data_delta_size": 0,
        "master_cluster": "b62e7f1b-28c2-4fa7-9226-63231bbd84ea",
        "master_cluster_name": "cluster_name_212",
        "slave_cluster": "5ea15037-7a21-4233-8c69-b8112156c474",
        "slave_cluster_name": "cluster_name_213",
        "disater_tolerant_plan": "de77ec92-ab63-4a7e-97dc-6c4e9ec667cf",
        "disaster_tolerant_plan_name": "plan1",
        "running_cluster": "b62e7f1b-28c2-4fa7-9226-63231bbd84ea",
        "running_cluster_name": "cluster_name_212",
        "last_backup_time": 1584599363,
        "next_execute_plan_time": 1584599962,
        "recovery_priority": "middle",
        "procedure": 0,
        "ctime": 1584590276,
        "dtp_type": "hci"
      }
    ]
  }
}
```

## /v1/disaster_tolerant_plan/mastercluster/backup/recovery
容灾主站点备份数据恢复
### 请求类型
POST

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
recover_vms|[]DisasterTolerantClusterBackupSingleRecoveryRequest|是|-|容灾恢复对象

### DisasterTolerantClusterBackupSingleRecoveryRequest 对象
名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
plan_uuid|string|是|-|容灾对象所属容灾计划uuid
vm_uuid|string|是|-|容灾对象uuid
vm_name|string|否|-|容灾对象名称
vm_backup_uuid|string|是|-|要恢复的备份uuid
startup_hosts|[]string|否|-|启动主机uuid数组

### 返回参数

名称|参数类型|描述
---|---|---
success|int|恢复成功的数量
fail|int|恢复失败的数量
results|[]Output|容灾对象恢复结果数组

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/disaster_tolerant_plan/mastercluster/backup/recovery
```
Body:
```
{
	"recover_vms": [
		{
			"plan_uuid": "28215d7b-6e3e-487d-a7bc-11804b876dda",
			"vm_uuid": "d3514d6f-4b92-488e-8f33-6ae1ad7ce5ba",
			"vm_backup_uuid": "74130b9b-7547-4a1f-82f0-2df7a7192d49",
			"startup_hosts": []
		}
	],
	"cluster_uuid": "5ea15037-7a21-4233-8c69-b8112156c474"
}
```

#### 返回示例
```
{
  "message": "",
  "message_cn": "",
  "scode": 0,
  "desc": "",
  "stack": null,
  "data": {
    "success": 1,
    "fail": 0,
    "results": [
        {
            "message": "",
            "message_cn": "",
            "scode": 0,
            "desc": "",
            "stack": null,
            "data": {
                "status": null,
                "vm_uuid": "d3514d6f-4b92-488e-8f33-6ae1ad7ce5ba",
                "vm_name": ""
            }
        }
    ]
  }
}
```

## /v1/disaster_tolerant_plan/slavecluster/backup/recovery
容灾备站点备份数据恢复
### 请求类型
POST

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
recover_vms|[]DisasterTolerantClusterBackupSingleRecoveryRequest|是|-|容灾恢复对象

### DisasterTolerantClusterBackupSingleRecoveryRequest 对象
名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
plan_uuid|string|是|-|容灾对象所属容灾计划uuid
vm_uuid|string|是|-|容灾对象uuid
vm_name|string|否|-|容灾对象名称
vm_backup_uuid|string|是|-|要恢复的备份uuid（容灾类型为hci的情况下必填）
startup_hosts|[]string|否|-|启动主机uuid数组

### 返回参数

名称|参数类型|描述
---|---|---
success|int|恢复成功的数量
fail|int|恢复失败的数量
results|[]Output|容灾对象恢复结果数组

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/disaster_tolerant_plan/slavecluster/backup/recovery
```
Body:
```
{
	"recover_vms": [
		{
			"plan_uuid": "28215d7b-6e3e-487d-a7bc-11804b876dda",
			"vm_uuid": "d3514d6f-4b92-488e-8f33-6ae1ad7ce5ba",
			"vm_backup_uuid": "74130b9b-7547-4a1f-82f0-2df7a7192d49",
			"startup_hosts": []
		}
	],
	"cluster_uuid": "5ea15037-7a21-4233-8c69-b8112156c474"
}
```

#### 返回示例
```
{
  "message": "",
  "message_cn": "",
  "scode": 0,
  "desc": "",
  "stack": null,
  "data": {
    "success": 1,
    "fail": 0,
    "results": [
        {
            "message": "",
            "message_cn": "",
            "scode": 0,
            "desc": "",
            "stack": null,
            "data": {
                "status": null,
                "vm_uuid": "d3514d6f-4b92-488e-8f33-6ae1ad7ce5ba",
                "vm_name": ""
            }
        }
    ]
  }
}
```

## /v1/disaster_tolerant_plan/state
容灾状态数据列表
### 请求类型
POST

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
master_cluster|string|否|-|容灾计划主站点集群uuid
plan_uuid|string|否|-|容灾计划uuid
vms|[]string|否|-|容灾对象在主站点的uuid数组
page|int32|否|-|页长
number|int32|否|-|页码
filter_types|[]string|否|-|容灾类型过滤数组
fuzzy|string|否|-|过滤关键字

### 返回参数

名称|参数类型|描述
---|---|---
total_count|int32|容灾对象总数
infos|[]DisasterTolerantStateVmInfo|容灾对象信息数组

### DisasterTolerantStateVmInfo 对象
名称|参数类型|描述
---|---|---
name|string|容灾对象名称
uuid|string|容灾对象在主站点的uuid
object_group|string|容灾对象所在分组名称
object_group_path|string|容灾对象所在分组路径
state|string|容灾对象状态
ip|[]string|ip数组
rpo|int64|容灾对象所属容灾计划rpo
satisfy_rpo|bool|容灾对象是否满足rpo
master_cluster|string|容灾对象所属容灾计划主站点集群uuid
master_cluster_name|string|容灾对象所属容灾计划主站点集群名称
slave_cluster|string|容灾对象所属容灾计划备站点集群uuid
slave_cluster_name|string|容灾对象所属容灾计划备站点集群名称
disaster_tolerant_plan|string|容灾对象所属容灾计划uuid
disaster_tolerant_plan_name|string|容灾对象所属容灾计划名称
running_cluster|string|容灾对象运行站点集群uuid
running_cluster_name|string|容灾对象运行站点集群名称
plan_enable|bool|容灾对象所属容灾计划是否启用
sync_data_delta_size|int64|同步数组增量大小
local_backup_duration|int64|本地备份时间
next_execute_plan_time|int64|容灾对象所属容灾策略下一次执行时间
recovery_priority|string|恢复优先级
ctime|int64|容灾对象创建时间
dtp_type|string|容灾对象所属容灾计划类型
last_error|string|容灾对象最近一个错误信息
deleted|bool|容灾对象是否已被删除
zone|string|容灾对象所在资源池

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/disaster_tolerant_plan/state
```
Body:
```
{
	"master_cluster": "",
	"plan_uuid": "",
	"vms": [],
	"page": 0,
	"number": 10,
	"filter_types": [
		"hci"
	],
	"fuzzy": "",
	"cluster_uuid": "5ea15037-7a21-4233-8c69-b8112156c474"
}
```

#### 正常返回示例
```
{
  "message": "",
  "message_cn": "",
  "scode": 0,
  "desc": "",
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
    "total_count": 2,
    "infos": [
      {
        "name": "vm2",
        "uuid": "d3514d6f-4b92-488e-8f33-6ae1ad7ce5ba",
        "object_group": "default",
        "object_group_path": "",
        "state": "正常",
        "ip": null,
        "rpo": 3600,
        "satisfy_rpo": true,
        "master_cluster": "5ea15037-7a21-4233-8c69-b8112156c474",
        "master_cluster_name": "cluster_name_213",
        "slave_cluster": "b62e7f1b-28c2-4fa7-9226-63231bbd84ea",
        "slave_cluster_name": "cluster_name_212",
        "disaster_tolerant_plan": "28215d7b-6e3e-487d-a7bc-11804b876dda",
        "disaster_tolerant_plan_name": "计划12",
        "running_cluster": "5ea15037-7a21-4233-8c69-b8112156c474",
        "running_cluster_name": "cluster_name_213",
        "plan_enable": true,
        "sync_data_delta_size": 0,
        "local_backup_duration": 1800,
        "next_execute_plan_time": 1584602013,
        "recovery_priority": "middle",
        "ctime": 1584598413,
        "dtp_type": "hci"
      },
      {
        "name": "test-子",
        "uuid": "3448a0dd-db8f-4ed5-a882-48096ab5367b",
        "object_group": "default",
        "object_group_path": "",
        "state": "正常",
        "ip": [
          "10.30.14.196"
        ],
        "rpo": 3600,
        "satisfy_rpo": true,
        "master_cluster": "b62e7f1b-28c2-4fa7-9226-63231bbd84ea",
        "master_cluster_name": "cluster_name_212",
        "slave_cluster": "5ea15037-7a21-4233-8c69-b8112156c474",
        "slave_cluster_name": "cluster_name_213",
        "disaster_tolerant_plan": "de77ec92-ab63-4a7e-97dc-6c4e9ec667cf",
        "disaster_tolerant_plan_name": "plan1",
        "running_cluster": "b62e7f1b-28c2-4fa7-9226-63231bbd84ea",
        "running_cluster_name": "cluster_name_212",
        "plan_enable": true,
        "sync_data_delta_size": 0,
        "local_backup_duration": 600,
        "next_execute_plan_time": 1584600562,
        "recovery_priority": "middle",
        "ctime": 1584590276,
        "dtp_type": "hci",
        "last_error": "",
        "deleted": false,
        "zone": "67521b-a639-8618-3250-67923bba2cea"
      }
    ]
  }
}
```

## /v1/disaster_tolerant_plan/vm/backup/list
容灾虚拟机备份数据列表
### 请求类型
POST

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
plan_uuid|string|是|-|容灾计划uuid
vm_uuid|string|是|-|容灾对象主站点或备站点uuid
start_time|int64|否|-|开始时间时间戳
end_time|int64|否|-|结束时间时间戳
page|int32|否|-|页长
number|int32|否|-|页码

### 返回参数

名称|参数类型|描述
---|---|---
total_count|int32|备份总数
backups|[]DisasterTolerantVmBackupInfo|备份信息数组

### DisasterTolerantVmBackupInfo对象
名称|参数类型|描述
---|---|---
Name|string|备份名称
Description|string|备份描述
Ctime|int64|备份创建时间

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/disaster_tolerant_plan/vm/backup/list
```
Body:
```
{
	"plan_uuid": "28215d7b-6e3e-487d-a7bc-11804b876dda",
	"vm_uuid": "d3514d6f-4b92-488e-8f33-6ae1ad7ce5ba",
	"start_time": 0,
	"end_time": 0,
	"page": 10,
	"number": 0,
	"cluster_uuid": "5ea15037-7a21-4233-8c69-b8112156c474"
}
```

#### 返回示例
```
{
  "message": "",
  "message_cn": "",
  "scode": 0,
  "desc": "",
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
    "total_count": 2,
    "backups": [
        {
            "Name": "DT-1629978635",
            "Description": "该快照为异地容灾备份于2021-08-26 19:50:35自动创建",
            "Ctime": 1629978636
        },
        {
            "Name": "DT-1629976835",
            "Description": "该快照为异地容灾备份于2021-08-26 19:20:35自动创建",
            "Ctime": 1629976836
        }
    ]
  }
}
```

## /v1/disaster_tolerant_plan/link/add
容灾链路添加
### 请求类型
POST

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
link_transport_limit|int64|是|-|链路传输带宽限制
link_side_relation|[]string|是|-|容灾链路两端站点名称数组
sides|[]DisasterToLerantSideManagement|是|-|容灾链路两端站点集群信息

### DisasterToLerantSideManagement对象
名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
ClusterUUID|string|是|-|集群uuid
ClusterName|string|是|-|集群名称

### 返回参数

名称|参数类型|描述
---|---|---
sides|[]DisasterTolerantLinkManagement|容灾链路信息数组

### DisasterTolerantLinkManagement对象
名称|参数类型|描述
---|---|---
uuid|string|容灾链路uuid
link_transport_limit|int64|链路传输带宽限制
link_side_relation|[]string|容灾链路两端站点名称数组
sides|[]DisasterToLerantSideManagement|容灾链路两端站点集群信息
status|bool|容灾链路连接状态
ctime|int64|容灾链路创建时间
mtime|int64|容灾链路修改时间

### DisasterToLerantSideManagement对象
名称|参数类型|描述
---|---|---
ClusterUUID|string|集群uuid
ClusterName|string|集群名称

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/disaster_tolerant_plan/link/add
```
Body:
```
{
	"link_transport_limit": -1,
	"link_side_relation": [
		"cluster_name_213",
		"cluster_name_212"
	],
	"sides": [
		{
			"ClusterUUID": "5ea15037-7a21-4233-8c69-b8112156c474",
			"ClusterName": "cluster_name_213"
		},
		{
			"ClusterUUID": "b62e7f1b-28c2-4fa7-9226-63231bbd84ea",
			"ClusterName": "cluster_name_212"
		}
	],
	"cluster_uuid": "5ea15037-7a21-4233-8c69-b8112156c474"
}
```

#### 返回示例
```
{
  "message": "",
  "message_cn": "",
  "scode": 0,
  "desc": "",
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
    "sides": [
      {
        "uuid": "753ae07c-38e6-42b2-aa6b-8b57e47f3702",
        "link_transport_limit": -1,
        "link_side_relation": [
          "cluster_name_213",
          "cluster_name_212"
        ],
        "sides": [
          {
            "ClusterUUID": "5ea15037-7a21-4233-8c69-b8112156c474",
            "ClusterName": "cluster_name_213"
          },
          {
            "ClusterUUID": "b62e7f1b-28c2-4fa7-9226-63231bbd84ea",
            "ClusterName": "cluster_name_212"
          }
        ],
        "status": true,
        "ctime": 1584600413,
        "mtime": 1584600413
      }
    ]
  }
}
```

## /v1/disaster_tolerant_plan/link/delete
容灾链路删除
### 请求类型
POST

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
uuid|string|是|-|容灾链路uuid

### 返回参数

名称|参数类型|描述
---|---|---
sides|[]DisasterTolerantLinkManagement|容灾链路信息数组

### DisasterTolerantLinkManagement对象
名称|参数类型|描述
---|---|---
uuid|string|容灾链路uuid
link_transport_limit|int64|链路传输带宽限制
link_side_relation|[]string|容灾链路两端站点名称数组
sides|[]DisasterToLerantSideManagement|容灾链路两端站点集群信息
status|bool|容灾链路连接状态
ctime|int64|容灾链路创建时间
mtime|int64|容灾链路修改时间

### DisasterToLerantSideManagement对象
名称|参数类型|描述
---|---|---
ClusterUUID|string|集群uuid
ClusterName|string|集群名称

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/disaster_tolerant_plan/link/delete
```
Body:
```
{
	"uuid": "753ae07c-38e6-42b2-aa6b-8b57e47f3702",
	"cluster_uuid": "5ea15037-7a21-4233-8c69-b8112156c474"
}
```

#### 返回示例
```
{
  "message": "",
  "message_cn": "",
  "scode": 0,
  "desc": "",
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
    "sides": null
  }
}
```

## /v1/disaster_tolerant_plan/link/list
容灾链路列表
### 请求类型
GET

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---

### 返回参数

名称|参数类型|描述
---|---|---
sides|[]DisasterTolerantLinkManagement|容灾链路信息数组

### DisasterTolerantLinkManagement对象
名称|参数类型|描述
---|---|---
uuid|string|容灾链路uuid
link_transport_limit|int64|链路传输带宽限制
link_side_relation|[]string|容灾链路两端站点名称数组
sides|[]DisasterToLerantSideManagement|容灾链路两端站点集群信息
status|bool|容灾链路连接状态
ctime|int64|容灾链路创建时间
mtime|int64|容灾链路修改时间

### DisasterToLerantSideManagement对象
名称|参数类型|描述
---|---|---
ClusterUUID|string|集群uuid
ClusterName|string|集群名称

### 示例

#### 请求示例
```
http://10.30.14.212:8080/v1/disaster_tolerant_plan/link/list?cluster_uuid=5ea15037-7a21-4233-8c69-b8112156c474
```

#### 返回示例
```
{
  "message": "",
  "message_cn": "",
  "scode": 0,
  "desc": "",
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
    "sides": [
      {
        "uuid": "753ae07c-38e6-42b2-aa6b-8b57e47f3702",
        "link_transport_limit": -1,
        "link_side_relation": [
          "cluster_name_213",
          "cluster_name_212"
        ],
        "sides": [
          {
            "ClusterUUID": "5ea15037-7a21-4233-8c69-b8112156c474",
            "ClusterName": "cluster_name_213"
          },
          {
            "ClusterUUID": "b62e7f1b-28c2-4fa7-9226-63231bbd84ea",
            "ClusterName": "cluster_name_212"
          }
        ],
        "status": true,
        "ctime": 1584600413,
        "mtime": 1584600413
      }
    ]
  }
}
```

## /v1/disaster_tolerant_plan/link/checking
容灾链路检测
### 请求类型
POST

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
uuid|string|是|-|容灾链路uuid
master_cluster|string|是|-|容灾链路主站点集群uuid
hosts|[]string|是|-|宿主机ip数组

### 返回参数

名称|参数类型|描述
---|---|---
is_ok|bool|网络是否能通

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/disaster_tolerant_plan/link/checking
```
Body:
```
{
	"uuid": "753ae07c-38e6-42b2-aa6b-8b57e47f3702",
	"master_cluster": "5ea15037-7a21-4233-8c69-b8112156c474",
	"hosts": [
		"10.30.11.210"
	],
	"cluster_uuid": "5ea15037-7a21-4233-8c69-b8112156c474"
}
```

#### 正常返回示例
```
{
  "message": "",
  "message_cn": "",
  "scode": 0,
  "desc": "",
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
    "is_ok": true
  }
}
```

## /v1/disaster_tolerant_plan/link/edit
容灾链路编辑
### 请求类型
POST

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
uuid|string|是|-|容灾链路uuid
link_transport_limit|int64|是|-|链路传输带宽限制

### 返回参数

名称|参数类型|描述
---|---|---
sides|[]DisasterTolerantLinkManagement|容灾链路信息数组

### DisasterTolerantLinkManagement对象
名称|参数类型|描述
---|---|---
uuid|string|容灾链路uuid
link_transport_limit|int64|链路传输带宽限制
link_side_relation|[]string|容灾链路两端站点名称数组
sides|[]DisasterToLerantSideManagement|容灾链路两端站点集群信息
status|bool|容灾链路连接状态
ctime|int64|容灾链路创建时间
mtime|int64|容灾链路修改时间

### DisasterToLerantSideManagement对象
名称|参数类型|描述
---|---|---
ClusterUUID|string|集群uuid
ClusterName|string|集群名称

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/disaster_tolerant_plan/link/edit
```
Body:
```
{
	"uuid": "753ae07c-38e6-42b2-aa6b-8b57e47f3702",
	"link_transport_limit": -1,
	"cluster_uuid": "5ea15037-7a21-4233-8c69-b8112156c474"
}
```

#### 正常返回示例
```
{
  "message": "",
  "message_cn": "",
  "scode": 0,
  "desc": "",
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
    "sides": [
      {
        "uuid": "753ae07c-38e6-42b2-aa6b-8b57e47f3702",
        "link_transport_limit": -1,
        "link_side_relation": [
          "cluster_name_213",
          "cluster_name_212"
        ],
        "sides": [
          {
            "ClusterUUID": "5ea15037-7a21-4233-8c69-b8112156c474",
            "ClusterName": "cluster_name_213"
          },
          {
            "ClusterUUID": "b62e7f1b-28c2-4fa7-9226-63231bbd84ea",
            "ClusterName": "cluster_name_212"
          }
        ],
        "status": true,
        "ctime": 1584600413,
        "mtime": 1584601410
      }
    ]
  }
}
```

## /v1/disaster_tolerant_plan/backup/execute
容灾虚拟机执行备份
### 请求类型
POST

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
exec_vms|[]DisasterTolerantVmBackupSingleExecuteRequest|是|-|执行备份的容灾对象参数数组

### DisasterTolerantVmBackupSingleExecuteRequest对象
名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
plan_uuid|string|是|-|容灾对象所属容灾计划uuid
vm_uuid|string|是|-|容灾对象在主站点的uuid
vm_name|string|否|-|容灾对象名称
source_cluster|string|是|-|容灾对象的源站点集群uuid
auto_shutoff|bool|是|-|执行备份前是否将容灾虚拟机关机
destination_activate|bool|是|-|是否将运行站点切换至目标站点
startup_hosts|[]string|否|-|启动主机uuid数组

### 返回参数

名称|参数类型|描述
---|---|---
success|int|备份成功的数量
fail|int|备份失败的数量
results|[]Output|容灾对象备份结果数组

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/disaster_tolerant_plan/backup/execute
```
Body:
```
{
	"exec_vms": [
		{
			"plan_uuid": "28215d7b-6e3e-487d-a7bc-11804b876dda",
			"vm_uuid": "b1603bf2-9777-40a5-8208-62cf5a2d4be7",
			"source_cluster": "5ea15037-7a21-4233-8c69-b8112156c474",
			"auto_shutoff": true,
			"destination_activate": true
		}
	],
	"cluster_uuid": "5ea15037-7a21-4233-8c69-b8112156c474"
}
```

#### 返回示例
```
{
  "message": "success",
  "message_cn": "成功",
  "scode": 0,
  "desc": "",
  "stack": null,
  "data": {
    "success": 1,
    "fail": 0,
    "results": [
      {
        "scode": 0,
        "desc": "",
        "message": "",
        "message_cn": "",
        "messageCn": "",
        "stack": [],
        "data": {
          "status": null,
          "vm_uuid": "b1603bf2-9777-40a5-8208-62cf5a2d4be7",
          "vm_name": ""
        }
      }
    ]
  }
}
```

## /v1/disaster_tolerant_plan/vm/confirm
容灾虚拟机确认迁移
### 请求类型
POST

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
exec_vms|[]DisasterTolerantVmBackupSingleExecuteRequest|是|-|执行备份的容灾对象参数数组

### DisasterTolerantVmBackupSingleExecuteRequest对象
名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
plan_uuid|string|是|-|容灾对象所属容灾计划uuid
vm_uuid|string|是|-|容灾对象的uuid
vm_name|string|否|-|容灾对象名称

### 返回参数

名称|参数类型|描述
---|---|---
success|int|确认成功的数量
fail|int|确认失败的数量
results|[]Output|容灾对象迁移确认结果数组

### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/disaster_tolerant_plan/vm/confirm
```
Body:
```
{
	"exec_vms": [
		{
			"plan_uuid": "28215d7b-6e3e-487d-a7bc-11804b876dda",
			"vm_uuid": "b1603bf2-9777-40a5-8208-62cf5a2d4be7"
		}
	],
	"cluster_uuid": "5ea15037-7a21-4233-8c69-b8112156c474"
}
```

#### 返回示例
```
{
  "message": "success",
  "message_cn": "成功",
  "scode": 0,
  "desc": "",
  "stack": null,
  "data": {
    "success": 1,
    "fail": 0,
    "results": [
      {
        "scode": 0,
        "desc": "",
        "message": "",
        "message_cn": "",
        "messageCn": "",
        "stack": [],
        "data": {
          "status": null,
          "vm_uuid": "b1603bf2-9777-40a5-8208-62cf5a2d4be7",
          "vm_name": ""
        }
      }
    ]
  }
}
```


