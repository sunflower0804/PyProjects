[back to api overview](../api_overview.md#api)

# network_vm

## /v1/deploy/network_vm/inspect
#### 功能：获取网络虚拟机信息
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 cluster_uuid|string| 是|""  | 集群uuid
 vm_ip|string| 是|""  | 网络虚拟机ip

### 返回参数
名称|参数类型|描述 
---|---|---
enable|bool|是否启动
vm_ip|string|网络虚拟机ip


### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/deploy/network_vm/inspect
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


## /v1/deploy/network_vm/update
#### 功能：更新网络虚拟机状态
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 cluster_uuid|string| 是|-  | 集群uuid
 is_enable|bool| 是|-  | 是否启动网络虚拟机
 vm_ip|string| 是|-  | 网络虚拟机ip

### 返回参数
名称|参数类型|描述 
---|---|---
 cluster_uuid|string| 是|-  | 集群uuid
 is_enable|bool| 是|-  | 是否启动网络虚拟机
 vm_ip|string| 是|-  | 网络虚拟机ip

### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/network_vm/update
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


