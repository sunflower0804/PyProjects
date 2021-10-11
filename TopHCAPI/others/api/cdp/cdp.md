[back to api overview](../api_overview.md#label_api)

### cdp相关接口
## /v1/volume/internal/cdp/edit
cdp编辑（不存在时即创建）
### 请求类型
POST

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cdp_priority|string|是|-|恢复优先级
reserve_capacity|uint64|是|-|占用CDP盘最大空间
reserve_duration|uint64|是|-|可恢复最近时长
volumes|[]InternalVolumeIdentifier|是|-|卷信息数组

### InternalVolumeIdentifier对象
名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|卷所属集群uuid
tenant|string|否|-|卷所属租户uuid
volume_uuid|string|是|-|卷uuid
volume_name|string|否|-|卷名称

### 返回参数

名称|参数类型|描述
---|---|---
success|int|操作成功数量
fail|int|操作失败数量
results|[]Output|操作结果数组

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/volume/internal/cdp/edit
```

Body:
```
{
	"cdp_priority": "mid",
    "reserve_capacity": 32212254720,
    "reserve_duration": 86400,
    "volumes": [
        {
            "cluster_uuid": "ee3ae4de-811a-45b5-b339-f7ad45872c33",
            "tenant": "257d6354-be6d-45ec-b65d-e961d6a1274b",
            "volume_uuid": "aae751ba-8b97-4259-9579-c40cbb806d9d"
        },
        {
            "cluster_uuid": "ee3ae4de-811a-45b5-b339-f7ad45872c33",
            "tenant": "257d6354-be6d-45ec-b65d-e961d6a1274b",
            "volume_uuid": "ff3ac375-6acd-433e-8b7e-85ce528b85ad"
        }
    ],
    "cluster_uuid": "ee3ae4de-811a-45b5-b339-f7ad45872c33"
}
```

#### 返回示例
```
{
  "message": "success",
  "message_cn": "成功",
  "scode": 0,
  "desc": "",
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
          "cluster_uuid": "ee3ae4de-811a-45b5-b339-f7ad45872c33",
          "cluster_name": "cluster_name_236",
          "cluster_mode": "",
          "tenant": "257d6354-be6d-45ec-b65d-e961d6a1274b",
          "tenant_name": "",
          "multiple": false,
          "vm_type": "",
          "volume_uuid": "aae751ba-8b97-4259-9579-c40cbb806d9d",
          "volume_name": "ken-vm-1-volume1-0",
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
          "cluster_uuid": "ee3ae4de-811a-45b5-b339-f7ad45872c33",
          "cluster_name": "cluster_name_236",
          "cluster_mode": "",
          "tenant": "257d6354-be6d-45ec-b65d-e961d6a1274b",
          "tenant_name": "",
          "multiple": false,
          "vm_type": "",
          "volume_uuid": "ff3ac375-6acd-433e-8b7e-85ce528b85ad",
          "volume_name": "vol-1",
          "owner": ""
        }
      }
    ]
  }
}
```

## /v1/volume/internal/cdp/enable
卷cdp启用（不存在时即创建）
### 请求类型
POST

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
volumes|[]InternalVolumeIdentifier|是|-|卷信息数组

### InternalVolumeIdentifier对象
名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|卷所属集群uuid
tenant|string|否|-|卷所属租户uuid
volume_uuid|string|是|-|卷uuid
volume_name|string|否|-|卷名称

### 返回参数

名称|参数类型|描述
---|---|---
success|int|操作成功数量
fail|int|操作失败数量
results|[]Output|操作结果数组

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/volume/internal/cdp/enable
```

Body:
```
{
    "volumes": [
        {
            "cluster_uuid": "ee3ae4de-811a-45b5-b339-f7ad45872c33",
            "tenant": "257d6354-be6d-45ec-b65d-e961d6a1274b",
            "volume_uuid": "aae751ba-8b97-4259-9579-c40cbb806d9d"
        }
    ],
    "cluster_uuid": "ee3ae4de-811a-45b5-b339-f7ad45872c33"
}
```

#### 返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
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
        "stack": null,
        "data": {
          "cluster_uuid": "ee3ae4de-811a-45b5-b339-f7ad45872c33",
          "cluster_name": "cluster_name_236",
          "cluster_mode": "",
          "tenant": "257d6354-be6d-45ec-b65d-e961d6a1274b",
          "tenant_name": "",
          "multiple": false,
          "vm_type": "",
          "volume_uuid": "aae751ba-8b97-4259-9579-c40cbb806d9d",
          "volume_name": "ken-vm-1-volume1-0",
          "owner": ""
        }
      }
    ]
  }
}
```

## /v1/volume/internal/cdp/disable
卷cdp停用
### 请求类型
POST

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
volumes|[]InternalVolumeIdentifier|是|-|卷信息数组

### InternalVolumeIdentifier对象
名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|卷所属集群uuid
tenant|string|否|-|卷所属租户uuid
volume_uuid|string|是|-|卷uuid
volume_name|string|否|-|卷名称

### 返回参数

名称|参数类型|描述
---|---|---
success|int|操作成功数量
fail|int|操作失败数量
results|[]Output|操作结果数组

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/volume/internal/cdp/disable
```

