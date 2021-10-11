## /v1/bare_metal/instance_add
#### 功能：裸金属实例添加
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid| string| 是|- | 集群uuid
 tenant| string| 是|- | 租户uuid

### node对象
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 name| string| 是| -| 实例名称
 zone_uuid| string | 是| -| 资源池uuid
 object_group| string| 是| -| 分组uuid
 os| string| 是| CentOS x64| 实例操作系统类型
 bm_host_uuid| string| 是| -| 裸金属主机uuid
 cpu_cores| int32| 是| -| 裸金属主机cpu大小
 mem_total| uint64| 是| -| 裸金属主机内存大小
 owner| string| 否| -| 用户uuid


### stroge_info对象
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
 --- |---|---|--- |---
 image_name| string| 是| -| 镜像名称
 repository_uuid| string| 是| -| 镜像仓库uuid
 system_disk| object| 是| -| 导入镜像磁盘信息

### system_disk对象
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
 --- |---|---|--- |---
 target_device| string| 是| -| 导入镜像磁盘


### 返回参数
 名称|参数类型|描述
 ---|---|---
 bm_instance_uuid| string| 裸金属实例uuid
 bm_instance_name| string| 裸金属实例名称



### 示例

#### 请求示例
```
http://localhost:9990/v1/bare_metal/instance_add
```
Body:
```
{
	"cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
	"tenant": "82300f99-a7e9-45bb-83cb-ca8b946b083e",
	"node": {
		"name": "111",
		"object_group": "658b8f67-e862-4770-ac17-77109cb6028b",
		"zone_uuid": "ac776392-dbf1-4272-b88b-4b2ac886cacb",
		"bm_host_uuid": "a3307502-f631-4304-905e-ccb1aecb589e",
		"os": "CentOS x64",
		"cpu_cores": 2,
		"mem_total": 4130054144,
		"mac": "",
		"owner": ""
	},
	"stroge_info": {
		"repository_uuid": "63619a2f-99a3-4e3e-8701-c01bd0accfee",
		"image_name": "xenial-server-cloudimg-amd64-disk1.img",
		"system_disk": {
			"target_device": "/dev/sda"
		},
	}
}
```
#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "bm_instance_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "bm_instance_name": "name"
  }
}
```

#### 异常返回示例

### 状态码


## /v1/bare_metal/instance_delete
#### 功能：裸金属实例添加
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid| string| 是|- | 集群uuid
 tenant| string| 是|- | 租户uuid
 bm_instance_uuid| string| 是|- | 裸金属实例uuid
 bm_instance_name| string| 否|- | 裸金属实例名称

### 返回参数
 名称|参数类型|描述
 ---|---|---
 bm_instance_uuid| string| 裸金属实例uuid
 bm_instance_name| string| 裸金属实例名称



### 示例

#### 请求示例
```
http://localhost:9990/v1/bare_metal/instance_delete
```
Body:
```
{
	"cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
	"tenant": "82300f99-a7e9-45bb-83cb-ca8b946b083e",
	"bm_instance_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
	"bm_instance_name": "name",
}
```
#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "bm_instance_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "bm_instance_name": "name"
  }
}
```

#### 异常返回示例

### 状态码



## /v1/bare_metal/instance_start
#### 功能：裸金属实例开机
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid| string| 是|- | 集群uuid
 tenant| string| 是|- | 租户uuid
 bm_instance_uuid| string| 是|- | 裸金属实例uuid
 bm_instance_name| string| 否|- | 裸金属实例名称

### 返回参数
 名称|参数类型|描述
 ---|---|---
 bm_instance_uuid| string| 裸金属实例uuid
 bm_instance_name| string| 裸金属实例名称



### 示例

