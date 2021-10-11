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
## 虚拟机相关
### GET&nbsp; /v1/compute/list
获取虚拟机列表

<big>**请求参数**</big>

 名称 | 参数类型 | 是否必填 | 描述
---|---|---|---
 cluster_uuid|string|否| 集群uuid
 tenant|string|否| 租户uuid
 include_trash_vm|bool|否| 是否包含回收站的虚拟机
 page_number|int|否| 分页序号
 page_size|int|否| 分页大小
 filter_name|string|否| 匹配虚拟机名称
 filter_uuid|string|否| 匹配虚拟机uuid
 filter_user_uuid|string|否| 匹配用户uuid
 filter_host_type|string|否| 匹配虚拟机类型
 filter_no_external_storage|bool|否| 是否排除使用共享存储的虚拟机
filter_vm_ip|string|否| 匹配虚拟机IP
filter_mac_address|string|否| 匹配虚拟机网卡MAC地址
filter_object_group|string|否| 匹配虚拟机分组uuid
filter_fuzzy|string|否| 模糊搜索。部分匹配虚拟机名、虚拟机uuid、网卡IP、网卡MAC地址
filter_zone|string|否| 匹配虚拟机资源池uuid
filter_recover_to_related_zones|int|否| 筛选"启用双活"选项。1：启用，2：未启用
filter_state|string|否| 筛选虚拟机状态
filter_agent|string|否| 筛选虚拟机Agent状态。
filter_action|string|否| 筛选虚拟机动作