Body:
```
{
    "volumes": [
        {
            "cluster_uuid": "ee3ae4de-811a-45b5-b339-f7ad45872c33",
            "tenant": "257d6354-be6d-45ec-b65d-e961d6a1274b",
            "volume_uuid": "aae751ba-8b97-4259-9579-c40cbb806d9d"
        }
    ],
    "cluster_uuid": "ee3ae4de-811a-45b5-b339-f7ad45872c33"
}
```

#### 返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
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
        "stack": null,
        "data": {
          "cluster_uuid": "ee3ae4de-811a-45b5-b339-f7ad45872c33",
          "cluster_name": "cluster_name_236",
          "cluster_mode": "",
          "tenant": "257d6354-be6d-45ec-b65d-e961d6a1274b",
          "tenant_name": "",
          "multiple": false,
          "vm_type": "",
          "volume_uuid": "aae751ba-8b97-4259-9579-c40cbb806d9d",
          "volume_name": "ken-vm-1-volume1-0",
          "owner": ""
        }
      }
    ]
  }
}
```

## /v1/volume/internal/cdp/list
卷cdp列表
### 请求类型
GET

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|否|-|租户uuid
filter_name|string|否|-|过滤关键字
page_num|int|否|-|页码
page_size|int|否|-|页长

### 返回参数

名称|参数类型|描述
---|---|---
TotalCount|int|总数
List|[]InternalVolumeCdpListInfo|卷cdp信息数组
each_range_list_state|[]EachResourceRangeListState|集群的操作结果数组

### InternalVolumeCdpListInfo对象
名称|参数类型|描述
---|---|---
cluster_uuid|string|集群uuid
cluster_name|string|集群名称
cluster_mode|string|集群模式
tenant|string|租户uuid
tenant_name|string|租户名称
volume_uuid|string|卷uuid
volume_name|string|卷名称
vm_name|string|卷所属虚拟机名称
vm_uuid|string|卷所属虚拟机uuid
reserve_duration|uint64|可恢复最近时长
reserve_capacity|uint64|占用CDP盘最大空间
cdp_create_time|int64|cdp创建时间
cdp_state|string|cdp启用状态
cdp_priority|string|恢复优先级

### EachResourceRangeListState对象
名称|参数类型|描述
---|---|---
cluster_uuid|string|集群uuid
cluster_name|string|集群名称
cluster_mode|string|集群模式
namespace_uuid|string|命名空间uuid
result|Output|结果
total_count|int|总数

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/volume/internal/cdp/list?tenant=257d6354-be6d-45ec-b65d-e961d6a1274b&filter_name=&page_num=0&page_size=10&cluster_uuid=ee3ae4de-811a-45b5-b339-f7ad45872c33
```

#### 返回示例
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
        "cluster_uuid": "ee3ae4de-811a-45b5-b339-f7ad45872c33",
        "cluster_name": "cluster_name_236",
        "cluster_mode": "",
        "tenant": "257d6354-be6d-45ec-b65d-e961d6a1274b",
        "tenant_name": "ken",
        "volume_uuid": "aae751ba-8b97-4259-9579-c40cbb806d9d",
        "volume_name": "ken-vm-1-volume1-0",
        "vm_name": "ken-vm-1",
        "vm_uuid": "25ebed59-522a-4779-9f38-b483b551e7fa",
        "reserve_duration": 86400,
        "reserve_capacity": 32212254720,
        "cdp_create_time": 1630053321,
        "cdp_state": "off",
        "cdp_priority": "mid"
      },
      {
        "cluster_uuid": "ee3ae4de-811a-45b5-b339-f7ad45872c33",
        "cluster_name": "cluster_name_236",
        "cluster_mode": "",
        "tenant": "257d6354-be6d-45ec-b65d-e961d6a1274b",
        "tenant_name": "ken",
        "volume_uuid": "ff3ac375-6acd-433e-8b7e-85ce528b85ad",
        "volume_name": "vol-1",
        "vm_name": "",
        "vm_uuid": "",
        "reserve_duration": 86400,
        "reserve_capacity": 32212254720,
        "cdp_create_time": 1630053321,
        "cdp_state": "off",
        "cdp_priority": "mid"
      }
    ],
    "each_range_list_state": [
      {
        "cluster_uuid": "ee3ae4de-811a-45b5-b339-f7ad45872c33",
        "cluster_name": "cluster_name_236",
        "cluster_mode": "",
        "namespace_uuid": "6a2cef30-d8f8-4268-aad0-172834d95768",
        "result": {
          "scode": 0,
          "desc": "",
          "message": "success",
          "message_cn": "成功",
          "stack": null,
          "data": ""
        },
        "total_count": 2
      }
    ]
  }
}
```

## /v1/volume/internal/cdp/info
卷cdp信息
### 请求类型
GET

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|否|-|租户uuid
volume_uuid|string|是|-|卷uuid
volume_name|string|否|-|卷名称

### 返回参数

名称|参数类型|描述
---|---|---
cdp_info|[]CdpInfoResponse|cdp信息数组
host_uuid|string|主机uuid

### CdpInfoResponse对象
名称|参数类型|描述
---|---|---
snaps|[]CdpSnapshotInfo|cdp快照信息数组
seq|uint64|序号
startTime|uint64|开始时间
use|uint64|已用空间
capacity|uint64|容量
ioStartTime|uint64|io开始时间
ioLastTime|uint64|io结束时间
online|bool|状态
usd_maddr|string|承载主机ip
usd_path|string|承载盘


### CdpSnapshotInfo对象
名称|参数类型|描述
---|---|---
name|string|io快照名
time|uint64|io快照创建时间

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/volume/internal/cdp/info?tenant=257d6354-be6d-45ec-b65d-e961d6a1274b&volume_uuid=aae751ba-8b97-4259-9579-c40cbb806d9d&volume_name=ken-vm-1-volume1-0&cluster_uuid=ee3ae4de-811a-45b5-b339-f7ad45872c33
```

