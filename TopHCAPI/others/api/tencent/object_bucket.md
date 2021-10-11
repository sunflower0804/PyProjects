[back to api overview](../api_overview.md#api)

## /v1/tencent/cos/bucket/create
#### 功能：创建存储桶
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TenantUuid | string|是|- |租户uuid
 ClusterUuid | string|是|- |集群uuid
 Region|string|是|- |地域
 BucketName|string|是|- |存储桶名称
 XCosACL|string|是|- |存储桶的访问权限

### 返回参数
名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/cos/bucket/create
```
Body:
```
{
    "Region": "ap-guangzhou",
    "BucketName": "123-1303063665",
    "XCosACL": "private",
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


## /v1/tencent/cos/bucket/delete
#### 功能：删除存储桶
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region|string|是|- |地域
BucketName|string|是|- |存储桶名称

### 返回参数
名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/cos/bucket/delete
```
Body:
```
{
    "Region": "ap-guangzhou",
    "BucketName": "123-1303063665",
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


## /v1/tencent/cos/bucket/list
#### 功能：查看存储桶列表
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TenantUuid | string|是|- |租户uuid
 ClusterUuid | string|是|- |集群uuid
 PageNum | int|否|0 |翻页偏移量
 PageSize | int|否|0 |每页的限制数量
 Fuzzy |string|否|- |过滤字符串

### 返回参数
名称|参数类型|描述
---|---|---
TotalCount |int|存储桶个数
List |struct array|存储桶列表
BuckName |string array|存储桶名称列表

### List 对象
Name|string|名称
Region|string|地域
CreationDate|string|创建日期

### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/cos/bucket/list
```
Body:
```
{
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
        "Name": "123-1303063665",
        "Region": "ap-guangzhou",
        "CreationDate": "2021-08-27T08:45:46Z"
      },
      {
        "Name": "maybe-1303063665",
        "Region": "ap-shenzhen-fsi",
        "CreationDate": "2020-12-21T09:35:20Z"
      }
    ],
    "BuckName": [
      "123",
      "maybe"
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/tencent/cos/bucket/inspect
#### 功能：查看存储桶内对象列表
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TenantUuid | string|是|- |租户uuid
 ClusterUuid | string|是|- |集群uuid
 PageNum | int|否|0 |翻页偏移量
 PageSize | int|否|0 |每页的限制数量
 Fuzzy |string|否|- |过滤字符串
 Region|string|是|- |地域

### 返回参数
名称|参数类型|描述
---|---|---
TotalCount|int|总数
List|struct array|对象列表

### List 对象
Key|string|对象名称
ETag|string|标志
Size|int|大小
LastModified|string|最后修改时间
StorageClass|string|存储类型
Owner|struct|所有者

### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/cos/bucket/inspect
```
Body:
```
{
    "Region": "ap-shenzhen-fsi",
    "PageNum": 0,
    "PageSize": 20,
    "Fuzzy": "",
    "BucketName": "maybe-1303063665",
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
        "Key": "myqcloud.com子类型_  .png",
        "ETag": "\"fd6933385792cb05c798977dbb2d2d0b\"",
        "Size": 68443,
        "PartNumber": 0,
        "LastModified": "2021-08-10T06:08:24.000Z",
        "StorageClass": "STANDARD",
        "Owner": {
          "UIN": "",
          "ID": "1303063665",
          "DisplayName": "1303063665"
        }
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/tencent/cos/bucket/acl/update
#### 功能：更改存储桶访问控制权限
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TenantUuid | string|是|- |租户uuid
 ClusterUuid | string|是|- |集群uuid
 Region|string|是|- |地域
 BucketName|string|是|- |存储桶名称
 XCosACL|string|是|- |存储桶的访问权限

### 返回参数
名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/cos/bucket/acl/update
```
Body:
```
{
    "Region": "ap-guangzhou",
    "BucketName": "123-1303063665",
    "Header": {
        "XCosACL": "public-read-write"
    },
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


## /v1/tencent/cos/bucket/clear
#### 功能：清空存储桶内对象列表
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region|string|是|- |地域
BucketName|string|是|- |存储桶名称

### 返回参数
名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/cos/bucket/clear
```
Body:
```
{
    "Region": "ap-guangzhou",
    "BucketName": "123-1303063665",
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


## /v1/tencent/cos/bucket/get/cors
#### 功能：获取存储桶CORS，实现跨域访问读取
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Region|string|是|- |地域
BucketName|string|是|- |存储桶名称

### 返回参数
名称|参数类型|描述
---|---|---
XMLName|struct|// A Name represents an XML name (Local) annotated
               // with a name space identifier (Space).
               // In tokens returned by Decoder.Token, the Space identifier
               // is given as a canonical URL, not the short prefix used
               // in the document being parsed.
Rules|struct array|---

### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/cos/bucket/get/cors
```
Body:
```
{
    "Region": "ap-guangzhou",
    "BucketName": "123-1303063665",
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
    "XMLName": {
      "Space": "",
      "Local": ""
    },
    "Rules": null
  }
}
```

#### 异常返回示例

### 状态码