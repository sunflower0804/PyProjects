[back to api overview](../api_overview.md#label_api)

[TOC]

---
<small>
备注：  
在该文档中，对数据结构用如下表述：  

+ 字段Field为Type类型： `Field : Type`  
+ 字段Field为Type数组类型： `Field : [ Type ]`  
+ 字段Field为<Type1, Type2>键值对的字典类型： `Field : { Type1 : Type2 }`
+ 字段Field为结构：`Field : { Field1 : Type1 }`
+ 当结构含有匿名字段时，代表该匿名结构下的字段直接作为结构的字段。即：  
`{ AnonType, Field : Type }`，当AnonType为`{ Field1 : Type1 }`时，等价于：`{ Field1 : Type1, Field : Type }`
</small>

# 请求接口
## 镜像仓库相关
### POST&nbsp; /v1/compute/repository/get
获取镜像仓库信息。

<big>**请求参数**</big>  

 名称 | 参数类型 | 是否必填 | 描述
---|---|---|---
 cluster_uuid|string|是| 集群uuid
 tenant|string|是| 租户uuid
 uuid|string|是| 镜像仓库uuid
 page_number|int|否| 分页序号
 page_size|int|否| 分页大小

+ **page_number, page_size**  
分页参数用于仓库的镜像列表分页展示。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
	"total_count" : Number,
	"list" : [ ImageFileInfo ],
	ComputeListRepositoryEntry,
	"path" : String
}
```

+ **total_count**  
镜像列表总数。用于分页展示。
+ **list**  
镜像信息列表。见[ImageFileInfo](#imagefileinfo)。
+ **ComputeListRepositoryEntry**  
镜像仓库信息。见[ComputeListRepositoryEntry](#computelistrepositoryentry)。
+ **path**  
镜像仓库访问路径。

获取镜像仓库信息时，若当时仓库的访问路径不可用，会触发仓库的重新挂载机制，并报错`scode : 22504`。需要等待重新挂载完成，路径正常后仓库才能正常返回信息。  

<big>**示例**</big>  
**请求示例**  
```
http://10.30.33.25:8080/v1/compute/repository/get?cluster_uuid=650ea11b-b7fb-4269-8232-aa53865aab3b&page_num=0&page_size=5&tenant=8aeb88f1-b894-4fae-99e8-e3c2434ec346&uuid=3e471f00-642c-4914-bb6f-f5a63e328d20
```
**返回示例**  
```json
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
        "Name": "kk.img",
        "Type": "File",
        "Size": 1645293568,
        "LastModified": 1630979901,
        "Md5": "aa3ef92105ac09f5a198f95a4d6efddd",
        "Vsize": 5368709120,
        "Format": "qcow2",
        "SecurityType": "",
        "Extra": null
      }
    ],
    "cluster_uuid": "650ea11b-b7fb-4269-8232-aa53865aab3b",
    "cluster_name": "host3222-cvm3322",
    "tenant": "8aeb88f1-b894-4fae-99e8-e3c2434ec346",
    "tenant_name": "gg_tenant",
    "uuid": "3e471f00-642c-4914-bb6f-f5a63e328d20",
    "name": "gg_iso",
    "usages": [
      "cdrom",
      "floppy",
      "image"
    ],
    "acl": null,
    "ctime": 1627611013,
    "mtime": 1627611013,
    "source_vsd": {
      "volume_uuid": "b4239d43-0c82-448b-b410-b03843d26fa3"
    },
    "capacity": 26843545600,
    "path": "http://10.30.32.22:28000/b4239d43-0c82-448b-b410-b03843d26fa3/data"
  }
}
```

### POST&nbsp; /v1/compute/repository/set
修改镜像仓库设置。

<big>**请求参数**</big>  
```
{
	CommonClusterTenantScope,
	"uuid" : String,
	"name" : String,
	"usages" : String,
	"acl" : RepositoryACL,
 	"source_volume" : ComputeRepositoryVolumeInfo,
	"source_vsd" : ComputeRepositoryVsdInfo
}
```

+ **CommonClusterTenantScope**  
指定镜像仓库所在集群、租户。见[CommonClusterTenantScope](#commonclustertenantscope)。  
_必需_ ： 是
+ **uuid**  
指定待修改镜像仓库的uuid。该项不可修改。  
_必需_ ： 是
+ **acl**  
_必需_ ： 是

修改参数见[ComputeListRepositoryEntry](#computelistrepositoryentry)。  
不需要修改的参数不指定或置空。但是`acl`参数置空为有效修改，因此必须传值。  
一个镜像仓库只能有一个source，即`source_volume`和`source_vsd`互斥。  

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
	ComputeListRepositoryEntry
}
```

