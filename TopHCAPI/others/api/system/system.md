[back to api overview](../api_overview.md#api)

### 系统相关接口
## /v1/system/version
系统版本号
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---



### 返回参数

名称|参数类型|描述 
---|---|---
version|string|版本号

#### 请求示例
```
http://192.168.201.13:9990/v1/system/version
```

#### 正常返回示例
```
{
  "status_code": 0,
  "message_en": "success",
  "message_cn": "成功",
  "data": {
     "version": "0.1  @go1.11.1 linux/amd64  SRC#a7b9ecf9f35bde6cf7d7b0ad2531e5d4d33073c5  CMN#6a7e043276b14099b653b06c31e9df90630d4be3"
}
```

#### 异常返回示例

### 状态码


## /v1/system/member/list
manger服务成员列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---

### 返回参数

名称|参数类型|描述 
---|---|---
leader|string|主节点
candidates|string array|成员列表
ready|bool|是否正常

### 示例

#### 请求示例
```
http://192.168.201.212:9990/v1/system/member/list
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
    "leader": "192.168.201.213",
    "candidates": [
      "192.168.201.212",
      "192.168.201.211",
      "192.168.201.213"
    ],
    "ready": true,
    "alias_source": ""
  }
}
```

#### 异常返回示例

### 状态码




## /v1/system/mail_setting/inspect
系统发信邮箱配置详情
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.213:8080/v1/system/mail_setting/inspect?cluster_uuid=b8205835-ee82-4aa0-8c8b-6269e85aabd5
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
    "enabled": true,
    "asynchronous_send_enabled": false,
    "sender_mail": "ningmengting0912@163.com",
    "sender_name": "天融信",
    "smtp_server_ip": "smtp.163.com",
    "smtp_server_port": 25,
    "smtp_tls_enabled": false,
    "smtp_account": "ningmengting0912@163.com",
    "smtp_password": "qwer1234"
  }
}
```

#### 异常返回示例

### 状态码




## /v1/system/mail_setting/update
系统发信邮箱配置
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
http://192.168.201.147:9990/v1/system/mail_setting/update
```
Body:
```
{
	"enabled": true,
	"asynchronous_send_enabled": true,
	"sender_mail": "ningmengting0912@163.com",
	"sender_name": "天融信",
	"smtp_server_ip": "smtp.163.com",
	"smtp_server_port": 25,
	"smtp_tls_enabled": false,
	"smtp_account": "ningmengting0912@163.com",
	"smtp_password": "qwer1234"
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
    "enabled": true,
    "asynchronous_send_enabled": true,
    "sender_mail": "ningmengting0912@163.com",
    "sender_name": "天融信",
    "smtp_server_ip": "smtp.163.com",
    "smtp_server_port": 25,
    "smtp_tls_enabled": false,
    "smtp_account": "ningmengting0912@163.com",
    "smtp_password": "qwer1234"
  }
}
```

#### 异常返回示例

### 状态码

## /v1/system/mail_setting/test
系统发信邮箱发送邮件测试
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
http://192.168.201.147:9990/v1/system/mail_setting/test
```
Body:
```
{
	"enabled": true,
	"asynchronous_send_enabled": true,
	"sender_mail": "ningmengting0912@163.com",
	"sender_name": "天融信",
	"smtp_server_ip": "smtp.163.com",
	"smtp_server_port": 25,
	"smtp_tls_enabled": false,
	"smtp_account": "ningmengting0912@163.com",
	"smtp_password": "qwer1234",
	"receiver_email": "1779913694@qq.com"
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


## /v1/system/setting/inspect
系统基础配置详情
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
http://192.168.201.213:8080/v1/system/setting/inspect?cluster_uuid=b8205835-ee82-4aa0-8c8b-6269e85aabd5
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
    "login_policy": {
      "login_fail_retry_times": 1,
      "login_fail_punish_seconds": 1,
      "token_expire_second": 2592000
    },
    "password_complexity_policy": {
      "password_expire_force_modify": false,
      "password_max_expired_age": 0,
      "password_expired_warn_age": 0,
      "password_expired_warn_windows_popup": false,
      "password_expired_warn_email_notify": false,
      "password_must_include_special_char": false,
      "password_minimum_length": 3,
      "notify_user_password_when_create": false
    },
    "mail_setting": {
      "enabled": true,
      "asynchronous_send_enabled": false,
      "sender_mail": "ningmengting0912@163.com",
      "sender_name": "天融信",
      "smtp_server_ip": "smtp.163.com",
      "smtp_server_port": 25,
      "smtp_tls_enabled": false,
      "smtp_account": "ningmengting0912@163.com",
      "smtp_password": "qwer1234"
    },
    "multi_authentication_setting": {
      "enabled": false,
      "authentication_type": ""
    },
    "access_control_policy": {
      "ip_access_control_policy": {
        "ip_ranges": {
          "ranges": []
        },
        "whitelist": false,
        "enabled": false
      },
      "time_access_control_policy": null
    },
    "front_style_setting": {
      "login_image": "",
      "navigate_color": "",
      "main_body_color": "",
      "login_url": "http://192.168.201.212:8080/#/login"
    },
    "storage_setting": {
      "hop_hc": 1
    },
    "snmp_settings": {
      "snmps": null
    },
    "password_special_char": "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^\u0026*_+-="
  }
}
```

#### 异常返回示例

### 状态码


## /v1/system/setting/update
系统设置更新
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
http://192.168.201.147:9990/v1/system/setting/update
```
Body:
```
{
	"login_policy": {
		"login_fail_retry_times": 1,
		"login_fail_punish_seconds": 1,
		"token_expire_second": 2592000
	},
	"password_complexity_policy": {
		"password_expire_force_modify": false,
		"password_max_expired_age": 0,
		"password_minimum_length": 3,
		"password_must_include_special_char": false,
		"password_expired_warn_age": 0,
		"password_expired_warn_windows_popup": false,
		"password_expired_warn_email_notify": false,
		"notify_user_password_when_create": false
	},
	"cluster_uuid": "b8205835-ee82-4aa0-8c8b-6269e85aabd5"
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
    "login_policy": {
      "login_fail_retry_times": 1,
      "login_fail_punish_seconds": 1,
      "token_expire_second": 2592000
    },
    "password_complexity_policy": {
      "password_expire_force_modify": false,
      "password_max_expired_age": 0,
      "password_expired_warn_age": 0,
      "password_expired_warn_windows_popup": false,
      "password_expired_warn_email_notify": false,
      "password_must_include_special_char": false,
      "password_minimum_length": 3,
      "notify_user_password_when_create": false
    },
    "mail_setting": {
      "enabled": true,
      "asynchronous_send_enabled": true,
      "sender_mail": "ningmengting0912@163.com",
      "sender_name": "天融信",
      "smtp_server_ip": "smtp.163.com",
      "smtp_server_port": 25,
      "smtp_tls_enabled": false,
      "smtp_account": "ningmengting0912@163.com",
      "smtp_password": "qwer1234"
    },
    "multi_authentication_setting": {
      "enabled": false,
      "authentication_type": ""
    },
    "access_control_policy": {
      "ip_access_control_policy": {
        "ip_ranges": {
          "ranges": []
        },
        "whitelist": false,
        "enabled": false
      },
      "time_access_control_policy": null
    },
    "front_style_setting": {
      "login_image": "",
      "navigate_color": "",
      "main_body_color": "",
      "login_url": "http://192.168.201.212:8080/#/login"
    },
    "storage_setting": {
      "hop_hc": 1
    },
    "snmp_settings": {
      "snmps": null
    }
  }
}
```

