
[back to api overview](../api_overview.md#api)

# host


## /v1/deploy/host/init
#### 功能：部署：初始化主机
#### 请求类型：POST

### 请求参数
 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 host_ip|string| 是|- | 主机ip
 host_name|string| 是|-  | 主机名称
 manage_network|[NetWorkInfo_object](host.md#NetWorkInfo_object)| 是|-  | 管理网络配置
 compute_network|[NetWorkInfo_object](host.md#NetWorkInfo_object)| 否|-  | 计算网络配置
 storage_network|[NetWorkInfo_object](host.md#NetWorkInfo_object)| 否|-  | 存储网络配置
 backup_network|[NetWorkInfo_object](host.md#NetWorkInfo_object)| 否|-  | 备份网络配置

#### NetWorkInfo_object
 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 network_name|string| 是|- | 网络名称
 network_ip|[]string| 是|- | ip列表
 network_eths|string| 是|- | 网卡列表

### 返回参数
名称|参数类型|描述 
---|---|---
 host_ip|string| 主机ip
 host_name|string| 主机名称
 manage_network|[NetWorkInfo_object](host.md#NetWorkInfo_object)| 管理网络配置
 compute_network|[NetWorkInfo_object](host.md#NetWorkInfo_object)| 计算网络配置
 storage_network|[NetWorkInfo_object](host.md#NetWorkInfo_object)| 存储网络配置
 backup_network|[NetWorkInfo_object](host.md#NetWorkInfo_object)| 备份网络配置


### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/deploy/host/init
```
Body:
```
{	
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



## /v1/deploy/host/network_card/inspect
#### 功能：获取主机网卡信息
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 host_ip|string| 是|""  | 主机ip

### 返回参数
名称|参数类型|描述 
---|---|---
host_ip|string|主机ip
host_name|string|主机名称
manage_net|[NetConfig_object](host.md#NetConfig_object)|管理网络信息
compute_net|[NetConfig_object](host.md#NetConfig_object)|计算网络信息
storage_net|[NetConfig_object](host.md#NetConfig_object)|存储网络信息
backup_net|[NetConfig_object](host.md#NetConfig_object)|备份网络信息
net_bonds|[NetBonding](host.md#NetBonding) array|网卡绑定信息

#### NetConfig_object
名称|参数类型|描述
---|---|---
network_card_name|string|网卡名称
network_card_addrs|[]string|网卡地址列
mtu|int32|最大传输单元


#### NetBonding
名称|参数类型|描述
---|---|---
NetBond_name|string|网卡绑定集合的名称
mode|string|
slaves|[]string|
addrs|[]string|集合中所有的ip地址
mtu|int64|最大传输单元


### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/deploy/host/network_card/inspect
```
Body:
```
{	
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


## /v1/deploy/host/scan 
#### 功能：主机扫描
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 begin_ip|string| 是|""  | 开始ip
 end_ip|string| 是|""  | 结束ip

### 返回参数
名称|参数类型|描述 
---|---|---
total_count|int|总数量
list|HostsInfo_object array|主机信息列表

#### HostsInfo_object 对象
名称|参数类型|描述
---|---|---
host_ip|string|主机ip
host_name|string|主机的名称
cluster_uuid|string|主机所属的集群的uuid
type|string|主机类型
host_info|[HostInfo_object](host.md#HostInfo_object)|主机信息
cpu_info|[CpuInfo_object](host.md#CpuInfo_object)|cpu信息
memory_info|[MemoryInfo_object](host.md#MemoryInfo_object)|内存信息
network_info|[NetworkInfo_object](host.md#NetworkInfo_object)|网络信息
disk_info|[DiskInfo_object](host.md#DiskInfo_object)|磁盘信息

#### HostInfo_object
名称|参数类型|描述
---|---|---
host_name|string|主机名
update_time|uint64|更新时间
boot_time|uint64|启动时间
procs|uint64|
os|string|操作系统
platform|string|
platform_family|string|
platform_version|string|
kernel_version|string|内核版本
virtualization_system|string|
virtualization_role|string|
host_id|string|主机id

#### CpuInfo_object
名称|参数类型|描述
---|---|---
model|string|主机名
model_name|string|主机名
cores|int32|多少cpu
sockets|int32|套接字
mhz|string|
used|string|使用率
system|string|
idle|string|空闲率
nice|string|
iowait|string|io延时
irq|string|
softirq|string|

#### MemoryInfo_object
名称|参数类型|描述
---|---|---
total|uint64|总内存大小
available|uint64|是可使用内存
used|uint64|已使用内存
free|uint64|空闲内存
buffers|uint64|
cached|uint64|
ksm|uint64|

#### NetworkInfo_object
名称|参数类型|描述
---|---|---
nbi|Nbi_object|所有的网卡列表

#### Nbi_object 对象
名称|参数类型|描述
---|---|---
mac|string|网卡mac地址
bandwith|int64|string|网络带宽
mtu|int64|最大传输单元
status|string|网卡状态
network_card_name|string|网卡名称
wiops|uint64|
riops|uint64|
wmbps|uint64|
rmbps|uint64|
errin|uint64|
errout|uint64|
dropin|uint64|
dropout|uint64|


#### DiskInfo_object
名称|参数类型|描述
---|---|---
dbi|Dbi_object array|

#### Dbi_object 对象
名称|参数类型|描述
---|---|---
path|string|
type|string|
total|uint64|
riops|uint64|
wiops|uint64|
rspeed|uint64|
wspeed|uint64|
riowait|uint64|
siowait|uint64|
light_on|bool|

### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/deploy/host/scan
```
Body:
```
{	
}
```


#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "ns": "hhh",
  }
}
```

#### 异常返回示例
### 状态码


## /v1/deploy/host/inspect
#### 功能：获取单个主机的信息
#### 请求类型：  GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 host_ip|string| 是|""  | 主机ip

### 返回参数
名称|参数类型|描述 
---|---|---
host_ip|string|主机ip
host_name|string|主机的名称
cluster_uuid|string|主机所属的集群的uuid
type|string|主机类型
host_info|[HostInfo_object](host.md#HostInfo_object)|主机信息
cpu_info|[CpuInfo_object](host.md#CpuInfo_object)|cpu信息
memory_info|[MemoryInfo_object](host.md#MemoryInfo_object)|内存信息
network_info|[NetworkInfo_object](host.md#NetworkInfo_object)|网络信息
disk_info|[DiskInfo_object](host.md#DiskInfo_object)|磁盘信息


### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/deploy/host/inspect
```
Body:
```
{	
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