修改后的镜像仓库详情。见[ComputeListRepositoryEntry](#computelistrepositoryentry)。

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","uuid":"854846e1-8f05-4d5d-bcaf-97ae1ee5d498","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","name":"temp22","usages":["image"],"acl":{"Values":[]},"source_vsd":{"volume_uuid":"c69451a6-e6be-46b0-a2bc-84307354374a"}}
```
**返回示例**  
```json
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "cluster_uuid": "650ea11b-b7fb-4269-8232-aa53865aab3b",
    "cluster_name": "host3222-cvm3322",
    "tenant": "a5badacf-a25c-4171-9aff-b619fc2d300a",
    "tenant_name": "ycb1",
    "uuid": "854846e1-8f05-4d5d-bcaf-97ae1ee5d498",
    "name": "temp22",
    "usages": [
      "image"
    ],
    "acl": {
      "Values": null
    },
    "ctime": 1631177666,
    "mtime": 1631177961,
    "source_vsd": {
      "volume_uuid": "c69451a6-e6be-46b0-a2bc-84307354374a"
    },
    "capacity": 1073741824
  }
}
```

### POST&nbsp; /v1/compute/repository/delete
删除镜像仓库。

<big>**请求参数**</big>  
```
{
	CommonClusterTenantScope,
	"uuid" : String
}
```

指定集群、租户、仓库uuid。  
删除镜像仓库不会导致镜像仓库存储源卷被一起删除。该卷可以后续手动删除。  

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","uuid":"854846e1-8f05-4d5d-bcaf-97ae1ee5d498"}
```
**返回示例**  
```json
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {}
}
```

### POST&nbsp; /v1/compute/repository/list
镜像仓库列表

<big>**请求参数**</big>  
```
{
	CommonClusterTenantScope,
	PagingParam,
	"filter_usage" : String,
	"filter_name" : String
}
```

+ **CommonClusterTenantScope**  
指定查询的集群、租户范围。允许不指定集群或租户，进行广范围查询。  
_必需_ ： 否
+ **PagingParam**  
仓库分页展示参数。见[PagingParam](#pagingparam)。  
_必需_ ： 否
+ **filter_name**  
过滤镜像仓库名称。镜像仓库名称需要包含`filter_name`子字符串。  
_必需_ ： 否
+ **filter_usage**  
过滤镜像仓库用途。镜像仓库用途需要匹配`filter_usage`。  
_必需_ ： 否

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
	"total_count" : Number,
	"list" : [ ComputeListRepositoryEntry ],
	"each_scope_list_state" : [ EachResourceRangeListState ]
}
```

+ **total_count**  
过滤后的镜像仓库总数。用于分页显示。
+ **list**  
镜像仓库信息列表。见[ComputeListRepositoryEntry](#computelistrepositoryentry)。
+ **each_scope_list_state**  
每个集群、租户的查询结果统计。见[EachResourceRangeListState](#eachresourcerangeliststate)。

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","page_num":0,"page_size":10,"tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","filter_name":"emp","multiple":false}
```
**返回示例**  
```json
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
        "cluster_uuid": "650ea11b-b7fb-4269-8232-aa53865aab3b",
        "cluster_name": "host3222-cvm3322",
        "tenant": "d55f75c6-bd47-4263-b507-372acfac06a0",
        "tenant_name": "ycb",
        "uuid": "a902c92d-911f-43b5-9df4-e946ef9120cc",
        "name": "temp",
        "usages": [
          "image"
        ],
        "acl": null,
        "ctime": 1626870195,
        "mtime": 1626870195,
        "source_vsd": {
          "volume_uuid": "1e57697c-a77a-4b6f-8cf9-615a7869d404"
        },
        "capacity": 10737418240
      }
    ],
    "each_scope_list_state": [
      {
        "cluster_uuid": "650ea11b-b7fb-4269-8232-aa53865aab3b",
        "cluster_name": "host3222-cvm3322",
        "namespace_uuid": "91a57ba2-2904-4c90-bc16-85ecbbad815f",
        "result": {
          "scode": 0,
          "desc": "",
          "message": "success",
          "message_cn": "成功",
          "stack": null,
          "data": ""
        },
        "total_count": 1
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/repository/create
创建镜像仓库及其存储源。

<big>**请求参数**</big>  
```
{
	CommonClusterTenantScope,
	"uuid" : String,
	"name" : String,
	"usages" : String,
	"acl" : RepositoryACL,
	"capacity" : Number,
	"zone" : String,
	"volume_type" : String,
	"pool_uuid" : String
}
```

指定镜像仓库的参数大致和[ComputeListRepositoryEntry](#computelistrepositoryentry)一样。不一样参数主要是存储源相关参数：  

+ **capacity**  
创建存储卷的容量，即镜像仓库的总容量。  
_必需_ ： 是
+ **zone**  
创建存储卷的资源池uuid。  
_必需_ ： 是
+ **volume_type**  
创建存储卷类型。  
_必需_ ： 是
_有效值_ ： `vsd`(内置存储), `share`(共享存储)
+ **pool_uuid**  
创建存储卷的存储池uuid。  
_必需_ ： 否

使用内置存储时，卷会强制创建在租户的特殊存储池中，`pool_uuid`无效。使用共享存储时，必需提供共享存储池uuid。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
	ComputeListRepositoryEntry
}
```

