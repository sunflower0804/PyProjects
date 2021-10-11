[back to api overview](../api_overview.md#label_api)

### 主机相关接口
## /v1/host/list/overview
主机列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 filter_host_name|string|否|-|过滤主机名称
 filter_zone_uuid|string|否|-|过滤出所在子集群的主机
 filter_healthy_only|bool|否|-|过滤出健康主机
 filter_service_type|string|是|-|过滤主机服务类型,创建卷时需要的主机选vsm类型
 page_num|int|否|0|第几页
 page_size|int|否|0|每页条数
### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.212:8080/v1/host/list/overview?filter_host_name=&page_num=0&filter_not_system_service=true&page_size=10&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
        "domain_name": "dom186190",
        "node": {
          "host_uuid": "f6db6e80-642f-4335-8b00-71f84809dfad",
          "domain_uuid": "35eb616c-7f1b-4ff6-bf58-586e0114f988",
          "host_name": "192.168.201.186",
          "is_system_service": false,
          "manager_net": {
            "name": "manager",
            "cidr_addrs": [
              "192.168.201.186/24",
              "fe80::d834:60ff:fea0:2443/64"
            ],
            "mtu": 1500,
            "bridge_uuid": "",
            "bridge_name": ""
          },
          "compute_net": null,
          "storage_net": {
            "name": "12321",
            "cidr_addrs": [
              "10.30.11.186/24"
            ],
            "mtu": 1500,
            "bridge_uuid": "",
            "bridge_name": ""
          },
          "backup_net": {
            "name": "12321",
            "cidr_addrs": [
              "10.30.11.186/24"
            ],
            "mtu": 1500,
            "bridge_uuid": "",
            "bridge_name": ""
          }
        },
        "boot_time": 1572570175,
        "cpu_cores": 10,
        "cpu_usage": 9.624437343159201,
        "memory_size": 9419456512,
        "memory_usage": 55.975026003708365,
        "disk_hdd_num": 10,
        "disk_sdd_num": 0,
        "gigabit_network_card_num": 2,
        "ten_gigabit_network_card_num": 0,
        "service_enable_list": [
          "usm",
          "vsm",
          "hyper"
        ],
        "services_state": {
          "manager": null,
          "center": null,
          "hyper": {
            "enabled": true,
            "mode": 0,
            "status": 1
          },
          "network": null,
          "usm": {
            "enabled": true,
            "mode": 0,
            "status": 1
          },
          "vsm": {
            "enabled": true,
            "mode": 0,
            "status": 1
          }
        },
        "labels": {},
        "agent_status": 1,
        "host_mode": 0,
        "setting": {
          "DPMAllowed": false,
          "IPMI": {
            "BMCIP": "1.1.1.1",
            "BMCUsername": "weiwei",
            "BMCPassword": "1231111111111",
            "BMCMAC": ""
          }
        }
      }
    ],
    "total_count": 1
  }
}
```

#### 异常返回示例

### 状态码



## /v1/host/get
主机详情
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 host_uuid|string|是|-|主机uuid
### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.212:8080/v1/host/get?domain_uuid=All&host_uuid=f6db6e80-642f-4335-8b00-71f84809dfad&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
    "host": {
      "label": {},
      "node": {
        "host_uuid": "f6db6e80-642f-4335-8b00-71f84809dfad",
        "domain_uuid": "35eb616c-7f1b-4ff6-bf58-586e0114f988",
        "host_name": "192.168.201.186",
        "is_system_service": false,
        "manager_net": {
          "name": "manager",
          "cidr_addrs": [
            "192.168.201.186/24",
            "fe80::d834:60ff:fea0:2443/64"
          ],
          "mtu": 1500,
          "bridge_uuid": "",
          "bridge_name": ""
        },
        "compute_net": null,
        "storage_net": {
          "name": "12321",
          "cidr_addrs": [
            "10.30.11.186/24"
          ],
          "mtu": 1500,
          "bridge_uuid": "",
          "bridge_name": ""
        },
        "backup_net": {
          "name": "12321",
          "cidr_addrs": [
            "10.30.11.186/24"
          ],
          "mtu": 1500,
          "bridge_uuid": "",
          "bridge_name": ""
        }
      },
      "service_enable_list": [
        "usm",
        "vsm",
        "hyper"
      ],
      "agent_status": 1,
      "host_hyper": {
        "ksm_enabled": true,
        "ple_enabled": true,
        "huge_pages_total": 0,
        "transparency_huge_pages_state": "madvise",
        "nested_enabled": true
      },
      "setting": {
        "DPMAllowed": false,
        "IPMI": {
          "BMCIP": "1.1.1.1",
          "BMCUsername": "weiwei",
          "BMCPassword": "1231111111111",
          "BMCMAC": ""
        }
      },
      "host_cpu": {
        "CPUSocket": 10,
        "CPUCores": 10,
        "CPUMHz": 2199.996,
        "CPUReserved": 0,
        "Baseline": "Westmere"
      },
      "host_mode": 0
    }
  }
}
```

