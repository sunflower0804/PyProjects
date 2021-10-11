[back to api overview](../api_overview.md#api)

## /v1/vsphere/w/list
文件夹列表（Folder:group-d1为根目录，在文件夹列表中没有；）
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
vsphere_uuid|string| 是|-| vsphere集群uuid
filter_datacenter_reference|string| 否|-|用来指定在哪个数据中心下的文件夹
filter_folder_type|string| 否|-|文件夹类型（该文件夹是用来添加虚拟机的还是其他的）vm,host,datastore,network可选；没指定数据中心时，此字段不生效


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.25:9990/v1/vsphere/folder/list?vsphere_uuid=d88958c0-4a1a-11e9-aded-5256ff006a00&filter_datacenter_reference=Datacenter%3Adatacenter-2&filter_folder_type
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
    "total_count": 19,
    "list": [
      {
        "folder_name": "vm",
        "folder_reference": "Folder:group-v195"
      },
      {
        "folder_name": "vm",
        "folder_reference": "Folder:group-v3"
      },
      {
        "folder_name": "network031201",
        "folder_reference": "Folder:group-n83"
      },
      {
        "folder_name": "已发现虚拟机",
        "folder_reference": "Folder:group-v21"
      },
      {
        "folder_name": "qqq",
        "folder_reference": "Folder:group-d429"
      },
      {
        "folder_name": "数据存储群集",
        "folder_reference": "StoragePod:group-p273"
      },
      {
        "folder_name": "vm",
        "folder_reference": "Folder:group-v425"
      },
      {
        "folder_name": "datacenter_folder_032701",
        "folder_reference": "Folder:group-n322"
      },
      {
        "folder_name": "datastore",
        "folder_reference": "Folder:group-s197"
      },
      {
        "folder_name": "network",
        "folder_reference": "Folder:group-n198"
      },
      {
        "folder_name": "network",
        "folder_reference": "Folder:group-n6"
      },
      {
        "folder_name": "host",
        "folder_reference": "Folder:group-h426"
      },
      {
        "folder_name": "datastore",
        "folder_reference": "Folder:group-s427"
      },
      {
        "folder_name": "folder_031901",
        "folder_reference": "Folder:group-d193"
      },
      {
        "folder_name": "host",
        "folder_reference": "Folder:group-h4"
      },
      {
        "folder_name": "datastore",
        "folder_reference": "Folder:group-s5"
      },
      {
        "folder_name": "host_cluster",
        "folder_reference": "Folder:group-h346"
      },
      {
        "folder_name": "network",
        "folder_reference": "Folder:group-n428"
      },
      {
        "folder_name": "host",
        "folder_reference": "Folder:group-h196"
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码