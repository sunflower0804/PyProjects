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
## 虚拟机备份相关

### GET&nbsp; /v1/compute/backup/list
虚拟机备份列表。

<big>**请求参数**</big>  

 名称 | 参数类型 | 是否必填 | 描述
---|---|---|---
 cluster_uuid|string|否| 集群uuid
 tenant|string|否| 租户uuid
filter_vm_uuid|string|否 | 特定虚拟机uuid
filter_backup_name|string|否 | 过滤虚拟机备份名
filter_backup_point_uuid|string|否 | 过滤备份点uuid
filter_backup_description|string|否 | 过滤虚拟机备份描述
start_time|int|否 | 过滤晚于start_time的虚拟机备份，unix时间
end_time|int|否 | 过滤早于end_time的虚拟机备份，unix时间
 page_number|int|否| 分页序号
 page_size|int|否| 分页大小

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
    "list" : [ ComputeBackupBaseInfo ],
    "total_count" : Number,
    "each_range_list_state" : [ EachResourceRangeListState ]
}
```

+ **list**  
虚拟机备份信息列表。 见[ComputeBackupBaseInfo](#computebackupbaseinfo)。  
+ **total_count**  
满足过滤条件的虚拟机备份总数。用于展示分页结果。
+ **each_range_list_state**  
每个集群、命名空间的查询结果统计。

<big>**示例**</big>  
**请求示例**  
```
http://10.30.33.25:8080/v1/compute/backup/list?cluster_uuid=650ea11b-b7fb-4269-8232-aa53865aab3b&tenant=a5badacf-a25c-4171-9aff-b619fc2d300a&filter_vm_uuid=b6b0e5b9-dacd-432b-9b83-c3e89799009d&filter_backup_name=&filter_backup_description=&start_time=0&end_time=0&page_num=0&page_size=10
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
    "list": [],
    "total_count": 0,
    "each_range_list_state": [
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
        "total_count": 0
      }
    ]
  }
}
```

### GET&nbsp; /v1/compute/backup/inspect
虚拟机备份详情。

<big>**请求参数**</big>  

 名称 | 参数类型 | 是否必填 | 描述
---|---|---|---
 cluster_uuid|string|否| 集群uuid
 tenant|string|否| 租户uuid
backup_uuid|string|是| 备份uuid

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
    ComputeBackupBaseInfo
}
```

