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
## 虚拟机快照相关

### GET&nbsp; /v1/compute/vsd/snapshot/list
虚拟机快照列表。

<big>**请求参数**</big>  

 名称 | 参数类型 | 是否必填 | 描述
---|---|---|---
 cluster_uuid|string|是| 集群uuid
 tenant|string|否| 租户uuid。为空时，不做检查。
 compute_uuid|string|是| 虚拟机uuid
 filter_name|string|是| 过滤快照名称
 page_number|int|否| 分页序号
 page_size|int|否| 分页大小

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
	"list" : [ GetVsdSnapshotResponse ],
	"total_count" : Number
}
```

+ **total_count**  
过滤后快照总数。用于分页展示。
+ **list**  
虚拟机快照列表。见[GetVsdSnapshotResponse](#getvsdsnapshotresponse)。

<big>**示例**</big>  
**请求示例**  
```
http://10.30.33.25:8080/v1/compute/vsd/snapshot/list?cluster_uuid=650ea11b-b7fb-4269-8232-aa53865aab3b&tenant=a5badacf-a25c-4171-9aff-b619fc2d300a&compute_uuid=b6b0e5b9-dacd-432b-9b83-c3e89799009d&page_num=0&page_size=0&filter_name=
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
    "list": [
      {
        "tenant": "",
        "tenant_name": "",
        "namespace": "",
        "uuid": "60fe79cb-0fc7-4d78-a0d7-64b9a87b47d2",
        "compute_uuid": "b6b0e5b9-dacd-432b-9b83-c3e89799009d",
        "name": "origin",
        "description": "",
        "ctime": 1631166673,
        "vm_detail": null,
        "screenshot_url": "",
        "screenshot_url_ssl": "",
        "domain_remote_url": "",
        "disk_snapshot_list": [
          {
            "VolumeUuid": "3e8b046d-99a2-4a28-ba73-01c8af4d85e0",
            "SnapshotUuid": "25a949de-eaad-4f99-9bf8-b794578d8cfe",
            "DiskDrive": "sda"
          }
        ],
        "attr": null
      }
    ],
    "total_count": 1
  }
}
```

### GET&nbsp; /v1/compute/vsd/snapshot/get
虚拟机快照详细信息。

<big>**请求参数**</big>  

 名称 | 参数类型 | 是否必填 | 描述
---|---|---|---
 cluster_uuid|string|是| 集群uuid
 tenant|string|否| 租户uuid。为空时，不做检查。
 compute_uuid|string|是| 虚拟机uuid
 name|string|是| 虚拟机快照名称

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
	GetVsdSnapshotResponse
}
```

+ **GetVsdSnapshotResponse**  
虚拟机快照详细信息。见[GetVsdSnapshotResponse](#getvsdsnapshotresponse)。

<big>**示例**</big>  
**请求示例**  
```
http://10.30.33.25:8080/v1/compute/vsd/snapshot/get?cluster_uuid=650ea11b-b7fb-4269-8232-aa53865aab3b&tenant=a5badacf-a25c-4171-9aff-b619fc2d300a&compute_uuid=b6b0e5b9-dacd-432b-9b83-c3e89799009d&name=origin
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
    "tenant": "",
    "tenant_name": "",
    "namespace": "",
    "uuid": "60fe79cb-0fc7-4d78-a0d7-64b9a87b47d2",
    "compute_uuid": "b6b0e5b9-dacd-432b-9b83-c3e89799009d",
    "name": "origin",
    "description": "",
    "ctime": 1631166673,
    "vm_detail": null,
    "screenshot_url": "",
    "domain_remote_url": "",
    "disk_snapshot_list": [
      {
        "VolumeUuid": "3e8b046d-99a2-4a28-ba73-01c8af4d85e0",
        "SnapshotUuid": "25a949de-eaad-4f99-9bf8-b794578d8cfe",
        "DiskDrive": "sda"
      }
    ],
    "attr": null
  }
}
```

### GET&nbsp; /v1/compute/vsd/snapshot/tree
获取虚拟机快照树。

<big>**请求参数**</big>  

 名称 | 参数类型 | 是否必填 | 描述
---|---|---|---
 cluster_uuid|string|是| 集群uuid
 tenant|string|否| 租户uuid。为空时，不做检查。
 compute_uuid|string|是| 虚拟机uuid

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
	"tree" : VirtualMachineSnapshotTree
}
```

+ **tree**  
虚拟机快照树信息。见[VirtualMachineSnapshotTree](#virtualmachinesnapshottree)。

<big>**示例**</big>  
**请求示例**  
```
http://10.30.33.25:8080/v1/compute/vsd/snapshot/tree?cluster_uuid=650ea11b-b7fb-4269-8232-aa53865aab3b&compute_uuid=b6b0e5b9-dacd-432b-9b83-c3e89799009d&tenant=a5badacf-a25c-4171-9aff-b619fc2d300a
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
    "tree": {
      "UUID": "b6b0e5b9-dacd-432b-9b83-c3e89799009d",
      "Parents": {
        "head": "origin",
        "origin": ""
      },
      "Children": {
        "": {
          "Children": [
            "origin"
          ]
        },
        "origin": {
          "Children": [
            "head"
          ]
        }
      }
    }
  }
}
```

### GET&nbsp; /v1/compute/vsd/snapshot/head
获取虚拟机当前快照。

<big>**请求参数**</big>  

 名称 | 参数类型 | 是否必填 | 描述
---|---|---|---
 cluster_uuid|string|是| 集群uuid
 tenant|string|否| 租户uuid。为空时，不做检查。
 compute_uuid|string|是| 虚拟机uuid

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
	GetVsdSnapshotResponse
}
```

