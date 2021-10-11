## /v1/bare_metal/host_add
#### 功能：注册裸金属主机节点
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid| string| 是|- | 集群uuid
 zone_uuid| string| 是|- | 资源池uuid

### node对象
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 bm_name| string| 是| -| 名称
 pxe_vm_uuid| string | 是| -| pxe服务器uuid
 pxe_vm_ip| string| 是| -| pxe服务器管理Ip
 Mac| string| 是| -| 裸金属服务器网卡mac地址

### drive_info对象
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 ipmi_address| string| 是|- | ipmi地址
 ipmi_port| int32| 是|623 | ipmi端口
 ipmi_username| string| 是|- | ipmi用户名
 ipmi_password| string| 是|- | ipmi用户密码
 ipmi_tool| string| 否|ipmi | 工具


### 返回参数
 名称|参数类型|描述
 ---|---|---
 bm_host_uuid| string| 裸金属主机节点uuid
 bm_host_name| string| 裸金属主机节点名称

### 示例

#### 请求示例
```
http://localhost:9990/v1/bare_metal/host_add
```
Body:
```
{
	"cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
	"zone_uuid": "ac776392-dbf1-4272-b88b-4b2ac886cacb",
	"zone_name": "default",
	"node": {
		"bm_name": "1111",
		"mac": "52:53:45:56:45:12",
		"pxe_vm_uuid": "5428047c-e311-433e-ad62-095cb5df3a23",
		"pxe_vm_ip": "10.30.12.39"
	},
	"drive_info": {
		"ipmi_address": "10.30.10.10",
		"ipmi_disable_time": 5,
		"ipmi_port": 623,
		"ipmi_username": "admin",
		"ipmi_password": "admin",
		"ipmi_tool": "ipmitool",
	},
}
```
#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "bm_host_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "bm_host_name": "name"
  }
}
```

#### 异常返回示例

### 状态码


## /v1/bare_metal/host_delete
#### 功能：删除裸金属主机节点
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid| string| 是|- | 集群uuid
 zone_uuid| string| 是|- | 资源池uuid
 zone_name| string| 否|- | 资源池名称
 bm_host_uuid| string| 是| 裸金属主机uuid
 bm_host_name| string| 否| 裸金属主机名称

### 返回参数
 名称|参数类型|描述
 ---|---|---

### 示例

#### 请求示例
```
http://localhost:9990/v1/bare_metal/host_delete
```
Body:
```
{
	"cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
	"zone_uuid": "ac776392-dbf1-4272-b88b-4b2ac886cacb",
	"zone_name": "default",
    "bm_host_uuid": "ac776392-dbf1-4272-b88b-4b2ac886cacb",
    "bm_host_name": "desault",
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


## /v1/bare_metal/host_shutdown
#### 功能：裸金属主机关机
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid| string| 是|- | 集群uuid
 zone_uuid| string| 是|- | 资源池uuid
 zone_name| string| 否|- | 资源池名称
 bm_host_uuid| string| 是| 裸金属主机uuid
 bm_host_name| string| 否| 裸金属主机名称

### 返回参数
 名称|参数类型|描述
 ---|---|---

### 示例

#### 请求示例
```
http://localhost:9990/v1/bare_metal/host_shutdown
```
Body:
```
{
	"cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
	"zone_uuid": "ac776392-dbf1-4272-b88b-4b2ac886cacb",
	"zone_name": "default",
    "bm_host_uuid": "ac776392-dbf1-4272-b88b-4b2ac886cacb",
    "bm_host_name": "desault",
}
```
#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
      "bm_host_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
      "bm_host_name": "name,
  }
}
```

#### 异常返回示例

### 状态码


## /v1/bare_metal/host_start
#### 功能：裸金属主机开机
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid| string| 是|- | 集群uuid
 zone_uuid| string| 是|- | 资源池uuid
 zone_name| string| 否|- | 资源池名称
 bm_host_uuid| string| 是| 裸金属主机uuid
 bm_host_name| string| 否| 裸金属主机名称

### 返回参数
 名称|参数类型|描述
 ---|---|---

### 示例

#### 请求示例
```
http://localhost:9990/v1/bare_metal/host_start
```
Body:
```
{
	"cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
	"zone_uuid": "ac776392-dbf1-4272-b88b-4b2ac886cacb",
	"zone_name": "default",
    "bm_host_uuid": "ac776392-dbf1-4272-b88b-4b2ac886cacb",
    "bm_host_name": "desault",
}
```
#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
      "bm_host_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
      "bm_host_name": "name,
  }
}
```

#### 异常返回示例

### 状态码