+ **ComputeBackupBaseInfo**  
虚拟机备份信息。 见[ComputeBackupBaseInfo](#computebackupbaseinfo)。 

<big>**示例**</big>  
**请求示例**  
```
http://10.30.33.25:8080/v1/compute/backup/list?cluster_uuid=650ea11b-b7fb-4269-8232-aa53865aab3b&tenant=8aeb88f1-b894-4fae-99e8-e3c2434ec346&backup_uuid=e6568a55-f381-4cc0-8f82-19f2ad0b9ae4
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
    "tenant": "8aeb88f1-b894-4fae-99e8-e3c2434ec346",
    "tenant_name": "gg_tenant",
    "cluster_uuid": "650ea11b-b7fb-4269-8232-aa53865aab3b",
    "cluster_name": "host3222-cvm3322",
    "namespace": "f9b86aba-3daf-426a-8f12-3a7cbd30628e",
    "uuid": "e6568a55-f381-4cc0-8f82-19f2ad0b9ae4",
    "compute_uuid": "9cfe5e48-a677-424d-8ed2-f7f791d50dd2",
    "compute_name": "gg_ubuntu",
    "backup_point_uuid": "16eda2b2-7859-4576-b3a0-1c54d479086a",
    "backup_point_name": "gg_nfs_202197",
    "name": "cdp_b180eeef-c02c-4748-9903-2c06fd3e26b7_vm_9cfe5e48-a677-424d-8ed2-f7f791d50dd2_2021-09-08 15:30:25",
    "description": "CDP策略自动生成备份",
    "create_time": 1631086225,
    "status": 0,
    "disks": [
      {
        "target_device": "sda",
        "backup_uuid": "f48296c3-5f41-4c52-8ec5-442ffbc5dfe3",
        "capacity": 5368709120,
        "replica": 1,
        "share": false
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/backup/create
虚拟机创建备份。

<big>**请求参数**</big>  
```
{
    CommonClusterTenantScope,
    "backup_point_uuid" ： String,
    "compute_uuid" : String,
    "backup_name" : String,
    "description" : String,
    "full_backup" : Bool
}
```

+ **CommonClusterTenantScope**  
指定集群和租户。见[CommonClusterTenantScope](#commonclustertenantscope)。  
_必需_ ： 是  
+ **backup_point_uuid**  
备份使用备份点uuid。  
_必需_ ： 是  
+ **compute_uuid**  
备份虚拟机uuid。  
_必需_ ： 是  
+ **backup_name**  
虚拟机备份名称。  
_必需_ ： 是  
+ **description**  
虚拟机备份描述。  
_必需_ ： 否  
+ **full_backup**  
是否全量备份。`true`：全量备份，`false`：增量备份。  
_必需_ ： 否  


<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
    "backup_uuid" : String
}
```

+ **backup_uuid**  
生成的虚拟机备份uuid。

接口正常返回时，仅备份的元数据创建完成，虚拟机进入备份中动作，备份进入备份中状态。实际数据备份是异步的。备份完成虚拟机动作、备份状态均自动改变。

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"b6b0e5b9-dacd-432b-9b83-c3e89799009d","backup_point_uuid":"281db4b0-c8ea-413a-9e93-64f47d7c952e","backup_name":"test-api","description":"","full_backup":true}
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
    "backup_uuid" : "7cfb9378-71ef-4011-9e70-3544a0038137"
  }
}
```

### POST&nbsp; /v1/compute/backup/delete
删除虚拟机备份。

<big>**请求参数**</big>  
```
{
    CommonClusterTenantScope,
    "backup_uuid" : String,
    "backup_name" : String
}
```

+ **CommonClusterTenantScope**  
指定集群和租户。见[CommonClusterTenantScope](#commonclustertenantscope)。  
_必需_ ： 是  
+ **backup_uuid**  
要删除的备份uuid。  
_必需_ ： 是  
+ **backup_name**  
要删除的备份名称。只用来记录操作日志。  
_必需_ ： 否  

删除虚拟机备份会同步删除备份点上的对应备份数据。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"b6b0e5b9-dacd-432b-9b83-c3e89799009d","backup_uuid":"7cfb9378-71ef-4011-9e70-3544a0038137","backup_name":"test-api"}
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

### POST&nbsp; /v1/compute/backup/restore
虚拟机备份恢复。

<big>**请求参数**</big>  
```
{
    CommonClusterTenantScope,
    "backup_uuid" : String,
    "backup_name" : String,
    "new_vm_name" : String,
    "restore_disks" : [ ComputeBackupRestoreDisk ],
    "object_group" : String,
    "zone_uuid" : String
}
```

+ **CommonClusterTenantScope**  
指定集群和租户。见[CommonClusterTenantScope](#commonclustertenantscope)。  
_必需_ ： 是  
+ **backup_uuid**  
要恢复的虚拟机备份uuid。  
_必需_ ： 是  
+ **backup_name**  
要恢复的虚拟机备份名称。只用来记录操作日志。  
_必需_ ： 否  
+ **new_vm_name**  
恢复后的虚拟机名称。  
_必需_ ： 是  
+ **restore_disks**  
恢复虚拟机的磁盘参数。见[ComputeBackupRestoreDisk](#computebackuprestoredisk)。  
_必需_ ： 是  
+ **object_group**  
恢复后的虚拟机分组。  
_必需_ ： 是  
+ **zone_uuid**  
恢复后的虚拟机资源池。  
_必需_ ： 是  

<a id="computebackuprestoredisk"></a>
**ComputeBackupRestoreDisk**  
```
{
    "target_device" : String,
    "pool_uuid" : String,
    "volume_name" : String,
    "usd_type" : String
}
```

+ **target_device**  
指定恢复磁盘的盘符。  
_必需_ ： 是  
+ **pool_uuid**  
恢复磁盘的存储池。  
_必需_ ： 是  
+ **volume_name**  
恢复磁盘的卷名称。  
_必需_ ： 是  
+ **usd_type**  
恢复磁盘使用的磁盘类型。  
_必需_ ： 是  

虚拟机备份恢复会创建出一台全新的虚拟机，并且备份数据恢复到磁盘上。即使备份是由当前集群当前仍存在的虚拟机生成的，也是生成一台全新虚拟机，而原虚拟机不受影响。  

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

虚拟机备份恢复是异步操作，接口正常返回只代表虚拟机被正常创建出来，数据恢复成功发起，虚拟机进入恢复中状态。需要等实际数据恢复完成，虚拟机状态自动改变。

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"bdc01c45-973c-4b7b-a565-7a03c74379e4","tenant":"","backup_uuid":"71779ff5-9e8d-4d37-a085-b3ce540de072","compute_uuid":"e3174e1d-bc9b-4fe5-8d4c-8d4245ff9a1a","compute_name":"","object_group":"f6e13b23-ce72-427b-98e6-99b10a78b4f4","new_vm_name":"test-restore","zone_uuid":"b9652fb7-f399-4826-a26c-aa5b4183183b","restore_disks":[{"target_device":"sda","pool_uuid":"965588d9-1ef9-4e32-b4da-57ea47dd4326","volume_name":"restore-1","usd_type":"HDD"}]}
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

### GET&nbsp; /v1/compute/backup/remote/list
虚拟机备份远端列表。

<big>**请求参数**</big>  

 名称 | 参数类型 | 是否必填 | 描述
---|---|---|---
 cluster_uuid|string|是| 集群uuid
 backuppoint_uuid|string|时| 备份点uuid
 page_number|int|否| 分页序号
 page_size|int|否| 分页大小

该接口查询备份点上的全部虚拟机备份，包括不是由该超融合集群创建的备份。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
    "total_count" : Number,
    "backups" : [ ComputeRemoteBackup ],
    "vm_infos" : {
        String : BackupVmInfo
    }
}
```