+ **GetVsdSnapshotResponse**  
虚拟机快照详细信息。见[GetVsdSnapshotResponse](#getvsdsnapshotresponse)。

<big>**示例**</big>  
**请求示例**  
```
http://10.30.33.25:8080/v1/compute/vsd/snapshot/head?cluster_uuid=650ea11b-b7fb-4269-8232-aa53865aab3b&compute_uuid=b6b0e5b9-dacd-432b-9b83-c3e89799009d&tenant=a5badacf-a25c-4171-9aff-b619fc2d300a
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
    "tenant": "",
    "tenant_name": "",
    "namespace": "",
    "uuid": "60fe79cb-0fc7-4d78-a0d7-64b9a87b47d2",
    "compute_uuid": "b6b0e5b9-dacd-432b-9b83-c3e89799009d",
    "name": "origin",
    "description": "",
    "ctime": 1631166673,
    "vm_detail": null,
    "screenshot_url": "",
    "domain_remote_url": "",
    "disk_snapshot_list": [
      {
        "VolumeUuid": "3e8b046d-99a2-4a28-ba73-01c8af4d85e0",
        "SnapshotUuid": "25a949de-eaad-4f99-9bf8-b794578d8cfe",
        "DiskDrive": "sda"
      }
    ],
    "attr": null
  }
}
```

### POST&nbsp; /v1/compute/vsd/snapshot/create
创建虚拟机快照。

<big>**请求参数**</big>  
```
{
	ComputeIdentifier,
	"name" : String,
	"description" : String,
	"domain_memory" : Bool
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **name**  
虚拟机快照名称。  
_必需_ ： 是  
+ **description**  
虚拟机快照描述。  
_必需_ ： 否  
+ **domain_memory**  
是否创建内存快照。  
_必需_ ： 否  

创建虚拟机快照要求磁盘只有内置存储磁盘或共享存储磁盘。  
`domain_memory=true`时，要求虚拟机处于运行状态，且租户开启内存快照空间。该接口将内存数据保存到文件并上传到特定路径，回滚快照时可同时拉起虚拟机至保存的运行状态。在数据保存、上传完以前，该快照不可用。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"b6b0e5b9-dacd-432b-9b83-c3e89799009d","compute_name":"test-templ","name":"temp","description":"","domain_memory":false}
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

### POST&nbsp; /v1/compute/vsd/snapshot/modify
修改虚拟机快照。

<big>**请求参数**</big>  
```
{
	ComputeIdentifier,
	"name" : String,
	"description" : String
}
```
+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **name**  
指定虚拟机快照名称。  
_必需_ ： 是  
+ **description**  
修改后的虚拟机快照描述。  

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"b6b0e5b9-dacd-432b-9b83-c3e89799009d","compute_name":"test-templ","name":"temp","description":"desc"}
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

### POST&nbsp; /v1/compute/vsd/snapshot/rollback
虚拟机快照回滚。

<big>**请求参数**</big>  
```
{
	ComputeIdentifier,
	"name" : String,
	"domain_memory" : Bool
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **name**  
虚拟机快照名称。  
_必需_ ： 是  
+ **domain_memory**  
是否使用内存快照。有内存快照的虚拟机快照，会在回滚后拉起虚拟机至保存快照时的运行状态。    
_必需_ ： 否  

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
	GetVsdSnapshotResponse
}
```
<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"b6b0e5b9-dacd-432b-9b83-c3e89799009d","compute_name":"test-templ","name":"origin","domain_memory":false}
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
  }
}
```

### POST&nbsp; /v1/compute/volume/snapshot/rollback
单独回滚虚拟机磁盘至特定快照。

<big>**请求参数**</big>  
```
{
	ComputeIdentifier,
	"disk_snapshot_list" : [ DiskSnapshotInfo ]
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **disk_snapshot_list**  
要回滚的虚拟机磁盘快照参数。见[DiskSnapshotInfo](#disksnapshotinfo)。

该接口要求虚拟机处于关机状态。  
该接口只回滚磁盘数据，不对虚拟机配置做回滚。  

<big>**返回数据**</big>  
接口返回数据先使用[BatchOutput](#batchoutput)封装，再用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
	DiskSnapshotInfo
}
```

+ **DiskSnapshotInfo**  
标识操作的虚拟机磁盘。和请求参数一致。

<big>**示例**</big>  
**请求示例**  
无

**返回示例**  
无

### POST&nbsp; /v1/compute/vsd/snapshot/delete
删除虚拟机快照。

<big>**请求参数**</big>  
```
{
	ComputeIdentifier,
	"name" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **name**  
虚拟机快照名称。  
_必需_ ： 是  

删除的快照要求不能有多个子快照。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"b6b0e5b9-dacd-432b-9b83-c3e89799009d","compute_name":"test-templ","name":"temp"}
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

## 虚拟机快照相关
### DiskSnapshotInfo
虚拟机快照对应磁盘快照信息。
```
{
	"VolumeUuid" : String,
	"SnapshotUuid" : String,
	"DiskDrive" : String
}
```

+ **VolumeUuid**  
磁盘卷uuid。
+ **SnapshotUuid**  
该快照中该磁盘对应的卷快照uuid。
+ **DiskDrive**  
磁盘卷磁盘类型。

### GetVsdSnapshotResponse
虚拟机快照详细信息。
```
{
	TenantIdentifier,
	"namespace" : String,
	"uuid" : String,
	"compute_uuid" : String,
	"name" : String,
	"description" : String,
	"ctime" : Number,
	"vm_detail" : ComputeInspectInfo,
	"screenshot_url" : String,
	"domain_remote_url" : String,
	"disk_snapshot_list" : [ DiskSnapshotInfo ],
	"attr" : {
		String : String
	}
}
```

+ **TenantIdentifier**  
虚拟机快照所在租户信息。
+ **namespace**  
虚拟机快照所在命名空间uuid。
+ **uuid**  
虚拟机快照uuid。
+ **compute_uuid**  
虚拟机快照对应虚拟机uuid。
+ **name**  
虚拟机快照名称。
+ **description**  
虚拟机快照描述。
+ **ctime**  
虚拟机快照创建时间。Unix时间。
+ **vm_detail**  
虚拟机快照记录的虚拟机详细配置。见[ComputeInspectInfo](compute.md#computeinspectinfo)。
+ **screenshot_url**  
虚拟机快照记录内存快照屏幕截图url。
+ **disk_snapshot_list**  
虚拟机快照对应磁盘快照信息。见[DiskSnapshotInfo](#disksnapshotinfo)。
+ **attr**  
其他属性。

### VirtualMachineSnapshotTree
虚拟机快照树信息。
```
{
	"UUID" : String,
	"Parents" : {
		String : String
	},
	"Children" : {
		String : {
			"Children" : [ String ]
		}
	}
}
```

+ **UUID**  
虚拟机uuid。
+ **Parents**  
虚拟机快照对应父快照。键为快照名，值为该快照对应父快照名称。
+ **Children**  
虚拟机快照对应子快照。键为快照名，值为该快照对应全部子快照名称。