+ **cluster_uuid**  
在指定uuid集群内搜索。如果`cluster_uuid`为空，则在纳管的全部集群内搜索，并汇总结果。  
+ **tenant**  
搜索指定租户的虚拟机。如果`tenant`为空，则搜索全部租户的虚拟机。  
如果`cluster_uuid`为空，则会在全部集群都搜索同一指定租户的虚拟机。如果同时为空，则搜索所有集群所有租户的虚拟机。
+ **page_number, page_size**  
统一见[PagingParam](#pagingparam)。
+ **filter_fuzzy**  
模糊搜索。支持模糊搜索的字段包括：虚拟机名称、虚拟机uuid、包含网卡IP、包含网卡MAC地址。  
模糊搜索匹配规则为，被搜索字段需要包含模糊搜索字符串，其中uuid、IP、MAC地址不区分大小写。
+ **filter_state**  
筛选特定虚拟机状态。字段有效值和查询返回的虚拟机状态字段有效值相同。  
_有效值_ ： "nostate"|"running"|"blocked"|"paused"|"shutdown"|"shutoff"|"crashed"|"pmsuspend"
+ **filter_agent**  
筛选特定虚拟机Agent状态。字段有效值和查询返回的虚拟机Agent状态字段有效值相同。  
_有效值_ ： "connected"|"disconnected"|"pending"
+ **filter_action**  
筛选虚拟机动作。字段有效值和查询返回的虚拟机动作字段有效值相同。  
_有效值_ ： "noaction"|"cloning"|"save"|"migrating"|"pending"|"importing"|"restoring"

<big>**返回数据**</big>

接口返回数据使用[Output](#output)封装。接口特定返回如下：
```
"data" : {
  "domains" : [ ComputeInfo ],
  "total_count" : Number,
  "each_range_list_state" : [ EachResourceRangeListState ],
  "object_group_counts" : {
    String : int
  }
}
```

+ **domains**  
虚拟机列表信息。  
_类型_：[ComputeInfo](#computeinfo)数组  
+ **total_count**  
满足过滤条件的结果总数。  
+ **each_range_list_state**  
单个集群查询结果。  
_类型_：[EachResourceRangeListState](#eachresourcerangeliststate)数组  
+ **object_group_counts**
虚拟机分组对应查询结果数量。  
_key_ : 虚拟机分组uuid  
_value_ : 该分组下满足过滤条件的虚拟机数量  

<big>**示例**</big>

**请求示例**
```
https://10.30.33.25/v1/compute/list?tenant=&page_num=0&page_size=10&filter_fuzzy=test-clone&filter_host_type=GUS&cluster_uuid=c27a25bc-5da2-430f-bfaf-6c8d33f21128
```
**返回示例**
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "domains": [
      {
        "tenant": "a5badacf-a25c-4171-9aff-b619fc2d300a",
        "tenant_name": "ycb1",
        "owner_is_ldap": false,
        "owner": "",
        "owner_name": "",
        "uuid": "b31d4319-476a-4f67-9c37-3cf5f4d54f0f",
        "name": "test-clone",
        "type": "GUS",
        "create_time": 1629783924,
        "modify_time": 1629784044,
        "deleted_time": 0,
        "state": "shutoff",
        "ga_state": "disconnected",
        "action": "noaction",
        "os": "CentOS x64",
        "first_shown_ip": "",
        "vdc_agent": "",
        "vdc_agent_list": null,
        "vdc_pool_uuid": "",
        "vdc_pool_name": "",
        "create_type": "",
        "namespace": "0d16efa9-5652-4226-8086-e4cac3c545f9",
        "machine_uuid": "",
        "labels": null,
        "interface_ips": [],
        "attr": null,
        "object_group": "e9017aa7-e19b-47b0-b638-e639aa9451c6",
        "object_group_name": "default",
        "plan": "",
        "plan_name": "",
        "plan_master_cluster_uuid": "",
        "plan_master_cluster_name": "",
        "plan_slave_cluster_uuid": "",
        "plan_slave_cluster_name": "",
        "running_cluster": "",
        "zone": "2871bab9-d6ed-4100-8d74-9c4442b52bb5",
        "zone_name": "default",
        "strategy": "",
        "strategy_name": "",
        "recover_to_related_zones": 2,
        "master_zone_take_over": 2,
        "spice_port_mapping": true,
        "console_server_listen_port": 0,
        "task_tag": 0,
        "statistic": {
          "cpu": {
            "ratio": 0,
            "logical": 1,
            "physical": 0
          },
          "mem": {
            "ratio": 0,
            "logical": 1073741824,
            "physical": 0
          },
          "disk": {
            "rd_bytes": 0,
            "wr_bytes": 0,
            "total": 0,
            "used": 0,
            "used_percent": 0
          },
          "network": {
            "rx_bytes": 0,
            "tx_bytes": 0
          },
          "process": {
            "cpu_usage": 0,
            "mem_usage": 0,
            "cpu_ratio": 0,
            "mem_ratio": 0,
            "host_cpu_total_rate": 0,
            "host_mem_total_rate": 0
          },
          "cpu_info": {
            "used_percent": 0,
            "cores": 0,
            "mhz": 0
          },
          "mem_info": {
            "used_percent": 0,
            "total": 0,
            "available": 0,
            "used": 0
          }
        },
        "interface": [
          {
            "interface_type": "ycb123",
            "mac_address": "52:56:ff:ab:36:81",
            "target_dev": "",
            "port_group": "239223b4-d21b-4b23-954f-796f17c75c49",
            "vlan_tag_ids": [
              14
            ],
            "driver": null,
            "vhost_queue": 0,
            "name": ""
          }
        ],
        "is_external_disk": false,
        "kvm_clock_enable": true,
        "virt_nested_enable": false,
        "memory_huge_pages_enable": false,
        "total_used": 2503995392,
        "has_passthrough_disk": false,
        "cluster_uuid": "c27a25bc-5da2-430f-bfaf-6c8d33f21128",
        "cluster_name": "host3223-cvm3323"
      }
    ],
    "total_count": 1,
    "each_range_list_state": [
      {
        "cluster_uuid": "c27a25bc-5da2-430f-bfaf-6c8d33f21128",
        "cluster_name": "host3223-cvm3323",
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
      "e9017aa7-e19b-47b0-b638-e639aa9451c6": 1
    },
    "cluster_total_resource": null
  }
}
```

### GET&nbsp; /v1/compute/inspect
获取虚拟机详情  
  

<big>**请求参数**</big>

名称 | 参数类型 | 是否必填 | 描述
---|---|---|---
 cluster_uuid|string|是| 集群uuid
 tenant|string|是| 租户uuid
 compute_uuid|string|是| 虚拟机uuid
 include_trash_vm|bool|否| 是否显示回收站的虚拟机

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：
```
"data" : {
    ClusterIdentifier,
    ComputeInspectInfo
}
```

+ **ClusterIdentifier**  
见[ClusterIdentifier](#clusteridentifier)
+ **ComputeInspectInfo**  
虚拟机详情信息。见[ComputeInspectInfo](#computeinspectinfo)

<big>**示例**</big>  
**请求示例**  
```
https://10.30.33.25/v1/compute/inspect?compute_uuid=b31d4319-476a-4f67-9c37-3cf5f4d54f0f&tenant=a5badacf-a25c-4171-9aff-b619fc2d300a&cluster_uuid=c27a25bc-5da2-430f-bfaf-6c8d33f21128
```
**返回示例**  
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "tenant": "a5badacf-a25c-4171-9aff-b619fc2d300a",
    "tenant_name": "ycb1",
    "owner_is_ldap": false,
    "owner": "",
    "owner_name": "",
    "uuid": "b31d4319-476a-4f67-9c37-3cf5f4d54f0f",
    "name": "test-clone",
    "type": "GUS",
    "create_time": 1629783924,
    "modify_time": 1629784044,
    "deleted_time": 0,
    "state": "shutoff",
    "ga_state": "disconnected",
    "action": "noaction",
    "os": "CentOS x64",
    "first_shown_ip": "",
    "vdc_agent": "",
    "vdc_agent_list": null,
    "vdc_pool_uuid": "",
    "vdc_pool_name": "",
    "create_type": "",
    "namespace": "0d16efa9-5652-4226-8086-e4cac3c545f9",
    "machine_uuid": "",
    "labels": null,
    "interface_ips": [],
    "attr": null,
    "object_group": "e9017aa7-e19b-47b0-b638-e639aa9451c6",
    "object_group_name": "default",
    "plan": "",
    "plan_name": "",
    "plan_master_cluster_uuid": "",
    "plan_master_cluster_name": "",
    "plan_slave_cluster_uuid": "",
    "plan_slave_cluster_name": "",
    "running_cluster": "",
    "zone": "2871bab9-d6ed-4100-8d74-9c4442b52bb5",
    "zone_name": "default",
    "strategy": "",
    "strategy_name": "",
    "spice_port_mapping": true,
    "console_server_listen_port": 0,
    "task_tag": 0,
    "mem_size": 1073741824,
    "mem_max": 274877906944,
    "memory_huge_pages_enable": false,
    "memory_qos": {
      "hard_limit": 0,
      "soft_limit": 0,
      "swap_hard_limit": 0,
      "min_guarantee": 0
    },
    "compute_name": "",
    "ha_mode": "on",
    "os_loader_path": "BIOS",
    "video": [
      {
        "model_type": "vga",
        "heads": 0,
        "ram_size": 131072,
        "vga_mem": 32768
      }
    ],
    "startup_setting": {
      "hosts": null,
      "labels": null
    },
    "vnc_enable": false,
    "mem_sec_enabled": false,
    "ha_config": {
      "priority": 0
    },
    "parent_uuid": "6ae9e142-f476-465f-868b-6026cddcd714",
    "migrate_dest": "",
    "baseline": "Haswell-noTSX-IBRS",
    "device_name": "",
    "import_machine": "",
    "exceed_cluster_baseline": false,
    "cpu_current": "1",
    "cpu_max_count": 2,
    "cpu_nr_count": 0,
    "cpu_sockets": 1,
    "cpu_socket_cores": 2,
    "vnc_port": 0,
    "vnc_password": "",
    "streaming_mode": "filter",
    "compression_mode": "glz",
    "spice_port": 5925,
    "spice_password": "7260a00f0794c10c7ed0652b0e465dd0",
    "panic": "on",
    "interfaces": [
      {
        "interface_id": "89359d64-00b4-4ab5-abce-f2b92c9da4ee",
        "interface_model_type": "virtio",
        "interface_type": "ycb123",
        "mac_address": "52:56:ff:ab:36:81",
        "target_dev": "",
        "port_group": "239223b4-d21b-4b23-954f-796f17c75c49",
        "port_group_name": "32012345678901234567890123456789",
        "vlan_tag_ids": [
          14
        ],
        "driver": null,
        "vhost_queue": 0,
        "bound_ip": "192.123.123.10",
        "name": ""
      }
    ],
    "cdrom": {},
    "floppy": {},
    "disks": [
      {
        "disk_target_device": "sda",
        "disk_target_bus": "scsi",
        "disk_vsd_source": {
          "volume_uuid": "42d2fc4e-9025-418b-871d-2d588873528b",
          "volume_name": "test-clone-volume-1",
          "disk_capacity": 21474836480,
          "pool_uuid": "42b3e3b6-b1d1-44c0-bf5c-b9cf73d594df",
          "pool_name": "ycb1-1000",
          "replica": "1",
          "drive_type": "HDD",
          "redundancy": 1,
          "attribute": null,
          "vsd_vendor": "LIBTARGET"
        },
        "disk_cache_mode": "none",
        "backing_store": {
          "index": 0,
          "format": null,
          "source": null,
          "backing_store": null
        },
        "disks_serial": "T001-871d2d588873528b",
        "wwn": "65254ffe9025418b",
        "disk_is_system": false
      }
    ],
    "device_order": [
      "sda",
      "hdd",
      "fda"
    ],
    "disk_type": [
      {
        "type": 3,
        "value": "sda"
      },
      {
        "type": 1,
        "value": "hdd"
      },
      {
        "type": 2,
        "value": "fda"
      }
    ],
    "usbs": [
      {
        "bus": 2,
        "port": "4",
        "product_id": "",
        "product_name": "控制台USB重定向接口",
        "vendor_id": "",
        "vendor_name": "",
        "source_type": "spice_vmc"
      }
    ],
    "is_external_disk": false,
    "has_passthrough_disk": false,
    "kvm_clock_enable": true,
    "virt_nested_enable": false,
    "cpu_reserve_enable": false,
    "cpu_reserve_numa": false,
    "memory_reserve_enable": false,
    "expand_config": {
      "cpu_auto_expand_enable": false,
      "memory_auto_expand_enable": false,
      "max_expand_cpu": 0,
      "max_expand_mem": 0,
      "expand_cpu": 0,
      "expand_mem": 0
    },
    "data_localization_mode_on": "off",
    "pci_devices": null,
    "mdev_devices": null,
    "tpm_devices": null,
    "recover_to_related_zones": 2,
    "master_zone_take_over": 2,
    "cluster_uuid": "c27a25bc-5da2-430f-bfaf-6c8d33f21128",
    "cluster_name": "host3223-cvm3323"
  }
}
```

### GET&nbsp; /v1/compute/detail
获取虚拟机监控信息。要求虚拟机正在运行，并且已安装并连接Guest Agent。

<big>**请求参数**</big>  

名称 | 参数类型 | 是否必填 | 描述
---|---|---|---
 cluster_uuid|string|是| 集群uuid
 tenant|string|是| 租户uuid
 compute_uuid|string|是| 虚拟机uuid

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：
```
"data" : {
    "VmDetails" : {
        String : VmDetailStatistic
    },
    Ctime : Number
}
```

+ **VmDetails**  
虚拟机监控详情map，只有一个键值对。键为指定的虚拟机uuid，值为收集到的详细监控数据。
+ **Ctime**  
监控数据生成时间，unix时间。

<big>**示例**</big>  
**请求示例**  
```
https://10.30.33.25/v1/compute/detail?cluster_uuid=c27a25bc-5da2-430f-bfaf-6c8d33f21128&tenant=e1170fde-f0fe-4f91-a568-ac4b84f00aad&compute_uuid=8af4efa0-a175-4ffd-8859-deb355df3051
```
**返回示例**  
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
    "VmDetails": {
      "8af4efa0-a175-4ffd-8859-deb355df3051": {
        "VmName": "red22",
        "VmDetails": {
          "UUID": "8af4efa0-a175-4ffd-8859-deb355df3051",
          "GaConnected": true,
          "CpuStat": {
            "Model": "60",
            "ModelName": "Intel Core Processor (Haswell, no TSX, IBRS)",
            "Cores": 2,
            "Sockets": 1,
            "Mhz": 2299.996,
            "User": 0.0010471204188481473,
            "System": 0.0005638340716874706,
            "Idle": 0.9983084977849447,
            "Nice": 0,
            "Iowait": 0.00008054772452678662,
            "Irq": 0,
            "Softirq": 0,
            "Steal": 0,
            "Guest": 0,
            "GuestNice": 0,
            "Stolen": 0
          },
          "DiskPartitions": [
            {
              "Name": "dm-0",
              "Capacity": 9135194112,
              "Partitions": [
                {
                  "Device": "/dev/mapper/rhel-root",
                  "Mountpoint": "/",
                  "Fstype": "xfs",
                  "Opts": "rw,seclabel,relatime,attr2,inode64,noquota",
                  "Total": 17821696,
                  "Free": 15241936,
                  "UsedPercent": 14.475389996552519,
                  "InodesTotal": 8921088,
                  "InodesUsed": 25376,
                  "InodesFree": 8895712,
                  "InodesUsedPercent": 0.28444960973370065,
                  "Used": 2579760,
                  "LV": ""
                }
              ]
            },
            {
              "Name": "dm-1",
              "Capacity": 1073741824,
              "Partitions": [
                {
                  "Device": "/dev/mapper/rhel-swap",
                  "Mountpoint": "",
                  "Fstype": "swap",
                  "Opts": "",
                  "Total": 2097152,
                  "Free": 0,
                  "UsedPercent": 0,
                  "InodesTotal": 0,
                  "InodesUsed": 0,
                  "InodesFree": 0,
                  "InodesUsedPercent": 0,
                  "Used": 0,
                  "LV": ""
                }
              ]
            },
            {
              "Name": "/dev/sda",
              "Capacity": 10737418240,
              "Partitions": [
                {
                  "Device": "/dev/sda1",
                  "Mountpoint": "/boot",
                  "Fstype": "xfs",
                  "Opts": "rw,seclabel,relatime,attr2,inode64,noquota",
                  "Total": 1017176,
                  "Free": 821272,
                  "UsedPercent": 19.25959715919369,
                  "InodesTotal": 512000,
                  "InodesUsed": 329,
                  "InodesFree": 511671,
                  "InodesUsedPercent": 0.0642578125,
                  "Used": 195904,
                  "LV": ""
                },
                {
                  "Device": "/dev/sda2",
                  "Mountpoint": "",
                  "Fstype": "LVM2_member",
                  "Opts": "",
                  "Total": 19945472,
                  "Free": 0,
                  "UsedPercent": 0,
                  "InodesTotal": 0,
                  "InodesUsed": 0,
                  "InodesFree": 0,
                  "InodesUsedPercent": 0,
                  "Used": 0,
                  "LV": "rhel-root;rhel-swap;"
                }
              ]
            }
          ],
          "DiskStats": [
            {
              "Name": "sda",
              "SerialNumber": "",
              "Label": "",
              "ReadCount": 0,
              "MergedReadCount": 0,
              "WriteCount": 0,
              "MergedWriteCount": 0,
              "ReadBytes": 0,
              "WriteBytes": 102,
              "ReadTime": 0,
              "WriteTime": 0,
              "IopsInProgress": 0,
              "IoTime": 5,
              "WeightedIO": 0,
              "UsageRate": 0.00008334260783624865
            },
            {
              "Name": "sda1",
              "SerialNumber": "",
              "Label": "",
              "ReadCount": 0,
              "MergedReadCount": 0,
              "WriteCount": 0,
              "MergedWriteCount": 0,
              "ReadBytes": 0,
              "WriteBytes": 0,
              "ReadTime": 0,
              "WriteTime": 0,
              "IopsInProgress": 0,
              "IoTime": 0,
              "WeightedIO": 0,
              "UsageRate": 0
            },
            {
              "Name": "sda2",
              "SerialNumber": "",
              "Label": "",
              "ReadCount": 0,
              "MergedReadCount": 0,
              "WriteCount": 0,
              "MergedWriteCount": 0,
              "ReadBytes": 0,
              "WriteBytes": 102,
              "ReadTime": 0,
              "WriteTime": 0,
              "IopsInProgress": 0,
              "IoTime": 5,
              "WeightedIO": 0,
              "UsageRate": 0.00008334260783624865
            },
            {
              "Name": "dm-0",
              "SerialNumber": "",
              "Label": "",
              "ReadCount": 0,
              "MergedReadCount": 0,
              "WriteCount": 0,
              "MergedWriteCount": 0,
              "ReadBytes": 0,
              "WriteBytes": 102,
              "ReadTime": 0,
              "WriteTime": 0,
              "IopsInProgress": 0,
              "IoTime": 5,
              "WeightedIO": 0,
              "UsageRate": 0.00008334260783624865
            },
            {
              "Name": "dm-1",
              "SerialNumber": "",
              "Label": "",
              "ReadCount": 0,
              "MergedReadCount": 0,
              "WriteCount": 0,
              "MergedWriteCount": 0,
              "ReadBytes": 0,
              "WriteBytes": 0,
              "ReadTime": 0,
              "WriteTime": 0,
              "IopsInProgress": 0,
              "IoTime": 0,
              "WeightedIO": 0,
              "UsageRate": 0
            }
          ],
          "InterfaceStats": [
            {
              "Name": "eth0",
              "Mac": "52:56:ff:22:00:bd",
              "Bandwidth": 0,
              "BytesSend": 0,
              "BytesRecv": 0,
              "PacketSend": 0,
              "PacketRecv": 0,
              "Errin": 0,
              "Errout": 0,
              "Dropin": 0,
              "Dropout": 0,
              "Fifoin": 0,
              "Fifoout": 0,
              "Addresses": null,
              "MTU": 1500,
              "LinkState": "up"
            }
          ],
          "MemoryStat": {
            "Total": 3976568832,
            "Available": 3663679488,
            "Used": 159903744,
            "UsedPercent": 4.02114865240688,
            "Free": 3676676096,
            "Active": 133459968,
            "Inactive": 77012992,
            "Wired": 0,
            "Laundry": 0,
            "Buffers": 1478656,
            "Cached": 138510336,
            "Writeback": 0,
            "Dirty": 0,
            "WritebackTmp": 0,
            "Shared": 8835072,
            "Slab": 42360832,
            "PageTables": 3313664,
            "SwapCached": 0,
            "CommitLimit": 3062022144,
            "CommittedAS": 445161472,
            "HighTotal": 0,
            "HighFree": 0,
            "LowTotal": 0,
            "LowFree": 0,
            "SwapTotal": 1073737728,
            "SwapFree": 1073737728,
            "Mapped": 29409280,
            "VMallocTotal": 35184372087808,
            "VMallocUsed": 12341248,
            "VMallocChunk": 35184352149504,
            "HugePagesTotal": 0,
            "HugePagesFree": 0,
            "HugePageSize": 2097152
          },
          "SystemStatistic": {
            "ProcessCount": 96,
            "TCPCount": 6,
            "UDPCount": 2,
            "UnixCount": 135,
            "FDCount": 896
          },
          "OSInfo": {
            "KernelRelease": "3.10.0-123.el7.x86_64",
            "KernelVersion": "#1 SMP Mon May 5 11:16:57 EDT 2014",
            "Machine": "amd64",
            "ID": "rhel",
            "Name": "Red Hat Enterprise Linux Server",
            "PrettyName": "Red Hat Enterprise Linux Server 7.0 (Maipo)",
            "Version": "7.0 (Maipo)",
            "VersionID": "7.0",
            "Variant": "",
            "VariantID": ""
          },
          "TimeNano": 1629959529044115291
        }
      }
    },
    "Ctime": 1629959529
  }
}
```

### POST&nbsp; /v1/compute/unified_create
统一创建虚拟机接口。根据提供的参数创建存储卷、创建虚拟机、连接到VPC网络。支持批量创建。

<big>**请求参数**</big>  
```
{
    UnifiedComputeCreateRequest,
    CommonClusterTenantScope,
    "user_uuid" : String,
    "create_num" : Number
}
```

+ **UnifiedComputeCreateRequest**  
完整虚拟机统一创建参数。详细参数说明参见[UnifiedComputeCreateRequest](#unifiedcomputecreaterequest)。  
_必需_ ： 是
+ **CommonClusterTenantScope**  
指定虚拟机创建的目的集群、目的租户。  
_必需_ ： 是
+ **user_uuid**  
分配给指定用户uuid。若指定，则创建后的虚拟机自动分配给指定用户。  
_必需_ ： 否
+ **create_num**  
批量创建数量。若不指定，则只创建一台虚拟机。创建数量大于1时，创建虚拟机名会自动加上后缀`-index`。  
_必需_ ： 否

<big>**返回数据**</big>  
接口返回数据先使用[BatchOutput](#batchoutput)封装，再用[Output](#output)封装。接口特定返回如下：
```
"data" : {
    "tenant" : String,
    "vm_uuid" : String,
    "index" : Number,
    "vm_name" : String,
    "volume_uuids" : [ String ],
    "mac_addresses" : [ String ]
}
```

+ **tenant**  
租户uuid。和请求参数的租户uuid一致。
+ **vm_uuid**  
创建生成的虚拟机uuid。若创建失败，则该项为空。
+ **index**  
创建请求序号。用于和其它批量发起的请求做区分。
+ **vm_name** 
创建虚拟机名称，批量创建情况下。即使创建失败，该项也不为空。
+ **volume_uuids**  
创建生成的存储卷uuid。包括内置存储卷和共享存储卷。
+ **mac_addresses**  
创建生成的网卡MAC地址。  

如果创建虚拟机失败，成功创建的存储卷会被回滚。如果是连接VPC网络失败，虚拟机和存储卷会被保留，后续可以手动连接。

<big>**示例**</big>  
**请求示例**  
```
{"cluster_uuid":"c27a25bc-5da2-430f-bfaf-6c8d33f21128","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","object_group":"e9017aa7-e19b-47b0-b638-e639aa9451c6","zone":"2871bab9-d6ed-4100-8d74-9c4442b52bb5","cpunr":1,"cpu_sockets":1,"cpu_socket_cores":1,"baseline":"Haswell-noTSX-IBRS","max_cpu_nr":1,"mem_size":1073741824,"mem_max":274877906944,"memory_huge_pages_enable":false,"type":"GUS","image_uuid":"","os":"CentOS x64","cloud_init_data":null,"meta":{"compute_name":"test","ha_mode":"on","ha_config":{"priority":0},"os_loader_path":"BIOS","video":[{"model_type":"vga"}],"panic_model":"isa","vnc_enable":false,"mem_sec_enabled":false,"data_localization_mode_on":"off","virt_nested_enable":false,"recover_to_related_zones":2,"master_zone_take_over":2,"startup_setting":null},"interfaces":[{"interface_model_type":"virtio","interface_type":"ycb123","port_group":"239223b4-d21b-4b23-954f-796f17c75c49","port_group_name":"32012345678901234567890123456789","vlan_tag_ids":[14],"in_bount":{"average":0,"peak":0,"burst":0},"out_bount":{"average":0,"peak":0,"burst":0},"peer":"on","bound_ip":null,"mac_address":"","switch_uuid":"","switch_name":"","gateway_name":"","gateway_uuid":""}],"disks":[{"disk_target_bus":"scsi","disk_cache_mode":"none","disk_unified_vsd":{"pool_uuid":"42b3e3b6-b1d1-44c0-bf5c-b9cf73d594df","pool_name":"ycb1-1000","volume_name":"test-volume1","disk_capacity":1073741824,"capacity":1073741824,"snap_capacity":3221225472,"attribute":{"replica":"1","DriveType":"HDD","VsdVendor":"LIBTARGET","ComponentSetShift":"0"}},"disk_vsd_source":null,"image_name":null,"image_uuid":null,"repository_uuid":"","redundancy":1}],"cdrom":{"name":"","image_uuid":"","repository_uuid":""},"floppy":{"name":"","image_uuid":"","repository_uuid":""},"create_num":1,"vm_type":"GUS"}
```
**返回示例**  
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
          "tenant": "a5badacf-a25c-4171-9aff-b619fc2d300a",
          "vm_uuid": "e6b3a5bf-e079-469c-8563-ed45f624c6b3",
          "index": 0,
          "vm_name": "test",
          "volume_uuids": [
            "6ff91874-adca-4109-b844-448c2d4200d4"
          ],
          "mac_addresses": [
            "52:56:ff:55:be:fb"
          ],
          "group": "e9017aa7-e19b-47b0-b638-e639aa9451c6",
          "group_name": "default"
        }
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/unified_import
统一导入虚拟机接口。在统一创建虚拟机接口[/v1/compute/unified_create](#post-v1computeunified_create)的基础上，进一步发起镜像导入。

<big>**请求参数**</big>  
总体请求参数同统一创建虚拟机接口[/v1/compute/unified_create](#post-v1computeunified_create)。  
差异点在于，该接口在磁盘相关参数里，需要指定待导入镜像相关参数。

<big>**返回数据**</big>  
接口返回数据先使用[BatchOutput](#batchoutput)封装，再用[Output](#output)封装。接口特定返回如下：  
返回数据同统一创建虚拟机接口[/v1/compute/unified_create](#post-v1computeunified_create)。  

如果虚拟机创建成功，但是发起导入镜像失败，虚拟机会被保留，允许后续手动导入。  
如果发起导入镜像成功，即使导入过程在接口返回前就失败，也不影响该接口返回。  

<big>**示例**</big>  
**请求示例**  
```
POST https://10.30.33.25/v1/compute/unified_import
{"cluster_uuid":"c27a25bc-5da2-430f-bfaf-6c8d33f21128","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","object_group":"e9017aa7-e19b-47b0-b638-e639aa9451c6","zone":"2871bab9-d6ed-4100-8d74-9c4442b52bb5","cpunr":1,"cpu_sockets":1,"cpu_socket_cores":1,"baseline":"Haswell-noTSX-IBRS","max_cpu_nr":1,"mem_size":1073741824,"mem_max":274877906944,"memory_huge_pages_enable":false,"type":"GUS","image_uuid":"","os":"CentOS x64","cloud_init_data":null,"meta":{"compute_name":"test","ha_mode":"on","ha_config":{"priority":0},"os_loader_path":"BIOS","video":[{"model_type":"vga"}],"panic_model":"isa","vnc_enable":false,"mem_sec_enabled":false,"data_localization_mode_on":"off","virt_nested_enable":false,"recover_to_related_zones":2,"master_zone_take_over":2,"startup_setting":null},"interfaces":[{"interface_model_type":"virtio","interface_type":"ycb123","port_group":"239223b4-d21b-4b23-954f-796f17c75c49","port_group_name":"32012345678901234567890123456789","vlan_tag_ids":[14],"in_bount":{"average":0,"peak":0,"burst":0},"out_bount":{"average":0,"peak":0,"burst":0},"peer":"on","bound_ip":null,"mac_address":"","switch_uuid":"","switch_name":"","gateway_name":"","gateway_uuid":""}],"disks":[{"disk_target_bus":"scsi","disk_cache_mode":"none","disk_unified_vsd":{"pool_uuid":"42b3e3b6-b1d1-44c0-bf5c-b9cf73d594df","pool_name":"ycb1-1000","volume_name":"test-volume1","disk_capacity":3221225472,"capacity":3221225472,"snap_capacity":9663676416,"attribute":{"replica":"1","DriveType":"HDD","VsdVendor":"LIBTARGET","ComponentSetShift":"0"}},"disk_vsd_source":null,"image_name":"xenial-server-cloudimg-amd64-disk1.img","image_uuid":"caf1c032-8812-430f-98c3-f2117e3affe0","repository_uuid":"15dd8b65-d4be-434f-92f9-88d13264e4f6","redundancy":1}],"cdrom":{"name":"","image_uuid":"","repository_uuid":""},"floppy":{"name":"","image_uuid":"","repository_uuid":""},"create_num":1,"vm_type":"GUS"}
```
**返回示例**  
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
          "tenant": "a5badacf-a25c-4171-9aff-b619fc2d300a",
          "vm_uuid": "fadd9191-e26a-46af-be57-17f28c6b9b14",
          "index": 0,
          "vm_name": "test",
          "volume_uuids": [
            "93e34385-eea2-4ee0-b432-c9305271c89a"
          ],
          "mac_addresses": [
            "52:56:ff:95:d1:7b"
          ],
          "group": "",
          "group_name": ""
        }
      }
    ]
  }
}
```
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "success": 0,
    "fail": 1,
    "results": [
      {
        "scode": 22211,
        "desc": "compute repository mounting failed",
        "message": "Unified create Vm import image failure",
        "message_cn": "创建虚拟机导入镜像失败",
        "stack": [
          "host:10.30.33.23,pid:1378,module:center,code:22211,filename:manager.go,func:importVm,line:4616",
          "host:10.30.33.23,pid:1378,module:center,code:22211,filename:manager.go,func:importVm,line:4617",
          "host:10.30.33.25,pid:15886,module:manager,code:22211,filename:util.go,func:callCenterOnce,line:257",
          "host:10.30.33.25,pid:15886,module:manager,code:22211,filename:util.go,func:callCenter,line:135",
          "host:10.30.33.25,pid:15886,module:manager,code:22211,filename:util.go,func:callCenterV2,line:79",
          "host:10.30.33.25,pid:15886,module:manager,code:22211,filename:compute.go,func:ComputeUnifiedImport,line:62",
          "host:10.30.33.25,pid:15886,module:manager,code:22211,filename:compute.go,func:func1,line:628"
        ],
        "data": {
          "tenant": "",
          "vm_uuid": "",
          "index": 0,
          "vm_name": "test2",
          "volume_uuids": null,
          "mac_addresses": null,
          "group": "",
          "group_name": ""
        }
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/create/from_template
基于虚拟机模板创建虚拟机。

<big>**请求参数**</big>  
```
{
    CommonClusterTenantScope,
    "baseline" : String,
    "vm_template_id" : String,
    "user_uuid" : String,
    "vm_config_override" : UnifiedComputeCreateRequest,
    "create_num" : Number,
    "object_group" : String,
    "assign_vm_uuid" : String,
    CloneTypeParam,
    "auto_snapshot" : Bool
}
```

+ **CommonClusterTenantScope**  
指定集群、租户。  
_必需_ ： 是
+ **baseline**  
指定虚拟机CPU基准类型。覆盖虚拟机模板设置。  
_必需_ ： 否
+ **vm_template_id**  
指定虚拟机模板uuid。  
_必需_ ： 是
+ **user_uuid**  
分配用户uuid。若指定，创建出来的虚拟机分配给指定用户。  
_必需_ ： 否
+ **vm_config_override**  
虚拟机创建配置。创建时覆盖虚拟机模板的设置。  
_必需_ ： 否
+ **create_num**  
批量创建数量。用法同[/v1/compute/unified_create](#post-v1computeunified_create)的`create_num`参数。  
_必需_ ： 否
+ **object_group**  
虚拟机分组uuid。指定创建后虚拟机分组。  
_必需_ ： 否
+ **assign_vm_uuid**  
指定创建后的虚拟机uuid。不允许和已有虚拟机重复。  
_必需_ ： 否
+ **CloneTypeParam** 
存储卷克隆参数。用来控制存储卷克隆行为。  
_必需_ ： 否
+ **auto_snapshot**  
是否自动创建快照。创建出来的虚拟机会自动带一个快照，表示刚创建完成时的状态。  
_必需_ ： 否


<big>**返回数据**</big>  
接口返回数据先使用[BatchOutput](#batchoutput)封装，再用[Output](#output)封装。接口特定返回如下：  
返回数据同统一创建虚拟机接口[/v1/compute/unified_create](#post-v1computeunified_create)。  

<big>**示例**</big>  
**请求示例**  
```
POST https://10.30.33.25/v1/compute/create/from_template
{"cluster_uuid":"c27a25bc-5da2-430f-bfaf-6c8d33f21128","tenant":"3fd90c32-f753-46b3-9b6b-9d67724c95c5","object_group":"eefcd799-3c9f-46fa-aa48-d2cc65d944a6","vm_template_id":"d2c90a85-21c7-43c6-a9db-ad50eab6362c","link":false,"component_cache":false,"vm_config_override":{"tenant":"3fd90c32-f753-46b3-9b6b-9d67724c95c5","zone":"2871bab9-d6ed-4100-8d74-9c4442b52bb5","cpunr":1,"cpu_sockets":1,"cpu_socket_cores":2,"baseline":"Haswell-noTSX-IBRS","max_cpu_nr":2,"mem_size":1073741824,"mem_max":274877906944,"memory_huge_pages_enable":false,"type":"GUS","image_uuid":"","os":"CentOS x64","meta":{"compute_name":"q2eq","ha_mode":"on","ha_config":{"priority":0},"os_loader_path":"BIOS","video":[{"index":0,"heads":1,"model_type":"vga","ram_size":131072,"vga_mem":32768,"screen_size":"3840 * 2160","disabled":false,"modify_heads":false,"modify_error":"","modify_size":false,"modify_type":false}],"panic_model":"isa","vnc_enable":false,"mem_sec_enabled":false,"data_localization_mode_on":"off","virt_nested_enable":false,"recover_to_related_zones":2,"master_zone_take_over":2,"startup_setting":null},"disks":[{"disk_target_device":"sda","disk_cache_mode":"无缓存","disk_unified_vsd":{"tenant":"3fd90c32-f753-46b3-9b6b-9d67724c95c5","pool_uuid":"3a3b1a34-1926-4c45-b66e-b93f555c3199","volume_name":"q2eq-volume-1","capacity":16106127360,"snap_capacity":48318382080,"attribute":{"replica":"1","DriveType":"HDD","VsdVendor":"LIBTARGET"}},"redundancy":1,"is_old":true}],"interfaces":[{"interface_model_type":"virtio","interface_type":"mirror","port_group":"edc39bfd-339e-4c78-a0b9-aac517d42b39","port_group_name":"default","vlan_tag_ids":[0],"in_bount":{"average":0,"peak":0,"burst":0},"out_bount":{"average":0,"peak":0,"burst":0}}],"cdrom":{"name":"","repository_uuid":""},"floppy":{"name":"","repository_uuid":""}}}
```
**返回示例**  
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
          "tenant": "",
          "vm_uuid": "8490ea64-874e-4816-90e4-fd8ea537f99a",
          "index": 0,
          "vm_name": "q2eq",
          "volume_uuids": null,
          "mac_addresses": null,
          "group": "",
          "group_name": ""
        }
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/delete
删除虚拟机。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "real_delete" : Bool,
    "is_delete_volumes" : Bool,
    "exclusive_desktop_uuid" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是
+ **real_delete**  
是否永久删除。`real_delete=true`时，虚拟机被永久删除。`real_delete=false`时，虚拟机被放入回收站。当登录用户不是管理员时，该参数强制为`false`。  
_必需_ ： 否
+ **is_delete_volumes**  
是否同时删除存储卷。`real_delete=false`时，变为卷是否放入回收站。  
_必需_ ： 否
+ **exclusive_desktop_uuid**  
通知操作的桌面池uuid。指定该参数以后，会通知到已连接的VDC客户端，更新对应桌面池的数据。  
_必需_ ： 否  

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。

若删除虚拟机成功，但是删除存储卷时出错，接口并不会返回错误。存储卷会残留，需要手动清除。

<big>**示例**</big>  
**请求示例**  
```
POST http://10.30.33.25:8080/v1/compute/delete
{"cluster_uuid":"c27a25bc-5da2-430f-bfaf-6c8d33f21128","compute_uuid":"acb1a12c-861e-484c-aac3-08367bd00f54","compute_name":"test-api","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","real_delete":true,"is_delete_volumes":true}
```
**返回示例**  
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

### POST&nbsp; /v1/compute/batch_delete
批量删除虚拟机。  

<big>**请求参数**</big>  
```
{
    "vms" : [ ComputeIdentifier ],
    "real_delete" : Bool,
    "is_delete_volumes" : Bool,    
    "exclusive_desktop_uuid" : String,
    "vm_type" : String
}
```

+ **vms**  
指定要操作的虚拟机。  
_必需_ ： 是
+ **real_delete**  
是否永久删除。`real_delete=true`时，虚拟机被永久删除。`real_delete=false`时，虚拟机被放入回收站。当登录用户不是管理员时，该参数强制为`false`。  
_必需_ ： 否
+ **is_delete_volumes**  
是否同时删除存储卷。`real_delete=false`时，变为卷是否放入回收站。  
_必需_ ： 否
+ **exclusive_desktop_uuid**  
通知操作的桌面池uuid。指定该参数以后，会通知到已连接的VDC客户端，更新对应桌面池的数据。  
_必需_ ： 否  
+ **vm_type**  
仅用于虚拟机相关接口记录操作日志时，描述里额外区分请求对象是桌面虚拟机还是云桌面。  
_必需_ ： 否  
_有效值_ ： 
    - "GCD" 桌面虚拟机
    - "GDT" 云桌面
    - 其他 无额外标记

<big>**返回数据**</big>  
接口返回数据先使用[BatchOutput](#batchoutput)封装，再用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[BatchOutput](#batchoutput)字段表示报错。

若删除虚拟机成功，但是删除存储卷时出错，接口并不会返回错误。存储卷会残留，需要手动清除。

<big>**示例**</big>  
**请求示例**  
```
POST http://10.30.33.25:8080/v1/compute/batch_delete
{"vms":[{"cluster_uuid":"c27a25bc-5da2-430f-bfaf-6c8d33f21128","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","owner":"","compute_uuid":"26c486af-7db1-4cd1-b719-68b22c3d079c","compute_name":"test-api2","cloud_init":true},{"cluster_uuid":"c27a25bc-5da2-430f-bfaf-6c8d33f21128","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","owner":"","compute_uuid":"0372d849-55e8-4b0a-bac3-cd9dffe44939","compute_name":"test-api1","cloud_init":true}],"vm_type":"GUS","real_delete":true,"is_delete_volumes":true,"cluster_uuid":"c27a25bc-5da2-430f-bfaf-6c8d33f21128"}
```
**返回示例**  
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
          "cluster_uuid": "c27a25bc-5da2-430f-bfaf-6c8d33f21128",
          "cluster_name": "host3223-cvm3323",
          "tenant": "a5badacf-a25c-4171-9aff-b619fc2d300a",
          "compute_uuid": "26c486af-7db1-4cd1-b719-68b22c3d079c",
          "compute_name": "test-api2",
          "owner": "",
          "vdc_agent": "",
          "vdc_agent_list": null,
          "desktop_pool_uuid": ""
        }
      },
      {
        "scode": 0,
        "desc": "",
        "message": "success",
        "message_cn": "成功",
        "stack": null,
        "data": {
          "cluster_uuid": "c27a25bc-5da2-430f-bfaf-6c8d33f21128",
          "cluster_name": "host3223-cvm3323",
          "tenant": "a5badacf-a25c-4171-9aff-b619fc2d300a",
          "compute_uuid": "0372d849-55e8-4b0a-bac3-cd9dffe44939",
          "compute_name": "test-api1",
          "owner": "",
          "vdc_agent": "",
          "vdc_agent_list": null,
          "desktop_pool_uuid": ""
        }
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/start
启动虚拟机

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "cloud_init" : Bool,
    "is_repair" : Bool,
    "exclusive_desktop_uuid" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是
+ **cloud_init**  
启动时是否带有cloud_init设置。若`cloud_init=true`，启动时会占用一个ide盘符位。  
_必需_ ： 否
+ **is_repair**  
启动时是否修复存储卷。  
_必需_ ： 否
+ **exclusive_desktop_uuid**  
通知操作的桌面池uuid。指定该参数以后，会通知到已连接的VDC客户端，更新对应桌面池的数据。  
_必需_ ： 否

请求虚拟机启动，需要当前虚拟机处于关机状态，并且当前无动作，否则接口会报错。。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

除了虚拟机本身，主机、存储卷、可用资源等相关因素也可能导致启动报错。

<big>**示例**</big>  
**请求示例**  
```
POST http://10.30.33.25:8080/v1/compute/start
{"cluster_uuid":"c27a25bc-5da2-430f-bfaf-6c8d33f21128","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"76a8ef31-a98d-485c-b967-97cefefa5088","compute_name":"test-api","owner":"","vm_type":"GUS","cloud_init":true}
```
**返回示例**  
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

### POST&nbsp; /v1/compute/batch_start
批量启动虚拟机  

<big>**请求参数**</big>  
```
{
    "vms" : [ ComputeIdentifier ],
    "cloud_init" : Bool,
    "is_repair" : Bool,
    "exclusive_desktop_uuid" : String,
    "vm_type" : String
}
```

+ **vms**  
指定要操作的虚拟机。  
_必需_ ： 是
+ **cloud_init**  
启动时是否带有cloud_init设置。若`cloud_init=true`，启动时会占用一个ide盘符位。  
_必需_ ： 否
+ **is_repair**  
启动时是否修复存储卷。  
_必需_ ： 否
+ **exclusive_desktop_uuid**  
通知操作的桌面池uuid。指定该参数以后，会通知到已连接的VDC客户端，更新对应桌面池的数据。  
_必需_ ： 否  
+ **vm_type**  
仅用于虚拟机相关接口记录操作日志时，描述里额外区分请求对象是桌面虚拟机还是云桌面。  
_必需_ ： 否  
_有效值_ ： 
    - "GCD" 桌面虚拟机
    - "GDT" 云桌面
    - 其他 无额外标记

请求虚拟机启动，需要当前虚拟机处于关机状态，并且当前无动作，否则接口会报错。。

<big>**返回数据**</big>  
接口返回数据先使用[BatchOutput](#batchoutput)封装，再用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[BatchOutput](#batchoutput)字段表示报错。

除了虚拟机本身，主机、存储卷、可用资源等相关因素也可能导致启动报错。该请求启动的虚拟机也可能导致同请求的其他虚拟机无法启动。

<big>**示例**</big>  
**请求示例**  
POST http://10.30.33.25:8080/v1/compute/start
```json
{"vms":[{"cluster_uuid":"c27a25bc-5da2-430f-bfaf-6c8d33f21128","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","owner":"","compute_uuid":"648b2a69-2846-4a52-8393-1c3f5105a669","compute_name":"test-api2","cloud_init":true},{"cluster_uuid":"c27a25bc-5da2-430f-bfaf-6c8d33f21128","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","owner":"","compute_uuid":"76a8ef31-a98d-485c-b967-97cefefa5088","compute_name":"test-api","cloud_init":true}],"vm_type":"GUS","cluster_uuid":"c27a25bc-5da2-430f-bfaf-6c8d33f21128"}
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
    "success": 1,
    "fail": 1,
    "results": [
      {
        "scode": 20926,
        "desc": "",
        "message": "host do not satisfy cpu bloat limitation",
        "message_cn": "主机不满足CPU超分配限制",
        "stack": [
          "host:10.30.33.23,pid:26372,module:center,code:20926,filename:compute-host.go,func:Weigh,line:206",
          "host:10.30.33.23,pid:26372,module:center,code:20926,filename:scheduler.go,func:Weigh,line:95",
          "host:10.30.33.23,pid:26372,module:center,code:20926,filename:scheduler.go,func:Run,line:120",
          "host:10.30.33.23,pid:26372,module:center,code:20926,filename:scheduler.go,func:ScheduleComputeHostModeDefault,line:339",
          "host:10.30.33.23,pid:26372,module:center,code:20926,filename:scheduler.go,func:ScheduleComputeHost,line:189",
          "host:10.30.33.23,pid:26372,module:center,code:20926,filename:manager.go,func:StartVmOutSide,line:424",
          "host:10.30.33.25,pid:30060,module:manager,code:20926,filename:util.go,func:callCenterOnce,line:257",
          "host:10.30.33.25,pid:30060,module:manager,code:20926,filename:util.go,func:callCenter,line:135",
          "host:10.30.33.25,pid:30060,module:manager,code:20926,filename:util.go,func:callCenterV2,line:79",
          "host:10.30.33.25,pid:30060,module:manager,code:20926,filename:compute.go,func:ComputeStart,line:101",
          "host:10.30.33.25,pid:30060,module:manager,code:20926,filename:compute.go,func:func1,line:4299"
        ],
        "data": {
          "cluster_uuid": "c27a25bc-5da2-430f-bfaf-6c8d33f21128",
          "cluster_name": "host3223-cvm3323",
          "tenant": "a5badacf-a25c-4171-9aff-b619fc2d300a",
          "compute_uuid": "76a8ef31-a98d-485c-b967-97cefefa5088",
          "compute_name": "test-api",
          "owner": "",
          "vdc_agent": "",
          "vdc_agent_list": null,
          "desktop_pool_uuid": ""
        }
      },
      {
        "scode": 0,
        "desc": "",
        "message": "success",
        "message_cn": "成功",
        "stack": null,
        "data": {
          "cluster_uuid": "c27a25bc-5da2-430f-bfaf-6c8d33f21128",
          "cluster_name": "host3223-cvm3323",
          "tenant": "a5badacf-a25c-4171-9aff-b619fc2d300a",
          "compute_uuid": "648b2a69-2846-4a52-8393-1c3f5105a669",
          "compute_name": "test-api2",
          "owner": "",
          "vdc_agent": "",
          "vdc_agent_list": null,
          "desktop_pool_uuid": ""
        }
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/shutdown
安全关闭虚拟机。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "exclusive_desktop_uuid" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是
+ **exclusive_desktop_uuid**  
通知操作的桌面池uuid。指定该参数以后，会通知到已连接的VDC客户端，更新对应桌面池的数据。  
_必需_ ： 否

要请求安全关闭虚拟机，虚拟机要求运行状态，无动作，Agent状态为已连接("connected")。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

接口返回无报错的情况，只代表关机请求已发送，触发虚拟机操作系统关机。虚拟机关机实际生效，需要等虚拟机操作系统完成所有关机准备，保存完数据，实际执行关机。也就是说，存在安全关闭虚拟机请求正常返回，但是虚拟机一直不关闭保持正常运行状态的情况。

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"bdc01c45-973c-4b7b-a565-7a03c74379e4","tenant":"a0313629-10fd-48dc-9e92-5dff744a3c0e","compute_uuid":"dbffd091-63b7-451c-831b-6f8154c007e4","compute_name":"centos-cgt","owner":""}
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


### POST&nbsp; /v1/compute/batch_shutdown
批量安全关闭虚拟机。

<big>**请求参数**</big>  
```
{
    "vms" : [ ComputeIdentifier ],
    "exclusive_desktop_uuid" : String,
    "vm_type" : String
}
```

+ **vms**  
指定要操作的虚拟机。  
_必需_ ： 是
+ **exclusive_desktop_uuid**  
通知操作的桌面池uuid。指定该参数以后，会通知到已连接的VDC客户端，更新对应桌面池的数据。  
_必需_ ： 否  
+ **vm_type**  
仅用于虚拟机相关接口记录操作日志时，描述里额外区分请求对象是桌面虚拟机还是云桌面。  
_必需_ ： 否  
_有效值_ ： 
    - "GCD" 桌面虚拟机
    - "GDT" 云桌面
    - 其他 无额外标记

要请求安全关闭虚拟机，虚拟机要求运行状态，无动作，Agent状态为已连接("connected")。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[BatchOutput](#batchoutput)字段表示报错。  

接口返回无报错的情况，只代表关机请求已发送，触发虚拟机操作系统关机。虚拟机关机实际生效，需要等虚拟机操作系统完成所有关机准备，保存完数据，实际执行关机。也就是说，存在安全关闭虚拟机请求正常返回，但是虚拟机一直不关闭保持正常运行状态的情况。

<big>**示例**</big>  
**请求示例**  
```json
{"vms":[{"cluster_uuid":"bdc01c45-973c-4b7b-a565-7a03c74379e4","tenant":"a0313629-10fd-48dc-9e92-5dff744a3c0e","owner":"","compute_uuid":"dbffd091-63b7-451c-831b-6f8154c007e4","compute_name":"centos-cgt"}],"vm_type":"GUS","cluster_uuid":"bdc01c45-973c-4b7b-a565-7a03c74379e4"}
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
          "cluster_uuid": "bdc01c45-973c-4b7b-a565-7a03c74379e4",
          "cluster_name": "12-150",
          "tenant": "a0313629-10fd-48dc-9e92-5dff744a3c0e",
          "compute_uuid": "dbffd091-63b7-451c-831b-6f8154c007e4",
          "compute_name": "centos-cgt",
          "owner": "",
          "vdc_agent": "",
          "vdc_agent_list": null,
          "desktop_pool_uuid": ""
        }
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/shutoff
关闭虚拟机

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "exclusive_desktop_uuid" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是
+ **exclusive_desktop_uuid**  
通知操作的桌面池uuid。指定该参数以后，会通知到已连接的VDC客户端，更新对应桌面池的数据。  
_必需_ ： 否

要请求关闭的虚拟机，要求为运行状态，无动作。不依赖Agent状态。虚拟机直接执行断电操作。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：
特定返回为空。使用[Output](#output)字段表示报错。  

关闭虚拟机接口为同步接口，接口返回无报错，就代表虚拟机断电关闭完成。

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"c27a25bc-5da2-430f-bfaf-6c8d33f21128","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"76a8ef31-a98d-485c-b967-97cefefa5088","compute_name":"test-api","owner":"","vm_type":"GUS"}
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

### POST&nbsp; /v1/compute/batch_shutoff
批量关闭虚拟机。

<big>**请求参数**</big>  
```
{
    "vms" : [ ComputeIdentifier ],
    "exclusive_desktop_uuid" : String,
    "vm_type" : String
}
```

+ **vms**  
指定要操作的虚拟机。  
_必需_ ： 是
+ **exclusive_desktop_uuid**  
通知操作的桌面池uuid。指定该参数以后，会通知到已连接的VDC客户端，更新对应桌面池的数据。  
_必需_ ： 否  
+ **vm_type**  
仅用于虚拟机相关接口记录操作日志时，描述里额外区分请求对象是桌面虚拟机还是云桌面。  
_必需_ ： 否  
_有效值_ ： 
    - "GCD" 桌面虚拟机
    - "GDT" 云桌面
    - 其他 无额外标记

要请求关闭的虚拟机，要求为运行状态，无动作。不依赖Agent状态。虚拟机直接执行断电操作。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[BatchOutput](#batchoutput)字段表示报错。  

关闭虚拟机接口为同步接口，接口返回无报错，就代表虚拟机断电关闭完成。

<big>**示例**</big>  
**请求示例**  
```json
{"vms":[{"cluster_uuid":"bdc01c45-973c-4b7b-a565-7a03c74379e4","tenant":"a0313629-10fd-48dc-9e92-5dff744a3c0e","owner":"","compute_uuid":"dbffd091-63b7-451c-831b-6f8154c007e4","compute_name":"centos-cgt"}],"vm_type":"GUS","cluster_uuid":"bdc01c45-973c-4b7b-a565-7a03c74379e4"}
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
          "cluster_uuid": "bdc01c45-973c-4b7b-a565-7a03c74379e4",
          "cluster_name": "12-150",
          "tenant": "a0313629-10fd-48dc-9e92-5dff744a3c0e",
          "compute_uuid": "dbffd091-63b7-451c-831b-6f8154c007e4",
          "compute_name": "centos-cgt",
          "owner": "",
          "vdc_agent": "",
          "vdc_agent_list": null,
          "desktop_pool_uuid": ""
        }
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/reboot
重启虚拟机。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "exclusive_desktop_uuid" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是
+ **exclusive_desktop_uuid**  
通知操作的桌面池uuid。指定该参数以后，会通知到已连接的VDC客户端，更新对应桌面池的数据。  
_必需_ ： 否

要请求重启的虚拟机，要求为运行状态，无动作。要求Agent状态为已连接("connected")。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

该重启虚拟机为异步操作。接口返回只代表操作正常发起，需要等待虚拟机实际触发重启。

<big>**示例**</big>  
```json
{"cluster_uuid":"c27a25bc-5da2-430f-bfaf-6c8d33f21128","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"76a8ef31-a98d-485c-b967-97cefefa5088","compute_name":"test-api","owner":"","vm_type":"GUS"}
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

### POST&nbsp; /v1/compute/batch_reboot
批量重启虚拟机。

<big>**请求参数**</big>  
```
{
    "vms" : [ ComputeIdentifier ],
    "exclusive_desktop_uuid" : String,
    "vm_type" : String
}
```

+ **vms**  
指定要操作的虚拟机。  
_必需_ ： 是
+ **exclusive_desktop_uuid**  
通知操作的桌面池uuid。指定该参数以后，会通知到已连接的VDC客户端，更新对应桌面池的数据。  
_必需_ ： 否  
+ **vm_type**  
仅用于虚拟机相关接口记录操作日志时，描述里额外区分请求对象是桌面虚拟机还是云桌面。  
_必需_ ： 否  
_有效值_ ： 
    - "GCD" 桌面虚拟机
    - "GDT" 云桌面
    - 其他 无额外标记

要请求重启的虚拟机，要求为运行状态，无动作。要求Agent状态为已连接("connected")。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[BatchOutput](#batchoutput)字段表示报错。  

该重启虚拟机为异步操作。接口返回只代表操作正常发起，需要等待虚拟机实际触发重启。

<big>**示例**</big>  
**请求示例**  
```json
{"vms":[{"cluster_uuid":"bdc01c45-973c-4b7b-a565-7a03c74379e4","tenant":"a0313629-10fd-48dc-9e92-5dff744a3c0e","owner":"","compute_uuid":"dbffd091-63b7-451c-831b-6f8154c007e4","compute_name":"centos-cgt"}],"vm_type":"GUS","cluster_uuid":"bdc01c45-973c-4b7b-a565-7a03c74379e4"}
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
          "cluster_uuid": "bdc01c45-973c-4b7b-a565-7a03c74379e4",
          "cluster_name": "12-150",
          "tenant": "a0313629-10fd-48dc-9e92-5dff744a3c0e",
          "compute_uuid": "dbffd091-63b7-451c-831b-6f8154c007e4",
          "compute_name": "centos-cgt",
          "owner": "",
          "vdc_agent": "",
          "vdc_agent_list": null,
          "desktop_pool_uuid": ""
        }
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/reboot_ga
通过Agent重启虚拟机。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "exclusive_desktop_uuid" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是
+ **exclusive_desktop_uuid**  
通知操作的桌面池uuid。指定该参数以后，会通知到已连接的VDC客户端，更新对应桌面池的数据。  
_必需_ ： 否

要请求重启的虚拟机，要求为运行状态，无动作。要求Agent状态为已连接("connected")。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

该重启虚拟机为异步操作。接口返回只代表操作正常发起，需要等待虚拟机实际触发重启。

<big>**示例**</big>  
```json
{"cluster_uuid":"c27a25bc-5da2-430f-bfaf-6c8d33f21128","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"76a8ef31-a98d-485c-b967-97cefefa5088","compute_name":"test-api","owner":"","vm_type":"GUS"}
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

### POST&nbsp; /v1/compute/batch_reboot_ga
批量重启虚拟机。

<big>**请求参数**</big>  
```
{
    "vms" : [ ComputeIdentifier ],
    "exclusive_desktop_uuid" : String,
    "vm_type" : String
}
```

+ **vms**  
指定要操作的虚拟机。  
_必需_ ： 是
+ **exclusive_desktop_uuid**  
通知操作的桌面池uuid。指定该参数以后，会通知到已连接的VDC客户端，更新对应桌面池的数据。  
_必需_ ： 否  
+ **vm_type**  
仅用于虚拟机相关接口记录操作日志时，描述里额外区分请求对象是桌面虚拟机还是云桌面。  
_必需_ ： 否  
_有效值_ ： 
    - "GCD" 桌面虚拟机
    - "GDT" 云桌面
    - 其他 无额外标记

要请求重启的虚拟机，要求为运行状态，无动作。要求Agent状态为已连接("connected")。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[BatchOutput](#batchoutput)字段表示报错。  

该重启虚拟机为异步操作。接口返回只代表操作正常发起，需要等待虚拟机实际触发重启。

<big>**示例**</big>  
**请求示例**  
```json
{"vms":[{"cluster_uuid":"bdc01c45-973c-4b7b-a565-7a03c74379e4","tenant":"a0313629-10fd-48dc-9e92-5dff744a3c0e","owner":"","compute_uuid":"dbffd091-63b7-451c-831b-6f8154c007e4","compute_name":"centos-cgt"}],"vm_type":"GUS","cluster_uuid":"bdc01c45-973c-4b7b-a565-7a03c74379e4"}
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
          "cluster_uuid": "bdc01c45-973c-4b7b-a565-7a03c74379e4",
          "cluster_name": "12-150",
          "tenant": "a0313629-10fd-48dc-9e92-5dff744a3c0e",
          "compute_uuid": "dbffd091-63b7-451c-831b-6f8154c007e4",
          "compute_name": "centos-cgt",
          "owner": "",
          "vdc_agent": "",
          "vdc_agent_list": null,
          "desktop_pool_uuid": ""
        }
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/reset
硬重启虚拟机。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "exclusive_desktop_uuid" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是
+ **exclusive_desktop_uuid**  
通知操作的桌面池uuid。指定该参数以后，会通知到已连接的VDC客户端，更新对应桌面池的数据。  
_必需_ ： 否

要请求重启的虚拟机，要求为运行状态，无动作。不要求Agent状态。虚拟机会断电重启，未保存的数据会丢失。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

该重启接口为同步接口。接口返回无报错即代表重启操作完成。

<big>**示例**</big>  
```json
{"cluster_uuid":"c27a25bc-5da2-430f-bfaf-6c8d33f21128","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"76a8ef31-a98d-485c-b967-97cefefa5088","compute_name":"test-api","owner":"","vm_type":"GUS"}
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

### POST&nbsp; /v1/compute/batch_reset
批量硬重启虚拟机。

<big>**请求参数**</big>  
```
{
    "vms" : [ ComputeIdentifier ],
    "exclusive_desktop_uuid" : String,
    "vm_type" : String
}
```

+ **vms**  
指定要操作的虚拟机。  
_必需_ ： 是
+ **exclusive_desktop_uuid**  
通知操作的桌面池uuid。指定该参数以后，会通知到已连接的VDC客户端，更新对应桌面池的数据。  
_必需_ ： 否  
+ **vm_type**  
仅用于虚拟机相关接口记录操作日志时，描述里额外区分请求对象是桌面虚拟机还是云桌面。  
_必需_ ： 否  
_有效值_ ： 
    - "GCD" 桌面虚拟机
    - "GDT" 云桌面
    - 其他 无额外标记

要请求重启的虚拟机，要求为运行状态，无动作。不要求Agent状态。虚拟机会断电重启，未保存的数据会丢失。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[BatchOutput](#batchoutput)字段表示报错。  

该重启接口为同步接口。接口返回无报错即代表重启操作完成。

<big>**示例**</big>  
**请求示例**  
```json
{"vms":[{"cluster_uuid":"bdc01c45-973c-4b7b-a565-7a03c74379e4","tenant":"a0313629-10fd-48dc-9e92-5dff744a3c0e","owner":"","compute_uuid":"dbffd091-63b7-451c-831b-6f8154c007e4","compute_name":"centos-cgt"}],"vm_type":"GUS","cluster_uuid":"bdc01c45-973c-4b7b-a565-7a03c74379e4"}
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
          "cluster_uuid": "bdc01c45-973c-4b7b-a565-7a03c74379e4",
          "cluster_name": "12-150",
          "tenant": "a0313629-10fd-48dc-9e92-5dff744a3c0e",
          "compute_uuid": "dbffd091-63b7-451c-831b-6f8154c007e4",
          "compute_name": "centos-cgt",
          "owner": "",
          "vdc_agent": "",
          "vdc_agent_list": null,
          "desktop_pool_uuid": ""
        }
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/suspend
暂停虚拟机。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "exclusive_desktop_uuid" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是
+ **exclusive_desktop_uuid**  
通知操作的桌面池uuid。指定该参数以后，会通知到已连接的VDC客户端，更新对应桌面池的数据。  
_必需_ ： 否

要求待暂停的虚拟机，处于运行状态、无动作。不限制Agent状态。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

该暂停接口为同步接口。接口返回无报错即代表暂停操作完成，虚拟机变为暂停状态。

<big>**示例**</big>  
```json
{"cluster_uuid":"c27a25bc-5da2-430f-bfaf-6c8d33f21128","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"76a8ef31-a98d-485c-b967-97cefefa5088","compute_name":"test-api","owner":"","vm_type":"GUS"}
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

### POST&nbsp; /v1/compute/batch_suspend
批量暂停虚拟机。

<big>**请求参数**</big>  
```
{
    "vms" : [ ComputeIdentifier ],
    "exclusive_desktop_uuid" : String,
    "vm_type" : String
}
```

+ **vms**  
指定要操作的虚拟机。  
_必需_ ： 是
+ **exclusive_desktop_uuid**  
通知操作的桌面池uuid。指定该参数以后，会通知到已连接的VDC客户端，更新对应桌面池的数据。  
_必需_ ： 否  
+ **vm_type**  
仅用于虚拟机相关接口记录操作日志时，描述里额外区分请求对象是桌面虚拟机还是云桌面。  
_必需_ ： 否  
_有效值_ ： 
    - "GCD" 桌面虚拟机
    - "GDT" 云桌面
    - 其他 无额外标记

要求待暂停的虚拟机，处于运行状态、无动作。不限制Agent状态。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[BatchOutput](#batchoutput)字段表示报错。  

该暂停接口为同步接口。接口返回无报错即代表暂停操作完成，虚拟机变为暂停状态。

<big>**示例**</big>  
**请求示例**  
```json
{"vms":[{"cluster_uuid":"bdc01c45-973c-4b7b-a565-7a03c74379e4","tenant":"a0313629-10fd-48dc-9e92-5dff744a3c0e","owner":"","compute_uuid":"dbffd091-63b7-451c-831b-6f8154c007e4","compute_name":"centos-cgt"}],"vm_type":"GUS","cluster_uuid":"bdc01c45-973c-4b7b-a565-7a03c74379e4"}
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
          "cluster_uuid": "bdc01c45-973c-4b7b-a565-7a03c74379e4",
          "cluster_name": "12-150",
          "tenant": "a0313629-10fd-48dc-9e92-5dff744a3c0e",
          "compute_uuid": "dbffd091-63b7-451c-831b-6f8154c007e4",
          "compute_name": "centos-cgt",
          "owner": "",
          "vdc_agent": "",
          "vdc_agent_list": null,
          "desktop_pool_uuid": ""
        }
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/resume
恢复虚拟机。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "exclusive_desktop_uuid" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是
+ **exclusive_desktop_uuid**  
通知操作的桌面池uuid。指定该参数以后，会通知到已连接的VDC客户端，更新对应桌面池的数据。  
_必需_ ： 否

要求待恢复的虚拟机，处于暂停状态、无动作。不限制Agent状态。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

该恢复接口为同步接口。接口返回无报错即代表恢复操作完成，虚拟机进入运行状态。

<big>**示例**</big>  
```json
{"cluster_uuid":"c27a25bc-5da2-430f-bfaf-6c8d33f21128","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"76a8ef31-a98d-485c-b967-97cefefa5088","compute_name":"test-api","owner":"","vm_type":"GUS"}
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

### POST&nbsp; /v1/compute/batch_resume
批量恢复虚拟机。

<big>**请求参数**</big>  
```
{
    "vms" : [ ComputeIdentifier ],
    "exclusive_desktop_uuid" : String,
    "vm_type" : String
}
```

+ **vms**  
指定要操作的虚拟机。  
_必需_ ： 是
+ **exclusive_desktop_uuid**  
通知操作的桌面池uuid。指定该参数以后，会通知到已连接的VDC客户端，更新对应桌面池的数据。  
_必需_ ： 否  
+ **vm_type**  
仅用于虚拟机相关接口记录操作日志时，描述里额外区分请求对象是桌面虚拟机还是云桌面。  
_必需_ ： 否  
_有效值_ ： 
    - "GCD" 桌面虚拟机
    - "GDT" 云桌面
    - 其他 无额外标记

要求待恢复的虚拟机，处于暂停状态、无动作。不限制Agent状态。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[BatchOutput](#batchoutput)字段表示报错。  

该恢复接口为同步接口。接口返回无报错即代表恢复操作完成，虚拟机进入运行状态。

<big>**示例**</big>  
**请求示例**  
```json
{"vms":[{"cluster_uuid":"bdc01c45-973c-4b7b-a565-7a03c74379e4","tenant":"a0313629-10fd-48dc-9e92-5dff744a3c0e","owner":"","compute_uuid":"dbffd091-63b7-451c-831b-6f8154c007e4","compute_name":"centos-cgt"}],"vm_type":"GUS","cluster_uuid":"bdc01c45-973c-4b7b-a565-7a03c74379e4"}
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
          "cluster_uuid": "bdc01c45-973c-4b7b-a565-7a03c74379e4",
          "cluster_name": "12-150",
          "tenant": "a0313629-10fd-48dc-9e92-5dff744a3c0e",
          "compute_uuid": "dbffd091-63b7-451c-831b-6f8154c007e4",
          "compute_name": "centos-cgt",
          "owner": "",
          "vdc_agent": "",
          "vdc_agent_list": null,
          "desktop_pool_uuid": ""
        }
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/save
休眠虚拟机。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "exclusive_desktop_uuid" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是
+ **exclusive_desktop_uuid**  
通知操作的桌面池uuid。指定该参数以后，会通知到已连接的VDC客户端，更新对应桌面池的数据。  
_必需_ ： 否

要求待休眠的虚拟机，处于运行状态、无动作。不限制Agent状态。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

该休眠接口为同步接口。接口返回无报错即代表恢复操作完成，虚拟机进入休眠状态。  
因为休眠操作涉及将内存数据写入磁盘，接口返回时间和超时时间都会较长。

<big>**示例**</big>  
```json
{"cluster_uuid":"c27a25bc-5da2-430f-bfaf-6c8d33f21128","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"76a8ef31-a98d-485c-b967-97cefefa5088","compute_name":"test-api","owner":"","vm_type":"GUS"}
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

### POST&nbsp; /v1/compute/batch_save
批量休眠虚拟机。

<big>**请求参数**</big>  
```
{
    "vms" : [ ComputeIdentifier ],
    "exclusive_desktop_uuid" : String,
    "vm_type" : String
}
```

+ **vms**  
指定要操作的虚拟机。  
_必需_ ： 是
+ **exclusive_desktop_uuid**  
通知操作的桌面池uuid。指定该参数以后，会通知到已连接的VDC客户端，更新对应桌面池的数据。  
_必需_ ： 否  
+ **vm_type**  
仅用于虚拟机相关接口记录操作日志时，描述里额外区分请求对象是桌面虚拟机还是云桌面。  
_必需_ ： 否  
_有效值_ ： 
    - "GCD" 桌面虚拟机
    - "GDT" 云桌面
    - 其他 无额外标记

要求待休眠的虚拟机，处于运行状态、无动作。不限制Agent状态。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[BatchOutput](#batchoutput)字段表示报错。  

该休眠接口为同步接口。接口返回无报错即代表恢复操作完成，虚拟机进入休眠状态。  
因为休眠操作涉及将内存数据写入磁盘，接口返回时间和超时时间都会较长。

<big>**示例**</big>  
**请求示例**  
```json
{"vms":[{"cluster_uuid":"bdc01c45-973c-4b7b-a565-7a03c74379e4","tenant":"a0313629-10fd-48dc-9e92-5dff744a3c0e","owner":"","compute_uuid":"dbffd091-63b7-451c-831b-6f8154c007e4","compute_name":"centos-cgt"}],"vm_type":"GUS","cluster_uuid":"bdc01c45-973c-4b7b-a565-7a03c74379e4"}
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
          "cluster_uuid": "bdc01c45-973c-4b7b-a565-7a03c74379e4",
          "cluster_name": "12-150",
          "tenant": "a0313629-10fd-48dc-9e92-5dff744a3c0e",
          "compute_uuid": "dbffd091-63b7-451c-831b-6f8154c007e4",
          "compute_name": "centos-cgt",
          "owner": "",
          "vdc_agent": "",
          "vdc_agent_list": null,
          "desktop_pool_uuid": ""
        }
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/restore
唤醒虚拟机。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "exclusive_desktop_uuid" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是
+ **exclusive_desktop_uuid**  
通知操作的桌面池uuid。指定该参数以后，会通知到已连接的VDC客户端，更新对应桌面池的数据。  
_必需_ ： 否

要求待唤醒的虚拟机，处于休眠状态、无动作。不限制Agent状态。  
该接口同样可唤醒因操作系统睡眠而进入的休眠状态。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

该唤醒接口为同步接口。接口返回无报错即代表唤醒操作完成，虚拟机进入运行状态。  

<big>**示例**</big>  
```json
{"cluster_uuid":"c27a25bc-5da2-430f-bfaf-6c8d33f21128","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"76a8ef31-a98d-485c-b967-97cefefa5088","compute_name":"test-api","owner":"","vm_type":"GUS"}
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

### POST&nbsp; /v1/compute/batch_restore
批量唤醒虚拟机。

<big>**请求参数**</big>  
```
{
    "vms" : [ ComputeIdentifier ],
    "exclusive_desktop_uuid" : String,
    "vm_type" : String
}
```

+ **vms**  
指定要操作的虚拟机。  
_必需_ ： 是
+ **exclusive_desktop_uuid**  
通知操作的桌面池uuid。指定该参数以后，会通知到已连接的VDC客户端，更新对应桌面池的数据。  
_必需_ ： 否  
+ **vm_type**  
仅用于虚拟机相关接口记录操作日志时，描述里额外区分请求对象是桌面虚拟机还是云桌面。  
_必需_ ： 否  
_有效值_ ： 
    - "GCD" 桌面虚拟机
    - "GDT" 云桌面
    - 其他 无额外标记

要求待唤醒的虚拟机，处于休眠状态、无动作。不限制Agent状态。  
该接口同样可唤醒因操作系统睡眠而进入的休眠状态。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[BatchOutput](#batchoutput)字段表示报错。  

该唤醒接口为同步接口。接口返回无报错即代表唤醒操作完成，虚拟机进入运行状态。  

<big>**示例**</big>  
**请求示例**  
```json
{"vms":[{"cluster_uuid":"bdc01c45-973c-4b7b-a565-7a03c74379e4","tenant":"a0313629-10fd-48dc-9e92-5dff744a3c0e","owner":"","compute_uuid":"dbffd091-63b7-451c-831b-6f8154c007e4","compute_name":"centos-cgt"}],"vm_type":"GUS","cluster_uuid":"bdc01c45-973c-4b7b-a565-7a03c74379e4"}
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
          "cluster_uuid": "bdc01c45-973c-4b7b-a565-7a03c74379e4",
          "cluster_name": "12-150",
          "tenant": "a0313629-10fd-48dc-9e92-5dff744a3c0e",
          "compute_uuid": "dbffd091-63b7-451c-831b-6f8154c007e4",
          "compute_name": "centos-cgt",
          "owner": "",
          "vdc_agent": "",
          "vdc_agent_list": null,
          "desktop_pool_uuid": ""
        }
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/balloon/set
设置内存气球。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "memory" : Number
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是
+ **memory**  
指定内存气球大小，单位bytes。允许设置0字节。
_必需_ ： 否

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"c27a25bc-5da2-430f-bfaf-6c8d33f21128","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"76a8ef31-a98d-485c-b967-97cefefa5088","compute_name":"test-api","vm_type":"GUS","memory":0}
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

### POST&nbsp; /v1/compute/log
获取虚拟机操作日志。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：
```
"data" : {
    "total_count" : Number,
    "infos" : [ VmLog ]
}
```

+ **total_count**  
操作日志总数。
+ **infos**  
详细操作日志信息。具体结构见[VmLog](#vmlog)

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","compute_uuid":"249725f2-adb2-4f61-8285-a9e6c358a51c","compute_name":"Redhat7-64(converter)-普通备份恢复1-5","tenant":"8f6dbbae-018d-442e-908f-6a8f2167971f","tenant_name":"kobe"}
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
    "total_count": 2,
    "infos": [
      {
        "UUID": "f5e7fd31-a153-4ab8-aafb-efc03a9fcce1",
        "ObjectType": "Compute",
        "ObjectUUID": "249725f2-adb2-4f61-8285-a9e6c358a51c",
        "ObjectName": "Redhat7-64(converter)-普通备份恢复1-5",
        "Ctime": 1630307978,
        "Message": "云服务器断电",
        "StartTime": 1630307978,
        "EndTime": 1630307978
      },
      {
        "UUID": "28219e35-d394-4987-8c94-45401e1d5cc2",
        "ObjectType": "Compute",
        "ObjectUUID": "249725f2-adb2-4f61-8285-a9e6c358a51c",
        "ObjectName": "Redhat7-64(converter)-普通备份恢复1-5",
        "Ctime": 1630303891,
        "Message": "云服务器启动",
        "StartTime": 1630303888,
        "EndTime": 1630303891
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/vcpu/set
设置虚拟机CPU数量。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "cpu_current" : Number,
    "cpu_max" : Number,
    "cpu_sockets" : Number,
    "cpu_socket_cores" : Number
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是
+ **cpu_current**  
设置虚拟机当前CPU核心数量。  
_必需_ ： 否
+ **cpu_max**  
设置虚拟机最大CPU核心数量。  
_必需_ ： 否
+ **cpu_sockets**  
设置虚拟机CPU插槽数。即CPU数量。  
_必需_ ： 否
+ **cpu_socket_cores**  
设置虚拟机CPU插槽核数。即每个插槽的CPU核心数量。  
_必需_ ： 否

虚拟机当前CPU核心数不能大于最大CPU核心数量。
CPU插槽数\*插槽核数=最大CPU核心数。修改最大核心数会导致对应修改插槽核数，保持插槽数。修改插槽数或插槽核数会导致对于修改最大核心数。两种修改同时指定且冲突时，接口会报错。

设置最大CPU核心数量、CPU插槽数、CPU插槽核数时，要求虚拟机为关机状态、无动作。
设置虚拟机当前CPU核心数量，可以在虚拟机运行时设置不小于旧值的值，对虚拟机做热添加CPU核心操作。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  
<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"bdc01c45-973c-4b7b-a565-7a03c74379e4","compute_uuid":"941a6937-5e62-455d-a18e-2c1aab33b774","compute_name":"centos","tenant":"a0313629-10fd-48dc-9e92-5dff744a3c0e","cpu_current":2,"cpu_max":2,"cpu_sockets":1,"cpu_socket_cores":2}
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

### POST&nbsp; /v1/compute/vgpu/set
设置虚拟机图形接口。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "compression" : String,
    "mode" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是
+ **compression**  
图像压缩模式。  
_必需_ ： 否  
_有效值_ : "off", "auto_glz", "auto_lz", "quic", "glz", "lz", "lz4"
+ **mode**  
流模式。  
_必需_ ： 否  
_有效值_ : "filter", "all", "off"

设置虚拟机图形接口，需要虚拟机为关机状态。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  
<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"bdc01c45-973c-4b7b-a565-7a03c74379e4","compute_uuid":"941a6937-5e62-455d-a18e-2c1aab33b774","compute_name":"centos","tenant":"a0313629-10fd-48dc-9e92-5dff744a3c0e","compression":"glz","mode":"filter"}
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

### POST&nbsp; /v1/compute/bootorder/set
设置虚拟机启动顺序。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "device_order" : [ String ]
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是
+ **device_order**  
设置启动顺序数组。每个设备用特定标识表示，按数组顺序表示启动顺序。未被指定启动顺序的设备，将会以特定顺序排在指定设置后。
磁盘用盘符标识，网卡用小写mac地址标识，usb设备用带地址和端口的字符串如"usb1-1"标识。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"e1170fde-f0fe-4f91-a568-ac4b84f00aad","compute_uuid":"bcc79314-4bf5-433a-9edc-d2b397614cf1","compute_name":"Redhat7-64(converter)-clone","device_order":["hda","hdd","fda","vda","sda","sdb","52:56:ff:d7:12:54","52:56:ff:ed:e7:72","usb2-4"]}
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

### POST&nbsp; /v1/compute/meta/set
设置虚拟机。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier，
    "meta" : ComputeMeta,
    "kvm_clock_enable" : Bool,
    "virt_nested_enable" : Bool,
    "memory_huge_pages_enable" : Bool,
    "expand_config" : ExpandConfig,
    "baseline" : String,
    "data_localization_mode" : String,
    "object_group" : String,
    "os" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是
+ **meta**  
虚拟机基本设置。见[ComputeMeta](#computemeta)。  
里面不做修改的字段，需要请求中不指定。  
_必需_ ： 否  
    - 修改操作系统标识，如果和原系统不是同类型，虚拟机要求为关机状态。
    - 开启双活要求集群有资源池授权，虚拟机不能使用共享磁盘。
    - meta.video字段中，显存相关设置不支持在该接口修改。  
+ **kvm_clock_enable**  
是否开启kvm时钟。  
_必需_ ： 否
+ **virt_nested_enable**  
是否开启嵌套虚拟化。  
_必需_ ： 否
+ **memory_huge_pages_enable**  
是否开启内存巨页。  
_必需_ ： 否
+ **expand_config**  
CPU、内存自动扩容设置。  
_必需_ ： 否
+ **baseline**  
设置虚拟机基准类型要求。  
_必需_ ： 否
+ **data_localization_mode**  
设置虚拟机数据本地化。  
_必需_ ： 否
+ **object_group**  
修改虚拟机分组。参数指定虚拟机分组uuid。  
_必需_ ： 否
+ **os**  
修改虚拟机操作系统标记。  
_必需_ ： 否

该接口允许同时修改多项设置。不同项可能有各自不同的修改条件。  
只修改部分项时，其他项参数要求不指定，否则认为是明确的设置操作。  

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  
<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","compute_uuid":"433ceb3f-6409-4879-949d-2aa2a3543889","compute_name":"test-api","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","meta":{"compute_name":"test-api2"}}
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

### POST&nbsp; /v1/compute/disk/attach
虚拟机添加磁盘。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "target_device" : String,
    "target_bus" : String,
    "source_volume" : DiskVolumeSource,
    "source_vsd" : DiskVsdSource,
    "disk_block_source" : DiskBlockSource,
    "disk_source_passthrough" : DiskPassthroughSource,
    "disk_cache_mode" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是
+ **target_device**  
指定磁盘盘符。  
_必需_ ： 否  
_有效值_ : "id[a-c]", "sd[a-o]", "vd[a-o]"  
指定的盘符，作为磁盘的唯一标识，需要未被使用。指定了盘符的同时，相当于指定了对应的`target_bus`。  
若未指定`target_device`，会自动根据`target_bus`分配一个盘符。如果`target_bus`不合法，或超过分配数量，接口将报错。  
+ **target_bus**  
指定磁盘驱动。  
_必需_ ： 否  
_有效值_ : "ide", "scsi", "virtio", "sata"  
+ **source_volume**  
共享存储类型磁盘源。见[DiskVolumeSource](#diskvolumesource)。  
_必需_ ： 否  
使用共享存储卷作为虚拟机磁盘。
+  **source_vsd**  
内置存储类型磁盘源。见[DiskVsdSource](#diskvsdsource)。  
_必需_ ： 否  
使用内置存储卷作为虚拟机磁盘。
+ **disk_block_source**  
内置存储块设备类型磁盘源。见[DiskBlockSource](#diskblocksource)。  
_必需_ ： 否  
使用内置存储块设备类型卷作为虚拟机磁盘。
+ **disk_source_passthrough**  
透传磁盘类型磁盘源。见[DiskPassthroughSource](#diskpassthroughsource)。  
_必需_ ： 否  
使用宿主机透传磁盘作为虚拟机磁盘。
+ **disk_cache_mode**  
磁盘缓存模式。  
_必需_ ： 否  
_有效值_ : "", "none", "default", "writeback", "writethrough"
设置磁盘缓存模式。指定"writeback", "writethrough"，并且"target_bus"为"scsi"时，会强制将"target_bus"转化为"virtio"，以使磁盘缓存生效。

尽管大部分参数非必需，`target_device`和`target_bus`二者至少要指定一个，而全部source参数必须且最多指定一个。  
全部source参数需要指定已存在的磁盘源，该接口不负责存储卷的创建。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  
<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"433ceb3f-6409-4879-949d-2aa2a3543889","compute_name":"test-api2","target_bus":"virtio","source_vsd":{"volume_uuid":"201c17d0-29ba-4efb-a924-060dfddeba59","redundancy":1},"disk_cache_mode":"none"}
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

### POST&nbsp; /v1/compute/disk/update
修改虚拟机磁盘配置。

```
{
    ComputeIdentifier,
    "old_disk" : Disk,
    "new_disk" : Disk
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **old_disk**  
指定待修改的虚拟机磁盘。见[Disk](#disk)。只使用`old_disk.disk_target_device`字段指定磁盘。  
_必需_ ： `old_disk.disk_target_device`  
+ **new_disk**  
修改后的磁盘参数。见[Disk](#disk)。  
_必需_ ： 是  
不做修改的字段不做传参。  
允许导致磁盘唯一标识`target_device`改变的修改。要求`target_device`未被占用，或`target_bus`存在可分配盘符。  
运行对磁盘源做修改。修改后，相关存储卷的虚拟机标记会对应改变。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  
<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"433ceb3f-6409-4879-949d-2aa2a3543889","compute_name":"test-api2","old_disk":{"disk_target_device":"sda"},"new_disk":{"disk_target_bus":"virtio"}}
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

### POST&nbsp; /v1/compute/disk/export 
虚拟机磁盘导出镜像。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "disk" : [ ComputeExportDisk ],
    "compress" : Bool
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **disk**  
磁盘导出相关参数。见[ComputeExportDisk](#computeexportdisk)  
_必需_ ： 是  
目前只支持单磁盘导出。 
+ **compress**  
是否压缩。  
_必需_ ： 否  

导出支持iscsi类型内置存储卷磁盘和共享存储卷磁盘。不支持块设备类型内置存储卷磁盘和透传磁盘。  
该接口运行在虚拟机运行状态下发起磁盘导出，不影响虚拟机数据读写。  

<a id="computeexportdisk"></a>
**ComputeExportDisk**  
```
{
    "image_name" : String,
    "image_type" : String,
    "device" : String,
    "snapshot_uuid" : String,
    "repository_uuid" : String
}
```

+ **image_name**  
磁盘导出镜像文件名。需要带后缀。  
_必需_ ： 是  
+ **image_type**  
导出镜像格式。  
_必需_ ： 是  
_有效值_ : "raw", "qcow2", "qed", "vdi", "vpc", "vmdk"
+ **device**  
磁盘盘符。指定导出磁盘。
_必需_ ： 是  
+ **snapshot_uuid**  
导出用磁盘快照uuid。  
_必需_ ： 否  
若不指定磁盘快照，则导出前会创建一个临时快照，并在导出后自动清除。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：
```
"data" : {
    "name" : String
}
```

+ **name**  
操作的虚拟机名称。

该接口要求磁盘存储卷可以创建新挂载点用于导出操作读取数据，且不能和已有挂载点主机相同。若可用主机不足，则接口返回`"scode" : 22161`错误。
虚拟机镜像导出为异步操作，接口返回只代表导出操作成功发起，虚拟机进入导出中动作。要等待虚拟机异步导出完成，状态自动改变。

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"433ceb3f-6409-4879-949d-2aa2a3543889","compute_name":"test-api2","disk":[{"image_name":"test-export","image_type":"qcow2","device":"vdb","repository_uuid":"4bbcba69-8671-480c-8386-9190e80c30a6","snapshot_uuid":""}],"compress":false}
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
    "name": "test-api2"
  }
}
```

### GET&nbsp; /v1/compute/disk/export/progress
虚拟机导出进度查询接口。

<big>**请求参数**</big>  

名称 | 参数类型 | 是否必填 | 描述
---|---|---|---
 cluster_uuid|string|是| 集群uuid
 tenant|string|是| 租户uuid
 compute_uuid|string|是| 虚拟机uuid

该接口要求虚拟机为导出中状态。可以对应多种导出方式。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：
```
"data" : {
    "progress" : Number
}
```

+ **progress**  
当前导出进度。整型，0-100。    

导出没发起或者导出完成后，请求该接口会返回`"scode" : 22151`错误，表示非导出中。

<big>**示例**</big>  
**请求示例**  
```
http://10.30.33.25:8080/v1/compute/disk/export/progress?cluster_uuid=650ea11b-b7fb-4269-8232-aa53865aab3b&tenant=a5badacf-a25c-4171-9aff-b619fc2d300a&compute_uuid=433ceb3f-6409-4879-949d-2aa2a3543889
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
    "progress": 0
  }
}
```

### POST&nbsp; /v1/compute/disk/detach
虚拟机磁盘卸载。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "target_device" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **target_device**  
指定卸载磁盘的盘符。
_必需_ ： 是  

卸载指定的盘符要求是磁盘的，这个接口不支持卸载光驱和软驱。  
只有scsi驱动的磁盘可以热卸载，其他磁盘要求在关机状态操作。所有磁盘都要在无动作，不在导出中的情况下卸载。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","compute_uuid":"433ceb3f-6409-4879-949d-2aa2a3543889","compute_name":"test-api2","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","target_device":"vda"}
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

### POST&nbsp; /v1/compute/import
虚拟机磁盘镜像导入。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "target_device" : String,
    "image_name" : String,
    "repository_uuid" : String
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **target_device**  
指定导入磁盘盘符。  
_必需_ ： 是  
+ **image_name**  
导入镜像名。  
_必需_ ： 是  
+ **repository_uuid**  
导入镜像所在镜像仓库uuid。  
_必需_ ： 是  

磁盘导入要求虚拟机处于关机状态、无动作，不在导出中。  
磁盘镜像导入不支持导入到透传磁盘。  

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

虚拟机磁盘导入是异步操作。接口正常返回只代表操作正常发起，虚拟机进入导入中动作。需要等待磁盘导入完成，状态自动改变。

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"88de8e11-2f85-4608-91fe-0c832d88549a","compute_name":"test-api3","image_name":"v3.220042.0046_thci01_NGVONE.1_haveroot.qcow2","target_device":"sda","repository_uuid":"9783c45d-cdbf-48b3-a257-c6a779cf891a"}
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

### POST&nbsp; /v1/compute/iscsi_import
虚拟机磁盘iscsi源导入。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "target_device" : String,
    "src_ip" : String,
    "src_port" : String,
    "src_iqn" : String,
    "username" : String,
    "password" : String,
    "lun_id" : Number
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **target_device**  
指定导入磁盘盘符。  
_必需_ ： 是  
+ **src_ip**  
iscsi源导入主机ip。  
_必需_ ： 是  
+ **src_port**  
iscsi源导入端口。  
_必需_ ： 是 
+ **src_iqn**  
iscsi源导入iqn。  
_必需_ ： 是  
+ **username**  
iscsi源导入用户名。  
_必需_ ： 否  
+ **src_iqn**  
iscsi源导入password。  
_必需_ ： 否  
+ **lun_id**  
iscsi源导入LUN id。    
_必需_ ： 否  

磁盘导入要求虚拟机处于关机状态、无动作，不在导出中。  
该接口从一个给定的iscsi targert读取数据，并导入到虚拟机磁盘中。  
用iscsi target导入时，相关参数用于挂载target，需要根据实际target设置传参。  
不支持导入到块设备磁盘和透传磁盘。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

虚拟机磁盘导入是异步操作。接口正常返回只代表操作正常发起，虚拟机进入导入中动作。需要等待磁盘导入完成，状态自动改变。

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"88de8e11-2f85-4608-91fe-0c832d88549a","compute_name":"test-api3","target_device":"sda","src_ip":"10.30.16.131","src_port":"21811","src_iqn":"iqn.2018-11.topsec.com.cn:201c17d0-29ba-4efb-a924-060dfddeba59id2013085","username":"","password":"","lun_id":1}
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

### POST&nbsp; /v1/compute/import/progress
虚拟机导入进度查询。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  

该接口要求虚拟机为导入中动作。可以对应多种导出方式。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：
```
"data" : {
    "progress" : Number,
    "detail" : {
        String : String
    }
}
```

+ **progress**  
当前导出进度。整型，0-100。  
+ **detail**  
额外进度信息。

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"88de8e11-2f85-4608-91fe-0c832d88549a"}
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
    "progress": 0,
    "detail": null
  }
}
```

### POST&nbsp; /v1/compute/security_vm/import/progress
安全网元导入进度。

<big>**请求参数**</big>  
```
{
    "security_vm_import_process_inspect_request_info_list" : [ SecurityVmImportProcessInspectRequestInfo ]
}
```

**SecurityVmImportProcessInspectRequestInfo**
```
{
    CommonClusterTenantScope，
    "vm_uuid" : String,
    "vm_ip" : String,
    "vm_type" : Number
}
```

+ **CommonClusterTenantScope**  
指定集群。见[CommonClusterTenantScope](#commonclustertenantscope)  
_必需_ ： 是  
+ **vm_uuid**  
待查询导入进度的虚拟机uuid。 
_必需_ ： 是  
+ **vm_ip**  
网元设置IP。部分类型网元允许多个实例，需要用这个参数作为区分。  
_必需_ ： 否  
+ **vm_type**  
指定查询的网元类型。整型枚举。  
_必需_ ： 是  
_有效值_ : 0-13, 100

不需要`vm_ip`字段网元类型，包括`0(VSECCENTER)`，`11(LIC_SERVER)`，`13(NGTP)`。  
请求参数中，`vm_uuid`，`vm_ip`和`vm_type`必须匹配。否则无法查询到正常结果。
接口可以同时查询多个网元的导入进度。

<big>**返回数据**</big>  
接口返回数据先使用[BatchOutput](#batchoutput)封装，再用[Output](#output)封装。接口特定返回如下：
```
"data" : {
    "vm_ip" : String,
    "vm_type" : Number,
    "progress" : Number,
    "import_state" : Number
}
```

+ **vm_ip**  
传入的参数`vm_ip`。
+ **vm_type**  
传入的参数`vm_type`。
+ **progress**  
当前导出进度。整型，0-100。  
+ **import_state**  
当前导入状态。整型，0-2。
_有效值_ ： 0(无)，1(导入中)，2(导入成功)

<big>**示例**</big>  
**请求示例**  
```json
{"security_vm_import_process_inspect_request_info_list":[{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","vm_uuid":"88de8e11-2f85-4608-91fe-0c832d88549a","vm_ip":"192.168.0.10","vm_type":100}]}
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
            "vm_ip" : "192.168.0.10",
            "vm_type" : 100,
            "progress" : 0,
            "import_state" : 1
        }
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/import/resume
虚拟机恢复导入。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  

要求虚拟机处于导入中断的状态，即关机状态、导入中动作，有导入中断的标记。
目前只有迁入云服务器功能发起的导入有导入中断状态。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：
```
"data" : {
    "compute_name" : String
}
```

+ **compute_name**  
恢复导入的虚拟机的名称。

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"88de8e11-2f85-4608-91fe-0c832d88549a"}
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
    "compute_name" : "test"
  }
}
```

### POST&nbsp; /v1/compute/import/abort
虚拟机终止导入。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  

要求虚拟机处于导入中断的状态，即关机状态、导入中动作，有导入中断的标记。
目前只有迁入云服务器功能发起的导入有导入中断状态。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：
```
"data" : {
    "compute_name" : String
}
```

+ **compute_name**  
终止导入的虚拟机的名称。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"88de8e11-2f85-4608-91fe-0c832d88549a"}
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
    "compute_name" : "test"
  }
}
```

### POST&nbsp; /v1/compute/migrate/abort
虚拟机中断迁移。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  

该接口要求虚拟机为运行状态，迁移中动作。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"88de8e11-2f85-4608-91fe-0c832d88549a"}
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

### POST&nbsp; /v1/compute/migrate
虚拟机迁移。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier
    "destination" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **destination**  
迁移目的主机uuid。  
_必需_ ： 是  

虚拟机跨迁移是异步操作，接口正常返回只代表操作成功发起，虚拟机进入迁移状态。发起虚拟机迁移，要求虚拟机为运行状态，无动作。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：
```
"data" : {
    "compute_name" : String
}
```

需要等待实际虚拟机迁移完成，状态才会变回运行状态、无动作。

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","compute_uuid":"433ceb3f-6409-4879-949d-2aa2a3543889","compute_name":"test-api2","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","destination":"963b6fd4-487e-4436-95c4-21a67aca5eaf"}
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
    "compute_name": "test-api2"
  }
}
```

### POST&nbsp; /v1/compute/cross_cluster_migrate
虚拟机跨集群迁移。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "destination_cluster" : String,
    "destination_host_uuid" : String,
    "destination_host_ip" : String,
    "destination_tenant" : String,
    "pool_uuid" : String,
    "zone_uuid" : String,
    "object_group" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **destination_cluster**  
目的集群uuid。  
_必需_ ： 是  
+ **destination_host_uuid**  
目的主机uuid。  
_必需_ ： 是  
+ **destination_host_ip**  
目的主机IP。  
_必需_ ： 是  
+ **destination_tenant**  
目的集群租户。  
_必需_ ： 是  
+ **pool_uuid**  
卷目的存储池uuid。  
_必需_ ： 是  
+ **zone_uuid**  
目的资源池uuid。  
_必需_ ： 是  
+ **object_group**  
目的虚拟机分组。  
_必需_ ： 是  

虚拟机跨集群迁移会在目的集群创建对应存储卷、虚拟机，并热迁移运行数据到目的虚拟机。  
虚拟机跨集群迁移要求虚拟机为运行状态，无动作。
虚拟机运行主机要求能够正常连接`destination_host_ip`

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

虚拟机跨集群迁移是异步操作，接口正常返回只代表操作成功发起，虚拟机进入迁移状态。需要等待实际虚拟机迁移完成，状态才会变回运行状态、无动作。

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","compute_uuid":"433ceb3f-6409-4879-949d-2aa2a3543889","compute_name":"test-api2","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","destination_cluster":"c27a25bc-5da2-430f-bfaf-6c8d33f21128","destination_host_uuid":"200e3364-e720-47e4-8b12-734422d6eae3","destination_host_ip":"10.30.32.23","destination_tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","pool_uuid":"42b3e3b6-b1d1-44c0-bf5c-b9cf73d594df","zone_uuid":"2871bab9-d6ed-4100-8d74-9c4442b52bb5","object_group":"e9017aa7-e19b-47b0-b638-e639aa9451c6"}
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

### POST&nbsp; /v1/compute/cross_cluster_cancel
虚拟机取消跨集群迁移。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  

取消跨集群迁移会将当前迁移中的虚拟机取消迁移，恢复运行状态，并将创建出来的目的集群虚拟机和存储卷清除掉。
取消跨集群迁移要求虚拟机是迁移中动作。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","compute_uuid":"433ceb3f-6409-4879-949d-2aa2a3543889","compute_name":"test-api2","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a"}
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

### POST&nbsp; /v1/compute/cross_cluster_pregress
查询虚拟机跨集群迁移进度。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  

该接口要求虚拟机为运行状态，迁移中动作。
如果检查到迁移失败，该接口也会将目的端虚拟机和卷清理掉。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：
```
"data" : {
    "progress" : Number
}
```

+ **progress**  
当前导出进度。整型，0-100。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","compute_uuid":"433ceb3f-6409-4879-949d-2aa2a3543889","compute_name":"test-api2","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a"}
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
    "progress" : 0
  }
}
```

### POST&nbsp; /v1/compute/graphics/password/set
修改虚拟机图像接口密码。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "vnc_password" : String,
    "spice_password" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **vnc_password**  
修改VNC密码。密码为加密后的字符串。
+ **spice_password**  
修改spice密码。密码为加密后的字符串。

不做修改的项不作传参即可。
该接口允许热修改VNC密码和spice密码。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"433ceb3f-6409-4879-949d-2aa2a3543889","compute_name":"test-api2","spice_password":"106b6c5a91eb9b432e577b880b843978"}
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

### POST&nbsp; /v1/compute/interface/attach
虚拟机添加网卡。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    Interface
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **Interface**  
虚拟机网卡参数。见[Interface](#interface)。  
_必需_ ： 是  

该接口支持热添加虚拟机网卡。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：
```
"data" : {
    "interface_return" : Interface
}
```

+ **interface_return**  
返回添加网卡的部分信息。目前只返回MAC地址、网卡ID。
<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"88de8e11-2f85-4608-91fe-0c832d88549a","compute_name":"test-api3","zone":"a6f8ad4a-3fdf-4cf6-8fda-90a8093f5316","interface_model_type":"e1000","interface_type":"dsfwd","port_group":"439d8d6a-9a83-4884-a7d8-5a312d6495aa","port_group_name":"voi端口组","vlan_tag_ids":[200],"switch_uuid":"","switch_name":null,"gateway_uuid":"","gateway_name":null,"peer":"on","bound_ip":null,"mac_address":null,"out_bount":{"average":100,"peak":0,"burst":0},"in_bount":{"average":0,"peak":0,"burst":0}}
```
**返回示例**  
```json
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "name": "",
    "uuid": "",
    "interface_return": {
      "interface_model_type": "e1000",
      "mac_address": "52:56:ff:79:9b:27",
    }
  }
}
```

### POST&nbsp; /v1/compute/modify/network
更改虚拟机网卡网络。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    Interface
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **Interface**  
虚拟机网卡参数。见[Interface](#interface)。  
_必需_ ： 是  

不支持更改VPC网络网卡，不支持更改网卡到VPC网络。  
接口允许更改本地网络、端口组、VLAN id。端口组的QOS会覆盖网卡QOS配置。  
该接口要求虚拟机处于关机状态，无动作、克隆中或导入中动作。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  
<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","compute_name":"test-api3","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"88de8e11-2f85-4608-91fe-0c832d88549a","mac_address":"52:56:ff:79:9b:27","interface_type":"dsfwd","port_group":"439d8d6a-9a83-4884-a7d8-5a312d6495aa","vlan_tag_ids":[200]}
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
    "name": "",
    "uuid": "",
    "interface_return": {
    }
  }
}
```

### POST&nbsp; /v1/compute/interface/detach
虚拟机网卡卸载。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "mac_address" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **mac_address**  
指定要卸载的网卡MAC地址。  
_必需_ ： 是  

该接口要求虚拟机无动作，可以是关机状态或运行状态。
卸载网卡后，网卡MAC地址被释放，可能被未来添加的网卡使用。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","compute_uuid":"88de8e11-2f85-4608-91fe-0c832d88549a","compute_name":"test-api3","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","mac_address":"52:56:ff:79:9b:27"}
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

### POST&nbsp; /v1/compute/interface/setqos
虚拟机设置网卡QOS。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    Interface
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **Interface**  
虚拟机网卡参数。见[Interface](#interface)。只需要指定`in_bount`或`out_bount`。  
_必需_ ： 是  

该接口允许关机状态或运行状态修改。热修改立刻生效。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"88de8e11-2f85-4608-91fe-0c832d88549a","compute_name":"test-api3","mac_address":"52:56:ff:a4:4d:ac","in_bount":{"average":0,"peak":0,"burst":0},"out_bount":{"average":100,"peak":0,"burst":0}}
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

### POST&nbsp; /v1/compute/pci/attach
虚拟机添加透传PCI设备。

<big>**请求参数**</big>  
```
{    
    ComputeIdentifier,
    "pci_device" : PCIDevice
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **pci_device**  
指定PCI设备。见[PCIDevice](#pcidevice)。  
_必需_ ： 是  

该接口要求虚拟机为运行状态。不允许关机状态操作。  
只能添加虚拟机当前运行主机上的PCI设备。该设备还需支持设备透传至虚拟机。  
添加PCI设备后，虚拟机会被限制只能在对应宿主机运行。  
因为宿主机限制，使用PCI设备和虚拟机启用HA互斥。  

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"88de8e11-2f85-4608-91fe-0c832d88549a","compute_name":"test-api3","pci_device":{"Domain":0,"Bus":0,"Slot":0,"Function":0}}
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

### POST&nbsp; /v1/compute/pci/detach
虚拟机卸载透传PCI设备。

<big>**请求参数**</big>  
```
{    
    ComputeIdentifier,
    "pci_device" : PCIDevice
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **pci_device**  
指定PCI设备。见[PCIDevice](#pcidevice)。  
_必需_ ： 是  

该接口允许关机状态下卸载，也允许运行状态下热拔PCI设备。  
设备卸载后，若没有其他透传设备，虚拟机将不再限制在对应主机运行。  
因为宿主机限制，使用PCI设备和虚拟机启用HA互斥。  

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"88de8e11-2f85-4608-91fe-0c832d88549a","compute_name":"test-api3","pci_device":{"Domain":0,"Bus":0,"Slot":0,"Function":0}}
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

### POST&nbsp; /v1/compute/mdev/attach
虚拟机添加透传Mdev设备。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "mdev_device" : MdevDevice
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **mdev_device**  
Mdev参数。见[MdevDevice](#mdevdevice)。

添加Mdev设备要求虚拟机为运行中状态。  
因为是宿主机透传设备，添加Mdev设备后虚拟机会被限制在对应主机上运行。  
因为宿主机限制，使用PCI设备和虚拟机启用HA互斥。  

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"88de8e11-2f85-4608-91fe-0c832d88549a","compute_name":"test-api3","mdev_device":{"src_address_uuid":"f5b85eec-8499-48cc-87d7-9d80ff6743a2","model":"vfio-pci","display":"off"}}
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

### POST&nbsp; /v1/compute/mdev/detach
虚拟机卸载透传Mdev设备。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "mdev_device" : MdevDevice
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **mdev_device**  
Mdev参数。见[MdevDevice](#mdevdevice)。只需要指定uuid。

卸载Mdev设备允许虚拟机为关机状态或开机状态。  
若卸载后虚拟机不再有透传设备，虚拟机将不再被限制在对应主机上运行。 

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"88de8e11-2f85-4608-91fe-0c832d88549a","compute_name":"test-api3","mdev_device":{"src_address_uuid":"f5b85eec-8499-48cc-87d7-9d80ff6743a2"}}
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

### POST&nbsp; /v1/compute/ip_mac_bind/update
虚拟机网卡绑定MAC地址和IP地址。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    Interface
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **Interface**  
虚拟机网卡参数。见[Interface](#interface)。
_必需_ ： 是  
需要的传参为`interface_id`, `mac_address`, `bound_ip`, `peer`。
  - 当`peer=""`时，不修改网卡MAC地址和IP地址绑定的关系。
  - 当`peer="mac"`时，修改网卡MAC地址和IP地址为绑定关系。
  - 当`peer!=""且peer!="mac"`时，修改网卡MAC地址和IP地址为不绑定关系。

该接口允许中虚拟机关机状态或运作状态发起。
该接口允许修改网卡MAC地址。此时虚拟机要求为关机状态。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"88de8e11-2f85-4608-91fe-0c832d88549a","compute_name":"test-api3","interface_id":"578521a6-532c-4283-a868-2cd7a791fb83","mac_address":"52:56:ff:79:9b:27","bound_ip":"10.11.12.13","peer":"mac"}
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

### GET&nbsp; /v1/compute/cloud_init/get
获取虚拟机初始化配置参数。

<big>**请求参数**</big>  

名称 | 参数类型 | 是否必填 | 描述
---|---|---|---
 cluster_uuid|string|是| 集群uuid
 tenant|string|是| 租户uuid
 compute_uuid|string|是| 虚拟机uuid

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
    "cloud_init_data" : CloudInitData
}
```

+ **cloud_init_data**  
初始化配置参数。见[CloudInitData](#cloudinitdata)。

<big>**示例**</big>  
**请求示例**  
```
http://10.30.12.150:8080/v1/compute/cloud_init/get?cluster_uuid=bdc01c45-973c-4b7b-a565-7a03c74379e4&tenant=a0313629-10fd-48dc-9e92-5dff744a3c0e&compute_uuid=66e88b84-e414-4ce6-b397-8c94bc63f318
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
    "cloud_init_data": {
      "meta_data": {
        "hostname": "hostname-1",
        "name": "hostname-1",
        "uuid": "66e88b84-e414-4ce6-b397-8c94bc63f318",
        "public_keys": {
          "key": ""
        }
      },
      "network_data": {
        "links": [
          {
            "ethernet_mac_address": "52:56:ff:82:5c:be",
            "id": "66d5b23e-0827-445d-9693-93511ce51496",
            "mtu": 1500,
            "type": "ovs"
          }
        ],
        "networks": [
          {
            "link": "66d5b23e-0827-445d-9693-93511ce51496",
            "type": "ipv4",
            "ip_address": "10.30.12.48",
            "netmask": "255.255.255.0"
          }
        ],
        "services": [
          {
            "address": "114.114.114.114",
            "type": "dns"
          }
        ]
      },
      "user_data": {
        "set_passwd": {
          "ssh_pwauth": {
            "value": true
          },
          "chpasswd": {
            "expire": {
              "value": true
            },
            "list": [
              "root:TopHCS@6666"
            ]
          }
        },
        "time_zone": {
          "timezone": "Asia/Shanghai"
        },
        "ssh": {
          "disable_root": {}
        },
        "users": {},
        "runcmd": {},
        "growpart": {
          "mode": "off"
        }
      }
    }
  }
}
```

### POST&nbsp; /v1/compute/cloud_init/set
设置虚拟机初始化配置。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "cloud_init_data" : CloudInitData
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **cloud_init_data**  
初始化配置参数。见[CloudInitData](#cloudinitdata)。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{
    "cluster_uuid": "bdc01c45-973c-4b7b-a565-7a03c74379e4",
    "tenant": "a0313629-10fd-48dc-9e92-5dff744a3c0e",
    "compute_uuid": "66e88b84-e414-4ce6-b397-8c94bc63f318",
    "cloud_init_data": {
        "meta_data": {
            "hostname": "hostname-1",
            "name": "hostname-1",
            "uuid": "66e88b84-e414-4ce6-b397-8c94bc63f318",
            "public_keys": {
                "key": ""
            }
        },
        "network_data": {
            "links": [
                {
                    "ethernet_mac_address": "52:56:ff:82:5c:be",
                    "id": "66d5b23e-0827-445d-9693-93511ce51496",
                    "mtu": 1500,
                    "type": "ovs"
                }
            ],
            "networks": [
                {
                    "link": "66d5b23e-0827-445d-9693-93511ce51496",
                    "type": "ipv4",
                    "ip_address": "10.30.12.48",
                    "netmask": "255.255.255.0"
                }
            ],
            "services": [
                {
                    "address": "114.114.114.114",
                    "type": "dns"
                }
            ]
        },
        "user_data": {
            "set_passwd": {
                "ssh_pwauth": {
                    "value": true
                },
                "chpasswd": {
                    "expire": {
                        "value": true
                    },
                    "list": [
                        "root:TopHCS@6666"
                    ]
                }
            },
            "time_zone": {
                "timezone": "Asia/Shanghai"
            },
            "ssh": {
                "disable_root": {}
            },
            "users": {},
            "runcmd": {},
            "growpart": {
                "mode": "off"
            }
        }
    }
}
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

### POST&nbsp; /v1/compute/clone/progress
查询虚拟机克隆进度。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  

该接口要求虚拟机处于克隆中动作。否则，接口返回报错`scode : 22102`。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
    "progress" : Number
}
```

+ **progress**  
克隆进度，0-100。

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"88de8e11-2f85-4608-91fe-0c832d88549a"}
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
    "progress" : 0
  }
}
```

### POST&nbsp; /v1/compute/clone
虚拟机克隆。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    CloneTypeParam,
    "clone_name" : String,
    "migrate_namespace" : String,
    "disks" : [ CloneVsdDisk ],
    "clone_num" : Number,
    "object_group" : String,
    "zone" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **CloneTypeParam**  
克隆参数。见[CloneTypeParam](#clonetypeparam)。  
_必需_ ： 否  
+ **clone_name**  
克隆后的虚拟机名称。如果`clone_num > 1`，则名称会添加序号后缀。  
_必需_ ： 是  
+ **migrate_namespace**  
跨租户克隆的目的租户。  
_必需_ ： 否  
+ **disks**  
指定每个磁盘克隆的参数。  
_必需_ ： 否  
+ **clone_num**  
克隆数量。  
_必需_ ： 否  
+ **object_group**  
克隆后的虚拟机分组。  
_必需_ ： 否  
+ **zone**  
克隆后的资源池。  
_必需_ ： 否  

**CloneVsdDisk** 
```
{
    "source_pool_uuid" : String,
    "target_device" : String
}
```

+ **source_pool_uuid**  
指定磁盘克隆目的存储池。  
_必需_ ： 是  
+ **target_device**  
指定该参数对应磁盘盘符。  
_必需_ ： 是  

<big>**返回数据**</big>  
接口返回数据先使用[BatchOutput](#batchoutput)封装，再用[Output](#output)封装。接口特定返回如下：
```
"data" : {
    "tenant" : String,
    "vm_uuid" : String,
    "index" : Number,
    "clone_name" : String
}
```

+ **tenant**  
空。
+ **vm_uuid**  
克隆源虚拟机uuid。  
+ **index**  
批量克隆虚拟机序号。
+ **clone_name**  
克隆后的虚拟机名称。

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_name":"test-api4","object_group":"0a5d3331-d9fe-4f6a-9c90-879dde781794","link":false,"snapshot":"","compute_uuid":"25c77828-9309-412b-be4a-74c05237f3f0","clone_name":"test-api4-clone-0907103108","zone":"a6f8ad4a-3fdf-4cf6-8fda-90a8093f5316"}
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
          "tenant": "",
          "vm_uuid": "25c77828-9309-412b-be4a-74c05237f3f0",
          "index": 0,
          "clone_name": "test-api4-clone-0907103108"
        }
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/backup/restore/progress
虚拟机备份恢复进度。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
    "progress" : Number 
}
```

+ **progress**  
恢复进度。整型，0-100。

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"25c77828-9309-412b-be4a-74c05237f3f0"}
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
    "progress" : 0
  }
}
```

### POST&nbsp; /v1/compute/assign
虚拟机分配用户。

<big>**请求参数**</big>  
```
{
    TenantIdentifier,
    "user_uuid" : String,
    "vms" : [ ComputeIdentifier ]
}
```

+ **TenantIdentifier**  
指定分配用户所在租户。用于查询用户。
+ **user_uuid**  
指定分配用户uuid。
+ **vms**  
指定待分配虚拟机。见[ComputeIdentifier](#computeidentifier)。需要指定集群、租户、虚拟机uuid。

<big>**返回数据**</big>  
接口返回数据先使用[BatchOutput](#batchoutput)封装，再用[Output](#output)封装。接口特定返回如下：
```
"data" : {
    ComputeIdentifier
}
```

+ **ComputeIdentifier**  
表明操作各台虚拟机。和请求参数相同。

<big>**示例**</big>  
**请求示例**  
```json
{"tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","vms":[{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"88de8e11-2f85-4608-91fe-0c832d88549a","compute_name":"test-api3","owner":"063cca58-980f-46cc-b637-8e762d1f8c59"}],"user_uuid":"063cca58-980f-46cc-b637-8e762d1f8c59"}
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
          "cluster_uuid": "650ea11b-b7fb-4269-8232-aa53865aab3b",
          "tenant": "a5badacf-a25c-4171-9aff-b619fc2d300a",
          "compute_uuid": "88de8e11-2f85-4608-91fe-0c832d88549a",
          "compute_name": "test-api3",
          "owner": "063cca58-980f-46cc-b637-8e762d1f8c59"
        }
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/unassign
虚拟机取消分配用户。

<big>**请求参数**</big>  
```
{
    "vms" : [ ComputeIdentifier ]
}
```

+ **vms**  
指定待取消分配虚拟机。见[ComputeIdentifier](#computeidentifier)。需要指定集群、租户、虚拟机uuid。

<big>**返回数据**</big>  
接口返回数据先使用[BatchOutput](#batchoutput)封装，再用[Output](#output)封装。接口特定返回如下：
```
"data" : {
    ComputeIdentifier
}
```

+ **ComputeIdentifier**  
表明操作各台虚拟机。和请求参数相同。

<big>**示例**</big>  
**请求示例**  
```json
{"vms":[{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"88de8e11-2f85-4608-91fe-0c832d88549a","compute_name":"test-api3","owner":""}]}
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
          "cluster_uuid": "650ea11b-b7fb-4269-8232-aa53865aab3b",
          "tenant": "a5badacf-a25c-4171-9aff-b619fc2d300a",
          "compute_uuid": "88de8e11-2f85-4608-91fe-0c832d88549a",
          "compute_name": "test-api3"
        }
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/set/vdc_agent
虚拟机设置云桌面终端。

<big>**请求参数**</big>  
```
{
    "vms" : [ ComputeSetVdcAgent ]
}
```

+ **vms**  
指定每台虚拟机的设置终端参数。  
_必需_ ： 是  

**ComputeSetVdcAgent**  
```
{
    ComputeIdentifier,
    "vdc_agent_list" : [ String ]
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **vdc_agent_list**  
终端列表。
_必需_ ： 否  

接口绑定、解绑终端的时候，会通知到对应终端。

<big>**返回数据**</big>  
接口返回数据先使用[BatchOutput](#batchoutput)封装，再用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
    ComputeSetVdcAgent
}
```

+ **ComputeSetVdcAgent**  
返回每项操作对应虚拟机。和请求参数值一样。

<big>**示例**</big>  
**请求示例**  
```json
{"vms":[{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"88de8e11-2f85-4608-91fe-0c832d88549a","compute_name":"test-api3","vdc_agent_list":["063cca58-980f-46cc-b637-8e762d1f8c59"]}]}
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
          "cluster_uuid": "650ea11b-b7fb-4269-8232-aa53865aab3b",
          "tenant": "a5badacf-a25c-4171-9aff-b619fc2d300a",
          "compute_uuid": "88de8e11-2f85-4608-91fe-0c832d88549a",
          "compute_name": "test-api3",
          "vdc_agent_list": [
            "063cca58-980f-46cc-b637-8e762d1f8c59"
          ]
        }
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/screenshot
虚拟机屏幕截图。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  

使用屏幕截图功能，首先要在对应租户中开启屏幕截图空间。  
该接口要求虚拟机为运行状态。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
    "screenshot_url" : String
}
```

+ **screenshot_url**  
创建的屏幕截图url。

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"c27a25bc-5da2-430f-bfaf-6c8d33f21128","tenant":"efbc5f81-3c57-4dbb-8850-3d2ce7ea56b8","compute_name":"centos-yume","compute_uuid":"93960a06-2b54-4649-ac9b-3dad81a7abf8"}
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
    "screenshot_url": "http://10.30.32.23:28000/164b0f54-c04c-450f-bf63-cbe4cf53f052/data/93960a06-2b54-4649-ac9b-3dad81a7abf8/detail/detail.png"
  }
}
```

### GET&nbsp; /v1/compute/list/screenshot
<big>**请求参数**</big>  

名称 | 参数类型 | 是否必填 | 描述
---|---|---|---
 cluster_uuid|string|是| 集群uuid
 tenant|string|是| 租户uuid
 compute_uuid|string|是| 虚拟机uuid

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
    "screenshot_urls" : [ String ]
}
```

+ **screenshot_urls**  
虚拟机所有的崩溃时保存的屏幕截图的url。 

<big>**示例**</big>  
**请求示例**  
```
http://10.30.33.25:8080/v1/compute/list/screenshot?cluster_uuid=c27a25bc-5da2-430f-bfaf-6c8d33f21128&tenant=efbc5f81-3c57-4dbb-8850-3d2ce7ea56b8&compute_name=centos-yume&compute_uuid=93960a06-2b54-4649-ac9b-3dad81a7abf8
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
    "final_screenshots": null
  }
}
```

### POST&nbsp; /v1/compute/volume/related/set
虚拟机设置集群双活。

<big>**请求参数**</big>  
```
{
    "infos" : [ ComputeSetVolumeRelatedRequest ]
}
```

+ **infos**  
批量设置虚拟机双活。每个虚拟机一个参数。

**ComputeSetVolumeRelatedRequest**  
```
{
    ComputeIdentifier,
    "recover_to_related_zones" : Number,
    "master_zone_take_over" : Number
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **recover_to_related_zones**  
是否开启集群双活。  
_有效值_ ： 1(开启), 2(关闭), 0(不修改)  
+ **master_zone_take_over**  
是否开启主集群接管。要触发需要开启双活。   
_有效值_ ： 1(开启), 2(关闭), 0(不修改)  

开启虚拟机集群双活要求集群授权允许，并且虚拟机只使用内置存储磁盘。  
关闭虚拟机集群双活要求虚拟机处于关机状态。  
开启虚拟机主集群接管，要求虚拟机开启集群双活。  

<big>**返回数据**</big>  
接口返回数据先使用[BatchOutput](#batchoutput)封装，再用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
    ComputeIdentifier
}
```

+ **ComputeIdentifier**  
展示操作的虚拟机。只展示`tenant`, `compute_uuid`, `compute_name`字段。

<big>**示例**</big>  
**请求示例**  
```json
{"infos":[{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"88de8e11-2f85-4608-91fe-0c832d88549a","compute_name":"test-api3","recover_to_related_zones":1,"master_zone_take_over":"0"}]}
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
          "tenant": "a5badacf-a25c-4171-9aff-b619fc2d300a",
          "compute_uuid": "88de8e11-2f85-4608-91fe-0c832d88549a",
          "compute_name": "test-api3"
        }
      }
    ]
  }
}
```

### GET&nbsp; /v1/compute/convert/host/info
获取迁入云服务器信息。

<big>**请求参数**</big>  


名称 | 参数类型 | 是否必填 | 描述
---|---|---|---
cluster_uuid|String|是| 查询发起的集群
convert_addr|String|是| 主机converter服务地址

待迁入云服务器需要运行converter服务，默认端口为6666。  
目的集群和待迁入云服务器要求网络能连通。  

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
    "HostInfo" : HostInfoResponse
}
```

+ **HostInfo**  
converter返回的云服务器信息。  

<big>**示例**</big>  
**请求示例**  
```
http://10.30.33.25:8080/v1/compute/convert/host/info?convert_addr=10.30.12.150:6666&cluster_uuid=650ea11b-b7fb-4269-8232-aa53865aab3b
```
**返回示例**  
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "HostInfo": {
      "status": {
        "code": 0,
        "message": "",
        "messageCn": "",
        "stack": null,
        "desc": "",
        "UUID": ""
      },
      "OS": "linux",
      "Platform": "ubuntu",
      "PlatformFamily": "debian",
      "PlatformVersion": "16.04",
      "KernelVersion": "4.14.254",
      "Cores": 4,
      "Sockets": 2,
      "MemTotal": 6249652224,
      "DiskList": [
        {
          "Path": "/dev/vda",
          "Type": "HDD",
          "Size": 53687091200
        },
        {
          "Path": "/dev/vdb",
          "Type": "HDD",
          "Size": 1073741824
        }
      ]
    }
  }
}
```

### POST&nbsp; /v1/compute/unified/convert/host
迁入云服务器。

<big>**请求参数**</big>  
```
{
    CreateUnifiedRequest,
    "image_params" : ImageParams_UnifiedConvertHost
}
```

+ **CreateUnifiedRequest**  
完整虚拟机创建参数。见[/v1/compute/unified_create](#post-v1computeunified_create)。  
_必需_ ： 是  
+ **image_params**  
云服务器converter相关参数。
_必需_ ： 是  

**ImageParams_UnifiedConvertHost**
```
{
    "converter_ip" : String,
    "converter_port" : String,
    "compress" : Bool,
    "key" : String
}
```

+ **converter_ip**  
云服务器converter服务IP。  
_必需_ ： 是  
+ **converter_port**  
云服务器converter服务端口。  
_必需_ ： 是  
+ **compress**  
converter传输数据时是否压缩数据。  
_必需_ ： 否  
+ **key**  
converter传输数据时加密用密钥。不指定时不启用加密。  
_必需_ ： 否  

该接口按照给定配置创建卷和虚拟机，并且对虚拟机发起导入，将云服务器数据导入至虚拟机磁盘中。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
完整虚拟机创建返回。见[/v1/compute/unified_create](#post-v1computeunified_create)。  

云服务器迁入是异步操作，接口正常返回仅代表操作正常发起，虚拟机被创建并进入导入中动作。需要等待后台操作完成，虚拟机才会恢复状态。  
如果导入发起失败，虚拟机会被保留，允许手动后续数据导入。

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","object_group":"0a5d3331-d9fe-4f6a-9c90-879dde781794","zone":"a6f8ad4a-3fdf-4cf6-8fda-90a8093f5316","cpunr":4,"cpu_sockets":2,"cpu_socket_cores":2,"baseline":"Haswell-noTSX-IBRS","max_cpu_nr":4,"mem_size":6442450944,"mem_max":274877906944,"type":"GUS","image_uuid":"","os":"CentOS x64","memory_huge_pages_enable":false,"image_params":{"converter_ip":"10.30.12.150","converter_port":"6666","compress":false,"key":""},"meta":{"compute_name":"test-host","ha_mode":"on","ha_config":{"priority":0},"os_loader_path":"BIOS","video":[{"model_type":"vga"}],"panic_model":"isa","vnc_enable":false,"mem_sec_enabled":false,"data_localization_mode_on":"off","virt_nested_enable":false,"recover_to_related_zones":2,"master_zone_take_over":2,"startup_setting":null},"interfaces":[{"interface_model_type":"virtio","interface_type":"dsfwd","port_group":"439d8d6a-9a83-4884-a7d8-5a312d6495aa","port_group_name":"voi端口组","vlan_tag_ids":[200],"in_bount":{"average":0,"peak":0,"burst":0},"out_bount":{"average":0,"peak":0,"burst":0},"switch_uuid":"","switch_name":""}],"disks":[{"disk_target_bus":"scsi","disk_cache_mode":"none","disk_unified_vsd":{"tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","pool_uuid":"30fcdfe5-5502-4c9d-a841-6f91a5803245","pool_name":"ycb1000","volume_name":"test-host-volume1","capacity":53687091200,"snap_capacity":161061273600,"attribute":{"replica":"1","DriveType":"HDD","VsdVendor":"LIBTARGET"}},"redundancy":1,"device":"/dev/vda"},{"disk_target_bus":"scsi","disk_cache_mode":"none","disk_unified_vsd":{"tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","pool_uuid":"30fcdfe5-5502-4c9d-a841-6f91a5803245","pool_name":"ycb1000","volume_name":"test-host-volume2","capacity":1073741824,"snap_capacity":3221225472,"attribute":{"replica":"1","DriveType":"HDD","VsdVendor":"LIBTARGET"}},"redundancy":1,"device":"/dev/vdb"}],"cdrom":{"name":"","repository_uuid":""},"floppy":{"name":"","repository_uuid":""},"create_num":1}
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
    "success": 1,
    "fail": 0,
    "results": [
      {
        "message": "success",
        "message_cn": "成功",
        "scode": 0,
        "desc": "",
        "stack": null,
        "data": {
          "tenant": "a5badacf-a25c-4171-9aff-b619fc2d300a",
          "vm_uuid": "",
          "index": 0,
          "vm_name": "",
          "volume_uuids": [],
          "mac_addresses": [],
          "group": "",
          "group_name": ""
        }
      }
    ]
  }
}
```

### GET&nbsp; /v1/compute/ova/info/inspect
查询ova文件信息。

<big>**请求参数**</big>  

 名称 | 参数类型 | 是否必填 | 描述
---|---|---|---
 cluster_uuid|string|是| 集群uuid
 tenant|string|是| 租户uuid
name|string|是| ova镜像文件名。从共享卷根目录开始的路径。
volume_type|string|否| rest共享卷类型，"vsd"(内置存储), "share"(共享存储)
volume_uuid|string|否| rest共享卷uuid
vsm_host_uuid|string|否| 宿主机存储介质源所在主机
ova_path|string|否| 宿主机存储介质源路径
repository_uuid|string|否| 镜像仓库uuid
format|string|是| 文件后缀。".ova", ".tva"

该接口支持多种ova文件源：  

+ **rest共享卷源**。指定参数`name`，`volume_type`，`volume_uuid`。要求卷已经挂载。支持内置存储共享卷，和共享存储共享卷。
+ **镜像仓库源**。指定参数`name`，`repository_uuid`。要求仓库路径可用。
+ **宿主机存储介质源**。指定参数`vsm_host_uuid`，`ova_path`。指定宿主机上特定路径的ova文件。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
    "domain" : Domain,
    "disks" : {
        "String" : DiskInfo
    },
    "ova_path" : String,
    "snapshot_name" : String
}
```

+ **domain**  
ova文件对应虚拟机配置。
+ **disks**  
ova文件记录虚拟机磁盘相关信息。磁盘文件路径为键，磁盘信息为值。
+ **ova_path**  
ova文件对应宿主机文件路径。
+ **snapshot_name**  
如果是超融合集群导出的ova文件，导出时使用的快照的名称。

<big>**示例**</big>  
**请求示例**  
```
http://10.30.33.25:8080/v1/compute/ova/info/inspect?tenant_uuid=a5badacf-a25c-4171-9aff-b619fc2d300a&format=.tva&volume_uuid=ff43fd25-07d2-42f5-a8c5-02f2a1623b93&repository_uuid=c5c6e82d-e7ea-47bc-b422-f2d9c767b080&name=centos7x64&volume_type=vsd&cluster_uuid=650ea11b-b7fb-4269-8232-aa53865aab3b
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
    "domain": {
      "xml_name": null,
      "type": "",
      "ID": 0,
      "name": "GUSe7bc32d8-2899-489b-b1a4-9e7bd7fa55bc",
      "UUID": "e7bc32d8-2899-489b-b1a4-9e7bd7fa55bc",
      "gen_id": null,
      "title": "",
      "description": "",
      "metadata": {
        "xml": "CiQ3MDJiNTk5Ni0wMzQ3LTQwNjMtYTlmZi0yYjVhNmI2YzI3ZjYqDeWFqOmHj+Wkh+S7vTFAusaUhwZKNQoDaGRhEi4KJGI4YWZhYmIwLTkwMjAtNDMwNy1iYjRkLTFjYjU0ZTg2NGY0ZBCAgICAGBgC"
      },
      "maximum_memory": {
        "value": 268435456,
        "unit": "KiB",
        "slots": 0
      },
      "memory": {
        "value": 4194304,
        "unit": "KiB",
        "dump_core": ""
      },
      "current_memory": {
        "value": 4194304,
        "unit": "KiB"
      },
      "block_IO_tune": null,
      "memory_tune": null,
      "memory_backing": null,
      "VCPU": {
        "placement": "",
        "CPU_set": "",
        "current": "2",
        "value": 4
      },
      "VCPUs": null,
      "IO_threads": 0,
      "IO_threads_IDs": null,
      "CPU_tune": null,
      "NUMA_tune": null,
      "resource": null,
      "sys_info": null,
      "bootloader": "",
      "bootloader_args": "",
      "OS": {
        "type": {
          "arch": "",
          "machine": "",
          "type": "hvm"
        },
        "init": "",
        "init_args": null,
        "init_env": null,
        "init_dir": "",
        "init_user": "",
        "init_group": "",
        "loader": {
          "path": "BIOS",
          "readonly": "",
          "secure": "",
          "type": ""
        },
        "NV_ram": null,
        "kernel": "",
        "initrd": "",
        "cmdline": "",
        "DTB": "",
        "ACPI": null,
        "boot_devices": null,
        "boot_menu": null,
        "BIOS": null,
        "SM_bios": null,
        "Firmware": ""
      },
      "ID_map": null,
      "features": null,
      "CPU": {
        "XML_name": null,
        "match": "",
        "mode": "custom",
        "check": "",
        "model": {
          "fallback": "forbid",
          "value": "Haswell-noTSX-IBRS",
          "vendor_ID": ""
        },
        "vendor": "",
        "topology": {
          "sockets": 2,
          "cores": 2,
          "threads": 0
        },
        "cache": null,
        "features": [
          {
            "policy": "disable",
            "name": "vmx"
          }
        ],
        "numa": null
      },
      "clock": {
        "offset": "utc",
        "basis": "",
        "adjustment": "",
        "timezone": "",
        "timer": null
      },
      "on_power_off": "",
      "on_reboot": "",
      "on_crash": "",
      "PM": null,
      "perf": null,
      "devices": {
        "emulator": "",
        "disks": [
          {
            "XML_name": null,
            "device": "disk",
            "raw_IO": "",
            "SGIO": "",
            "snapshot": "",
            "driver": null,
            "auth": null,
            "source": {
              "file": null,
              "block": null,
              "dir": null,
              "network": {
                "protocol": "vsd",
                "name": "",
                "TLS": "",
                "hosts": null,
                "initiator": null,
                "snapshot": null,
                "config": {
                  "file": "",
                  "redundancy": 0
                },
                "auth": null,
                "Query": ""
              },
              "volume": null,
              "startup_policy": "",
              "index": 0,
              "encryption": null,
              "reservations": null,
              "NVME": null,
              "Slices": null,
              "SSL": null,
              "Cookies": null,
              "Readahead": null,
              "Timeout": null
            },
            "backing_store": {
              "index": 0,
              "format": null,
              "source": {
                "file": {
                  "file": "/exports/ff43fd25-07d2-42f5-a8c5-02f2a1623b93/.tms.rest/centos7x64.tva/centos7x64-disk1.qcow2",
                  "sec_label": null
                },
                "block": null,
                "dir": null,
                "network": null,
                "volume": null,
                "startup_policy": "",
                "index": 0,
                "encryption": null,
                "reservations": null,
                "NVME": null,
                "Slices": null,
                "SSL": null,
                "Cookies": null,
                "Readahead": null,
                "Timeout": null
              },
              "backing_store": null
            },
            "geometry": null,
            "block_IO": null,
            "mirror": null,
            "target": null,
            "IO_tune": null,
            "read_only": null,
            "shareable": null,
            "transient": null,
            "Serial": "",
            "WWN": "",
            "vendor": "",
            "product": "",
            "encryption": null,
            "boot": null,
            "alias": null,
            "address": null,
            "Model": "",
            "DiskPool": "",
            "IsSystem": false
          }
        ],
        "controllers": null,
        "leases": null,
        "filesystems": null,
        "interfaces": [
          {
            "XML_name": null,
            "managed": "",
            "trust_guest_RX_filter": "",
            "MAC": {
              "address": "52:56:ff:bb:b2:d8"
            },
            "source": {
              "user": null,
              "ethernet": null,
              "v_host_user": null,
              "server": null,
              "client": null,
              "m_cast": null,
              "network": {
                "network": "manage",
                "port_group": "24f042d5-4000-4acd-9f90-33ac2d67ff54"
              },
              "bridge": null,
              "internal": null,
              "direct": null,
              "hostdev": null,
              "UDP": null
            },
            "boot": null,
            "vLan": null,
            "virtual_port": {
              "params": {
                "Any": null,
                "VEPA_8021_qbg": null,
                "VN_tag_8021_qbh": null,
                "open_v_switch": {
                  "interface_ID": "7410a608-5408-45ec-8c23-aa146fd3be53",
                  "profile_ID": ""
                },
                "mido_net": null
              }
            },
            "ip": [
              {
                "address": "10.30.44.207",
                "family": "ipv4",
                "prefix": 20,
                "peer": "",
                "name": "eth0"
              }
            ],
            "route": null,
            "script": null,
            "target": null,
            "guest": null,
            "model": {
              "type": "virtio"
            },
            "driver": null,
            "backend": null,
            "filter_ref": null,
            "tune": null,
            "link": null,
            "MTU": null,
            "Bandwidth": null,
            "coalesce": null,
            "ROM": null,
            "alias": null,
            "address": null,
            "Teaming": null,
            "PortOptions": null
          }
        ],
        "smartcards": null,
        "serials": null,
        "parallels": null,
        "consoles": null,
        "channels": null,
        "inputs": null,
        "TPMs": null,
        "graphics": [
          {
            "XML_name": null,
            "SDL": null,
            "VNC": null,
            "RDP": null,
            "desktop": null,
            "spice": {
              "port": 5904,
              "TLS_port": 0,
              "auto_port": "yes",
              "listen": "::0.0.0.0",
              "keymap": "",
              "default_mode": "",
              "passwd": "9e7bd7fa55bc",
              "passwd_valid_to": "",
              "connected": "",
              "listeners": null,
              "channel": null,
              "image": {
                "compression": "glz"
              },
              "JPEG": null,
              "z_lib": null,
              "playback": null,
              "streaming": {
                "mode": "filter"
              },
              "mouse": null,
              "clip_board": null,
              "file_transfer": null,
              "GL": null
            },
            "EGL_headless": null
          }
        ],
        "sounds": null,
        "videos": [
          {
            "XML_name": null,
            "model": {
              "type": "vga",
              "heads": 0,
              "ram": 131072,
              "v_ram": 0,
              "v_ram64": 0,
              "VGA_mem": 32768,
              "primary": "",
              "accel": null,
              "Resolution": null
            },
            "driver": null,
            "alias": null,
            "address": null
          }
        ],
        "hostdevs": null,
        "redir_devs": [
          {
            "XML_name": null,
            "bus": "usb",
            "source": {
              "null": null,
              "VC": null,
              "pty": null,
              "dev": null,
              "file": null,
              "pipe": null,
              "stdIO": null,
              "UDP": null,
              "TCP": null,
              "UNIX": null,
              "spice_VMC": {},
              "spice_port": null,
              "NMDM": null
            },
            "protocol": null,
            "boot": null,
            "alias": null,
            "address": {
              "PCI": null,
              "drive": null,
              "virtio_serial": null,
              "CCID": null,
              "USB": {
                "bus": 2,
                "port": "4",
                "device": 0
              },
              "spapr_VIO": null,
              "virtio_s390": null,
              "CCW": null,
              "virtio_mmio": null,
              "ISA": null,
              "DIMM": null,
              "Unassigned": null
            }
          }
        ],
        "redir_filters": null,
        "hubs": null,
        "watchdog": null,
        "mem_balloon": null,
        "RNGs": null,
        "NVRAM": null,
        "panics": [
          {
            "XML_name": null,
            "model": "isa",
            "alias": null,
            "address": null
          }
        ],
        "shmems": null,
        "memorydevs": null,
        "IOMMU": null,
        "v_sock": null
      },
      "sec_label": null,
      "QEMU_commandline": null,
      "LXC_namespace": null,
      "VMWare_data_center_path": null,
      "key_wrap": null,
      "launch_security": null,
      "QEMUCapabilities": null,
      "BHyveCommandline": null,
      "info": {
        "uuid": "e7bc32d8-2899-489b-b1a4-9e7bd7fa55bc",
        "ns": "7ade31d4-4a0d-436d-a742-82bb8d05cb3b",
        "name": "centos7x64备份恢复",
        "type": "GUS",
        "ctime": 1625636353,
        "mtime": 1625636538,
        "state": 5,
        "action": 0,
        "ga_state": "disconnect",
        "life_cycle": null,
        "is_image": false,
        "parent_uuid": "702b5996-0347-4063-a9ff-2b5a6b6c27f6",
        "create_type": 4,
        "os": "CentOS x64",
        "HA_mode": "on",
        "machine_uuid": "",
        "migrate_dst": "",
        "define_machine": "",
        "import_machine": "",
        "auto_start": false,
        "MachineIP": "",
        "import_target_device": "",
        "DefineMachineIP": "",
        "StartupSetting": null,
        "Label": null,
        "DeletedTime": 0,
        "Owner": "",
        "AutoExpand": {
          "CpuEnabled": true,
          "ExpandedCpu": 0,
          "MemEnabled": true,
          "ExpandedMem": 0,
          "MaxExpandCpu": 2,
          "MaxExpandMem": 2147483648
        },
        "MemSec": null,
        "Baseline": "Haswell-noTSX-IBRS",
        "DataLocalizationMode": "off",
        "ExtraIPs": null,
        "Zone": "3a739a15-467d-4869-a1aa-a4cd3fdb8009",
        "ObjectGroup": "5f0447da-972f-463c-8f7d-034cf60211f5",
        "RecoveryPolicy": {
          "RecoverToRelatedZones": 2,
          "MasterZoneTakeOver": 2
        },
        "DisasterTolerancePlan": "",
        "DeviceName": "",
        "ShownIp": "",
        "Hidden": false,
        "SetHidden": false,
        "Attrs": null,
        "SpicePortMapping": false,
        "ConsoleSeverListenPort": 0,
        "BlockResizeReq": null,
        "MigrateDstIp": "",
        "QemuMonitorEvent": null,
        "VdcAgent": "",
        "SetVdcAgent": false,
        "VdcAgentList": null,
        "VdcPool": "",
        "VdcPoolName": "",
        "NUMA": false,
        "ha_config": null,
        "TaskTag": 0
      }
    },
    "disks": {
      "/exports/ff43fd25-07d2-42f5-a8c5-02f2a1623b93/.tms.rest/centos7x64.tva/centos7x64-disk1.qcow2": {
        "unit": "",
        "addr": "",
        "capacity": 6442450944,
        "populatedSize": 0,
        "ctrltype": "ide",
        "vid": ""
      }
    },
    "ova_path": "/exports/ff43fd25-07d2-42f5-a8c5-02f2a1623b93/data/centos7x64.tva",
    "snapshot_name": ""
  }
}
```

### POST&nbsp; /v1/compute/unified/import/ova
从OVA文件模板导入虚拟机。

<big>**请求参数**</big>  
```
{
    CreateUnifiedRequest,
    "image_params" : ImageParams_UnifiedImportOVA,
    "host_uuid" : String,
    "path" : String
}
```

+ **CreateUnifiedRequest**  
完整虚拟机创建参数。见[/v1/compute/unified_create](#post-v1computeunified_create)。  
+ **image_params**  
ova文件源相关参数。
+ **host_uuid**  
指定宿主机存储介质源宿主机uuid。
+ **path**  
指定宿主机存储介质源文件路径。

该接口按照给定配置创建卷和虚拟机，并且对虚拟机发起导入，将ova文件磁盘数据导入至虚拟机磁盘中。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
完整虚拟机创建返回。见[/v1/compute/unified_create](#post-v1computeunified_create)。  

ova模板导入虚拟机是异步操作，接口正常返回仅代表操作正常发起，虚拟机进入导入中动作。需要等待后台操作完成，虚拟机才会恢复状态。  
如果导入发起失败，虚拟机会被保留，允许手动后续数据导入。

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","object_group":"0a5d3331-d9fe-4f6a-9c90-879dde781794","zone":"a6f8ad4a-3fdf-4cf6-8fda-90a8093f5316","cpunr":2,"cpu_sockets":1,"cpu_socket_cores":2,"baseline":"Haswell-noTSX-IBRS","max_cpu_nr":2,"mem_size":4294967296,"mem_max":274877906944,"type":"GUS","image_uuid":"","os":"CentOS x64","image_params":{"name":"centos7x64","volume_uuid":"ff43fd25-07d2-42f5-a8c5-02f2a1623b93","repository_uuid":"c5c6e82d-e7ea-47bc-b422-f2d9c767b080","ova_path":"/exports/ff43fd25-07d2-42f5-a8c5-02f2a1623b93/data/centos7x64.tva","volume_type":"vsd"},"memory_huge_pages_enable":false,"meta":{"compute_name":"centos7x64","ha_mode":"on","ha_config":{"priority":0},"os_loader_path":"BIOS","video":[{"model_type":"vga"}],"panic_model":"isa","vnc_enable":false,"mem_sec_enabled":false,"data_localization_mode_on":"off","virt_nested_enable":false,"recover_to_related_zones":2,"master_zone_take_over":2,"startup_setting":null},"interfaces":[{"interface_model_type":"virtio","interface_type":"dsfwd","port_group":"439d8d6a-9a83-4884-a7d8-5a312d6495aa","port_group_name":"voi端口组","vlan_tag_ids":[200],"in_bount":{"average":0,"peak":0,"burst":0},"out_bount":{"average":0,"peak":0,"burst":0},"switch_uuid":"","switch_name":""}],"disks":[{"disk_target_bus":"scsi","disk_cache_mode":"none","disk_unified_vsd":{"tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","pool_uuid":"30fcdfe5-5502-4c9d-a841-6f91a5803245","pool_name":"ycb1000","volume_name":"centos7x64-volume1","capacity":6442450944,"snap_capacity":19327352832,"attribute":{"replica":"1","DriveType":"HDD","VsdVendor":"LIBTARGET"}},"redundancy":1,"file_path":"/exports/ff43fd25-07d2-42f5-a8c5-02f2a1623b93/.tms.rest/centos7x64.tva/centos7x64-disk1.qcow2"}],"cdrom":{"name":"","repository_uuid":""},"floppy":{"name":"","repository_uuid":""},"create_num":1}
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
    "success": 1,
    "fail": 0,
    "results": [
      {
        "message": "success",
        "message_cn": "成功",
        "scode": 0,
        "desc": "",
        "stack": null,
        "data": {
          "tenant": "a5badacf-a25c-4171-9aff-b619fc2d300a",
          "vm_uuid": "b270c11b-d974-4d72-b9bc-bf38edf5ade4",
          "index": 0,
          "vm_name": "centos7x64",
          "volume_uuids": [
            "958e8593-597b-47ec-9b4e-93693d23b6b7"
          ],
          "mac_addresses": [
            "52:56:ff:5e:60:6b"
          ],
          "group": "",
          "group_name": ""
        }
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/export/ova
虚拟机导出到OVA文件。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "disks" : ExportOVADiskInfo,
    "host_uuid" : String,
    "path" : String,
    "format" : String,
    "compress" : Bool,
    "support" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是    
+ **disks**  
虚拟机磁盘相关导出参数。第一个`ExportOVADiskInfo`和后面的意义有所不同。  
_必需_ ： 是    
+ **host_uuid**  
导出到存储介质时指定宿主机uuid。  
_必需_ ： 否    
+ **path**  
导出到存储介质时指定文件路径。  
_必需_ ： 否    
+ **format**  
文件格式后缀。  
_必需_ ： 是  
_有效值_ ： ".ova", ".tva"
+ **compress**  
导出数据是否压缩。  
_必需_ ： 否    
+ **support**  
ova文件支持格式。
_必需_ ： 是  
_有效值_ ： "virtualbox, "vmware"

**ExportOVADiskInfo** 
```
{
    "ova_name" : String,
    "volume_type" : String,
    "volume_uuid" : String,
    "device" : String,
    "snapshot_name" : String,
    "disk_type" : String,
    "repository_uuid" : String
}
```

`disks[0]`对应参数  

+ **ova_name**  
导出文件名。（不包括后缀） 
_必需_ ： 是  
+ **volume_type**  
导出卷类型。  
_有效值_ ： "vsd"(内置存储卷/镜像仓库), "share"(共享存储卷), ""(存储介质)
+ **volume_uuid**  
导出卷uuid。当导出类型为镜像仓库或存储介质时不传。
+ **snapshot_name**  
虚拟机快照名。若指定，则导出基于指定虚拟机快照。否则临时创建虚拟机快照进行导出。
+ **repository_uuid**  
镜像仓库uuid。

`disks[1:]`后续磁盘对应参数  

+ **device**  
指定该参数对应虚拟机磁盘盘符。
+ **disk_type**  
导出后记录的磁盘类型。  
_有效值_ ： "ide", "virtio", "scsi", ""(默认，按现在磁盘参数确定)

接口允许虚拟机关机状态或开机状态时发起，但是要求无动作。  
因为导出需要卷挂载全新的只读挂载点，因此虚拟机运行时可能无法满足该要求而报错`scode:22161`。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

虚拟机导出到OVA文件为异步操作。接口正常返回只代表导出成功发起，虚拟机进入导出中状态。需要等导出实际完成，状态才自动恢复。

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant_uuid":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"25c77828-9309-412b-be4a-74c05237f3f0","compute_name":"test-api4","disks":[{"ova_name":"test-export","volume_uuid":"1e57697c-a77a-4b6f-8cf9-615a7869d404","snapshot_name":"","repository_uuid":"a902c92d-911f-43b5-9df4-e946ef9120cc","volume_type":"vsd"},{"device":"sda"}],"format":".ova","support":"vmware"}
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

### GET&nbsp; /v1/compute/list/ova/path
查询宿主机存储介质目录。

<big>**请求参数**</big>  

 名称 | 参数类型 | 是否必填 | 描述
---|---|---|---
 cluster_uuid|string|是| 集群uuid
 vsm_host_uuid|string|是| 查询主机uuid
 dir|string|是| 查询子目录

查询路径被限制在特定路径下，无法查询宿主机任意路径。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
    "path_info" : [ VMPathInfo ]
}
```

+ **path_info**  
指定目录下文件/目录信息。

<big>**示例**</big>  
**请求示例**  
```
http://10.30.33.25:8080/v1/compute/list/ova/path?vsm_host_uuid=963b6fd4-487e-4436-95c4-21a67aca5eaf&dir=%2F&cluster_uuid=650ea11b-b7fb-4269-8232-aa53865aab3b
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
    "path_info": null
  }
}
```

### POST&nbsp; /v1/compute/migrate/from/vsphere
虚拟机从VSphere集群迁移至超融合集群。

<big>**请求参数**</big>  
```
{
    CommonClusterTenantScope,
    "pool_uuid" : String,
    "vsphere_uuid" : String,
    "vm_reference" : String,
    "vsphere_vm_name" : String,
    "TopHC_vm_name" : String,
    "disk_drive_type" : String
}
```

+ **CommonClusterTenantScope**  
指定集群和租户。见[CommonClusterTenantScope](#commonclustertenantscope)。  
_必需_ ： 是  
+ **baseline**  
指定CPU基准类型。  
_必需_ ： 是  
+ **pool_uuid**  
存储池uuid。新存储卷都在这个存储池内创建。  
_必需_ ： 是  
+ **vsphere_uuid**  
VSphere集群uuid。  
_必需_ ： 是  
+ **vm_reference**  
VSphere集群虚拟机id。  
_必需_ ： 是  
+ **vsphere_vm_name**  
VSphere集群虚拟机名称。  
_必需_ ： 是  
+ **TopHC_vm_name**  
迁移后虚拟机名称。  
_必需_ ： 是  
+ **disk_drive_type**  
数据盘类型。存储卷创建参数。  
_必需_ ： 是  
_有效值_ ： "HDD", "SSD", "any", ""(默认)

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
完整虚拟机创建返回。见[/v1/compute/unified_create](#post-v1computeunified_create)。  

从VSphere集群迁移是异步操作，接口正常返回只代表虚拟机创建成功，并且导入正常发起，虚拟机进入导入动作。要等实际导入完成，虚拟机状态才会自动改变。  
如果导入发起报错，虚拟机不做回滚，允许后续发起数据导入操作。  
导入成功完成后，会将VSphere集群虚拟机关机，并将超融合集群的虚拟机开机。  

<big>**示例**</big>  
**请求示例**  
```json
{"vsphere_uuid":"8afef2fa-cea7-4e4a-9579-bc2fb664ae64","vm_reference":"VirtualMachine:vm-1009","cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","pool_uuid":"30fcdfe5-5502-4c9d-a841-6f91a5803245","zone":"a6f8ad4a-3fdf-4cf6-8fda-90a8093f5316","TopHC_vm_name":"test_migrate","baseline":"Haswell-noTSX-IBRS","disk_drive_type":"HDD"}
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
    "tenant": "a5badacf-a25c-4171-9aff-b619fc2d300a",
    "vm_uuid": "130925c2-5a15-4d46-82bb-2b8463a26d7e",
    "index": 0,
    "vm_name": "test_migrate",
    "volume_uuids": [
      "08ffe388-6801-4ae2-a452-c3bde101d6b8"
    ],
    "mac_addresses": [
      "52:56:ff:8d:fb:3e"
    ],
    "group": "",
    "group_name": ""
  }
}
```

### POST&nbsp; /v1/compute/migrate/to/vsphere
虚拟机从超融合集群迁移到VSphere集群。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "vsphere_vm_name" : String,
    "vsphere_uuid" : String,
    "datacenter_reference" : String,
    "host_reference" : String,
    "vm_config" : {
        "version" : String,
        "guest_id" : String,
        "files" : {
            "vm_path_name" : String
        }
    }
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是    
+ **vsphere_vm_name**  
迁移后VSphere集群虚拟机名称。  
_必需_ ： 是  
+ **vsphere_uuid**  
VSphere集群uuid。  
_必需_ ： 是  
+ **datacenter_reference**  
VSphere集群数据中心id。  
_必需_ ： 是  
+ **host_reference**  
VSphere集群主机id。  
_必需_ ： 是  
+ **vm_config.version**  
VSphere虚拟机版本。  
_必需_ ： 是  
+ **vm_config.guest_id**  
VSphere虚拟机操作系统。  
_必需_ ： 是  
+ **vm_config.files.vm_path_name**  
VSphere虚拟机磁盘数据存储id。  
_必需_ ： 是  

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

迁移至VSphere集群是异步操作，接口正常返回只代表虚拟机创建成功，并且导出正常发起，虚拟机进入导出动作。要等实际导出完成，虚拟机状态才会自动改变。  
导入成功完成后，会将超融合集群虚拟机关机，并将VSphere集群的虚拟机开机。  

<big>**示例**</big>  
**请求示例**  
```json
{"vsphere_uuid":"8afef2fa-cea7-4e4a-9579-bc2fb664ae64","datacenter_reference":"Datacenter:datacenter-2","host_reference":"HostSystem:host-9","vm_config":{"version":"ESXi 6.7 及更高版本","guest_id":"CentOS 7 (64 位)","files":{"vm_path_name":"DataStore-HDD3"}},"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant_uuid":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"130925c2-5a15-4d46-82bb-2b8463a26d7e","compute_name":"test_migrate","vsphere_vm_name":"test_migrate"}
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

### POST&nbsp; /v1/compute/cdrom/attach
虚拟机插入光驱镜像。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "source_network_name" : String,
    "repository_uuid" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **source_network_name**  
光驱镜像名。  
_必需_ ： 是  
+ **repository_uuid**  
镜像仓库uuid。  
_必需_ ： 是  

该接口允许在虚拟机虚拟机关机状态或运行状态下发起。  

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","compute_uuid":"b6b0e5b9-dacd-432b-9b83-c3e89799009d","compute_name":"test-templ","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","source_network_name":"centos7x64.iso","repository_uuid":"c5c6e82d-e7ea-47bc-b422-f2d9c767b080"}
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

### POST&nbsp; /v1/compute/cdrom/detach
虚拟机弹出光驱镜像。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  

该接口允许在虚拟机虚拟机关机状态或运行状态下发起。  
该接口只移除光驱对镜像的使用，不移除光驱设备。  

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","compute_uuid":"b6b0e5b9-dacd-432b-9b83-c3e89799009d","compute_name":"test-templ","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a"}
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

### POST&nbsp; /v1/compute/floppy/attach
虚拟机插入软驱镜像。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "source_network_name" : String,
    "repository_uuid" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **source_network_name**  
光驱镜像名。  
_必需_ ： 是  
+ **repository_uuid**  
镜像仓库uuid。  
_必需_ ： 是  

该接口允许在虚拟机虚拟机关机状态或运行状态下发起。  

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","compute_uuid":"b6b0e5b9-dacd-432b-9b83-c3e89799009d","compute_name":"test-templ","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","source_network_name":"virt.vfd","repository_uuid":"c5c6e82d-e7ea-47bc-b422-f2d9c767b080"}
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

### POST&nbsp; /v1/compute/floppy/detach
虚拟机弹出软驱镜像。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  

该接口允许在虚拟机虚拟机关机状态或运行状态下发起。  
该接口只移除软驱对镜像的使用，不移除软驱设备。  

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","compute_uuid":"b6b0e5b9-dacd-432b-9b83-c3e89799009d","compute_name":"test-templ","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a"}
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

### GET&nbsp; /v1/compute/vm/create/support/config
获取支持的虚拟机创建配置。

<big>**请求参数**</big>  

 名称 | 参数类型 | 是否必填 | 描述
---|---|---|---
 cluster_uuid|string|是| 集群uuid
 zone|string|否| 集群uuid。只会影响返回的`ClusterBaseline`,`MaxTargetRedundancy`,`ClusterSupportedBaseline`字段。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定见返回示例：  

<big>**示例**</big>  
**请求示例**  
```
http://10.30.33.25:8080/v1/compute/vm/create/support/config?zone=a6f8ad4a-3fdf-4cf6-8fda-90a8093f5316&cluster_uuid=650ea11b-b7fb-4269-8232-aa53865aab3b
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
    "OsTypes": {
      "linux": [
        "Ubuntu",
        "Ubuntu x64",
        "CentOS",
        "CentOS x64",
        "Fedora",
        "Fedora 64",
        "Red Hat Enterprise Linux 8 x64",
        "Red Hat Enterprise Linux 7 x64",
        "Red Hat Enterprise Linux 6",
        "Red Hat Enterprise Linux 6 x64",
        "Red Hat Enterprise Linux 5",
        "Red Hat Enterprise Linux 5 x64",
        "Asianux 8 x64",
        "Asianux 7 x64",
        "Asianux 4",
        "Asianux 4 x64",
        "Asianux Server 3",
        "Asianux Server 3 x64",
        "Debian 11.x 64",
        "Debian 11.x",
        "Debian 10.x 64",
        "Debian 10.x",
        "Debian 9.x 64",
        "Debian 9.x",
        "Debian 8.x",
        "Debian 8.x 64",
        "Debian 7.x",
        "Debian 7.x 64",
        "Debian 6.x",
        "Debian 6.x 64",
        "Mandrake Linux",
        "Mandriva Linux",
        "Mandriva Linux x64",
        "Novell Linux Desktop 9",
        "OpenSUSE",
        "OpenSUSE 64",
        "Oracle Enterprise Linux",
        "Oracle Enterprise Linux x64",
        "SUSE Linux Enterprise 15 x64",
        "SUSE Linux Enterprise 12 x64",
        "SUSE Linux Enterprise 11",
        "SUSE Linux Enterprise 11 x64",
        "SUSE Linux Enterprise 10",
        "SUSE Linux Enterprise 10 x64",
        "SUSE Linux Enterprise 7/8/9",
        "SUSE Linux Enterprise 7/8/9 x64",
        "SUSE Linux",
        "SUSE Linux x64",
        "Turbolinux",
        "Turbolinux x64",
        "Other Linux 5.x kernel",
        "Other Linux 5.x kernel x64",
        "Other Linux 4.x kernel",
        "Other Linux 4.x kernel x64",
        "Other Linux 3.x kernel",
        "Other Linux 3.x kernel x64",
        "Other Linux 2.6.x kernel",
        "Other Linux 2.6.x kernel x64",
        "Other Linux 2.4.x kernel",
        "Other Linux 2.4.x kernel x64",
        "UOS",
        "Deepin",
        "中标麒麟",
        "银河麒麟"
      ],
      "others": [
        "FreeBSD",
        "NetBSD",
        "OpenBSD",
        "Solaris",
        "Mac OS X",
        "NGTOS"
      ],
      "topsec": [
        "负载均衡器",
        "虚拟路由器"
      ],
      "windows": [
        "Windows 10",
        "Windows 10 x64",
        "Windows 8",
        "Windows 8 x64",
        "Windows 7",
        "Windows 7 x64",
        "Windows Vista",
        "Windows Vista x64 Edition",
        "Windows XP Professional",
        "Windows XP Professional x64 Edition",
        "Windows Server 2019 x64",
        "Windows Server 2016",
        "Windows Server 2012",
        "Windows Server 2008 R2 x64",
        "Windows Server 2008",
        "Windows Server 2008 x64",
        "Windows Server 2003 Standard Edition",
        "Windows Server 2003 Standard x64 Edition",
        "Windows Server 2003 Enterprise Edition",
        "Windows Server 2003 Enterprise x64 Edition",
        "Windows Server 2003 Smail Business",
        "Windows Server 2003 Web Edition",
        "Windows 2000",
        "Windows NT"
      ]
    },
    "InterfaceModels": [
      "virtio",
      "e1000",
      "rtl8139"
    ],
    "TargetDevices": [
      "hda",
      "hdb",
      "hdc",
      "sda",
      "sdb",
      "sdc",
      "sdd",
      "sde",
      "sdf",
      "sdg",
      "sdh",
      "sdi",
      "sdj",
      "sdk",
      "sdl",
      "sdm",
      "sdn",
      "sdo",
      "vda",
      "vdb",
      "vdc",
      "vdd",
      "vde",
      "vdf",
      "vdg",
      "vdh",
      "vdi",
      "vdj",
      "vdk",
      "vdl",
      "vdm",
      "vdn",
      "vdo"
    ],
    "NetworkTypes": [
      "internal",
      "storage",
      "dsfwd",
      "manage",
      "mirror"
    ],
    "VideoModels": [
      "qxl",
      "vga"
    ],
    "BootLoaders": [
      "BIOS",
      "UEFI"
    ],
    "PanicDevices": [
      "none",
      "isa"
    ],
    "HAModes": [
      "auto",
      "on",
      "off"
    ],
    "MaxInterfaceCount": 10,
    "Baselines": {
      "archs": [
        {
          "name": "x86",
          "vendors": [
            {
              "name": "QEMU",
              "models": [
                "qemu32",
                "kvm32",
                "cpu64-rhel5",
                "cpu64-rhel6",
                "kvm64",
                "qemu64"
              ]
            },
            {
              "name": "Intel",
              "models": [
                "486",
                "pentium",
                "pentium2",
                "pentium3",
                "pentiumpro",
                "coreduo",
                "n270",
                "core2duo",
                "Conroe",
                "Penryn",
                "Nehalem",
                "Nehalem-IBRS",
                "Westmere",
                "Westmere-IBRS",
                "SandyBridge",
                "SandyBridge-IBRS",
                "IvyBridge",
                "IvyBridge-IBRS",
                "Haswell-noTSX",
                "Haswell-noTSX-IBRS",
                "Haswell",
                "Haswell-IBRS",
                "Broadwell-noTSX",
                "Broadwell-noTSX-IBRS",
                "Broadwell",
                "Broadwell-IBRS",
                "Skylake-Client",
                "Skylake-Client-IBRS",
                "Skylake-Client-noTSX-IBRS",
                "Skylake-Server",
                "Skylake-Server-IBRS",
                "Skylake-Server-noTSX-IBRS",
                "Cascadelake-Server",
                "Cascadelake-Server-noTSX",
                "Icelake-Client",
                "Icelake-Client-noTSX",
                "Icelake-Server",
                "Icelake-Server-noTSX",
                "Cooperlake"
              ]
            },
            {
              "name": "AMD",
              "models": [
                "athlon",
                "phenom",
                "Opteron_G1",
                "Opteron_G2",
                "Opteron_G3",
                "Opteron_G4",
                "Opteron_G5",
                "EPYC",
                "EPYC-IBPB",
                "EPYC-Rome"
              ]
            },
            {
              "name": "Hygon",
              "models": [
                "Dhyana"
              ]
            }
          ]
        },
        {
          "name": "ppc64",
          "vendors": [
            {
              "name": "IBM",
              "models": [
                "POWER6",
                "POWER7",
                "POWER8",
                "POWER9"
              ]
            },
            {
              "name": "Freescale",
              "models": [
                "POWERPC_e5500",
                "POWERPC_e6500"
              ]
            }
          ]
        },
        {
          "name": "arm",
          "vendors": [
            {
              "name": "ARM",
              "models": [
                "cortex-a53",
                "cortex-a57",
                "cortex-a72"
              ]
            },
            {
              "name": "Qualcomm",
              "models": [
                "Falkor"
              ]
            },
            {
              "name": "Cavium",
              "models": [
                "ThunderX299xx"
              ]
            },
            {
              "name": "Hisilicon",
              "models": [
                "Kunpeng-920"
              ]
            },
            {
              "name": "Phytium",
              "models": [
                "FT-2000plus",
                "Tengyun-S2500"
              ]
            }
          ]
        }
      ]
    },
    "ClusterBaseline": "Haswell-noTSX-IBRS",
    "MaxTargetRedundancy": 3,
    "ClusterSupportedBaseline": [
      "Opteron_G1",
      "pentium2",
      "486",
      "coreduo",
      "Westmere",
      "pentium",
      "n270",
      "core2duo",
      "Conroe",
      "cpu64-rhel6",
      "cpu64-rhel5",
      "qemu64",
      "qemu32",
      "kvm64",
      "Opteron_G2",
      "Nehalem",
      "pentium3",
      "kvm32",
      "Penryn"
    ]
  }
}
```

### GET&nbsp; /v1/compute/state/summary
虚拟机状态统计。

<big>**请求参数**</big>  

 名称 | 参数类型 | 是否必填 | 描述
---|---|---|---
 cluster_uuid|string|是| 集群uuid
 tenant|string|否| 租户uuid。为空时，指定全部租户。
 filter_machine_uuid|string|否| 指定宿主机uuid

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
    "total" : Number,
    "no_state_count" : Number,
    "running_count" : Number,
    "blocked_count" : Number,
    "paused_count" : Number,
    "shutdown_count" : Number,
    "shutoff_count" : Number,
    "crashed_count" : Number,
    "pmsuspend_count" : Number,
    "cloning_count" : Number,
    "save_count" : Number,
    "migrating_count" : Number,
    "pending_count" : Number,
    "importing_count" : Number,
    "unknown_count" : Number,
    "restoring_count" : Number
}
```
<big>**示例**</big>  
**请求示例**  
```json
无
```
**返回示例**  
```json
无
```

### POST&nbsp; /v1/compute/vmemory/set
设置虚拟机内存。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "vmemory" : Number
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **vmemory**  
指定虚拟机内存。单位Bytes，大小不能超过256G。  
_必需_ ： 是  

该接口支持在关机状态下修改内存，也支持运行状态下热添加内存。  

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","compute_uuid":"b6b0e5b9-dacd-432b-9b83-c3e89799009d","compute_name":"test-templ","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","vmemory":2147483648,"mem_max":274877906944}
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

### POST&nbsp; /v1/compute/usb/attach
虚拟机插入usb设备。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "usb" : [ AttachUSBSingleRequest ]
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **usb**  
指定添加的usb设备参数。支持批量添加。
_必需_ ： 是  

**AttachUSBSingleRequest**  
```
{
    "pass_through_usb_bus" : Number,
    "pass_through_usb_port" : Number,
    "redirect_usb_bus" : Number,
    "redirect_usb_port" : Number,
    "spice_vmc_usb_bus" : Number,
    "spice_vmc_usb_port" : Number,
    "source_usb_host_uuid" : String,
    "source_usb_bus" : Number,
    "source_usb_device" : Number
}
```

支持三种类型usb设备源中的一种：  

+ **透传usb设备**。`pass_through_usb_bus`和`pass_through_usb_port`。将宿主机的usb设备直接透传给虚拟机。和其他透传设备一样，要求关闭高可用，只能在运行状态添加，并且会限制虚拟机运行主机。
+ **重定向usb设备**。`redirect_usb_bus`和`redirect_usb_port`。开启usb重定向服务，将特定tcp请求重定向至usb设备。该类型允许使用不同主机上的usb设备。
+ **spice vmc接口**。`spice_vmc_usb_bus`和`spice_vmc_usb_port`。用于spice客户端重定向usb设备的接口。

透传usb设备和重定向usb设备都引用一个实际的宿主机usb设备。都需要提供`source_usb_host_uuid`, `source_usb_bus`, `source_usb_device`参数。

三种usb设备源都要指定在虚拟机中的设备位置，不能和已有usb设备冲突。其中：

+ `bus 0`是usb1.1，`port`支持1-2共2个，其中`port 1`默认被占用。  
+ `bus 1`是usb2.0，`port`支持1-6共6个。  
+ `bus 2`是usb3.0，`port`支持1-4共4个。默认`port 4`被一个spice vmc接口占用，但是可以手动移除。  

如果`port`不指定，则会在选定bus自动选择一个可用port供usb设备使用。  
除了要添加的usb设备类型对应的参数，其余类型要求的参数均不可指定。  
除了透传usb设备要求在运行状态添加，其他usb设备也可以在关机状态下添加。  

<big>**返回数据**</big>  
接口返回数据先使用[BatchOutput](#batchoutput)封装，再用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"b6b0e5b9-dacd-432b-9b83-c3e89799009d","compute_name":"test-templ","usb":[{"source_usb_host_uuid":"27b506e4-ed2d-4c78-b723-e5fe77303d93","source_usb_bus":1,"source_usb_device":1,"pass_through_usb_bus":2}]}
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
    "success": 1,
    "fail": 0,
    "results": [
      {
        "message": "success",
        "message_cn": "成功",
        "scode": 0,
        "desc": "",
        "stack": null,
        "data": {}
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/usb/detach
虚拟机卸载usb设备。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "target_bus" : Number,
    "target_port" : Number
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **target_bus**  
目标usb设备总线号。  
_必需_ ： 是  
+ **target_port**  
目标usb设备端口号。  

该接口允许虚拟机在关机状态或运行状态下卸载所有usb设备。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","compute_uuid":"b6b0e5b9-dacd-432b-9b83-c3e89799009d","compute_name":"test-templ","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","target_bus":2,"target_port":1}
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

### POST&nbsp; /v1/compute/cpu/reserve
虚拟机设置CPU预留。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "cpu_reserve_enable" : Bool
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **cpu_reserve_enable**  
是否开启CPU预留。  
_必需_ ： 是  

该接口允许虚拟机在关机状态或运行状态下设置。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"b6b0e5b9-dacd-432b-9b83-c3e89799009d","compute_name":"test-templ","cpu_reserve_enable":true,"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b"}
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

### POST&nbsp; /v1/compute/memory/reserve
虚拟机设置内存预留。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "memory_reserve_enable" : Bool
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **cpu_reserve_enable**  
是否开启内存预留。  
_必需_ ： 是  

该接口只允许在虚拟机关机状态下设置。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"b6b0e5b9-dacd-432b-9b83-c3e89799009d","compute_name":"test-templ","memory_reserve_enable":true}
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

### POST&nbsp; /v1/compute/interface/mac/update
虚拟机修改网卡MAC地址。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "old_mac_address" : String,
    "new_mac_address" : String
}
```

+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **old_mac_address**  
指定待修改网卡的MAC地址。  
_必需_ ： 是  
+ **new_mac_address**  
指定网卡修改后的MAC地址。  
_必需_ ： 是  

该接口只允许在虚拟机关机状态下设置。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
特定返回为空。使用[Output](#output)字段表示报错。  

<big>**示例**</big>  
**请求示例**  
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","compute_name":"test-templ","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"b6b0e5b9-dacd-432b-9b83-c3e89799009d","old_mac_address":"52:56:ff:1e:a5:a9","new_mac_address":"52:56:ff:1e:a5:aa"}
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

### POST&nbsp; /v1/compute/alter/device_name
修改windows虚拟机设备名称。

<big>**请求参数**</big>  
```
{
    ComputeIdentifier,
    "device_name" : String
}
```
+ **ComputeIdentifier**  
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。  
_必需_ ： 是  
+ **device_name**  
待修改的设备名称。

该接口要求虚拟机处于运行状态，并且Agent状态要求为已连接。

<big>**返回数据**</big>  
接口返回数据使用[Output](#output)封装。接口特定返回如下：  
```
"data" : {
    "compute_uuid" : String,
    "compute_name" : String,
    "device_name" : String
}
```

<big>**示例**</big>  
**请求示例**  
无

**返回示例**  
无

### POST&nbsp; /v1/compute/group/create
创建虚拟机分组。

<big>**请求参数**</big>
```
{
    CommonClusterTenantScope,
    "parent_group" : String,
    "group_name" : String
}
```

+ **CommonClusterTenantScope**
指定集群和租户。见[CommonClusterTenantScope](#commonclustertenantscope)。
_必需_ ： 是
+ **parent_group**
父虚拟机分组。通过该参数生成嵌套虚拟机组。不指定时则会在租户顶层生成新分组。
_必需_ ： 否
+ **group_name**
虚拟机分组名称。名称不能和已有同级虚拟机分组冲突。
_必需_ ： 是

无法在default分组下创建子分组。
分组最多嵌套5层，层次过深无法创建。

<big>**返回数据**</big>
接口返回数据使用[Output](#output)封装。接口特定返回如下：
```
"data" : {
    ObjectGroupCache
}
```

新创建的虚拟机分组信息。见[ObjectGroupCache](#objectgroupcache)。

<big>**示例**</big>
**请求示例**
```json
{"tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","group_name":"test","cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","parent_group":null}
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
    "Metadata": {
      "UUID": "da633538-1178-45c5-bbb9-1b20bdcf612c",
      "Namespace": "91a57ba2-2904-4c90-bc16-85ecbbad815f",
      "Name": "test",
      "Desc": "",
      "Parent": "",
      "Attrs": null,
      "RefCount": 0,
      "Children": null
    },
    "Children": null,
    "Refs": null,
    "Depth": 1
  }
}
```

### POST&nbsp; /v1/compute/group/delete
删除虚拟机分组。

<big>**请求参数**</big>
```
{
    CommonClusterTenantScope,
    "group_uuid" : String
}
```

指定集群、租户、待删除虚拟机分组uuid。
删除一个虚拟机分组，会将它下面的全部子分组同时删除。
当待虚拟机分组或者任意被其嵌套的分组非空时，分组无法删除。
无法删除default分组。

<big>**返回数据**</big>
接口返回数据使用[Output](#output)封装。接口特定返回如下：
特定返回为空。使用[Output](#output)字段表示报错。

<big>**示例**</big>
**请求示例**
```json
{"tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","group_name":"test2","group_uuid":"1c9a9c69-be8e-495d-b697-405bdfa6c23c","cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b"}
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

### POST&nbsp; /v1/compute/group/update
编辑虚拟机分组。

<big>**请求参数**</big>
```
{
    CommonClusterTenantScope,
    "group_name" : String,
    "group_uuid" : String
}
```

指定集群、租户、待删除虚拟机分组uuid。
该接口目前仅用于修改分组名称。若不传`group_name`，不报错也不做修改。

<big>**返回数据**</big>
接口返回数据使用[Output](#output)封装。接口特定返回如下：
```
"data" : {
}
```
<big>**示例**</big>
**请求示例**
```json
{"tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","group_name":"test2","cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","group_uuid":"da633538-1178-45c5-bbb9-1b20bdcf612c"}
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

### GET&nbsp; /v1/compute/group/inspect
获取虚拟机分组信息。

<big>**请求参数**</big>

 名称 | 参数类型 | 是否必填 | 描述
---|---|---|---
 cluster_uuid|string|是| 集群uuid
 tenant|string|是| 租户uuid
 group_uuid|string|是| 虚拟机分组uuid

<big>**返回数据**</big>
接口返回数据使用[Output](#output)封装。接口特定返回如下：
```
"data" : {
    ObjectGroupCache
}
```

虚拟机分组信息。见[ObjectGroupCache](#objectgroupcache)。

<big>**示例**</big>
**请求示例**
```
http://10.30.12.150:8080/v1/compute/group/inspect?tenant=a0313629-10fd-48dc-9e92-5dff744a3c0e&cluster_uuid=bdc01c45-973c-4b7b-a565-7a03c74379e4&group_uuid=a1735326-a5fe-4c0f-8294-b6822bd0b105
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
    "Metadata": {
      "UUID": "a1735326-a5fe-4c0f-8294-b6822bd0b105",
      "Namespace": "8ae9e9eb-dff9-4ecf-9306-c9e1c98764df",
      "Name": "default",
      "Parent": "",
      "RefCount": 0,
      "Children": null
    },
    "Children": null,
    "Refs": [
      {
        "UUID": "055610f8-7386-471d-9e81-2c9b141c2a1c",
        "Type": 1
      }
    ],
    "Depth": 1
  }
}
```

### GET&nbsp; /v1/compute/group/tree
查看虚拟机分组树。

<big>**请求参数**</big>

 名称 | 参数类型 | 是否必填 | 描述
---|---|---|---
 cluster_uuid|string|否| 集群uuid
 tenant|string|否| 租户uuid

该接口将虚拟机分组的嵌套关系按树状结构显示出来，用于界面展示。
若指定了集群和租户，则结果顶层为单个租户节点，次层为租户下的全部分组节点。
若集群或租户有任何一个未指定，则顶层为并列的集群节点，次层为租户节点，再次层为命名空间节点，再下一层才是实际的分组数据。

<big>**返回数据**</big>
接口返回数据使用[Output](#output)封装。接口特定返回如下：
```
"data" : {
    "list" : [ ComputeGroupObjectMeta ],
    "total_count" : Number,
    "each_range_list_state" : [ EachResourceRangeListState ]
}
```

+ **list**
顶层节点数据。通过`Children`字段形成树状结构。见[ComputeGroupObjectMeta](#computegroupobjectmeta)。
+ **total_count**
顶层节点数量。
+ **each_range_list_state**
每个集群、租户单独的查询数据统计。见[EachResourceRangeListState](#eachresourcerangeliststate)。

<big>**示例**</big>
**请求示例**
```
http://10.30.33.25:8080/v1/compute/group/tree?tenant=a5badacf-a25c-4171-9aff-b619fc2d300a&filter_name=&cluster_uuid=
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
        "UUID": "650ea11b-b7fb-4269-8232-aa53865aab3b",
        "Namespace": "",
        "Name": "host3222-cvm3322",
        "Desc": "",
        "Parent": "",
        "Attrs": null,
        "RefCount": 0,
        "Children": [
          {
            "UUID": "a5badacf-a25c-4171-9aff-b619fc2d300a",
            "Namespace": "",
            "Name": "ycb1",
            "Desc": "",
            "Parent": "650ea11b-b7fb-4269-8232-aa53865aab3b",
            "Attrs": null,
            "RefCount": 0,
            "Children": [
              {
                "UUID": "91a57ba2-2904-4c90-bc16-85ecbbad815f",
                "Namespace": "",
                "Name": "ycb1",
                "Desc": "",
                "Parent": "a5badacf-a25c-4171-9aff-b619fc2d300a",
                "Attrs": null,
                "RefCount": 0,
                "Children": [
                  {
                    "UUID": "0a5d3331-d9fe-4f6a-9c90-879dde781794",
                    "Namespace": "91a57ba2-2904-4c90-bc16-85ecbbad815f",
                    "Name": "default",
                    "Desc": "",
                    "Parent": "91a57ba2-2904-4c90-bc16-85ecbbad815f",
                    "Attrs": null,
                    "RefCount": 5,
                    "Children": [],
                    "fake": false,
                    "deny_child_create": false,
                    "is_stop": false,
                    "is_health": false,
                    "cluster_uuid": "650ea11b-b7fb-4269-8232-aa53865aab3b",
                    "cluster_name": "host3222-cvm3322",
                    "tenant": "a5badacf-a25c-4171-9aff-b619fc2d300a",
                    "tenant_name": "ycb1"
                  }
                ],
                "fake": true,
                "deny_child_create": false,
                "is_stop": false,
                "is_health": false,
                "cluster_uuid": "650ea11b-b7fb-4269-8232-aa53865aab3b",
                "cluster_name": "host3222-cvm3322",
                "tenant": "a5badacf-a25c-4171-9aff-b619fc2d300a",
                "tenant_name": "ycb1"
              }
            ],
            "fake": true,
            "deny_child_create": true,
            "is_stop": false,
            "is_health": false,
            "cluster_uuid": "650ea11b-b7fb-4269-8232-aa53865aab3b",
            "cluster_name": "host3222-cvm3322",
            "tenant": "a5badacf-a25c-4171-9aff-b619fc2d300a",
            "tenant_name": "ycb1"
          }
        ],
        "fake": true,
        "deny_child_create": true,
        "is_stop": false,
        "is_health": true,
        "cluster_uuid": "650ea11b-b7fb-4269-8232-aa53865aab3b",
        "cluster_name": "host3222-cvm3322"
      }
    ],
    "total_count": 1,
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
        "total_count": 1
      }
    ]
  }
}
```

### POST&nbsp; /v1/compute/group/move
移动虚拟机分组。

<big>**请求参数**</big>
```
{
    CommonClusterTenantScope,
    "group_uuid" : String,
    "parent_group" : String
}
```

+ **CommonClusterTenantScope, group_uuid**
指定集群、租户、虚拟机分组uuid。
+ **parent_group**
移动的目的分组uuid。若为空，则移动到分组顶层。

移动分组会保持子分组的嵌套关系，即一同移动。
分组下有虚拟机时允许移动。
分组不能造成自己或任何嵌套分组超过最大5层的深度限制。

<big>**返回数据**</big>
接口返回数据使用[Output](#output)封装。接口特定返回如下：
特定返回为空。使用[Output](#output)字段表示报错。

<big>**示例**</big>
**请求示例**
```json
{"tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","group_name":"tes1","cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","parent_group":"da633538-1178-45c5-bbb9-1b20bdcf612c","group_uuid":"636608f9-478c-4c0e-9696-366d26c5c761"}
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

### POST&nbsp; /v1/compute/video/attach
虚拟机添加显示设备。

<big>**请求参数**</big>
```
{
    ComputeIdentifier,
    "videos" : [ ComputeVideo ]
}
```

+ **ComputeIdentifier**
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。
_必需_ ： 是
+ **videos**
添加的显示设备参数。见[ComputeVideo](#computevideo)。
_必需_ ： 是

该接口要求虚拟机处于关机状态。
虚拟机已有显示设备和待添加显示设备，都只能是QXL类型。

<big>**返回数据**</big>
接口返回数据使用[Output](#output)封装。接口特定返回如下：
```
"data" : {
    "name" : String,
    "uuid" : String
}
```

返回结果标记操作虚拟机。和请求参数相同。

<big>**示例**</big>
**请求示例**
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","compute_name":"test-templ","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"b6b0e5b9-dacd-432b-9b83-c3e89799009d","videos":[{"model_type":"qxl","ram_size":131072,"vga_mem":32768}]}
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
    "name" : "test-templ",
    "uuid" : "b6b0e5b9-dacd-432b-9b83-c3e89799009d"
  }
}
```

### POST&nbsp; /v1/compute/video/detach
移除虚拟机显示设备。

<big>**请求参数**</big>
```
{
    ComputeIdentifier,
    "heads" : Number
}
```

+ **ComputeIdentifier**
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。
_必需_ ： 是
+ **heads**
移除序号为`heads`的显示设备。

该接口要求虚拟机为关机状态。
`heads`序号从0开始，并且序号0的显示设备不能删除。
显示设备删除后，序号重新从0开始排。

<big>**返回数据**</big>
接口返回数据使用[Output](#output)封装。接口特定返回如下：
```
"data" : {
    "name" : String,
    "uuid" : String
}
```

返回结果标记操作虚拟机。和请求参数相同。

<big>**示例**</big>
**请求示例**
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","compute_name":"test-templ","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"b6b0e5b9-dacd-432b-9b83-c3e89799009d","heads":1}
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
    "name" : "test-templ",
    "uuid" : "b6b0e5b9-dacd-432b-9b83-c3e89799009d"
  }
}
```

### POST&nbsp; /v1/compute/video/edit
虚拟机编辑显示设备。

<big>**请求参数**</big>
```
{
    ComputeIdentifier,
    "video" : ComputeVideo
}
```

+ **ComputeIdentifier**
指定虚拟机。见[ComputeIdentifier](#computeidentifier)。
_必需_ ： 是
+ **video**
修改的显示设备参数。用`video.heads`指定修改显示设备的序号。见[ComputeVideo](#computevideo)。
_必需_ ： 是

该接口要求虚拟机处于关机状态。
无法在有多个显示设备的情况下修改设备为QXL以外的类型。

<big>**返回数据**</big>
接口返回数据使用[Output](#output)封装。接口特定返回如下：
```
"data" : {
    "name" : String,
    "uuid" : String
}
```

返回结果标记操作虚拟机。和请求参数相同。

<big>**示例**</big>
**请求示例**
```json
{"cluster_uuid":"650ea11b-b7fb-4269-8232-aa53865aab3b","compute_name":"test-templ","tenant":"a5badacf-a25c-4171-9aff-b619fc2d300a","compute_uuid":"b6b0e5b9-dacd-432b-9b83-c3e89799009d","videos":[{"model_type":"qxl","ram_size":131072,"vga_mem":32768}]}
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
    "name" : "test-templ",
    "uuid" : "b6b0e5b9-dacd-432b-9b83-c3e89799009d"
  }
}
```

---

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

### EachResourceRangeListState
多集群或多命名空间操作、查询API中，返回记录每个集群、命名空间的操作、查询结果的数据。
```
{
    ClusterIdentifier,
    NamespaceIdentifier,
    "result" : Output,
    "total_count" : Number
}
```

+ **ClusterIdentifier**  
展示该部分对应的请求集群。
+ **NamespaceIdentifier**  
展示该部分对应的请求命名空间。
+ **result**  
记录该部分对应的请求错误信息。`Output.data`字段不使用。
+ **total_count**  
对于列表请求，记录该部分对应查询的满足筛选条件的结果总数。

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

### PagingParam
通用分页配置参数。
```
{
    "page_number" : Number,
    "page_size" : Number
}
```

+ **page_number**  
分页序号。返回第`page_number`页结果。从第0页开始。  
_是否必需_： 否  
+ **page_size**  
分页大小。返回结果以`page_size`个结果为一页。若不大于0则不进行分页。  
_是否必需_： 否  

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

## 虚拟机相关
### CloneTypeParam
克隆参数。
```
{
    "link" : Bool,
    "snapshot" : String,
    "component_cache" : Bool
}
```

+ **link**  
是否使用连接克隆。
+ **snapshot**  
指定克隆用快照名。
+ **component_cache**  
是否开启组件缓存特性。要求`link=true`。

### CloudInitData
虚拟机初始化配置参数。

### ComputeIdentifier
指定、描述相关虚拟机。
```
{
    CommonClusterTenantScope,
    "compute_uuid" : String,
    "compute_name" : String,
    "owner" : String
}
```

+ **CommonClusterTenantScope**  
指定、展示相关集群、租户。见[CommonClusterTenantScope](#commonclustertenantscope)。
+ **compute_uuid**  
指定虚拟机uuid。请求中的主要参数。
+ **compute_name**  
指定、展示虚拟机名。多用于返回数据，也用于相关请求记录操作日志。部分接口用作参数。
+ **owner**  
部分请求中，用于指定通知客户端操作修改的用户uuid，告知用户客户端更新数据。


### ComputeInfo
TODO

### ComputeMeta
```
{
    "compute_name" : String,
    "ha_mode" : String,
    "os_loader_path" : String,
    "video" : [ ComputeVideo ],
    "panic_model" : String,
    "startup_setting" : StartupSetting,
    "vnc_enable" : Bool,
    "mem_sec_enabled" : Bool,
    "shown_ip" : String,
    "virt_nested_enable" : Bool,
    "data_localization_mode_on" : String,
    "recover_to_related_zones" : Number,
    "master_zone_take_over" : Number
}
```

+ **compute_name**  
虚拟机名。
+ **ha_mode**  
是否开启HA。  
_有效值_ ： "on", "off", "auto"。目前auto和on完全相同。
+ **os_loader_path**  
虚拟机启动加载方式。  
_有效值_ ： "BIOS", "UEFI"
+ **video**  
虚拟机显示设备配置。见[ComputeVideo](#computevideo)。
+ **panic_model**  
蓝屏捕捉功能。  
_有效值_ ： "isa", "none"。isa为开启，none为关闭。
+ **startup_setting**  
虚拟机启动主机配置。见[StartupSetting](#startupsetting)。
+ **vnc_enable**  
是否开启VNC。
+ **mem_sec_enabled**  
是否开启内存安全。
+ **shown_ip**  
虚拟机展示IP。
+ **virt_nested_enable**  
是否开启嵌套虚拟化。
+ **data_localization_mode_on**  
是否开启数据本地化。  
_有效值_ ： "on"， "off"
+ **recover_to_related_zones**  
设置集群双活。  
_有效值_ ： 1(开启), 2(关闭)
+ **master_zone_take_over**  
设置主集群接管。要触发需要开启双活。  
_有效值_ ： 1(开启), 2(关闭)

### ComputeGroupObjectMeta
虚拟机分组树节点。
```
{
    "UUID" : String,
    "Namespace" : String,
    "Name" : String,
    "Parent" : String,
    "RefCount" : Number,
    "Children" : [ ComputeGroupObjectMeta ],
    "fake" : Bool,
    "is_stop" : Bool,
    "is_health" : Bool,
    ClusterIdentifier,
    TenantIdentifier
}
```

+ **UUID**
虚拟机分组uuid。
+ **Namespace**
虚拟机分组命名空间uuid。
+ **Name**
虚拟机分组名称。
+ **Parent**
父虚拟机分组uuid。
+ **RefCount**
包含的虚拟机计数。
+ **Children**
包含的子节点。通过该字段形成树状结构。
+ **fake**
是否是抽象节点。`fake=true`时，该节点时接口为了展示集群、租户、命名空间的逻辑关系，而添加的嵌套节点，并不对应实际虚拟机分组。
+ **is_stop**
集群是否已停用。只在集群节点上有效。
+ **is_health**
集群是否健康。只在集群节点上有效。
+ **ClusterIdentifier**
展示集群信息。
+ **TenantIdentifier**
展示租户信息。

### ComputeVideo
虚拟机显示设备配置。
```
{
    "model_type" : String,
    "heads" : Number,
    "ram_size" : Number,
    "vga_mem" ： Number
}
```

+ **model_type**  
显示设备驱动。  
_有效值_ ： "qxl", "vga", "virtio", "none"
+ **heads**  
最大显示输出数。  
+ **ram_size**  
显存大小, 单位kB。限制屏幕最大分辨率。
+ **vga_mem**  
vga显存大小，单位kB。限制屏幕最大分辨率。

### Disk
虚拟机磁盘数据。
```
{
    "disk_target_device" : String,
    "disk_target_bus" : String,
    "disk_volume_source" : DiskVolumeSource,
    "disk_vsd_source" : DiskVsdSource,
    "disk_block_source" : DiskBlockSource,
    "disk_source_passthrough" : DiskPassthroughSource,
    "disk_cache_mode" : String,
    "disks_serial" : String,
    "wwn" : String,
    "disk_is_system" : Bool
}
```

+ **disk_target_device**  
指定、展示磁盘盘符。  
_有效值_ : "id[a-c]", "sd[a-o]", "vd[a-o]"  
该字段作为虚拟机内磁盘的唯一标识，通常用来指定虚拟机中的某个磁盘。  
若添加新磁盘时未指定`disk_target_device`，会自动根据`disk_target_bus`分配一个盘符。  
作为磁盘返回时必定会有该字段。    
+ **disk_target_bus**  
指定、展示磁盘驱动。  
_有效值_ : "ide", "scsi", "virtio", "sata"  
作为磁盘返回时必定会有该字段。  
+ **disk_volume_source**  
共享存储类型磁盘源。见[DiskVolumeSource](#diskvolumesource)。  
使用共享存储卷作为虚拟机磁盘。
+  **disk_vsd_source**  
内置存储类型磁盘源。见[DiskVsdSource](#diskvsdsource)。  
使用内置存储卷作为虚拟机磁盘。
+ **disk_block_source**  
内置存储块设备类型磁盘源。见[DiskBlockSource](#diskblocksource)。  
使用内置存储块设备类型卷作为虚拟机磁盘。
+ **disk_source_passthrough**  
透传磁盘类型磁盘源。见[DiskPassthroughSource](#diskpassthroughsource)。  
使用宿主机透传磁盘作为虚拟机磁盘。
+ **disk_cache_mode**  
磁盘缓存模式。  
_有效值_ : "", "none", "default", "writeback", "writethrough"
设置磁盘缓存模式。指定"writeback", "writethrough"，并且"target_bus"为"scsi"时，会强制将"target_bus"转化为"virtio"，以使磁盘缓存生效。
+ **disks_serial**  
展示磁盘序列号。
+ **wwn**  
展示磁盘WWN。
+ **disk_is_system**  
展示磁盘是否是系统盘。影响虚拟机启动顺序。  

一个磁盘有且只有一个源。作为参数如果要设置磁盘源，卷必须要指定一个`disk_xxx_source`。作为返回，必定有一个`disk_xxx_source`。  
只有`ide`和`scsi`驱动的磁盘才有`disks_serial`,`wwn`。

### DiskBlockSource
内置存储块设备类型磁盘源。
```
{
    "volume_uuid" : Stirng,
    "host_dev" : String,
    "volume_name" : String,
    "disk_capacity" ： Number,
    "pool_uuid" : String,
    "pool_name" : String,
    "replica" : String,
    "drive_type" : String,
    "vsd_vendor" : String
}
```

+ **volume_uuid**  
指定、展示磁盘对应卷uuid。卷是内置存储的块设备类型卷。
+ **host_dev**  
展示磁盘卷挂载后的块设备名。请求中不需要指定。

其余字段均为展示内置存储卷相关信息。

### DiskPassthroughSource
透传磁盘类型磁盘源。
```
{
    "disk_id" : String,
    "host_uuid" : String,
    "host_ip" : String,
    "disk_capacity" : Number,
    "disk_path" : String
}
```

+ **disk_id**  
指定、展示透传磁盘ID。磁盘ID可以通过专门的接口查询。
+ **host_uuid**  
指定、展示透传磁盘所在主机ID。

其余字段均为展示透传磁盘的相关信息。

###  DiskVolumeSource
共享存储类型磁盘源。
```
{
    "pool" : String,
    "volume" : String,
    "volume_uuid" : String,
    "disk_capacity" : Number,
    "pool_name" : String,
    "replica" : String,
    "drive_type" : String
}
```

+ **pool**  
指定、展示共享存储卷的存储池uuid。
+ **volume**  
展示共享存储卷名。
+ **volume_uuid**  
指定、展示共享存储卷uuid。

其余字段均为展示共享存储卷的相关信息。

### DiskVsdSource
内置存储类型磁盘源。
```
{
    "volume_uuid" : String,
    "volume_name" : String,
    "disk_capacity" : Number,
    "pool_uuid" : String,
    "pool_name" : String,
    "replica" : String,
    "drive_type" : String,
    "redundancy" : Number,
    "vsd_vendor" : String
}
```

+ **volume_uuid**  
指定、展示内置存储卷uuid。
+ **redundancy**  
指定、展示iscsi卷链路冗余数。该设置项只对iscsi卷生效。

其余字段均为展示内置存储卷的相关信息。  
若请求通过`volume_uuid`指定了块设备类型卷，创建后会改为使用[DiskBlockSource](#diskblocksource)展示，`redundancy`也会被丢弃。

### Interface
虚拟机网卡设置。
```
{
    "interface_id" : String,
    "interface_model_type" : String,
    "interface_type" : String,
    "mac_address" : String,
    "ips" : [ String ],
    "in_bount" : InterfaceBound,
    "out_bount" : InterfaceBound,
    "switch_uuid" : String,
    "switch_name" : String,
    "gateway_uuid" : String,
    "gateway_name" : String,
    "port_group" : String,
    "port_group_name" : String,
    "vlan_tag_ids" : [ Number ],
    "bound_ip" : String,
    "peer" : String
}
```

+ **interface_id**  
展示网卡ID。该ID集群内唯一。  
+ **interface_model_type**  
指定、展示网卡类型。会影响到网卡驱动。  
_有效值_ ： "virtio", "e1000", "rtl8139"  
+ **interface_type**  
指定、展示网卡网络名。  
_有效值_ ： 本地网络名，"internal"(vpc网络)  
+ **mac_address**  
指定、展示网卡MAC地址。MAC地址在集群内唯一。
+ **ips**  
展示网卡IP。
+ **in_bount**  
指定、展示网卡接收QOS。见[Interface](#interface)。
+ **out_bount**  
指定、展示网卡发送QOS。见[Interface](#interface)。  
+ **switch_uuid**  
指定、展示连接VPC交换机uuid。只有网络为`internal`时才生效。  
+ **switch_name**  
展示连接VPC交换机名称。
+ **gateway_uuid**  
指定、展示连接VPC网关uuid。只有网络为`internal`时才生效。  
+ **gateway_name**  
展示连接VPC网关名称。
+ **port_group**  
指定、展示端口组uuid。使用本地网络时该项是必需项。
+ **port_group_name**  
展示端口组名称。
+ **vlan_tag_ids**  
指定、展示VLAN id。只在端口组设置了VLAN才可用。
+ **bound_ip**  
指定、展示网卡绑定IP。
+ **peer**  
指定是否对MAC和IP进行绑定。 
_有效值_ ： ""(不绑定), "mac"(绑定)

### InterfaceBound
虚拟机网卡QOS设置。
```
{
    "average" : Number,
    "peak" : Number,
    "burst" : Number
}
```

+ **average**  
指定、展示网速均值限制。单位kB/s。当`average`为0时等同于不设置QOS。
+ **peak**  
指定、展示网速峰值限制。单位kB/s。
+ **burst**  
指定、展示流量波峰大小限制。单位kB。

### MdevDevice
Mdev设备参数。
```
{
    "src_address_uuid" : String,
    "model" : String,
    "display" : String
}
```

+ **src_address_uuid**  
指定、展示设备uuid。  
+ **model**  
指定、展示设备驱动。  
_有效值_ ： "vfio-pci", "vfio-ccw", "vfio-ap"
+ **display**  
指定、展示是否开启设备加速。  
_有效值_ ： "on", "off"

详细说明见[libvirt domain官方文档](https://libvirt.org/formatdomain.html#usb-pci-scsi-devices)。

### ObjectGroupCache
虚拟机分组信息。
```
{
    "Metadata" : ObjectGroupMeta,
    "Children" : [ String ],
    "Refs" : [ ObjectGroupRef ],
    "Depth" : Number
}
```

+ **Metadata**
虚拟机分组配置。见[ObjectGroupMeta](#objectgroupmeta)。
+ **Children**
子虚拟机分组uuid。
+ **Refs**
记录虚拟机分组内的虚拟机uuid。
+ **Depth**
虚拟机分组深度。最低深度1，最大深度5。

### ObjectGroupMeta
```
{
    "UUID" : String,
    "Namespace" : String,
    "Name" : String,
    "Parent" : String,
    "RefCount" : Number
}
```

+ **UUID**
虚拟机分组uuid。
+ **Namespace**
虚拟机分组命名空间uuid。
+ **Name**
虚拟机分组名称。
+ **Parent**
父虚拟机分组uuid。
+ **RefCount**
包含的虚拟机计数。

### PCIDevice
虚拟机PCI设备参数。
```
{
    "Domain" : Number,
    "Bus" : Number,
    "Slot" : Number,
    "Function" : Number
}
```

各项参数和宿主机描述PCI设备地址的参数一致。

### StartupSetting
TODO

### UnifiedComputeCreateRequest
TODO

### VmLog
虚拟机操作日志信息。
```
{
    "UUID" : String,
    "ObjectType" : String,
    "ObjectUUID" : String,
    "ObjectName" : String,
    "Ctime" : Number,
    "Message" : String,
    "StartTime" : Number,
    "EndTime" : Number
}
```

+ **UUID**  
日志uuid。
+ **ObjectType**  
操作类型。例如，虚拟机接口为"Compute"。
+ **ObjectUUID**  
操作对象uuid。在虚拟机接口里即虚拟机uuid。
+ **ObjectName**  
操作对象名称。在虚拟机接口里即虚拟机名称。
+ **Ctime**  
日志写入时间。精确到秒。
+ **Message**  
操作描述。
+ **StartTime**  
操作发起时间。精确到秒。
+ **EndTime**  
操作结束时间。精确到秒。