+ **total_count**  
查询到的虚拟机备份数量。用于分页展示。
+ **backups**  
虚拟机备份详细信息列表。见[ComputeRemoteBackup](#computeremotebackup)。
+ **vm_infos**  
虚拟机信息。展示备份涉及到的虚拟机信息。见[BackupVmInfo](#backupvminfo)。

<big>**示例**</big>  
**请求示例**  
无

**返回示例**  
无

### POST&nbsp; /v1/compute/backup/remote/import
从远端导入虚拟机备份。

<big>**请求参数**</big>  
```
{
    "cluster_uuid" : String,
    "backup" : [ ComputeVmBackup ]
}
```  

+ **cluster_uuid**  
指定集群uuid。  
_必需_ ： 是  
+ **backup**  
指定待导入虚拟机备份。
_必需_ ： 是  

该接口允许将指定备份点的虚拟机备份添加进集群，无论备份是否由该集群产生的。  

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
    "backups" : [ ComputeRemoteBackup ],
    "vm_infos" : {
        String : BackupVmInfo
    }
}
```

+ **backups**  
导入的虚拟机备份信息列表。见[ComputeRemoteBackup](#computeremotebackup)。
+ **vm_infos**  
虚拟机信息。展示备份涉及到的虚拟机信息。见[BackupVmInfo](#backupvminfo)。

<big>**示例**</big>  
**请求示例**  
无

**返回示例**  
无


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

## 虚拟机备份相关
### ComputeRemoteBackup
虚拟机备份信息。
```
{
	ComputeVmBackup,
	ClusterIdentifier
}
```

+ **ComputeVmBackup**  
备份元数据。见[ComputeVmBackup](#computevmbackup)。
+ **ClusterIdentifier**  
备份所在集群。见[ClusterIdentifier](#clusteridentifier)。

### BackupVmInfo
虚拟机备份涉及虚拟机信息。
```
{
	"Name" : String
}
```

+ **Name** 
相关虚拟机当前名称。

### ComputeBackupBaseInfo
虚拟机备份信息。
```
{
    ClusterIdentifier,
    TenantIdentifier,
    "uuid" : String,
    "compute_uuid" : String,
    "compute_name" : String,
    "backup_point_uuid" : String,
    "backup_point_name" : String,
    "name" : String,
    "description" : String,
    "create_time" : Number,
    "status" : Number,
    "disks" : [ ComputeDiskBackups ]
}
```

+ **ClusterIdentifier**  
虚拟机备份所在集群。
+ **TenantIdentifier**  
虚拟机备份所在租户。
+ **uuid**  
虚拟机备份uuid。
+ **compute_uuid**  
备份虚拟机uuid。
+ **compute_name**  
备份虚拟机名称。
+ **backup_point_uuid**  
备份点uuid。
+ **backup_point_name**  
备份点名称。
+ **name**  
虚拟机备份名称。
+ **description**  
虚拟机备份描述。
+ **create_time**  
虚拟机备份创建时间。Unix时间。
+ **status**  
虚拟机备份状态。`0`：备份成功，`1`：备份中，`2`：备份失败。
+ **disks**  
虚拟机备份磁盘信息。见[ComputeDiskBackups](#computediskbackups)。

### ComputeDiskBackups
```
{
    "target_device" : String,
    "backup_uuid" : String,
    "capacity" : Number,
    "replica" : Number,
    "share" : Bool
}
```

+ **target_device**  
备份的虚拟机磁盘盘符。
+ **backup_uuid**  
虚拟机磁盘卷备份uuid。
+ **capacity**  
虚拟机磁盘卷容量。单位Bytes。
+ **replica**  
虚拟机磁盘卷副本数。
+ **share**  
虚拟机磁盘卷是否是共享卷。

### ComputeVmBackup
虚拟机备份元数据。
```
{
	"UUID" : String,
	"NsUUID" : String,
	"VmUUID" : String,
	"BpUUID" : String,
	"Name" : String,
	"Desc" : String,
	"Ctime" : Number,
	"DiskBackups" : {
		String : ComputeVmBackupDiskInfo
	},
	"Status" : Number,
	"Filename" : String,
	"ExpiredTime" : Number
}
```

+ **UUID**  
虚拟机备份uuid。
+ **NsUUID**  
虚拟机命名空间uuid。
+ **VmUUID**  
生成备份的虚拟机uuid。
+ **BpUUID**  
备份点uuid。
+ **Name**  
虚拟机备份名称。
+ **Desc**  
虚拟机备份描述。
+ **Ctime**  
虚拟机备份创建时间。Unix时间。
+ **DiskBackups**  
虚拟机备份对应磁盘备份信息。见[ComputeVmBackupDiskInfo](#computevmbackupdiskinfo)。
+ **Status**  
虚拟机备份状态。`0`：备份成功，`1`：备份中，`2`：备份失败。
+ **Filename**  
虚拟机备份对应文件名。
+ **ExpiredTime**  
虚拟机备份过期时间。Unix时间。

### ComputeVmBackupDiskInfo
虚拟机备份磁盘备份信息。
```
{
	"BackupUUID" ： String,
	"Capacity" : Number,
	"Replica" ： Number,
	"VolSnapUUID" : String,
	"share" : Bool
}
```

+ **BackupUUID**  
虚拟机磁盘卷备份uuid。
+ **Capacity**  
虚拟机磁盘卷容量。单位Bytes。
+ **Replica**  
虚拟机磁盘卷副本数。
+ **VolSnapUUID**  
虚拟机磁盘卷备份用快照uuid。
+ **share**  
虚拟机磁盘卷是否是共享卷。
