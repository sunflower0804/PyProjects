

## /v1/network/bridge/vlan/update
#### 功能：网桥vlan修改
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
cluster_uuid| string| 是| -| 集群uuid
uuid| string| 是| -| 二层网络uuid
vlan_allows| []uint32| 是| -| 二层网络uuid
vlan_mode| string| 是| trunk| vlan模式

### 返回参数
名称|参数类型|描述 
---|---|---


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/bridge/vlan/update
```
Body:
```	
{
	"cluster_uuid": "232671ca-d1e7-44ea-9278-a7c2d5920fa7",
	"uuid": "28a2ad7c-4011-43cd-b4f6-58a60c50a560",
	"vlan_mode": "trunk",
	"vlan_allows": [
		1
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
  "data": {}
}
```

#### 异常返回示例

### 状态码




## /v1/network/bridge/bond/update 
#### 功能：网桥绑定信息修改
#### 请求类型：post

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
  cluster_uuid| string| 是| -| 集群uuid
  uuid| string| 是| -| 二层网络uuid
  bond_config| object| 是| -| bond配置

### bond_config对象
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
bond_mode| int32| 否| -| bond模式
lacp_config| object| 否|- | 链路聚合配置

### 返回参数
名称|参数类型|描述
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/bridge/bond/update
```
Body:
```
{
    "cluster_uuid":"49bb08f9-1c60-49ee-85d6-6fde276895c5",
    "uuid":"b0baaba4-f6e4-46d9-a2cb-b66f113fb24a",
    "bond_config":{
        "bond_mode":1
    }
}
```	
todo
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码


## /v1/network/layer2/stp/update 
#### 功能：二层网络stp修改
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/layer2/stp/update 
```
Body:
```	
todo
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码



## /v1/network/layer2/list
#### 功能：获取二层网络列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
cluster_uuid| string| 是| -| 集群uuid
page_num| int32| 否| -|
page_size| int32| 否| -|


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/layer2/list?page_num=0&page_size=10&filter_name=&flag=true&cluster_uuid=3bf461e0-b92c-4df1-9aa6-4bf71ad2db7d
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
    "total_count": 1,
    "list": [
      {
        "Name": "manage",
        "Ctime": 1570781028,
        "Mtime": 1570781028,
        "Bridge": {
          "name": "br0",
          "ports": [
            "73776a52-1095-4c5f-97c0-a34eec180de4",
            "e25064ae-31c4-48f5-865b-dd9246843762",
            "f5cb5faf-cc4d-4ecc-9826-ce00f8521cec"
          ],
          "mirrors": null,
          "netflow": null,
          "sflow": null,
          "flood_vlans": null,
          "auto_attach": null,
          "controller": null,
          "flow_tables": null,
          "fail_mode": null,
          "datapath_id": "",
          "datapath_type": "",
          "datapath_version": "2.11.1",
          "ipfix": null,
          "protocols": [
            "openflow1.0",
            "openflow1.1",
            "openflow1.2",
            "openflow1.3",
            "openflow1.4",
            "openflow1.5"
          ],
          "stp": false,
          "stp_status": null,
          "rstp": false,
          "rstp_status": null,
          "mcast_snooping_enable": false,
          "ExtIDs": {
            "BridgeType": "manager",
            "bond_mode": "fault-tolerance (active-backup)",
            "mtu": "1500"
          },
          "OthConf": null,
          "intefaces": [
            {
              "name": "br0",
              "ifindex": 0,
              "mac_in_use": "",
              "mac": null,
              "error": null,
              "ofport": 0,
              "ofport_request": null,
              "type": "internal",
              "remote_ip": "",
              "localip": "",
              "in_key": "",
              "out_key": "",
              "key": "",
              "tos": "",
              "ttl": "",
              "df_default": "",
              "egress_pkt_mark": "",
              "packet_type": "",
              "exts": "",
              "csum": "",
              "peer": "",
              "mtu": 1500,
              "mtu_request": null,
              "admin_state": "",
              "link_state": "",
              "link_resets": 0,
              "link_speed": null,
              "duplex": null,
              "lacp_current": null,
              "status": {
                "driver_name": "openvswitch"
              },
              "statistics": null,
              "ingress_policing_rate": 0,
              "ingress_policing_burst": 0,
              "options": null,
              "bfd": null,
              "bfd_status": null,
              "other_config": null,
              "external_ids": null,
              "lldp": false,
              "uuid": "0f8a06aa-23da-41b9-92aa-b36ba438fe93"
            }
          ],
          "bridgeType": 2,
          "uuid": "b7c95024-ad5e-40d4-8050-2d0d0b93e45c",
          "BondName": "manager",
          "Uplinks": [
            "enp2s1"
          ],
          "BondNameInfo": [
            {
              "name": "enp2s1",
              "ifindex": 0,
              "mac_in_use": "",
              "mac": null,
              "error": null,
              "ofport": 0,
              "ofport_request": null,
              "type": "",
              "remote_ip": "",
              "localip": "",
              "in_key": "",
              "out_key": "",
              "key": "",
              "tos": "",
              "ttl": "",
              "df_default": "",
              "egress_pkt_mark": "",
              "packet_type": "",
              "exts": "",
              "csum": "",
              "peer": "",
              "mtu": 1500,
              "mtu_request": null,
              "admin_state": "",
              "link_state": "",
              "link_resets": 0,
              "link_speed": null,
              "duplex": null,
              "lacp_current": null,
              "status": null,
              "statistics": null,
              "ingress_policing_rate": 0,
              "ingress_policing_burst": 0,
              "options": null,
              "bfd": null,
              "bfd_status": null,
              "other_config": null,
              "external_ids": null,
              "lldp": false,
              "uuid": ""
            }
          ]
        },
        "Interface": null,
        "Mtu": 1500,
        "Uplink": [
          "enp2s1"
        ],
        "AttachQuantity": 6,
        "Info": null,
        "VlanMode": "",
        "AllowsVlan": null,
        "PortGroups": [
          "ef627fab-a177-4c6d-98a1-33bad2f5e907"
        ],
        "BondConfig": null,
        "ReserveVlan": null,
        "UUID": "b990a6f4-e1d1-47a6-bbb4-0bf98b98f4de",
        "BackupReserveVlan": ""
        "VMachine": null,
        "Zone": "64864753-88a2-4020-8627-bf055964b4d8",
        "ZoneName": "default"
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/network/layer2/inspect
#### 功能：获取二层网络详情
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
cluster_uuid| string| 是| -| 集群uuid
uuid| string| 是| -| 二层网络uuid

### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
v1/network/layer2/inspect?name=manage&cluster_uuid=3bf461e0-b92c-4df1-9aa6-4bf71ad2db7d&uuid=28a2ad7c-4011-43cd-b4f6-58a60c50a560
```
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
    "Layer2Info": {
      "Name": "manage",
      "Ctime": 1570781028,
      "Mtime": 1570781028,
      "Bridge": {
        "name": "br0",
        "ports": [
          "6c7da44e-0774-4850-9442-0d0f45d68b65",
          "73776a52-1095-4c5f-97c0-a34eec180de4",
          "be467377-f12e-4b89-8d51-91d65cca8303",
          "c933c4ef-e169-43d2-919d-102784beb541",
          "e25064ae-31c4-48f5-865b-dd9246843762",
          "eb49c4c1-2610-4f49-8a57-3f995d94102a"
        ],
        "mirrors": null,
        "netflow": null,
        "sflow": null,
        "flood_vlans": null,
        "auto_attach": null,
        "controller": null,
        "flow_tables": null,
        "fail_mode": null,
        "datapath_id": "",
        "datapath_type": "",
        "datapath_version": "2.11.1",
        "ipfix": null,
        "protocols": [
          "openflow1.0",
          "openflow1.1",
          "openflow1.2",
          "openflow1.3",
          "openflow1.4",
          "openflow1.5"
        ],
        "stp": false,
        "stp_status": null,
        "rstp": false,
        "rstp_status": null,
        "mcast_snooping_enable": false,
        "ExtIDs": {
          "BridgeType": "manager",
          "bond_mode": "fault-tolerance (active-backup)",
          "mtu": "1500"
        },
        "OthConf": null,
        "intefaces": [
          {
            "name": "br0",
            "ifindex": 0,
            "mac_in_use": "",
            "mac": null,
            "error": null,
            "ofport": 0,
            "ofport_request": null,
            "type": "internal",
            "remote_ip": "",
            "localip": "",
            "in_key": "",
            "out_key": "",
            "key": "",
            "tos": "",
            "ttl": "",
            "df_default": "",
            "egress_pkt_mark": "",
            "packet_type": "",
            "exts": "",
            "csum": "",
            "peer": "",
            "mtu": 1500,
            "mtu_request": null,
            "admin_state": "",
            "link_state": "",
            "link_resets": 0,
            "link_speed": null,
            "duplex": null,
            "lacp_current": null,
            "status": {
              "driver_name": "openvswitch"
            },
            "statistics": null,
            "ingress_policing_rate": 0,
            "ingress_policing_burst": 0,
            "options": null,
            "bfd": null,
            "bfd_status": null,
            "other_config": null,
            "external_ids": null,
            "lldp": false,
            "uuid": "0f8a06aa-23da-41b9-92aa-b36ba438fe93"
          }
        ],
        "bridgeType": 2,
        "uuid": "b7c95024-ad5e-40d4-8050-2d0d0b93e45c",
        "BondName": "manager",
        "Uplinks": [
          "enp2s1"
        ],
        "BondNameInfo": [
          {
            "name": "enp2s1",
            "ifindex": 0,
            "mac_in_use": "",
            "mac": null,
            "error": null,
            "ofport": 0,
            "ofport_request": null,
            "type": "",
            "remote_ip": "",
            "localip": "",
            "in_key": "",
            "out_key": "",
            "key": "",
            "tos": "",
            "ttl": "",
            "df_default": "",
            "egress_pkt_mark": "",
            "packet_type": "",
            "exts": "",
            "csum": "",
            "peer": "",
            "mtu": 1500,
            "mtu_request": null,
            "admin_state": "",
            "link_state": "",
            "link_resets": 0,
            "link_speed": null,
            "duplex": null,
            "lacp_current": null,
            "status": null,
            "statistics": null,
            "ingress_policing_rate": 0,
            "ingress_policing_burst": 0,
            "options": null,
            "bfd": null,
            "bfd_status": null,
            "other_config": null,
            "external_ids": null,
            "lldp": false,
            "uuid": ""
          }
        ]
      },
      "Interface": null,
      "Mtu": 1500,
      "Uplink": [
        "enp2s1"
      ],
      "AttachQuantity": 6,
      "Info": {
        "BridgeName": "br0",
        "HostInfo": {
          "192.168.201.28": {
            "Name": "192.168.201.28",
            "HostIP": "192.168.201.28",
            "BondMode": "fault-tolerance (active-backup)",
            "BondName": "manager",
            "Uplinks": [
              "enp2s1"
            ],
            "IFaceInfos": [
              {
                "name": "enp2s1",
                "ifindex": 0,
                "mac_in_use": "",
                "mac": null,
                "error": null,
                "ofport": 0,
                "ofport_request": null,
                "type": "",
                "remote_ip": "",
                "localip": "",
                "in_key": "",
                "out_key": "",
                "key": "",
                "tos": "",
                "ttl": "",
                "df_default": "",
                "egress_pkt_mark": "",
                "packet_type": "",
                "exts": "",
                "csum": "",
                "peer": "",
                "mtu": 1500,
                "mtu_request": null,
                "admin_state": "",
                "link_state": "",
                "link_resets": 0,
                "link_speed": null,
                "duplex": null,
                "lacp_current": null,
                "status": null,
                "statistics": null,
                "ingress_policing_rate": 0,
                "ingress_policing_burst": 0,
                "options": null,
                "bfd": null,
                "bfd_status": null,
                "other_config": null,
                "external_ids": null,
                "lldp": false,
                "uuid": ""
              }
            ]
          }
        }
      },
      "VlanMode": "",
      "AllowsVlan": null,
      "PortGroups": [
        "ef627fab-a177-4c6d-98a1-33bad2f5e907"
      ],
      "BondConfig": null,
      "ReserveVlan": null,
      "UUID": "b990a6f4-e1d1-47a6-bbb4-0bf98b98f4de",
      "BackupReserveVlan": ""
    },
    "port_group_list": [
      {
        "port_group_name": "default",
        "port_group_uuid": "ef627fab-a177-4c6d-98a1-33bad2f5e907",
        "create_time": 1570781028,
        "update_time": 1570781028,
        "vlan_id": 0,
        "layer2_name": "manage",
        "ext_ids": null,
        "attach_quantity": 6,
        "bandwidth": null
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码

## /v1/network/layer2/delete
#### 功能：二层网络删除
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
cluster_uuid| string| 是| -| 集群uuid
uuid| string| 是| -| 二层网络uuid
name| string| 否| -| 二层网络名称

### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/layer2/delete
```
Body:
```	
{
    "cluster_uuid": "",
    "uuid": "",
    "name": "",
}
```
#### 正常返回示例
```
```

#### 异常返回示例

### 状态码


## /v1/network/layer2/create 
#### 功能：创建二层网络
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
cluster_uuid| string| 是| -| 集群uuid
name| string| 否| -| 二层网络名称
zone_uuid| string| 否| -| 资源池uuid
vlan_mode| string| 否| -| vlan模式
vlan_allows| []uint32| 是| -| 添加的vlan
bond_config| object| 是| bond配置
uplink| []string| 是 物理网卡

### bond_config对象
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
bond_mode| int32| 否| -| bond模式
lacp_config| object| 否|- | 链路聚合配置


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/layer2/create 
```
Body:
```	
{
	"name": "1111",
	"vlan_mode": "trunk",
	"uplink": [
		"eno3"
	],
	"vlan_allows": [
		2,
		5,
		3
	],
	"zone_uuid": "8dbde5bf-d9e2-472c-8c47-f58deeca3a6c",
	"bond_config": {
		"bond_mode": 0
	},
	"cluster_uuid": "49bb08f9-1c60-49ee-85d6-6fde276895c5"
}
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码


## /v1/network/layer2/port_group/create
#### 功能：创建二层网络端口组
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/layer2/port_group/create
```
Body:
```	
{
  "port_group_name": "ddd",
  "layer2_network_uuid": "8e13984c-c2ee-45aa-b3bd-097f1fcf5ab8",
  "vlan_id": null,
  "zone_uuid": "64864753-88a2-4020-8627-bf055964b4d8",
  "cluster_uuid": "42e3b0db-5dce-4893-9421-7ae6fe8ac0ee"
}
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码



## /v1/network/layer2/port_group/delete
#### 功能：删除二层网络端口组
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/layer2/port_group/delete
```
Body:
```	
{
  "port_group_uuid": "62ba0743-b633-489a-ae76-31d7866e41ac",
  "port_group_name": "default",
  "cluster_uuid": "42e3b0db-5dce-4893-9421-7ae6fe8ac0ee"
}
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码


## /v1/network/layer2/port_group/inspect
#### 功能：获取二层网络端口组详情
#### 请求类型：

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/layer2/port_group/inspect
```
Body:
```	
todo
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码





## /v1/network/layer2/port_group/list
#### 功能：获取二层网络端口组列表
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://10.30.12.161:8080/v1/network/layer2/port_group/list?cluster_uuid=b088822c-1176-4c79-9df7-5fad80c7fd1d
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
    "list": [
      {
        "port_group_name": "default",
        "port_group_uuid": "d611b70d-281b-4bf9-9dc6-c4c904577128",
        "create_time": 1569305654,
        "update_time": 1569305654,
        "vlan_id": 0,
        "layer2_name": "manage",
        "ext_ids": null,
        "attach_quantity": 35,
        "bandwidth": null,
        "vm": null,
        "zone_uuid": "1272116b-03fc-4717-ab99-8b502d091d08",
        "zone_name": "default",
        "l2network_uuid": ""
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/network/layer2/modify
#### 功能：获取二层网络mirror详情
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid| string| 是| -| 集群uuid
uuid| string| 是| -| 二层网络uuid
name| string| 是| -| 二层网络名称
manage| bool| 否| -| 管理服务
storage| bool| 否| -| 存储服务区
hyper| bool| 否| -| 计算服务
spice| bool| 否| -| spice服务器
spice| bool| 否| -| pxe服务

### 返回参数
名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/layer2/modify
```
Body:
```
{
	"uuid": "28a2ad7c-4011-43cd-b4f6-58a60c50a560",
	"name": "pxe",
	"pxe": false,
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
  "data": {}
}
```

#### 异常返回示例

### 状态码


## /v1/network/brigde/bond/set
#### 功能：网桥绑定设置
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid| string| 是| -| 集群uuid
host_ip| string| 是| -| 主机ip
uplink| string| 是| -| 网卡名称
uuid| string| 是| -| 二层网络uuid


### 返回参数
名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/brigde/bond/set
```
Body:
```
{
	"cluster_uuid": "39058114-31a1-452f-9ce7-54c002ca7f53",
	"host_ip": "10.30.47.161",
	"uuid": "4bb067f7-5970-46a1-88c5-2ed932dde767",
	"uplink": "eno3"
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

## /v1/network/gateway/network_card/delete
#### 功能：网关网卡删除
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid| string| 是| -| 集群uuid
 host_ip| string| 是| -| 主机ip
 uplink| string| 是| -| 网卡名称
 uuid| string| 是| -| 二层网络uuid


### 返回参数
名称|参数类型|描述
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/gateway/network_card/delete
```
Body:
```
{
	"cluster_uuid": "49bb08f9-1c60-49ee-85d6-6fde276895c5",
	"host_ip": "10.30.100.21",
	"uuid": "b0baaba4-f6e4-46d9-a2cb-b66f113fb24a",
	"network_card_name": "eno3"
}
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码


## /v1/network/bridge/mcast_snoop/status/update
#### 功能：主机网桥mcast_snoop状态更新
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
   cluster_uuid| string| 是| -| 集群uuid
   uuid| string| 是| -| 二层网络uuid
   is_enable_mcast_snoop| bool| 是| -| 是否开启主播侦听


### 返回参数
名称|参数类型|描述
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/network/bridge/mcast_snoop/status/update
```
Body:
```
{
    "cluster_uuid":"49bb08f9-1c60-49ee-85d6-6fde276895c5",
    "uuid":"b0baaba4-f6e4-46d9-a2cb-b66f113fb24a",
    "is_enable_mcast_snoop":true
}
```
#### 正常返回示例
```
todo
```

#### 异常返回示例

### 状态码


