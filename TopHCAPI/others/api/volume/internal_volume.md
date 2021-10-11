[back to api overview](../api_overview.md#label_api)
### 融合存储卷(内置卷)相关接口
## /v1/volume/internal/list
内置卷列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|否|-|租户uuid
filter_fuzzy|string|否|-|过滤卷名称、卷uuid、卷状态、资源池名称
filter_mount_type|int|否|-|过滤未挂载/已挂载的卷（1：已挂载；2：未挂载）
filter_dev_type|string|否|-|过滤设备类型，不同类型间用＠分隔（block:SCSI设备；target:iSCSI　Target设备；nfs：共享设备nfs；smb：共享设备smb；hdfs：共享设备HDFS；rest：共享设备rest;s3：共享设备s3；swift：共享设备swift）
no_detail|bool|否|-|是否显示卷所有数据
page_num|int|否|0|第几页
page_size|int|否|0|每页数据条数

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.213:8080/v1/volume/internal/list?tenant=76373db8-e98d-4ad5-a373-9e9e4cd6048e&filter_name=volume-1107141532&page_num=0&page_size=10&no_detail=true&filter_mount_type=0&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
```


#### 正常返回示例
```
{
  "message": "success",
  "message_cn": "成功",
  "scode": 0,
  "desc": "",
  "stack": null,
  "data": {
    "List": [
      {
        "Namespace": "aa425e94-35aa-4642-9bda-4eb2e3f72913",
        "Pool": "c37429d5-471d-47d4-b18d-b863de5d63f6",
        "Name": "volume-0423100604",
        "UUID": "4a486475-ca43-429a-8acc-fdc59d93977c",
        "Capacity": 1073741824,
        "SnapCapacity": 3221225472,
        "SliceSize": 1073741824,
        "Status": 1,
        "Vendor": "",
        "Replicas": null,
        "RW": null,
        "RO": null,
        "AccessPath": {
          "55c94054-baa1-4882-b1bf-2825b334c92a": "/dev/sdn"
        },
        "InvalidAccessPath": null,
        "Accounts": null,
        "Attr": {
          "55c94054-baa1-4882-b1bf-2825b334c92a_VSD_PORT": "40799",
          "ComponentSetShift": "0",
          "ComponentShift": "30",
          "DataType": "replica",
          "DelMode": "default",
          "DevType": "share",
          "DriveType": "HDD",
          "Encrypto": "off",
          "InitFS": "false",
          "ReadBytesLimit": "0",
          "ReadIOPSLimit": "",
          "RestPort": "28000",
          "RestSSLPort": "28443",
          "Safety": "first",
          "ScheduleOption": "intelligent",
          "SetRelated": "false",
          "ShareMountable": "false",
          "ShareType": "rest",
          "StripeShift": "17",
          "TargetID": "1",
          "ThinProvision": "on",
          "VmCache": "none",
          "VolumeName": "volume-0423100604",
          "WriteBytesLimit": "0",
          "WriteIOPSLimit": "",
          "Zone": "a0692d7b-1c8c-410a-b79c-fd5a6faca569",
          "ZoneName": "default",
          "replica": "1"
        },
        "UserPerms": null,
        "UserGroupPerms": null,
        "SharePoint": {
          "rest": "/4a486475-ca43-429a-8acc-fdc59d93977c/data"
        },
        "Ctime": 1587607541,
        "EventState": 0,
        "Label": null,
        "DeletedTime": 0,
        "PoolName": "pool_1",
        "FinishPercent": 0,
        "VsdState": {
          "55c94054-baa1-4882-b1bf-2825b334c92a": 0
        },
        "SnapLength": 0,
        "vReplicaHost": null,
        "used": 29360128,
        "tenant_name": "zhanghai",
        "tenant": "aa425e94-35aa-4642-9bda-4eb2e3f72913",
        "owner_name": "",
        "owner": "",
        "owner_is_ldap": false
      }
    ],
    "TotalCount": 1
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/internal/max_replica
融合存储卷最大副本数
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
zone_uuid|string|是|-|子集群uuid
tenant|string|是|-|租户uuid
drive_type|string|是|-|SSD,HDD可选


### 返回参数

名称|参数类型|描述
---|---|---
total_count|int|最大副本数

### 示例

#### 请求示例
```
http://192.168.201.213:8080/v1/volume/internal/list?tenant=76373db8-e98d-4ad5-a373-9e9e4cd6048e&filter_name=volume-1107141532&page_num=0&page_size=10&no_detail=true&filter_mount_type=0&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
    "total_count": 3
  }
}
```

#### 异常返回示例

### 状态码




## /v1/volume/internal/get
内置卷详情
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
volume_uuid|string|是|-|卷uuid
no_detail|bool|否|-|是否获取所有数据,如果获取所有数据可能有点耗时

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.213:8080/v1/volume/internal/get?volume_uuid=768d5ddb-4a5e-462f-9274-2340534f6ae7&tenant=76373db8-e98d-4ad5-a373-9e9e4cd6048e&no_detail=true&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
```


#### 正常返回示例
```
{
  "message": "success",
  "message_cn": "成功",
  "scode": 0,
  "desc": "",
  "stack": null,
  "data": {
    "total_count": 1,
    "volume": {
      "Namespace": "d1b0742d-7a6a-4409-9076-0bf8aac63087",
      "Pool": "e7b322b9-d03d-4952-bd86-74e2f9827e48",
      "Name": "tttt-volume1",
      "UUID": "b4e03742-4d19-4505-844d-7d8e7857723d",
      "Capacity": 1073741824,
      "SnapCapacity": 3221225472,
      "SliceSize": 1073741824,
      "Status": 1,
      "Vendor": "",
      "Replicas": null,
      "RW": null,
      "RO": null,
      "AccessPath": null,
      "InvalidAccessPath": null,
      "Accounts": null,
      "Attr": {
        "ComponentSetShift": "0",
        "ComponentShift": "30",
        "DataType": "replica",
        "DelMode": "default",
        "DevType": "target",
        "DriveType": "HDD",
        "InitFS": "false",
        "Safety": "first",
        "ScheduleOption": "intelligent",
        "ShareMountable": "true",
        "StripeShift": "20",
        "ThinProvision": "on",
        "VirtualMachine": "a68ec6f0-2c6c-4fc5-a37c-f01a4bd9eb48",
        "VirtualMachineName": "tttt-template-0415160216",
        "VirtualMachineTemplate": "yes",
        "VolumeName": "tttt-volume1",
        "Zone": "64864753-88a2-4020-8627-bf055964b4d8",
        "ZoneName": "default",
        "replica": "2"
      },
      "UserPerms": null,
      "UserGroupPerms": null,
      "SharePoint": null,
      "Ctime": 1586937724,
      "EventState": 0,
      "Label": null,
      "DeletedTime": 0,
      "PoolName": "xzh",
      "FinishPercent": 0,
      "VsdState": null,
      "SnapLength": 0,
      "vReplicaHost": null,
      "used": 0,
      "tenant_name": "xzh",
      "tenant": "d1b0742d-7a6a-4409-9076-0bf8aac63087",
      "owner_name": "",
      "owner": "",
      "owner_is_ldap": false
    }
  }
}
```

#### 异常返回示例

### 状态码

## /v1/volume/internal/create
融合存储卷添加
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
count|int|是|-|添加卷的个数(用于批量添加)
volume_name|string|是|-|卷名称
capacity|uint64|是|-|卷容量,单位字节
snap_capacity|uint64|是|-|卷快照容量,单位字节;一般为卷容量的3倍
pool_uuid|string|是|-|存储池uuid
tenant|string|是|-|租户uuid
cluster_uuid|string|是|-|集群uuid
attribute|map object|是|-|卷属性字典对
hosts|[]string|否|-|主机数组,填入一个宿主机uuid

### attribute对象

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
DevType|string|是|-|设备类型;block,target可选,分别表示SCSI块设备,iSCSI Target;
DataType|string|是|-|数据类型;replica可选,表示副本;
Safety|string|是|-|安全级别（first：弱一致,second：最终一致；third：强一致）
ChecksumData|string|否|false|是否开启数据校验（true：开启；false：关闭）
ChecksumHeader|string|否|false|是否开启头部校验（true：开启；false：关闭）
DriveType|string|是|-|存储介质（HDD：机械硬盘；SSD：固态硬盘）
Encrypto|string|否|off|是否加密（on:加密；off:不加密）
ReadBytesLimit|string|否|""|读带宽限制
ReadIOPSLimit|string|否|""|读IOPS限制
ScheduleOption|string|否|-|调度（intelligent：智能选择；performance：性能优先）
Sector|string|是|-|扇区大小
ThinProvision|string|否|on|开启精简配置（on:开启；off:关闭）
VsdVendor|string|否|-|云盘类型（LIBTARGET：普通云盘1.0；TCMURUNNER；普通云盘2.0；LIBTARGETMP：高效云盘）
WriteBytesLimit|string|否|""|写带宽限制
WriteIOPSLimit|string|否|""|写IOPS限制
Zone|string|是|-|资源池uuid
ZoneName|string|是|-|资源池名称
replica|string|否|-|副本数



### 返回参数

名称|参数类型|描述
---|---|---
volume_uuid|string|卷uuid
volume_name|string|卷名称

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/create
```
Body:
```
{
	"count": 1,
	"volume_name": "volume-0824145216",
	"capacity": 1073741824,
	"snap_capacity": 3221225472,
	"pool_uuid": "75b47132-ed52-4739-bcf4-88f8b9687d90",
	"tenant": "b5be02e1-e146-4168-84cc-5e0dda85c22b",
	"attribute": {
		"DevType": "block",
		"DataType": "replica",
		"Safety": "first",
		"Encrypto": "off",
		"VsdVendor": "LIBTARGET",
		"DriveType": "HDD",
		"ThinProvision": "on",
		"ReadIOPSLimit": "",
		"WriteIOPSLimit": "",
		"ReadBytesLimit": "",
		"WriteBytesLimit": "",
		"VmCache": "none",
		"ScheduleOption": "intelligent",
		"Zone": "5170b980-8312-4d72-8abf-5a56d8351b5c",
		"ZoneName": "default",
		"ChecksumHeader": "off",
		"ChecksumData": "off",
		"Sector": "512",
		"replica": "2",
		"ComponentSetShift": "0",
		"ComponentShift": "30",
		"StripeShift": "20"
	},
	"cluster_uuid": "462601ce-727e-4c2f-ab45-6123dd3951cd"
}
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "messageCn": "",
  "stack": null,
  "data": {
    "success": 1,
    "fail": 0,
    "results": [
      {
        "scode": 0,
        "desc": "",
        "message": "success",
        "message_cn": "成功",
        "messageCn": "",
        "stack": null,
        "data": {
          "volume_uuid": "18fbdcff-2fee-49e2-af8e-f300f64c9df4",
          "volume_name": "volume-1107192432-0112"
        }
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码

## /v1/volume/internal/delete
内置卷删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
real_delete|bool|否|false|是否彻底删除（true：彻底删除；false：一般删除）
tenant|string|是|-|租户uuid
volume_name|string|是|-|租户uuid
volume_uuid|string|是|-|卷uuid


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/delete
```
Body:
```
{
	"tenant": "8b69bb2f-2a6e-4149-9f43-8d2e2b780df1",
	"volume_name": "volume-1107192432-0112",
	"volume_uuid": "18fbdcff-2fee-49e2-af8e-f300f64c9df4",
	"real_delete": true,
	"cluster_uuid": "b088822c-1176-4c79-9df7-5fad80c7fd1d"
}
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "messageCn": "",
  "stack": null,
  "data": {
    "volume": {
      "tenant": "",
      "name": "",
      "uuid": "",
      "pool": "",
      "namespace": "",
      "capacity": 0,
      "snap_capacity": 0,
      "status": 0,
      "ctime": 0,
      "flag": 0
    }
  }
}
```

#### 异常返回示例

### 状态码



## /v1/volume/internal/batch_delete
内置卷批量删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
real_delete|bool|否|false|是否彻底删除（true：彻底删除；false：一般删除）
volumes|object|是|-|卷信息

### volumes

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
volume_uuid|string|是|-|卷uuid
volume_name|string|是|-|卷名称


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/batch_delete
```
Body:
```
{
	"volumes": [
		{
			"cluster_uuid": "462601ce-727e-4c2f-ab45-6123dd3951cd",
			"tenant": "b5be02e1-e146-4168-84cc-5e0dda85c22b",
			"volume_uuid": "35a0779b-2e39-48df-9e64-46e0e52be3e2",
			"volume_name": "volume-0824111205"
		},
		{
			"cluster_uuid": "462601ce-727e-4c2f-ab45-6123dd3951cd",
			"tenant": "b5be02e1-e146-4168-84cc-5e0dda85c22b",
			"volume_uuid": "76ca3e46-2d09-4fc5-9a57-5c7c63bfea11",
			"volume_name": "test"
		}
	],
	"real_delete": true,
	"cluster_uuid": "462601ce-727e-4c2f-ab45-6123dd3951cd"
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
    "success": 2,
    "fail": 0,
    "results": [
      {
        "scode": 0,
        "desc": "",
        "message": "success",
        "message_cn": "成功",
        "stack": null,
        "data": {
          "cluster_uuid": "462601ce-727e-4c2f-ab45-6123dd3951cd",
          "cluster_name": "超融合集群A",
          "cluster_mode": "",
          "tenant": "b5be02e1-e146-4168-84cc-5e0dda85c22b",
          "tenant_name": "",
          "multiple": false,
          "vm_type": "",
          "volume_uuid": "76ca3e46-2d09-4fc5-9a57-5c7c63bfea11",
          "volume_name": "test",
          "owner": ""
        }
      },
      {
        "scode": 0,
        "desc": "",
        "message": "success",
        "message_cn": "成功",
        "stack": null,
        "data": {
          "cluster_uuid": "462601ce-727e-4c2f-ab45-6123dd3951cd",
          "cluster_name": "超融合集群A",
          "cluster_mode": "",
          "tenant": "b5be02e1-e146-4168-84cc-5e0dda85c22b",
          "tenant_name": "",
          "multiple": false,
          "vm_type": "",
          "volume_uuid": "35a0779b-2e39-48df-9e64-46e0e52be3e2",
          "volume_name": "volume-0824111205",
          "owner": ""
        }
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/internal/create/from_replica
内置卷从副本中创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TODO


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/create/from_replica
```
Body:
```
{
	"fromVolUUID": "bcb6ba4d-73a5-4d8a-aba3-ea85d10b583a",
	"fromVolRid": 0,
	"newVolumePoolUUID": "cb29e13f-152a-4aed-94c9-e5bfe594eff7",
	"newVolumeName": "ccc",
	"Accounts": [
		{
			"username": "volume_user",
			"password": "111111111111",
			"devType": "target",
			"flag": 1,
			"outgoing": false
		}
	],
	"HostUUID": null,
	"Capacity": 1073741824,
	"SnapCapacity": 3221225472,
	"MapHostCount": 0,
	"CreateOption": {
		"Hosts": {
			"Host": null
		},
		"Label": {
			"selectors": null
		}
	},
	"attr": {
		"ComponentSetShift": "0",
		"ComponentShift": "30",
		"DataType": "replica",
		"DelMode": "default",
		"DevType": "target",
		"DriveType": "HDD",
		"Encrypto": "off",
		"InitFS": "false",
		"ReadBytesLimit": "0",
		"ReadIOPSLimit": "3",
		"ReadOnly": "on",
		"Safety": "first",
		"ScheduleOption": "intelligent",
		"StripeShift": "17",
		"TargetACL": "1.1.1.1",
		"ThinProvision": "off",
		"VmCache": "none",
		"VolumeName": "volume-1108102056",
		"WriteBytesLimit": "0",
		"WriteIOPSLimit": "0",
		"replica": "2",
		"linearShift": "0",
		"linearNum": "17"
	},
	"cluster_uuid": "b8205835-ee82-4aa0-8c8b-6269e85aabd5"
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

#### 异常返回示例

### 状态码


## /v1/volume/internal/info/update
内置卷编辑
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-|集群uuid
 tenant|string|是|-|租户uuid
 volume_uuid|string|是|-|卷uuid
 volume_name|string|是|-|原卷名称
 volume_new_name|string|是|-|新卷名称
 volume_attribute_safety|string|否|-|安全级别，不传代表不修改该属性（first：弱一致;second：最终一致；third：强一致）
 volume_attribute_header_check|string|否|-|是否开启头部校验，不传代表不修改该属性（true：开启；false：关闭）
 volume_attribute_data_check|string|否|-|是否开启数据校验，不传代表不修改该属性（true：开启；false：关闭）
 volume_attribute_sector|string|否|-|扇区大小，不传代表不修改该属性
 snap_capacity|uint64|否|-|快照容量大小，不传代表不修改该属性
 
### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/info/update
```
Body:
```
{
	"tenant": "b3c011b0-6e4a-487e-b9af-022f869dc790",
	"volume_uuid": "bcb6ba4d-73a5-4d8a-aba3-ea85d10b583a",
	"volume_name": "volume-1108102056",
	"volume_new_name": "volume-11081020561",
	"cluster_uuid": "b8205835-ee82-4aa0-8c8b-6269e85aabd5"
	"volume_attribute_safety": "second",
	"volume_attribute_header_check": "true",
	"volume_attribute_data_check": "true",
	"volume_attribute_sector": "512",
	"snap_capacity": 3221225472
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

## /v1/volume/internal/iops/update
内置卷iops设置
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-|集群uuid
 tenant|string|是|-|租户uuid
 volume_uuid|string|是|-|卷uuid
 volume_name|string|是|-|卷名称
 write_bytes_limit|string|是|""|写带宽限制
 read_bytes_limit|string|是|""|读带宽限制
 write_iops_limit|string|是|""|写IOPS限制
 read_iops_limit|string|是|""|写IOPS限制


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/iops/update
```
Body:
```
{
	"tenant": "b3c011b0-6e4a-487e-b9af-022f869dc790",
	"volume_uuid": "bcb6ba4d-73a5-4d8a-aba3-ea85d10b583a",
	"volume_name": "volume-11081020561",
	"read_iops_limit": 3,
	"write_iops_limit": 0,
	"read_bytes_limit": 0,
	"write_bytes_limit": 0,
	"cluster_uuid": "b8205835-ee82-4aa0-8c8b-6269e85aabd5"
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


## /v1/volume/internal/replica/add
内置卷副本添加
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 volUUID|string|是|-|卷uuid
 volume_name|string|是|-|卷名称
 deltaRidNum|int|是|-|新增副本数量
 cluster_uuid|string|是|-|集群uuid


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/replica/add
```
Body:
```
{
	"volUUID": "bcb6ba4d-73a5-4d8a-aba3-ea85d10b583a",
	"volume_name": "volume-0824145216",
	"deltaRidNum": 1,
	"cluster_uuid": "b8205835-ee82-4aa0-8c8b-6269e85aabd5"
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

#### 异常返回示例

### 状态码


## /v1/volume/internal/replica/delete
内置卷副本删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 volUUID|string|是|-|卷uuid
 volume_name|string|是|-|卷名称
 rid|int|是|-|副本id
 cluster_uuid|string|是|-|集群uuid


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/replica/delete
```
Body:
```
{
	"volUUID": "bcb6ba4d-73a5-4d8a-aba3-ea85d10b583a",
	"volume_name": "volume-0824145216",
	"rid": 1,
	"cluster_uuid": "b8205835-ee82-4aa0-8c8b-6269e85aabd5"
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

#### 异常返回示例

### 状态码



## /v1/volume/internal/vreplica/get
内置卷虚拟副本获取
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TODO


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/vreplica/get
```
Body:
```
{
	"UUID": "bcb6ba4d-73a5-4d8a-aba3-ea85d10b583a",
	"cluster_uuid": "b8205835-ee82-4aa0-8c8b-6269e85aabd5"
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
    "Status": {
      "code": 0,
      "message": "",
      "messageCn": "",
      "stack": null,
      "desc": "",
      "UUID": ""
    },
    "TotalCount": 1,
    "Infos": [
      {
        "Namespace": "b3c011b0-6e4a-487e-b9af-022f869dc790",
        "Pool": "cb29e13f-152a-4aed-94c9-e5bfe594eff7",
        "Name": "volume-11081020561",
        "UUID": "bcb6ba4d-73a5-4d8a-aba3-ea85d10b583a",
        "Capacity": 1073741824,
        "SnapCapacity": 3221225472,
        "SliceSize": 1073741824,
        "Status": 1,
        "Vendor": "",
        "Replicas": null,
        "RW": null,
        "RO": null,
        "AccessPath": null,
        "InvalidAccessPath": null,
        "Accounts": [
          {
            "username": "volume_user",
            "password": "111111111111",
            "devType": "target",
            "flag": 1,
            "outgoing": false
          }
        ],
        "Attr": {
          "ComponentSetShift": "0",
          "ComponentShift": "30",
          "DataType": "replica",
          "DelMode": "default",
          "DevType": "target",
          "DriveType": "HDD",
          "Encrypto": "off",
          "InitFS": "false",
          "ReadBytesLimit": "0",
          "ReadIOPSLimit": "3",
          "ReadOnly": "on",
          "Safety": "first",
          "ScheduleOption": "intelligent",
          "StripeShift": "17",
          "TargetACL": "1.1.1.1",
          "ThinProvision": "on",
          "VmCache": "none",
          "VolumeName": "volume-1108102056",
          "WriteBytesLimit": "0",
          "WriteIOPSLimit": "0",
          "replica": "2"
        },
        "UserPerms": null,
        "UserGroupPerms": null,
        "SharePoint": null,
        "Ctime": 1573179688,
        "EventState": 0,
        "Label": null,
        "DeletedTime": 0,
        "PoolName": "gg_pool",
        "FinishPercent": 0,
        "VsdState": null,
        "SnapLength": 0,
        "vReplicaHost": null,
        "used": 0
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码




## /v1/volume/internal/device_type/convert
内置卷类型转换
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TODO


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/device_type/convert
```
Body:
```
{
	"tenant": "b3c011b0-6e4a-487e-b9af-022f869dc790",
	"volume_uuid": "bcb6ba4d-73a5-4d8a-aba3-ea85d10b583a",
	"volume_name": "volume-11081020561",
	"new_device_type": "target",
	"target_acl": "ALL",
	"cluster_uuid": "b8205835-ee82-4aa0-8c8b-6269e85aabd5"
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

## /v1/volume/internal/account/update
内置卷用户信息更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TODO


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/account/update
```
Body:
```
{
	"tenant": "b3c011b0-6e4a-487e-b9af-022f869dc790",
	"volume_uuid": "bcb6ba4d-73a5-4d8a-aba3-ea85d10b583a",
	"volume_name": "volume-11081020561",
	"accounts": [
		{
			"user_name": "volume_user",
			"password": "111111111111",
			"dev_type": "target",
			"outgoing": false,
			"flag": 1
		}
	],
	"cluster_uuid": "b8205835-ee82-4aa0-8c8b-6269e85aabd5"
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



## /v1/volume/internal/component/list
内置卷组件列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
volume_uuid|string|是|-|卷uuid
filter_component_status|int32|否|-|
replica_id|int|否|-|
page_num|int|否|0|第几页
page_size|int|否|0|每页数据条数

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.213:8080/v1/volume/internal/component/list?tenant=b3c011b0-6e4a-487e-b9af-022f869dc790&volume_uuid=bcb6ba4d-73a5-4d8a-aba3-ea85d10b583a&page_size=300&page_num=0&filter_component_status=-1&replica_id=0&cluster_uuid=b8205835-ee82-4aa0-8c8b-6269e85aabd5
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
    "list": [
      {
        "Namespace": "b3c011b0-6e4a-487e-b9af-022f869dc790",
        "Pool": "cb29e13f-152a-4aed-94c9-e5bfe594eff7",
        "Name": "volume-11081020561",
        "UUID": "bcb6ba4d-73a5-4d8a-aba3-ea85d10b583a",
        "Capacity": 1073741824,
        "SnapCapacity": 3221225472,
        "SliceSize": 1073741824,
        "Status": 1,
        "Vendor": "",
        "Replicas": [
          {
            "UUID": "8e621066-28a0-46dc-91d3-58f243547297",
            "Index": 0,
            "Status": 1,
            "Components": [
              {
                "UUID": "6dae950c-0de2-46c5-8129-13d6f670ef28",
                "HostUUID": "4507360c-d5e4-47ab-9d23-0dcea6895613",
                "UsdUUID": "aca64db7-e7ef-450c-b318-f19b580375dc",
                "Cid": 0,
                "Capacity": 1073741824,
                "Start": 0,
                "Status": 1,
                "MAddr": "192.168.201.188",
                "DAddr": "10.30.11.188",
                "EventState": 0,
                "Rid": 0,
                "UsdPath": "/dev/sdc"
              }
            ],
            "EventState": 0
          }
        ],
        "RW": null,
        "RO": null,
        "AccessPath": null,
        "InvalidAccessPath": null,
        "Accounts": [
          {
            "username": "volume_user",
            "password": "111111111111",
            "devType": "target",
            "flag": 1,
            "outgoing": false
          }
        ],
        "Attr": {
          "ComponentSetShift": "0",
          "ComponentShift": "30",
          "DataType": "replica",
          "DelMode": "default",
          "DevType": "target",
          "DriveType": "HDD",
          "Encrypto": "off",
          "InitFS": "false",
          "ReadBytesLimit": "0",
          "ReadIOPSLimit": "3",
          "ReadOnly": "on",
          "Safety": "first",
          "ScheduleOption": "intelligent",
          "StripeShift": "17",
          "TargetACL": "1.1.1.1",
          "ThinProvision": "on",
          "VmCache": "none",
          "VolumeName": "volume-1108102056",
          "WriteBytesLimit": "0",
          "WriteIOPSLimit": "0",
          "replica": "2"
        },
        "UserPerms": null,
        "UserGroupPerms": null,
        "SharePoint": null,
        "Ctime": 1573179688,
        "EventState": 0,
        "Label": null,
        "DeletedTime": 0,
        "PoolName": "gg_pool",
        "FinishPercent": 0,
        "VsdState": null,
        "SnapLength": 0,
        "vReplicaHost": null,
        "used": 0
      }
    ],
    "total_count": 1
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/internal/expansion
内置卷扩容
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TODO


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/expansion
```
Body:
```
{
	"tenant": "b3c011b0-6e4a-487e-b9af-022f869dc790",
	"volume_uuid": "184610bf-a119-4614-a477-c9dc98dbd8b7",
	"volume_name": "ccc",
	"capacity": 2147483648,
	"cluster_uuid": "b8205835-ee82-4aa0-8c8b-6269e85aabd5"
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
    "tenant": "",
    "name": "",
    "uuid": "",
    "pool": "",
    "namespace": "",
    "capacity": 0,
    "snap_capacity": 0,
    "status": 0,
    "ctime": 0,
    "flag": 0
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/internal/mount/list
内置卷可挂载主机列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
volume_uuid|string|是|-|卷uuid
page_num|int|否|0|第几页
page_size|int|否|0|每页数据条数

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.213:8080/v1/volume/internal/mount/list?tenant=b3c011b0-6e4a-487e-b9af-022f869dc790&volume_uuid=184610bf-a119-4614-a477-c9dc98dbd8b7&page_num=0&page_size=3&cluster_uuid=b8205835-ee82-4aa0-8c8b-6269e85aabd5
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
    "mount_hosts": [],
    "unmount_hosts": [
      {
        "host_uuid": "8d517b1d-61b8-4f6b-9eaf-6525531a0d3f",
        "host_ip": "192.168.201.191",
        "manager_net": {
          "name": "manager",
          "cidr_addrs": [
            "192.168.201.191/24",
            "fe80::7032:3fff:fef4:6c4e/64"
          ],
          "mtu": 1500,
          "bridge_uuid": "",
          "bridge_name": ""
        },
        "compute_net": {
          "name": "",
          "cidr_addrs": null,
          "mtu": 0,
          "bridge_uuid": "",
          "bridge_name": ""
        },
        "backup_net": {
          "name": "storage",
          "cidr_addrs": [
            "10.30.11.191/24"
          ],
          "mtu": 1500,
          "bridge_uuid": "",
          "bridge_name": ""
        },
        "storage_net": {
          "name": "storage",
          "cidr_addrs": [
            "10.30.11.191/24"
          ],
          "mtu": 1500,
          "bridge_uuid": "",
          "bridge_name": ""
        },
        "agent_status": 1,
        "host_mode": 0
      }
    ],
    "mount_hosts_total_count": 0,
    "unmount_hosts_total_count": 6
  }
}
```

#### 异常返回示例

### 状态码



## /v1/volume/internal/map
内置卷挂载
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
TODO


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/map
```
Body:
```
{
	"tenant": "b3c011b0-6e4a-487e-b9af-022f869dc790",
	"volume_uuid": "bcb6ba4d-73a5-4d8a-aba3-ea85d10b583a",
	"volume_name": "volume-11081020561",
	"hosts": [
		"fd403dd8-4b88-41b2-8464-b8ed7318e0d0"
	],
	"cluster_uuid": "b8205835-ee82-4aa0-8c8b-6269e85aabd5"
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


## /v1/volume/internal/unmap
内置卷卸载
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
TODO


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/unmap
```
Body:
```
{
	"tenant": "b3c011b0-6e4a-487e-b9af-022f869dc790",
	"volume_uuid": "bcb6ba4d-73a5-4d8a-aba3-ea85d10b583a",
	"volume_name": "volume-11081020561",
	"hosts": [
		"fd403dd8-4b88-41b2-8464-b8ed7318e0d0"
	],
	"force": false,
	"cluster_uuid": "b8205835-ee82-4aa0-8c8b-6269e85aabd5"
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

## /v1/volume/internal/component/migrate
内置卷组件迁移
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
TODO


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/component/migrate
```
Body:
```
{
	"tenant": "b3c011b0-6e4a-487e-b9af-022f869dc790",
	"volume_name": "volume-11081020561",
	"usd_uuid": "cf829606-c16c-4e59-81df-810401ba4de0",
	"components": [
		"6dae950c-0de2-46c5-8129-13d6f670ef28"
	],
	"cluster_uuid": "b8205835-ee82-4aa0-8c8b-6269e85aabd5"
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


## /v1/volume/internal/component/unused_usd
内置卷组件未使用数据盘列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
component_has_used_usds|string|是|-|

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.213:8080/v1/volume/internal/component/unused_usd?tenant=b3c011b0-6e4a-487e-b9af-022f869dc790&component_has_used_usds=aca64db7-e7ef-450c-b318-f19b580375dc&cluster_uuid=b8205835-ee82-4aa0-8c8b-6269e85aabd5
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
    "list": [
      {
        "host_uuid": "fd403dd8-4b88-41b2-8464-b8ed7318e0d0",
        "usd_uuid": "cf829606-c16c-4e59-81df-810401ba4de0"
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/internal/attribute/set
内置卷组件设置属性
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
TODO


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/attribute/set
```
Body:
```
{
	"tenant": "b3c011b0-6e4a-487e-b9af-022f869dc790",
	"volume_uuid": "bcb6ba4d-73a5-4d8a-aba3-ea85d10b583a",
	"volume_name": "volume-11081020561",
	"attribute": {
		"ReadOnly": "off"
	},
	"cluster_uuid": "b8205835-ee82-4aa0-8c8b-6269e85aabd5"
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

## /v1/volume/internal/clone
内置卷克隆
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant|string|是|-|源卷租户uuid
cluster_uuid|string|是|-|集群uuid
clone_pool_uuid|string|目的存储池uuid
volume_uuid|string|是|-|源卷uuid
volume_name|string|是|-|源卷名称
snapshot_uuid|string|是|-|快照uuid
clone_tenant|string|是|-|目的租户uuid
clone_volume_name|string|是|-|目的卷名称
link|bool|否|false|是否链接克隆
retain_snapshot|bool|否|false|是否保留快照
compress_data|bool|否|false|是否压缩
attr|map object|否|-|克隆属性

###attr

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
DriveType|string|否|-|目的卷存储介质（HDD:机械硬盘；SSD：固态硬盘）


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/attribute/set
```
Body:
```
{
	"tenant": "b5be02e1-e146-4168-84cc-5e0dda85c22b",
	"clone_pool_uuid": "75b47132-ed52-4739-bcf4-88f8b9687d90",
	"volume_uuid": "9c169277-7201-4ea1-9d39-56e1b1100368",
	"volume_name": "volume-0824145216",
	"snapshot_uuid": "d8b16abf-36f4-4a46-be3c-5cfa35d71018",
	"clone_tenant": "b5be02e1-e146-4168-84cc-5e0dda85c22b",
	"clone_volume_name": "clone",
	"link": true,
	"retain_snapshot": true,
	"cluster_uuid": "462601ce-727e-4c2f-ab45-6123dd3951cd",
	"attr": null
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
    "uuid": "2189a850-ae21-4d6d-9d9a-ca14f76257ec",
    "name": "vvv"
  }
}
```

#### 异常返回示例

### 状态码

## /v1/volume/internal/clone/progress
内置卷克隆进度
### 请求类型
get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
volume_uuid|string|是|-|目的卷uuid

### 返回参数

名称|参数类型|描述
---|---|---
finish_percent|float64|克隆进度

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/clone/progress?volume_uuid=9c169277-7201-4ea1-9d39-56e1b1100368&cluster_uuid=462601ce-727e-4c2f-ab45-6123dd3951cd
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
    "progress": 97
  }
}
```

#### 异常返回示例

### 状态码

## /v1/volume/internal/repair
内置卷修复
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant|string|是|-|租户uuid
cluster_uuid|string|是|-|集群uuid
volume_uuid|string|是|-|卷uuid
volume_name|string|是|-|卷名称

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/repair
```
Body:
```
{
	"tenant": "b5be02e1-e146-4168-84cc-5e0dda85c22b",
	"volume_uuid": "9c169277-7201-4ea1-9d39-56e1b1100368",
	"volume_name": "volume-0824145216",
	"cluster_uuid": "462601ce-727e-4c2f-ab45-6123dd3951cd",
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

## /v1/volume/internal/capacity/used/update
内置卷已使用容量更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant|string|是|-|租户uuid
cluster_uuid|string|是|-|集群uuid
volume_uuid|string|是|-|卷uuid
volume_name|string|是|-|卷名称

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/repair
```
Body:
```
{
	"tenant": "b5be02e1-e146-4168-84cc-5e0dda85c22b",
	"volume_uuid": "9c169277-7201-4ea1-9d39-56e1b1100368",
	"volume_name": "volume-0824145216",
	"cluster_uuid": "462601ce-727e-4c2f-ab45-6123dd3951cd",
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

## /v1/volume/internal/zone/related/set
内置卷批量设置延伸
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
infos|[]InternalVolumeRelatedInfo|是|-|卷信息

###infos
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
volume_uuid|string|是|-|卷uuid
volume_name|string|是|-|卷名称

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/zone/related/set
```
Body:
```
{
	"infos": [
		{
			"volume_uuid": "6809e3e5-2ff2-4a8c-a239-d17dc6947c2b",
			"volume_name": "related-2"
		},
		{
			"volume_uuid": "2b190372-c522-46dd-a2a5-7bfb95acf092",
			"volume_name": "related-1"
		}
	],
	"cluster_uuid": "c27a25bc-5da2-430f-bfaf-6c8d33f21128"
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
    "success": 2,
    "fail": 0,
    "results": [
      {
        "message": "success",
        "message_cn": "成功",
        "scode": 0,
        "desc": "",
        "stack": null,
        "data": {
          "volume_uuid": "6809e3e5-2ff2-4a8c-a239-d17dc6947c2b",
          "volume_name": "related-2"
        }
      },
      {
        "message": "success",
        "message_cn": "成功",
        "scode": 0,
        "desc": "",
        "stack": null,
        "data": {
          "volume_uuid": "2b190372-c522-46dd-a2a5-7bfb95acf092",
          "volume_name": "related-1"
        }
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码

## /v1/volume/internal/zone/unrelated/set
内置卷批量解除延伸
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
infos|[]InternalVolumeRelatedInfo|是|-|卷信息

###InternalVolumeRelatedInfo
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
volume_uuid|string|是|-|卷uuid
volume_name|string|是|-|卷名称

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/zone/unrelated/set
```
Body:
```
{
	"infos": [
		{
			"volume_uuid": "6809e3e5-2ff2-4a8c-a239-d17dc6947c2b",
			"volume_name": "related-2"
		},
		{
			"volume_uuid": "2b190372-c522-46dd-a2a5-7bfb95acf092",
			"volume_name": "related-1"
		}
	],
	"cluster_uuid": "c27a25bc-5da2-430f-bfaf-6c8d33f21128"
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
    "success": 2,
    "fail": 0,
    "results": [
      {
        "message": "success",
        "message_cn": "成功",
        "scode": 0,
        "desc": "",
        "stack": null,
        "data": {
          "volume_uuid": "6809e3e5-2ff2-4a8c-a239-d17dc6947c2b",
          "volume_name": "related-2"
        }
      },
      {
        "message": "success",
        "message_cn": "成功",
        "scode": 0,
        "desc": "",
        "stack": null,
        "data": {
          "volume_uuid": "2b190372-c522-46dd-a2a5-7bfb95acf092",
          "volume_name": "related-1"
        }
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码

## /v1/volume/internal/replica/get_domain
内置卷获取副本所在的保护域
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
volume_uuid|string|是|-|卷uuid
rid|int32|是|-|副本id

### 返回参数

名称|参数类型|描述
---|---|---
domain_uuid|string|保护域uuid

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/replica/get_domain?cluster_uuid=c27a25bc-5da2-430f-bfaf-6c8d33f21128&volume_uuid=6809e3e5-2ff2-4a8c-a239-d17dc6947c2b&rid=0
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
    "domain_uuid": "9ca2f65b-ab91-42ea-8ae1-962668f4d82d"
  }
}
```

#### 异常返回示例

### 状态码

