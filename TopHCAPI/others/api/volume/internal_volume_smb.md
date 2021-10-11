[back to api overview](../api_overview.md#label_api)
### Samba卷用户组和用户相关接口

## /v1/volume/internal/user/group/create
Samba卷用户组添加
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
http://192.168.201.147:9990/v1/volume/internal/user/group/create
```
Body:
```
{
	"name": "group1",
	"type": "samba",
	"tenant_uuid": "",
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
    "user_group_uuid": "7e150ddb-de96-4d44-a0d5-ef9484d208e8",
    "type": "samba",
    "name": "group1",
    "ctime": 1573191376,
    "mtime": 1573191376,
    "user_num": 0
  }
}
```

#### 异常返回示例

### 状态码

## /v1/volume/internal/user/group/delete
Samba卷用户组删除
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
http://192.168.201.147:9990/v1/volume/internal/user/group/delete
```
Body:
```
{
	"user_group_uuid": "7e150ddb-de96-4d44-a0d5-ef9484d208e8",
	"tenant_uuid": "",
	"user_group_name": "group1",
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
    "user_group_uuid": "",
    "type": "",
    "name": "",
    "ctime": 0,
    "mtime": 0,
    "user_num": 0
  }
}
```

#### 异常返回示例

### 状态码

## /v1/volume/internal/user/group/list
Samba卷用户组列表
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
http://192.168.201.213:8080/v1/volume/internal/user/group/list?tenant_uuid=&page_num=0&page_size=5&filter_name=&type=samba&cluster_uuid=b8205835-ee82-4aa0-8c8b-6269e85aabd5
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
    "total_count": 1,
    "list": [
      {
        "user_group_uuid": "caa4ddba-729d-4ade-bedf-ddb993e0091c",
        "type": "samba",
        "name": "group1",
        "ctime": 1573191653,
        "mtime": 1573191653,
        "user_num": 0
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码



## /v1/volume/internal/user/group/assign
Samba卷用户组添加授权
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
http://192.168.201.147:9990/v1/volume/internal/user/group/assign
```
Body:
```
{
	"tenant_uuid": "",
	"dir_perms": {
		"caa4ddba-729d-4ade-bedf-ddb993e0091c": 1
	},
	"volume_uuid": "8652dfcb-9c83-4f93-b964-b8c87942869a",
	"path": "8652dfcb-9c83-4f93-b964-b8c87942869a",
	"volume_name": "volume-1108114153_smb",
	"user_group_type": "samba",
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
    "list": {
      "user_group_uuid": "",
      "type": "",
      "name": "",
      "ctime": 0,
      "mtime": 0,
      "user_num": 0
    }
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/internal/user/group/unassign
Samba卷用户组取消授权
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
http://192.168.201.147:9990/v1/volume/internal/user/group/unassign
```
Body:
```
{
	"tenant_uuid": "",
	"dir_perms": {
		"caa4ddba-729d-4ade-bedf-ddb993e0091c": 1
	},
	"volume_uuid": "8652dfcb-9c83-4f93-b964-b8c87942869a",
	"path": "8652dfcb-9c83-4f93-b964-b8c87942869a",
	"volume_name": "volume-1108114153_smb",
	"user_group_type": "samba",
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
    "list": {
      "user_group_uuid": "",
      "type": "",
      "name": "",
      "ctime": 0,
      "mtime": 0,
      "user_num": 0
    }
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/internal/user/create
Samba卷用户添加
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
http://192.168.201.147:9990/v1/volume/internal/user/create
```
Body:
```
{
	"tenant_uuid": "",
	"email": "",
	"name": "user1",
	"password": "admin",
	"user_group_uuid": "caa4ddba-729d-4ade-bedf-ddb993e0091c",
	"type": "samba",
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
    "user_uuid": "f04095cd-dc8c-445a-967d-083551794740",
    "type": "samba",
    "name": "user1",
    "passwd": "",
    "email": "",
    "ref": 0,
    "ctime": 1573192125,
    "mtime": 1573192125,
    "user_group_uuid": "caa4ddba-729d-4ade-bedf-ddb993e0091c",
    "user_group_name": "group1"
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/internal/user/delete
Samba卷用户删除
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
http://192.168.201.147:9990/v1/volume/internal/user/delete
```
Body:
```
{
	"user_uuid": "f04095cd-dc8c-445a-967d-083551794740",
	"user_name": "user1",
	"type": "samba",
	"tenant_uuid": "",
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
    "user_uuid": "",
    "type": "",
    "name": "",
    "passwd": "",
    "email": "",
    "ref": 0,
    "ctime": 0,
    "mtime": 0,
    "user_group_uuid": "",
    "user_group_name": ""
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/internal/user/list
Samba卷用户列表
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
http://192.168.201.213:8080/v1/volume/internal/user/list?tenant_uuid=&page_num=0&page_size=5&filter_name=&user_group=group1&user_group_uuid=caa4ddba-729d-4ade-bedf-ddb993e0091c&type=samba&cluster_uuid=b8205835-ee82-4aa0-8c8b-6269e85aabd5
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
    "total_count": 1,
    "list": [
      {
        "user_uuid": "3bd59586-f072-4397-9616-0a79fa0fa097",
        "type": "samba",
        "name": "user1",
        "passwd": "",
        "email": "",
        "ref": 0,
        "ctime": 1573192513,
        "mtime": 1573192513,
        "user_group_uuid": "caa4ddba-729d-4ade-bedf-ddb993e0091c",
        "user_group_name": "group1"
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/internal/user/assign
Samba卷用户添加授权
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
http://192.168.201.147:9990/v1/volume/internal/user/assign
```
Body:
```
{
	"tenant_uuid": "",
	"dir_perms": {
		"3bd59586-f072-4397-9616-0a79fa0fa097": 1
	},
	"volume_uuid": "8652dfcb-9c83-4f93-b964-b8c87942869a",
	"path": "8652dfcb-9c83-4f93-b964-b8c87942869a",
	"volume_name": "volume-1108114153_smb",
	"user_type": "samba",
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
    "user_uuid": "",
    "type": "",
    "name": "",
    "passwd": "",
    "email": "",
    "ref": 0,
    "ctime": 0,
    "mtime": 0,
    "user_group_uuid": "",
    "user_group_name": ""
  }
}
```

#### 异常返回示例

### 状态码


## /v1/volume/internal/user/unassign
Samba卷用户取消授权
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
http://192.168.201.147:9990/v1/volume/internal/user/unassign
```
Body:
```
{
	"tenant_uuid": "",
	"dir_perms": {
		"3bd59586-f072-4397-9616-0a79fa0fa097": 1
	},
	"volume_uuid": "8652dfcb-9c83-4f93-b964-b8c87942869a",
	"path": "8652dfcb-9c83-4f93-b964-b8c87942869a",
	"volume_name": "volume-1108114153_smb",
	"user_type": "samba",
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
    "user_uuid": "",
    "type": "",
    "name": "",
    "passwd": "",
    "email": "",
    "ref": 0,
    "ctime": 0,
    "mtime": 0,
    "user_group_uuid": "",
    "user_group_name": ""
  }
}
```

#### 异常返回示例

### 状态码



## /v1/volume/internal/path/perms/list
Samba卷目录列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
cluster_uuid|string|是|-|集群uuid
volume_uuid|string|是|-|卷uuid


### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.213:8080/v1/volume/internal/path/perms/list?volume_uuid=8652dfcb-9c83-4f93-b964-b8c87942869a&tenant_uuid=&cluster_uuid=b8205835-ee82-4aa0-8c8b-6269e85aabd5
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
    "total_count": 1,
    "perms": {
      "volUUID": "",
      "AllDirs": [
        "8652dfcb-9c83-4f93-b964-b8c87942869a"
      ],
      "UserPerms": {},
      "UserGroupPerms": {}
    }
  }
}
```

#### 异常返回示例

### 状态码