#### 异常返回示例

### 状态码


## /v1/system/compute/version/upgrade
系统版本包升级
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
http://192.168.201.147:9990/v1/system/compute/version/upgrade
```
Body:
```
{
	"list": [
		{
			"host_ip": "10.30.12.55",
			"service_type": "storage"
		}
	],
	"cluster_uuid": "b088822c-1176-4c79-9df7-5fad80c7fd1d"
}
```

#### 正常返回示例
```
TODO
```

#### 异常返回示例

### 状态码



## /v1/system/upgrade_package/list
系统版本升级包列表
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
http://10.30.12.161:8080/v1/system/upgrade_package/list?cluster_uuid=b088822c-1176-4c79-9df7-5fad80c7fd1d
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "messageCn": "",
  "stack": null,
  "data": {
    "package_list": null,
    "host_list": [
      "10.30.12.161",
      "10.30.12.165",
      "10.30.12.55"
    ],
    "list": [
      {
        "host_ip": "10.30.12.161",
        "type_version": {
          "cloud": "1.4"
        },
        "upgrade_package_list": []
      },
      {
        "host_ip": "10.30.12.165",
        "type_version": {
          "compute": "1.4.rc2",
          "storage": "1.4.rc2"
        },
        "upgrade_package_list": []
      },
      {
        "host_ip": "10.30.12.55",
        "type_version": {
          "compute": "1.4.rc2",
          "storage": "1.3"
        },
        "upgrade_package_list": []
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码

## /v1/system/upgrade_package/current/inspect
系统当前版本包详情
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid

### 返回参数

名称|参数类型|描述
---|---|---
package_name|string|版本包名称
md5|string|md5值
version|string|版本
update_time|int64|升级包升级时间
size|int64|升级包大小

### 示例

#### 请求示例
```
http://10.30.10.34:8080/v1/system/upgrade_package/current/inspect?cluster_uuid=3afdbbfc-e45a-430e-abba-842074a8b035
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
    "package_name": "updatepackage_3.2.5.rc2.tar.gz",
    "md5": "41ff13b3b85609c5f5a932b106c5130d",
    "version": "3.2.5.rc2",
    "update_time": 1615374182,
    "size": 340416119
  }
}
```

#### 异常返回示例

### 状态码


## /v1/system/compute/version/list
系统备份版本包列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
host_ip|string|是|-|主机ip

### 返回参数

名称|参数类型|描述
---|---|---
package_name|string|版本包名称
md5|string|md5值
version|string|版本
update_time|int64|升级包升级时间
size|int64|升级包大小

### 示例

#### 请求示例
```
http://10.30.10.34:8080/v1/system/compute/version/list?host_ip=10.30.12.39&cluster_uuid=232671ca-d1e7-44ea-9278-a7c2d5920fa7
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
        "package_name": "backup_3.2.5.0_20210428_1725.tar.gz",
        "md5": "34c4a9a1d544229c078529ac19a06c36",
        "version": "3.2.5.0",
        "update_time": 1619601979,
        "size": 134980056
      },
      {
        "package_name": "backup_3.2.5.1_20210428_1903.tar.gz",
        "md5": "78f9c7f3e162eaa47ec65dde4d66e4a5",
        "version": "3.2.5.1",
        "update_time": 1619607810,
        "size": 135091085
      },
      {
        "package_name": "backup_3.2.5.2_20210611_1438.tar.gz",
        "md5": "1e5b4bbadf831ef385e55c3d7d1628be",
        "version": "3.2.5.2",
        "update_time": 1623393558,
        "size": 135266946
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码