## /v1/bare_metal/host_reset
#### 功能：裸金属主机重启
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid| string| 是|- | 集群uuid
 zone_uuid| string| 是|- | 资源池uuid
 zone_name| string| 否|- | 资源池名称
 bm_host_uuid| string| 是| 裸金属主机uuid
 bm_host_name| string| 否| 裸金属主机名称

### 返回参数
 名称|参数类型|描述
 ---|---|---

### 示例

#### 请求示例
```
http://localhost:9990/v1/bare_metal/host_reset
```
Body:
```
{
	"cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
	"zone_uuid": "ac776392-dbf1-4272-b88b-4b2ac886cacb",
	"zone_name": "default",
    "bm_host_uuid": "ac776392-dbf1-4272-b88b-4b2ac886cacb",
    "bm_host_name": "desault",
}
```
#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
      "bm_host_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
      "bm_host_name": "name,
  }
}
```

#### 异常返回示例

### 状态码


## /v1/bare_metal/host_initialize
#### 功能：裸金属主机初始化
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid| string| 是|- | 集群uuid
 zone_uuid| string| 是|- | 资源池uuid
 zone_name| string| 否|- | 资源池名称
 bm_host_uuid| string| 是| 裸金属主机uuid
 bm_host_name| string| 否| 裸金属主机名称

### 返回参数
 名称|参数类型|描述
 ---|---|---

### 示例

#### 请求示例
```
http://localhost:9990/v1/bare_metal/host_initialize
```
Body:
```
{
	"cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
	"zone_uuid": "ac776392-dbf1-4272-b88b-4b2ac886cacb",
	"zone_name": "default",
    "bm_host_uuid": "ac776392-dbf1-4272-b88b-4b2ac886cacb",
    "bm_host_name": "desault",
}
```
#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
      "bm_host_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400",
      "bm_host_name": "name,
  }
}
```

#### 异常返回示例


## /v1/bare_metal/host_list
#### 功能：裸金属主机列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid| string| 是|- | 集群uuid
 filter_zone_uuid| string| 否| 资源池进行过滤
 filter_host_name| string| 否| 名称进行过滤
 filter_fuzzy| string| 否| 名称进行过滤
 filter_uuid| string| 否| uuid进行过滤
 FilterFuzzy| string| 否| 模糊规则进行过滤
 FilterFuzzy| string| 否| 模糊规则进行过滤
 page_num|int|否|0|显示页码
 page_size|int|否|0|每页显示多少数据

### 返回参数
 名称|参数类型|描述
 ---|---|---

### 示例