#### 异常返回示例

### 状态码



## /v1/host/add
添加主机
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
http://10.30.10.23:8080/v1/host/add
```

Body:
```
{
	"node": {
		"domain_uuid": "728fbb03-d15d-4f0d-9d8b-74c5316fdea4",
		"host_name": "10.30.12.77",
		"manager_net": {
			"name": "manager",
			"cidr_addrs": [
				"10.30.12.77/24",
				"fe80::d42a:58ff:fe5e:fa4a/64"
			]
		},
		"storage_net": {
			"name": "manager",
			"cidr_addrs": [
				"10.30.12.77/24",
				"fe80::d42a:58ff:fe5e:fa4a/64"
			]
		}
	},
	"cluster_uuid": "667822c9-fec0-43ca-94dc-68ed45becce3"
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
    "ip": "",
    "port": 0
  }
}
```

#### 异常返回示例

### 状态码



## /v1/host/delete
删除主机
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
http://10.30.10.23:8080/v1/host/delete
```

Body:
```
{
	"domain_uuid": "728fbb03-d15d-4f0d-9d8b-74c5316fdea4",
	"host_uuid": "8b4650b1-b881-4632-ad98-1d8523289925",
	"host_name": "domin-68",
	"cluster_uuid": "667822c9-fec0-43ca-94dc-68ed45becce3"
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
    "ip": "",
    "port": 0
  }
}
```

#### 异常返回示例

### 状态码


