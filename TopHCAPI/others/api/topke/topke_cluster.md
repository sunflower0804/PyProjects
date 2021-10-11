[back to api overview](../api_overview.md#topke_cluster)

### 容器云集群接口
## /v1/topke/cluster/deploy
部署容器云集群
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant_uuid|string|是|""|租户uuid
name|string|是|""|集群名
desc|string|否|""|描述
cluster_node_scale|string|是|""|集群工作节点规模
master_list|string array|是|[]|master节点列表
node_list|string array|是|[]|工作节点列表
RegistryConfig|struct|否|{}|镜像仓库配置
KubernetesVersion|string|是|""|k8s集群版本
ServicePodCidr|string|否|""|服务网段
PodCidr|string|否|""|容器组网段
ControlPlaneConfig|struct|否|""|控制面板配置
use_managed_registry_project|struct|是|{}|使用已纳管的镜像仓库
### 返回参数

名称|参数类型|描述
---|---|---




### 示例

#### 请求示例
https://10.30.100.178/v1/topke/cluster/deploy
```
{
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"name": "newk8s1",
	"desc": "",
	"cluster_node_scale": "medium",
	"master_list": [{
		"IP": "10.30.100.68",
		"NodeName": "k8s-node-10-30-100-68"
	}],
	"node_list": [{
		"IP": "10.30.100.78",
		"NodeName": "k8s-node-10-30-100-78"
	}],
	"RegistryConfig": {
		"RegistryAddress": "",
		"Project": "",
		"User": "",
		"Password": ""
	},
	"KubernetesVersion": "v1.18.0",
	"ServicePodCidr": "",
	"PodCidr": "",
	"ControlPlaneConfig": {
		"KubeProxyConfig": {
			"Mode": "iptables"
		}
	},
	"use_managed_registry_project": {
		"registry_uuid": "9cbd63e0-2d42-4e52-bb5e-80b861cc868a",
		"project_name": "newk8s"
	}
}
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "",
  "message_cn": "",
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
    "uuid": "f4a4f4f1-e3d7-498e-b1d3-f72449f27c1f"
  }
}
```

## /v1/topke/cluster/deploy/status/inspect
获取容器云集群部署状态
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
uuid|string|否|""|集群uuid
### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
https://10.30.100.178/v1/topke/cluster/deploy/status/inspect?uuid=f4a4f4f1-e3d7-498e-b1d3-f72449f27c1f

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "",
  "message_cn": "",
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
    "DeployStage": {
      "Name": "topke_deploy_newk8s1",
      "Stages": [
        {
          "name": "init node status",
          "name_cn": "注册集群信息到部署节点",
          "start_time": 1630044538,
          "end_time": 1630044538,
          "success": true,
          "error": null,
          "is_finish": true
        },
        {
          "name": "setup masters",
          "name_cn": "部署管理节点, 该过程会持续4-6分钟",
          "start_time": 1630044538,
          "end_time": 0,
          "success": false,
          "error": null,
          "is_finish": false
        },
        {
          "name": "update cluster certificate",
          "name_cn": "更新集群证书",
          "start_time": 0,
          "end_time": 0,
          "success": false,
          "error": null,
          "is_finish": false
        },
        {
          "name": "setup workers",
          "name_cn": "部署工作节点",
          "start_time": 0,
          "end_time": 0,
          "success": false,
          "error": null,
          "is_finish": false
        }
      ],
      "CurrentStage": 1,
      "State": "running"
    },
    "RegistryConfig": {
      "RegistryAddress": "https://10.30.100.155",
      "Project": "newk8s",
      "User": "admin",
      "Password": "",
      "TlsConfig": null
    },
    "KubernetesVersion": "v1.18.0",
    "ServicePodCidr": "10.96.0.0/12",
    "ServiceDnsDomain": "",
    "ControlPlaneConfig": {
      "ConfigYaml": "",
      "NetworkPluginConfig": {
        "PluginType": "calico",
        "ContainerRegistry": null,
        "CalicoConfig": {
          "Version": "v3.14"
        }
      },
      "HAConfig": null,
      "MonitorPluginConfig": {
        "ContainerRegistry": null
      },
      "KubectlPluginConfig": {
        "ContainerRegistry": null
      },
      "RegistryDistributePluginConfig": {
        "ContainerRegistry": null
      },
      "KubeProxyConfig": {
        "Mode": "iptables"
      },
      "StoragePluginConfig": {
        "ContainerRegistry": null,
        "LocalStorage": {},
        "NfsStoragePluginConfig": {},
        "TopkeStoragePluginConfig": {},
        "CephStoragePluginConfig": {}
      },
      "NamespaceControllerPluginConfig": {
        "ContainerRegistry": null
      }
    },
    "WorkerConfig": null,
    "OwnerInfo": {
      "ClusterUUID": "f4a4f4f1-e3d7-498e-b1d3-f72449f27c1f",
      "ClusterName": "newk8s1",
      "ExtraMessage": ""
    },
    "NodeConfig": null,
    "EtcdDatabaseBackupPolicy": null,
    "PodCidr": "192.168.0.0/16",
    "DataBaseConfig": null,
    "tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
    "uuid": "f4a4f4f1-e3d7-498e-b1d3-f72449f27c1f",
    "master_list": [
      {
        "IP": "10.30.100.68",
        "NodeName": "k8s-node-10-30-100-68",
        "Priority": 0
      }
    ],
    "node_list": [
      {
        "IP": "10.30.100.78",
        "NodeName": "k8s-node-10-30-100-78",
        "Priority": 0
      }
    ],
    "name": "newk8s1",
    "desc": "",
    "creat_time": 1630044537,
    "is_over": false,
    "err_info": "",
    "total_status": [
      {
        "time": 1630044538,
        "addr": "10.30.100.68",
        "message": "deploying"
      },
      {
        "time": 1630044538,
        "addr": "10.30.100.78",
        "message": "uninitialized"
      }
    ],
    "use_managed_registry_project": {
      "registry_uuid": "9cbd63e0-2d42-4e52-bb5e-80b861cc868a",
      "project_name": "newk8s"
    },
    "max_not_failure_worker_node_num": null,
    "cluster_node_scale": "medium"
  }
}
```

## /v1/topke/cluster/host/scan
扫描可用的容器云主机节点
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
begin|string|是|""|起始IP
end|string|是|""|结束IP
### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
https://10.30.100.178/v1/topke/cluster/host/scan

```
{
	"begin": "10.30.100.10",
	"end": "10.30.100.200",
}
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "",
  "message_cn": "",
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
    "hosts_info": [
      {
        "ip": "10.30.100.77",
        "host_name": "TOS-10077",
        "version": "3.3.0.rc1  @go1.15.1 linux/amd64  SRC#c1d13a0bd1a10eb3364ada4bb4666b5953f03d2d  CMN#521f229a67a4cd884daddd5d79c0bee7819dfcb9",
        "host_info": {
          "CpuInfo": {
            "Cores": 8
          },
          "VirtualMemoryInfo": {
            "Total": 12412125184
          }
        }
      }
    ],
    "total_count": 1
  }
}
```

## /v1/topke/cluster/vip/test
测试虚拟IP是否可用
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
vip|string|是|""|虚拟IP
port|int|是|0|对外端口，不能使用6443
### 返回参数

名称|参数类型|描述
---|---|---


### 示例
 
#### 请求示例
https://10.30.100.178/v1/topke/cluster/vip/test
```
{
 "vip": "10.30.100.15",
 "port": 6443,
}
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "",
  "message_cn": "",
  "stack": null,
  "data":null 
}
```
## /v1/topke/cluster/deploy/node/create
部署一个集群节点
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---

### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
https://10.30.100.178/v1/topke/cluster/deploy/node/create
```
{
	"uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"node_list": [{
		"IP": "10.30.100.68",
		"NodeName": "new-node-10-30-100-68"
	}],
	"use_managed_registry_project": {
		"registry_uuid": "9cbd63e0-2d42-4e52-bb5e-80b861cc868a",
		"project_name": "newk8s"
	}
}
```

#### 正常返回示例


## /v1/topke/cluster/add
纳管已存在集群
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
Name|string|是|""|集群名
kube_config_data|string|是|""|集群kubeconfig配置
### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/cluster/add
```
{
	"Name": "2.5",
	"kube_config_data": "77u/YXBpVmVyc2lvbjogdjEKY2x1c3RlcnM6Ci0gY2x1c3RlcjoKICAgIGNlcnRpZmljYXRlLWF1dGhvcml0eS1kYXRhOiBMUzB0TFMxQ1JVZEpUaUJEUlZKVVNVWkpRMEZVUlMwdExTMHRDazFKU1VONVJFTkRRV0pEWjBGM1NVSkJaMGxDUVVSQlRrSm5hM0ZvYTJsSE9YY3dRa0ZSYzBaQlJFRldUVkpOZDBWUldVUldVVkZFUlhkd2NtUlhTbXdLWTIwMWJHUkhWbnBOUWpSWVJGUkplRTFFWTNsT2VrRjZUWHBuZDA1R2IxaEVWRTE0VFVSamVVNVVRWHBOZW1kM1RrWnZkMFpVUlZSTlFrVkhRVEZWUlFwQmVFMUxZVE5XYVZwWVNuVmFXRkpzWTNwRFEwRlRTWGRFVVZsS1MyOWFTV2gyWTA1QlVVVkNRbEZCUkdkblJWQkJSRU5EUVZGdlEyZG5SVUpCUzJvNUNqQnBSVzQ0UnpWelRuQkxZa1Z5YVVoUWF6bDBSbU5OYldOaGFWVnpWVTkyUWtaWllsWXZZVTF2WjBSRmJHbHdWRlJJZVZsS2FqaDVPREpUUW1SM1RXMEtaRkZ4UlVjM2VXcFpZMXBqZGpod1dEVmtlVFU0ZW1aUVNVNVBaRk5oVVd0aFRGSmFTV3A0T1dWc2JWcFFUbmx5VEVaMlFtcEJhRTlrUVV0MU5YaE5SUXB6TmpoTFoyVTViMDlMUVZaVVUwZHRXWFp2TURGclJtOHZlakZEWldaVlQzQTFiV3BUYTJ4VUsxSXljamwxVVhWVmQyUkhOMGxNVHpkMllsbHNiMEZEQ2tkelJYQmpObFJ1Y1dscWFITTJNMjl3Ynk5TGFXVnNWRkpPWjBwdGQxSXdOM3B0YjA1d1EzSkZORUZyYXpkeVFsaERSbFprTkc5UFYwaGpaMHBEV2prS1dURkZXR0ZPWlVWclJHNDFjMVpRYTJWdlN5dFJabVJQTVZGdU4xUlRiakZ4UjA5bVVVRnFSVEp5WVdReGRWRkJNWG8yVTNnek1GcFNPVTFTUnk5TU1BcDZhekU1YTJWdmRWaHdTVk5SVEZWWGJuaHpRMEYzUlVGQllVMXFUVU5GZDBSbldVUldVakJRUVZGSUwwSkJVVVJCWjB0clRVRTRSMEV4VldSRmQwVkNDaTkzVVVaTlFVMUNRV1k0ZDBSUldVcExiMXBKYUhaalRrRlJSVXhDVVVGRVoyZEZRa0ZLUWpkSldqQmhSRU5HZDNCaWRUTnBkVnB6YW5VdlJuTlBTbkFLYzJKRWEzWnJhVFJ0TVZRNFdVeGFNelV6YWxSQmQyeDBNbmR3ZDNWUGJXbHpWbVpyYkhSRmVtWmhVVXRPWkVodU5VOVBibkl4VkNzNWNUZFlZM1Z3WlFvdlUyNTVkbFZOYTFZM2MwUktZa0ozYzJ0elZtcEVLelpZVEVSa1lVZEdkR1JEY1VSRmRrRlRUa3BPWnpKWFIwSkpZV1F5Y1hKd1pHc3hiWGxIU3pSMUNsRlVWVzVFWVhsdFRFMXRTRk5WTkN0MFNqVjBTaTkzVWtoUWRFcEVhMVZKTm1oTWNWQmpVa3hTVW5RM1NGbHZiSFJ2YW5kSFpIbEtiVTlEUjBOblQxSUtORll2WVdwbFMyWTNOekYwUW5oekwzQlFabTR2TmpnNGJIcHdXSGt4T0hGRlltc3lNekI2TmxKWU5YbG5jUzh3VUN0eU9WUk9lVEZtWm1GcFRscEJWUXB2TUVSdldYUkxkbUVyY0RRd2FEWjZZVXBCYVhoQ1lUQXpaRFZvV0RGVmExaHpTRTlzWTBoWWVpOUNkVWxCUzJZd1FVSlpSMXA0U2tZNGR6MEtMUzB0TFMxRlRrUWdRMFZTVkVsR1NVTkJWRVV0TFMwdExRbz0KICAgIHNlcnZlcjogaHR0cHM6Ly8xMC4zMC4xMDAuMTExOjg0NDMKICBuYW1lOiBrdWJlcm5ldGVzCmNvbnRleHRzOgotIGNvbnRleHQ6CiAgICBjbHVzdGVyOiBrdWJlcm5ldGVzCiAgICB1c2VyOiBrdWJlcm5ldGVzLWFkbWluCiAgbmFtZToga3ViZXJuZXRlcy1hZG1pbkBrdWJlcm5ldGVzCmN1cnJlbnQtY29udGV4dDoga3ViZXJuZXRlcy1hZG1pbkBrdWJlcm5ldGVzCmtpbmQ6IENvbmZpZwpwcmVmZXJlbmNlczoge30KdXNlcnM6Ci0gbmFtZToga3ViZXJuZXRlcy1hZG1pbgogIHVzZXI6CiAgICBjbGllbnQtY2VydGlmaWNhdGUtZGF0YTogTFMwdExTMUNSVWRKVGlCRFJWSlVTVVpKUTBGVVJTMHRMUzB0Q2sxSlNVTTRha05EUVdSeFowRjNTVUpCWjBsSlVXWm1abmhhUXpBNGVsbDNSRkZaU2t0dldrbG9kbU5PUVZGRlRFSlJRWGRHVkVWVVRVSkZSMEV4VlVVS1FYaE5TMkV6Vm1sYVdFcDFXbGhTYkdONlFXVkdkekI1VFZSQk0wMXFZM2ROZWswMFRVUlNZVVozTUhsTmFrRXpUV3BqZDAxNlVYaE5WRTVoVFVSUmVBcEdla0ZXUW1kT1ZrSkJiMVJFYms0MVl6TlNiR0pVY0hSWldFNHdXbGhLZWsxU2EzZEdkMWxFVmxGUlJFVjRRbkprVjBwc1kyMDFiR1JIVm5wTVYwWnJDbUpYYkhWTlNVbENTV3BCVGtKbmEzRm9hMmxIT1hjd1FrRlJSVVpCUVU5RFFWRTRRVTFKU1VKRFowdERRVkZGUVRWWFQwRXlablJGUnpKMU9HZDNlRmtLYUcxSVZrbHJlSGxZZUVvd1pIUXhZbWRRVldocE5VUnFMekF6TTNOcU5FTnRPV2h6U2xkVFQyWnpObWt4ZGpoSVQxZHhTWFZNTld0RFFXZDZOWEJsY2dwdFFtcEZlblp6UW1WdGVsSlNTemhOU1dKclIzWk1RWEZEY205dVJrRTBLM0phVTFSR2QyNVVOalZTZEZCRGFFaHNiRWhVWlVsbk4zbG9TSEJVTm1kMUNuWXlTVkJaVmpBMU9VVnRVVFJtUzFCRVF6aERiRFJoTldSdFduVlFXRzlxTW1FeFptVnJaa1p1VDJoVFdIb3lkRkZzTjJoNU16SjJLMEZhZVVadVVEQUtNR2xGV1haamQzRkZVemRqWkZWR1lTOWxkMWd3ZW1velYxaE5ORVZPY3pCV2JVWk5jV1V4V0ZwSVNuWXdUV0Z4TVZkcE4xUndNakp1UVhOcE5qTm9Ud3BtZUcxTlpYWTJRV05CTkM5VE5sZDBOa3QwWTJKalVUZDVkVTR4YlhaUlVsRmxkV0ZoTjJadlVreFFTRUZWWTNnMWVVNHlURUZ6UnpGWVFrYzBUVVV2Q2pJMGFreDVkMGxFUVZGQlFtOTVZM2RLVkVGUFFtZE9Wa2hST0VKQlpqaEZRa0ZOUTBKaFFYZEZkMWxFVmxJd2JFSkJkM2REWjFsSlMzZFpRa0pSVlVnS1FYZEpkMFJSV1VwTGIxcEphSFpqVGtGUlJVeENVVUZFWjJkRlFrRkZObm93VVhSSU5WbGtkVEZWTnpOMVVuZ3dTMFpVYjI4dksxUTRkazVxTTFGTE5BbzNMMDlaYlV4VU1IZFRhRGc1WlZaVVNEazBVVlpMUkRsWFFsTlhWM2hXUXpaa2FUSTJZbmxCU3l0ek1HbzVXRTFXY1dsa2RHbzJlR3hDTVdsd1ZYZENDakIzUlUxQlpHMTBibEpPTUhSeE5tdENNeXRZYm5Cb2QwWkJNMnRQYm5oTU1GWmxLMFpVYW01SmFsUTRiMEV6UkhVMk5XMXpjWHBKWWs1bU1IRjBaemdLWWs1RWJURkVkRmhGU0hkRVNtaG5aMkZtZHl0bFIzRlJPRlpvV200NGRtTlRZV3QyTmtOMFExWnRhRTVLVUVkeE1XWm5SRXhxVlhjNGJHVlRUVTVCZGdwRmQyWkRVMjVwZFVGUlRtNXVWM1pPUmxWYVpGbDZNVVIzWVV0NWVVNVJVRXBpZGtJMmFXdHpWaTlWY2xSS05uaDZVaTh6YkRCMk1YTnpVMHR6SzFaVkNpOVBhMHRoY1U4eFZHTTJNVE5KV0VGemJWaFlVVkp6VUVGV2FEZHZRbXAyTkVnNFZTOUNRbVJ3YjB0RlpXUnJkRGR0VFQwS0xTMHRMUzFGVGtRZ1EwVlNWRWxHU1VOQlZFVXRMUzB0TFFvPQogICAgY2xpZW50LWtleS1kYXRhOiBMUzB0TFMxQ1JVZEpUaUJTVTBFZ1VGSkpWa0ZVUlNCTFJWa3RMUzB0TFFwTlNVbEZiM2RKUWtGQlMwTkJVVVZCTlZkUFFUSm1kRVZITW5VNFozZDRXV2h0U0ZaSmEzaDVXSGhLTUdSME1XSm5VRlZvYVRWRWFpOHdNek56YWpSRENtMDVhSE5LVjFOUFpuTTJhVEYyT0VoUFYzRkpkVXcxYTBOQlozbzFjR1Z5YlVKcVJYcDJjMEpsYlhwU1VrczRUVWxpYTBkMlRFRnhRM0p2YmtaQk5Dc0tjbHBUVkVaM2JsUTJOVkowVUVOb1NHeHNTRlJsU1djM2VXaEljRlEyWjNWMk1rbFFXVll3TlRsRmJWRTBaa3RRUkVNNFEydzBZVFZrYlZwMVVGaHZhZ295WVRGbVpXdG1SbTVQYUZOWWVqSjBVV3czYUhrek1uWXJRVnA1Um01UU1EQnBSVmwyWTNkeFJWTTNZMlJWUm1FdlpYZFlNSHBxTTFkWVRUUkZUbk13Q2xadFJrMXhaVEZZV2toS2RqQk5ZWEV4VjJrM1ZIQXlNbTVCYzJrMk0yaFBabmh0VFdWMk5rRmpRVFF2VXpaWGREWkxkR05pWTFFM2VYVk9NVzEyVVZJS1VXVjFZV0UzWm05U1RGQklRVlZqZURWNVRqSk1RWE5ITVZoQ1J6Uk5SUzh5TkdwTWVYZEpSRUZSUVVKQmIwbENRVU4zUVVWVFp5czNWWEZDVDFCREt3cFFiMFJSV2xWNWJEZ3dOVkJSVHpOSUsyaFNZbU5QY2xCcFVuaG5kbFZIUVdGWmJYaFZkRlU1VnpaUWVGTlJWVXRsUkRGSlRsSXJVM3BoWkVsM05GQlpDakZtTldaNVpXbFdPWGwxWm10bGFXd3hlVXhyTVdWcU9YUmhURWhKUmxoV1oyRndWVVpJTjFnd1RVZG5aaXNyU2todGJ6QkhaV1JHTkc5dldrMHpTMjRLU2xGb2NUWTVOVmRRY0dGblVXUXhSbHBNUlVkc01qSjJWbmRZYUhSUk5GTnZOR1pyUmt0T1RXVlFjM2M0WlhWd2VWQjJPRTFDZVZOSFUycE9VMWxWUmdwUVpVRjNUWHBpVlZOdVZGZE5UbkJsSzBaR2FIcHhRMmhuTUUwemJsaFhWR3QyTDJ0V01ETkxkVXRXUkhsUVRYQnNOM05STTFwR2VUVmtXbEpJZEhOMkNuaGxjMnhrVUhWVVFUSTFObVZ2TkhaYVRqZE1TVk12ZWxGbmJ5czBUWGhYU0U1SWRWaElVR0YzTVhWeFlVNTJTRFpwTTFkdmRHbFVhREZCUm1kc0szQUtNbWRqYjJVMVJVTm5XVVZCT0RKSGVqTndSVk5DZFhScmRIaFFTVWxtT0U1aWFGWnVSVE5CYzNweUwxQjNZazR3WlhBMVdVbzJlVFJ5UVVjemVFZDZiZ292T0dSUldFd3lTMEpzZUdKdVZEbGxaSHA1Wm5CTGF6TkNORXRCYzBaeFMxbGhhWEJyV21SNGJtaFFSalk0UlZOSWIwSnljV1YxUjJsaFowRmxOMlJvQ2xKTlpWcDViVlJXT1dsS2IxQm5NMVJGVlhCS0sydHFOWHAwTkdOdVRsbEVLMmgyZVN0eWFFNXNhRVJYUWxkNmJtbDNRMlJ0VlUxRFoxbEZRVGhWWjFVS1FqVjNVbGRNUm0wclMwWnRlV3BKVFdjM2IwaFBSWFl2WVVaaVJtVnBXakZ5U1RNd05XMXdhVkZZTmt0SFlVWkZkSEJUTVd3clRHWkhkWGxsZEZaUmNRcEhPVE5uTTNWM01HRXhMM1F2ZUc0MVYySmxlbHBzY1d4NVdXcG9NVmxOYzNkblpIa3lTamczUkdReFYwZFBOMVZHU0U1U09XNHlVbXBpU20xblZ6SXZDakJYT0ZaMGRuSnVNR3RsWlM5dmRIbHhkWE5XWWt0dVRYUXdlQzlWTTA0MmMxWnZkbVIwYTBObldVRXhTbGRYYjNWV1kwNWhZMDlvWTNSR2JVVjRUREFLYzJadVJFNWxRMmtyVTBjNU9EVnJRVEpoYWpSaFVFRmxjRE5XWjJ0RlQwNURRa2xXV0d4S1VXd3dVblZNZUU1TGVVWk5ORWR5Wkc5cVYyWmhiWEp5VkFwSWIybEJkMWRvVUVVMVVrcHhaWGg0SzNGelNDOVBWbmhGT1RKbVNtMXJORWx5YjBSb01HUjBjWGN2UjFaVVFqZ3JlRXg1WXpWTlVsTkdSa3BOYW1KSENrY3JjRkZOTkZSR2RUQkdlRUk1YmpjNFdrNDBhbmRMUW1kSEwyTnhkWGxqVUhFMlVVVk9NVlZrZDA1dVJVMWFRbWxRWkdkNFNtcHlTV05NZGpoaU5Tc0tWV1o0UW1ScGVFaE1iQ3RVYkZCbVVrZG9MMEV6ZHpkemFFOW5jMnBTYXl0V1VFMUdURFJvV1dkVk5qQkVRbUU0VWtWQkx6VnVlalZMVkhGRlFtdDNkUXBvSzBKSFkyMXhURWt3SzB3MmJXUlJlamM0Ym0xRlVFcFphSGt2WkZJM01FVlhNREJDYVZwSVltbzRNVUkwVTFkWFQyZzBSVXRGY1hCb01XRm1TbVZqQ2paRlUwSkJiMGRDUVVwbllrNTZhMnhYTHk5M01tdFlkVEJ1Y1RKNVMxVlpkbmN5UWt0MlZuSTJlR1ZrZDB0ck1HZFNRMkpsZDJkNWFYWjVVamRNWm1JS1pIUXdSMGdyT0ZGdU4xcHZNM2xwTlU1dFowYzJiRFYzV0VkemNrMVRZVEF5Vlc1Uk1uZFRZVUY1VWxaTlIxWlpXQ3QyWVhCb1RWUTJTMnhCUkRKcWRRcGxTM2xTUkdaT01HRmpibFZhY0c5dlNHcDVUMnhpT1d0NlNFNUlUR2Q1SzJGRE1uWXlVbFZEUWpsVEsxSmpXV1oxSzBSVkNpMHRMUzB0UlU1RUlGSlRRU0JRVWtsV1FWUkZJRXRGV1MwdExTMHRDZz09Cg==",
}
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "",
  "message_cn": "",
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
    "TotalCount": 1,
    "Infos": [
      {
        "UUID": "7c8602b3-f879-48a7-a3d0-c0137eb8ea7c",
        "Name": "2.5",
        "Config": {
          "Host": "https://10.30.100.111:8443",
          "APIPath": "",
          "Username": "",
          "Password": "",
          "BearerToken": "",
          "BearerTokenFile": "",
          "TlsClientConfig": {
            "Insecure": false,
            "ServerName": "",
            "CertFile": "",
            "KeyFile": "",
            "CAFile": "",
            "CertData": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUM4akNDQWRxZ0F3SUJBZ0lJUWZmZnhaQzA4ell3RFFZSktvWklodmNOQVFFTEJRQXdGVEVUTUJFR0ExVUUKQXhNS2EzVmlaWEp1WlhSbGN6QWVGdzB5TVRBM01qY3dNek00TURSYUZ3MHlNakEzTWpjd016UXhNVE5hTURReApGekFWQmdOVkJBb1REbk41YzNSbGJUcHRZWE4wWlhKek1Sa3dGd1lEVlFRREV4QnJkV0psY201bGRHVnpMV0ZrCmJXbHVNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQTVXT0EyZnRFRzJ1OGd3eFkKaG1IVklreHlYeEowZHQxYmdQVWhpNURqLzAzM3NqNENtOWhzSldTT2ZzNmkxdjhIT1dxSXVMNWtDQWd6NXBlcgptQmpFenZzQmVtelJSSzhNSWJrR3ZMQXFDcm9uRkE0K3JaU1RGd25UNjVSdFBDaEhsbEhUZUlnN3loSHBUNmd1CnYySVBZVjA1OUVtUTRmS1BEQzhDbDRhNWRtWnVQWG9qMmExZmVrZkZuT2hTWHoydFFsN2h5MzJ2K0FaeUZuUDAKMGlFWXZjd3FFUzdjZFVGYS9ld1gwemozV1hNNEVOczBWbUZNcWUxWFpISnYwTWFxMVdpN1RwMjJuQXNpNjNoTwpmeG1NZXY2QWNBNC9TNld0Nkt0Y2JjUTd5dU4xbXZRUlFldWFhN2ZvUkxQSEFVY3g1eU4yTEFzRzFYQkc0TUUvCjI0akx5d0lEQVFBQm95Y3dKVEFPQmdOVkhROEJBZjhFQkFNQ0JhQXdFd1lEVlIwbEJBd3dDZ1lJS3dZQkJRVUgKQXdJd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFFNnowUXRINVlkdTFVNzN1UngwS0ZUb28vK1Q4dk5qM1FLNAo3L09ZbUxUMHdTaDg5ZVZUSDk0UVZLRDlXQlNXV3hWQzZkaTI2YnlBSytzMGo5WE1WcWlkdGo2eGxCMWlwVXdCCjB3RU1BZG10blJOMHRxNmtCMytYbnBod0ZBM2tPbnhMMFZlK0ZUam5JalQ4b0EzRHU2NW1zcXpJYk5mMHF0ZzgKYk5EbTFEdFhFSHdESmhnZ2FmdytlR3FROFZoWm44dmNTYWt2NkN0Q1ZtaE5KUEdxMWZnRExqVXc4bGVTTU5BdgpFd2ZDU25pdUFRTm5uV3ZORlVaZFl6MUR3YUt5eU5RUEpidkI2aWtzVi9VclRKNnh6Ui8zbDB2MXNzU0tzK1ZVCi9Pa0thcU8xVGM2MTNJWEFzbVhYUVJzUEFWaDdvQmp2NEg4VS9CQmRwb0tFZWRrdDdtTT0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=",
            "KeyData": "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFb3dJQkFBS0NBUUVBNVdPQTJmdEVHMnU4Z3d4WWhtSFZJa3h5WHhKMGR0MWJnUFVoaTVEai8wMzNzajRDCm05aHNKV1NPZnM2aTF2OEhPV3FJdUw1a0NBZ3o1cGVybUJqRXp2c0JlbXpSUks4TUlia0d2TEFxQ3JvbkZBNCsKclpTVEZ3blQ2NVJ0UENoSGxsSFRlSWc3eWhIcFQ2Z3V2MklQWVYwNTlFbVE0ZktQREM4Q2w0YTVkbVp1UFhvagoyYTFmZWtmRm5PaFNYejJ0UWw3aHkzMnYrQVp5Rm5QMDBpRVl2Y3dxRVM3Y2RVRmEvZXdYMHpqM1dYTTRFTnMwClZtRk1xZTFYWkhKdjBNYXExV2k3VHAyMm5Bc2k2M2hPZnhtTWV2NkFjQTQvUzZXdDZLdGNiY1E3eXVOMW12UVIKUWV1YWE3Zm9STFBIQVVjeDV5TjJMQXNHMVhCRzRNRS8yNGpMeXdJREFRQUJBb0lCQUN3QUVTZys3VXFCT1BDKwpQb0RRWlV5bDgwNVBRTzNIK2hSYmNPclBpUnhndlVHQWFZbXhVdFU5VzZQeFNRVUtlRDFJTlIrU3phZEl3NFBZCjFmNWZ5ZWlWOXl1ZmtlaWwxeUxrMWVqOXRhTEhJRlhWZ2FwVUZIN1gwTUdnZisrSkhtbzBHZWRGNG9vWk0zS24KSlFocTY5NVdQcGFnUWQxRlpMRUdsMjJ2VndYaHRRNFNvNGZrRktOTWVQc3c4ZXVweVB2OE1CeVNHU2pOU1lVRgpQZUF3TXpiVVNuVFdNTnBlK0ZGaHpxQ2hnME0zblhXVGt2L2tWMDNLdUtWRHlQTXBsN3NRM1pGeTVkWlJIdHN2Cnhlc2xkUHVUQTI1NmVvNHZaTjdMSVMvelFnbys0TXhXSE5IdVhIUGF3MXVxYU52SDZpM1dvdGlUaDFBRmdsK3AKMmdjb2U1RUNnWUVBODJHejNwRVNCdXRrdHhQSUlmOE5iaFZuRTNBc3pyL1B3Yk4wZXA1WUo2eTRyQUczeEd6bgovOGRRWEwyS0JseGJuVDllZHp5ZnBLazNCNEtBc0ZxS1lhaXBrWmR4bmhQRjY4RVNIb0JycWV1R2lhZ0FlN2RoClJNZVp5bVRWOWlKb1BnM1RFVXBKK2tqNXp0NGNuTllEK2h2eStyaE5saERXQld6bml3Q2RtVU1DZ1lFQThVZ1UKQjV3UldMRm0rS0ZteWpJTWc3b0hPRXYvYUZiRmVpWjFySTMwNW1waVFYNktHYUZFdHBTMWwrTGZHdXlldFZRcQpHOTNnM3V3MGExL3QveG41V2JlelpscWx5WWpoMVlNc3dnZHkySjg3RGQxV0dPN1VGSE5SOW4yUmpiSm1nVzIvCjBXOFZ0dnJuMGtlZS9vdHlxdXNWYktuTXQweC9VM042c1ZvdmR0a0NnWUExSldXb3VWY05hY09oY3RGbUV4TDAKc2ZuRE5lQ2krU0c5ODVrQTJhajRhUEFlcDNWZ2tFT05DQklWWGxKUWwwUnVMeE5LeUZNNEdyZG9qV2ZhbXJyVApIb2lBd1doUEU1UkpxZXh4K3FzSC9PVnhFOTJmSm1rNElyb0RoMGR0cXcvR1ZUQjgreEx5YzVNUlNGRkpNamJHCkcrcFFNNFRGdTBGeEI5bjc4Wk40andLQmdHL2NxdXljUHE2UUVOMVVkd05uRU1aQmlQZGd4SmpySWNMdjhiNSsKVWZ4QmRpeEhMbCtUbFBmUkdoL0EzdzdzaE9nc2pSaytWUE1GTDRoWWdVNjBEQmE4UkVBLzVuejVLVHFFQmt3dQpoK0JHY21xTEkwK0w2bWRRejc4bm1FUEpZaHkvZFI3MEVXMDBCaVpIYmo4MUI0U1dXT2g0RUtFcXBoMWFmSmVjCjZFU0JBb0dCQUpnYk56a2xXLy93MmtYdTBucTJ5S1VZdncyQkt2VnI2eGVkd0trMGdSQ2Jld2d5aXZ5UjdMZmIKZHQwR0grOFFuN1pvM3lpNU5tZ0c2bDV3WEdzck1TYTAyVW5RMndTYUF5UlZNR1ZZWCt2YXBoTVQ2S2xBRDJqdQplS3lSRGZOMGFjblVacG9vSGp5T2xiOWt6SE5ITGd5K2FDMnYyUlVDQjlTK1JjWWZ1K0RVCi0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0tCg==",
            "CAData": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUN5RENDQWJDZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwcmRXSmwKY201bGRHVnpNQjRYRFRJeE1EY3lOekF6TXpnd05Gb1hEVE14TURjeU5UQXpNemd3TkZvd0ZURVRNQkVHQTFVRQpBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUJBS2o5CjBpRW44RzVzTnBLYkVyaUhQazl0RmNNbWNhaVVzVU92QkZZYlYvYU1vZ0RFbGlwVFRIeVlKajh5ODJTQmR3TW0KZFFxRUc3eWpZY1pjdjhwWDVkeTU4emZQSU5PZFNhUWthTFJaSWp4OWVsbVpQTnlyTEZ2QmpBaE9kQUt1NXhNRQpzNjhLZ2U5b09LQVZUU0dtWXZvMDFrRm8vejFDZWZVT3A1bWpTa2xUK1Iycjl1UXVVd2RHN0lMTzd2Yllsb0FDCkdzRXBjNlRucWlqaHM2M29wby9LaWVsVFJOZ0ptd1IwN3ptb05wQ3JFNEFrazdyQlhDRlZkNG9PV0hjZ0pDWjkKWTFFWGFOZUVrRG41c1ZQa2VvSytRZmRPMVFuN1RTbjFxR09mUUFqRTJyYWQxdVFBMXo2U3gzMFpSOU1SRy9MMAp6azE5a2VvdVhwSVNRTFVXbnhzQ0F3RUFBYU1qTUNFd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWRFd0VCCi93UUZNQU1CQWY4d0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFKQjdJWjBhRENGd3BidTNpdVpzanUvRnNPSnAKc2JEa3ZraTRtMVQ4WUxaMzUzalRBd2x0Mndwd3VPbWlzVmZrbHRFemZhUUtOZEhuNU9PbnIxVCs5cTdYY3VwZQovU255dlVNa1Y3c0RKYkJ3c2tzVmpEKzZYTERkYUdGdGRDcURFdkFTTkpOZzJXR0JJYWQycXJwZGsxbXlHSzR1ClFUVW5EYXltTE1tSFNVNCt0SjV0Si93UkhQdEpEa1VJNmhMcVBjUkxSUnQ3SFlvbHRvandHZHlKbU9DR0NnT1IKNFYvYWplS2Y3NzF0QnhzL3BQZm4vNjg4bHpwWHkxOHFFYmsyMzB6NlJYNXlncS8wUCtyOVROeTFmZmFpTlpBVQpvMERvWXRLdmErcDQwaDZ6YUpBaXhCYTAzZDVoWDFVa1hzSE9sY0hYei9CdUlBS2YwQUJZR1p4SkY4dz0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=",
            "NextProtos": null
          }
        },
        "Desc": "",
        "IsStop": false,
        "Attr": null,
        "CTime": 0,
        "MTime": 0,
        "State": "running",
        "state_desc": "",
        "is_managed": true
      }
    ]
  }
}
```




## /v1/topke/cluster/delete
移除集群的纳管
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
UUID|string|是|""|集群UUID
### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/cluster/delete
```
{
	"UUID": "7c8602b3-f879-48a7-a3d0-c0137eb8ea7c",
}
```

#### 正常返回示例

## /v1/topke/cluster/get
获取集群详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant_uuid|string|是|""|租户UUID
uuid|string|是|""|集群UUID

### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
https://10.30.100.178/v1/topke/cluster/get
```
{
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
}
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "",
  "message_cn": "",
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
    "total_count": 1,
    "list": [
      {
        "uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
        "name": "111",
        "config": {
          "Host": "https://10.30.100.111:8443",
          "APIPath": "",
          "Username": "",
          "Password": "",
          "BearerToken": "",
          "BearerTokenFile": "",
          "TlsClientConfig": {
            "Insecure": false,
            "ServerName": "",
            "CertFile": "",
            "KeyFile": "",
            "CAFile": "",
            "CertData": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUM4akNDQWRxZ0F3SUJBZ0lJUWZmZnhaQzA4ell3RFFZSktvWklodmNOQVFFTEJRQXdGVEVUTUJFR0ExVUUKQXhNS2EzVmlaWEp1WlhSbGN6QWVGdzB5TVRBM01qY3dNek00TURSYUZ3MHlNakEzTWpjd016UXhNVE5hTURReApGekFWQmdOVkJBb1REbk41YzNSbGJUcHRZWE4wWlhKek1Sa3dGd1lEVlFRREV4QnJkV0psY201bGRHVnpMV0ZrCmJXbHVNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQTVXT0EyZnRFRzJ1OGd3eFkKaG1IVklreHlYeEowZHQxYmdQVWhpNURqLzAzM3NqNENtOWhzSldTT2ZzNmkxdjhIT1dxSXVMNWtDQWd6NXBlcgptQmpFenZzQmVtelJSSzhNSWJrR3ZMQXFDcm9uRkE0K3JaU1RGd25UNjVSdFBDaEhsbEhUZUlnN3loSHBUNmd1CnYySVBZVjA1OUVtUTRmS1BEQzhDbDRhNWRtWnVQWG9qMmExZmVrZkZuT2hTWHoydFFsN2h5MzJ2K0FaeUZuUDAKMGlFWXZjd3FFUzdjZFVGYS9ld1gwemozV1hNNEVOczBWbUZNcWUxWFpISnYwTWFxMVdpN1RwMjJuQXNpNjNoTwpmeG1NZXY2QWNBNC9TNld0Nkt0Y2JjUTd5dU4xbXZRUlFldWFhN2ZvUkxQSEFVY3g1eU4yTEFzRzFYQkc0TUUvCjI0akx5d0lEQVFBQm95Y3dKVEFPQmdOVkhROEJBZjhFQkFNQ0JhQXdFd1lEVlIwbEJBd3dDZ1lJS3dZQkJRVUgKQXdJd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFFNnowUXRINVlkdTFVNzN1UngwS0ZUb28vK1Q4dk5qM1FLNAo3L09ZbUxUMHdTaDg5ZVZUSDk0UVZLRDlXQlNXV3hWQzZkaTI2YnlBSytzMGo5WE1WcWlkdGo2eGxCMWlwVXdCCjB3RU1BZG10blJOMHRxNmtCMytYbnBod0ZBM2tPbnhMMFZlK0ZUam5JalQ4b0EzRHU2NW1zcXpJYk5mMHF0ZzgKYk5EbTFEdFhFSHdESmhnZ2FmdytlR3FROFZoWm44dmNTYWt2NkN0Q1ZtaE5KUEdxMWZnRExqVXc4bGVTTU5BdgpFd2ZDU25pdUFRTm5uV3ZORlVaZFl6MUR3YUt5eU5RUEpidkI2aWtzVi9VclRKNnh6Ui8zbDB2MXNzU0tzK1ZVCi9Pa0thcU8xVGM2MTNJWEFzbVhYUVJzUEFWaDdvQmp2NEg4VS9CQmRwb0tFZWRrdDdtTT0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=",
            "KeyData": "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFb3dJQkFBS0NBUUVBNVdPQTJmdEVHMnU4Z3d4WWhtSFZJa3h5WHhKMGR0MWJnUFVoaTVEai8wMzNzajRDCm05aHNKV1NPZnM2aTF2OEhPV3FJdUw1a0NBZ3o1cGVybUJqRXp2c0JlbXpSUks4TUlia0d2TEFxQ3JvbkZBNCsKclpTVEZ3blQ2NVJ0UENoSGxsSFRlSWc3eWhIcFQ2Z3V2MklQWVYwNTlFbVE0ZktQREM4Q2w0YTVkbVp1UFhvagoyYTFmZWtmRm5PaFNYejJ0UWw3aHkzMnYrQVp5Rm5QMDBpRVl2Y3dxRVM3Y2RVRmEvZXdYMHpqM1dYTTRFTnMwClZtRk1xZTFYWkhKdjBNYXExV2k3VHAyMm5Bc2k2M2hPZnhtTWV2NkFjQTQvUzZXdDZLdGNiY1E3eXVOMW12UVIKUWV1YWE3Zm9STFBIQVVjeDV5TjJMQXNHMVhCRzRNRS8yNGpMeXdJREFRQUJBb0lCQUN3QUVTZys3VXFCT1BDKwpQb0RRWlV5bDgwNVBRTzNIK2hSYmNPclBpUnhndlVHQWFZbXhVdFU5VzZQeFNRVUtlRDFJTlIrU3phZEl3NFBZCjFmNWZ5ZWlWOXl1ZmtlaWwxeUxrMWVqOXRhTEhJRlhWZ2FwVUZIN1gwTUdnZisrSkhtbzBHZWRGNG9vWk0zS24KSlFocTY5NVdQcGFnUWQxRlpMRUdsMjJ2VndYaHRRNFNvNGZrRktOTWVQc3c4ZXVweVB2OE1CeVNHU2pOU1lVRgpQZUF3TXpiVVNuVFdNTnBlK0ZGaHpxQ2hnME0zblhXVGt2L2tWMDNLdUtWRHlQTXBsN3NRM1pGeTVkWlJIdHN2Cnhlc2xkUHVUQTI1NmVvNHZaTjdMSVMvelFnbys0TXhXSE5IdVhIUGF3MXVxYU52SDZpM1dvdGlUaDFBRmdsK3AKMmdjb2U1RUNnWUVBODJHejNwRVNCdXRrdHhQSUlmOE5iaFZuRTNBc3pyL1B3Yk4wZXA1WUo2eTRyQUczeEd6bgovOGRRWEwyS0JseGJuVDllZHp5ZnBLazNCNEtBc0ZxS1lhaXBrWmR4bmhQRjY4RVNIb0JycWV1R2lhZ0FlN2RoClJNZVp5bVRWOWlKb1BnM1RFVXBKK2tqNXp0NGNuTllEK2h2eStyaE5saERXQld6bml3Q2RtVU1DZ1lFQThVZ1UKQjV3UldMRm0rS0ZteWpJTWc3b0hPRXYvYUZiRmVpWjFySTMwNW1waVFYNktHYUZFdHBTMWwrTGZHdXlldFZRcQpHOTNnM3V3MGExL3QveG41V2JlelpscWx5WWpoMVlNc3dnZHkySjg3RGQxV0dPN1VGSE5SOW4yUmpiSm1nVzIvCjBXOFZ0dnJuMGtlZS9vdHlxdXNWYktuTXQweC9VM042c1ZvdmR0a0NnWUExSldXb3VWY05hY09oY3RGbUV4TDAKc2ZuRE5lQ2krU0c5ODVrQTJhajRhUEFlcDNWZ2tFT05DQklWWGxKUWwwUnVMeE5LeUZNNEdyZG9qV2ZhbXJyVApIb2lBd1doUEU1UkpxZXh4K3FzSC9PVnhFOTJmSm1rNElyb0RoMGR0cXcvR1ZUQjgreEx5YzVNUlNGRkpNamJHCkcrcFFNNFRGdTBGeEI5bjc4Wk40andLQmdHL2NxdXljUHE2UUVOMVVkd05uRU1aQmlQZGd4SmpySWNMdjhiNSsKVWZ4QmRpeEhMbCtUbFBmUkdoL0EzdzdzaE9nc2pSaytWUE1GTDRoWWdVNjBEQmE4UkVBLzVuejVLVHFFQmt3dQpoK0JHY21xTEkwK0w2bWRRejc4bm1FUEpZaHkvZFI3MEVXMDBCaVpIYmo4MUI0U1dXT2g0RUtFcXBoMWFmSmVjCjZFU0JBb0dCQUpnYk56a2xXLy93MmtYdTBucTJ5S1VZdncyQkt2VnI2eGVkd0trMGdSQ2Jld2d5aXZ5UjdMZmIKZHQwR0grOFFuN1pvM3lpNU5tZ0c2bDV3WEdzck1TYTAyVW5RMndTYUF5UlZNR1ZZWCt2YXBoTVQ2S2xBRDJqdQplS3lSRGZOMGFjblVacG9vSGp5T2xiOWt6SE5ITGd5K2FDMnYyUlVDQjlTK1JjWWZ1K0RVCi0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0tCg==",
            "CAData": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUN5RENDQWJDZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwcmRXSmwKY201bGRHVnpNQjRYRFRJeE1EY3lOekF6TXpnd05Gb1hEVE14TURjeU5UQXpNemd3TkZvd0ZURVRNQkVHQTFVRQpBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUJBS2o5CjBpRW44RzVzTnBLYkVyaUhQazl0RmNNbWNhaVVzVU92QkZZYlYvYU1vZ0RFbGlwVFRIeVlKajh5ODJTQmR3TW0KZFFxRUc3eWpZY1pjdjhwWDVkeTU4emZQSU5PZFNhUWthTFJaSWp4OWVsbVpQTnlyTEZ2QmpBaE9kQUt1NXhNRQpzNjhLZ2U5b09LQVZUU0dtWXZvMDFrRm8vejFDZWZVT3A1bWpTa2xUK1Iycjl1UXVVd2RHN0lMTzd2Yllsb0FDCkdzRXBjNlRucWlqaHM2M29wby9LaWVsVFJOZ0ptd1IwN3ptb05wQ3JFNEFrazdyQlhDRlZkNG9PV0hjZ0pDWjkKWTFFWGFOZUVrRG41c1ZQa2VvSytRZmRPMVFuN1RTbjFxR09mUUFqRTJyYWQxdVFBMXo2U3gzMFpSOU1SRy9MMAp6azE5a2VvdVhwSVNRTFVXbnhzQ0F3RUFBYU1qTUNFd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWRFd0VCCi93UUZNQU1CQWY4d0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFKQjdJWjBhRENGd3BidTNpdVpzanUvRnNPSnAKc2JEa3ZraTRtMVQ4WUxaMzUzalRBd2x0Mndwd3VPbWlzVmZrbHRFemZhUUtOZEhuNU9PbnIxVCs5cTdYY3VwZQovU255dlVNa1Y3c0RKYkJ3c2tzVmpEKzZYTERkYUdGdGRDcURFdkFTTkpOZzJXR0JJYWQycXJwZGsxbXlHSzR1ClFUVW5EYXltTE1tSFNVNCt0SjV0Si93UkhQdEpEa1VJNmhMcVBjUkxSUnQ3SFlvbHRvandHZHlKbU9DR0NnT1IKNFYvYWplS2Y3NzF0QnhzL3BQZm4vNjg4bHpwWHkxOHFFYmsyMzB6NlJYNXlncS8wUCtyOVROeTFmZmFpTlpBVQpvMERvWXRLdmErcDQwaDZ6YUpBaXhCYTAzZDVoWDFVa1hzSE9sY0hYei9CdUlBS2YwQUJZR1p4SkY4dz0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=",
            "NextProtos": null
          }
        },
        "desc": "",
        "is_stop": false,
        "attr": null,
        "create_time": 1628500128,
        "update_time": 1628500128,
        "state": "running",
        "state_desc": "",
        "is_managed": true,
        "tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
        "tenant_name": "dev",
        "kube_version": {
          "major": "1",
          "minor": "18",
          "gitVersion": "v1.18.0",
          "gitCommit": "9e991415386e4cf155a24b1da15becaa390438d8",
          "gitTreeState": "clean",
          "buildDate": "2020-03-25T14:50:46Z",
          "goVersion": "go1.13.8",
          "compiler": "gc",
          "platform": "linux/amd64"
        },
        "is_high_available": true,
        "kube_config_data": "",
        "cluster_node_scale": "",
        "PodCidr": "",
        "ServicePodCidr": ""
      }
    ]
  }
}
```



## /v1/topke/cluster/list
获取集群列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant_uuid|string|是|""|集群所属租户
sort_by|string|是|""|排序字段
sort_desc|bool|否|false|是否降序
### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
https://10.30.100.178/v1/topke/cluster/list
```
{
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"sort_by": "TopKESortByName",
	"sort_desc": true,
}
```
#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "",
  "message_cn": "",
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
    "total_count": 1,
    "list": [
      {
        "uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
        "name": "111",
        "config": {
          "Host": "https://10.30.100.111:8443",
          "APIPath": "",
          "Username": "",
          "Password": "",
          "BearerToken": "",
          "BearerTokenFile": "",
          "TlsClientConfig": {
            "Insecure": false,
            "ServerName": "",
            "CertFile": "",
            "KeyFile": "",
            "CAFile": "",
            "CertData": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUM4akNDQWRxZ0F3SUJBZ0lJUWZmZnhaQzA4ell3RFFZSktvWklodmNOQVFFTEJRQXdGVEVUTUJFR0ExVUUKQXhNS2EzVmlaWEp1WlhSbGN6QWVGdzB5TVRBM01qY3dNek00TURSYUZ3MHlNakEzTWpjd016UXhNVE5hTURReApGekFWQmdOVkJBb1REbk41YzNSbGJUcHRZWE4wWlhKek1Sa3dGd1lEVlFRREV4QnJkV0psY201bGRHVnpMV0ZrCmJXbHVNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQTVXT0EyZnRFRzJ1OGd3eFkKaG1IVklreHlYeEowZHQxYmdQVWhpNURqLzAzM3NqNENtOWhzSldTT2ZzNmkxdjhIT1dxSXVMNWtDQWd6NXBlcgptQmpFenZzQmVtelJSSzhNSWJrR3ZMQXFDcm9uRkE0K3JaU1RGd25UNjVSdFBDaEhsbEhUZUlnN3loSHBUNmd1CnYySVBZVjA1OUVtUTRmS1BEQzhDbDRhNWRtWnVQWG9qMmExZmVrZkZuT2hTWHoydFFsN2h5MzJ2K0FaeUZuUDAKMGlFWXZjd3FFUzdjZFVGYS9ld1gwemozV1hNNEVOczBWbUZNcWUxWFpISnYwTWFxMVdpN1RwMjJuQXNpNjNoTwpmeG1NZXY2QWNBNC9TNld0Nkt0Y2JjUTd5dU4xbXZRUlFldWFhN2ZvUkxQSEFVY3g1eU4yTEFzRzFYQkc0TUUvCjI0akx5d0lEQVFBQm95Y3dKVEFPQmdOVkhROEJBZjhFQkFNQ0JhQXdFd1lEVlIwbEJBd3dDZ1lJS3dZQkJRVUgKQXdJd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFFNnowUXRINVlkdTFVNzN1UngwS0ZUb28vK1Q4dk5qM1FLNAo3L09ZbUxUMHdTaDg5ZVZUSDk0UVZLRDlXQlNXV3hWQzZkaTI2YnlBSytzMGo5WE1WcWlkdGo2eGxCMWlwVXdCCjB3RU1BZG10blJOMHRxNmtCMytYbnBod0ZBM2tPbnhMMFZlK0ZUam5JalQ4b0EzRHU2NW1zcXpJYk5mMHF0ZzgKYk5EbTFEdFhFSHdESmhnZ2FmdytlR3FROFZoWm44dmNTYWt2NkN0Q1ZtaE5KUEdxMWZnRExqVXc4bGVTTU5BdgpFd2ZDU25pdUFRTm5uV3ZORlVaZFl6MUR3YUt5eU5RUEpidkI2aWtzVi9VclRKNnh6Ui8zbDB2MXNzU0tzK1ZVCi9Pa0thcU8xVGM2MTNJWEFzbVhYUVJzUEFWaDdvQmp2NEg4VS9CQmRwb0tFZWRrdDdtTT0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=",
            "KeyData": "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFb3dJQkFBS0NBUUVBNVdPQTJmdEVHMnU4Z3d4WWhtSFZJa3h5WHhKMGR0MWJnUFVoaTVEai8wMzNzajRDCm05aHNKV1NPZnM2aTF2OEhPV3FJdUw1a0NBZ3o1cGVybUJqRXp2c0JlbXpSUks4TUlia0d2TEFxQ3JvbkZBNCsKclpTVEZ3blQ2NVJ0UENoSGxsSFRlSWc3eWhIcFQ2Z3V2MklQWVYwNTlFbVE0ZktQREM4Q2w0YTVkbVp1UFhvagoyYTFmZWtmRm5PaFNYejJ0UWw3aHkzMnYrQVp5Rm5QMDBpRVl2Y3dxRVM3Y2RVRmEvZXdYMHpqM1dYTTRFTnMwClZtRk1xZTFYWkhKdjBNYXExV2k3VHAyMm5Bc2k2M2hPZnhtTWV2NkFjQTQvUzZXdDZLdGNiY1E3eXVOMW12UVIKUWV1YWE3Zm9STFBIQVVjeDV5TjJMQXNHMVhCRzRNRS8yNGpMeXdJREFRQUJBb0lCQUN3QUVTZys3VXFCT1BDKwpQb0RRWlV5bDgwNVBRTzNIK2hSYmNPclBpUnhndlVHQWFZbXhVdFU5VzZQeFNRVUtlRDFJTlIrU3phZEl3NFBZCjFmNWZ5ZWlWOXl1ZmtlaWwxeUxrMWVqOXRhTEhJRlhWZ2FwVUZIN1gwTUdnZisrSkhtbzBHZWRGNG9vWk0zS24KSlFocTY5NVdQcGFnUWQxRlpMRUdsMjJ2VndYaHRRNFNvNGZrRktOTWVQc3c4ZXVweVB2OE1CeVNHU2pOU1lVRgpQZUF3TXpiVVNuVFdNTnBlK0ZGaHpxQ2hnME0zblhXVGt2L2tWMDNLdUtWRHlQTXBsN3NRM1pGeTVkWlJIdHN2Cnhlc2xkUHVUQTI1NmVvNHZaTjdMSVMvelFnbys0TXhXSE5IdVhIUGF3MXVxYU52SDZpM1dvdGlUaDFBRmdsK3AKMmdjb2U1RUNnWUVBODJHejNwRVNCdXRrdHhQSUlmOE5iaFZuRTNBc3pyL1B3Yk4wZXA1WUo2eTRyQUczeEd6bgovOGRRWEwyS0JseGJuVDllZHp5ZnBLazNCNEtBc0ZxS1lhaXBrWmR4bmhQRjY4RVNIb0JycWV1R2lhZ0FlN2RoClJNZVp5bVRWOWlKb1BnM1RFVXBKK2tqNXp0NGNuTllEK2h2eStyaE5saERXQld6bml3Q2RtVU1DZ1lFQThVZ1UKQjV3UldMRm0rS0ZteWpJTWc3b0hPRXYvYUZiRmVpWjFySTMwNW1waVFYNktHYUZFdHBTMWwrTGZHdXlldFZRcQpHOTNnM3V3MGExL3QveG41V2JlelpscWx5WWpoMVlNc3dnZHkySjg3RGQxV0dPN1VGSE5SOW4yUmpiSm1nVzIvCjBXOFZ0dnJuMGtlZS9vdHlxdXNWYktuTXQweC9VM042c1ZvdmR0a0NnWUExSldXb3VWY05hY09oY3RGbUV4TDAKc2ZuRE5lQ2krU0c5ODVrQTJhajRhUEFlcDNWZ2tFT05DQklWWGxKUWwwUnVMeE5LeUZNNEdyZG9qV2ZhbXJyVApIb2lBd1doUEU1UkpxZXh4K3FzSC9PVnhFOTJmSm1rNElyb0RoMGR0cXcvR1ZUQjgreEx5YzVNUlNGRkpNamJHCkcrcFFNNFRGdTBGeEI5bjc4Wk40andLQmdHL2NxdXljUHE2UUVOMVVkd05uRU1aQmlQZGd4SmpySWNMdjhiNSsKVWZ4QmRpeEhMbCtUbFBmUkdoL0EzdzdzaE9nc2pSaytWUE1GTDRoWWdVNjBEQmE4UkVBLzVuejVLVHFFQmt3dQpoK0JHY21xTEkwK0w2bWRRejc4bm1FUEpZaHkvZFI3MEVXMDBCaVpIYmo4MUI0U1dXT2g0RUtFcXBoMWFmSmVjCjZFU0JBb0dCQUpnYk56a2xXLy93MmtYdTBucTJ5S1VZdncyQkt2VnI2eGVkd0trMGdSQ2Jld2d5aXZ5UjdMZmIKZHQwR0grOFFuN1pvM3lpNU5tZ0c2bDV3WEdzck1TYTAyVW5RMndTYUF5UlZNR1ZZWCt2YXBoTVQ2S2xBRDJqdQplS3lSRGZOMGFjblVacG9vSGp5T2xiOWt6SE5ITGd5K2FDMnYyUlVDQjlTK1JjWWZ1K0RVCi0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0tCg==",
            "CAData": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUN5RENDQWJDZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwcmRXSmwKY201bGRHVnpNQjRYRFRJeE1EY3lOekF6TXpnd05Gb1hEVE14TURjeU5UQXpNemd3TkZvd0ZURVRNQkVHQTFVRQpBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUJBS2o5CjBpRW44RzVzTnBLYkVyaUhQazl0RmNNbWNhaVVzVU92QkZZYlYvYU1vZ0RFbGlwVFRIeVlKajh5ODJTQmR3TW0KZFFxRUc3eWpZY1pjdjhwWDVkeTU4emZQSU5PZFNhUWthTFJaSWp4OWVsbVpQTnlyTEZ2QmpBaE9kQUt1NXhNRQpzNjhLZ2U5b09LQVZUU0dtWXZvMDFrRm8vejFDZWZVT3A1bWpTa2xUK1Iycjl1UXVVd2RHN0lMTzd2Yllsb0FDCkdzRXBjNlRucWlqaHM2M29wby9LaWVsVFJOZ0ptd1IwN3ptb05wQ3JFNEFrazdyQlhDRlZkNG9PV0hjZ0pDWjkKWTFFWGFOZUVrRG41c1ZQa2VvSytRZmRPMVFuN1RTbjFxR09mUUFqRTJyYWQxdVFBMXo2U3gzMFpSOU1SRy9MMAp6azE5a2VvdVhwSVNRTFVXbnhzQ0F3RUFBYU1qTUNFd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWRFd0VCCi93UUZNQU1CQWY4d0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFKQjdJWjBhRENGd3BidTNpdVpzanUvRnNPSnAKc2JEa3ZraTRtMVQ4WUxaMzUzalRBd2x0Mndwd3VPbWlzVmZrbHRFemZhUUtOZEhuNU9PbnIxVCs5cTdYY3VwZQovU255dlVNa1Y3c0RKYkJ3c2tzVmpEKzZYTERkYUdGdGRDcURFdkFTTkpOZzJXR0JJYWQycXJwZGsxbXlHSzR1ClFUVW5EYXltTE1tSFNVNCt0SjV0Si93UkhQdEpEa1VJNmhMcVBjUkxSUnQ3SFlvbHRvandHZHlKbU9DR0NnT1IKNFYvYWplS2Y3NzF0QnhzL3BQZm4vNjg4bHpwWHkxOHFFYmsyMzB6NlJYNXlncS8wUCtyOVROeTFmZmFpTlpBVQpvMERvWXRLdmErcDQwaDZ6YUpBaXhCYTAzZDVoWDFVa1hzSE9sY0hYei9CdUlBS2YwQUJZR1p4SkY4dz0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=",
            "NextProtos": null
          }
        },
        "desc": "",
        "is_stop": false,
        "attr": null,
        "create_time": 1628500128,
        "update_time": 1628500128,
        "state": "running",
        "state_desc": "",
        "is_managed": true,
        "tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
        "tenant_name": "dev",
        "kube_version": {
          "major": "1",
          "minor": "18",
          "gitVersion": "v1.18.0",
          "gitCommit": "9e991415386e4cf155a24b1da15becaa390438d8",
          "gitTreeState": "clean",
          "buildDate": "2020-03-25T14:50:46Z",
          "goVersion": "go1.13.8",
          "compiler": "gc",
          "platform": "linux/amd64"
        },
        "is_high_available": true,
        "kube_config_data": "",
        "cluster_node_scale": "",
        "PodCidr": "",
        "ServicePodCidr": ""
      }
    ]
  }
}
```
## /v1/topke/cluster/registry/distribute
分发私有镜像仓库证书到集群节点上
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
clusters|string array|是|[]|下发镜像仓库证书到哪些集群
registry|struct|是|{}| 下发证书的镜像仓库
### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
https://10.30.100.178/v1/topke/cluster/registry/distribute
```
{
	"clusters": ["d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1"],
	"registry": {
		"registry_uuid": "9cbd63e0-2d42-4e52-bb5e-80b861cc868a"
	},
}
```
#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "",
  "message_cn": "",
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
    "total": 1,
    "success": 1,
    "fail": 0,
    "results": [
      {
        "code": 0,
        "message": "",
        "messageCn": "",
        "stack": null,
        "desc": "",
        "UUID": "",
        "message_cn": "",
        "data": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
        "scode": 0
      }
    ]
  }
}
```