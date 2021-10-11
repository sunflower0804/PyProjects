[back to api overview](../api_overview.md#label_api)
### 虚拟机组相关接口
## /v1/compute/group/create
虚拟机组添加
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
group_name|string|是|-|组名称
parent_group|string|否|-|父组uuid,表示创建在哪层,不填表示第一层

### 返回参数

名称|参数类型|描述
---|---|---
TODO
### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/compute/group/create
```
Body:
```
{
	"tenant": "8b1d51a9-117e-4456-ab35-9fb47288cbce",
	"group_name": "group1",
	"parent_group": null,
	"cluster_uuid": "e12b4f57-e3f0-4f93-83da-76ce1eda8595"
}
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
    "Metadata": {
      "UUID": "f2f198b9-bbf8-4363-81b0-c8b30dc478eb",
      "Namespace": "8b1d51a9-117e-4456-ab35-9fb47288cbce",
      "Name": "group1",
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

#### 异常返回示例

### 状态码


## /v1/compute/group/delete
虚拟机组删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
group_name|string|是|-|组名称
group_uuid|string|是|-|组uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO
### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/compute/group/delete
```
Body:
```
{
	"tenant": "8b1d51a9-117e-4456-ab35-9fb47288cbce",
	"group_name": "rrr",
	"group_uuid": "2a2bda08-081b-46b0-bdb3-4b4b3e47e909",
	"cluster_uuid": "e12b4f57-e3f0-4f93-83da-76ce1eda8595"
}
```

#### 正常返回示例
```
{
  "message": "success",
  "message_cn": "成功",
  "scode": 0,
  "desc": "",
  "stack": null,
  "data": {}
}
```

#### 异常返回示例

### 状态码

## /v1/compute/group/update
虚拟机组更新(修改组名)
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
group_name|string|是|-|组名称
group_uuid|string|是|-|组uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO
### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/compute/group/update
```
Body:
```
{
	"tenant": "8b1d51a9-117e-4456-ab35-9fb47288cbce",
	"group_name": "group11",
	"group_uuid": "f2f198b9-bbf8-4363-81b0-c8b30dc478eb",
	"cluster_uuid": "e12b4f57-e3f0-4f93-83da-76ce1eda8595"
}
```

#### 正常返回示例
```
{
  "message": "success",
  "message_cn": "成功",
  "scode": 0,
  "desc": "",
  "stack": null,
  "data": {}
}
```

#### 异常返回示例

### 状态码



### /v1/compute/group/tree
虚拟机组树状图,最外层为租户不能选;如下面返回结果,虚拟机可添加在group11或default组下
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|否|-|租户uuid

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://10.30.12.89:8080/v1/compute/group/tree?tenant=8b1d51a9-117e-4456-ab35-9fb47288cbce&filter_type=1&cluster_uuid=e12b4f57-e3f0-4f93-83da-76ce1eda8595
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
    "list": [
      {
        "UUID": "8b1d51a9-117e-4456-ab35-9fb47288cbce",
        "Namespace": "8b1d51a9-117e-4456-ab35-9fb47288cbce",
        "Name": "zhanghai",
        "Desc": "",
        "Parent": "",
        "Attrs": null,
        "RefCount": 0,
        "Children": [
          {
            "UUID": "e39ccc64-b6cd-48b3-9b79-7257ed8efde0",
            "Namespace": "8b1d51a9-117e-4456-ab35-9fb47288cbce",
            "Name": "default",
            "Desc": "",
            "Parent": "8b1d51a9-117e-4456-ab35-9fb47288cbce",
            "Attrs": null,
            "RefCount": 2,
            "Children": [],
            "fake": false,
            "deny_child_create": false
          },
          {
            "UUID": "f2f198b9-bbf8-4363-81b0-c8b30dc478eb",
            "Namespace": "8b1d51a9-117e-4456-ab35-9fb47288cbce",
            "Name": "group11",
            "Desc": "",
            "Parent": "8b1d51a9-117e-4456-ab35-9fb47288cbce",
            "Attrs": null,
            "RefCount": 0,
            "Children": [],
            "fake": false,
            "deny_child_create": false
          }
        ],
        "fake": true,
        "deny_child_create": false
      }
    ],
    "total_count": 1
  }
}
```

#### 异常返回示例

### 状态码

## /v1/compute/group/move
虚拟机组移动
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
group_name|string|是|-|组名称
group_uuid|string|是|-|组uuid
parent_group|string|是|-|父组uuid,表示移动到哪层

### 返回参数

名称|参数类型|描述
---|---|---
TODO
### 示例

#### 请求示例
```
http://192.168.201.211:8080/v1/compute/group/move
```
Body:
```
{
	"tenant": "8b1d51a9-117e-4456-ab35-9fb47288cbce",
	"group_name": "cccc",
	"parent_group": "0b647649-0f53-4bc0-8510-4ac95d1901a5",
	"group_uuid": "94265d44-fc43-4f73-8b59-d03f9c3fd2ae",
	"cluster_uuid": "e12b4f57-e3f0-4f93-83da-76ce1eda8595"
}
```

#### 正常返回示例
```
{
  "message": "success",
  "message_cn": "成功",
  "scode": 0,
  "desc": "",
  "stack": null,
  "data": {}
}
```

#### 异常返回示例

### 状态码

