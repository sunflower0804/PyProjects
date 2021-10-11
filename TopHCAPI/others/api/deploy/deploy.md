[back to api overview](../api_overview.md#api)

# deploy


## /v1/deploy/vm/setup
#### 功能：拉起虚拟机
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 vm_type|string| 是|- | 虚拟机类型
 vm_infos|[VmInfos_object](deploy.md#VmInfos_object)|是| - |要创建个虚拟机的信息
 
 #### VmInfos_object
 host_ip|string| 是|- | 主机ip
 host_name|string| 是|-  | 主机名称
 manage_network|[NetWorkInfo_object](deploy.md#NetWorkInfo_object)| 是|-  | 管理网络配置
 compute_network|[NetWorkInfo_object](deploy.md#NetWorkInfo_object)| 否|-  | 计算网络配置
 storage_network|[NetWorkInfo_object](deploy.md#NetWorkInfo_object)| 否|-  | 存储网络配置
 backup_network|[NetWorkInfo_object](deploy.md#networkinfo_object)| 否|-  | 备份网络配置

#### NetWorkInfo_object
 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 host_ip|string| 是|- | 宿主机ip
 vm_ip|string| 是|- | 虚拟机的ip
 netmask|string| 是|- | 子网掩码
 gateway|string| 是|- | 网关
 

### 返回参数
名称|参数类型|描述 
---|---|---
 vm_type|string|  虚拟机类型
 vm_infos|VmInfos_object array|要创建个虚拟机的信息
 
 #### VmInfos_object 对象
 名称|参数类型|描述
 ---|---|---
 host_ip|string|宿主机ip
 vm_ip|string|虚拟机的ip
 netmask|string|子网掩码
 gateway|string|网关



### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/deploy/vm/setup
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



## /v1/deploy/cluster/setup
#### 功能：拉起集群
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 ips|[]string| 是|""  | 要组成集群的虚拟机ip


### 返回参数
名称|参数类型|描述 
---|---|---
ips|[]string| 要组成集群的虚拟机ip


### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/deploy/cluster/setup
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


## /v1/deploy/cluster/create
#### 功能：部署模式下添加集群
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 manager_ip|string| 是|""  | 已经部署的集群的某一个节点的ip
 target_ip|string| 是|""  | 要添加的集群的某个节点的ip
 cluster_name|string| 是|""  | 集群名称
 cluster_desc|string| 否|""  | 集群描述信息

### 返回参数
名称|参数类型|描述 
---|---|---
 manager_ip|string|  已经部署的集群的某一个节点的ip
 target_ip|string| 要添加的集群的某个节点的ip
 cluster_name|string| 集群名称
 cluster_desc|string| 集群描述信息


### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/deploy/cluster/create
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




