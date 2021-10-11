[back to api overview](../api_overview.md#label_api)
### 共享存储卷(第三方卷)相关接口
### /v1/volume/share/list
共享存储卷(第三方卷)列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
filter_pool_uuid|string|否|-|池uuid
filter_name|string|否|-|按名称过滤
page_num|int|否|0|第几页
page_size|int|否|0|每页条数
### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.213:8080/v1/volume/share/list
```
Body:
```
{
  "tenant": "fab210d2-b9b8-4b0b-bd61-50812ce3d4d0",
  "filter_pool_uuid": "",
  "filter_name": "",
  "page_num": 0,
  "page_size": 10,
  "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0"
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
    "list": [
      {
        "tenant": "fab210d2-b9b8-4b0b-bd61-50812ce3d4d0",
        "tenant_name": "zhangyiru",
        "volume": {
          "UUID": "7fc3da44-118c-461b-9cf7-baba77f01502",
          "Name": "qqq-shareVolume1-0",
          "NamespaceUUID": "83b1add8-2b9d-4f0c-8f3b-e0c3a2001006",
          "Type": "block",
          "PoolUUID": "f0dc0363-5e70-419a-95ad-2c49c14d70c1",
          "Capacity": 3221225472,
          "Used": 196894,
          "Attr": {
            "VirtualMachine": "863b64eb-c8ed-4f25-9af9-9c96b28a7200",
            "VirtualMachineDevice": "sda",
            "VirtualMachineHostUUID": "f04d95d6-c4f2-45c9-a1ef-164482af658a",
            "VirtualMachineName": "qqq",
            "VirtualMachineType": "GUS"
          },
          "PoolName": "bbb",
          "ZoneUUID": "3e2f589c-d5d7-4807-9c03-238fe967cdbd",
          "ZoneName": "default",
          "SnapLength": 0,
          "SnapCap": 9663676416,
          "Ctime": 1614840756,
          "Mtime": 1615771441,
          "AccessPath": {
            "f04d95d6-c4f2-45c9-a1ef-164482af658a": "/share/pool-f0dc0363-5e70-419a-95ad-2c49c14d70c1/volume/7fc3da44-118c-461b-9cf7-baba77f01502"
          },
          "EventState": 0,
          "ShareNsUUIDs": null,
          "Parent": "",
          "ParentSnapshot": "",
          "Children": null
        },
        "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0",
        "cluster_name": "cluster_name_243",
        "cluster_mode": ""
      },
      {
        "tenant": "fab210d2-b9b8-4b0b-bd61-50812ce3d4d0",
        "tenant_name": "zhangyiru",
        "volume": {
          "UUID": "515ed422-5bd9-4c38-a7f2-425e743a09d4",
          "Name": "备份中发GV",
          "NamespaceUUID": "83b1add8-2b9d-4f0c-8f3b-e0c3a2001006",
          "Type": "block",
          "PoolUUID": "ca12d616-73c4-4629-a5c0-a37a8e163c33",
          "Capacity": 12884901888,
          "Used": 0,
          "Attr": null,
          "PoolName": "rbd198",
          "ZoneUUID": "3e2f589c-d5d7-4807-9c03-238fe967cdbd",
          "ZoneName": "default",
          "SnapLength": 0,
          "SnapCap": 38654705664,
          "Ctime": 1614681406,
          "Mtime": 1614681406,
          "AccessPath": {
            "f04d95d6-c4f2-45c9-a1ef-164482af658a": ""
          },
          "EventState": 0,
          "ShareNsUUIDs": null,
          "Parent": "",
          "ParentSnapshot": "",
          "Children": null
        },
        "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0",
        "cluster_name": "cluster_name_243",
        "cluster_mode": ""
      },
    "each_range_list_state": [
      {
        "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0",
        "cluster_name": "cluster_name_243",
        "cluster_mode": "",
        "namespace_uuid": "83b1add8-2b9d-4f0c-8f3b-e0c3a2001006",
        "result": {
          "scode": 0,
          "desc": "",
          "message": "success",
          "message_cn": "成功",
          "stack": null,
          "data": ""
        },
        "total_count": 10
      }
    ],
    "TotalCount": 10
  }
}
```

#### 异常返回示例

### 状态码



## /v1/volume/share/create
共享存储卷(第三方)添加
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
pool_uuid|string|是|-|共享存储池uuid
volume_name|string|是|-|共享存储卷名称
volume_type|string|是|-|共享存储卷类型（block/share/fs）
capacity|uint64|否|-|卷容量,单位字节，填写已有卷路径时可以不传，会自动识别卷大小
snap_capacity|uint64|是|-|快照容量,单位字节
backing_file|string|否|-|已有卷文件路径，不传则创建一个空卷


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/share/create
```
Body:
```
{
  "tenant": "fab210d2-b9b8-4b0b-bd61-50812ce3d4d0",
  "pool_name": "disks",
  "pool_uuid": "0eca2be3-056f-4634-a25b-5cf717e067fb",
  "volume_name": "test",
  "volume_type": "block",
  "capacity": 4294967296,
  "snap_capacity": 12884901888,
  "backing_file":"/xgp/my.qcow2",
  "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0"
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
    "volume": {
      "UUID": "bc570c7b-e9fd-4fe7-a02e-f36fdbc72c79",
      "Name": "test",
      "NamespaceUUID": "83b1add8-2b9d-4f0c-8f3b-e0c3a2001006",
      "Type": "block",
      "PoolUUID": "0eca2be3-056f-4634-a25b-5cf717e067fb",
      "Capacity": 4294967296,
      "Used": 0,
      "Attr": null,
      "PoolName": "disks",
      "ZoneUUID": "3e2f589c-d5d7-4807-9c03-238fe967cdbd",
      "ZoneName": "default",
      "SnapLength": 0,
      "SnapCap": 12884901888,
      "Ctime": 1615790928,
      "Mtime": 1615790928,
      "AccessPath": {
        "f04d95d6-c4f2-45c9-a1ef-164482af658a": "/share/pool-0eca2be3-056f-4634-a25b-5cf717e067fb/volume/bc570c7b-e9fd-4fe7-a02e-f36fdbc72c79"
      },
      "EventState": 0,
      "ShareNsUUIDs": null,
      "Parent": "",
      "ParentSnapshot": "",
      "Children": null
    },
    "clone_progress": 0,
    "cluster_uuid": "",
    "cluster_name": "",
    "cluster_mode": "",
    "tenant": "",
    "tenant_name": ""
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/share/delete
共享存储卷删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
volume_uuid|string|是|-|卷uuid
volume_name|string|是|-|卷名称
tenant|string|是|-|租户uuid
cluster_uuid|string|是|-|集群uuid
force|bool|否|-|是否强制删除

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/share/delete
```
Body:
```
{
  "tenant": "fab210d2-b9b8-4b0b-bd61-50812ce3d4d0",
  "volume_uuid": "bc570c7b-e9fd-4fe7-a02e-f36fdbc72c79",
  "volume_name": "test",
  "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0",
  "force": true
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
    "volume": null,
    "clone_progress": 0,
    "cluster_uuid": "",
    "cluster_name": "",
    "cluster_mode": "",
    "tenant": "",
    "tenant_name": ""
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/share/get
共享存储卷详情获取
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
volume_uuid|string|是|-|卷uuid
tenant|string|是|-|租户uuid
cluster_uuid|string|是|-|集群uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/share/get
```
Body:
```
{
  "tenant": "fab210d2-b9b8-4b0b-bd61-50812ce3d4d0",
  "volume_uuid": "fba864c4-d9f7-451b-a775-f2777557be55",
  "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0"
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
    "volume": {
      "UUID": "7fc3da44-118c-461b-9cf7-baba77f01502",
      "Name": "qqq-shareVolume1-0",
      "NamespaceUUID": "83b1add8-2b9d-4f0c-8f3b-e0c3a2001006",
      "Type": "block",
      "PoolUUID": "f0dc0363-5e70-419a-95ad-2c49c14d70c1",
      "Capacity": 3221225472,
      "Used": 196894,
      "Attr": {
        "VirtualMachine": "863b64eb-c8ed-4f25-9af9-9c96b28a7200",
        "VirtualMachineDevice": "sda",
        "VirtualMachineHostUUID": "f04d95d6-c4f2-45c9-a1ef-164482af658a",
        "VirtualMachineName": "qqq",
        "VirtualMachineType": "GUS"
      },
      "PoolName": "bbb",
      "ZoneUUID": "3e2f589c-d5d7-4807-9c03-238fe967cdbd",
      "ZoneName": "default",
      "SnapLength": 0,
      "SnapCap": 9663676416,
      "Ctime": 1614840756,
      "Mtime": 1615771441,
      "AccessPath": {
        "f04d95d6-c4f2-45c9-a1ef-164482af658a": "/share/pool-f0dc0363-5e70-419a-95ad-2c49c14d70c1/volume/7fc3da44-118c-461b-9cf7-baba77f01502"
      },
      "EventState": 0,
      "ShareNsUUIDs": null,
      "Parent": "",
      "ParentSnapshot": "",
      "Children": null
    },
    "clone_progress": 0,
    "cluster_uuid": "",
    "cluster_name": "",
    "cluster_mode": "",
    "tenant": "",
    "tenant_name": ""
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/share/used/update
共享存储卷更新已使用容量
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
volume_uuid|string|是|-|卷uuid
volume_name|string|是|-|卷名称
tenant|string|是|-|租户uuid
cluster_uuid|string|是|-|集群uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/share/used/update
```
Body:
```
{
  "tenant": "fab210d2-b9b8-4b0b-bd61-50812ce3d4d0",
  "volume_uuid": "fba864c4-d9f7-451b-a775-f2777557be55",
  "volume_name": "snap",
  "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0"
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
    "volume": null,
    "clone_progress": 0,
    "cluster_uuid": "",
    "cluster_name": "",
    "cluster_mode": "",
    "tenant": "",
    "tenant_name": ""
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/share/snap_length/update
共享存储卷更新快照已使用容量
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
volume_uuid|string|是|-|卷uuid
volume_name|string|是|-|卷名称
tenant|string|是|-|租户uuid
cluster_uuid|string|是|-|集群uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/share/snap_length/update
```
Body:
```
{
  "tenant": "fab210d2-b9b8-4b0b-bd61-50812ce3d4d0",
  "volume_uuid": "fba864c4-d9f7-451b-a775-f2777557be55",
  "volume_name": "snap",
  "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0"
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
    "volume": null,
    "clone_progress": 0,
    "cluster_uuid": "",
    "cluster_name": "",
    "cluster_mode": "",
    "tenant": "",
    "tenant_name": ""
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/share/clone
共享存储卷克隆
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
volume_uuid|string|是|-|卷uuid
volume_name|string|是|-|卷名称
cluster_uuid|string|是|-|集群uuid
clone_dst_vol_name|string|是|-|新卷uuid
clone_dst_vol_tenant|string|是|-|新卷租户uuid
clone_dst_pool_uuid|string|是|-|新卷所在的池uuid
is_link|bool|是|-|是否链接克隆
snapshot_uuid|string|是|-|克隆基于的快照uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/share/clone
```
Body:
```
{
  "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0",
  "volume_uuid": "3e0925e0-648d-4217-bc1a-079cdbcf2e41",
  "volume_name": "zzz",
  "clone_dst_pool_uuid": "0eca2be3-056f-4634-a25b-5cf717e067fb",
  "clone_dst_vol_name": "test",
  "clone_dst_vol_tenant": "fab210d2-b9b8-4b0b-bd61-50812ce3d4d0",
  "snapshot_uuid": "ef333eb6-300f-4ef8-ac85-704c111376c7",
  "is_link": true
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
    "volume": null,
    "clone_progress": 0,
    "cluster_uuid": "",
    "cluster_name": "",
    "cluster_mode": "",
    "tenant": "",
    "tenant_name": ""
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/share/clone/progress
共享存储卷克隆进度
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
volume_uuid|string|是|-|卷uuid
tenant|string|是|-|租户uuid
cluster_uuid|string|是|-|集群uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/share/clone/progress?cluster_uuid=7015835c-56a6-4773-937c-1dbcbe5dfba5&tenant=94aa5dc6-b5c2-4044-a771-6256437f3412&volume_uuid=94aa5dc6-b5c2-4044-a771-6256437f3412
```
Body:
```
{
  "tenant": "fab210d2-b9b8-4b0b-bd61-50812ce3d4d0",
  "volume_uuid": "fba864c4-d9f7-451b-a775-f2777557be55",
  "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0"
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
    "volume": null,
    "clone_progress": 70.2,
    "cluster_uuid": "",
    "cluster_name": "",
    "cluster_mode": "",
    "tenant": "",
    "tenant_name": ""
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/share/backup/add
共享存储卷备份创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
volume_uuid|string|是|-|卷uuid
cluster_uuid|string|是|-|集群uuid
backup_name|string|是|-|备份名称
backup_point_uuid|string|是|-|备份点uuid
snapshot_uuid|string|是|-|备份基于的快照uuid
desc|string|否|-|描述


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/share/backup/add
```
Body:
```
{
  "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0",
  "volume_uuid": "3e0925e0-648d-4217-bc1a-079cdbcf2e41",
  "snapshot_uuid": "ef333eb6-300f-4ef8-ac85-704c111376c7",
  "backup_name": "backup",
  "backup_point_uuid": "7f74897a-3084-45e1-a413-6cd168ddd4b5",
  "desc": ""
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
    "backup": {
      "tenant": "fab210d2-b9b8-4b0b-bd61-50812ce3d4d0",
      "tenant_name": "zhangyiru",
      "UUID": "4e4033af-1847-49fd-9f5a-b7f9f06cac52",
      "Name": "backup",
      "BpUUID": "7f74897a-3084-45e1-a413-6cd168ddd4b5",
      "NsUUID": "83b1add8-2b9d-4f0c-8f3b-e0c3a2001006",
      "VolumeUUID": "3e0925e0-648d-4217-bc1a-079cdbcf2e41",
      "VolumeCapacity": 3221225472,
      "Snapshot": "aaa",
      "Ctime": 1615793159,
      "Desc": "",
      "Attr": null,
      "VolumeType": "block",
      "Mtime": 1615793159,
      "BpName": "",
      "ExpiredTime": 0,
      "VolumeEventStatus": 0,
      "SnapshotUUID": "ef333eb6-300f-4ef8-ac85-704c111376c7",
      "Status": "BackupStarted",
      "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0",
      "cluster_name": "cluster_name_243",
      "cluster_mode": ""
    }
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/share/backup/delete
共享存储卷备份删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant|string|是|-|租户uuid
cluster_uuid|string|是|-|集群uuid
backup_uuid|string|是|-|备份名称



### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/share/backup/delete
```
Body:
```
{
  "tenant": "fab210d2-b9b8-4b0b-bd61-50812ce3d4d0",
  "backup_uuid": "fba864c4-d9f7-451b-a775-f2777557be55",
  "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0"
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


## /v1/volume/share/backup/restore
共享存储卷备份恢复
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
new_volume_tenant|string|是|-|新卷所在的租户uuid
cluster_uuid|string|是|-|集群uuid
backup_uuid|string|是|-|备份名称
new_volume_name|string|是|-|恢复的新卷名称
new_pool_uuid|string|是|-|新卷的所在的池uuid



### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/share/backup/restore
```
Body:
```
{
  "backup_uuid": "4e4033af-1847-49fd-9f5a-b7f9f06cac52",
  "new_volume_name": "restore",
  "new_pool_uuid": "0eca2be3-056f-4634-a25b-5cf717e067fb",
  "new_volume_tenant": "fab210d2-b9b8-4b0b-bd61-50812ce3d4d0",
  "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0"
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
    "backup": null
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/share/backup/list
共享存储卷备份列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
page_num|int|否|0|第几页
page_size|int|否|0|每页条数
cluster_uuid|string|是|-|集群uuid
filter_desc|string|否|-|过滤描述
filter_start_time|string|否|-|过滤备份创建时间段的开始时间
filter_end_time|string|是|-|过滤备份创建时间段的结束时间
filter_volume_uuid|string|否|-|卷uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/share/backup/list?page_num=0&page_size=10&filter_name=&tenant=fab210d2-b9b8-4b0b-bd61-50812ce3d4d0&filter_desc=&filter_start_time=1615192208&filter_end_time=1615797008&cluster_uuid=a97eb422-f42b-4b85-8556-725f152661f0&filter_volume_uuid=3e0925e0-648d-4217-bc1a-079cdbcf2e41
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
    "backup": null
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/share/snapshot/create
共享存储卷快照创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant|string|是|-|租户uuid
cluster_uuid|string|是|-|集群uuid
volume_uuid|string|是|-|卷uuid
snapshot_name|string|是|-|快照名称
desc|string|否|-|快照描述



### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/share/snapshot/create
```
Body:
```
{
  "tenant": "fab210d2-b9b8-4b0b-bd61-50812ce3d4d0",
  "desc": "",
  "snapshot_name": "snap",
  "volume_uuid": "3e0925e0-648d-4217-bc1a-079cdbcf2e41",
  "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0"
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
    "snapshot": {
      "Name": "snap",
      "UUID": "a22d8596-df43-4918-b050-3d9b86d76092",
      "Volume": "3e0925e0-648d-4217-bc1a-079cdbcf2e41",
      "Desc": "",
      "Status": 0,
      "Ctime": 1615797815,
      "Attr": null,
      "Size": 0,
      "Children": [
        "head"
      ],
      "Parent": "aaa",
      "Ref": 0
    },
    "tree": null,
    "cluster_uuid": "",
    "cluster_name": "",
    "cluster_mode": "",
    "tenant": "",
    "tenant_name": ""
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/share/snapshot/delete
共享存储卷快照删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant|string|是|-|租户uuid
cluster_uuid|string|是|-|集群uuid
volume_uuid|string|是|-|卷uuid
snapshot_name|string|是|-|快照名称
snapshot_uuid|string|是|-|快照uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/share/snapshot/delete
```
Body:
```
{
  "tenant": "fab210d2-b9b8-4b0b-bd61-50812ce3d4d0",
  "volume_uuid": "3e0925e0-648d-4217-bc1a-079cdbcf2e41",
  "snapshot_name": "snap",
  "snapshot_uuid": "a22d8596-df43-4918-b050-3d9b86d76092",
  "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0"
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
    "snapshot": null,
    "tree": null,
    "cluster_uuid": "",
    "cluster_name": "",
    "cluster_mode": "",
    "tenant": "",
    "tenant_name": ""
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/share/snapshot/rollback
共享存储卷快照回滚
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant|string|是|-|租户uuid
cluster_uuid|string|是|-|集群uuid
volume_uuid|string|是|-|卷uuid
snapshot_uuid|string|是|-|快照uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/share/snapshot/rollback
```
Body:
```
{
  "tenant": "fab210d2-b9b8-4b0b-bd61-50812ce3d4d0",
  "volume_uuid": "3e0925e0-648d-4217-bc1a-079cdbcf2e41",
  "snapshot_uuid": "ef333eb6-300f-4ef8-ac85-704c111376c7",
  "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0"
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
    "snapshot": null,
    "tree": null,
    "cluster_uuid": "",
    "cluster_name": "",
    "cluster_mode": "",
    "tenant": "",
    "tenant_name": ""
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/share/snapshot/tree/get
共享存储卷快照树查询
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant|string|是|-|租户uuid
cluster_uuid|string|是|-|集群uuid
volume_uuid|string|是|-|卷uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/share/snapshot/tree/get
```
Body:
```
{
  "tenant": "fab210d2-b9b8-4b0b-bd61-50812ce3d4d0",
  "volume_uuid": "3e0925e0-648d-4217-bc1a-079cdbcf2e41",
  "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0"
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
    "snapshot": null,
    "tree": {
      "UUID": "",
      "Parents": {
        "aaa": "",
        "head": "aaa"
      },
      "Children": {
        "": {
          "Children": [
            "aaa"
          ]
        },
        "aaa": {
          "Children": [
            "head"
          ]
        }
      },
      "Root": "aaa"
    },
    "cluster_uuid": "",
    "cluster_name": "",
    "cluster_mode": "",
    "tenant": "",
    "tenant_name": ""
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/share/snapshot/list
共享存储卷快照列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant|string|是|-|租户uuid
cluster_uuid|string|是|-|集群uuid
volume_uuid|string|是|-|卷uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/volume/share/snapshot/list
```
Body:
```
{
  "tenant": "fab210d2-b9b8-4b0b-bd61-50812ce3d4d0",
  "volume_uuid": "3e0925e0-648d-4217-bc1a-079cdbcf2e41",
  "cluster_uuid": "a97eb422-f42b-4b85-8556-725f152661f0"
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
    "list": [
      {
        "Name": "aaa",
        "UUID": "ef333eb6-300f-4ef8-ac85-704c111376c7",
        "Volume": "3e0925e0-648d-4217-bc1a-079cdbcf2e41",
        "Desc": "",
        "Status": 0,
        "Ctime": 1615791886,
        "Attr": {
          "LinkCloneUsed": "LinkCloneUsed"
        },
        "Size": 0,
        "Children": [
          "head"
        ],
        "Parent": "",
        "Ref": 1
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