修改后的镜像仓库详情。见[ComputeListRepositoryEntry](#computelistrepositoryentry)。

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","name":"temp2","usages":["image"],"acl":{"Values":[]},"capacity":1073741824,"zone":"a6f8ad4a-3fdf-4cf6-8fda-90a8093f5316","volume_type":"vsd","pool_uuid":""}
```
**返回示例**  
```json
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "cluster_uuid": "650ea11b-b7fb-4269-8232-aa53865aab3b",
    "cluster_name": "host3222-cvm3322",
    "tenant": "a5badacf-a25c-4171-9aff-b619fc2d300a",
    "tenant_name": "ycb1",
    "uuid": "854846e1-8f05-4d5d-bcaf-97ae1ee5d498",
    "name": "temp2",
    "usages": [
      "image"
    ],
    "acl": {
      "Values": null
    },
    "ctime": 1631177666,
    "mtime": 1631177666,
    "source_vsd": {
      "volume_uuid": "c69451a6-e6be-46b0-a2bc-84307354374a"
    },
    "capacity": 1073741824
  }
}
```

# 数据结构
## 通用结构
### BatchOutput
批量接口的统一返回结构。以统一对批量接口做错误检查、处理。
```
{
    "success" : Number,
    "fail" : Number,
    "results" : [ Output ]
}
```

+ **success, fail**  
成功、失败操作个数。
+ **results**  
每个操作请求的返回结果。每个结果用[Output](#output)封装，即接口的特定返回结构位于Response."results"\[\]."data"下。

### ClusterIdentifier
指定、描述相关集群。
```
{
    "cluster_uuid" : String,
    "cluster_name" : String,
    "cluster_mode" : String
}
```

+ **cluster_uuid**  
指定、展示集群uuid。请求中的主要参数。若为空，则指定纳管的全部超融合集群。
+ **cluster_name**  
展示集群名称。特定接口中作为请求参数使用。若`cluster_uuid`为空，该项为空。
+ **cluster_mode**  
仅用于展示集群类型。请求中该字段未使用。

### CommonClusterTenantScope
标记请求的目的集群、目的租户和目的命名空间的结构。被用于指定请求对象。
```
{
    ClusterIdentifier,
    TenantIdentifier,
    NamespaceIdentifier,
    "multiple" : Bool,
    "vm_type" : String
}
```

+ **ClusterIdentifier**  
见[ClusterIdentifier](#clusteridentifier)
+ **TenantIdentifier**  
见[TenantIdentifier](#tenantidentifier)
+ **NamespaceIdentifier**  
见[NamespaceIdentifier](#namespaceidentifier)
+ **multiple**  
对于default租户，用于区分请求对应的是全部纳管命名空间，还是只对应default命名空间。  
对于其他租户无效。
+ **vm_type**  
仅用于虚拟机相关接口记录操作日志时，描述里额外区分请求对象是桌面虚拟机还是云桌面。  
_有效值_ ： 
    - "GCD" 桌面虚拟机
    - "GDT" 云桌面
    - 其他 无额外标记

### EachResourceRangeListState
多集群或多命名空间操作、查询API中，返回记录每个集群、命名空间的操作、查询结果的数据。
```
{
    ClusterIdentifier,
    NamespaceIdentifier,
    "result" : Output,
    "total_count" : Number
}
```

+ **ClusterIdentifier**  
展示该部分对应的请求集群。
+ **NamespaceIdentifier**  
展示该部分对应的请求命名空间。
+ **result**  
记录该部分对应的请求错误信息。`Output.data`字段不使用。
+ **total_count**  
对于列表请求，记录该部分对应查询的满足筛选条件的结果总数。

### NamespaceIdentifier
指定、描述相关命名空间。
```
{
    "namespace_uuid" : String,
    "namespace_name" : String
}
```

+ **namespace_uuid**  
展示命名空间uuid。特定接口作为请求参数使用。
+ **namespace_name**  
展示命名空间名称。特定接口作为请求参数使用。

### Output
大部分http接口的统一返回结构。不同接口的不同类型的返回数据，都用这个结构封装成统一的实际返回结构，以统一做错误检查和处理。
```
{
    "scode" : Number,
    "desc" : String,
    "message" : String,
    "message_cn" : String,
    "stack" : [
        String
    ],
    "data" : Struct
}
```

+ **scode**   
错误码。不同错误码表示不同的错误原因。特别的，当`scode`等于0时，表示没有错误。
+ **desc**  
具体错误情景描述。包括错误信息的补充，与报错相关的对象，或一些第三方报错等。
+ **message**  
与错误码对应的英文错误信息。
+ **message_cn**  
与错误码对应的中文错误信息。
+ **stack**  
错误返回路径。记录错误发生时的服务、运行函数、运行位置等调试信息。
+ **data**  
接口实际返回数据。  
_类型_ ： 由各个接口单独约定。

### PagingParam
通用分页配置参数。
```
{
    "page_number" : Number,
    "page_size" : Number
}
```

+ **page_number**  
分页序号。返回第`page_number`页结果。从第0页开始。  
_是否必需_： 否  
+ **page_size**  
分页大小。返回结果以`page_size`个结果为一页。若不大于0则不进行分页。  
_是否必需_： 否  

### TenantIdentifier
指定、描述相关集群。
```
{
    "tenant" : String,
    "tenant_name" : String
}
```

+ **tenant**  
指定、展示租户uuid。请求中的主要参数。若为空，则指定所有租户。
+ **tenant_name**  
展示租户名称。特定接口用作为请求参数使用。若`tenant`为空，该项为空。

## 镜像仓库相关
### ComputeListRepositoryEntry
镜像仓库信息。
```
{
	CommonClusterTenantScope,
	"uuid" : String,
	"name" : String,
	"usages" : [ String ],
	"acl" : RepositoryACL,
	"ctime" : Number,
	"mtime" : Number,
	"source_volume" : ComputeRepositoryVolumeInfo,
	"source_vsd" : ComputeRepositoryVsdInfo,
	"capacity" : Number
}
```

+ **CommonClusterTenantScope**  
镜像仓库所在集群、租户。见[CommonClusterTenantScope](#commonclustertenantscope)。  
+ **uuid**  
镜像仓库uuid。
+ **name**  
镜像仓库名称。
+ **usages**  
镜像仓库用途标记。常用标记有：`cdrom`光驱,`floppy`软驱,`image`镜像,`security`安全网元,`stack-template`应用模板。
+ **acl**  
镜像仓库租户使用权限控制。见[RepositoryACL](#repositoryacl)。
+ **ctime**  
镜像仓库创建时间。Unix时间。
+ **mtime**  
镜像仓库修改时间。Unix时间。
+ **source_volume**  
镜像仓库共享存储源信息。有该项表明镜像仓库使用共享存储卷作为仓库存储。见[ComputeRepositoryVolumeInfo](#computerepositoryvolumeinfo)。
+ **source_vsd**  
镜像仓库内置存储源信息。有该项表明镜像仓库使用内置存储卷作为仓库存储。见[ComputeRepositoryVsdInfo](#computerepositoryvsdinfo)。
+ **capacity**  
镜像仓库总容量。

### ComputeRepositoryVolumeInfo
镜像仓库共享存储源信息。
```
{
	"volume" : String,
	"pool" : String,
	"machine_uuid" : String,
	"protocol" : String
}
```

+ **volume**  
共享存储卷uuid。
+ **pool**  
共享存储池uuid。
+ **machine_uuid**  
共享存储卷所在主机uuid。
+ **protocol**  
共享存储池类型。

### ComputeRepositoryVsdInfo 
镜像仓库内置存储源信息。
```
{
	"volume_uuid" : String
}
```

+ **volume_uuid**  
内置存储卷uuid。

### ImageFileInfo
镜像仓库存储的镜像相关信息。
```
{
	"Name" : String,
	"Type" : String,
	"Size" : Number,
	"LastModified" : Number,
	"Md5" : String,
	"Vsize" : Number,
	"Format" : String,
	"SecurityType" : String
}
```

+ **Name**  
镜像文件名。
+ **Type**  
类型。`File`或者`Dir`
+ **Size**  
文件实际大小。单位Bytes。
+ **LastModified**  
最后修改时间。Unix时间。
+ **Md5**  
文件md5值。
+ **Vsize**  
镜像文件对应磁盘大小。
+ **Format**  
文件格式。即文件后缀名。
+ **SecurityType**  
镜像上传时指定的安全网元类型。

### RepositoryACL
镜像仓库租户使用权限控制。
```
{
	"Values" : [ String ]
}
```

+ **Values**  
允许使用该仓库的租户uuid列表。  

要跨租户使用镜像仓库时，要求租户要在镜像仓库权限控制列表里。  
如果希望镜像仓库为租户私有，只需`Values`为空。  
如果不希望镜像仓库对租户做限制，只需整个RepositoryACL对象为空。  
不管什么情况，仓库所在的租户都会有该仓库的使用权限。  