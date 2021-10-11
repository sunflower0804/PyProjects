## /v1/container/list
#### 功能：获取容器列表
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/container/list
```
Body:
```	
{
	"Container": {
		"ExtraInfo": {
			"Ns": "ed350282-de88-4e2a-98fc-da2029a60138"
		}
	},
	"paging": {
		"page_size": 20,
		"page_number": 0
	},
	"filter": {
		"Name": ""
	},
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
    "TotalCount": 1,
    "Infos": [
      {
        "Info": {
          "Name": "ubuntu_2",
          "UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
          "config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": true,
            "OpenStdin": true,
            "StdinOnce": true,
            "Cmd": null,
            "Healthcheck": null,
            "ArgsEscaped": false,
            "Image": "ubuntu",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "NetworkDisabled": false,
            "MacAddress": "",
            "OnBuild": null,
            "Labels": null,
            "StopSignal": "",
            "StopTimeout": 0,
            "Shell": null,
            "ImageAuthConfig": null,
            "ContainerProbeSpec": null,
            "Env": null,
            "ImagePullPolicy": "Always",
            "ExposedPorts": null,
            "ImageAuthSecret": ""
          },
          "hostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
              "Type": "",
              "Config": null
            },
            "NetworkMode": "",
            "RestartPolicy": {
              "Name": "no",
              "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "thci",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "DNS": null,
            "DNSOptions": null,
            "DNSSearch": null,
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "StorageOpt": null,
            "Tmpfs": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 0,
            "Sysctls": null,
            "Runtime": "",
            "ConsoleSize": null,
            "Isolation": "",
            "Mounts": null,
            "MaskedPaths": null,
            "ReadonlyPaths": null,
            "Init": false,
            "Resource": {
              "CPUShares": 0,
              "Memory": 0,
              "NanoCPUs": 0,
              "CgroupParent": "",
              "BlkioWeight": 0,
              "BlkioWeightDevice": null,
              "BlkioDeviceReadBps": null,
              "BlkioDeviceWriteBps": null,
              "BlkioDeviceReadIOps": null,
              "BlkioDeviceWriteIOps": null,
              "CPUPeriod": 0,
              "CPUQuota": 0,
              "CPURealtimePeriod": 0,
              "CPURealtimeRuntime": 0,
              "CpusetCpus": "",
              "CpusetMems": "",
              "Devices": null,
              "DeviceCgroupRules": null,
              "DiskQuota": 0,
              "KernelMemory": 0,
              "MemoryReservation": 0,
              "MemorySwap": 0,
              "MemorySwappiness": 0,
              "OomKillDisable": false,
              "PidsLimit": 0,
              "Ulimits": null
            },
            "SecretData": null,
            "PortBindings": null
          },
          "networkingConfig": {
            "EndpointsConfig": null
          },
          "ExtraInfo": {
            "MachineUUID": "",
            "State": "stopped",
            "Ns": "ed350282-de88-4e2a-98fc-da2029a60138",
            "CTime": 1573112392,
            "MTime": 1573112392,
            "HostIP": "",
            "ConsoleSeverListenPort": 0,
            "HAMode": "on",
            "Action": 0,
            "DeleteTime": 0,
            "Owner": "",
            "ErrorDetail": "",
            "NotHealthy": false
          },
          "ContainerStats": null,
          "Logs": "",
          "Warnings": null,
          "AttachInterfacesResult": null,
          "DetachInterfacesResult": null,
          "StartupConfig": {
            "HostUUID": "",
            "Labels": null,
            "HostIP": ""
          },
          "HasAttachInterface": false
        },
        "tenant": "ed350282-de88-4e2a-98fc-da2029a60138",
        "tenant_name": "lts",
        "owner": "",
        "owner_name": "",
        "owner_is_ldap": false
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码

## /v1/container/inspect
#### 功能：获取容器详情
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/container/inspect
```
Body:
```	
{
	"container": {
		"UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
		"ExtraInfo": {
			"Ns": "ed350282-de88-4e2a-98fc-da2029a60138"
		}
	},
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
    "TotalCount": 0,
    "Infos": [
      {
        "Info": {
          "Name": "ubuntu_2",
          "UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
          "config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": true,
            "OpenStdin": true,
            "StdinOnce": true,
            "Cmd": null,
            "Healthcheck": null,
            "ArgsEscaped": false,
            "Image": "ubuntu",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "NetworkDisabled": false,
            "MacAddress": "",
            "OnBuild": null,
            "Labels": null,
            "StopSignal": "",
            "StopTimeout": 0,
            "Shell": null,
            "ImageAuthConfig": null,
            "ContainerProbeSpec": null,
            "Env": null,
            "ImagePullPolicy": "Always",
            "ExposedPorts": null,
            "ImageAuthSecret": ""
          },
          "hostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
              "Type": "",
              "Config": null
            },
            "NetworkMode": "",
            "RestartPolicy": {
              "Name": "no",
              "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "thci",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "DNS": null,
            "DNSOptions": null,
            "DNSSearch": null,
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "StorageOpt": null,
            "Tmpfs": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 0,
            "Sysctls": null,
            "Runtime": "",
            "ConsoleSize": null,
            "Isolation": "",
            "Mounts": null,
            "MaskedPaths": null,
            "ReadonlyPaths": null,
            "Init": false,
            "Resource": {
              "CPUShares": 0,
              "Memory": 0,
              "NanoCPUs": 0,
              "CgroupParent": "",
              "BlkioWeight": 0,
              "BlkioWeightDevice": null,
              "BlkioDeviceReadBps": null,
              "BlkioDeviceWriteBps": null,
              "BlkioDeviceReadIOps": null,
              "BlkioDeviceWriteIOps": null,
              "CPUPeriod": 0,
              "CPUQuota": 0,
              "CPURealtimePeriod": 0,
              "CPURealtimeRuntime": 0,
              "CpusetCpus": "",
              "CpusetMems": "",
              "Devices": null,
              "DeviceCgroupRules": null,
              "DiskQuota": 0,
              "KernelMemory": 0,
              "MemoryReservation": 0,
              "MemorySwap": 0,
              "MemorySwappiness": 0,
              "OomKillDisable": false,
              "PidsLimit": 0,
              "Ulimits": null
            },
            "SecretData": null,
            "PortBindings": null
          },
          "networkingConfig": {
            "EndpointsConfig": null
          },
          "ExtraInfo": {
            "MachineUUID": "",
            "State": "stopped",
            "Ns": "ed350282-de88-4e2a-98fc-da2029a60138",
            "CTime": 1573112392,
            "MTime": 1573112392,
            "HostIP": "",
            "ConsoleSeverListenPort": 0,
            "HAMode": "on",
            "Action": 0,
            "DeleteTime": 0,
            "Owner": "",
            "ErrorDetail": "",
            "NotHealthy": false
          },
          "ContainerStats": null,
          "Logs": "",
          "Warnings": null,
          "AttachInterfacesResult": null,
          "DetachInterfacesResult": null,
          "StartupConfig": {
            "HostUUID": "",
            "Labels": null,
            "HostIP": ""
          },
          "HasAttachInterface": false
        },
        "tenant": "ed350282-de88-4e2a-98fc-da2029a60138",
        "tenant_name": "lts",
        "owner": "",
        "owner_name": "",
        "owner_is_ldap": false
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/container/create
#### 功能：创建容器
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/container/create
```
Body:
```	
{
	"create_num": 1,
	"container": {
		"Name": "test",
		"config": {
			"Tty": true,
			"OpenStdin": true,
			"StdinOnce": true,
			"Env": null,
			"WorkingDir": "",
			"Image": "ubuntu",
			"ImagePullPolicy": "Always",
			"Cmd": [],
			"Entrypoint": [],
			"ImageAuthConfig": null,
			"ContainerProbeSpec": null,
			"Labels": null
		},
		"hostConfig": {
			"VolumeDriver": "thci",
			"Resource": {
				"Memory": 0,
				"CPUShares": 0,
				"CpusetCpus": null,
				"MemoryReservation": 0,
				"MemorySwap": 0,
				"Devices": null
			},
			"RestartPolicy": {
				"Name": "no",
				"MaximumRetryCount": null
			},
			"Privileged": false,
			"PidMode": null,
			"LogConfig": {
				"Config": null
			},
			"SecretData": null,
			"CapAdd": [],
			"CapDrop": []
		},
		"ExtraInfo": {
			"Ns": "ed350282-de88-4e2a-98fc-da2029a60138",
			"HAMode": "on"
		},
		"networkingConfig": {
			"EndpointsConfig": []
		},
		"StartupConfig": {
			"HostUUID": null,
			"HostIP": null,
			"Labels": null
		}
	},
	"disk": [],
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
    "success": 1,
    "fail": 0,
    "results": [
      {
        "scode": 0,
        "desc": "",
        "message": "success",
        "message_cn": "成功",
        "stack": null,
        "data": {
          "tenant": "",
          "index": 0,
          "name": "test",
          "uuid": "45193309-1271-40ee-bb1d-f9c475af9089",
          "Info": null
        }
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码



## /v1/container/remove
#### 功能：删除容器
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/container/remove
```
Body:
```	
{
	"containers": [
		{
			"container": {
				"UUID": "45193309-1271-40ee-bb1d-f9c475af9089",
				"ExtraInfo": {
					"Ns": "ed350282-de88-4e2a-98fc-da2029a60138"
				}
			},
			"DeleteVolume": true,
			"RealDelete": true,
			"DeleteImage": true
		}
	],
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
    "success": 1,
    "fail": 0,
    "results": [
      {
        "scode": 0,
        "desc": "",
        "message": "success",
        "message_cn": "成功",
        "stack": null,
        "data": {
          "tenant": "",
          "Name": "",
          "UUID": "45193309-1271-40ee-bb1d-f9c475af9089",
          "config": null,
          "hostConfig": null,
          "networkingConfig": null,
          "ExtraInfo": {
            "MachineUUID": "",
            "State": "",
            "Ns": "ed350282-de88-4e2a-98fc-da2029a60138",
            "CTime": 0,
            "MTime": 0,
            "HostIP": "",
            "ConsoleSeverListenPort": 0,
            "HAMode": "",
            "Action": 0,
            "DeleteTime": 0,
            "Owner": "",
            "ErrorDetail": "",
            "NotHealthy": false
          },
          "ContainerStats": null,
          "Logs": "",
          "Warnings": null,
          "AttachInterfacesResult": null,
          "DetachInterfacesResult": null,
          "StartupConfig": null,
          "HasAttachInterface": false
        }
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码



## /v1/container/start
#### 功能：启动容器
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/container/start
```
Body:
```	
{
	"containers": [
		{
			"container": {
				"UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
				"ExtraInfo": {
					"Ns": "ed350282-de88-4e2a-98fc-da2029a60138"
				}
			}
		}
	],
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
    "success": 1,
    "fail": 0,
    "results": [
      {
        "scode": 0,
        "desc": "",
        "message": "success",
        "message_cn": "成功",
        "stack": null,
        "data": {
          "tenant": "",
          "Name": "",
          "UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
          "config": null,
          "hostConfig": null,
          "networkingConfig": null,
          "ExtraInfo": {
            "MachineUUID": "",
            "State": "",
            "Ns": "ed350282-de88-4e2a-98fc-da2029a60138",
            "CTime": 0,
            "MTime": 0,
            "HostIP": "",
            "ConsoleSeverListenPort": 0,
            "HAMode": "",
            "Action": 0,
            "DeleteTime": 0,
            "Owner": "",
            "ErrorDetail": "",
            "NotHealthy": false
          },
          "ContainerStats": null,
          "Logs": "",
          "Warnings": null,
          "AttachInterfacesResult": null,
          "DetachInterfacesResult": null,
          "StartupConfig": null,
          "HasAttachInterface": false
        }
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码



## /v1/container/stop
#### 功能：关闭容器
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/container/stop
```
Body:
```	
{
	"containers": [
		{
			"container": {
				"UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
				"ExtraInfo": {
					"Ns": "ed350282-de88-4e2a-98fc-da2029a60138"
				}
			}
		}
	],
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
    "success": 1,
    "fail": 0,
    "results": [
      {
        "scode": 0,
        "desc": "",
        "message": "success",
        "message_cn": "成功",
        "stack": null,
        "data": {
          "tenant": "",
          "Name": "",
          "UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
          "config": null,
          "hostConfig": null,
          "networkingConfig": null,
          "ExtraInfo": {
            "MachineUUID": "",
            "State": "",
            "Ns": "ed350282-de88-4e2a-98fc-da2029a60138",
            "CTime": 0,
            "MTime": 0,
            "HostIP": "",
            "ConsoleSeverListenPort": 0,
            "HAMode": "",
            "Action": 0,
            "DeleteTime": 0,
            "Owner": "",
            "ErrorDetail": "",
            "NotHealthy": false
          },
          "ContainerStats": null,
          "Logs": "",
          "Warnings": null,
          "AttachInterfacesResult": null,
          "DetachInterfacesResult": null,
          "StartupConfig": null,
          "HasAttachInterface": false
        }
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码



## /v1/container/pause
#### 功能：暂停容器
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/container/pause
```
Body:
```	
{
	"containers": [
		{
			"container": {
				"UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
				"ExtraInfo": {
					"Ns": "ed350282-de88-4e2a-98fc-da2029a60138"
				}
			}
		}
	],
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
    "success": 1,
    "fail": 0,
    "results": [
      {
        "scode": 0,
        "desc": "",
        "message": "success",
        "message_cn": "成功",
        "stack": null,
        "data": {
          "tenant": "",
          "Name": "",
          "UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
          "config": null,
          "hostConfig": null,
          "networkingConfig": null,
          "ExtraInfo": {
            "MachineUUID": "",
            "State": "",
            "Ns": "ed350282-de88-4e2a-98fc-da2029a60138",
            "CTime": 0,
            "MTime": 0,
            "HostIP": "",
            "ConsoleSeverListenPort": 0,
            "HAMode": "",
            "Action": 0,
            "DeleteTime": 0,
            "Owner": "",
            "ErrorDetail": "",
            "NotHealthy": false
          },
          "ContainerStats": null,
          "Logs": "",
          "Warnings": null,
          "AttachInterfacesResult": null,
          "DetachInterfacesResult": null,
          "StartupConfig": null,
          "HasAttachInterface": false
        }
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码



## /v1/container/resume
#### 功能：恢复容器
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/container/resume
```
Body:
```	
{
	"containers": [
		{
			"container": {
				"UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
				"ExtraInfo": {
					"Ns": "ed350282-de88-4e2a-98fc-da2029a60138"
				}
			}
		}
	],
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
    "success": 1,
    "fail": 0,
    "results": [
      {
        "scode": 0,
        "desc": "",
        "message": "success",
        "message_cn": "成功",
        "stack": null,
        "data": {
          "tenant": "",
          "Name": "",
          "UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
          "config": null,
          "hostConfig": null,
          "networkingConfig": null,
          "ExtraInfo": {
            "MachineUUID": "",
            "State": "",
            "Ns": "ed350282-de88-4e2a-98fc-da2029a60138",
            "CTime": 0,
            "MTime": 0,
            "HostIP": "",
            "ConsoleSeverListenPort": 0,
            "HAMode": "",
            "Action": 0,
            "DeleteTime": 0,
            "Owner": "",
            "ErrorDetail": "",
            "NotHealthy": false
          },
          "ContainerStats": null,
          "Logs": "",
          "Warnings": null,
          "AttachInterfacesResult": null,
          "DetachInterfacesResult": null,
          "StartupConfig": null,
          "HasAttachInterface": false
        }
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码



## /v1/container/disk/attach
#### 功能：添加磁盘
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/container/disk/attach
```
Body:
```	
{
	"container": {
		"UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
		"hostConfig": {
			"Binds": [
				{
					"VolumeUUID": "b4bb6e7f-0f2f-4f0a-936e-cb6bd4c44450",
					"ContainerPath": "",
					"Perm": "rw"
				}
			]
		}
	},
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
    "TotalCount": 1,
    "Infos": [
      {
        "Info": {
          "Name": "u44444bu34444",
          "UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
          "config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": true,
            "OpenStdin": true,
            "StdinOnce": true,
            "Cmd": [
              "/bin/bash"
            ],
            "Healthcheck": null,
            "ArgsEscaped": false,
            "Image": "ubuntu",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "NetworkDisabled": false,
            "MacAddress": "",
            "OnBuild": null,
            "Labels": null,
            "StopSignal": "",
            "StopTimeout": 0,
            "Shell": null,
            "ImageAuthConfig": null,
            "ContainerProbeSpec": null,
            "Env": null,
            "ImagePullPolicy": "Always",
            "ExposedPorts": null,
            "ImageAuthSecret": ""
          },
          "hostConfig": {
            "Binds": [
              {
                "VolumeUUID": "b4bb6e7f-0f2f-4f0a-936e-cb6bd4c44450",
                "ContainerPath": "/b4bb6e7f-0f2f-4f0a-936e-cb6bd4c44450",
                "Portal": "",
                "volumePath": "",
                "VolumeType": "",
                "Perm": "rw",
                "ExtraInfo": {
                  "Name": "volume-1107160641",
                  "Capacity": 1073741824,
                  "PoolName": "100",
                  "PoolUUID": "4b2ed759-bff6-44b7-8bb9-655754f7dce2",
                  "DevType": "block",
                  "DataType": "replica",
                  "Replica": "2",
                  "ECDataShard": "",
                  "ECParityShard": "",
                  "DriveType": "HDD"
                }
              }
            ],
            "ContainerIDFile": "",
            "LogConfig": {
              "Type": "",
              "Config": null
            },
            "NetworkMode": "",
            "RestartPolicy": {
              "Name": "no",
              "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "thci",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "DNS": null,
            "DNSOptions": null,
            "DNSSearch": null,
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "StorageOpt": null,
            "Tmpfs": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 0,
            "Sysctls": null,
            "Runtime": "",
            "ConsoleSize": null,
            "Isolation": "",
            "Mounts": null,
            "MaskedPaths": null,
            "ReadonlyPaths": null,
            "Init": false,
            "Resource": {
              "CPUShares": 0,
              "Memory": 0,
              "NanoCPUs": 0,
              "CgroupParent": "",
              "BlkioWeight": 0,
              "BlkioWeightDevice": null,
              "BlkioDeviceReadBps": null,
              "BlkioDeviceWriteBps": null,
              "BlkioDeviceReadIOps": null,
              "BlkioDeviceWriteIOps": null,
              "CPUPeriod": 0,
              "CPUQuota": 0,
              "CPURealtimePeriod": 0,
              "CPURealtimeRuntime": 0,
              "CpusetCpus": "",
              "CpusetMems": "",
              "Devices": null,
              "DeviceCgroupRules": null,
              "DiskQuota": 0,
              "KernelMemory": 0,
              "MemoryReservation": 0,
              "MemorySwap": 0,
              "MemorySwappiness": 0,
              "OomKillDisable": false,
              "PidsLimit": 0,
              "Ulimits": null
            },
            "SecretData": null,
            "PortBindings": null
          },
          "networkingConfig": {
            "EndpointsConfig": null
          },
          "ExtraInfo": {
            "MachineUUID": "07bc76c4-ce06-4383-988d-8dd4ee493012",
            "State": "stopped",
            "Ns": "ed350282-de88-4e2a-98fc-da2029a60138",
            "CTime": 1573112392,
            "MTime": 1573146427,
            "HostIP": "192.168.201.188",
            "ConsoleSeverListenPort": 5900,
            "HAMode": "on",
            "Action": 0,
            "DeleteTime": 0,
            "Owner": "",
            "ErrorDetail": "",
            "NotHealthy": false
          },
          "ContainerStats": null,
          "Logs": "",
          "Warnings": null,
          "AttachInterfacesResult": {
            "Success": 0,
            "Fail": 0,
            "Results": null
          },
          "DetachInterfacesResult": null,
          "StartupConfig": {
            "HostUUID": "",
            "Labels": null,
            "HostIP": ""
          },
          "HasAttachInterface": true
        }
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码



## /v1/container/disk/detach
#### 功能：容器删掉磁盘
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/container/disk/detach
```
Body:
```	
{
	"container": {
		"UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
		"hostConfig": {
			"Binds": [
				{
					"VolumeUUID": "b4bb6e7f-0f2f-4f0a-936e-cb6bd4c44450"
				}
			]
		}
	},
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
    "TotalCount": 0,
    "Infos": null
  }
}
```

#### 异常返回示例

### 状态码


## /v1/container/interface/attach
#### 功能：容器添加网卡
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/container/interface/attach
```
Body:
```	
{
	"container": {
		"UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
		"ExtraInfo": {
			"Ns": "ed350282-de88-4e2a-98fc-da2029a60138"
		},
		"networkingConfig": {
			"EndpointsConfig": [
				{
					"Bridge": "internal",
					"PortGroupUUID": null,
					"Tag": null,
					"CInfo": {},
					"ModelType": "virtio",
					"Bandwidth": {
						"Outbound": {
							"Peak": 0,
							"Floor": 0
						},
						"Inbound": {
							"Peak": 0,
							"Burst": 0
						}
					}
				}
			]
		}
	},
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
    "TotalCount": 1,
    "Infos": [
      {
        "Info": {
          "Name": "u44444bu34444",
          "UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
          "config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": true,
            "OpenStdin": true,
            "StdinOnce": true,
            "Cmd": [
              "/bin/bash"
            ],
            "Healthcheck": null,
            "ArgsEscaped": false,
            "Image": "ubuntu",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "NetworkDisabled": false,
            "MacAddress": "",
            "OnBuild": null,
            "Labels": null,
            "StopSignal": "",
            "StopTimeout": 0,
            "Shell": null,
            "ImageAuthConfig": null,
            "ContainerProbeSpec": null,
            "Env": null,
            "ImagePullPolicy": "Always",
            "ExposedPorts": null,
            "ImageAuthSecret": ""
          },
          "hostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
              "Type": "",
              "Config": null
            },
            "NetworkMode": "",
            "RestartPolicy": {
              "Name": "no",
              "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "thci",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "DNS": null,
            "DNSOptions": null,
            "DNSSearch": null,
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "StorageOpt": null,
            "Tmpfs": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 0,
            "Sysctls": null,
            "Runtime": "",
            "ConsoleSize": null,
            "Isolation": "",
            "Mounts": null,
            "MaskedPaths": null,
            "ReadonlyPaths": null,
            "Init": false,
            "Resource": {
              "CPUShares": 0,
              "Memory": 0,
              "NanoCPUs": 0,
              "CgroupParent": "",
              "BlkioWeight": 0,
              "BlkioWeightDevice": null,
              "BlkioDeviceReadBps": null,
              "BlkioDeviceWriteBps": null,
              "BlkioDeviceReadIOps": null,
              "BlkioDeviceWriteIOps": null,
              "CPUPeriod": 0,
              "CPUQuota": 0,
              "CPURealtimePeriod": 0,
              "CPURealtimeRuntime": 0,
              "CpusetCpus": "",
              "CpusetMems": "",
              "Devices": null,
              "DeviceCgroupRules": null,
              "DiskQuota": 0,
              "KernelMemory": 0,
              "MemoryReservation": 0,
              "MemorySwap": 0,
              "MemorySwappiness": 0,
              "OomKillDisable": false,
              "PidsLimit": 0,
              "Ulimits": null
            },
            "SecretData": null,
            "PortBindings": null
          },
          "networkingConfig": {
            "EndpointsConfig": [
              {
                "IPAMConfig": null,
                "Links": null,
                "Aliases": null,
                "NetworkID": "",
                "EndpointID": "",
                "Gateway": "",
                "IPAddress": "",
                "IPPrefixLen": 0,
                "IPv6Gateway": "",
                "GlobalIPv6Address": "",
                "GlobalIPv6PrefixLen": 0,
                "MacAddress": "52:56:ff:77:8e:88",
                "Bridge": "br-int",
                "ModelType": "virtio",
                "InterfaceName": "eth9",
                "OvsPortName": "0f2bf37357734_l",
                "Mtu": 0,
                "IFaceUUID": "bea1bdba-bdf1-4313-b2be-efb9ca666695",
                "Allocate_Flush": true,
                "QoSUUID": "",
                "QueueUUID": "",
                "DriverOpts": null,
                "Bandwidth": {
                  "Inbound": {
                    "Peak": 0,
                    "Burst": 0,
                    "Floor": 0
                  },
                  "Outbound": {
                    "Peak": 0,
                    "Burst": 0,
                    "Floor": 0
                  }
                },
                "CInfo": {
                  "Name": "",
                  "UUID": "",
                  "Object": ""
                },
                "Tag": 0,
                "PortGroupUUID": "",
                "PotrGroupName": ""
              }
            ]
          },
          "ExtraInfo": {
            "MachineUUID": "6040ac60-6c0d-46f6-9af6-90e522e41fe9",
            "State": "running",
            "Ns": "ed350282-de88-4e2a-98fc-da2029a60138",
            "CTime": 1573112392,
            "MTime": 1573146714,
            "HostIP": "192.168.201.187",
            "ConsoleSeverListenPort": 5900,
            "HAMode": "on",
            "Action": 0,
            "DeleteTime": 0,
            "Owner": "",
            "ErrorDetail": "",
            "NotHealthy": false
          },
          "ContainerStats": null,
          "Logs": "",
          "Warnings": null,
          "AttachInterfacesResult": {
            "Success": 1,
            "Fail": 0,
            "Results": [
              {
                "Endpoint": {
                  "IPAMConfig": null,
                  "Links": null,
                  "Aliases": null,
                  "NetworkID": "",
                  "EndpointID": "",
                  "Gateway": "",
                  "IPAddress": "",
                  "IPPrefixLen": 0,
                  "IPv6Gateway": "",
                  "GlobalIPv6Address": "",
                  "GlobalIPv6PrefixLen": 0,
                  "MacAddress": "52:56:ff:77:8e:88",
                  "Bridge": "br-int",
                  "ModelType": "virtio",
                  "InterfaceName": "eth9",
                  "OvsPortName": "0f2bf37357734_l",
                  "Mtu": 0,
                  "IFaceUUID": "bea1bdba-bdf1-4313-b2be-efb9ca666695",
                  "Allocate_Flush": true,
                  "QoSUUID": "",
                  "QueueUUID": "",
                  "DriverOpts": null,
                  "Bandwidth": {
                    "Inbound": {
                      "Peak": 0,
                      "Burst": 0,
                      "Floor": 0
                    },
                    "Outbound": {
                      "Peak": 0,
                      "Burst": 0,
                      "Floor": 0
                    }
                  },
                  "CInfo": {
                    "Name": "",
                    "UUID": "",
                    "Object": ""
                  },
                  "Tag": 0,
                  "PortGroupUUID": "",
                  "PotrGroupName": ""
                },
                "Status": {
                  "code": 0,
                  "message": "",
                  "messageCn": "",
                  "stack": null,
                  "desc": "",
                  "UUID": ""
                }
              }
            ]
          },
          "DetachInterfacesResult": null,
          "StartupConfig": {
            "HostUUID": "",
            "Labels": null,
            "HostIP": ""
          },
          "HasAttachInterface": true
        }
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码



## /v1/container/interface/detach
#### 功能：容器删掉网卡
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/container/interface/detach
```
Body:
```	
{
	"container": {
		"UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
		"ExtraInfo": {
			"Ns": "ed350282-de88-4e2a-98fc-da2029a60138"
		},
		"networkingConfig": {
			"EndpointsConfig": [
				{
					"Bridge": "internal",
					"MacAddress": "52:56:ff:77:8e:88"
				}
			]
		}
	},
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
    "TotalCount": 1,
    "Infos": [
      {
        "Info": {
          "Name": "u44444bu34444",
          "UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
          "config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": true,
            "OpenStdin": true,
            "StdinOnce": true,
            "Cmd": [
              "/bin/bash"
            ],
            "Healthcheck": null,
            "ArgsEscaped": false,
            "Image": "ubuntu",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "NetworkDisabled": false,
            "MacAddress": "",
            "OnBuild": null,
            "Labels": null,
            "StopSignal": "",
            "StopTimeout": 0,
            "Shell": null,
            "ImageAuthConfig": null,
            "ContainerProbeSpec": null,
            "Env": null,
            "ImagePullPolicy": "Always",
            "ExposedPorts": null,
            "ImageAuthSecret": ""
          },
          "hostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
              "Type": "",
              "Config": null
            },
            "NetworkMode": "",
            "RestartPolicy": {
              "Name": "no",
              "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "thci",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "DNS": null,
            "DNSOptions": null,
            "DNSSearch": null,
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "StorageOpt": null,
            "Tmpfs": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 0,
            "Sysctls": null,
            "Runtime": "",
            "ConsoleSize": null,
            "Isolation": "",
            "Mounts": null,
            "MaskedPaths": null,
            "ReadonlyPaths": null,
            "Init": false,
            "Resource": {
              "CPUShares": 0,
              "Memory": 0,
              "NanoCPUs": 0,
              "CgroupParent": "",
              "BlkioWeight": 0,
              "BlkioWeightDevice": null,
              "BlkioDeviceReadBps": null,
              "BlkioDeviceWriteBps": null,
              "BlkioDeviceReadIOps": null,
              "BlkioDeviceWriteIOps": null,
              "CPUPeriod": 0,
              "CPUQuota": 0,
              "CPURealtimePeriod": 0,
              "CPURealtimeRuntime": 0,
              "CpusetCpus": "",
              "CpusetMems": "",
              "Devices": null,
              "DeviceCgroupRules": null,
              "DiskQuota": 0,
              "KernelMemory": 0,
              "MemoryReservation": 0,
              "MemorySwap": 0,
              "MemorySwappiness": 0,
              "OomKillDisable": false,
              "PidsLimit": 0,
              "Ulimits": null
            },
            "SecretData": null,
            "PortBindings": null
          },
          "networkingConfig": {
            "EndpointsConfig": null
          },
          "ExtraInfo": {
            "MachineUUID": "6040ac60-6c0d-46f6-9af6-90e522e41fe9",
            "State": "running",
            "Ns": "ed350282-de88-4e2a-98fc-da2029a60138",
            "CTime": 1573112392,
            "MTime": 1573146847,
            "HostIP": "192.168.201.187",
            "ConsoleSeverListenPort": 5900,
            "HAMode": "on",
            "Action": 0,
            "DeleteTime": 0,
            "Owner": "",
            "ErrorDetail": "",
            "NotHealthy": false
          },
          "ContainerStats": null,
          "Logs": "",
          "Warnings": null,
          "AttachInterfacesResult": {
            "Success": 1,
            "Fail": 0,
            "Results": [
              {
                "Endpoint": {
                  "IPAMConfig": null,
                  "Links": null,
                  "Aliases": null,
                  "NetworkID": "",
                  "EndpointID": "",
                  "Gateway": "",
                  "IPAddress": "",
                  "IPPrefixLen": 0,
                  "IPv6Gateway": "",
                  "GlobalIPv6Address": "",
                  "GlobalIPv6PrefixLen": 0,
                  "MacAddress": "52:56:ff:77:8e:88",
                  "Bridge": "br-int",
                  "ModelType": "virtio",
                  "InterfaceName": "eth9",
                  "OvsPortName": "0f2bf37357734_l",
                  "Mtu": 0,
                  "IFaceUUID": "bea1bdba-bdf1-4313-b2be-efb9ca666695",
                  "Allocate_Flush": true,
                  "QoSUUID": "",
                  "QueueUUID": "",
                  "DriverOpts": null,
                  "Bandwidth": {
                    "Inbound": {
                      "Peak": 0,
                      "Burst": 0,
                      "Floor": 0
                    },
                    "Outbound": {
                      "Peak": 0,
                      "Burst": 0,
                      "Floor": 0
                    }
                  },
                  "CInfo": {
                    "Name": "",
                    "UUID": "",
                    "Object": ""
                  },
                  "Tag": 0,
                  "PortGroupUUID": "",
                  "PotrGroupName": ""
                },
                "Status": {
                  "code": 0,
                  "message": "",
                  "messageCn": "",
                  "stack": null,
                  "desc": "",
                  "UUID": ""
                }
              }
            ]
          },
          "DetachInterfacesResult": {
            "Success": 0,
            "Fail": 1,
            "Results": [
              {
                "Endpoint": {
                  "IPAMConfig": null,
                  "Links": null,
                  "Aliases": null,
                  "NetworkID": "",
                  "EndpointID": "",
                  "Gateway": "",
                  "IPAddress": "",
                  "IPPrefixLen": 0,
                  "IPv6Gateway": "",
                  "GlobalIPv6Address": "",
                  "GlobalIPv6PrefixLen": 0,
                  "MacAddress": "52:56:ff:77:8e:88",
                  "Bridge": "br-int",
                  "ModelType": "",
                  "InterfaceName": "eth9",
                  "OvsPortName": "0f2bf37357734_l",
                  "Mtu": 0,
                  "IFaceUUID": "",
                  "Allocate_Flush": false,
                  "QoSUUID": "",
                  "QueueUUID": "",
                  "DriverOpts": null,
                  "Bandwidth": null,
                  "CInfo": null,
                  "Tag": 0,
                  "PortGroupUUID": "",
                  "PotrGroupName": ""
                },
                "Status": {
                  "code": 33305,
                  "message": "disconnect container ef89fb35-3723-4d7c-838e-7f27831579c0 with network ovs bridge br-int error",
                  "messageCn": "容器ef89fb35-3723-4d7c-838e-7f27831579c0断开连接网络ovs bridge br-int失败",
                  "stack": [
                    "host:192.168.201.187,pid:1512,module:hyper,code:33305,filename:container.go,func:RpcContainerDetachInterface,line:1016"
                  ],
                  "desc": "container ef89fb35-3723-4d7c-838e-7f27831579c0 disconnectOvsBridgePort br-int interface eth9 fail:command:/usr/bin/ovs-vsctl,args:[del-port br-int 0f2bf37357734_l]  fail:command:/usr/bin/ovs-vsctl,args:[del-port br-int 0f2bf37357734_l] fail: exit status 1 ovs-vsctl: no port named 0f2bf37357734_l\n",
                  "UUID": "317d5c65-c6f8-4923-98f5-e638edb5daa4"
                }
              }
            ]
          },
          "StartupConfig": {
            "HostUUID": "",
            "Labels": null,
            "HostIP": ""
          },
          "HasAttachInterface": true
        }
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/container/interface/qos/update
#### 功能：修改容器网卡
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/container/interface/qos/update
```
Body:
```	
{
	"container": {
		"UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
		"ExtraInfo": {
			"Ns": "ed350282-de88-4e2a-98fc-da2029a60138"
		},
		"networkingConfig": {
			"EndpointsConfig": [
				{
					"MacAddress": "52:56:ff:28:b4:e8",
					"QoSUUID": "5f28afa8-e335-4a8c-a289-bcca0167fb8a",
					"QueueUUID": "e67a06fe-8a44-4aa6-85cf-99756832eb44",
					"Bridge": "internal",
					"OvsPortName": "ca2110ac3fdb4_l",
					"Bandwidth": {
						"Outbound": {
							"Peak": 200,
							"Floor": 0
						},
						"Inbound": {
							"Peak": 0,
							"Burst": 0
						}
					}
				}
			]
		}
	},
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
    "TotalCount": 0,
    "Infos": null
  }
}
```

#### 异常返回示例

### 状态码




## /v1/container/logical_switch/connect
#### 功能：容器连接交换机
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/container/logical_switch/connect
```
Body:
```	
{
	"NameSpace": "ed350282-de88-4e2a-98fc-da2029a60138",
	"Mac": "52:56:ff:28:b4:e8",
	"LogicalSwitch": {
		"UUID": "53ffd0c2-6612-4e59-8b23-78f108936248"
	},
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
    "name": "",
    "namespace": "",
    "uuid": ""
  }
}
```

#### 异常返回示例

### 状态码



## /v1/container/logical_switch/disconnect
#### 功能：容器网卡断开交换机
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/container/logical_switch/disconnect
```
Body:
```	
{
	"NameSpace": "ed350282-de88-4e2a-98fc-da2029a60138",
	"Mac": "52:56:ff:28:b4:e8",
	"LogicalSwitch": {
		"UUID": "53ffd0c2-6612-4e59-8b23-78f108936248"
	},
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
    "name": "",
    "namespace": "",
    "uuid": ""
  }
}
```

#### 异常返回示例

### 状态码



## /v1/container/stats
#### 功能：容器统计
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/container/stats
```
Body:
```	
{
	"container": {
		"UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
		"ExtraInfo": {
			"Ns": "ed350282-de88-4e2a-98fc-da2029a60138"
		}
	},
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
    "TotalCount": 1,
    "Infos": [
      {
        "Info": {
          "Name": "u44444bu34444",
          "UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
          "config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": true,
            "OpenStdin": true,
            "StdinOnce": true,
            "Cmd": [
              "/bin/bash"
            ],
            "Healthcheck": null,
            "ArgsEscaped": false,
            "Image": "ubuntu",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "NetworkDisabled": false,
            "MacAddress": "",
            "OnBuild": null,
            "Labels": null,
            "StopSignal": "",
            "StopTimeout": 0,
            "Shell": null,
            "ImageAuthConfig": null,
            "ContainerProbeSpec": null,
            "Env": null,
            "ImagePullPolicy": "Always",
            "ExposedPorts": null,
            "ImageAuthSecret": ""
          },
          "hostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
              "Type": "",
              "Config": null
            },
            "NetworkMode": "",
            "RestartPolicy": {
              "Name": "no",
              "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "thci",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "DNS": null,
            "DNSOptions": null,
            "DNSSearch": null,
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "StorageOpt": null,
            "Tmpfs": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 0,
            "Sysctls": null,
            "Runtime": "",
            "ConsoleSize": null,
            "Isolation": "",
            "Mounts": null,
            "MaskedPaths": null,
            "ReadonlyPaths": null,
            "Init": false,
            "Resource": {
              "CPUShares": 0,
              "Memory": 0,
              "NanoCPUs": 0,
              "CgroupParent": "",
              "BlkioWeight": 0,
              "BlkioWeightDevice": null,
              "BlkioDeviceReadBps": null,
              "BlkioDeviceWriteBps": null,
              "BlkioDeviceReadIOps": null,
              "BlkioDeviceWriteIOps": null,
              "CPUPeriod": 0,
              "CPUQuota": 0,
              "CPURealtimePeriod": 0,
              "CPURealtimeRuntime": 0,
              "CpusetCpus": "",
              "CpusetMems": "",
              "Devices": null,
              "DeviceCgroupRules": null,
              "DiskQuota": 0,
              "KernelMemory": 0,
              "MemoryReservation": 0,
              "MemorySwap": 0,
              "MemorySwappiness": 0,
              "OomKillDisable": false,
              "PidsLimit": 0,
              "Ulimits": null
            },
            "SecretData": null,
            "PortBindings": null
          },
          "networkingConfig": {
            "EndpointsConfig": [
              {
                "IPAMConfig": null,
                "Links": null,
                "Aliases": null,
                "NetworkID": "",
                "EndpointID": "",
                "Gateway": "",
                "IPAddress": "",
                "IPPrefixLen": 0,
                "IPv6Gateway": "",
                "GlobalIPv6Address": "",
                "GlobalIPv6PrefixLen": 0,
                "MacAddress": "52:56:ff:28:b4:e8",
                "Bridge": "br-int",
                "ModelType": "virtio",
                "InterfaceName": "eth3",
                "OvsPortName": "ca2110ac3fdb4_l",
                "Mtu": 0,
                "IFaceUUID": "d9c1bbf5-140b-479f-94ed-6423ef6e41a8",
                "Allocate_Flush": true,
                "QoSUUID": "9fa3e864-ef41-4799-a342-de678c7b4b33",
                "QueueUUID": "7097e13e-6709-4e77-a0c4-744bb7fd12e5",
                "DriverOpts": null,
                "Bandwidth": {
                  "Inbound": {
                    "Peak": 0,
                    "Burst": 0,
                    "Floor": 0
                  },
                  "Outbound": {
                    "Peak": 200,
                    "Burst": 0,
                    "Floor": 0
                  }
                },
                "CInfo": {
                  "Name": "",
                  "UUID": "",
                  "Object": ""
                },
                "Tag": 0,
                "PortGroupUUID": "",
                "PotrGroupName": ""
              }
            ]
          },
          "ExtraInfo": {
            "MachineUUID": "6040ac60-6c0d-46f6-9af6-90e522e41fe9",
            "State": "running",
            "Ns": "ed350282-de88-4e2a-98fc-da2029a60138",
            "CTime": 1573112392,
            "MTime": 1573148402,
            "HostIP": "192.168.201.187",
            "ConsoleSeverListenPort": 5900,
            "HAMode": "on",
            "Action": 0,
            "DeleteTime": 0,
            "Owner": "",
            "ErrorDetail": "",
            "NotHealthy": false
          },
          "ContainerStats": {
            "CPUPercentage": 0,
            "Memory": 2060288,
            "MemoryLimit": 8362168320,
            "MemoryPercentage": 0.02463820292964397,
            "NetworkRx": 0,
            "NetworkTx": 0,
            "BlockRead": 3829760,
            "BlockWrite": 0,
            "PidsCurrent": 1,
            "Time": 1573116016
          },
          "Logs": "",
          "Warnings": null,
          "AttachInterfacesResult": {
            "Success": 1,
            "Fail": 0,
            "Results": [
              {
                "Endpoint": {
                  "IPAMConfig": null,
                  "Links": null,
                  "Aliases": null,
                  "NetworkID": "",
                  "EndpointID": "",
                  "Gateway": "",
                  "IPAddress": "",
                  "IPPrefixLen": 0,
                  "IPv6Gateway": "",
                  "GlobalIPv6Address": "",
                  "GlobalIPv6PrefixLen": 0,
                  "MacAddress": "52:56:ff:28:b4:e8",
                  "Bridge": "br-int",
                  "ModelType": "virtio",
                  "InterfaceName": "eth3",
                  "OvsPortName": "ca2110ac3fdb4_l",
                  "Mtu": 0,
                  "IFaceUUID": "d9c1bbf5-140b-479f-94ed-6423ef6e41a8",
                  "Allocate_Flush": true,
                  "QoSUUID": "",
                  "QueueUUID": "",
                  "DriverOpts": null,
                  "Bandwidth": {
                    "Inbound": {
                      "Peak": 0,
                      "Burst": 0,
                      "Floor": 0
                    },
                    "Outbound": {
                      "Peak": 0,
                      "Burst": 0,
                      "Floor": 0
                    }
                  },
                  "CInfo": {
                    "Name": "",
                    "UUID": "",
                    "Object": ""
                  },
                  "Tag": 0,
                  "PortGroupUUID": "",
                  "PotrGroupName": ""
                },
                "Status": {
                  "code": 0,
                  "message": "",
                  "messageCn": "",
                  "stack": null,
                  "desc": "",
                  "UUID": ""
                }
              }
            ]
          },
          "DetachInterfacesResult": {
            "Success": 0,
            "Fail": 1,
            "Results": [
              {
                "Endpoint": {
                  "IPAMConfig": null,
                  "Links": null,
                  "Aliases": null,
                  "NetworkID": "",
                  "EndpointID": "",
                  "Gateway": "",
                  "IPAddress": "",
                  "IPPrefixLen": 0,
                  "IPv6Gateway": "",
                  "GlobalIPv6Address": "",
                  "GlobalIPv6PrefixLen": 0,
                  "MacAddress": "52:56:ff:77:8e:88",
                  "Bridge": "br-int",
                  "ModelType": "",
                  "InterfaceName": "eth9",
                  "OvsPortName": "0f2bf37357734_l",
                  "Mtu": 0,
                  "IFaceUUID": "",
                  "Allocate_Flush": false,
                  "QoSUUID": "",
                  "QueueUUID": "",
                  "DriverOpts": null,
                  "Bandwidth": null,
                  "CInfo": null,
                  "Tag": 0,
                  "PortGroupUUID": "",
                  "PotrGroupName": ""
                },
                "Status": {
                  "code": 33305,
                  "message": "disconnect container ef89fb35-3723-4d7c-838e-7f27831579c0 with network ovs bridge br-int error",
                  "messageCn": "容器ef89fb35-3723-4d7c-838e-7f27831579c0断开连接网络ovs bridge br-int失败",
                  "stack": [
                    "host:192.168.201.187,pid:1512,module:hyper,code:33305,filename:container.go,func:RpcContainerDetachInterface,line:1016"
                  ],
                  "desc": "container ef89fb35-3723-4d7c-838e-7f27831579c0 disconnectOvsBridgePort br-int interface eth9 fail:command:/usr/bin/ovs-vsctl,args:[del-port br-int 0f2bf37357734_l]  fail:command:/usr/bin/ovs-vsctl,args:[del-port br-int 0f2bf37357734_l] fail: exit status 1 ovs-vsctl: no port named 0f2bf37357734_l\n",
                  "UUID": "317d5c65-c6f8-4923-98f5-e638edb5daa4"
                }
              }
            ]
          },
          "StartupConfig": {
            "HostUUID": "",
            "Labels": null,
            "HostIP": ""
          },
          "HasAttachInterface": true
        }
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/container/log
#### 功能：获取容器日志
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/container/log
```
Body:
```	
{
	"container": {
		"UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
		"ExtraInfo": {
			"Ns": "ed350282-de88-4e2a-98fc-da2029a60138"
		}
	},
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
    "TotalCount": 1,
    "Infos": [
      {
        "Info": {
          "Name": "u44444bu34444",
          "UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
          "config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": true,
            "OpenStdin": true,
            "StdinOnce": true,
            "Cmd": [
              "/bin/bash"
            ],
            "Healthcheck": null,
            "ArgsEscaped": false,
            "Image": "ubuntu",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "NetworkDisabled": false,
            "MacAddress": "",
            "OnBuild": null,
            "Labels": null,
            "StopSignal": "",
            "StopTimeout": 0,
            "Shell": null,
            "ImageAuthConfig": null,
            "ContainerProbeSpec": null,
            "Env": null,
            "ImagePullPolicy": "Always",
            "ExposedPorts": null,
            "ImageAuthSecret": ""
          },
          "hostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
              "Type": "",
              "Config": null
            },
            "NetworkMode": "",
            "RestartPolicy": {
              "Name": "no",
              "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "thci",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "DNS": null,
            "DNSOptions": null,
            "DNSSearch": null,
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "StorageOpt": null,
            "Tmpfs": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 0,
            "Sysctls": null,
            "Runtime": "",
            "ConsoleSize": null,
            "Isolation": "",
            "Mounts": null,
            "MaskedPaths": null,
            "ReadonlyPaths": null,
            "Init": false,
            "Resource": {
              "CPUShares": 0,
              "Memory": 0,
              "NanoCPUs": 0,
              "CgroupParent": "",
              "BlkioWeight": 0,
              "BlkioWeightDevice": null,
              "BlkioDeviceReadBps": null,
              "BlkioDeviceWriteBps": null,
              "BlkioDeviceReadIOps": null,
              "BlkioDeviceWriteIOps": null,
              "CPUPeriod": 0,
              "CPUQuota": 0,
              "CPURealtimePeriod": 0,
              "CPURealtimeRuntime": 0,
              "CpusetCpus": "",
              "CpusetMems": "",
              "Devices": null,
              "DeviceCgroupRules": null,
              "DiskQuota": 0,
              "KernelMemory": 0,
              "MemoryReservation": 0,
              "MemorySwap": 0,
              "MemorySwappiness": 0,
              "OomKillDisable": false,
              "PidsLimit": 0,
              "Ulimits": null
            },
            "SecretData": null,
            "PortBindings": null
          },
          "networkingConfig": {
            "EndpointsConfig": [
              {
                "IPAMConfig": null,
                "Links": null,
                "Aliases": null,
                "NetworkID": "",
                "EndpointID": "",
                "Gateway": "",
                "IPAddress": "",
                "IPPrefixLen": 0,
                "IPv6Gateway": "",
                "GlobalIPv6Address": "",
                "GlobalIPv6PrefixLen": 0,
                "MacAddress": "52:56:ff:28:b4:e8",
                "Bridge": "br-int",
                "ModelType": "virtio",
                "InterfaceName": "eth3",
                "OvsPortName": "ca2110ac3fdb4_l",
                "Mtu": 0,
                "IFaceUUID": "d9c1bbf5-140b-479f-94ed-6423ef6e41a8",
                "Allocate_Flush": true,
                "QoSUUID": "9fa3e864-ef41-4799-a342-de678c7b4b33",
                "QueueUUID": "7097e13e-6709-4e77-a0c4-744bb7fd12e5",
                "DriverOpts": null,
                "Bandwidth": {
                  "Inbound": {
                    "Peak": 0,
                    "Burst": 0,
                    "Floor": 0
                  },
                  "Outbound": {
                    "Peak": 200,
                    "Burst": 0,
                    "Floor": 0
                  }
                },
                "CInfo": {
                  "Name": "",
                  "UUID": "",
                  "Object": ""
                },
                "Tag": 0,
                "PortGroupUUID": "",
                "PotrGroupName": ""
              }
            ]
          },
          "ExtraInfo": {
            "MachineUUID": "6040ac60-6c0d-46f6-9af6-90e522e41fe9",
            "State": "running",
            "Ns": "ed350282-de88-4e2a-98fc-da2029a60138",
            "CTime": 1573112392,
            "MTime": 1573148483,
            "HostIP": "192.168.201.187",
            "ConsoleSeverListenPort": 5900,
            "HAMode": "on",
            "Action": 0,
            "DeleteTime": 0,
            "Owner": "",
            "ErrorDetail": "",
            "NotHealthy": false
          },
          "ContainerStats": {
            "CPUPercentage": 0,
            "Memory": 2060288,
            "MemoryLimit": 8362168320,
            "MemoryPercentage": 0.02463820292964397,
            "NetworkRx": 0,
            "NetworkTx": 0,
            "BlockRead": 3829760,
            "BlockWrite": 0,
            "PidsCurrent": 1,
            "Time": 1573116151
          },
          "Logs": "",
          "Warnings": null,
          "AttachInterfacesResult": {
            "Success": 1,
            "Fail": 0,
            "Results": [
              {
                "Endpoint": {
                  "IPAMConfig": null,
                  "Links": null,
                  "Aliases": null,
                  "NetworkID": "",
                  "EndpointID": "",
                  "Gateway": "",
                  "IPAddress": "",
                  "IPPrefixLen": 0,
                  "IPv6Gateway": "",
                  "GlobalIPv6Address": "",
                  "GlobalIPv6PrefixLen": 0,
                  "MacAddress": "52:56:ff:28:b4:e8",
                  "Bridge": "br-int",
                  "ModelType": "virtio",
                  "InterfaceName": "eth3",
                  "OvsPortName": "ca2110ac3fdb4_l",
                  "Mtu": 0,
                  "IFaceUUID": "d9c1bbf5-140b-479f-94ed-6423ef6e41a8",
                  "Allocate_Flush": true,
                  "QoSUUID": "",
                  "QueueUUID": "",
                  "DriverOpts": null,
                  "Bandwidth": {
                    "Inbound": {
                      "Peak": 0,
                      "Burst": 0,
                      "Floor": 0
                    },
                    "Outbound": {
                      "Peak": 0,
                      "Burst": 0,
                      "Floor": 0
                    }
                  },
                  "CInfo": {
                    "Name": "",
                    "UUID": "",
                    "Object": ""
                  },
                  "Tag": 0,
                  "PortGroupUUID": "",
                  "PotrGroupName": ""
                },
                "Status": {
                  "code": 0,
                  "message": "",
                  "messageCn": "",
                  "stack": null,
                  "desc": "",
                  "UUID": ""
                }
              }
            ]
          },
          "DetachInterfacesResult": {
            "Success": 0,
            "Fail": 1,
            "Results": [
              {
                "Endpoint": {
                  "IPAMConfig": null,
                  "Links": null,
                  "Aliases": null,
                  "NetworkID": "",
                  "EndpointID": "",
                  "Gateway": "",
                  "IPAddress": "",
                  "IPPrefixLen": 0,
                  "IPv6Gateway": "",
                  "GlobalIPv6Address": "",
                  "GlobalIPv6PrefixLen": 0,
                  "MacAddress": "52:56:ff:77:8e:88",
                  "Bridge": "br-int",
                  "ModelType": "",
                  "InterfaceName": "eth9",
                  "OvsPortName": "0f2bf37357734_l",
                  "Mtu": 0,
                  "IFaceUUID": "",
                  "Allocate_Flush": false,
                  "QoSUUID": "",
                  "QueueUUID": "",
                  "DriverOpts": null,
                  "Bandwidth": null,
                  "CInfo": null,
                  "Tag": 0,
                  "PortGroupUUID": "",
                  "PotrGroupName": ""
                },
                "Status": {
                  "code": 33305,
                  "message": "disconnect container ef89fb35-3723-4d7c-838e-7f27831579c0 with network ovs bridge br-int error",
                  "messageCn": "容器ef89fb35-3723-4d7c-838e-7f27831579c0断开连接网络ovs bridge br-int失败",
                  "stack": [
                    "host:192.168.201.187,pid:1512,module:hyper,code:33305,filename:container.go,func:RpcContainerDetachInterface,line:1016"
                  ],
                  "desc": "container ef89fb35-3723-4d7c-838e-7f27831579c0 disconnectOvsBridgePort br-int interface eth9 fail:command:/usr/bin/ovs-vsctl,args:[del-port br-int 0f2bf37357734_l]  fail:command:/usr/bin/ovs-vsctl,args:[del-port br-int 0f2bf37357734_l] fail: exit status 1 ovs-vsctl: no port named 0f2bf37357734_l\n",
                  "UUID": "317d5c65-c6f8-4923-98f5-e638edb5daa4"
                }
              }
            ]
          },
          "StartupConfig": {
            "HostUUID": "",
            "Labels": null,
            "HostIP": ""
          },
          "HasAttachInterface": true
        }
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/container/assign
#### 功能：分配容器
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/container/assign
```
Body:
```	
{
	"container": {
		"UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
		"ExtraInfo": {
			"Ns": "ed350282-de88-4e2a-98fc-da2029a60138",
			"Owner": "ed350282-de88-4e2a-98fc-da2029a60138"
		}
	},
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
    "TotalCount": 0,
    "Infos": [
      {
        "Info": null
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/container/daemon/update
#### 功能： 容器daemon修改
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/container/daemon/update
```
Body:
```	
{
	"BIP": "",
	"DNS": null,
	"DNSOptions": null,
	"DNSSearch": null,
	"LiveRestoreEnabled": true,
	"MaxConcurrentDownloads": {
		"Data": 0
	},
	"MaxConcurrentUploads": {
		"Data": 0
	},
	"InsecureRegistries": null,
	"Registries": null,
	"ShmSize": {
		"Data": 0
	},
	"EnableIPv6": false,
	"FixedCIDRv6": "2001::0/64",
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
    "Status": {
      "code": 0,
      "message": "",
      "messageCn": "",
      "stack": null,
      "desc": "",
      "UUID": ""
    },
    "Hosts": null,
    "Registries": null,
    "InsecureRegistries": null,
    "BIP": "",
    "LiveRestoreEnabled": true,
    "MaxConcurrentDownloads": {
      "Data": 0
    },
    "MaxConcurrentUploads": {
      "Data": 0
    },
    "DNS": null,
    "DNSOptions": null,
    "DNSSearch": null,
    "NeedToRestartDaemon": true,
    "ShmSize": {
      "Data": 0
    },
    "OperateHosts": null,
    "EnableIPv6": false,
    "FixedCIDRv6": "2001::0/64"
  }
}
```

#### 异常返回示例

### 状态码



## /v1/container/daemon/get
#### 功能：获取容器daemon信息
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/container/daemon/get
```
Body:
```	
{
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
    "Status": {
      "code": 0,
      "message": "",
      "messageCn": "",
      "stack": null,
      "desc": "",
      "UUID": ""
    },
    "Hosts": null,
    "Registries": null,
    "InsecureRegistries": null,
    "BIP": "",
    "LiveRestoreEnabled": true,
    "MaxConcurrentDownloads": {
      "Data": 0
    },
    "MaxConcurrentUploads": {
      "Data": 0
    },
    "DNS": null,
    "DNSOptions": null,
    "DNSSearch": null,
    "NeedToRestartDaemon": true,
    "ShmSize": {
      "Data": 0
    },
    "OperateHosts": null,
    "EnableIPv6": false,
    "FixedCIDRv6": "2001::0/64"
  }
}
```

#### 异常返回示例

### 状态码


## /v1/container/daemon/start
#### 功能：重启容器daemon
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/container/daemon/start
```
Body:
```	
{
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
    "success": 3,
    "fail": 0,
    "results": [
      {
        "scode": 0,
        "desc": "",
        "message": "",
        "message_cn": "",
        "stack": [],
        "data": {
          "host_uuid": "07bc76c4-ce06-4383-988d-8dd4ee493012",
          "host_ip": "192.168.201.188"
        }
      },
      {
        "scode": 0,
        "desc": "",
        "message": "",
        "message_cn": "",
        "stack": [],
        "data": {
          "host_uuid": "f6db6e80-642f-4335-8b00-71f84809dfad",
          "host_ip": "192.168.201.186"
        }
      },
      {
        "scode": 0,
        "desc": "",
        "message": "",
        "message_cn": "",
        "stack": [],
        "data": {
          "host_uuid": "6040ac60-6c0d-46f6-9af6-90e522e41fe9",
          "host_ip": "192.168.201.187"
        }
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/container/update/metadata 
#### 功能：修改容器
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
--- |---|---|--- |---
 todo


### 返回参数
名称|参数类型|描述 
---|---|---
 todo


### 示例

#### 请求示例
```
http://localhost:9990/v1/container/update/metadata 
```
Body:
```	
{
	"container": {
		"Name": "u44444bu34444dddd",
		"UUID": "ef89fb35-3723-4d7c-838e-7f27831579c0",
		"config": {
			"Hostname": "",
			"Domainname": "",
			"User": "",
			"AttachStdin": false,
			"AttachStdout": false,
			"AttachStderr": false,
			"Tty": true,
			"OpenStdin": true,
			"StdinOnce": true,
			"Cmd": [
				"/bin/bash"
			],
			"Healthcheck": null,
			"ArgsEscaped": false,
			"Image": "ubuntu",
			"Volumes": null,
			"WorkingDir": "",
			"Entrypoint": null,
			"NetworkDisabled": false,
			"MacAddress": "",
			"OnBuild": null,
			"Labels": null,
			"StopSignal": "",
			"StopTimeout": 0,
			"Shell": null,
			"ImageAuthConfig": null,
			"ContainerProbeSpec": null,
			"Env": null,
			"ImagePullPolicy": "Always",
			"ExposedPorts": null,
			"ImageAuthSecret": ""
		},
		"hostConfig": {
			"Binds": null,
			"ContainerIDFile": "",
			"LogConfig": {
				"Type": "",
				"Config": null
			},
			"NetworkMode": "",
			"RestartPolicy": {
				"Name": "no",
				"MaximumRetryCount": 0
			},
			"AutoRemove": false,
			"VolumeDriver": "thci",
			"VolumesFrom": null,
			"CapAdd": null,
			"CapDrop": null,
			"DNS": null,
			"DNSOptions": null,
			"DNSSearch": null,
			"ExtraHosts": null,
			"GroupAdd": null,
			"IpcMode": "",
			"Cgroup": "",
			"Links": null,
			"OomScoreAdj": 0,
			"PidMode": "",
			"Privileged": false,
			"PublishAllPorts": false,
			"ReadonlyRootfs": false,
			"SecurityOpt": null,
			"StorageOpt": null,
			"Tmpfs": null,
			"UTSMode": "",
			"UsernsMode": "",
			"ShmSize": 0,
			"Sysctls": null,
			"Runtime": "",
			"ConsoleSize": null,
			"Isolation": "",
			"Mounts": null,
			"MaskedPaths": null,
			"ReadonlyPaths": null,
			"Init": false,
			"Resource": {
				"CPUShares": 0,
				"Memory": 0,
				"NanoCPUs": 0,
				"CgroupParent": "",
				"BlkioWeight": 0,
				"BlkioWeightDevice": null,
				"BlkioDeviceReadBps": null,
				"BlkioDeviceWriteBps": null,
				"BlkioDeviceReadIOps": null,
				"BlkioDeviceWriteIOps": null,
				"CPUPeriod": 0,
				"CPUQuota": 0,
				"CPURealtimePeriod": 0,
				"CPURealtimeRuntime": 0,
				"CpusetCpus": "",
				"CpusetMems": "",
				"Devices": null,
				"DeviceCgroupRules": null,
				"DiskQuota": 0,
				"KernelMemory": 0,
				"MemoryReservation": 0,
				"MemorySwap": 0,
				"MemorySwappiness": 0,
				"OomKillDisable": false,
				"PidsLimit": 0,
				"Ulimits": null
			},
			"SecretData": null,
			"PortBindings": null
		},
		"networkingConfig": {
			"EndpointsConfig": [
				{
					"IPAMConfig": null,
					"Links": null,
					"Aliases": null,
					"NetworkID": "",
					"EndpointID": "",
					"Gateway": "",
					"IPAddress": "",
					"IPPrefixLen": 0,
					"IPv6Gateway": "",
					"GlobalIPv6Address": "",
					"GlobalIPv6PrefixLen": 0,
					"MacAddress": "52:56:ff:28:b4:e8",
					"Bridge": "internal",
					"ModelType": "virtio",
					"InterfaceName": "eth3",
					"OvsPortName": "ca2110ac3fdb4_l",
					"Mtu": 0,
					"IFaceUUID": "d9c1bbf5-140b-479f-94ed-6423ef6e41a8",
					"Allocate_Flush": true,
					"QoSUUID": "9fa3e864-ef41-4799-a342-de678c7b4b33",
					"QueueUUID": "7097e13e-6709-4e77-a0c4-744bb7fd12e5",
					"DriverOpts": null,
					"Bandwidth": {
						"Inbound": {
							"Peak": 0,
							"Burst": 0,
							"Floor": 0
						},
						"Outbound": {
							"Peak": 200,
							"Burst": 0,
							"Floor": 0
						}
					},
					"CInfo": {
						"Name": "aaa",
						"UUID": "53ffd0c2-6612-4e59-8b23-78f108936248",
						"Object": "switch"
					},
					"Tag": 0,
					"PortGroupUUID": "",
					"PotrGroupName": ""
				}
			]
		},
		"ExtraInfo": {
			"MachineUUID": "6040ac60-6c0d-46f6-9af6-90e522e41fe9",
			"State": "exited",
			"Ns": "ed350282-de88-4e2a-98fc-da2029a60138",
			"CTime": 1573112392,
			"MTime": 1573148957,
			"HostIP": "192.168.201.187",
			"ConsoleSeverListenPort": 5900,
			"HAMode": "on",
			"Action": 0,
			"DeleteTime": 0,
			"Owner": "",
			"ErrorDetail": "",
			"NotHealthy": false
		},
		"ContainerStats": {
			"CPUPercentage": 0,
			"Memory": 2060288,
			"MemoryLimit": 8362168320,
			"MemoryPercentage": 0.02463820292964397,
			"NetworkRx": 0,
			"NetworkTx": 0,
			"BlockRead": 3829760,
			"BlockWrite": 0,
			"PidsCurrent": 1,
			"Time": 1573116211
		},
		"Logs": "",
		"Warnings": null,
		"AttachInterfacesResult": {
			"Success": 1,
			"Fail": 0,
			"Results": [
				{
					"Endpoint": {
						"IPAMConfig": null,
						"Links": null,
						"Aliases": null,
						"NetworkID": "",
						"EndpointID": "",
						"Gateway": "",
						"IPAddress": "",
						"IPPrefixLen": 0,
						"IPv6Gateway": "",
						"GlobalIPv6Address": "",
						"GlobalIPv6PrefixLen": 0,
						"MacAddress": "52:56:ff:28:b4:e8",
						"Bridge": "br-int",
						"ModelType": "virtio",
						"InterfaceName": "eth3",
						"OvsPortName": "ca2110ac3fdb4_l",
						"Mtu": 0,
						"IFaceUUID": "d9c1bbf5-140b-479f-94ed-6423ef6e41a8",
						"Allocate_Flush": true,
						"QoSUUID": "",
						"QueueUUID": "",
						"DriverOpts": null,
						"Bandwidth": {
							"Inbound": {
								"Peak": 0,
								"Burst": 0,
								"Floor": 0
							},
							"Outbound": {
								"Peak": 0,
								"Burst": 0,
								"Floor": 0
							}
						},
						"CInfo": {
							"Name": "",
							"UUID": "",
							"Object": ""
						},
						"Tag": 0,
						"PortGroupUUID": "",
						"PotrGroupName": ""
					},
					"Status": {
						"code": 0,
						"message": "",
						"messageCn": "",
						"stack": null,
						"desc": "",
						"UUID": ""
					}
				}
			]
		},
		"DetachInterfacesResult": {
			"Success": 0,
			"Fail": 1,
			"Results": [
				{
					"Endpoint": {
						"IPAMConfig": null,
						"Links": null,
						"Aliases": null,
						"NetworkID": "",
						"EndpointID": "",
						"Gateway": "",
						"IPAddress": "",
						"IPPrefixLen": 0,
						"IPv6Gateway": "",
						"GlobalIPv6Address": "",
						"GlobalIPv6PrefixLen": 0,
						"MacAddress": "52:56:ff:77:8e:88",
						"Bridge": "br-int",
						"ModelType": "",
						"InterfaceName": "eth9",
						"OvsPortName": "0f2bf37357734_l",
						"Mtu": 0,
						"IFaceUUID": "",
						"Allocate_Flush": false,
						"QoSUUID": "",
						"QueueUUID": "",
						"DriverOpts": null,
						"Bandwidth": null,
						"CInfo": null,
						"Tag": 0,
						"PortGroupUUID": "",
						"PotrGroupName": ""
					},
					"Status": {
						"code": 33305,
						"message": "disconnect container ef89fb35-3723-4d7c-838e-7f27831579c0 with network ovs bridge br-int error",
						"messageCn": "容器ef89fb35-3723-4d7c-838e-7f27831579c0断开连接网络ovs bridge br-int失败",
						"stack": [
							"host:192.168.201.187,pid:1512,module:hyper,code:33305,filename:container.go,func:RpcContainerDetachInterface,line:1016"
						],
						"desc": "container ef89fb35-3723-4d7c-838e-7f27831579c0 disconnectOvsBridgePort br-int interface eth9 fail:command:/usr/bin/ovs-vsctl,args:[del-port br-int 0f2bf37357734_l]  fail:command:/usr/bin/ovs-vsctl,args:[del-port br-int 0f2bf37357734_l] fail: exit status 1 ovs-vsctl: no port named 0f2bf37357734_l\n",
						"UUID": "317d5c65-c6f8-4923-98f5-e638edb5daa4"
					}
				}
			]
		},
		"StartupConfig": {
			"HostUUID": "",
			"Labels": null,
			"HostIP": ""
		},
		"HasAttachInterface": true
	},
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
    "TotalCount": 0,
    "Infos": [
      {
        "Info": null
      }
    ]
  }
}
```

#### 异常返回示例

### 状态码