#### 返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "cdp_info": [
      {
        "status": {
          "code": 0,
          "message": "",
          "messageCn": "",
          "stack": null,
          "desc": "",
          "UUID": ""
        },
        "snaps": [
          {
            "name": "CDP-auto-1630057893",
            "time": 1630057893506590075
          },
          {
            "name": "CDP-auto-1630057911",
            "time": 1630057911140129264
          }
        ],
        "seq": 0,
        "startTime": 1630057893420086896,
        "use": 38,
        "capacity": 10737418240,
        "ioStartTime": 1630057911140129264,
        "ioLastTime": 1630057911140129264,
        "online": true,
        "usd_maddr": "10.30.12.237",
        "usd_path": "/dev/sdd"
      }
    ],
    "host_uuid": ""
  }
}
```


## /v1/volume/internal/cdp/clean
卷cdp删除
### 请求类型
POST

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|否|-|租户uuid
volume_uuid|string|是|-|卷uuid
volume_name|string|否|-|卷名称
usd_seq|uint64|否|-|需要删除的io快照序号（不传则删除卷cdp，传则删除卷cdp的某一条io日志信息）

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/volume/internal/cdp/clean
```

Body:
```
{
    "usd_seq": 0,
    "tenant": 257d6354-be6d-45ec-b65d-e961d6a1274b，
    "volume_uuid": "aae751ba-8b97-4259-9579-c40cbb806d9",
    "volume_name": "ken-vm-1-volume1-0",
    "cluster_uuid": ee3ae4de-811a-45b5-b339-f7ad45872c33
}
```

#### 返回示例
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

## /v1/volume/internal/cdp/view
卷cdp查看
### 请求类型
POST

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
op|string|是|-|操作
snapshot_name|string|是|-|io快照名称
tenant|string|否|-|租户uuid
timestamp|uint64|是|-|选择查看的时间戳
volume_uuid|string|是|-|卷uuid
volume_name|string|否|-|卷名称

### 返回参数

名称|参数类型|描述
---|---|---
cdp_info|[]CdpInfoResponse|cdp信息数组
host_uuid|string|主机uuid

### CdpInfoResponse对象
名称|参数类型|描述
---|---|---
snaps|[]CdpSnapshotInfo|cdp快照信息数组
seq|uint64|序号
startTime|uint64|开始时间
use|uint64|已用空间
capacity|uint64|容量
ioStartTime|uint64|io开始时间
ioLastTime|uint64|io结束时间
online|bool|状态
usd_maddr|string|承载主机ip
usd_path|string|承载盘


### CdpSnapshotInfo对象
名称|参数类型|描述
---|---|---
name|string|io快照名
time|uint64|io快照创建时间

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/volume/internal/cdp/view
```

Body:
```
{
    "cluster_uuid": "ee3ae4de-811a-45b5-b339-f7ad45872c33",
    "op": "on",
    "snapshot_name": "CDP-auto-1630060807",
    "tenant": "257d6354-be6d-45ec-b65d-e961d6a1274b",
    "timestamp": 1630060862000000000,
    "volume_name": "cdp-1",
    "volume_uuid": "ddc4adf3-830e-4ec3-b1dc-85571aea15c7"
}
```

#### 返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "cdp_info": null,
    "host_uuid": "48459090-6ced-4476-a6b4-2880b1e21d5a"
  }
}
```

## /v1/volume/internal/cdp/revert
卷cdp回滚
### 请求类型
POST

### 请求参数

名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
snapshot_name|string|是|-|io快照名称
tenant|string|否|-|租户uuid
timestamp|uint64|是|-|选择回滚的时间戳
volume_uuid|string|是|-|卷uuid
volume_name|string|否|-|卷名称

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/volume/internal/cdp/revert
```

Body:
```
{
    "cluster_uuid": "ee3ae4de-811a-45b5-b339-f7ad45872c33",
    "snapshot_name": "CDP-auto-1630060807",
    "tenant": "257d6354-be6d-45ec-b65d-e961d6a1274b",
    "timestamp": 1630060862000000000,
    "volume_name": "cdp-1",
    "volume_uuid": "ddc4adf3-830e-4ec3-b1dc-85571aea15c7"
}
```

#### 返回示例
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