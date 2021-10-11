[back to api overview](../api_overview.md#api)

## /v1/tencent/snapshot/create
#### 功能：创建快照
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
DiskIds |string array|是|- |需要创建快照的云硬盘ID
SnapshotName |string|是|- |快照名称
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region | string|是|- | 地域

### 返回参数
名称|参数类型|描述 
无


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/snapshot/create
```
Body:
```
{
    "Region": "ap-guangzhou",
    "DiskId": "disk-plqkg6me",
    "SnapshotName": "123",
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


## /v1/tencent/snapshot/list
#### 功能：快照列表
#### 请求类型：post

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
SnapshotIds |string array| 否|---|要查询快照的ID列表
Filters |struct array|---|否 |过滤条件
Order |string|否|- |输出云盘列表的排列顺序
OrderField |string|否|- |快照列表排序的依据字段
TenantUuid |string|是|- |租户uuid
ClusterUuid |string|是|- |集群uuid
Region |string|是|- | 地域
Fuzzy |string|否|- |过滤字符串
PageNum |int|否|0 |翻页偏移量
PageSize |int|否|0 |每页的限制数量


### 返回参数
名称|参数类型|描述 
TotalCount|int|总数
SnapshotId|string|快照ID
Placement|struct|快照所在的位置
DiskUsage|string|创建此快照的云硬盘类型
DiskId|string| 创建此快照的云硬盘ID
DiskSize|uint64|创建此快照的云硬盘大小
SnapshotState|string| 快照的状态
SnapshotName|string|快照名称
Percent|uint64|快照创建进度百分比
CreateTime|string|快照的创建时间
DeadlineTime|string|快照到期时间
Encrypt|bool|是否为加密盘创建的快照
IsPermanent|bool | 是否为永久快照
CopyingToRegions |string array| 快照正在跨地域复制的目的地域
CopyFromRemote | bool | 是否为跨地域复制的快照
Images | struct array | 快照关联的镜像列表
ImageCount | uint64 | 快照关联的镜像个数
SnapshotType | string | 快照类型
ShareReference | uint64 | 快照当前被共享数

### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/snapshot/list
```
Body:
```
{
    "Region": "ap-guangzhou",
    "PageNum": 0,
    "Fuzzy": "",
    "PageSize": 10,
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
    "TotalCount": 3,
    "List": [
      {
        "SnapshotId": "snap-6ixzjp6d",
        "Placement": {
          "Zone": "ap-guangzhou-3",
          "ProjectId": 1196468,
          "CdcId": "",
          "CageId": "",
          "CdcName": ""
        },
        "DiskUsage": "DATA_DISK",
        "DiskId": "disk-nrc1gaps",
        "DiskSize": 10,
        "SnapshotState": "NORMAL",
        "SnapshotName": "auto_disk-nrc1gaps_20210731_23",
        "Percent": 100,
        "CreateTime": "2021-07-31 23:06:45",
        "DeadlineTime": "2021-08-30 23:00:00",
        "Encrypt": false,
        "IsPermanent": false,
        "CopyFromRemote": false,
        "ImageCount": 0,
        "SnapshotType": "PRIVATE_SNAPSHOT",
        "ShareReference": 0
      },
      {
        "SnapshotId": "snap-napmq1fj",
        "Placement": {
          "Zone": "ap-guangzhou-3",
          "ProjectId": 1196468,
          "CdcId": "",
          "CageId": "",
          "CdcName": ""
        },
        "DiskUsage": "DATA_DISK",
        "DiskId": "disk-eg0qthd6",
        "DiskSize": 10,
        "SnapshotState": "NORMAL",
        "SnapshotName": "auto_disk-eg0qthd6_20210807_23",
        "Percent": 100,
        "CreateTime": "2021-08-07 23:06:44",
        "DeadlineTime": "2021-09-06 23:00:00",
        "Encrypt": false,
        "IsPermanent": false,
        "CopyFromRemote": false,
        "ImageCount": 0,
        "SnapshotType": "PRIVATE_SNAPSHOT",
        "ShareReference": 0
      },
      {
        "SnapshotId": "snap-hn9huy55",
        "Placement": {
          "Zone": "ap-guangzhou-3",
          "ProjectId": 1196468,
          "CdcId": "",
          "CageId": "",
          "CdcName": ""
        },
        "DiskUsage": "SYSTEM_DISK",
        "DiskId": "disk-plqkg6me",
        "DiskSize": 50,
        "SnapshotState": "NORMAL",
        "SnapshotName": "123",
        "Percent": 100,
        "CreateTime": "2021-08-27 19:30:22",
        "DeadlineTime": "",
        "Encrypt": false,
        "IsPermanent": true,
        "CopyFromRemote": false,
        "ImageCount": 0,
        "SnapshotType": "PRIVATE_SNAPSHOT",
        "ShareReference": 0
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/tencent/snapshot/delete
#### 功能：删除快照
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
SnapshotIds | string array| 是|-|要删除的快照ID列表
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region | string|是|- |  地域

### 返回参数
名称|参数类型|描述 
无


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/snapshot/delete
```
Body:
```
{
    "Region": "ap-guangzhou",
    "SnapshotIds": [
        "snap-napmq1fj"
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


## /v1/tencent/snapshot/apply 
#### 功能：快照回滾
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
SnapshotId |string|是|- |快照ID
DiskId |string|是|- |快照原云硬盘ID
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region | string|是|- | 地域

### 返回参数
名称|参数类型|描述 
无


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/snapshot/apply
```
Body:
```
{
    "Region": "ap-guangzhou",
    "SnapshotId": "snap-hn9huy55",
    "DiskId": "disk-plqkg6me",
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


## /v1/tencent/auto_snapshot/policy/create
#### 功能：定期快照策略创建
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
Policy |struct array|是|- |定期快照的执行策略
AutoSnapshotPolicyName |string|是|- |要创建的定期快照策略名
IsActivated |bool|否|- |是否激活定期快照策略
IsPermanent |bool|否|- |通过该定期快照策略创建的快照是否永久保留
RetentionDays |int64|是|- |通过该定期快照策略创建的快照保留天数，默认保留7天
DryRun |bool|否|- |是否创建定期快照的执行策略
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region | string|是|- | 地域

### 返回参数
名称|参数类型|描述 
无


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/auto_snapshot/policy/create
```
Body:
```
{
    "Region": "ap-guangzhou",
    "Policy": [
        {
            "DayOfWeek": [
                0
            ],
            "Hour": [
                23
            ]
        }
    ],
    "AutoSnapshotPolicyName": "test",
    "IsActivated": true,
    "IsPermanent": false,
    "RetentionDays": 1,
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


## /v1/tencent/auto_snapshot/policy/delete
#### 功能：定期快照策略删除
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
AutoSnapshotPolicyIds |string array|否|- |要删除的定期快照策略ID列表
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region | string|是|- | 地域

### 返回参数
名称|参数类型|描述 
无


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/auto_snapshot/policy/delete
```
Body:
```
{
    "Region": "ap-guangzhou",
    "AutoSnapshotPolicyIds": [
        "asp-63p7jk73"
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


## /v1/tencent/auto_snapshot/policy/update
#### 功能：定期快照策略更新
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
AutoSnapshotPolicyIds |string|是|- |定期快照策略ID
Policy |struct array|否|- |定期快照的执行策略
AutoSnapshotPolicyName |string|否|- |要创建的定期快照策略名
IsActivated |bool|否|- |是否激活定期快照策略
IsPermanent |bool |否|- |通过该定期快照策略创建的快照是否永久保留
RetentionDays |uint64|否|- |通过该定期快照策略创建的快照保留天数
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region | string|是|- | 地域

### 返回参数
名称|参数类型|描述 
无


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/auto_snapshot/policy/update
```
Body:
```
{
    "Region": "ap-guangzhou",
    "AutoSnapshotPolicyId": "asp-63p7jk73",
    "Policy": [
        {
            "DayOfWeek": [
                1
            ],
            "Hour": [
                23
            ]
        }
    ],
    "AutoSnapshotPolicyName": "test",
    "IsActivated": true,
    "IsPermanent": false,
    "RetentionDays": 1,
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



## /v1/tencent/auto_snapshot/policy/list
#### 功能：定期快照策略列表
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
AutoSnapshotPolicyIds |string array| 否|-|要查询的定期快照策略ID列表
Filters |struct array|否|- |过滤条件
Order |string|否|- |输出定期快照列表的排列顺序
OrderField |string|否|- |定期快照列表排序的依据字段
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region | string|是|- |  地域
Fuzzy |string|否|- |---
PageNum | int|否|0 |翻页偏移量
PageSize | int|否|0 |每页的限制数量

### 返回参数
名称|参数类型|描述 
TotalCount | int | 总数
AutoSnapshotPolicyId | string | 定期快照策略ID
AutoSnapshotPolicyName | string | 定期快照策略名称
AutoSnapshotPolicyState | string | 定期快照策略的状态
IsActivated | bool | 定期快照策略是否激活
IsPermanent | bool | 使用该定期快照策略创建出来的快照是否永久保留
RetentionDays | string | 使用该定期快照策略创建出来的快照保留天数
CreateTime | string | 定期快照策略的创建时间
NextTriggerTime | string | 定期快照下次触发的时间
Policy | string array| 定期快照的执行策略
DiskIdSet | string array| 已绑定当前定期快照策略的云盘ID列表


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/auto_snapshot/policy/list
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
    "TotalCount": 2,
    "List": [
      {
        "AutoSnapshotPolicyId": "asp-peiq4wwp",
        "AutoSnapshotPolicyName": "test001",
        "AutoSnapshotPolicyState": "NORMAL",
        "IsActivated": true,
        "IsPermanent": false,
        "RetentionDays": 30,
        "CreateTime": "2021-07-29 16:46:56",
        "NextTriggerTime": "2021-08-28 23:00:00",
        "Policy": [
          {
            "DayOfWeek": [
              6
            ],
            "Hour": [
              23
            ]
          }
        ]
      },
      {
        "AutoSnapshotPolicyId": "asp-63p7jk73",
        "AutoSnapshotPolicyName": "test",
        "AutoSnapshotPolicyState": "NORMAL",
        "IsActivated": true,
        "IsPermanent": false,
        "RetentionDays": 1,
        "CreateTime": "2021-08-27 19:40:13",
        "NextTriggerTime": "2021-08-30 23:00:00",
        "Policy": [
          {
            "DayOfWeek": [
              1
            ],
            "Hour": [
              23
            ]
          }
        ]
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/tencent/auto_snapshot/policy/bind
#### 功能：云硬盘绑定定期快照策略
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
AutoSnapshotPolicyIds | string| 是|-|要绑定的定期快照策略ID
DiskIds |string array|是|- |要绑定的云硬盘ID列表,一次请求最多绑定80块云盘
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region | string|是|- | 地域

### 返回参数
名称|参数类型|描述 
无


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/auto_snapshot/policy/bind
```
Body:
```
{
    "Region": "ap-guangzhou",
    "AutoSnapshotPolicyId": "asp-63p7jk73",
    "DiskIds": [
        "disk-plqkg6me"
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


## /v1/tencent/auto_snapshot/policy/unbind
#### 功能：云硬盘解绑定期快照策略
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
DiskIds |string array|是|- |要解绑定期快照策略的云盘ID列表
AutoSnapshotPolicyIds | string| 是|-|要解绑的定期快照策略ID
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region | string|是|- | 地域

### 返回参数
名称|参数类型|描述 
无


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/auto_snapshot/policy/unbind
```
Body:
```
{
    "Region": "ap-guangzhou",
    "AutoSnapshotPolicyId": "asp-63p7jk73",
    "DiskIds": [
        "disk-plqkg6me"
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


## /v1/tencent/snapshot/distributed/inspect
#### 功能：各地存在快照数量
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
SnapshotIds | string array| 否|-|要查询快照的ID列表
Filters |struct array|否|- |过滤条件
Offset |uint64|否|0 |偏移量
Limit |uint64|否|20 |返回数量，默认为20，最大值为100
Order |string|否|- |输出定期快照列表的排列顺序
OrderField |string|否|- |定期快照列表排序的依据字段
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid

### 返回参数
名称|参数类型|描述 
Count|int|地域数量
Region|string|地域
RegionName|string|地域名字
RegionState|string|地域状态


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/snapshot/distributed/inspect
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
        "RegionName": "曼谷",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-beijing",
        "RegionName": "北京",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-chengdu",
        "RegionName": "成都",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-chongqing",
        "RegionName": "重庆",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 3,
        "Region": "ap-guangzhou",
        "RegionName": "广州",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-hongkong",
        "RegionName": "中国香港",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-mumbai",
        "RegionName": "孟买",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-nanjing",
        "RegionName": "南京",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-seoul",
        "RegionName": "首尔",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-shanghai",
        "RegionName": "上海",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-shanghai-fsi",
        "RegionName": "上海金融",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-shenzhen-fsi",
        "RegionName": "深圳金融",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-singapore",
        "RegionName": "新加坡",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "ap-tokyo",
        "RegionName": "东京",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "eu-frankfurt",
        "RegionName": "法兰克福",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "eu-moscow",
        "RegionName": "莫斯科",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "na-ashburn",
        "RegionName": "弗吉尼亚",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "na-siliconvalley",
        "RegionName": "硅谷",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 0,
        "Region": "na-toronto",
        "RegionName": "多伦多",
        "RegionState": "AVAILABLE"
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/tencent/auto_snapshot/distributed/inspect
#### 功能：各地域存在快照策略数量
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
AutoSnapshotPolicyIds | string array| 否|-|要查询的定期快照策略ID列表
Filters |struct array|否|- |过滤条件
Offset |uint64|否|- |偏移量
Limit |uint64|否|- |返回数量，默认为20，最大值为100
Order |string|否|- |输出定期快照列表的排列顺序
OrderField |string|否|- |定期快照列表排序的依据字段
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid

### 返回参数
名称|参数类型|描述 
Count|int|地域数量
Region|string|地域
RegionName|string|地域名字
RegionState|string|地域状态


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/auto_snapshot/distributed/inspect
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
        "Count": 1,
        "Region": "ap-bangkok",
        "RegionName": "亚太地区(曼谷)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 1,
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
        "Count": 1,
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
        "Count": 1,
        "Region": "ap-hongkong",
        "RegionName": "港澳台地区(中国香港)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 1,
        "Region": "ap-mumbai",
        "RegionName": "亚太地区(孟买)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 1,
        "Region": "ap-nanjing",
        "RegionName": "华东地区(南京)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 1,
        "Region": "ap-seoul",
        "RegionName": "亚太地区(首尔)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 1,
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
        "Count": 1,
        "Region": "ap-singapore",
        "RegionName": "东南亚地区(新加坡)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 1,
        "Region": "ap-tokyo",
        "RegionName": "亚太地区(东京)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 1,
        "Region": "eu-frankfurt",
        "RegionName": "欧洲地区(法兰克福)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 1,
        "Region": "eu-moscow",
        "RegionName": "欧洲地区(莫斯科)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 1,
        "Region": "na-ashburn",
        "RegionName": "美国东部(弗吉尼亚)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 1,
        "Region": "na-siliconvalley",
        "RegionName": "美国西部(硅谷)",
        "RegionState": "AVAILABLE"
      },
      {
        "Count": 1,
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