[back to api overview](../api_overview.md#api)


## /v1/tencent/disk/create
#### 功能：云硬盘创建
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
DiskType |string|是|- |磁盘介质类型 CLOUD_BASIC表示普通云硬盘，CLOUD_PREMIUM表示高性能云硬盘，CLOUD_SSD表示SSD云硬盘
DiskChargeType |string|是|- |云硬盘计费类型 PREPAID：预付费，即包年包月；POSTPAID_BY_HOUR：按小时后付费；CDCPAID：独享集群付费
Placement |struct|是|- |实例所在的位置
DiskName | string|否|- |云盘显示名称。
DiskCount |uint64|否|1 |创建云硬盘数量
DiskChargePrepaid |struct|否|- |预付费模式
DiskSize |uint64|是|- |云硬盘大小，单位为GB
SnapshotId |string|否|- |快照ID
ClientToken |string|否|- |用于保证请求幂等性的字符串。
Encrypt |string|否|- | 传入该参数用于创建加密云盘
Tags |struct array|否|- |云盘绑定的标签。
Shareable |bool|否|- |可选参数，默认为False。传入True时，云盘将创建为共享型云盘。
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region | string|是|- |  地域


### 返回参数
名称|参数类型|描述


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/disk/create
```
Body:
```
{
    "Region": "ap-guangzhou",
    "Placement": {
        "Zone": "ap-guangzhou-3"
    },
    "DiskSize": 20,
    "DiskName": "123",
    "DiskCount": 1,
    "DiskType": "CLOUD_PREMIUM",
    "TenantUuid": "system",
    "ClusterUuid": "72db4b34-1473-418f-ade4-de00b956f16b"
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


## /v1/tencent/disk/distributed/inspect
#### 功能：各地域创建的云硬盘
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
DiskIds |string array|---|--- |按照一个或者多个云硬盘ID查询。
Filters |struct array|否|0 |过滤条件
Offset |uint64|否|0 |偏移量
Limit |uint64|否|0 |返回数量，默认为20，最大值为100
Order |string|否|- |输出云盘列表的排列顺序
OrderField |string|否|- |云盘列表排序的依据字段
ReturnBindAutoSnapshotPolicy |bool|否|- |盘详情中是否需要返回云盘绑定的定期快照策略ID
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region | string|否|- |  地域

### 返回参数
名称|参数类型|描述
Count|int|地域数量
Region|string|地域
RegionName|string|地域名字
RegionState|string|地域状态


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/disk/distributed/inspect
```
Body:
```
{
    "TenantUuid": "system",
    "ClusterUuid": "72db4b34-1473-418f-ade4-de00b956f16b"
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
    "List": [
      {
        "Count": 0,
        "Region": "ap-bangkok",
        "RegionName": "亚太地区(曼谷)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-beijing",
        "RegionName": "华北地区(北京)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-chengdu",
        "RegionName": "西南地区(成都)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-chongqing",
        "RegionName": "西南地区(重庆)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 2,
        "Region": "ap-guangzhou",
        "RegionName": "华南地区(广州)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-hongkong",
        "RegionName": "港澳台地区(中国香港)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-mumbai",
        "RegionName": "亚太地区(孟买)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-nanjing",
        "RegionName": "华东地区(南京)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-seoul",
        "RegionName": "亚太地区(首尔)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-shanghai",
        "RegionName": "华东地区(上海)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-shanghai-fsi",
        "RegionName": "华东地区(上海金融)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-shenzhen-fsi",
        "RegionName": "华南地区(深圳金融)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-singapore",
        "RegionName": "东南亚地区(新加坡)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-tokyo",
        "RegionName": "亚太地区(东京)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "eu-frankfurt",
        "RegionName": "欧洲地区(法兰克福)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "eu-moscow",
        "RegionName": "欧洲地区(莫斯科)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "na-ashburn",
        "RegionName": "美国东部(弗吉尼亚)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "na-siliconvalley",
        "RegionName": "美国西部(硅谷)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "na-toronto",
        "RegionName": "北美地区(多伦多)",
        "RegionState": "AVAILABLE"
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码



## /v1/tencent/disk/list
#### 功能：磁盘列表
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
 DiskIds |string array|否|- |按照一个或者多个云硬盘ID查询。
 Filters |struct array|否|0 |过滤条件
 Offset |uint64|否|0 |偏移量
 Limit |uint64|否|0 |返回数量，默认为20，最大值为100
 Order |string|否|- |输出云盘列表的排列顺序
 OrderField |string|否|- |云盘列表排序的依据字段
 ReturnBindAutoSnapshotPolicy |bool|否|- |盘详情中是否需要返回云盘绑定的定期快照策略ID
 TenantUuid | string|是|- |租户uuid
 ClusterUuid | string|是|- |集群uuid
 Region | string|是|0 |  地域
 State |string|否|- |状态
 AutoSnapshotPolicyId |string|否|- |根据策略id进行过滤
 Fuzzy |string|否|- |过滤字符串
 Zone |string|否|- |可用区
 PageNum | int|否|0 |翻页偏移量
 PageSize | int|否|0 |每页的限制数量

### 返回参数
名称|参数类型|描述
TotalCount|uint64|总共数量
DiskId|string|云硬盘ID
DiskUsage|string|云硬盘类型
DiskChargeType|string|付费模式
Portable|bool|是否为弹性云盘，false表示非弹性云盘，true表示弹性云盘。
Placement|struct|云硬盘所在的位置
SnapshotAbility|bool|云盘是否具备创建快照的能力
DiskName|string|云硬盘名称
DiskSize|uint64|云硬盘大小
DiskState|string|云盘状态
DiskType|string|云盘介质类型
Attached|bool|云盘是否挂载到云主机上
InstanceId|string|云硬盘挂载的云主机ID
CreateTime|string|云硬盘的创建时间
DeadlineTime|string|云硬盘的到期时间
Rollbacking|bool|云盘是否处于快照回滚状态
RollbackPercent|uint64|云盘快照回滚的进度
Encrypt|bool|云盘是否为加密盘
AutoRenewFlagError|bool|云盘已挂载到子机，且子机与云盘都是包年包月
RenewFlag|string|自动续费标识
DeadlineError|bool|在云盘已挂载到实例，且实例与云盘都是包年包月的条件下，此字段才有意义
IsReturnable|bool|判断预付费的云盘是否支持主动退还
ReturnFailCode|int64|付费云盘在不支持主动退还的情况下，该参数表明不支持主动退还的具体原因
AutoSnapshotPolicyIds|array|云盘关联的定期快照ID
Tags|array|与云盘绑定的标签
DeleteWithInstance|bool|云盘是否与挂载的实例一起销毁
DifferDaysOfDeadline|int64|当前时间距离盘到期的天数
Migrating|bool|云盘是否处于类型变更中
MigratePercent|uint64|云盘类型变更的迁移进度
Shareable|bool|云盘是否为共享型云盘
InstanceIdList|string array|对于非共享型云盘，该参数为空数组。对于共享型云盘，则表示该云盘当前被挂载到的CVM实例InstanceId
SnapshotCount|int64|云盘拥有的快照总数
SnapshotSize|int64|云盘拥有的快照总容量
BackupDisk|bool|云盘因欠费销毁或者期销毁时， 是否使用快照备份数据的标识。True， 销毁时创建快照进行数据备份。False 表示直接销毁，不进行数据备份。
IsModify | bool | 是否修改
IsExpand | bool | 是否扩展
IsDetach | bool | 是否分离
IsDelete | bool | 是否删除

### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/disk/list
```
Body:
```
{
    "Region": "ap-guangzhou",
    "PageSize": 10,
    "Fuzzy": "",
    "PageNum": 0,
    "TenantUuid": "system",
    "ClusterUuid": "72db4b34-1473-418f-ade4-de00b956f16b"
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
    "TotalCount": 1,
    "List": [
      {
        "DiskId": "disk-giys4n0i",
        "DiskUsage": "DATA_DISK",
        "DiskChargeType": "POSTPAID_BY_HOUR",
        "Portable": true,
        "Placement": {
          "Zone": "ap-guangzhou-3",
          "ProjectId": 1196468,
          "CdcId": "",
          "CageId": "",
          "CdcName": ""
        },
        "SnapshotAbility": true,
        "DiskName": "123",
        "DiskSize": 20,
        "DiskState": "UNATTACHED",
        "DiskType": "CLOUD_PREMIUM",
        "Attached": false,
        "InstanceId": "",
        "CreateTime": "2021-08-27 17:40:15",
        "DeadlineTime": "",
        "Rollbacking": false,
        "RollbackPercent": 0,
        "Encrypt": false,
        "AutoRenewFlagError": false,
        "RenewFlag": "",
        "DeadlineError": false,
        "IsReturnable": false,
        "ReturnFailCode": 10,
        "DeleteWithInstance": false,
        "Migrating": false,
        "MigratePercent": 0,
        "Shareable": false,
        "SnapshotCount": 0,
        "SnapshotSize": 0,
        "BackupDisk": false
      }
    ],
    "Properties": [
      {
        "IsModify": false,
        "IsExpand": true,
        "IsDetach": false,
        "IsDelete": true
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码



## /v1/tencent/disk/inspect 
#### 功能：云硬盘详情
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
DiskIds |string array|是|- |按照一个或者多个云硬盘ID查询。
Filters |struct array|否|- |过滤条件
Offset |uint64|否|0 |偏移量
Limit |uint64|否|20 |返回数量，默认为20，最大值为100
Order |string|否|- |输出云盘列表的排列顺序
OrderField |string|否|- |云盘列表排序的依据字段
ReturnBindAutoSnapshotPolicy |bool|否|- |盘详情中是否需要返回云盘绑定的定期快照策略ID
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region | string|是|- |  地域


### 返回参数
名称|参数类型|描述 
DiskId|string|云硬盘ID
DiskUsage|string|云硬盘类型
DiskChargeType|string|付费模式
Portable|bool|是否为弹性云盘，false表示非弹性云盘，true表示弹性云盘。
Placement|struct|云硬盘所在的位置
SnapshotAbility|bool|云盘是否具备创建快照的能力
DiskName|string|云硬盘名称
DiskSize|uint64|云硬盘大小
DiskState|string|云盘状态
DiskType|string|云盘介质类型
Attached|bool|云盘是否挂载到云主机上
InstanceId|string|云硬盘挂载的云主机ID
CreateTime|string|云硬盘的创建时间
DeadlineTime|string|云硬盘的到期时间
Rollbacking|bool|云盘是否处于快照回滚状态
RollbackPercent|uint64|云盘快照回滚的进度
Encrypt|bool|云盘是否为加密盘
AutoRenewFlagError|bool|云盘已挂载到子机，且子机与云盘都是包年包月
RenewFlag|string|自动续费标识
DeadlineError|bool|在云盘已挂载到实例，且实例与云盘都是包年包月的条件下，此字段才有意义
IsReturnable|bool|判断预付费的云盘是否支持主动退还
ReturnFailCode|int64|付费云盘在不支持主动退还的情况下，该参数表明不支持主动退还的具体原因
AutoSnapshotPolicyIds|string array|云盘关联的定期快照ID
Tags|struct array|与云盘绑定的标签
DeleteWithInstance|bool|云盘是否与挂载的实例一起销毁
DifferDaysOfDeadline|int64|当前时间距离盘到期的天数
Migrating|bool|云盘是否处于类型变更中
MigratePercent|uint64|云盘类型变更的迁移进度
Shareable|bool|云盘是否为共享型云盘
InstanceIdList|string array|对于非共享型云盘，该参数为空数组。对于共享型云盘，则表示该云盘当前被挂载到的CVM实例InstanceId
SnapshotCount|int64|云盘拥有的快照总数
SnapshotSize|int64|云盘拥有的快照总容量
BackupDisk|bool|云盘因欠费销毁或者期销毁时， 是否使用快照备份数据的标识。True， 销毁时创建快照进行数据备份。False 表示直接销毁，不进行数据备份。


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/disk/inspect
```
Body:
```
{
    "Region": "ap-guangzhou",
    "DiskId": "disk-giys4n0i",
    "TenantUuid": "system",
    "ClusterUuid": "72db4b34-1473-418f-ade4-de00b956f16b"
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
    "DiskId": "disk-giys4n0i",
    "DiskUsage": "DATA_DISK",
    "DiskChargeType": "POSTPAID_BY_HOUR",
    "Portable": true,
    "Placement": {
      "Zone": "ap-guangzhou-3",
      "ProjectId": 1196468,
      "CdcId": "",
      "CageId": "",
      "CdcName": ""
    },
    "SnapshotAbility": true,
    "DiskName": "123",
    "DiskSize": 20,
    "DiskState": "UNATTACHED",
    "DiskType": "CLOUD_PREMIUM",
    "Attached": false,
    "InstanceId": "",
    "CreateTime": "2021-08-27 17:40:15",
    "DeadlineTime": "",
    "Rollbacking": false,
    "RollbackPercent": 0,
    "Encrypt": false,
    "AutoRenewFlagError": false,
    "RenewFlag": "",
    "DeadlineError": false,
    "IsReturnable": false,
    "ReturnFailCode": 10,
    "DeleteWithInstance": false,
    "Migrating": false,
    "MigratePercent": 0,
    "Shareable": false,
    "SnapshotCount": 0,
    "SnapshotSize": 0,
    "BackupDisk": false
  }
}
```

#### 异常返回示例

### 状态码



## /v1/tencent/disk/update
#### 功能：更新磁盘
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
DiskIds |string array|是|- |按照一个或者多个云硬盘ID查询。
ProjectId |uint64 |否|-|新的云硬盘项目ID
DiskName |string|否|- |新的云硬盘名称
Portable |bool|否|- |是否为弹性云盘，FALSE表示非弹性云盘，TRUE表示弹性云盘。仅支持非弹性云盘修改为弹性云盘。
DeleteWithInstance |bool|否|- |成功挂载到云主机后该云硬盘是否随云主机销毁，TRUE表示随云主机销毁，FALSE表示不随云主机销毁。仅支持按量计费云硬盘数据盘。
DiskType |string|否|- |变更云盘类型
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region | string|是|0 |  地域

### 返回参数
名称|参数类型|描述 
无


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/disk/update
```
Body:
```
{
    "Region": "ap-guangzhou",
    "DiskId": "disk-giys4n0i",
    "DeleteWithInstance": false,
    "DiskName": "1234",
    "TenantUuid": "system",
    "ClusterUuid": "72db4b34-1473-418f-ade4-de00b956f16b"
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


## /v1/tencent/disk/resize
#### 功能：修改云硬盘size
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
DiskIds |string array|是|- |按照一个或者多个云硬盘ID查询。
DiskSize | uint64 |是|- |云硬盘扩容后的大小
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region | string|是|- |  地域

### 返回参数
名称|参数类型|描述 
无

### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/disk/resize
```
Body:
```
{
    "Region": "ap-guangzhou",
    "DiskId": "disk-giys4n0i",
    "DiskSize": 80,
    "TenantUuid": "system",
    "ClusterUuid": "72db4b34-1473-418f-ade4-de00b956f16b"
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


## /v1/tencent/disk/logs/list
#### 功能：日志列表
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
Filters |struct array|---|--- |过滤条件
BeginTime |string|---|--- |要查询的操作日志的起始时间
EndTime |string|---|--- |要查询的操作日志的截止时间
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region | string|是|- |  地域
DiskId |string|是|- |磁盘ID
Fuzzy |string|---|--- |---
PageNum | int|否|0 |翻页偏移量
PageSize | int|否|0 |每页的限制数量

### 返回参数
名称|参数类型|描述 
TotalCount|int|总数
Operator|string|操作者的UIN
Operation|string|操作类型
DiskId|string|操作的云盘ID
OperationState|string|操作的状态
StartTime|string|开始时间
EndTime|string|结束时间


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/disk/logs/list
```
Body:
```
{
    "PageNum": 0,
    "PageSize": 10,
    "Region": "ap-guangzhou",
    "DiskId": "disk-giys4n0i",
    "BeginTime": "2021-08-27 00:00:00",
    "EndTime": "2021-08-27 23:59:59",
    "TenantUuid": "system",
    "ClusterUuid": "72db4b34-1473-418f-ade4-de00b956f16b"
}
```
#### 正常返回示例
```
{
  "Response": {
    "RequestId": "xx",
    "DiskOperationLogSet": [
      {
        "OperationState": "xx",
        "StartTime": "xx",
        "Operator": "xx",
        "Operation": "xx",
        "EndTime": "xx",
        "DiskId": "xx"
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/tencent/disk/delete
#### 功能：磁盘删除
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
DiskIds |string struct|是|- |需退还的云盘ID列表
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region | string|是|- |  地域

### 返回参数
名称|参数类型|描述 
无


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/disk/delete
```
Body:
```
{
    "Region": "ap-guangzhou",
    "DiskIds": [
        "disk-giys4n0i"
    ],
    "TenantUuid": "system",
    "ClusterUuid": "72db4b34-1473-418f-ade4-de00b956f16b"
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


## /v1/tencent/disk/attach
#### 功能：挂载磁盘
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
DiskIds |string array|是|- |将要被挂载的弹性云盘ID
InstanceId |string|是|- |云服务器实例ID
DeleteWithInstance |bool|否|- |可选参数
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region | string|是|- |  地域

### 返回参数
名称|参数类型|描述 
无


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/disk/attach
```
Body:
```
{
    "Region": "ap-guangzhou",
    "InstanceId": "ins-gkfro58u",
    "DiskIds": [
        "disk-giys4n0i"
    ],
    "TenantUuid": "system",
    "ClusterUuid": "72db4b34-1473-418f-ade4-de00b956f16b"
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

## /v1/tencent/disk/detach
#### 功能：卸载磁盘
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
DiskIds |string array|是|- |将要解挂的云硬盘ID
InstanceId |string|否|- |对于非共享型云盘，会忽略该参数
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region | string|否|0 |  地域

### 返回参数
名称|参数类型|描述 
无


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/disk/detach
```
Body:
```
{
    "Region": "ap-guangzhou",
    "InstanceId": "ins-gkfro58u",
    "DiskIds": [
        "disk-giys4n0i"
    ],
    "TenantUuid": "system",
    "ClusterUuid": "72db4b34-1473-418f-ade4-de00b956f16b"
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