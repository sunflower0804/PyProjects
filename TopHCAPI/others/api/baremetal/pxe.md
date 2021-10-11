## /v1/cluster/deploy/pxe_service/vm
#### 功能：pxe服务器创建
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid| string| 是|- | 集群uuid
 manage_cidr| string| 是|- | pxe服务器管理网络cird
 ManageGateway| string| 是|- | pxe服务器管理网络网关
 domain_uuid| string| 是|- | 所属域
 pxe_netwok_uuid| string| 是|- | pxe服务器二层网桥uuid
 PxePgUUID| string| 是|- | pxe服务器二层网桥端口组uuid
 l2_network_name| string| 是|- | pxe服务器二层网桥端口名称
 pxe_server_cidr| string| 是|- | pxe服务器服务网络cird
 pxe_gateway| string| 是|- | pxe服务器服务网络网关
 pxe_start_ipaddr| string| 是|- | pxe服务器dhcp地址池起始网络
 pxe_ending_ipaddr| string| 是|- | pxe服务器dhcp地址池结束网络


### 返回参数
 名称|参数类型|描述
 ---|---|---



### 示例

#### 请求示例
```
http://localhost:9990/v1/cluster/deploy/pxe_service/vm
```

```
Body
```
{
	"cluster_uuid": "650ea11b-b7fb-4269-8232-aa53865aab3b",
	"manage_cidr": "10.30.142.120/24",
	"manage_gateway": "10.30.10.1",
	"domain_uuid": "a2f57b31-573e-4af3-9ae9-688706bc0db9",
	"pxe_netwok_uuid": "df7b7082-1687-4b27-ad84-91d099c1d12c",
	"pxe_pg_uuid": "439d8d6a-9a83-4884-a7d8-5a312d6495aa",
	"pxe_server_cidr": "10.30.97.12/24",
	"pxe_start_ipaddr": "10.30.97.2",
	"pxe_ending_ipaddr": "10.30.97.3",
	"pxe_gateway": "10.30.97.1",
	"l2_network_name": "dsfwd"
}

#### 正常返回示例
```
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

#### 异常返回示例

### 状态码


## /v1/cluster/pxe_service/vm/list
#### 功能：pxe服務器列表
#### 请求类型：Get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid| string| 是|- | 集群uuid
 filter_ip| string| 否|- | pxe服务器Ip


### 返回参数
 名称|参数类型|描述
 ---|---|---



### 示例

#### 请求示例
```
http://localhost:9990/v1/cluster/pxe_service/vm/list?cluster_uuid=&&filter_ip
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
    "infos": [
      {
        "UUID": "3e0e463f-d4f0-4236-8f92-27ddaf20aadb",
        "ManagerIP": "10.30.37.215/20",
        "MnGateway": "",
        "Pxe": {
          "PxeServerIP": "10.30.97.250/24",
          "PxeStartIP": "10.30.97.251",
          "PxeEndingIP": "10.30.97.254",
          "PxeGateway": "10.30.97.1",
          "PxeNetworkUUID": "",
          "PxePgUUID": "fa6c214f-9bfc-4b18-9a70-0940f2fa105f"
        },
        "DomainUUID": "9ca2f65b-ab91-42ea-8ae1-962668f4d82d",
        "ImportState": 4,
        "ImportProgress": 100,
        "ImportMachine": "",
        "VmUUID": "3e0e463f-d4f0-4236-8f92-27ddaf20aadb",
        "CTime": 1628757183,
        "MTime": 1629873931,
        "NsUUID": "39c8d859-4322-4a99-837b-f7c32bc1a194",
        "DomainName": "Domain23",
        "HostUUID": "debd3e19-32a2-4b4b-9534-a70a36ec9dce",
        "DhcpInfo": {
          "UUID": "bd92895c-afc9-4695-9173-92546396afc9",
          "Mode": 2,
          "Used": null,
          "Ctime": 1628757170,
          "Mtime": 1629873931,
          "IpaddrRange": {
            "StartIp": "10.30.97.251",
            "EndIp": "10.30.97.254",
            "Mask": "",
            "Gateway": "",
            "DNSServer": "",
            "DhcpServer": "",
            "Mtu": 0
          },
          "Cidr": null,
          "UsedIpInfoList": null,
          "HostCount": 4,
          "StartIpDecimal": 169763323,
          "EndIpDecimal": 169763326,
          "UserAssignIpInfoList": null,
          "TimeZone": "",
          "DhcpHostIp": ""
        },
        "HostIp": "",
        "Status": 1,
        "CPUInfo": null,
        "memoryInfo": null,
        "NetworkCardInfo": null,
        "NoneDiskClients": 0,
        "BMHosts": 1
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/cluster/pxe_service/vm/delete
#### 功能：pxe服務器删除
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid| string| 是|- | 集群uuid
 filter_ip| string| 是|- | pxe服务器Ip


### 返回参数
 名称|参数类型|描述
 ---|---|---


### 示例

#### 请求示例
```
http://localhost:9990/v1/cluster/pxe_service/vm/delete
```

{
	"cluster_uuid": "650ea11b-b7fb-4269-8232-aa53865aab3b",
	"uuid": "4c3a8c69-82e9-4414-9e4b-0f009f62a553",
	"force": true
}

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
    "infos": []
  }
}
```

#### 异常返回示例

### 状态码

## /v1/cluster//pxe_service/file/upload
#### 功能：pxe服务器上传文件
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 cluster_uuid| string| 是|- | 集群uuid
 filter_ip| string| 是|- | pxe服务器Ip

需要一个gz.tar文件， myfile

### 返回参数
 名称|参数类型|描述
 ---|---|---



### 示例

#### 请求示例
```
http://localhost:9990/v1/pxe_service/file/upload

{
	"cluster_uuid": "650ea11b-b7fb-4269-8232-aa53865aab3b",
	"pxe_ip": "10.30.12.39",
}

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