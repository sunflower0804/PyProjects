[back to api overview](../api_overview.md#label_api)

### license相关接口
## /v1/license/get
集群license信息获取
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|
### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.212:8080/v1/license/get?cluster_uuid=c5793204-f4ed-44ae-977a-63609adf2dcd
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
    "status": {
      "code": 0,
      "message": "",
      "messageCn": "",
      "stack": null,
      "desc": "",
      "UUID": ""
    },
    "license": {
      "encryptKey": "",
      "encryptedLicense": "",
      "CTime": 1572570444,
      "MTime": 1572570444,
      "license": {
        "CLUSTER_UUID": "00000000-0000-0000-0000-000000000000",
        "COMPUTE": "enable",
        "COPYRIGHT": "TOPSEC",
        "CUSTOM_NAME": "TOPSEC",
        "GATEWAY": "enable",
        "INCREASE": "false",
        "NETWORK": "enable",
        "PHYSICAL_CPU_NUM": "50",
        "PRODUCT": "NGFW4000-UF(TG-41308)",
        "PRODUCT_SESSION": "1000000",
        "PSN": "K1101054297",
        "ROUTER": "enable",
        "SECURITY_GROUP": "enable",
        "SERIALNO": "xxxxxxxxxxxx.001",
        "STORAGE": "enable",
        "STORAGE_CAPACITY": "9999T",
        "SWITCH": "enable",
        "TOPHCI_EXPIRE": "2019-12-31",
        "TOPHCI_TRY_EXPIRE": "2019-04-16",
        "USD_AUTH_TYPE": "NONE",
        "VDFW": "enable",
        "VGATE": "enable"
      }
    }
  }
}
```

#### 异常返回示例

### 状态码


## /v1/license/add
集群激活license
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TODO


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/license/add
```
Body:
```
{
	"tenant": "2fd69493-5005-4a2e-9e60-f6923040a48d",
	"encrypted_license": "5t3fd3tef5ye",
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
  "data": {
    "status": {
      "code": 0,
      "message": "",
      "messageCn": "",
      "stack": null,
      "desc": "",
      "UUID": ""
    },
    "license": {
      "encryptKey": "",
      "encryptedLicense": "",
      "CTime": 1572570444,
      "MTime": 1572570444,
      "license": {
        "CLUSTER_UUID": "00000000-0000-0000-0000-000000000000",
        "COMPUTE": "enable",
        "COPYRIGHT": "TOPSEC",
        "CUSTOM_NAME": "TOPSEC",
        "GATEWAY": "enable",
        "INCREASE": "false",
        "NETWORK": "enable",
        "PHYSICAL_CPU_NUM": "50",
        "PRODUCT": "NGFW4000-UF(TG-41308)",
        "PRODUCT_SESSION": "1000000",
        "PSN": "K1101054297",
        "ROUTER": "enable",
        "SECURITY_GROUP": "enable",
        "SERIALNO": "xxxxxxxxxxxx.001",
        "STORAGE": "enable",
        "STORAGE_CAPACITY": "9999T",
        "SWITCH": "enable",
        "TOPHCI_EXPIRE": "2019-12-31",
        "TOPHCI_TRY_EXPIRE": "2019-04-16",
        "USD_AUTH_TYPE": "NONE",
        "VDFW": "enable",
        "VGATE": "enable"
      }
    }
  }
}
```

#### 异常返回示例

### 状态码

## /v1/license/list
集群激活license
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TODO


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.147:9990/v1/license/list?cluster_uuid=49bb08f9-1c60-49ee-85d6-6fde276895c5
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
        "encryptKey": "",
        "encryptedLicense": "",
        "CTime": 1619158578,
        "MTime": 1619158578,
        "license": {
          "BARE_METAL": "enable",
          "BILLING": "enable",
          "CLOUD_DESKTOP_VM": "2000",
          "CLUSTER_UUID": "00000000-0000-0000-0000-000000000000",
          "COMPUTE": "enable",
          "COMPUTE_CONTAINER": "enable",
          "COMPUTE_DESKTOP": "enable",
          "COMPUTE_SERVER": "enable",
          "GATEWAY": "enable",
          "INCREASE": "true",
          "MULTI_CLUSTER": "disable",
          "NETWORK": "enable",
          "PHYSICAL_CPU_NUM": "2030",
          "PRODUCT_TYPE": "TopDC",
          "ROUTER": "enable",
          "SECURITY_GROUP": "enable",
          "STORAGE": "enable",
          "STORAGE_BLOCK": "enable",
          "STORAGE_CAPACITY": "2100T",
          "STORAGE_FILE": "enable",
          "STORAGE_OBJECT": "enable",
          "SWITCH": "enable",
          "TOPHCI_EXPIRE": "2021-12-31",
          "TOPHCI_TRY_EXPIRE": "2021-05-23",
          "USD_AUTH_TYPE": "NONE",
          "VDFW": "enable",
          "VGATE": "enable"
        },
        "cluster_uuid": "49bb08f9-1c60-49ee-85d6-6fde276895c5",
        "cluster_name": "cluster_10_30_100_24",
        "cluster_mode": ""
      }
    ],
    "total_count": 1,
    "each_range_list_state": [
      {
        "cluster_uuid": "49bb08f9-1c60-49ee-85d6-6fde276895c5",
        "cluster_name": "cluster_10_30_100_24",
        "cluster_mode": "",
        "result": {
          "scode": 0,
          "desc": "",
          "message": "success",
          "message_cn": "成功",
          "stack": null,
          "data": ""
        },
        "total_count": 0
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码