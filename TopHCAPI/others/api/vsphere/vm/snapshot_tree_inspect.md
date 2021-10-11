[back to api overview](../api_overview.md#api)

## /v1/vsphere/vm/snapshot/tree/inspect
获取虚拟机快照树
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 vsphere_uuid|string| 是|-  | vsphere uuid
 vm_reference|string|是|-|虚拟机的唯一标识

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.25:9990/v1/vsphere/vm/snapshot/tree/inspect?vsphere_uuid=e0a133e7-4568-11e9-8ea8-5256ff006a00&vm_reference=VirtualMachine%3Avm-41
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
    "CurrentSnapshot": {
      "Type": "VirtualMachineSnapshot",
      "Value": "snapshot-123"
    },
    "RootSnapshotList": [
      {
        "Snapshot": {
          "Type": "VirtualMachineSnapshot",
          "Value": "snapshot-87"
        },
        "Vm": {
          "Type": "VirtualMachine",
          "Value": "vm-41"
        },
        "Name": "虚拟机快照 2019%252f3%252f12 下午8:31:23",
        "Description": "",
        "Id": 1,
        "CreateTime": "2019-03-12T12:32:09.393437Z",
        "State": "poweredOff",
        "Quiesced": false,
        "BackupManifest": "",
        "ChildSnapshotList": [
          {
            "Snapshot": {
              "Type": "VirtualMachineSnapshot",
              "Value": "snapshot-123"
            },
            "Vm": {
              "Type": "VirtualMachine",
              "Value": "vm-41"
            },
            "Name": "snapshot_031501",
            "Description": "",
            "Id": 2,
            "CreateTime": "2019-03-15T11:01:19.040187Z",
            "State": "poweredOff",
            "Quiesced": false,
            "BackupManifest": "",
            "ChildSnapshotList": null,
            "ReplaySupported": false
          }
        ],
        "ReplaySupported": false
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码