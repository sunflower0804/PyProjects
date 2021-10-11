[back to api overview](../api_overview.md#api)

## /v1/tencent/compute/create
#### 功能：创建虚拟机
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region|string|是|- |地域
Placement |struct|是|- |实例所在的位置
ImageId |string|否|- |指定有效的[镜像]
InstanceChargeType |string|是|- |实例[计费类型]
InstanceChargePrepaid |struct|否|-|预付费模式
InstanceType |string|是|-|实例机型
SystemDisk |struct|否|- |实例系统盘配置信息
DataDisks |array|否|- |实例数据盘配置信息
VirtualPrivateCloud |struct|否|- |私有网络相关信息配置
InternetAccessible |struct|否|0 |公网带宽相关信息设置
InstanceCount |int64|否|1 |购买实例数量
InstanceName |string|否|“未命名”|实例显示名称
SecurityGroupIds |string array|是|- |实例所属安全组
EnhancedService |struct|否|- |增强服务

### 返回参数
名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/compute/create
```
Body:
```
{
    "Region": "ap-guangzhou",
    "Placement": {
        "Zone": "ap-guangzhou-3"
    },
    "ImageId": "img-9id7emv7",
    "SystemDisk": {
        "DiskType": "CLOUD_PREMIUM",
        "DiskSize": 50
    },
    "InternetAccessible": {
        "InternetMaxBandwidthOut": 1,
        "PublicIpAssigned": true
    },
    "securityGroupId": [
        "sg-n5ihii7d"
    ],
    "InstanceCount": 1,
    "InstanceName": "123",
    "LoginSettings": {
        "Password": "964322396.cda"
    },
    "InstanceType": "MA2.SMALL8",
    "EnhancedService": {
        "SecurityService": {
            "Enabled": false
        },
        "MonitorService": {
            "Enabled": false
        }
    },
    "cluster_uuid": "a7d3bc11-e5dd-4fc3-90cf-f9bb466ba9df",
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


## /v1/tencent/compute/delete
#### 功能：删除云服务器
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TenantUuid | string|是|- |租户uuid
 ClusterUuid | string|是|- |集群uuid
 Region|string|是|- |地域
 InstanceIds|string array|是|- |一个或多个待操作的实例ID

### 返回参数
名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/compute/delete
```
Body:
```
{
    "Region": "ap-guangzhou",
    "InstanceIds": [
        "ins-2n9bmcww"
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


## /v1/tencent/compute/update
#### 功能：更新云服务器，用于修改实例的属性（目前只支持修改实例的名称和关联的安全组）
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TenantUuid | string|是|- |租户uuid
 ClusterUuid | string|是|- |集群uuid
 Region|string|是|- |地域
 InstanceIds|string array|是|- |一个或多个待操作的实例ID
 InstanceName|string|否|“” |实例名称
 SecurityGroups|string array|否|- |指定实例的安全组Id列表

### 返回参数
名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/compute/update
```
Body:
```
{
    "Region": "ap-guangzhou",
    "InstanceIds": [
        "ins-2n9bmcww"
    ],
    "InstanceName": "1234",
    "cluster_uuid": "a7d3bc11-e5dd-4fc3-90cf-f9bb466ba9df",
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


## /v1/tencent/compute/reset
#### 功能：用于重装指定实例上的操作系统
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TenantUuid | string|是|- |租户uuid
 ClusterUuid | string|是|- |集群uuid
 Region|string|是|- |地域
 InstanceId|string|是|- |实例ID
 SystemDisk|struct|是|- |实例系统盘配置信息
 LoginSettings|struct|是|- |实例登录设置
 EnhancedService|struct|否|- |增强服务
 ImageId|string|是|- |指定有效的[镜像]

### 返回参数
名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/compute/reset
```
Body:
```
{
    "Region": "ap-guangzhou",
    "InstanceId": "ins-2n9bmcww",
    "SystemDisk": {
        "DiskType": "CLOUD_PREMIUM",
        "DiskSize": 50
    },
    "LoginSettings": {
        "Password": "964322396.cda"
    },
    "EnhancedService": {
        "SecurityService": {
            "Enabled": false
        },
        "MonitorService": {
            "Enabled": false
        }
    },
    "ImageId": "img-n7nyt2d7",
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


## /v1/tencent/compute/list
#### 功能：云服务列表
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TenantUuid | string|是|- |租户uuid
 ClusterUuid | string|是|- |集群uuid
 PageNum | int|否|0 |翻页偏移量
 PageSize | int|否|0 |每页的限制数量
 Region|string|是|- |地域
 Fuzzy |string|否|“” |过滤字符串

### 返回参数
名称|参数类型|描述
---|---|---
TotalCount|int|实例总数
List|struct array|云服务器列表
VpcName|string array|vpc名称

### List 对象
Placement|struct|实例所在的位置
InstanceId|string|实例`ID`
InstanceType|string|实例机型
CPU|int64|实例的CPU核数
Memory|int64|实例内存容量
RestrictState|string|实例业务状态
InstanceName|string|实例名称
InstanceChargeType|string|实例计费模式
SystemDisk|struct|实例系统盘信息
DataDisks|struct array|实例数据盘信息
PrivateIpAddresses|string array|实例主网卡的内网`IP`列表
PublicIpAddresses|string array|实例主网卡的公网`IP`列表
InternetAccessible|struct|实例带宽信息
VirtualPrivateCloud|struct|实例所属虚拟私有网络信息
ImageId|string|生产实例所使用的镜像
RenewFlag|string|自动续费标识
CreatedTime|string|创建时间
ExpiredTime|string|到期时间
OsName|string|操作系统名称
SecurityGroupIds|string array|实例所属安全组
LoginSettings|struct|实例登录设置
InstanceState|string|实例状态
Tags|struct array|实例关联的标签列表
StopChargingMode|string|实例的关机计费模式
Uuid|string|实例全局唯一ID
LatestOperation|string|实例的最新操作
LatestOperationState|string|实例的最新操作状态
LatestOperationRequestId|string|实例最新操作的唯一请求
DisasterRecoverGroupId|string|分散置放群组ID
IPv6Addresses|string|实例的IPv6地址
CamRoleName|string|CAM角色名
### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/compute/list
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
        "Placement": {
          "Zone": "ap-guangzhou-3",
          "ProjectId": 1196468
        },
        "InstanceId": "ins-2n9bmcww",
        "InstanceType": "MA2.SMALL8",
        "CPU": 1,
        "Memory": 8,
        "RestrictState": "NORMAL",
        "InstanceName": "123",
        "InstanceChargeType": "POSTPAID_BY_HOUR",
        "SystemDisk": {
          "DiskType": "CLOUD_PREMIUM",
          "DiskId": "disk-m361x8sm",
          "DiskSize": 50
        },
        "PrivateIpAddresses": [
          "172.16.16.4"
        ],
        "PublicIpAddresses": [
          "119.29.162.50"
        ],
        "InternetAccessible": {
          "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
          "InternetMaxBandwidthOut": 1
        },
        "VirtualPrivateCloud": {
          "VpcId": "vpc-evvn0y6d",
          "SubnetId": "subnet-nv3ex0mo",
          "AsVpcGateway": false
        },
        "ImageId": "img-9id7emv7",
        "CreatedTime": "2021-08-27T07:11:56Z",
        "OsName": "Windows Server 2016 数据中心版 64位中文版",
        "SecurityGroupIds": [
          "sg-5ythgemh"
        ],
        "LoginSettings": {},
        "InstanceState": "RUNNING",
        "StopChargingMode": "NOT_APPLICABLE",
        "Uuid": "e9c8f253-a621-40d5-9615-8ee7a2d53e84",
        "LatestOperation": "ResetInstancesPassword",
        "LatestOperationState": "OPERATING",
        "LatestOperationRequestId": "bfa1d715-39c3-43e1-855f-2ee87e541264",
        "DisasterRecoverGroupId": "",
        "CamRoleName": "",
        "InstanceTypeName": "内存型MA2"
      }
    ],
    "VpcName": [
      "Default-VPC"
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/tencent/compute/inspect
#### 功能：云服务器详情
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TenantUuid | string|是|- |租户uuid
 ClusterUuid | string|是|- |集群uuid
 Region|string|是|- |地域
 InstanceId|string|是|- |实例ID

### 返回参数
名称|参数类型|描述
---|---|---
Placement|struct|实例所在的位置
InstanceId|string|实例`ID`
InstanceType|string|实例机型
CPU|int64|实例的CPU核数
Memory|int64|实例内存容量
RestrictState|string|实例业务状态
InstanceName|string|实例名称
InstanceChargeType|string|实例计费模式
SystemDisk|struct|实例系统盘信息
DataDisks|struct array|实例数据盘信息
PrivateIpAddresses|string array|实例主网卡的内网`IP`列表
PublicIpAddresses|string array|实例主网卡的公网`IP`列表
InternetAccessible|struct|实例带宽信息
VirtualPrivateCloud|struct|实例所属虚拟私有网络信息
ImageId|string|生产实例所使用的镜像
RenewFlag|string|自动续费标识
CreatedTime|string|创建时间
ExpiredTime|string|到期时间
OsName|string|操作系统名称
SecurityGroupIds|string array|实例所属安全组
LoginSettings|struct|实例登录设置
InstanceState|string|实例状态
Tags|struct array|实例关联的标签列表
StopChargingMode|string|实例的关机计费模式
Uuid|string|实例全局唯一ID
LatestOperation|string|实例的最新操作
LatestOperationState|string|实例的最新操作状态
LatestOperationRequestId|string|实例最新操作的唯一请求
DisasterRecoverGroupId|string|分散置放群组ID
IPv6Addresses|string|实例的IPv6地址
CamRoleName|string|CAM角色名

### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/compute/inspect
```
Body:
```
{
    "Region": "ap-guangzhou",
    "InstanceId": "ins-2n9bmcww",
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
    "Placement": {
      "Zone": "ap-guangzhou-3",
      "ProjectId": 1196468
    },
    "InstanceId": "ins-2n9bmcww",
    "InstanceType": "MA2.SMALL8",
    "CPU": 1,
    "Memory": 8,
    "RestrictState": "NORMAL",
    "InstanceName": "1234",
    "InstanceChargeType": "POSTPAID_BY_HOUR",
    "SystemDisk": {
      "DiskType": "CLOUD_PREMIUM",
      "DiskId": "disk-m361x8sm",
      "DiskSize": 50
    },
    "PrivateIpAddresses": [
      "172.16.16.4"
    ],
    "PublicIpAddresses": [
      "119.29.162.50"
    ],
    "InternetAccessible": {
      "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
      "InternetMaxBandwidthOut": 1
    },
    "VirtualPrivateCloud": {
      "VpcId": "vpc-evvn0y6d",
      "SubnetId": "subnet-nv3ex0mo",
      "AsVpcGateway": false
    },
    "ImageId": "img-n7nyt2d7",
    "CreatedTime": "2021-08-27T07:11:56Z",
    "OsName": "CentOS 8.2 64位",
    "SecurityGroupIds": [
      "sg-5ythgemh"
    ],
    "LoginSettings": {},
    "InstanceState": "RUNNING",
    "StopChargingMode": "NOT_APPLICABLE",
    "Uuid": "e9c8f253-a621-40d5-9615-8ee7a2d53e84",
    "LatestOperation": "ResetInstance",
    "LatestOperationState": "SUCCESS",
    "LatestOperationRequestId": "80795021-0ee4-4abe-ba79-4ee063880252",
    "DisasterRecoverGroupId": "",
    "CamRoleName": "",
    "InstanceTypeName": "内存型MA2"
  }
}
```

#### 异常返回示例

### 状态码


## /v1/tencent/compute/turn_on
#### 功能：开启云服务器
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TenantUuid | string|是|- |租户uuid
 ClusterUuid | string|是|- |集群uuid
 Region|string|是|- |地域
 InstanceId|string array|是|- |实例ID

### 返回参数
名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/compute/turn_on
```
Body:
```
{
    "Region": "ap-guangzhou",
    "InstanceIds": [
        "ins-2n9bmcww"
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


## /v1/tencent/compute/turn_off
#### 功能：创建镜像
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TenantUuid | string|是|- |租户uuid
 ClusterUuid | string|是|- |集群uuid
 Region|string|是|- |地域
 InstanceId|string array|是|- |实例ID
 ForceStop|bool|否|false |是否强制关机

### 返回参数
名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/compute/turn_off
```
Body:
```
{
    "Region": "ap-guangzhou",
    "InstanceIds": [
        "ins-2n9bmcww"
    ],
    "ForceStop": false,
    "cluster_uuid": "a7d3bc11-e5dd-4fc3-90cf-f9bb466ba9df",
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
