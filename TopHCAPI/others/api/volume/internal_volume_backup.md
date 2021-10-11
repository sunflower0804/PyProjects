[back to api overview](../api_overview.md#label_api)
### 融合存储卷(内置卷)备份相关接口
## /v1/volume/internal/backup/list
内置卷备份列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
filter_desc|string|否|-|过滤描述
filter_name|string|否|-|过滤名称
filter_volume_uuid|string|否|-|过滤卷uuid
filter_start_time|int64|否|-|过滤开始时间,时间戳
filter_end_time|int64|否|-|过滤结束时间,时间戳
### 返回参数

名称|参数类型|描述
---|---|---
list|object array|列表
total_count|int|总数量

#### list对象
名称|参数类型|描述
---|---|---
tenant|string|租户uuid
tenant_name|string|租户名称
UUID|string|卷备份uuid
Name|string|卷备份名称
BpUUID|string|备份点uuid
VolumeUUID|string|卷uuid
VolumeCapacity|uint64|卷容量
snapshot|string|快照名称
Ctime|int64|创建时间
Mtime|int64|修改时间
Desc|string|卷备份描述
BpName|string|备份点名称

### 示例

#### 请求示例
```
http://192.168.201.213:8080/v1/volume/internal/backup/list?page_num=0&page_size=5&filter_name=&tenant=b3c011b0-6e4a-487e-b9af-022f869dc790&filter_desc=&filter_start_time=0&filter_end_time=0&filter_volume_uuid=8652dfcb-9c83-4f93-b964-b8c87942869a&cluster_uuid=b8205835-ee82-4aa0-8c8b-6269e85aabd5
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
    "total_count": 1,
    "list": [
      {
        "tenant": "b3c011b0-6e4a-487e-b9af-022f869dc790",
        "tenant_name": "gg_tenant",
        "UUID": "1b90f66d-324d-4f2d-9c9a-81fe522d1370",
        "Name": "backname1",
        "BpUUID": "322e8d08-6630-4d45-a448-0f8e23e491ac",
        "NsUUID": "b3c011b0-6e4a-487e-b9af-022f869dc790",
        "VolumeUUID": "8652dfcb-9c83-4f93-b964-b8c87942869a",
        "VolumeCapacity": 1073741824,
        "snapshot": "asdf",
        "Ctime": 1573193278,
        "Desc": "",
        "Attr": {
          "ComponentSetShift": "0",
          "ComponentShift": "30",
          "DataType": "replica",
          "DevType": "share",
          "ShareType": "smb",
          "StripeShift": "17",
          "replica": "2"
        },
        "Rid": 0,
        "Mtime": 0,
        "BpName": "gg_smb_backup",
        "ExpiredTime": 0
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/internal/backup/add
内置卷备份添加
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
volume_uuid|string|是|-|卷uuid
snapshot_uuid|string|是|-|快照uuid
name|string|是|-|备份名称
backup_point_uuid|string|是|-|备份点uuid
description|string|否|-|描述
full_backup|bool|否|false|是否全量备份（true：全量备份；false:增量备份）


### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/internal/backup/add
```
Body:
```
{
	"tenant": "b3c011b0-6e4a-487e-b9af-022f869dc790",
	"volume_uuid": "8652dfcb-9c83-4f93-b964-b8c87942869a",
	"snapshot_uuid": "a46888b3-6a71-42d2-bc0b-9e66265143c5",
	"name": "backname1",
	"backup_point_uuid": "322e8d08-6630-4d45-a448-0f8e23e491ac",
	"description": "",
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


## /v1/volume/internal/backup/delete
内置卷备份删除
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
http://192.168.201.147:9990/v1/volume/internal/backup/delete
```
Body:
```
{
	"tenant": "b3c011b0-6e4a-487e-b9af-022f869dc790",
	"backup_uuid": "1b90f66d-324d-4f2d-9c9a-81fe522d1370",
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


## /v1/volume/internal/backup/restore
内置卷备份恢复
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
http://192.168.201.147:9990/v1/volume/internal/backup/restore
```
Body:
```
{
	"tenant": "b3c011b0-6e4a-487e-b9af-022f869dc790",
	"backup_uuid": "1b90f66d-324d-4f2d-9c9a-81fe522d1370",
	"new_volume_name": "备份恢复1",
	"new_pool_uuid": "cb29e13f-152a-4aed-94c9-e5bfe594eff7",
	"usd_type": "HDD",
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

## /v1/volume/internal/backup/batch_delete
内置卷备份批量删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
backups|[]InternalVolumeBackupIdentifier|是|-|卷信息

###InternalVolumeBackupIdentifier
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
backup_uuid|string|是|-|备份uuid
backup_name|string|是|-|备份名称

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
	"backups": [
		{
			"cluster_uuid": "c123a9ab-1699-482e-aa69-60b68d2d6c7d",
			"tenant": "c7af6cd8-82b1-46a9-a7db-1293609c22ef",
			"backup_uuid": "a0828764-9657-4481-a28b-3818682e9cd1",
			"backup_name": "www"
		},
		{
			"cluster_uuid": "c123a9ab-1699-482e-aa69-60b68d2d6c7d",
			"tenant": "c7af6cd8-82b1-46a9-a7db-1293609c22ef",
			"backup_uuid": "ed33be76-2d08-4095-8537-9e416c8309c2",
			"backup_name": "sss"
		}
	]
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
          "cluster_uuid": "c123a9ab-1699-482e-aa69-60b68d2d6c7d",
          "cluster_name": "TOPEC",
          "tenant": "c7af6cd8-82b1-46a9-a7db-1293609c22ef",
          "backup_uuid": "a0828764-9657-4481-a28b-3818682e9cd1",
          "backup_name": "www"
        }
      },
      {
        "scode": 0,
        "desc": "",
        "message": "success",
        "message_cn": "成功",
        "stack": null,
        "data": {
          "cluster_uuid": "c123a9ab-1699-482e-aa69-60b68d2d6c7d",
          "cluster_name": "TOPEC",
          "tenant": "c7af6cd8-82b1-46a9-a7db-1293609c22ef",
          "backup_uuid": "ed33be76-2d08-4095-8537-9e416c8309c2",
          "backup_name": "sss"
        }
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码

## /v1/volume/internal/backup/from/remote
内置卷获取远端备份
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
backuppoint_uuid|string|是|-|备份点uuid
filter_name|string|否|-|过滤备份名称
page_num|int|否|0|第几页
page_size|int|否|0|每页数据条数


### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://10.30.32.80:8080/v1/volume/internal/backup/from/remote?tenant=b5be02e1-e146-4168-84cc-5e0dda85c22b&backuppoint_uuid=7bda3ebf-e915-4bc7-98bf-7f39f70425ef&filter_name=&page_num=0&page_size=10&cluster_uuid=462601ce-727e-4c2f-ab45-6123dd3951cd
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
    "total_count": 1,
    "List": [
      {
        "UUID": "5c028d4f-fe12-479c-91d1-84a56d49268c",
        "Name": "4444",
        "BpUUID": "7bda3ebf-e915-4bc7-98bf-7f39f70425ef",
        "NsUUID": "da78aaa0-3df5-4461-83f1-103643b11eb4",
        "VolumeUUID": "ffc2949e-4a36-4a55-a2fa-459dd0ecdcb7",
        "VolumeCapacity": 13958643712,
        "snapshot": "2021-07-27T17-12-57_618725024",
        "Ctime": 1627377633,
        "Desc": "",
        "Attr": {
          "ComponentSetShift": "0",
          "ComponentShift": "30",
          "DataType": "replica",
          "DevType": "target",
          "StripeShift": "20",
          "replica": "2"
        },
        "Rid": 0,
        "Mtime": 0,
        "BpName": "nfs-backup",
        "ExpiredTime": 0,
        "VolumeEventState": 0,
        "SnapshotUUID": "",
        "Status": "BackupFinished"
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码

## /v1/volume/internal/backup/save
内置卷导入远端备份
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
TODO

### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://10.30.32.80:8080/v1/volume/internal/backup/save
```

Body:
```
{
	"tenant": "b5be02e1-e146-4168-84cc-5e0dda85c22b",
	"backup": [
		{
			"UUID": "5c028d4f-fe12-479c-91d1-84a56d49268c",
			"Name": "4444",
			"BpUUID": "7bda3ebf-e915-4bc7-98bf-7f39f70425ef",
			"NsUUID": "da78aaa0-3df5-4461-83f1-103643b11eb4",
			"VolumeUUID": "ffc2949e-4a36-4a55-a2fa-459dd0ecdcb7",
			"VolumeCapacity": 13958643712,
			"snapshot": "2021-07-27T17-12-57_618725024",
			"Ctime": 1627377633,
			"Desc": "",
			"Attr": {
				"ComponentSetShift": "0",
				"ComponentShift": "30",
				"DataType": "replica",
				"DevType": "target",
				"StripeShift": "20",
				"replica": "2"
			},
			"Rid": 0,
			"Mtime": 0,
			"BpName": "nfs-backup",
			"ExpiredTime": 0,
			"VolumeEventState": 0,
			"SnapshotUUID": "",
			"Status": "BackupFinished",
			"index": 1,
			"volumeName": "4444",
			"snapName": "2021-07-27T17-12-57_618725024",
			"C_time": "2021-07-27 17:20:33"
		}
	],
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
    "total_count": 0,
    "List": []
  }
}
```

#### 异常返回示例

### 状态码