#### 请求示例
```
http://localhost:9990/v1/bare_metal/instance_start
```
Body:
```
{
	"cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
	"tenant": "82300f99-a7e9-45bb-83cb-ca8b946b083e",
	"bm_instance_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
	"bm_instance_name": "name",
}
```
#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "bm_instance_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "bm_instance_name": "name"
  }
}
```

#### 异常返回示例

### 状态码


## /v1/bare_metal/instance_shutdown
#### 功能：裸金属实例关机
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid| string| 是|- | 集群uuid
 tenant| string| 是|- | 租户uuid
 bm_instance_uuid| string| 是|- | 裸金属实例uuid
 bm_instance_name| string| 否|- | 裸金属实例名称

### 返回参数
 名称|参数类型|描述
 ---|---|---
 bm_instance_uuid| string| 裸金属实例uuid
 bm_instance_name| string| 裸金属实例名称



### 示例

#### 请求示例
```
http://localhost:9990/v1/bare_metal/instance_shutdown
```
Body:
```
{
	"cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
	"tenant": "82300f99-a7e9-45bb-83cb-ca8b946b083e",
	"bm_instance_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
	"bm_instance_name": "name",
}
```
#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
  }
}
```

#### 异常返回示例

### 状态码


## /v1/bare_metal/instance_reset
#### 功能：裸金属实例重启
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid| string| 是|- | 集群uuid
 tenant| string| 是|- | 租户uuid
 bm_instance_uuid| string| 是|- | 裸金属实例uuid
 bm_instance_name| string| 否|- | 裸金属实例名称

### 返回参数
 名称|参数类型|描述
 ---|---|---
 bm_instance_uuid| string| 裸金属实例uuid
 bm_instance_name| string| 裸金属实例名称



### 示例