#### 请求示例
```
http://localhost:9990/v1/bare_metal/host_list?page_num=0&page_size=5&cluster_uuid=232671ca-d1e7-44ea-9278-a7c2d5920fa7&filter_zone_uuid=0a257fd1-58a8-4abf-803c-538e7348652b&filter_fuzzy=
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
        "cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
        "cluster_name": "cluster_name_37",
        "uuid": "a3307502-f631-4304-905e-ccb1aecb589e",
        "name": "host-14",
        "ctime": 1629170731,
        "mtime": 1629458415,
        "action": 0,
        "ip": "10.30.14.231",
        "zone_uuid": "ac776392-dbf1-4272-b88b-4b2ac886cacb",
        "power_status": "on",
        "state": 1,
        "zone_name": "default",
        "mac": "52:54:00:df:df:cb",
        "pxe_service_ip": "10.30.12.39",
        "pxe_service_uuid": "5428047c-e311-433e-ad62-095cb5df3a23",
        "drive_type": "IPMI",
        "ipmi_info": {
          "ipmi_address": "10.30.12.107",
          "ipmi_disable_time": 5,
          "ipmi_port": 6230,
          "ipmi_username": "admin",
          "ipmi_password": "b7f4e6ac9de22516a4c3f6ef72db075a",
          "ipmi_tool": "ipmitool",
          "ipmi_protocal_version": "",
          "ipmi_priv_level": ""
        },
        "drive_inter_face": {
          "boot": "",
          "console": "",
          "deploy": "",
          "managertool": "",
          "network": "",
          "power": "",
          "raid": "",
          "storage": ""
        },
        "agent_state": "",
        "attr": null,
        "Addr": "",
        "Host": {
          "Hostname": "localhost.localdomain",
          "Uptime": 40,
          "BootTime": 1629180409,
          "Procs": 136,
          "OS": "linux",
          "Platform": "centos",
          "PlatformFamily": "rhel",
          "PlatformVersion": "8.2.2004",
          "KernelVersion": "4.18.0-193.19.1.el8_2.x86_64",
          "VirtualizationSystem": "",
          "VirtualizationRole": "",
          "HostID": "",
          "CountFDs": 736,
          "CountThreads": 87,
          "CountConns": 62,
          "IFaces": null
        },
        "Cpu": {
          "Model": "61",
          "ModelName": "Intel Core Processor (Broadwell, IBRS)",
          "Cores": 2,
          "Sockets": 2,
          "Mhz": 2199.968,
          "User": 1.4778325123151614,
          "System": 0.49261083743841627,
          "Idle": 97.04433497537038,
          "Nice": 0,
          "Iowait": 0,
          "Irq": 0.49261083743841627,
          "Softirq": 0.4926108374384273,
          "CpuTemp": -1
        },
        "Load": null,
        "Mem": {
          "Total": 4130054144,
          "Available": 2776563712,
          "Used": 178487296,
          "Free": 2884939776,
          "Buffers": 0,
          "Cached": 1066627072,
          "KSM": 0,
          "UsedSlot": 1,
          "TotalSlot": 0,
          "FormFactor": "DIMM",
          "Speed": "Unknown"
        },
        "Net": {
          "Nbi": [
            {
              "Addrs": [
                "10.30.14.231/24",
                "fe80::5054:ff:fedf:dfcb/64"
              ],
              "Mac": "52:54:00:df:df:cb",
              "Bandwidth": -1,
              "MTU": 1500,
              "Status": "up",
              "name": "ens3",
              "WIOPS": 1,
              "RIOPS": 3,
              "WMBPS": 159,
              "RMBPS": 2143,
              "Errin": 0,
              "Errout": 0,
              "Dropin": 0,
              "Dropout": 0
            }
          ],
          "TcpNum": 6,
          "UdpNum": 3,
          "UnixNum": 53,
          "TimeNano": 1629180449361546928,
          "Net_Gate": {
            "default": "10.30.14.1"
          }
        },
        "Disk": {
          "Dbi": [
            {
              "Path": "/dev/sda",
              "Type": "HDD",
              "Total": 214748364800,
              "RIOPS": 0,
              "WIOPS": 0,
              "RSpeed": 0,
              "WSpeed": 0,
              "RIOwait": 0,
              "WIOwait": 0,
              "IoTime": 0,
              "UsageRate": 0,
              "LightOn": false,
              "Smart": {
                "SMARTSupport": false,
                "DeviceModel": "",
                "SerialNumber": "",
                "RotationRate": "",
                "RotationRateRPM": 0,
                "IsSSD": false,
                "TransportProtocol": "",
                "Healthy": false,
                "FormFactor": "",
                "Temperature": 0,
                "LifeTime": 0,
                "Attributes": null
              },
              "IsSysDisk": false,
              "Interface": "scsi",
              "WWN": "",
              "ID": ""
            }
          ],
          "SystemDisk": {
            "Path": "rootfs",
            "Parts": null
          },
          "TimeNano": 1629180449368631458
        },
        "VSM": null,
        "USM": null,
        "Center": null,
        "Hyper": null,
        "Network": null,
        "SSHD": null,
        "Agent": null,
        "Gpu": null,
        "share": null,
        "TopFlow": null,
        "Ctime": 0
      }
    ],
    "total_count": 1,
    "each_range_list_state": [
      {
        "cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
        "cluster_name": "cluster_name_37",
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

#### 异常返回示例

### 状态码


## /v1/bare_metal/host_get
#### 功能：裸金属主机详情
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid| string| 是|- | 集群uuid
 bm_host_uuid| string| 是|- | 裸金属主机uuid
 zone_uuid| string| 是|- |资源池uuid

### 返回参数
 名称|参数类型|描述
 ---|---|---

### 示例

#### 请求示例
```
http://localhost:9990/v1/bare_metal/host_get?zone_uuid=ac776392-dbf1-4272-b88b-4b2ac886cacb&cluster_uuid=232671ca-d1e7-44ea-9278-a7c2d5920fa7&bm_host_uuid=a3307502-f631-4304-905e-ccb1aecb589e
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
    "data": {
      "cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
      "cluster_name": "cluster_name_37",
      "uuid": "a3307502-f631-4304-905e-ccb1aecb589e",
      "name": "host-14",
      "ctime": 1629170731,
      "mtime": 1629701139,
      "action": 0,
      "ip": "",
      "zone_uuid": "ac776392-dbf1-4272-b88b-4b2ac886cacb",
      "power_status": "on",
      "state": 1,
      "zone_name": "default",
      "mac": "52:54:00:df:df:cb",
      "pxe_service_ip": "10.30.12.39",
      "pxe_service_uuid": "5428047c-e311-433e-ad62-095cb5df3a23",
      "drive_type": "IPMI",
      "ipmi_info": {
        "ipmi_address": "10.30.12.107",
        "ipmi_disable_time": 5,
        "ipmi_port": 6230,
        "ipmi_username": "admin",
        "ipmi_password": "b7f4e6ac9de22516a4c3f6ef72db075a",
        "ipmi_tool": "ipmitool",
        "ipmi_protocal_version": "",
        "ipmi_priv_level": ""
      },
      "drive_inter_face": {
        "boot": "",
        "console": "",
        "deploy": "",
        "managertool": "",
        "network": "",
        "power": "",
        "raid": "",
        "storage": ""
      },
      "agent_state": "",
      "attr": null,
      "Addr": "",
      "Host": {
        "Hostname": "localhost.localdomain",
        "Uptime": 40,
        "BootTime": 1629180409,
        "Procs": 136,
        "OS": "linux",
        "Platform": "centos",
        "PlatformFamily": "rhel",
        "PlatformVersion": "8.2.2004",
        "KernelVersion": "4.18.0-193.19.1.el8_2.x86_64",
        "VirtualizationSystem": "",
        "VirtualizationRole": "",
        "HostID": "",
        "CountFDs": 736,
        "CountThreads": 87,
        "CountConns": 62,
        "IFaces": null
      },
      "Cpu": {
        "Model": "61",
        "ModelName": "Intel Core Processor (Broadwell, IBRS)",
        "Cores": 2,
        "Sockets": 2,
        "Mhz": 2199.968,
        "User": 1.4778325123151614,
        "System": 0.49261083743841627,
        "Idle": 97.04433497537038,
        "Nice": 0,
        "Iowait": 0,
        "Irq": 0.49261083743841627,
        "Softirq": 0.4926108374384273,
        "CpuTemp": -1
      },
      "Load": null,
      "Mem": {
        "Total": 4130054144,
        "Available": 2776563712,
        "Used": 178487296,
        "Free": 2884939776,
        "Buffers": 0,
        "Cached": 1066627072,
        "KSM": 0,
        "UsedSlot": 1,
        "TotalSlot": 0,
        "FormFactor": "DIMM",
        "Speed": "Unknown"
      },
      "Net": {
        "Nbi": [
          {
            "Addrs": [
              "10.30.14.231/24",
              "fe80::5054:ff:fedf:dfcb/64"
            ],
            "Mac": "52:54:00:df:df:cb",
            "Bandwidth": -1,
            "MTU": 1500,
            "Status": "up",
            "name": "ens3",
            "WIOPS": 1,
            "RIOPS": 3,
            "WMBPS": 159,
            "RMBPS": 2143,
            "Errin": 0,
            "Errout": 0,
            "Dropin": 0,
            "Dropout": 0
          }
        ],
        "TcpNum": 6,
        "UdpNum": 3,
        "UnixNum": 53,
        "TimeNano": 1629180449361546928,
        "Net_Gate": {
          "default": "10.30.14.1"
        }
      },
      "Disk": {
        "Dbi": [
          {
            "Path": "/dev/sda",
            "Type": "HDD",
            "Total": 214748364800,
            "RIOPS": 0,
            "WIOPS": 0,
            "RSpeed": 0,
            "WSpeed": 0,
            "RIOwait": 0,
            "WIOwait": 0,
            "IoTime": 0,
            "UsageRate": 0,
            "LightOn": false,
            "Smart": {
              "SMARTSupport": false,
              "DeviceModel": "",
              "SerialNumber": "",
              "RotationRate": "",
              "RotationRateRPM": 0,
              "IsSSD": false,
              "TransportProtocol": "",
              "Healthy": false,
              "FormFactor": "",
              "Temperature": 0,
              "LifeTime": 0,
              "Attributes": null
            },
            "IsSysDisk": false,
            "Interface": "scsi",
            "WWN": "",
            "ID": ""
          }
        ],
        "SystemDisk": {
          "Path": "rootfs",
          "Parts": null
        },
        "TimeNano": 1629180449368631458
      },
      "VSM": null,
      "USM": null,
      "Center": null,
      "Hyper": null,
      "Network": null,
      "SSHD": null,
      "Agent": null,
      "Gpu": null,
      "share": null,
      "TopFlow": null,
      "Ctime": 0
    }
  }
}
```

#### 异常返回示例

### 状态码



## /v1/bare_metal/host_delete
#### 功能：删除裸金属主机节点
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid| string| 是|- | 集群uuid
 zone_uuid| string| 是|- | 资源池uuid
 zone_name| string| 否|- | 资源池名称
 bm_host_uuid| string| 是| 裸金属主机uuid
 bm_host_name| string| 否| 裸金属主机名称

### 返回参数
 名称|参数类型|描述
 ---|---|---

### 示例

#### 请求示例
```
http://localhost:9990/v1/bare_metal/host_delete
```
Body:
```
{
	"cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
	"zone_uuid": "ac776392-dbf1-4272-b88b-4b2ac886cacb",
	"zone_name": "default",
    "bm_host_uuid": "ac776392-dbf1-4272-b88b-4b2ac886cacb",
    "bm_host_name": "desault",
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