## /v1/host/label/attach
主机引用标签
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
http://10.30.10.23:8080/v1/host/label/attach
```

Body:
```
{
	"host_uuid": "07bc76c4-ce06-4383-988d-8dd4ee493012",
	"label": {
		"system::secret": "force"
	},
	"host_name": "192.168.201.188",
	"cluster_uuid": "c5793204-f4ed-44ae-977a-63609adf2dcd"
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


## /v1/host/label/detach
主机解除标签
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
http://10.30.10.23:8080/v1/host/label/detach
```

Body:
```
{
	"host_uuid": "07bc76c4-ce06-4383-988d-8dd4ee493012",
	"label": {
		"system::secret": "force"
	},
	"host_name": "192.168.201.188",
	"cluster_uuid": "c5793204-f4ed-44ae-977a-63609adf2dcd"
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


## /v1/host/label/value/update
主机编辑标签
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
http://10.30.10.23:8080/v1/host/label/value/update
```

Body:
```
{
	"host_uuid": "07bc76c4-ce06-4383-988d-8dd4ee493012",
	"label": {
		"system::secret": "optional"
	},
	"host_name": "192.168.201.188",
	"cluster_uuid": "c5793204-f4ed-44ae-977a-63609adf2dcd"
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


## /v1/host/mode/set
主机模式设置
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
http://10.30.10.23:8080/v1/host/mode/set
```

Body:
```
{
	"host_uuid": "07bc76c4-ce06-4383-988d-8dd4ee493012",
	"host_name": "192.168.201.188",
	"mode": 1,
	"cluster_uuid": "c5793204-f4ed-44ae-977a-63609adf2dcd"
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


## /v1/host/service/enable
主机添加服务
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
http://10.30.10.23:8080/v1/host/service/enable
```

Body:
```
{
	"host_uuid": "f6db6e80-642f-4335-8b00-71f84809dfad",
	"domain_uuid": "35eb616c-7f1b-4ff6-bf58-586e0114f988",
	"service_enable_list": [
		"hyper",
		"usm",
		"vsm"
	],
	"host_name": "192.168.201.186",
	"cluster_uuid": "c5793204-f4ed-44ae-977a-63609adf2dcd"
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


## /v1/host/service/disable
主机停止服务
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
http://10.30.10.23:8080/v1/host/service/disable
```

Body:
```
{
	"host_uuid": "f6db6e80-642f-4335-8b00-71f84809dfad",
	"domain_uuid": "35eb616c-7f1b-4ff6-bf58-586e0114f988",
	"service_disable_list": [
		"hyper"
	],
	"host_name": "192.168.201.186",
	"cluster_uuid": "c5793204-f4ed-44ae-977a-63609adf2dcd"
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


## /v1/host/statistic/total
主机统计信息获取
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|
host_uuid|string|是|-|
TODO

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.212:8080/v1/host/statistic/total?cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd&host_uuid=f6db6e80-642f-4335-8b00-71f84809dfad&count=1
```


#### 正常返回示例
```
TODO
```

#### 异常返回示例

### 状态码


## /v1/host/statistic/realtime
主机信息实时统计(所有)
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|
host_uuid|string|是|-|

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://10.30.12.52:8080/v1/host/statistic/realtime?host_uuid=63303ca0-bc20-477a-8fd4-2b5e914be8ff&cluster_uuid=667822c9-fec0-43ca-94dc-68ed45becce3
```


#### 正常返回示例
```
TODO
```

#### 异常返回示例

### 状态码


## /v1/host/statistic/realtime/option
主机信息实时统计(可选需要数据)
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|
host_uuid|string|是|-|
disk|string|否|false|是否获取磁盘信息
load|string|否|false|
mem|string|否|false|
net|string|否|false|
vsm|string|否|false|
usm|string|否|false|
center|string|否|false|
hyper|string|否|false|
network|string|否|false|
sshd|string|否|false|
agent|string|否|false|

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.212:8080/v1/host/statistic/realtime/option?host_uuid=f6db6e80-642f-4335-8b00-71f84809dfad&disk=true&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
```


#### 正常返回示例
```
TODO
```

#### 异常返回示例

### 状态码


## /v1/host/disk/light/on
点亮磁盘定位灯
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
http://10.30.10.23:8080/v1/host/disk/light/on
```

Body:
```
{
	"host_uuid": "f6db6e80-642f-4335-8b00-71f84809dfad",
	"device": "/dev/sdd",
	"host_name": "192.168.201.186",
	"cluster_uuid": "c5793204-f4ed-44ae-977a-63609adf2dcd"
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

## /v1/host/disk/light/off
关闭磁盘定位灯
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
http://10.30.10.23:8080/v1/host/disk/light/off
```

Body:
```
{
	"host_uuid": "f6db6e80-642f-4335-8b00-71f84809dfad",
	"device": "/dev/sdd",
	"host_name": "192.168.201.186",
	"cluster_uuid": "c5793204-f4ed-44ae-977a-63609adf2dcd"
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


## /v1/host/disk/scan
磁盘扫描
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
http://10.30.10.23:8080/v1/host/disk/scan
```

Body:
```
{
	"host_uuid": "f6db6e80-642f-4335-8b00-71f84809dfad",
	"host_name": "192.168.201.186",
	"cluster_uuid": "c5793204-f4ed-44ae-977a-63609adf2dcd"
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


## /v1/host/log/collect
主机日志收集
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
hosts|[]HostIdentifier|是|-|主机信息
start_time|int64|否|0|日志的起始时间
end_time|int64|否|0|日志的终止时间

###HostIdentifier
名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
host_uuid|是|-|主机uuid
host_name|是|-|主机名称

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://10.30.10.23:8080/v1/host/log/collect
```

Body:
```
{
	"hosts": [
		{
			"cluster_uuid": "c123a9ab-1699-482e-aa69-60b68d2d6c7d",
			"host_uuid": "c326ed48-adbc-42ab-8836-a0b43261156c",
			"host_name": "10.30.12.219"
		},
		{
			"cluster_uuid": "c123a9ab-1699-482e-aa69-60b68d2d6c7d",
			"host_uuid": "24ee9e0d-f51f-4ff5-908b-795195bf3d52",
			"host_name": "10.30.12.218"
		}
	],
	"start_time": 1630386133,
	"end_time": 1630396933
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
    "DownloadUrl": "",
    "Collecting": false
  }
}
```

#### 异常返回示例

### 状态码


## /v1/host/log/check
检查日志收集的状态
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|
host_uuid|string|是|-|

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.212:8080/v1/host/log/check?cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd&host_uuid=f6db6e80-642f-4335-8b00-71f84809dfad
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
    "DownloadUrl": "",
    "Collecting": true
  }
}
```

#### 异常返回示例

### 状态码

## /v1/host/usb/list
主机usb列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|
host_uuid|string|是|-|
page_num|int|否|0|第几页
page_size|int|否|0|每页显示条数

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.212:8080/v1/host/usb/list?page_num=0&page_size=10&host_uuid=f6db6e80-642f-4335-8b00-71f84809dfad&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
    "total_count": 4,
    "list": [
      {
        "name": "usb_usb4",
        "usage": "",
        "bus": 4,
        "device": 1,
        "product_id": "0x0003",
        "product_name": "3.0 root hub",
        "vendor_id": "0x1d6b",
        "vendor_name": "Linux Foundation"
      },
      {
        "name": "usb_usb3",
        "usage": "",
        "bus": 3,
        "device": 1,
        "product_id": "0x0002",
        "product_name": "2.0 root hub",
        "vendor_id": "0x1d6b",
        "vendor_name": "Linux Foundation"
      },
      {
        "name": "usb_usb2",
        "usage": "",
        "bus": 2,
        "device": 1,
        "product_id": "0x0001",
        "product_name": "1.1 root hub",
        "vendor_id": "0x1d6b",
        "vendor_name": "Linux Foundation"
      },
      {
        "name": "usb_usb1",
        "usage": "",
        "bus": 1,
        "device": 1,
        "product_id": "0x0002",
        "product_name": "2.0 root hub",
        "vendor_id": "0x1d6b",
        "vendor_name": "Linux Foundation"
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码



## /v1/host/ipmi_setting/update
主机设置IPMI
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
http://10.30.10.23:8080/v1/host/ipmi_setting/update
```

Body:
```
{
	"host_uuid": "6040ac60-6c0d-46f6-9af6-90e522e41fe9",
	"host_name": "192.168.201.187",
	"setting": {
		"IPMI": {
			"BMCIP": "1.1.1.1",
			"BMCUsername": "111",
			"BMCPassword": "111",
			"BMCMAC": ""
		}
	},
	"cluster_uuid": "c5793204-f4ed-44ae-977a-63609adf2dcd"
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



## /v1/host/gateway/update
主机网关设置
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
http://10.30.10.23:8080/v1/host/gateway/update
```

Body:
```
{
	"host_ip": "192.168.201.186",
	"host_name": "192.168.201.186",
	"gateway_ip": "1.1.1.1",
	"network_name": "manage",
	"cluster_uuid": "c5793204-f4ed-44ae-977a-63609adf2dcd"
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



## /v1/host/network/list
主机网路列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 filter_zone_uuid|string|是|-|过滤出所在子集群的主机
 page_num|int|否|0|第几页
 page_size|int|否|0|每页条数


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://10.30.12.37:8080/v1/host/network/list?page_num=0&page_size=10&cluster_uuid=232671ca-d1e7-44ea-9278-a7c2d5920fa7&filter_zone_uuid=ac776392-dbf1-4272-b88b-4b2ac886cacb
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
        "host_uuid": "d9018863-713a-44d9-93b3-cd743d4e32e3",
        "domain_uuid": "fc157bc1-cc21-421c-b292-144d7727110a",
        "host_name": "10.30.12.37",
        "is_system_service": true,
        "manager_net": {
          "name": "eth0",
          "cidr_addrs": [
            "10.30.12.37/24"
          ],
          "mtu": 0,
          "bridge_uuid": "",
          "bridge_name": "",
          "gateways": [
            "10.30.12.1",
            "10.30.12.1"
          ]
        },
        "compute_net": null,
        "storage_net": {
          "name": "eth0",
          "cidr_addrs": [
            "10.30.12.37/24"
          ],
          "mtu": 0,
          "bridge_uuid": "",
          "bridge_name": "",
          "gateways": null
        },
        "backup_net": {
          "name": "eth0",
          "cidr_addrs": [
            "10.30.12.37/24"
          ],
          "mtu": 0,
          "bridge_uuid": "",
          "bridge_name": "",
          "gateways": null
        },
        "zone_uuid": "ac776392-dbf1-4272-b88b-4b2ac886cacb",
        "zone_name": "default"
      },
      {
        "host_uuid": "7e0585f6-67da-47b6-a083-9f58d604c146",
        "domain_uuid": "41aed8e3-fa4d-469a-8782-8a6b6660f72d",
        "host_name": "10.30.12.120",
        "is_system_service": false,
        "manager_net": {
          "name": "manager",
          "cidr_addrs": [
            "10.30.12.120/24"
          ],
          "mtu": 0,
          "bridge_uuid": "",
          "bridge_name": "",
          "gateways": [
            "10.30.12.1"
          ]
        },
        "compute_net": {
          "pxe": {
            "name": "pxeeth",
            "cidr_addrs": null,
            "mtu": 1500,
            "bridge_uuid": "",
            "bridge_name": "br-pxe",
            "gateways": null
          }
        },
        "storage_net": {
          "name": "storage",
          "cidr_addrs": [
            "10.30.12.120/24"
          ],
          "mtu": 0,
          "bridge_uuid": "",
          "bridge_name": "",
          "gateways": null
        },
        "backup_net": {
          "name": "storage",
          "cidr_addrs": [
            "10.30.12.120/24"
          ],
          "mtu": 0,
          "bridge_uuid": "",
          "bridge_name": "",
          "gateways": null
        },
        "zone_uuid": "ac776392-dbf1-4272-b88b-4b2ac886cacb",
        "zone_name": "default"
      },
      {
        "host_uuid": "81310d15-14f4-497f-956b-ca0b8fd6c44e",
        "domain_uuid": "fc157bc1-cc21-421c-b292-144d7727110a",
        "host_name": "GNW10.30.12.10",
        "is_system_service": true,
        "manager_net": {
          "name": "eth0",
          "cidr_addrs": [
            "10.30.12.10/24"
          ],
          "mtu": 1500,
          "bridge_uuid": "",
          "bridge_name": "",
          "gateways": [
            "10.30.12.1"
          ]
        },
        "compute_net": null,
        "storage_net": {
          "name": "eth0",
          "cidr_addrs": [
            "10.30.12.10/24"
          ],
          "mtu": 1500,
          "bridge_uuid": "",
          "bridge_name": "",
          "gateways": null
        },
        "backup_net": {
          "name": "eth0",
          "cidr_addrs": [
            "10.30.12.10/24"
          ],
          "mtu": 1500,
          "bridge_uuid": "",
          "bridge_name": "",
          "gateways": null
        },
        "zone_uuid": "ac776392-dbf1-4272-b88b-4b2ac886cacb",
        "zone_name": "default"
      }
    ],
    "total_count": 3
  }
}
```

#### 异常返回示例

### 状态码


## v1/host/networkconfig/update
主机网路修改
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 node| HostNode object|是|-| 主机参数


### HostNode对象
  名称 | 参数类型 | 是否必填 | 默认值 | 描述
 --- |---|---|--- |---
 host_uuid|string|是|-| 主机uuid
 domain_uuid|string|是|-| 主机所属保护域uuid
 manager_net|NetInfo对象|否|-| 主机管理网络
 storage_net|NetInfo对象|否|-| 主机存储网络


### NetInfo对象对象
 name| string| 是|- | 网卡名
 cidr_addrs| []string|是 |- | 网卡子网和网卡子网掩码组成的cidr地址
 gateways| string|是 |- | 网关
 mtu| int32| 否|- | mtu

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://10.30.10.23:8080/v1/host/networkconfig/update
```

Body:
```
{
	"cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
	"node": {
		"host_uuid": "7e0585f6-67da-47b6-a083-9f58d604c146",
		"domain_uuid": "41aed8e3-fa4d-469a-8782-8a6b6660f72d",
		"manager_net": {
			"name": "manager",
			"cidr_addrs": [
				"10.30.12.120/24"
			],
			"gateways": [
				"10.30.12.1"
			]
		},
		"storage_net": {
			"name": "storage",
			"cidr_addrs": [
				"10.30.12.120/24"
			],
			"gateways": [
				"10.30.12.1"
			]
		}
	}
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


## v1/host/adapter/list
主机网络设备列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 host_ip| string|是|-| 主机ip

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://10.30.12.37:8080/v1/host/adapter/list?cluster_uuid=232671ca-d1e7-44ea-9278-a7c2d5920fa7&host_ip=10.30.12.120
```
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
    "adapters": [
      {
        "Name": "managerbr",
        "Type": 1,
        "IPAddr": [
          "10.30.12.120/24",
          "fe80::a952:bc4a:1caf:e420/64"
        ],
        "Gateway": "10.30.12.1",
        "Bandwidth": -1,
        "Status": "up",
        "MTU": 1500,
        "Mac": "d2:3e:c1:ca:1f:42",
        "Ifaces": [
          {
            "Addrs": null,
            "Mac": "52:56:ff:0c:ff:98",
            "Name": "ens5",
            "Bandwidth": -1,
            "MTU": 1500,
            "Status": "up"
          }
        ]
      },
      {
        "Name": "storagebr",
        "Type": 2,
        "IPAddr": null,
        "Gateway": "",
        "Bandwidth": 0,
        "Status": "unknown",
        "MTU": 1500,
        "Mac": "c6:34:3f:61:95:49",
        "Ifaces": []
      },
      {
        "Name": "br-pxe",
        "Type": 3,
        "IPAddr": null,
        "Gateway": "",
        "Bandwidth": -1,
        "Status": "up",
        "MTU": 1500,
        "Mac": "5e:81:2f:c2:ba:45",
        "Ifaces": [
          {
            "Addrs": [
              "fe80::b5b2:fa10:58ae:f283/64"
            ],
            "Mac": "52:56:ff:71:84:49",
            "Name": "ens7",
            "Bandwidth": -1,
            "MTU": 1500,
            "Status": "up"
          }
        ]
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码



## v1/host/dns/get
主机dns列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 host_ip| string|是|-| 主机ip

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://10.30.12.37:8080/v1/host/dns/get
```

```
Body

{
    "host_ip":"10.30.12.120",
    "cluster_uuid":"232671ca-d1e7-44ea-9278-a7c2d5920fa7"
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
    "nameserver_active": "223.5.5.5",
    "nameserver_backup": ""
  }
}
```

#### 异常返回示例

### 状态码



## v1/host/dns/update
主机dns更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 host_ip| string|是|-| 主机ip
 nameserver_active| string| 否| "223.5.5.5"| 首选DNS服务器
 nameserver_backup| string| 否| "223.5.5.5"| 备选DNS服务器

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://10.30.12.37:8080/v1/host/dns/update
```

```
Body
{
	"nameserver_active": "223.5.5.5",
	"nameserver_backup": "233.5.5.5",
	"host_ip": "10.30.12.120",
	"cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7"
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
    "nameserver_active": "223.5.5.5",
    "nameserver_backup": ""
  }
}
```

#### 异常返回示例

### 状态码



## v1/host/staticroute/list
主机静态路由列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 host_ip| string|是|-| 主机ip

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://10.30.12.37:8080/v1/host/staticroute/list?host_ip=10.30.12.120&cluster_uuid=232671ca-d1e7-44ea-9278-a7c2d5920fa7
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
    "StaticRoutes": [
      {
        "Destination": "0.0.0.0",
        "Mask": "0.0.0.0",
        "Gateway": "10.30.12.1",
        "Iface": "managerbr",
        "Metric": 0
      },
      {
        "Destination": "10.30.12.0",
        "Mask": "255.255.255.0",
        "Gateway": "0.0.0.0",
        "Iface": "managerbr",
        "Metric": 0
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/host/staticroute/create
主机静态路由添加
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 host_ip| string|是|-| 主机ip
 destination| string|是|-| 目的地址
 mask| string|是|-| 子网掩码
 gateway| string|是|-| 网关

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://10.30.12.37:8080/v1/host/staticroute/create
```
```
Body
```

{
	"host_ip": "10.30.12.120",
	"cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
	"destination": "10.30.14.0",
	"mask": "255.255.255.0",
	"gateway": "10.30.14.1"
}


#### 正常返回示例

```

#### 异常返回示例

### 状态码


## /v1/host/staticroute/delete
主机静态路由删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 host_ip| string|是|-| 主机ip
 destination| string|是|-| 目的地址
 mask| string|是|-| 子网掩码
 gateway| string|是|-| 网关

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://10.30.12.37:8080/v1/host/staticroute/delete
```
```
Body
```

{
	"host_ip": "10.30.12.120",
	"cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
	"destination": "10.30.10.0",
	"mask": "255.255.255.0",
	"gateway": "10.30.12.1"
}

#### 正常返回示例

```

#### 异常返回示例

### 状态码

## /v1/host/staticroute/update
主机静态路由更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 host_ip| string|是|-| 主机ip
 destination| string|是|-| 目的地址
 mask| string|是|-| 子网掩码
 gateway| string|是|-| 网关

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://10.30.12.37:8080/v1/host/staticroute/update
```
```
Body
```

{
	"host_ip": "10.30.12.120",
	"cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
	"destination": "10.30.10.0",
	"mask": "255.255.255.0",
	"gateway": "10.30.12.1"
}

#### 正常返回示例

```

#### 异常返回示例

### 状态码


## /v1/host/networkconfig/split

主机静态路由更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 host_uuid| string|是|-| 主机uuid
 ip_address| string|是|-| 存储网络地址
 devices| []string|是|-| 主机物理网卡
 gateway| string|否|-| 存储网络网关


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://10.30.12.37:8080/v1/host/staticroute/update
```
```
Body
```

{
	"host_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
	"cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
	"ip_address": "10.30.10.0",
	"devices": [
	            "eth0"
	            ],
	"gateway": "10.30.12.1"
}

#### 正常返回示例

```

#### 异常返回示例

### 状态码


## /v1/host/statistic/network/interface

主机静态路由更新
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid|string|是|-| 集群uuid
 host_ip| string|是|-| 主机ip


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://10.30.12.37:8080/v1/host/statistic/network/interface?host_ip=10.30.12.120&cluster_uuid=232671ca-d1e7-44ea-9278-a7c2d5920fa7
```
```
Body
```
#### 正常返回示例
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "Data": [
      {
        "Addrs": [
          "10.30.12.120/24",
          "fe80::a952:bc4a:1caf:e420/64"
        ],
        "Mac": "d2:3e:c1:ca:1f:42",
        "Name": "managerbr",
        "Bandwidth": 0,
        "MTU": 1500,
        "Status": "unknown"
      },
      {
        "Addrs": null,
        "Mac": "d6:a8:6e:c2:d7:4b",
        "Name": "br-int",
        "Bandwidth": 0,
        "MTU": 1500,
        "Status": "unknown"
      },
      {
        "Addrs": null,
        "Mac": "c6:34:3f:61:95:49",
        "Name": "storagebr",
        "Bandwidth": 0,
        "MTU": 1500,
        "Status": "unknown"
      }
    ]
  }
}

```

#### 异常返回示例

### 状态码