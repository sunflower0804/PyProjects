[back to api overview](../api_overview.md#api)

# topology

## /v1/network/topology/node/move
#### 功能：更新网络拓扑节点信息
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid
 list|array|是|""  | 节点列表
 
 #### list对象
 名称|参数类型|描述 
--- |---|---|--- |---
 namespace|string|是|""  |名称空间
 parent_uuid|string|是|""  |父节点的uuid
 node_type|int32|是|""  |节点类型
 coordinate_x|int32|是|0  |横坐标
 coordinate_y|int32|是|0  |纵坐标

### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 list|array| 节点列表
 
 #### list对象
 名称|参数类型|描述 
--- |---|---
 namespace|string|名称空间
 parent_uuid|string| 父节点的uuid
 node_type|int32| 节点类型
 coordinate_x|int32| 横坐标
 coordinate_y|int32| 纵坐标

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/topology/node/move
```
Body:
```
{	
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "list": [
    {
        "namespace":"",
        "parent_uuid:"",
        "node_type": 1,
        "coordinate_x":100,
        "coordinate_y":100,
    },
    {
        "namespace":"",
        "parent_uuid:"",
        "node_type": 1,
        "coordinate_x":100,
        "coordinate_y":100,
    }
    
    ]
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "list": [
    {
        "namespace":"",
        "parent_uuid:"",
        "node_type": 1,
        "coordinate_x":100,
        "coordinate_y":100,
    },
    {
        "namespace":"",
        "parent_uuid:"",
        "node_type": 1,
        "coordinate_x":100,
        "coordinate_y":100,
    }
    
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/network/topology/get
#### 功能：获取网络拓扑图
#### 请求类型：GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|- | 租户uuid

### 返回参数
名称|参数类型|描述 
---|---|---
vms|TopoVM_object array| 虚拟机列表
gateways|TopoGateway_object array| 网关列表
switchs|TopoSwitch_object array| 交换机列表
routers|TopoRouter_object array| 路由器列表
links|Links_object array| 连接信息

### 示例
#### 请求示例
```
http://localhost:9990/v1/network/topology/get?tenant_uuid="4a7e240b-14aa-11e9-b0b9-5256ff003400"
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



## /v1/network/topology/node/add
#### 功能：添加游离的虚拟机节点
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|-  | 租户uuid
 uuid|string| 是|-  | 添加的虚拟机节点的uuid
 node_type|int32| 是|-  | 节点类型
 macs|[]string| 是|-  | mac地址
 coordinate_x|int32| 是|-  | 横坐标
 coordinate_y|int32| 是|-  | 纵坐标
 

### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 uuid|string| 添加的虚拟机节点的uuid
 node_type|int32| 节点类型
 macs|[]string| mac地址
 coordinate_x|int32| 横坐标
 coordinate_y|int32| 纵坐标

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/topology/node/add
```
Body:
```
{	
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400"
    "node_type": 1
    "coordinate_x": 100
    "coordinate_y": 100
    "macs": [
        "fe80::291c:95cd:52e4:7a07%23",
        "f280::291c:95cd:52e4:7a07%23"
    ]
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400"
    "node_type": 1
    "coordinate_x": 100
    "coordinate_y": 100
    "macs": [
        "fe80::291c:95cd:52e4:7a07%23",
        "f280::291c:95cd:52e4:7a07%23"
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/network/topology/node/delete
#### 功能：删除拓扑节点
#### 请求类型：POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 tenant_uuid|string| 是|""  | 租户uuid
 uuid|string| 是|""  | 删除的虚拟机节点的uuid
 node_type|int32| 是|0  | 节点类型
 

### 返回参数
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 uuid|string| 删除的虚拟机节点的uuid
 node_type|int32| 节点类型
 

### 示例

#### 请求示例
```
http://localhost:9990/v1/network/topology/node/delete
```
Body:
```
{	
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400"
    "node_type": 1
}
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
    "tenant_uuid": "4a7e240b-14aa-11e9-b0b9-5256ff003400"
    "parent_uuid": "55b2edab-14aa-11e9-b0b9-5256ff003400"
    "node_type": 1
  }
}
```

#### 异常返回示例

### 状态码







