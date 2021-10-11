[back to api overview](../api_overview.md#label_api)
### 租户相关接口
## /v1/tenant/list
租户列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
system|bool|否|false|是否显示系统租户
filter_name|string|否|-|过滤名称
page_num|int|否|0|第几页
page_size|int|否|0|每页数据条数

### 返回参数

名称|参数类型|描述
---|---|---
list|array|租户列表
latest_used_tenants|array|当前用户(调用这个接口的用户)最近使用过的租户

#### list对象
名称|参数类型|描述
---|---|---
name|string|租户名称
uuid|string|租户uuid
cluster_uuid|string|所在集群uuid
create_time|int64|创建时间
namespace|string|命名空间
user_num|int|租户下用户总数(包括租户管理员)
normal_user_num|int|租户下普通用户数(不包括包括租户管理员)
policy_num|int|角色数量
group_num|int|用户组数量
ldap_enabled|bool|是否启用LDAP服务
administrator|object|租户(管理员)信息
#### administrator对象
名称|参数类型|描述
---|---|---
uuid|string|租户(管理员)uuid
name|string|租户(管理员)名称
email|string|租户(管理员)邮箱
event_windows_popup_push|object|告警弹窗推送;1为最低级(提示)，4为最高级(紧急)
event_email_push|object|告警邮件推送;1为最低级(提示)，4为最高级(紧急)
phone|string|电话
description|string|描述
create_time|int64|创建时间
tenant|string|租户uuid
role|string|administrator为租户管理员
group|string|所在用户组
policys|array|用户角色uuid
default_cluster|string|默认集群
is_ldap|bool|是否为ldap用户
last_password_modify_time|int64|最近密码修改时间
#### latest_used_tenants对象
名称|参数类型|描述
---|---|---
name|string|租户名称
uuid|string|租户uuid
namespace|string|命名空间
### 示例

#### 请求示例
```
http://192.168.201.213:8080/v1/tenant/list?page_num=0&page_size=10&filter_name=gg_tenant01&system=true&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
        "name": "gg_tenant01",
        "uuid": "76373db8-e98d-4ad5-a373-9e9e4cd6048e",
        "cluster_uuid": "c5793204-f4ed-44ae-977a-63609adf2dcd",
        "create_time": 1572849656,
        "namespace": "76373db8-e98d-4ad5-a373-9e9e4cd6048e",
        "user_num": 5,
        "normal_user_num": 0,
        "policy_num": 1,
        "group_num": 4,
        "ldap_enabled": false,
        "administrator": {
          "uuid": "c1a746d7-7589-4e3e-a89e-3b1139d98cd4",
          "name": "gg_user_001",
          "email": "12@12.com",
          "event_windows_popup_push": {
            "push_level": 4,
            "push_enabled": true
          },
          "event_email_push": {
            "push_level": 4,
            "push_enabled": true
          },
          "phone": "",
          "description": "",
          "create_time": 1572849687,
          "tenant": "76373db8-e98d-4ad5-a373-9e9e4cd6048e",
          "role": "administrator",
          "group": "e48a4059-7542-48b4-8825-38d142c8888b",
          "policys": [
            "76373db8-e98d-4ad5-a373-9e9e4cd6048e"
          ],
          "default_cluster": "c5793204-f4ed-44ae-977a-63609adf2dcd",
          "is_ldap": false,
          "last_password_modify_time": 1572849687
        }
      }
    ],
    "latest_used_tenants": [
      {
        "name": "gg_tenant01",
        "uuid": "76373db8-e98d-4ad5-a373-9e9e4cd6048e",
        "namespace": "76373db8-e98d-4ad5-a373-9e9e4cd6048e"
      },
      {
        "name": "All",
        "uuid": "",
        "namespace": ""
      },
      {
        "name": "gg_tenant",
        "uuid": "2fd69493-5005-4a2e-9e60-f6923040a48d",
        "namespace": "2fd69493-5005-4a2e-9e60-f6923040a48d"
      }
    ],
    "total_count": 1
  }
}
```

#### 异常返回示例

### 状态码


## /v1/tenant/add
租户添加(会同时为该租户添加一个和租户同名的用户,即租户管理员)
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant|string|是|-|租户名称
password|string|是|-|租户密码
email|string|是|-|租户邮箱
phone|string|是|-|租户电话
quota|object|是|-|租户配额
cluster_uuid|string|是|-|集群
vm_screenshot_is_opened|bool|否|-|是否开启屏幕截图空间
vm_memory_snapshot_is_opened|bool|否|-|是否开启内存快照空间

### quota对象
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cpu_cores|uint32|是|-|cpu核数
memory_size|uint64|是|-|内存配额,单位字节
storage_size|uint64|是|-|存储配额,单位字节
switch_size|uint64|是|-|交换机配额,个数
router_size|uint64|是|-|路由配额,个数
gateway_size|uint64|是|-|网关配额,个数
vm_screenshot_is_opened|uint64|否|-|屏幕截图空间,单位字节
vm_memory_snapshot_is_opened|uint64|否|-|内存快照空间,单位字节

### 返回参数

名称|参数类型|描述
---|---|---
uuid|string|租户uuid

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/tenant/add
```
Body:
```
{
  "tenant": "zzz",
  "password": "21232f297a57a5a743894a0e4a801fc3",
  "email": "dsfsd@fed.com",
  "phone": "13611111111",
  "quota": {
    "cpu_cores": 50,
    "memory_size": 107374182400,
    "storage_size": 1099511627776,
    "switch_size": 1,
    "router_size": 1,
    "gateway_size": 1,
    "vm_screenshot_space": 1073741824,
    "vm_domain_memory_space": 10737418240
  },
  "vm_screenshot_is_opened": true,
  "vm_memory_snapshot_is_opened": true,
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
  "stack": null,
  "data": {
    "uuid": "315aa203-1965-4e89-b493-18f2baffbbf5"
  }
}
```

#### 异常返回示例

### 状态码


## /v1/tenant/delete
租户删除(系统租户system除外)
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
tenant_name|string|是|-|租户名称


### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/tenant/delete
```
Body:
```
{
  "tenant": "03a0012d-acca-47ec-b649-218127530af6",
  "tenant_name": "1111",
  "cluster_uuid": "185d4703-f815-47ef-94b7-1ae7ae0fc204"
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




## /v1/tenant/quota/get
租户配额获取
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid

### 返回参数

名称|参数类型|描述
---|---|---
quota|object|租户配额
available|object|剩余可用配额
SnapLength|uint64|快照已使用;单位G

#### quota对象
 名称 | 参数类型 |描述
--- |---|---|--- |---
cpu_cores|uint32|cpu核数
memory_size|uint64|内存配额,单位字节
storage_size|uint64|存储配额,单位字节
switch_size|uint64|交换机配额
router_size|uint64|路由配额
gateway_size|uint64|网关配额

#### available对象
 名称 | 参数类型 |描述
--- |---|---|--- |---
cpu_cores|uint32|cpu核数
memory_size|uint64|内存配额,单位字节
storage_size|uint64|存储配额,单位字节
switch_size|uint64|交换机配额
router_size|uint64|路由配额
gateway_size|uint64|网关配额

### 示例

#### 请求示例
```
http://192.168.201.213:8080/v1/tenant/quota/get?tenant=315aa203-1965-4e89-b493-18f2baffbbf5&cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
    "quota": {
      "cpu_cores": 50,
      "memory_size": 107374182400,
      "storage_size": 1099511627776,
      "gateway_size": 1,
      "router_size": 1,
      "switch_size": 10
    },
    "available": {
      "cpu_cores": 50,
      "memory_size": 107374182400,
      "storage_size": 1099511627776,
      "gateway_size": 1,
      "router_size": 0,
      "switch_size": 8
    },
    "SnapLength": 0
  }
}
```

#### 异常返回示例

### 状态码


## /v1/tenant/quota/update
租户配额更新(系统租户system除外)
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
tenant_name|string|是|-|租户名称
quota|object|是|-|租户配额
### quota对象
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cpu_cores|uint32|否|-|cpu核数
memory_size|uint64|否|-|内存配额,单位字节
storage_size|uint64|否|-|存储配额,单位字节
switch_size|uint64|否|-|交换机配额
router_size|uint64|否|-|路由配额
gateway_size|uint64|否|-|网关配额

### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/tenant/quota/update
```
Body:
```
{
  "tenant": "03a0012d-acca-47ec-b649-218127530af6",
  "tenant_name": "1111",
  "quota": {
    "cpu_cores": 50,
    "memory_size": 107374182400,
    "storage_size": 1099511627776,
    "gateway_size": 1,
    "router_size": 1,
    "switch_size": 10
  },
  "cluster_uuid": "185d4703-f815-47ef-94b7-1ae7ae0fc204"
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

## /v1/tenant/ldap/sync
租户LDAP同步账户
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
tenant|string|是|-|租户uuid
tenant_name|string|是|-|租户名称


### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://192.168.201.213:8080/v1/tenant/ldap/sync
```
Body:
```
{
	"tenant": "315aa203-1965-4e89-b493-18f2baffbbf5",
	"tenant_name": "api-test",
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

