[back to api overview](../api_overview.md#api)

## /v1/tencent/event/list
#### 功能：查看云服务器的event
#### 请求类型：post

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
EndTime | int64|是|- |结束时间
StartTime | int64|是|- |开始时间
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region|string | 是|- |腾讯云云服务器所在地域
InstanceId | string|是|- |腾讯云云服务器实例id
Fuzzy | string|否|- |过滤字符
PageNum | int|否|0 |页数
PageSize | int|否|0 |页大小

### 返回参数
名称|参数类型|描述
---|---|---
List | array | 事件列表
TotalCount | int | 事件总数

### list 对象
Resources | struct |资源对
AccountID |int64 |主账号ID
CloudAuditEvent |string|日志详情
ErrorCode| int64 |鉴权错误码
EventId| string |日志ID
EventName | string |事件名称
EventNameCn|string|事件名称中文描述
EventRegion|string|事件地域
EventSource|string|请求来源
EventTime|string|事件时间
RequestID|string|请求ID
ResourceRegion|string|资源地域
ResourceTypeCn|string|资源类型中文描述
SecretId|string|证书ID
SourceIPAddress|string|源IP
Username|string|用户名

### Resources 对象
ResourceName|string|资源名称
ResourceType|string|资源类型

### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/event/list
```
Body:
```
{
    "PageNum": 0,
    "PageSize": 10,
    "Region": "ap-guangzhou",
    "InstanceId": "ins-in511g92",
    "StartTime": 1629907200,
    "EndTime": 1629993599,
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
        "Resources": {
          "ResourceName": "instance/ins-in511g92",
          "ResourceType": "cvm"
        },
        "AccountID": 10001500767*,
        "CloudAuditEvent": "{\"userIdentity\":{\"principalId\":\"100015596048\",\"accountId\":\"100015007673\",\"secretId\":\"\",\"type\":\"CAMUser\",\"userName\":\"100015596048\",\"sessionContext\":\"\"},\"@timestamp\":\"2021-08-26T06:59:07.012875\",\"onlyRecordNotSeen\":\"0\",\"eventRegion\":\"ap-guangzhou\",\"eventVersion\":2,\"errorCode\":\"0\",\"errorMessage\":\"permission verify\",\"requestID\":\"22901fbd-a884-40ea-8708-54119e22a495\",\"eventID\":\"22901fbd-a884-40ea-8708-54119e22a495\",\"apiVersion\":\"3.0\",\"eventType\":\"ApiCall\",\"actionType\":\"Write\",\"authMode\":\"2\",\"isRisk\":\"0\",\"ruleId\":\"0\",\"httpMethod\":\"POST\",\"apiErrorCode\":0,\"apiErrorMessage\":\"\",\"userAgent\":\"\",\"eventTime\":1629961140,\"updateEsTime\":16299611402449116,\"sensitiveAction\":\"\",\"cliIp\":\"\",\"eventPlatform\":\"0\",\"sourceIPAddress\":\"\",\"resourceType\":\"cvm\",\"eventName\":\"StopInstances\",\"eventSource\":\"cvm.tencentcloudapi.com\",\"requestParameters\":\"\",\"resources\":\"[\\\"qcs:id\\\\\\/1196468:cvm:ap-guangzhou:uin\\\\\\/100015007673:instance\\\\\\/ins-in511g92\\\"]\",\"resourceName\":\"instance\\/ins-in511g92\",\"cloudapi\":0,\"auth\":1,\"signature\":0}",
        "ErrorCode": 0,
        "EventName": "StopInstances",
        "EventNameCn": "关闭实例",
        "EventRegion": "ap-guangzhou",
        "EventSource": "cvm.tencentcloudapi.com",
        "EventTime": "1629961140",
        "RequestID": "22901fbd-a884-40ea-8708-54119e22a4**",
        "ResourceRegion": "ap-guangzhou",
        "ResourceTypeCn": "云服务器",
        "SecretId": "",
        "SourceIPAddress": "",
        "Username": "10001559604*"
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/tencent/event/snapshot/logs/list
#### 功能：查看快照的日志
#### 请求类型：post

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
EndTime | int64|是|- |结束时间
StartTime | int64|是|- |开始时间
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region|string | 是|- |快照所属云服务器所在地域
SnapshotId | string|是|- |快照id
Fuzzy | string|否|- |过滤字符
PageNum | int|否|0 |页数
PageSize | int|否|0 |页大小

### 返回参数
名称|参数类型|描述
---|---|---
List | array | 事件列表
TotalCount | int | 事件总数

### list 对象
Resources | struct |资源对
AccountID |int64 |主账号ID
CloudAuditEvent |string|日志详情
ErrorCode| int64 |鉴权错误码
EventId| string |日志ID
EventName | string |事件名称
EventNameCn|string|事件名称中文描述
EventRegion|string|事件地域
EventSource|string|请求来源
EventTime|string|事件时间
RequestID|string|请求ID
ResourceRegion|string|资源地域
ResourceTypeCn|string|资源类型中文描述
SecretId|string|证书ID
SourceIPAddress|string|源IP
Username|string|用户名

### Resources 对象
ResourceName|string|资源名称
ResourceType|string|资源类型

### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/event/snapshot/logs/list
```
Body:
```
{
    "PageNum": 0,
    "PageSize": 10,
    "SnapshotId": "snap-6ixzjp6d",
    "Region": "ap-guangzhou",
    "StartTime": 1627401600,
    "EndTime": 1629993599,
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
        "Resources": {
          "ResourceName": "volume/*|snapshot/snap-6ixzjp6d",
          "ResourceType": "cvm"
        },
        "AccountID": 1000150076**,
        "CloudAuditEvent": "{\"userIdentity\":{\"principalId\":\"100015596048\",\"accountId\":\"100015007673\",\"secretId\":\"\",\"type\":\"CAMUser\",\"userName\":\"100015596048\",\"sessionContext\":\"\"},\"@timestamp\":\"2021-08-05T07:30:00.804501\",\"onlyRecordNotSeen\":\"0\",\"eventRegion\":\"ap-guangzhou\",\"eventVersion\":2,\"errorCode\":\"0\",\"errorMessage\":\"permission verify\",\"requestID\":\"6326bcab-e6f2-482a-a807-276d0c0a2931\",\"eventID\":\"6326bcab-e6f2-482a-a807-276d0c0a2931\",\"apiVersion\":\"3.0\",\"eventType\":\"ApiCall\",\"actionType\":\"Write\",\"authMode\":\"2\",\"isRisk\":\"0\",\"ruleId\":\"0\",\"httpMethod\":\"POST\",\"apiErrorCode\":0,\"apiErrorMessage\":\"\",\"userAgent\":\"\",\"eventTime\":1628148590,\"updateEsTime\":16281485973093297,\"sensitiveAction\":\"\",\"cliIp\":\"\",\"eventPlatform\":\"0\",\"sourceIPAddress\":\"\",\"resourceType\":\"cvm\",\"eventName\":\"CreateCbsStorages\",\"eventSource\":\"cvm.tencentcloudapi.com\",\"requestParameters\":\"\",\"resources\":\"[\\\"qcs::cvm:gz:uin\\\\\\/100015007673:volume\\\\\\/*\\\",\\\"qcs:id\\\\\\/1196468:cvm:gz:uin\\\\\\/100015007673:snapshot\\\\\\/snap-6ixzjp6d\\\"]\",\"resourceName\":\"volume\\/*|snapshot\\/snap-6ixzjp6d\",\"cloudapi\":0,\"auth\":1,\"signature\":0}",
        "ErrorCode": 0,
        "EventName": "CreateCbsStorages",
        "EventNameCn": "购买云盘",
        "EventRegion": "ap-guangzhou",
        "EventSource": "cvm.tencentcloudapi.com",
        "EventTime": "1628148590",
        "RequestID": "6326bcab-e6f2-482a-a807-276d0c0a29**",
        "ResourceRegion": "",
        "ResourceTypeCn": "云服务器",
        "SecretId": "",
        "SourceIPAddress": "",
        "Username": "10001559604*"
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码