#### 请求示例
```
http://localhost:9990/v1/bare_metal/instance_reset
```
Body:
```
{
	"cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
	"tenant": "82300f99-a7e9-45bb-83cb-ca8b946b083e",
	"bm_instance_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
	"bm_instance_name": "name",
}
```
#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
  }
}
```

#### 异常返回示例

### 状态码


## /v1/bare_metal/instance_list
#### 功能：裸金属实例列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid| string| 是|- | 集群uuid
 tenant| string| 否|- | 租户uuid
 filter_name| string| 否|- | 按名称过滤
 filter_uuid| string| 否|- | 按uuid过滤
 filter_fuzzy| string| 否|- | 按模糊规则过滤
 filter_user_uuid| string| 否|- | 按用户过滤
 page_num|int|否|0|显示页码
 page_size|int|否|0|每页显示多少数据


### 返回参数
 名称|参数类型|描述
 ---|---|---


### 示例

#### 请求示例
```
http://localhost:9990/v1/bare_metal/instance_list?tenant=82300f99-a7e9-45bb-83cb-ca8b946b083e&page_num=0&page_size=10&filter_fuzzy=&cluster_uuid=232671ca-d1e7-44ea-9278-a7c2d5920fa7
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
    "lists": [
      {
        "cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
        "cluster_name": "cluster_name_37",
        "tenant": "82300f99-a7e9-45bb-83cb-ca8b946b083e",
        "tenant_name": "zhangqi",
        "owner_is_ldap": false,
        "owner": "",
        "owner_name": "",
        "uuid": "a2df5e85-58e3-48ec-ab65-8d671970b698",
        "name": "2222",
        "create_time": 1629704470,
        "modify_time": 1629704473,
        "power_status": "on",
        "agent_state": "disconnected",
        "action": 2,
        "os": "CentOS x64",
        "mac": "",
        "create_type": "bms",
        "namespace": "cadb1027-3a5b-4012-97d3-8092feca912c",
        "attr": null,
        "object_group": "658b8f67-e862-4770-ac17-77109cb6028b",
        "object_group_name": "default",
        "zone_uuid": "ac776392-dbf1-4272-b88b-4b2ac886cacb",
        "zone_name": "default",
        "ip": "",
        "bm_host_uuid": "a3307502-f631-4304-905e-ccb1aecb589e",
        "cpu_cores": 2,
        "mem_total": 4130054144,
        "bm_host_name": "host-14",
        "storage_info": {
          "system_disk": {
            "target_device": "/dev/sda"
          },
          "image_name": "xenial-server-cloudimg-amd64-disk1.img",
          "repository_uuid": "63619a2f-99a3-4e3e-8701-c01bd0accfee"
        },
      }
    ],
    "total_count": 1,
    "each_range_list_state": [
      {
        "cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
        "cluster_name": "cluster_name_37",
        "namespace_uuid": "cadb1027-3a5b-4012-97d3-8092feca912c",
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
    ],
    "object_group_counts": {
      "658b8f67-e862-4770-ac17-77109cb6028b": 1
    }
  }
}
```

#### 异常返回示例

### 状态码



## /v1/bare_metal/instance_get
#### 功能：裸金属实例详情
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid| string| 是|- | 集群uuid
 tenant| string| 否|- | 租户uuid
 bm_instance_uuid| string| 是|- | 裸金属实例uuid
 bm_instance_name| string| 否|- | 裸金属实例名称
 zone_uuid| string| 否|- | 资源池uuid


### 返回参数
 名称|参数类型|描述
 ---|---|---


### 示例

#### 请求示例
```
http://localhost:9990/v1/bare_metal/instance_get?cluster_uuid=232671ca-d1e7-44ea-9278-a7c2d5920fa7&zone_uuid=ac776392-dbf1-4272-b88b-4b2ac886cacb&bm_instance_uuid=a2df5e85-58e3-48ec-ab65-8d671970b698&bm_instance_name=2222
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
    "cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
    "cluster_name": "cluster_name_37",
    "data": {
      "tenant": "82300f99-a7e9-45bb-83cb-ca8b946b083e",
      "tenant_name": "zhangqi",
      "owner_is_ldap": false,
      "owner": "",
      "owner_name": "",
      "uuid": "a2df5e85-58e3-48ec-ab65-8d671970b698",
      "name": "2222",
      "create_time": 1629704470,
      "modify_time": 1629704473,
      "power_status": "on",
      "agent_state": "disconnected",
      "action": 2,
      "os": "CentOS x64",
      "mac": "",
      "create_type": "bms",
      "namespace": "cadb1027-3a5b-4012-97d3-8092feca912c",
      "attr": null,
      "object_group": "658b8f67-e862-4770-ac17-77109cb6028b",
      "object_group_name": "",
      "zone_uuid": "ac776392-dbf1-4272-b88b-4b2ac886cacb",
      "zone_name": "default",
      "ip": "",
      "bm_host_uuid": "a3307502-f631-4304-905e-ccb1aecb589e",
      "cpu_cores": 2,
      "mem_total": 4130054144,
      "bm_host_name": "host-14",
      "storage_info": {
        "system_disk": {
          "target_device": "/dev/sda"
        },
        "image_name": "xenial-server-cloudimg-amd64-disk1.img",
        "repository_uuid": "63619a2f-99a3-4e3e-8701-c01bd0accfee"
      },
    }
  }
}
```

#### 异常返回示例

### 状态码



## /v1/bare_metal/instance_import/progress
#### 功能：裸金属实例镜像导入进度
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid| string| 是|- | 集群uuid
 tenant| string| 否|- | 租户uuid
 bm_instance_uuid| string| 是|- | 裸金属实例uuid


### 返回参数
 名称|参数类型|描述
 ---|---|---
 bm_instance_uuid| string| 裸金属实例uuid
 bm_instance_name| string| 裸金属实例名称
 progress| int32| 导入进度


### 示例

#### 请求示例
```
http://localhost:9990/v1/bare_metal/instance_import/progress?cluster_uuid=43ba460e-23eb-41bf-9764-3406daf92c09&tenant=bcb8f422-81c8-4f92-90d0-20c647135f1e&bm_instance_uuid=cefa5174-a07e-41e6-8e54-16ea26c1ae67
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
		"bm_instance_uuid": "",
		"bm_instance_name": "",
		"progress": 79
	}
}
```

#### 异常返回示例

### 状态码


