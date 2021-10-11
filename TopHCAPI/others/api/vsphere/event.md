
##  /v1/vsphere/event/root/list
#### 功能：获取vsphere集群下的所有事件
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
vsphere_uuid |string|是|-|vsphere集群uuid
filter_name|string|否|- |过滤字符串
page_num | int|否|0 |翻页偏移量
page_size | int|否|0 |每页的限制数量

### 返回参数
名称|参数类型|描述
---|---|---
TotalCount|int|总数
List|struct array|事件列表

### List 对象
Category|string|类别
Description|string|描述
Time|int64|事件时间
User|string|用户

### 示例

#### 请求示例
```
http://10.30.12.184:8080/v1/vsphere/event/root/list?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&page_num=0&
page_size=10&filter_name=&cluster_uuid=52601d51-7b60-4e16-8c77-cedf08056c91
```
Body:
```

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
    "total_count": 1000,
    "list": [
      {
        "category": "info",
        "description": "硬件传感器状态: 处理器 green，内存 green，风扇 red，电压 green，温度 green，功率 red，系统主板 green，电池 green，存储 green，其他 green",
        "time": 1630390959,
        "user": "System"
      },
      {
        "category": "info",
        "description": "硬件传感器状态: 处理器 green，内存 green，风扇 red，电压 green，温度 green，功率 red，系统主板 green，电池 green，存储 green，其他 green",
        "time": 1630390866,
        "user": "System"
      },
      {
        "category": "info",
        "description": "硬件传感器状态: 处理器 green，内存 green，风扇 red，电压 green，温度 green，功率 red，系统主板 green，电池 green，存储 green，其他 green",
        "time": 1630390773,
        "user": "System"
      },
      {
        "category": "info",
        "description": "硬件传感器状态: 处理器 green，内存 green，风扇 red，电压 green，温度 green，功率 red，系统主板 green，电池 green，存储 green，其他 green",
        "time": 1630390681,
        "user": "System"
      },
      {
        "category": "info",
        "description": "硬件传感器状态: 处理器 green，内存 green，风扇 red，电压 green，温度 green，功率 red，系统主板 green，电池 green，存储 green，其他 green",
        "time": 1630390588,
        "user": "System"
      },
      {
        "category": "info",
        "description": "硬件传感器状态: 处理器 green，内存 green，风扇 red，电压 green，温度 green，功率 red，系统主板 green，电池 green，存储 green，其他 green",
        "time": 1630390495,
        "user": "System"
      },
      {
        "category": "info",
        "description": "硬件传感器状态: 处理器 green，内存 green，风扇 red，电压 green，温度 green，功率 red，系统主板 green，电池 green，存储 green，其他 green",
        "time": 1630390403,
        "user": "System"
      },
      {
        "category": "info",
        "description": "硬件传感器状态: 处理器 green，内存 green，风扇 red，电压 green，温度 green，功率 red，系统主板 green，电池 green，存储 green，其他 green",
        "time": 1630390310,
        "user": "System"
      },
      {
        "category": "info",
        "description": "硬件传感器状态: 处理器 green，内存 green，风扇 red，电压 green，温度 green，功率 red，系统主板 green，电池 green，存储 green，其他 green",
        "time": 1630390217,
        "user": "System"
      },
      {
        "category": "info",
        "description": "硬件传感器状态: 处理器 green，内存 green，风扇 red，电压 green，温度 green，功率 red，系统主板 green，电池 green，存储 green，其他 green",
        "time": 1630390125,
        "user": "System"
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


##  /v1/vsphere/event/resource/list
#### 功能：获取vsphere指定资源的事件
#### 请求类型：get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
vsphere_uuid |string|是|-|vsphere集群uuid
filter_name|string|否|- |过滤字符串
page_num | int|否|0 |翻页偏移量
page_size | int|否|0 |每页的限制数量
reference|string|是|- |(主机、数据中心、数据存储、虚拟机)reference

### 返回参数
名称|参数类型|描述
---|---|---
TotalCount|int|总数
List|struct array|事件列表

### List 对象
Category|string|类别
Description|string|描述
Time|int64|事件时间
User|string|用户

### 示例

#### 请求示例
```
http://10.30.12.184:8080/v1/vsphere/event/resource/list?vsphere_uuid=e0fd06e7-b891-4fca-ad56-e36981bee2a3&page_num=0&reference=VirtualMachine:vm-119&
page_size=10&filter_name=&cluster_uuid=52601d51-7b60-4e16-8c77-cedf08056c91
```
Body:
```

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
    "total_count": 500,
    "list": [
      {
        "category": "信息",
        "description": "任务: 设置控制台窗口的屏幕分辨率",
        "time": 1630396630,
        "user": "VSPHERE.LOCAL\\Administrator"
      },
      {
        "category": "信息",
        "description": "任务: 设置控制台窗口的屏幕分辨率",
        "time": 1630396628,
        "user": "VSPHERE.LOCAL\\Administrator"
      },
      {
        "category": "信息",
        "description": "已获得 TopSecDC 中的 10.30.40.11 上的类型为 webmks 的 ActiveDirectory 的票证",
        "time": 1630396628,
        "user": "VSPHERE.LOCAL\\Administrator"
      },
      {
        "category": "信息",
        "description": "已在 TopSecDC 中的 10.30.40.11 上重新配置 ActiveDirectory。  \n \n已修改:  \n \n 已添加:  \n \n 已删除:  \n \n",
        "time": 1630396528,
        "user": "VSPHERE.LOCAL\\Administrator"
      },
      {
        "category": "信息",
        "description": "任务: 重新配置虚拟机",
        "time": 1630396528,
        "user": "VSPHERE.LOCAL\\Administrator"
      },
      {
        "category": "info",
        "description": "在 TopSecDC 中群集 10.30.40.11 中的 10.30.40.11 上已成功整合虚拟机 ActiveDirectory 磁盘。",
        "time": 1630396516,
        "user": "VSPHERE.LOCAL\\Administrator"
      },
      {
        "category": "信息",
        "description": "任务: 创建虚拟机快照",
        "time": 1630396465,
        "user": "VSPHERE.LOCAL\\Administrator"
      },
      {
        "category": "信息",
        "description": "任务: 移除快照",
        "time": 1630396464,
        "user": "VSPHERE.LOCAL\\Administrator"
      },
      {
        "category": "信息",
        "description": "已在 TopSecDC 中的 10.30.40.11 上重新配置 ActiveDirectory。  \n \n已修改:  \n \n 已添加:  \n \n 已删除:  \n \n",
        "time": 1630392924,
        "user": "VSPHERE.LOCAL\\Administrator"
      },
      {
        "category": "信息",
        "description": "任务: 重新配置虚拟机",
        "time": 1630392924,
        "user": "VSPHERE.LOCAL\\Administrator"
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码