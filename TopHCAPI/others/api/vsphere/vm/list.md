[back to api overview](../api_overview.md#api)

## /v1/vsphere/vm/list
虚拟机列表（虚拟机和模板）
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 vsphere_uuid|string| 是|-  | vsphere uuid
 filter_type|string|否|-|vm,template可选，筛选虚拟机和模板

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.25:9990/v1/vsphere/vm/list?vsphere_uuid=757a9afa-5a01-11e9-b9ab-5256fffab0f3&filter_type=vm
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
    "total_count": 5,
    "list": [
      {
        "vm_name": "Debian GNU_Linux 10 (1)",
        "vm_reference": "VirtualMachine:vm-23"
      },
      {
        "vm_name": "dd",
        "vm_reference": "VirtualMachine:vm-329"
      },
      {
        "vm_name": "vm_040102",
        "vm_reference": "VirtualMachine:vm-398"
      },
      {
        "vm_name": "新建虚拟机",
        "vm_reference": "VirtualMachine:vm-393"
      },
      {
        "vm_name": "vm_040108",
        "vm_reference": "VirtualMachine:vm-396"
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码