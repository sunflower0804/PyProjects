# 命名规范
## 路由命名规范

* /api版本/资源/动作。 如`/v1/host/delete`
* /api版本/资源/子资源/.../动作。 如`/v1/host/vm/statistic`
* `/v1/network/switch/gateway/disconnect`
* 资源如果需要多个单词进行描述，则单词间采用`_`进行分隔。
* api需要传名称是用来写入操作日志，本身通过uuid识别
### 路由资源命名规范
* 虚拟机 vm
* 宿主机 host
* 镜像仓库  repository
* 网络 network
* 规格 specification
* 统一对象存储管理 usm
* 虚拟对象存储 vsm
* 统计 statistics
* 安全组  security_group
* 负载均衡器 load_balancer

### 部分常见参数命名
* cpu核数  cpu_cores
* 存储空间容量 storage_size
* 可用存储空间容量 available_storage_size
* 内存空间容量 memory_size
* 租户名 tenant_name
* 租户uuid tenant_uuid
* 用户名  user_name
* 数据硬盘 usd
* MAC地址  mac_address
* 创建时间 create_time
* 更新时间 update_time
* 虚拟ip  vip
* 内存统计 mem_statistics
* cpu统计 cpu_statistics
* 开始时间 start_time
* 结束时间 end_time

### 动作规范
#### 通用
* 获取资源详情：inspect
* 资源列表： list
* 删除资源:  delete
* 更新资源:  update，特殊更新资源视具体的动作而定。
* 创建资源: create 
* 打开dhcp：enable
* 关闭dhcp：disable

#### 特殊
** 待完善 **

    
## 请求参数命名规范
* 命名统一采用`小写字符+下划线(_)+小写字符`形式, 如`cluster_uuid`. 如有需要可以采用`小写字符+下划线(_)+小写字符+下划线(_)+小写字符`
* 命名必须准确。 如果需要用户传递租户名，使用"tenant_name"作为参数名。
    如果需要用户传递租户UUID, 使用"tenant_uuid"作为参数名。 
    * 除了常见的uuid,id,dns,等专有缩写名词外，尽可能不要使用缩写。如果有缩写，提交到文档，以告知。
* 有效字符: `a-z_`
* 不同api如果使用同样的资源的UUID作为参数，如host，统一使用host_uuid(举例), 不要在使用其他描述如physicalMachineUUID之类的。


## 回应参数命名规范
* 命名统一采用`小写字符+下划线(_)+小写字符`形式, 如`cluster_uuid`.
如有需要可以采用`小写字符+下划线(_)+小写字符+下划线(_)+小写字符`
* 命名必须准确。 如果返回租户名，使用"tenant_name"作为参数名。
    如果返回租户UUID, 使用"tenant_uuid"作为参数名。
   * 除了常见的uuid,id,dns,等专有缩写名词外，尽可能不要使用缩写。如果有缩写，提交到文档，以告知。
* 有效字符: `a-z_`


# HTTP请求规范
## HTTP请求规范
* 获取服务器资源： GET请求， 如获取资源详情，获取资源列表等
* 更改/删除服务器资源：POST请求， 如添加虚拟机，更改虚拟机名等

## HTTP请求通用头
```
Authorization："token"
Content-Type： "application/json"
```

## HTTP请求通用回应

### HTTP请求状态码
* 200：  操作成功与否，都一致返回200状态码。
* 404：  API路由未找到


### HTTP 200  状态码回应结构体
* status_code: 操作状态码，
    * 0: 成功
    * 非0: 失败
* message: 状态信息英文。
* message_cn: 状态信息中文
* stack: 状态码非0时，返回出错调用栈
* data: 操作结果，根据操作不同返回数据不同。

#### 请求成功示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "volume": {
      "tenant": "",
      "name": "",
      "uuid": "c7e3ffe3-b072-477e-a92b-8d01243530a9",
      "pool": "",
      "namespace": "",
      "capacity": 0,
      "snap_capacity": 0,
      "status": 0,
      "ctime": 0,
      "flag": 0
    }
  }
}
```
#### 请求失败示例
```
{
  "status_code": 10183,
  "message": "user not exist",
  "message_cn": "用户不存在",
  "stack": [
    "ip:192.168.122.1,pid:31823,bin:manager,code:10183,filename:model_user.go,func:ModifyPassword,line:226"
  ],
  "data": null
}
```

#### 操作状态码，中英文描述 http状态码
* 英文描述，首单词字母大写，其余小写

```
//待完善。
StatusCode   Description                 DescriptionCN        HTTP Status Code
10000       "Manager server error: %s"   "服务器出错: %s"       200
10001       "Parse parameter error: %s"  "参数解析出错: %s"     200
```

# 常见请求回应规范
### 常见回应列表
* total_count: 列表资源数量
* list: 资源列表
* 注意：资源列表返回的资源对象禁止存放可能无限增长的资源字段，如host中虚拟机列表等。
* list需要排序，1)创建时间 2)字符排序
```
{
    "total_count":"",
    "list": [],
}
```
### 批量

批量操作只返回成功。在data中包含批量任务成功失败状态。
```
{
  "status_code": 0,
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "success": 8,
    "fail": 2,
    "results":[
        {
            "status_code": 0,
            "message": "success",
            "message_cn": "成功",
            "stack": null,
            "data": {
                "host": "123aaaaa"
            }
        } ,
        {
            "status_code": 11000,
            "message": "User Not Exist",
            "message_cn": "用户不存在",
            "stack": [....],
            "data": {
                "host": "123aaaaa"
            }
        }  
    ]
  }
}
```

### 删除
* data中包含删除资源请求参数的信息
```
//示例：
{
    "tenant_uuid" : "178ab233-4406-4f94-ac18-7fcfc5995e64"
}

```


### 更新
* data返回更新资源的请求参数
```
//示例
{
  "tenant_uuid" : "178ab233-4406-4f94-ac18-7fcfc5995e64"  
}
```