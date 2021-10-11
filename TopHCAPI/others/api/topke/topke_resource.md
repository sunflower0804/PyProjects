[back to api overview](../api_overview.md#topke_resource)

### 容器云集群资源接口

## /v1/topke/namespace/list
获取命名空间列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
tenant_uuid|string|是|""|租户uuid
fuzzy|string|否|""|模糊匹配
sort_by|string|否|""|排序字段
sort_desc|bool|否|false|是否降序
page_size|int|否|0| 页大小
page_num|int|否|0|页码


### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/namespace/list
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"fuzzy": "",
	"page_size": 10,
	"page_num": 0,
	"sort_by": "",
	"sort_desc": false
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
    "type_meta": null,
    "list_meta": null,
    "total_count": 10,
    "list": [
      {
        "kind": "Namespace",
        "apiVersion": "v1",
        "metadata": {
          "name": "velero",
          "selfLink": "/api/v1/namespaces/velero",
          "uid": "301726ca-25ab-4942-9db9-31e16aa0b0c6",
          "resourceVersion": "11770021",
          "creationTimestamp": "2021-08-23T08:11:59Z",
          "annotations": {
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Namespace\",\"metadata\":{\"annotations\":{},\"name\":\"velero\"}}\n",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629706319",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "finalizers": [
            "kubernetes"
          ]
        },
        "status": {
          "phase": "Active"
        },
        "gateway_enable": false
      },
    ...
```

## /v1/topke/namespace/get
命名空间详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
namespace|struct|是|{}| k8s资源描述
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/namespace/get
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"namespace": {
		"metadata": {
			"name": "aaaa"
		}
	}
}
```
#### 正常返回示例

## /v1/topke/namespace/update
命名空间更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
namespace|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/namespace/update

```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"workspace": "aaa",
	"namespace": {
		"metadata": {
			"name": "aaaa",
			"annotations": {
				"topke.desc": "sdf"
			}
		}
	},
}
```

#### 正常返回示例

## /v1/topke/namespace/delete
命名空间删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
namespace|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/namespace/delete
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"workspace": "aaa",
	"namespace": {
		"metadata": {
			"name": "aaaa",
			"annotations": {
				"topke.desc": ""
			}
		}
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
    "TotalCount": 0,
    "gateway": "",
    "TypeMeta": null,
    "ListMeta": null,
    "Infos": null
  }
}
```

## /v1/topke/namespace/add
命名空间创建 
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
namespace|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/namespace/add
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"workspace": "aaa",
	"namespace": {
		"metadata": {
			"name": "aaaa",
			"annotations": {
				"topke.desc": ""
			}
		}
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
    "TotalCount": 1,
    "gateway": "",
    "TypeMeta": null,
    "ListMeta": null,
    "Infos": [
      {
        "Namespace": {
          "metadata": {
            "name": "aaaa",
            "selfLink": "/api/v1/namespaces/aaaa",
            "uid": "e531f4ec-64b8-4500-998e-eaf464a0d09b",
            "resourceVersion": "12673811",
            "creationTimestamp": "2021-08-25T06:32:05Z",
            "labels": {
              "workspace.topke.io": "aaa"
            },
            "annotations": {
              "topke.desc": ""
            },
            "managedFields": [
              {
                "manager": "manager",
                "operation": "Update",
                "apiVersion": "v1",
                "time": "2021-08-25T06:32:05Z",
                "fieldsType": "FieldsV1",
                "fieldsV1": {
                  "f:metadata": {
                    "f:annotations": {
                      ".": {},
                      "f:topke.desc": {}
                    },
                    "f:labels": {
                      ".": {},
                      "f:workspace.topke.io": {}
                    }
                  },
                  "f:status": {
                    "f:phase": {}
                  }
                }
              }
            ]
          },
          "spec": {
            "finalizers": [
              "kubernetes"
            ]
          },
          "status": {
            "phase": "Active"
          },
          "cpu_usage": "0m",
          "mem_usage": "0Mi",
          "pod_count": 0
        },
        "CTime": 1629873125
      }
    ]
  }
}
```


## /v1/topke/service/create
创建服务
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
service|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/service/create
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"workspace": "aaa",
	"service": {
		"metadata": {
			"name": "aaa",
			"namespace": "aaaa",
			"annotations": {
				"topke.desc": ""
			},
			"labels": {}
		},
		"spec": {
			"sessionAffinity": "ClientIP",
			"selector": {
				"a": "b"
			},
			"ports": [{
				"protocol": "TCP",
				"name": "tcp-cjmmw9",
				"targetPort": 80,
				"port": 80
			}],
			"sessionAffinityConfig": {
				"clientIP": {
					"timeoutSeconds": 10800
				}
			},
			"clusterIP": ""
		}
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
    "TotalCount": 1,
    "TypeMeta": null,
    "ListMeta": null,
    "Infos": [
      {
        "Service": {
          "metadata": {
            "name": "aaa",
            "namespace": "aaaa",
            "selfLink": "/api/v1/namespaces/aaaa/services/aaa",
            "uid": "c0a852dd-9fcc-4c03-b010-b9a6f3de5f34",
            "resourceVersion": "12676038",
            "creationTimestamp": "2021-08-25T06:38:52Z",
            "annotations": {
              "topke.desc": ""
            },
            "managedFields": [
              {
                "manager": "manager",
                "operation": "Update",
                "apiVersion": "v1",
                "time": "2021-08-25T06:38:52Z",
                "fieldsType": "FieldsV1",
                "fieldsV1": {
                  "f:metadata": {
                    "f:annotations": {
                      ".": {},
                      "f:topke.desc": {}
                    }
                  },
                  "f:spec": {
                    "f:ports": {
                      ".": {},
                      "k:{\"port\":80,\"protocol\":\"TCP\"}": {
                        ".": {},
                        "f:name": {},
                        "f:port": {},
                        "f:protocol": {},
                        "f:targetPort": {}
                      }
                    },
                    "f:selector": {
                      ".": {},
                      "f:a": {}
                    },
                    "f:sessionAffinity": {},
                    "f:sessionAffinityConfig": {
                      ".": {},
                      "f:clientIP": {
                        ".": {},
                        "f:timeoutSeconds": {}
                      }
                    },
                    "f:type": {}
                  }
                }
              }
            ]
          },
          "spec": {
            "ports": [
              {
                "name": "tcp-cjmmw9",
                "protocol": "TCP",
                "port": 80,
                "targetPort": 80
              }
            ],
            "selector": {
              "a": "b"
            },
            "clusterIP": "10.97.147.74",
            "type": "ClusterIP",
            "sessionAffinity": "ClientIP",
            "sessionAffinityConfig": {
              "clientIP": {
                "timeoutSeconds": 10800
              }
            }
          },
          "status": {
            "loadBalancer": {}
          }
        },
        "CTime": 1629873532
      }
    ]
  }
}
```
## /v1/topke/service/delete
删除服务
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
service|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/service/delete
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"service": {
		"metadata": {
			"name": "aaa",
			"namespace": "default"
		}
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
    "type_meta": null,
    "list_meta": null,
    "total_count": 0,
    "list": null,
    "each_range_list_state": null
  }
}
```


## /v1/topke/service/get
服务详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
service|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/service/get
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"service": {
		"metadata": {
			"name": "service-25rfi791pvknskotzdu5yrab",
			"namespace": "default"
		}
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
    "type_meta": null,
    "list_meta": null,
    "total_count": 1,
    "list": [
      {
        "kind": "Service",
        "apiVersion": "v1",
        "metadata": {
          "name": "service-25rfi791pvknskotzdu5yrab",
          "namespace": "default",
          "selfLink": "/api/v1/namespaces/default/services/service-25rfi791pvknskotzdu5yrab",
          "uid": "df7d97c0-ad94-470e-9c4f-e36159c78969",
          "resourceVersion": "5806478",
          "creationTimestamp": "2021-08-10T11:14:01Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1628594041",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "ports": [
            {
              "name": "tcp-gu9s85",
              "protocol": "TCP",
              "port": 56060,
              "targetPort": 1256
            }
          ],
          "selector": {
            "statefulset": "statefulset-dkxgnmogy9wnh72veg1g35h8"
          },
          "clusterIP": "None",
          "type": "ClusterIP",
          "sessionAffinity": "None"
        },
        "status": {
          "loadBalancer": {}
        }
      }
    ],
    "each_range_list_state": null
  }
}v
```

## /v1/topke/service/update
服务更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
service|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/service/update
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"namespace": "aaaa",
	"service": {
		"kind": "Service",
		"apiVersion": "v1",
		"metadata": {
			"name": "aaa",
			"namespace": "aaaa",
			"selfLink": "/api/v1/namespaces/aaaa/services/aaa",
			"uid": "c0a852dd-9fcc-4c03-b010-b9a6f3de5f34",
			"resourceVersion": "12676038",
			"creationTimestamp": "2021-08-25T06:38:52Z",
			"annotations": {
				"topke.desc": ""
			}
		},
		"spec": {
			"ports": [{
				"name": "tcp-cjmmw9",
				"protocol": "TCP",
				"port": 801,
				"targetPort": 80
			}],
			"selector": {
				"a": "b"
			},
			"clusterIP": "10.97.147.74",
			"type": "ClusterIP",
			"sessionAffinity": "ClientIP",
			"sessionAffinityConfig": {
				"clientIP": {
					"timeoutSeconds": 10800
				}
			}
		},
		"status": {
			"loadBalancer": {}
		}
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
    "TotalCount": 1,
    "TypeMeta": null,
    "ListMeta": null,
    "Infos": [
      {
        "Service": {
          "metadata": {
            "name": "aaa",
            "namespace": "aaaa",
            "selfLink": "/api/v1/namespaces/aaaa/services/aaa",
            "uid": "c0a852dd-9fcc-4c03-b010-b9a6f3de5f34",
            "resourceVersion": "12676463",
            "creationTimestamp": "2021-08-25T06:38:52Z",
            "annotations": {
              "topke.desc": ""
            },
            "managedFields": [
              {
                "manager": "manager",
                "operation": "Update",
                "apiVersion": "v1",
                "time": "2021-08-25T06:40:10Z",
                "fieldsType": "FieldsV1",
                "fieldsV1": {
                  "f:metadata": {
                    "f:annotations": {
                      ".": {},
                      "f:topke.desc": {}
                    }
                  },
                  "f:spec": {
                    "f:ports": {
                      ".": {},
                      "k:{\"port\":801,\"protocol\":\"TCP\"}": {
                        ".": {},
                        "f:name": {},
                        "f:port": {},
                        "f:protocol": {},
                        "f:targetPort": {}
                      }
                    },
                    "f:selector": {
                      ".": {},
                      "f:a": {}
                    },
                    "f:sessionAffinity": {},
                    "f:sessionAffinityConfig": {
                      ".": {},
                      "f:clientIP": {
                        ".": {},
                        "f:timeoutSeconds": {}
                      }
                    },
                    "f:type": {}
                  }
                }
              }
            ]
          },
          "spec": {
            "ports": [
              {
                "name": "tcp-cjmmw9",
                "protocol": "TCP",
                "port": 801,
                "targetPort": 80
              }
            ],
            "selector": {
              "a": "b"
            },
            "clusterIP": "10.97.147.74",
            "type": "ClusterIP",
            "sessionAffinity": "ClientIP",
            "sessionAffinityConfig": {
              "clientIP": {
                "timeoutSeconds": 10800
              }
            }
          },
          "status": {
            "loadBalancer": {}
          }
        },
        "CTime": 1629873532
      }
    ]
  }
}
```



## /v1/topke/service/list
服务列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/service/list
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"page_size": 10,
	"page_num": 0,
	"fuzzy": "",
	"workspace": "aaa",
	"namespace": "aaaa"
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
    "TypeMeta": {},
    "ListMeta": {
      "selfLink": "/api/v1/namespaces/aaaa/services",
      "resourceVersion": "12676469"
    },
    "Infos": [
      {
        "Service": {
          "metadata": {
            "name": "aaa",
            "namespace": "aaaa",
            "selfLink": "/api/v1/namespaces/aaaa/services/aaa",
            "uid": "c0a852dd-9fcc-4c03-b010-b9a6f3de5f34",
            "resourceVersion": "12676463",
            "creationTimestamp": "2021-08-25T06:38:52Z",
            "annotations": {
              "topke.desc": ""
            },
            "managedFields": [
              {
                "manager": "manager",
                "operation": "Update",
                "apiVersion": "v1",
                "time": "2021-08-25T06:40:10Z",
                "fieldsType": "FieldsV1",
                "fieldsV1": {
                  "f:metadata": {
                    "f:annotations": {
                      ".": {},
                      "f:topke.desc": {}
                    }
                  },
                  "f:spec": {
                    "f:ports": {
                      ".": {},
                      "k:{\"port\":801,\"protocol\":\"TCP\"}": {
                        ".": {},
                        "f:name": {},
                        "f:port": {},
                        "f:protocol": {},
                        "f:targetPort": {}
                      }
                    },
                    "f:selector": {
                      ".": {},
                      "f:a": {}
                    },
                    "f:sessionAffinity": {},
                    "f:sessionAffinityConfig": {
                      ".": {},
                      "f:clientIP": {
                        ".": {},
                        "f:timeoutSeconds": {}
                      }
                    },
                    "f:type": {}
                  }
                }
              }
            ]
          },
          "spec": {
            "ports": [
              {
                "name": "tcp-cjmmw9",
                "protocol": "TCP",
                "port": 801,
                "targetPort": 80
              }
            ],
            "selector": {
              "a": "b"
            },
            "clusterIP": "10.97.147.74",
            "type": "ClusterIP",
            "sessionAffinity": "ClientIP",
            "sessionAffinityConfig": {
              "clientIP": {
                "timeoutSeconds": 10800
              }
            }
          },
          "status": {
            "loadBalancer": {}
          }
        },
        "CTime": 1629873532
      }
    ]
  }
}
```


## /v1/topke/endpoints/add
服务端点添加
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
endpoints|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例


#### 正常返回示例


## /v1/topke/endpoints/delete
服务端点删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
endpoints|struct|是|{}| k8s资源描述
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例


#### 正常返回示例


## /v1/topke/endpoints/get
服务端点详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
endpoints|struct|是|{}| k8s资源描述
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例


#### 正常返回示例

## /v1/topke/endpoints/list
服务端点列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant_uuid|string|是|""|租户uuid
fuzzy|string|否|""|模糊匹配
sort_by|string|否|""|排序字段
sort_desc|bool|否|false|是否降序
page_size|int|否|0| 页大小
page_num|int|否|0|页码
workspace|string|否|""|工作名
namespace|string|否|""|命名空间名
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例


#### 正常返回示例

## /v1/topke/pod/add
容器组添加
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
pod|struct|是|{}| k8s资源描述
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例


#### 正常返回示例

## /v1/topke/pod/log/list
容器组日志列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
pod|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/pod/log/list
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"pod": {
		"metadata": {
			"name": "test-7679d8475d-kcfwp",
			"namespace": "default"
		}
	},
	"pod_log_options": {
		"container": "container-guhw08",
		"timestamps": true,
		"tailLines": 20,
		"insecureSkipTLSVerifyBackend": false,
		"follow": false
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
    "total_count": 0,
    "type_meta": null,
    "list_meta": null,
    "end_time": 0,
    "log_list": null,
    "list": null
  }
}
```

## /v1/topke/pod/delete
容器组删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
pod|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/pod/delete
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"pod": {
		"metadata": {
			"name": "test-7679d8475d-kcfwp",
			"namespace": "default"
		}
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
    "total_count": 0,
    "type_meta": null,
    "list_meta": null,
    "end_time": 0,
    "log_list": null,
    "list": null
  }
}
```
## /v1/topke/pod/update
容器组更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
pod|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例


#### 正常返回示例

## /v1/topke/pod/get
容器组详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
pod|struct|是|{}| k8s资源描述
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/pod/get
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"yaml": true,
	"pod": {
		"metadata": {
			"namespace": "default",
			"name": "test-7679d8475d-ctgwj"
		}
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "end_time": 0,
    "log_list": null,
    "list": [
      {
        "kind": "Pod",
        "apiVersion": "v1",
        "metadata": {
          "name": "test-7679d8475d-ctgwj",
          "generateName": "test-7679d8475d-",
          "namespace": "default",
          "selfLink": "/api/v1/namespaces/default/pods/test-7679d8475d-ctgwj",
          "uid": "a843b667-e1b0-4cb7-ba1d-dd6ed989c121",
          "resourceVersion": "12704924",
          "creationTimestamp": "2021-08-25T08:06:04Z",
          "labels": {
            "deployment": "deployment-pvleq1wxys9jtedj71h2itgs",
            "pod-template-hash": "7679d8475d"
          },
          "annotations": {
            "cni.projectcalico.org/podIP": "192.168.237.150/32",
            "cni.projectcalico.org/podIPs": "192.168.237.150/32",
            "podpreset.admission.kubernetes.io/podpreset-sync-timezone": "2587",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629878764",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          },
          "ownerReferences": [
            {
              "apiVersion": "apps/v1",
              "kind": "ReplicaSet",
              "name": "test-7679d8475d",
              "uid": "7eaa2c3b-2cca-47aa-9bb5-cd5bbdad31da",
              "controller": true,
              "blockOwnerDeletion": true
            }
          ]
        },
        "spec": {
          "volumes": [
            {
              "name": "timezone",
              "hostPath": {
                "path": "/usr/share/zoneinfo/Asia/Shanghai",
                "type": ""
              }
            },
            {
              "name": "default-token-vchtg",
              "secret": {
                "secretName": "default-token-vchtg",
                "defaultMode": 420
              }
            }
          ],
          "containers": [
            {
              "name": "container-guhw08",
              "image": "10.30.100.155/library/ubuntu-debug:1",
              "ports": [
                {
                  "name": "tcp-poou7u",
                  "containerPort": 80,
                  "protocol": "TCP"
                }
              ],
              "resources": {
                "limits": {
                  "cpu": "1",
                  "memory": "1000Mi"
                },
                "requests": {
                  "cpu": "50m",
                  "memory": "10Mi"
                }
              },
              "volumeMounts": [
                {
                  "name": "timezone",
                  "mountPath": "/etc/localtime"
                },
                {
                  "name": "default-token-vchtg",
                  "readOnly": true,
                  "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount"
                }
              ],
              "terminationMessagePath": "/dev/termination-log",
              "terminationMessagePolicy": "File",
              "imagePullPolicy": "IfNotPresent"
            }
          ],
          "restartPolicy": "Always",
          "terminationGracePeriodSeconds": 30,
          "dnsPolicy": "ClusterFirst",
          "serviceAccountName": "default",
          "serviceAccount": "default",
          "nodeName": "xxx-10-30-100-220",
          "securityContext": {},
          "affinity": {},
          "schedulerName": "default-scheduler",
          "tolerations": [
            {
              "key": "node.kubernetes.io/not-ready",
              "operator": "Exists",
              "effect": "NoExecute",
              "tolerationSeconds": 300
            },
            {
              "key": "node.kubernetes.io/unreachable",
              "operator": "Exists",
              "effect": "NoExecute",
              "tolerationSeconds": 300
            }
          ],
          "priority": 0,
          "enableServiceLinks": true
        },
        "status": {
          "phase": "Running",
          "conditions": [
            {
              "type": "Initialized",
              "status": "True",
              "lastProbeTime": null,
              "lastTransitionTime": "2021-08-25T08:06:04Z"
            },
            {
              "type": "Ready",
              "status": "True",
              "lastProbeTime": null,
              "lastTransitionTime": "2021-08-25T08:06:06Z"
            },
            {
              "type": "ContainersReady",
              "status": "True",
              "lastProbeTime": null,
              "lastTransitionTime": "2021-08-25T08:06:06Z"
            },
            {
              "type": "PodScheduled",
              "status": "True",
              "lastProbeTime": null,
              "lastTransitionTime": "2021-08-25T08:06:04Z"
            }
          ],
          "hostIP": "10.30.100.220",
          "podIP": "192.168.237.150",
          "podIPs": [
            {
              "ip": "192.168.237.150"
            }
          ],
          "startTime": "2021-08-25T08:06:04Z",
          "containerStatuses": [
            {
              "name": "container-guhw08",
              "state": {
                "running": {
                  "startedAt": "2021-08-25T08:06:06Z"
                }
              },
              "lastState": {},
              "ready": true,
              "restartCount": 0,
              "image": "10.30.100.155/library/ubuntu-debug:1",
              "imageID": "docker-pullable://10.30.100.155/library/ubuntu-debug@sha256:9e4319cd3df02b1107c16769145d6ca4e69893a66c9f696e82a49719d1a7adf4",
              "containerID": "docker://ce3dee75e7f9bc811c717be4516bc701553bba27c2dace1e04fd1be082d70936",
              "started": true
            }
          ],
          "qosClass": "Burstable"
        }
      }
    ]
  }
}
```


## /v1/topke/pod/list
容器组列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
tenant_uuid|string|是|""|租户uuid
fuzzy|string|否|""|模糊匹配
sort_by|string|否|""|排序字段
sort_desc|bool|否|false|是否降序
page_size|int|否|0| 页大小
page_num|int|否|0|页码
workspace|string|否|""|工作名
namespace|string|否|""|命名空间名
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/pod/list
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"namespace": "default",
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"fuzzy": "",
	"page_size": 10,
	"page_num": 0,
	"sort_by": "",
	"sort_desc": false
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
    "type_meta": null,
    "list_meta": null,
    "end_time": 0,
    "log_list": null,
    "list": [
      {
        "kind": "Pod",
        "apiVersion": "v1",
        "metadata": {
          "name": "test-7679d8475d-ctgwj",
          "generateName": "test-7679d8475d-",
          "namespace": "default",
          "selfLink": "/api/v1/namespaces/default/pods/test-7679d8475d-ctgwj",
          "uid": "a843b667-e1b0-4cb7-ba1d-dd6ed989c121",
          "resourceVersion": "12704924",
          "creationTimestamp": "2021-08-25T08:06:04Z",
          "labels": {
            "deployment": "deployment-pvleq1wxys9jtedj71h2itgs",
            "pod-template-hash": "7679d8475d"
          },
          "annotations": {
            "cni.projectcalico.org/podIP": "192.168.237.150/32",
            "cni.projectcalico.org/podIPs": "192.168.237.150/32",
            "podpreset.admission.kubernetes.io/podpreset-sync-timezone": "2587",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629878764",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          },
          "ownerReferences": [
            {
              "apiVersion": "apps/v1",
              "kind": "ReplicaSet",
              "name": "test-7679d8475d",
              "uid": "7eaa2c3b-2cca-47aa-9bb5-cd5bbdad31da",
              "controller": true,
              "blockOwnerDeletion": true
            }
          ]
        },
        "spec": {
          "volumes": [
            {
              "name": "timezone",
              "hostPath": {
                "path": "/usr/share/zoneinfo/Asia/Shanghai",
                "type": ""
              }
            },
            {
              "name": "default-token-vchtg",
              "secret": {
                "secretName": "default-token-vchtg",
                "defaultMode": 420
              }
            }
          ],
          "containers": [
            {
              "name": "container-guhw08",
              "image": "10.30.100.155/library/ubuntu-debug:1",
              "ports": [
                {
                  "name": "tcp-poou7u",
                  "containerPort": 80,
                  "protocol": "TCP"
                }
              ],
              "resources": {
                "limits": {
                  "cpu": "1",
                  "memory": "1000Mi"
                },
                "requests": {
                  "cpu": "50m",
                  "memory": "10Mi"
                }
              },
              "volumeMounts": [
                {
                  "name": "timezone",
                  "mountPath": "/etc/localtime"
                },
                {
                  "name": "default-token-vchtg",
                  "readOnly": true,
                  "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount"
                }
              ],
              "terminationMessagePath": "/dev/termination-log",
              "terminationMessagePolicy": "File",
              "imagePullPolicy": "IfNotPresent"
            }
          ],
          "restartPolicy": "Always",
          "terminationGracePeriodSeconds": 30,
          "dnsPolicy": "ClusterFirst",
          "serviceAccountName": "default",
          "serviceAccount": "default",
          "nodeName": "xxx-10-30-100-220",
          "securityContext": {},
          "affinity": {},
          "schedulerName": "default-scheduler",
          "tolerations": [
            {
              "key": "node.kubernetes.io/not-ready",
              "operator": "Exists",
              "effect": "NoExecute",
              "tolerationSeconds": 300
            },
            {
              "key": "node.kubernetes.io/unreachable",
              "operator": "Exists",
              "effect": "NoExecute",
              "tolerationSeconds": 300
            }
          ],
          "priority": 0,
          "enableServiceLinks": true
        },
        "status": {
          "phase": "Running",
          "conditions": [
            {
              "type": "Initialized",
              "status": "True",
              "lastProbeTime": null,
              "lastTransitionTime": "2021-08-25T08:06:04Z"
            },
            {
              "type": "Ready",
              "status": "True",
              "lastProbeTime": null,
              "lastTransitionTime": "2021-08-25T08:06:06Z"
            },
            {
              "type": "ContainersReady",
              "status": "True",
              "lastProbeTime": null,
              "lastTransitionTime": "2021-08-25T08:06:06Z"
            },
            {
              "type": "PodScheduled",
              "status": "True",
              "lastProbeTime": null,
              "lastTransitionTime": "2021-08-25T08:06:04Z"
            }
          ],
          "hostIP": "10.30.100.220",
          "podIP": "192.168.237.150",
          "podIPs": [
            {
              "ip": "192.168.237.150"
            }
          ],
          "startTime": "2021-08-25T08:06:04Z",
          "containerStatuses": [
            {
              "name": "container-guhw08",
              "state": {
                "running": {
                  "startedAt": "2021-08-25T08:06:06Z"
                }
              },
              "lastState": {},
              "ready": true,
              "restartCount": 0,
              "image": "10.30.100.155/library/ubuntu-debug:1",
              "imageID": "docker-pullable://10.30.100.155/library/ubuntu-debug@sha256:9e4319cd3df02b1107c16769145d6ca4e69893a66c9f696e82a49719d1a7adf4",
              "containerID": "docker://ce3dee75e7f9bc811c717be4516bc701553bba27c2dace1e04fd1be082d70936",
              "started": true
            }
          ],
          "qosClass": "Burstable"
        },
        "resource_request": {
          "cpu": "50m",
          "memory": "10Mi"
        },
        "resource_limit": {
          "cpu": "1",
          "memory": "1000Mi"
        },
        "pod_status": {
          "status": "Running",
          "message": "",
          "reason": "",
          "ready_containers": 1,
          "total_containers": 1
        },
        "max_restarts": 0,
        "controller": {
          "object_meta": {
            "name": "test",
            "namespace": "default",
            "selfLink": "/apis/apps/v1/namespaces/default/deployments/test",
            "uid": "d6b76928-d84a-4ed7-a2e6-687b82eb6cd5",
            "resourceVersion": "12704926",
            "generation": 1,
            "creationTimestamp": "2021-08-12T08:39:36Z",
            "annotations": {
              "deployment.kubernetes.io/revision": "1",
              "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"metadata\":{\"annotations\":{},\"name\":\"test\",\"namespace\":\"default\"},\"spec\":{\"progressDeadlineSeconds\":600,\"replicas\":1,\"revisionHistoryLimit\":10,\"selector\":{\"matchLabels\":{\"deployment\":\"deployment-pvleq1wxys9jtedj71h2itgs\"}},\"strategy\":{\"rollingUpdate\":{\"maxSurge\":\"25%\",\"maxUnavailable\":\"25%\"},\"type\":\"RollingUpdate\"},\"template\":{\"metadata\":{\"creationTimestamp\":null,\"labels\":{\"deployment\":\"deployment-pvleq1wxys9jtedj71h2itgs\"}},\"spec\":{\"affinity\":{},\"containers\":[{\"image\":\"10.30.100.155/library/ubuntu-debug:1\",\"imagePullPolicy\":\"IfNotPresent\",\"name\":\"container-guhw08\",\"ports\":[{\"containerPort\":80,\"name\":\"tcp-poou7u\",\"protocol\":\"TCP\"}],\"resources\":{\"limits\":{\"cpu\":\"1\",\"memory\":\"1000Mi\"},\"requests\":{\"cpu\":\"50m\",\"memory\":\"10Mi\"}},\"terminationMessagePath\":\"/dev/termination-log\",\"terminationMessagePolicy\":\"File\"}],\"dnsPolicy\":\"ClusterFirst\",\"restartPolicy\":\"Always\",\"schedulerName\":\"default-scheduler\",\"securityContext\":{},\"serviceAccount\":\"default\",\"serviceAccountName\":\"default\",\"terminationGracePeriodSeconds\":30}}}}\n"
            }
          },
          "type_meta": {
            "kind": "Deployment",
            "apiVersion": "apps/v1"
          }
        },
        "node_info": {
          "kind": "Node",
          "name": "xxx-10-30-100-220",
          "uid": "a4465f54-3cd3-4ae7-83eb-0c38e363ded7",
          "apiVersion": "v1",
          "resourceVersion": "12703750"
        },
        "resource_convert": [
          {
            "container": "container-guhw08",
            "limits": {
              "cpu": 1000,
              "memory": 1000
            },
            "requests": {
              "cpu": 50,
              "memory": 10
            }
          }
        ]
      }
    ],
    "each_range_list_state": [
      {
        "cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
        "cluster_name": "111",
        "result": {
          "code": 0,
          "message": "",
          "messageCn": "",
          "stack": null,
          "desc": "",
          "UUID": "",
          "message_cn": "",
          "data": "",
          "scode": 0
        },
        "total_count": 1
      }
    ]
  }
}
```

## /v1/topke/deployment/create
无状态副本集创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
deployment|struct|是|{}| k8s资源描述
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/deployment/create
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"deployment": {
		"metadata": {
			"namespace": "default",
			"labels": {},
			"annotations": {
				"topke.desc": ""
			},
			"name": "aaa"
		},
		"spec": {
			"replicas": 1,
			"selector": {
				"matchLabels": {
					"deployment": "deployment-ukqi2x4s1v149nx7gm7olpy6"
				}
			},
			"template": {
				"metadata": {
					"labels": {
						"deployment": "deployment-ukqi2x4s1v149nx7gm7olpy6"
					}
				},
				"spec": {
					"nodeSelector": {},
					"containers": [{
						"name": "container-rc6irq",
						"imagePullPolicy": "IfNotPresent",
						"resources": {
							"requests": {
								"cpu": "50m",
								"memory": "10Mi"
							},
							"limits": {
								"cpu": "1000m",
								"memory": "1000Mi"
							}
						},
						"image": "10.30.100.155/library/nginx:11",
						"ports": [{
							"protocol": "TCP",
							"name": "tcp-hskz6j",
							"containerPort": 80
						}],
						"command": [],
						"args": [],
						"env": [],
						"volumeMounts": []
					}],
					"affinity": {},
					"serviceAccount": "default",
					"initContainers": [],
					"imagePullSecrets": [],
					"volumes": []
				}
			},
			"strategy": {
				"type": "RollingUpdate"
			}
		}
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
    "type_meta": null,
    "list_meta": null,
    "static_total_count": 0,
    "total_count": 1,
    "version_list": null,
    "list": [
      {
        "kind": "Deployment",
        "apiVersion": "apps/v1",
        "metadata": {
          "name": "aaa",
          "namespace": "default",
          "selfLink": "/apis/apps/v1/namespaces/default/deployments/aaa",
          "uid": "89c5bcab-62bf-4ae6-9735-d339cee1b9a4",
          "resourceVersion": "12707264",
          "generation": 1,
          "creationTimestamp": "2021-08-25T08:13:51Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629879231",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "replicas": 1,
          "selector": {
            "matchLabels": {
              "deployment": "deployment-ukqi2x4s1v149nx7gm7olpy6"
            }
          },
          "template": {
            "metadata": {
              "creationTimestamp": null,
              "labels": {
                "deployment": "deployment-ukqi2x4s1v149nx7gm7olpy6"
              }
            },
            "spec": {
              "containers": [
                {
                  "name": "container-rc6irq",
                  "image": "10.30.100.155/library/nginx:11",
                  "ports": [
                    {
                      "name": "tcp-hskz6j",
                      "containerPort": 80,
                      "protocol": "TCP"
                    }
                  ],
                  "resources": {
                    "limits": {
                      "cpu": "1",
                      "memory": "1000Mi"
                    },
                    "requests": {
                      "cpu": "50m",
                      "memory": "10Mi"
                    }
                  },
                  "terminationMessagePath": "/dev/termination-log",
                  "terminationMessagePolicy": "File",
                  "imagePullPolicy": "IfNotPresent"
                }
              ],
              "restartPolicy": "Always",
              "terminationGracePeriodSeconds": 30,
              "dnsPolicy": "ClusterFirst",
              "serviceAccountName": "default",
              "serviceAccount": "default",
              "securityContext": {},
              "affinity": {},
              "schedulerName": "default-scheduler"
            }
          },
          "strategy": {
            "type": "RollingUpdate",
            "rollingUpdate": {
              "maxUnavailable": "25%",
              "maxSurge": "25%"
            }
          },
          "revisionHistoryLimit": 10,
          "progressDeadlineSeconds": 600
        },
        "status": {},
        "resource_convert": [
          {
            "container": "container-rc6irq",
            "limits": {
              "cpu": 1000,
              "memory": 1000
            },
            "requests": {
              "cpu": 50,
              "memory": 10
            }
          }
        ]
      }
    ]
  }
}
```

## /v1/topke/deployment/recreate
无状态副本集容器组重创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
deployment|struct|是|{}| k8s资源描述
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/deployment/recreate
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"deployment": {
		"metadata": {
			"namespace": "default",
			"name": "aaa"
		}
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
    "type_meta": null,
    "list_meta": null,
    "static_total_count": 0,
    "total_count": 1,
    "version_list": null,
    "list": [
      {
        "kind": "Deployment",
        "apiVersion": "apps/v1",
        "metadata": {
          "name": "aaa",
          "namespace": "default",
          "selfLink": "/apis/apps/v1/namespaces/default/deployments/aaa",
          "uid": "89c5bcab-62bf-4ae6-9735-d339cee1b9a4",
          "resourceVersion": "12707295",
          "generation": 1,
          "creationTimestamp": "2021-08-25T08:13:51Z",
          "annotations": {
            "deployment.kubernetes.io/revision": "1",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629879231",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "replicas": 1,
          "selector": {
            "matchLabels": {
              "deployment": "deployment-ukqi2x4s1v149nx7gm7olpy6"
            }
          },
          "template": {
            "metadata": {
              "creationTimestamp": null,
              "labels": {
                "deployment": "deployment-ukqi2x4s1v149nx7gm7olpy6"
              }
            },
            "spec": {
              "containers": [
                {
                  "name": "container-rc6irq",
                  "image": "10.30.100.155/library/nginx:11",
                  "ports": [
                    {
                      "name": "tcp-hskz6j",
                      "containerPort": 80,
                      "protocol": "TCP"
                    }
                  ],
                  "resources": {
                    "limits": {
                      "cpu": "1",
                      "memory": "1000Mi"
                    },
                    "requests": {
                      "cpu": "50m",
                      "memory": "10Mi"
                    }
                  },
                  "terminationMessagePath": "/dev/termination-log",
                  "terminationMessagePolicy": "File",
                  "imagePullPolicy": "IfNotPresent"
                }
              ],
              "restartPolicy": "Always",
              "terminationGracePeriodSeconds": 30,
              "dnsPolicy": "ClusterFirst",
              "serviceAccountName": "default",
              "serviceAccount": "default",
              "securityContext": {},
              "affinity": {},
              "schedulerName": "default-scheduler"
            }
          },
          "strategy": {
            "type": "RollingUpdate",
            "rollingUpdate": {
              "maxUnavailable": "25%",
              "maxSurge": "25%"
            }
          },
          "revisionHistoryLimit": 10,
          "progressDeadlineSeconds": 600
        },
        "status": {
          "observedGeneration": 1,
          "replicas": 1,
          "updatedReplicas": 1,
          "readyReplicas": 1,
          "availableReplicas": 1,
          "conditions": [
            {
              "type": "Available",
              "status": "True",
              "lastUpdateTime": "2021-08-25T08:13:54Z",
              "lastTransitionTime": "2021-08-25T08:13:54Z",
              "reason": "MinimumReplicasAvailable",
              "message": "Deployment has minimum availability."
            },
            {
              "type": "Progressing",
              "status": "True",
              "lastUpdateTime": "2021-08-25T08:13:54Z",
              "lastTransitionTime": "2021-08-25T08:13:51Z",
              "reason": "NewReplicaSetAvailable",
              "message": "ReplicaSet \"aaa-659c65cff4\" has successfully progressed."
            }
          ]
        },
        "resource_convert": [
          {
            "container": "container-rc6irq",
            "limits": {
              "cpu": 1000,
              "memory": 1000
            },
            "requests": {
              "cpu": 50,
              "memory": 10
            }
          }
        ]
      }
    ]
  }
}
```
## /v1/topke/deployment/delete
无状态副本集删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
deployment|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/deployment/delete
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"deployment": {
		"metadata": {
			"name": "aaa",
			"namespace": "default"
		}
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
    "type_meta": null,
    "list_meta": null,
    "static_total_count": 0,
    "total_count": 0,
    "version_list": null,
    "list": null
  }
}
```
## /v1/topke/deployment/update
无状态副本集更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
deployment|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/deployment/update
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"yaml": true,
	"deployment": {
		"kind": "Deployment",
		"apiVersion": "apps/v1",
		"metadata": {
			"name": "test",
			"namespace": "default",
			"selfLink": "/apis/apps/v1/namespaces/default/deployments/test",
			"uid": "d6b76928-d84a-4ed7-a2e6-687b82eb6cd5",
			"resourceVersion": "12704926",
			"generation": 1,
			"creationTimestamp": "2021-08-12T08:39:36Z",
			"annotations": {
				"deployment.kubernetes.io/revision": "1",
				"kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"metadata\":{\"annotations\":{},\"name\":\"test\",\"namespace\":\"default\"},\"spec\":{\"progressDeadlineSeconds\":600,\"replicas\":1,\"revisionHistoryLimit\":10,\"selector\":{\"matchLabels\":{\"deployment\":\"deployment-pvleq1wxys9jtedj71h2itgs\"}},\"strategy\":{\"rollingUpdate\":{\"maxSurge\":\"25%\",\"maxUnavailable\":\"25%\"},\"type\":\"RollingUpdate\"},\"template\":{\"metadata\":{\"creationTimestamp\":null,\"labels\":{\"deployment\":\"deployment-pvleq1wxys9jtedj71h2itgs\"}},\"spec\":{\"affinity\":{},\"containers\":[{\"image\":\"10.30.100.155/library/ubuntu-debug:1\",\"imagePullPolicy\":\"IfNotPresent\",\"name\":\"container-guhw08\",\"ports\":[{\"containerPort\":80,\"name\":\"tcp-poou7u\",\"protocol\":\"TCP\"}],\"resources\":{\"limits\":{\"cpu\":\"1\",\"memory\":\"1000Mi\"},\"requests\":{\"cpu\":\"50m\",\"memory\":\"10Mi\"}},\"terminationMessagePath\":\"/dev/termination-log\",\"terminationMessagePolicy\":\"File\"}],\"dnsPolicy\":\"ClusterFirst\",\"restartPolicy\":\"Always\",\"schedulerName\":\"default-scheduler\",\"securityContext\":{},\"serviceAccount\":\"default\",\"serviceAccountName\":\"default\",\"terminationGracePeriodSeconds\":30}}}}\n",
				"topke.cluster.name": "111",
				"topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
				"topke.createtime.unix": "1628757576",
				"topke.tenant.name": "dev",
				"topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
			}
		},
		"spec": {
			"replicas": 1,
			"selector": {
				"matchLabels": {
					"deployment": "deployment-pvleq1wxys9jtedj71h2itgs"
				}
			},
			"template": {
				"metadata": {
					"creationTimestamp": null,
					"labels": {
						"deployment": "deployment-pvleq1wxys9jtedj71h2itgs"
					}
				},
				"spec": {
					"containers": [{
						"name": "container-guhw08",
						"image": "10.30.100.155/library/ubuntu-debug:2",
						"ports": [{
							"name": "tcp-poou7u",
							"containerPort": 80,
							"protocol": "TCP"
						}],
						"resources": {
							"limits": {
								"cpu": "1",
								"memory": "1000Mi"
							},
							"requests": {
								"cpu": "50m",
								"memory": "10Mi"
							}
						},
						"terminationMessagePath": "/dev/termination-log",
						"terminationMessagePolicy": "File",
						"imagePullPolicy": "IfNotPresent"
					}],
					"restartPolicy": "Always",
					"terminationGracePeriodSeconds": 30,
					"dnsPolicy": "ClusterFirst",
					"serviceAccountName": "default",
					"serviceAccount": "default",
					"securityContext": {},
					"affinity": {},
					"schedulerName": "default-scheduler"
				}
			},
			"strategy": {
				"type": "RollingUpdate",
				"rollingUpdate": {
					"maxUnavailable": "25%",
					"maxSurge": "25%"
				}
			},
			"revisionHistoryLimit": 10,
			"progressDeadlineSeconds": 600
		},
		"status": {
			"observedGeneration": 1,
			"replicas": 1,
			"updatedReplicas": 1,
			"readyReplicas": 1,
			"availableReplicas": 1,
			"conditions": [{
				"type": "Progressing",
				"status": "True",
				"lastUpdateTime": "2021-08-12T08:39:36Z",
				"lastTransitionTime": "2021-08-12T08:39:36Z",
				"reason": "NewReplicaSetAvailable",
				"message": "ReplicaSet \"test-7679d8475d\" has successfully progressed."
			}, {
				"type": "Available",
				"status": "True",
				"lastUpdateTime": "2021-08-25T08:06:06Z",
				"lastTransitionTime": "2021-08-25T08:06:06Z",
				"reason": "MinimumReplicasAvailable",
				"message": "Deployment has minimum availability."
			}]
		}
	},
	"cluster_uuid": "43f771ba-87b6-4f20-9633-3bc04e0dc379"
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
    "type_meta": null,
    "list_meta": null,
    "static_total_count": 0,
    "total_count": 1,
    "version_list": null,
    "list": [
      {
        "kind": "Deployment",
        "apiVersion": "apps/v1",
        "metadata": {
          "name": "test",
          "namespace": "default",
          "selfLink": "/apis/apps/v1/namespaces/default/deployments/test",
          "uid": "d6b76928-d84a-4ed7-a2e6-687b82eb6cd5",
          "resourceVersion": "12708100",
          "generation": 2,
          "creationTimestamp": "2021-08-12T08:39:36Z",
          "annotations": {
            "deployment.kubernetes.io/revision": "1",
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"metadata\":{\"annotations\":{},\"name\":\"test\",\"namespace\":\"default\"},\"spec\":{\"progressDeadlineSeconds\":600,\"replicas\":1,\"revisionHistoryLimit\":10,\"selector\":{\"matchLabels\":{\"deployment\":\"deployment-pvleq1wxys9jtedj71h2itgs\"}},\"strategy\":{\"rollingUpdate\":{\"maxSurge\":\"25%\",\"maxUnavailable\":\"25%\"},\"type\":\"RollingUpdate\"},\"template\":{\"metadata\":{\"creationTimestamp\":null,\"labels\":{\"deployment\":\"deployment-pvleq1wxys9jtedj71h2itgs\"}},\"spec\":{\"affinity\":{},\"containers\":[{\"image\":\"10.30.100.155/library/ubuntu-debug:1\",\"imagePullPolicy\":\"IfNotPresent\",\"name\":\"container-guhw08\",\"ports\":[{\"containerPort\":80,\"name\":\"tcp-poou7u\",\"protocol\":\"TCP\"}],\"resources\":{\"limits\":{\"cpu\":\"1\",\"memory\":\"1000Mi\"},\"requests\":{\"cpu\":\"50m\",\"memory\":\"10Mi\"}},\"terminationMessagePath\":\"/dev/termination-log\",\"terminationMessagePolicy\":\"File\"}],\"dnsPolicy\":\"ClusterFirst\",\"restartPolicy\":\"Always\",\"schedulerName\":\"default-scheduler\",\"securityContext\":{},\"serviceAccount\":\"default\",\"serviceAccountName\":\"default\",\"terminationGracePeriodSeconds\":30}}}}\n",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1628757576",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "replicas": 1,
          "selector": {
            "matchLabels": {
              "deployment": "deployment-pvleq1wxys9jtedj71h2itgs"
            }
          },
          "template": {
            "metadata": {
              "creationTimestamp": null,
              "labels": {
                "deployment": "deployment-pvleq1wxys9jtedj71h2itgs"
              }
            },
            "spec": {
              "containers": [
                {
                  "name": "container-guhw08",
                  "image": "10.30.100.155/library/ubuntu-debug:2",
                  "ports": [
                    {
                      "name": "tcp-poou7u",
                      "containerPort": 80,
                      "protocol": "TCP"
                    }
                  ],
                  "resources": {
                    "limits": {
                      "cpu": "1",
                      "memory": "1000Mi"
                    },
                    "requests": {
                      "cpu": "50m",
                      "memory": "10Mi"
                    }
                  },
                  "terminationMessagePath": "/dev/termination-log",
                  "terminationMessagePolicy": "File",
                  "imagePullPolicy": "IfNotPresent"
                }
              ],
              "restartPolicy": "Always",
              "terminationGracePeriodSeconds": 30,
              "dnsPolicy": "ClusterFirst",
              "serviceAccountName": "default",
              "serviceAccount": "default",
              "securityContext": {},
              "affinity": {},
              "schedulerName": "default-scheduler"
            }
          },
          "strategy": {
            "type": "RollingUpdate",
            "rollingUpdate": {
              "maxUnavailable": "25%",
              "maxSurge": "25%"
            }
          },
          "revisionHistoryLimit": 10,
          "progressDeadlineSeconds": 600
        },
        "status": {
          "observedGeneration": 1,
          "replicas": 1,
          "updatedReplicas": 1,
          "readyReplicas": 1,
          "availableReplicas": 1,
          "conditions": [
            {
              "type": "Progressing",
              "status": "True",
              "lastUpdateTime": "2021-08-12T08:39:36Z",
              "lastTransitionTime": "2021-08-12T08:39:36Z",
              "reason": "NewReplicaSetAvailable",
              "message": "ReplicaSet \"test-7679d8475d\" has successfully progressed."
            },
            {
              "type": "Available",
              "status": "True",
              "lastUpdateTime": "2021-08-25T08:06:06Z",
              "lastTransitionTime": "2021-08-25T08:06:06Z",
              "reason": "MinimumReplicasAvailable",
              "message": "Deployment has minimum availability."
            }
          ]
        }
      }
    ]
  }
}
```

## /v1/topke/deployment/get
无状态副本集详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
deployment|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/deployment/get
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"yaml": true,
	"deployment": {
		"metadata": {
			"namespace": "default",
			"name": "test"
		}
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
    "type_meta": null,
    "list_meta": null,
    "static_total_count": 0,
    "total_count": 1,
    "version_list": null,
    "list": [
      {
        "kind": "Deployment",
        "apiVersion": "apps/v1",
        "metadata": {
          "name": "test",
          "namespace": "default",
          "selfLink": "/apis/apps/v1/namespaces/default/deployments/test",
          "uid": "d6b76928-d84a-4ed7-a2e6-687b82eb6cd5",
          "resourceVersion": "12704926",
          "generation": 1,
          "creationTimestamp": "2021-08-12T08:39:36Z",
          "annotations": {
            "deployment.kubernetes.io/revision": "1",
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"metadata\":{\"annotations\":{},\"name\":\"test\",\"namespace\":\"default\"},\"spec\":{\"progressDeadlineSeconds\":600,\"replicas\":1,\"revisionHistoryLimit\":10,\"selector\":{\"matchLabels\":{\"deployment\":\"deployment-pvleq1wxys9jtedj71h2itgs\"}},\"strategy\":{\"rollingUpdate\":{\"maxSurge\":\"25%\",\"maxUnavailable\":\"25%\"},\"type\":\"RollingUpdate\"},\"template\":{\"metadata\":{\"creationTimestamp\":null,\"labels\":{\"deployment\":\"deployment-pvleq1wxys9jtedj71h2itgs\"}},\"spec\":{\"affinity\":{},\"containers\":[{\"image\":\"10.30.100.155/library/ubuntu-debug:1\",\"imagePullPolicy\":\"IfNotPresent\",\"name\":\"container-guhw08\",\"ports\":[{\"containerPort\":80,\"name\":\"tcp-poou7u\",\"protocol\":\"TCP\"}],\"resources\":{\"limits\":{\"cpu\":\"1\",\"memory\":\"1000Mi\"},\"requests\":{\"cpu\":\"50m\",\"memory\":\"10Mi\"}},\"terminationMessagePath\":\"/dev/termination-log\",\"terminationMessagePolicy\":\"File\"}],\"dnsPolicy\":\"ClusterFirst\",\"restartPolicy\":\"Always\",\"schedulerName\":\"default-scheduler\",\"securityContext\":{},\"serviceAccount\":\"default\",\"serviceAccountName\":\"default\",\"terminationGracePeriodSeconds\":30}}}}\n",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1628757576",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "replicas": 1,
          "selector": {
            "matchLabels": {
              "deployment": "deployment-pvleq1wxys9jtedj71h2itgs"
            }
          },
          "template": {
            "metadata": {
              "creationTimestamp": null,
              "labels": {
                "deployment": "deployment-pvleq1wxys9jtedj71h2itgs"
              }
            },
            "spec": {
              "containers": [
                {
                  "name": "container-guhw08",
                  "image": "10.30.100.155/library/ubuntu-debug:1",
                  "ports": [
                    {
                      "name": "tcp-poou7u",
                      "containerPort": 80,
                      "protocol": "TCP"
                    }
                  ],
                  "resources": {
                    "limits": {
                      "cpu": "1",
                      "memory": "1000Mi"
                    },
                    "requests": {
                      "cpu": "50m",
                      "memory": "10Mi"
                    }
                  },
                  "terminationMessagePath": "/dev/termination-log",
                  "terminationMessagePolicy": "File",
                  "imagePullPolicy": "IfNotPresent"
                }
              ],
              "restartPolicy": "Always",
              "terminationGracePeriodSeconds": 30,
              "dnsPolicy": "ClusterFirst",
              "serviceAccountName": "default",
              "serviceAccount": "default",
              "securityContext": {},
              "affinity": {},
              "schedulerName": "default-scheduler"
            }
          },
          "strategy": {
            "type": "RollingUpdate",
            "rollingUpdate": {
              "maxUnavailable": "25%",
              "maxSurge": "25%"
            }
          },
          "revisionHistoryLimit": 10,
          "progressDeadlineSeconds": 600
        },
        "status": {
          "observedGeneration": 1,
          "replicas": 1,
          "updatedReplicas": 1,
          "readyReplicas": 1,
          "availableReplicas": 1,
          "conditions": [
            {
              "type": "Progressing",
              "status": "True",
              "lastUpdateTime": "2021-08-12T08:39:36Z",
              "lastTransitionTime": "2021-08-12T08:39:36Z",
              "reason": "NewReplicaSetAvailable",
              "message": "ReplicaSet \"test-7679d8475d\" has successfully progressed."
            },
            {
              "type": "Available",
              "status": "True",
              "lastUpdateTime": "2021-08-25T08:06:06Z",
              "lastTransitionTime": "2021-08-25T08:06:06Z",
              "reason": "MinimumReplicasAvailable",
              "message": "Deployment has minimum availability."
            }
          ]
        }
      }
    ]
  }
}
```

## /v1/topke/deployment/list
无状态副本集列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
tenant_uuid|string|是|""|租户uuid
fuzzy|string|否|""|模糊匹配
sort_by|string|否|""|排序字段
sort_desc|bool|否|false|是否降序
page_size|int|否|0| 页大小
page_num|int|否|0|页码
workspace|string|否|""|工作名
namespace|string|否|""|命名空间名
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/deployment/list
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"namespace": "default",
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"fuzzy": "",
	"page_size": 10,
	"page_num": 0,
	"sort_by": "",
	"sort_desc": false
	
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
    "type_meta": null,
    "list_meta": null,
    "static_total_count": 0,
    "total_count": 1,
    "version_list": null,
    "list": [
      {
        "kind": "Deployment",
        "apiVersion": "apps/v1",
        "metadata": {
          "name": "test",
          "namespace": "default",
          "selfLink": "/apis/apps/v1/namespaces/default/deployments/test",
          "uid": "d6b76928-d84a-4ed7-a2e6-687b82eb6cd5",
          "resourceVersion": "12704926",
          "generation": 1,
          "creationTimestamp": "2021-08-12T08:39:36Z",
          "annotations": {
            "deployment.kubernetes.io/revision": "1",
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"metadata\":{\"annotations\":{},\"name\":\"test\",\"namespace\":\"default\"},\"spec\":{\"progressDeadlineSeconds\":600,\"replicas\":1,\"revisionHistoryLimit\":10,\"selector\":{\"matchLabels\":{\"deployment\":\"deployment-pvleq1wxys9jtedj71h2itgs\"}},\"strategy\":{\"rollingUpdate\":{\"maxSurge\":\"25%\",\"maxUnavailable\":\"25%\"},\"type\":\"RollingUpdate\"},\"template\":{\"metadata\":{\"creationTimestamp\":null,\"labels\":{\"deployment\":\"deployment-pvleq1wxys9jtedj71h2itgs\"}},\"spec\":{\"affinity\":{},\"containers\":[{\"image\":\"10.30.100.155/library/ubuntu-debug:1\",\"imagePullPolicy\":\"IfNotPresent\",\"name\":\"container-guhw08\",\"ports\":[{\"containerPort\":80,\"name\":\"tcp-poou7u\",\"protocol\":\"TCP\"}],\"resources\":{\"limits\":{\"cpu\":\"1\",\"memory\":\"1000Mi\"},\"requests\":{\"cpu\":\"50m\",\"memory\":\"10Mi\"}},\"terminationMessagePath\":\"/dev/termination-log\",\"terminationMessagePolicy\":\"File\"}],\"dnsPolicy\":\"ClusterFirst\",\"restartPolicy\":\"Always\",\"schedulerName\":\"default-scheduler\",\"securityContext\":{},\"serviceAccount\":\"default\",\"serviceAccountName\":\"default\",\"terminationGracePeriodSeconds\":30}}}}\n",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1628757576",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "replicas": 1,
          "selector": {
            "matchLabels": {
              "deployment": "deployment-pvleq1wxys9jtedj71h2itgs"
            }
          },
          "template": {
            "metadata": {
              "creationTimestamp": null,
              "labels": {
                "deployment": "deployment-pvleq1wxys9jtedj71h2itgs"
              }
            },
            "spec": {
              "containers": [
                {
                  "name": "container-guhw08",
                  "image": "10.30.100.155/library/ubuntu-debug:1",
                  "ports": [
                    {
                      "name": "tcp-poou7u",
                      "containerPort": 80,
                      "protocol": "TCP"
                    }
                  ],
                  "resources": {
                    "limits": {
                      "cpu": "1",
                      "memory": "1000Mi"
                    },
                    "requests": {
                      "cpu": "50m",
                      "memory": "10Mi"
                    }
                  },
                  "terminationMessagePath": "/dev/termination-log",
                  "terminationMessagePolicy": "File",
                  "imagePullPolicy": "IfNotPresent"
                }
              ],
              "restartPolicy": "Always",
              "terminationGracePeriodSeconds": 30,
              "dnsPolicy": "ClusterFirst",
              "serviceAccountName": "default",
              "serviceAccount": "default",
              "securityContext": {},
              "affinity": {},
              "schedulerName": "default-scheduler"
            }
          },
          "strategy": {
            "type": "RollingUpdate",
            "rollingUpdate": {
              "maxUnavailable": "25%",
              "maxSurge": "25%"
            }
          },
          "revisionHistoryLimit": 10,
          "progressDeadlineSeconds": 600
        },
        "status": {
          "observedGeneration": 1,
          "replicas": 1,
          "updatedReplicas": 1,
          "readyReplicas": 1,
          "availableReplicas": 1,
          "conditions": [
            {
              "type": "Progressing",
              "status": "True",
              "lastUpdateTime": "2021-08-12T08:39:36Z",
              "lastTransitionTime": "2021-08-12T08:39:36Z",
              "reason": "NewReplicaSetAvailable",
              "message": "ReplicaSet \"test-7679d8475d\" has successfully progressed."
            },
            {
              "type": "Available",
              "status": "True",
              "lastUpdateTime": "2021-08-25T08:06:06Z",
              "lastTransitionTime": "2021-08-25T08:06:06Z",
              "reason": "MinimumReplicasAvailable",
              "message": "Deployment has minimum availability."
            }
          ]
        },
        "resource_convert": [
          {
            "container": "container-guhw08",
            "limits": {
              "cpu": 1000,
              "memory": 1000
            },
            "requests": {
              "cpu": 50,
              "memory": 10
            }
          }
        ]
      }
    ],
    "each_range_list_state": [
      {
        "cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
        "cluster_name": "111",
        "result": {
          "code": 0,
          "message": "",
          "messageCn": "",
          "stack": null,
          "desc": "",
          "UUID": "",
          "message_cn": "",
          "data": "",
          "scode": 0
        },
        "total_count": 1
      }
    ]
  }
}
```


## /v1/topke/statefulset/create
创建有状态副本集
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
statefulset|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/statefulset/create
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"statefulset": {
		"metadata": {
			"namespace": "default",
			"labels": {},
			"annotations": {
				"topke.desc": ""
			},
			"name": "aaa"
		},
		"spec": {
			"replicas": 1,
			"selector": {
				"matchLabels": {
					"statefulset": "statefulset-el7kibl2nmh2divcnnzuv1ek"
				}
			},
			"template": {
				"metadata": {
					"labels": {
						"statefulset": "statefulset-el7kibl2nmh2divcnnzuv1ek"
					}
				},
				"spec": {
					"nodeSelector": {},
					"containers": [{
						"name": "container-4bnwx9",
						"imagePullPolicy": "IfNotPresent",
						"resources": {
							"requests": {
								"cpu": "50m",
								"memory": "10Mi"
							},
							"limits": {
								"cpu": "1000m",
								"memory": "1000Mi"
							}
						},
						"image": "10.30.100.155/library/nginx:11",
						"ports": [{
							"protocol": "TCP",
							"name": "tcp-2hsqwh",
							"containerPort": 80
						}],
						"command": [],
						"args": [],
						"env": [],
						"volumeMounts": []
					}],
					"affinity": {},
					"serviceAccount": "default",
					"initContainers": [],
					"imagePullSecrets": [],
					"volumes": []
				}
			},
			"updateStrategy": {
				"type": "RollingUpdate"
			},
			"serviceName": "service-frexxrgnid00eym5k3iuv5r5",
			"volumeClaimTemplates": []
		}
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
    "static_total_count": 0,
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "StatefulSet",
        "apiVersion": "apps/v1",
        "metadata": {
          "name": "aaa",
          "namespace": "default",
          "selfLink": "/apis/apps/v1/namespaces/default/statefulsets/aaa",
          "uid": "494bd08d-5a03-4a2d-af31-e58f57851617",
          "resourceVersion": "12709265",
          "generation": 1,
          "creationTimestamp": "2021-08-25T08:20:17Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629879617",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "replicas": 1,
          "selector": {
            "matchLabels": {
              "statefulset": "statefulset-el7kibl2nmh2divcnnzuv1ek"
            }
          },
          "template": {
            "metadata": {
              "creationTimestamp": null,
              "labels": {
                "statefulset": "statefulset-el7kibl2nmh2divcnnzuv1ek"
              }
            },
            "spec": {
              "containers": [
                {
                  "name": "container-4bnwx9",
                  "image": "10.30.100.155/library/nginx:11",
                  "ports": [
                    {
                      "name": "tcp-2hsqwh",
                      "containerPort": 80,
                      "protocol": "TCP"
                    }
                  ],
                  "resources": {
                    "limits": {
                      "cpu": "1",
                      "memory": "1000Mi"
                    },
                    "requests": {
                      "cpu": "50m",
                      "memory": "10Mi"
                    }
                  },
                  "terminationMessagePath": "/dev/termination-log",
                  "terminationMessagePolicy": "File",
                  "imagePullPolicy": "IfNotPresent"
                }
              ],
              "restartPolicy": "Always",
              "terminationGracePeriodSeconds": 30,
              "dnsPolicy": "ClusterFirst",
              "serviceAccountName": "default",
              "serviceAccount": "default",
              "securityContext": {},
              "affinity": {},
              "schedulerName": "default-scheduler"
            }
          },
          "serviceName": "service-frexxrgnid00eym5k3iuv5r5",
          "podManagementPolicy": "OrderedReady",
          "updateStrategy": {
            "type": "RollingUpdate"
          },
          "revisionHistoryLimit": 10
        },
        "status": {
          "replicas": 0
        },
        "resource_convert": [
          {
            "container": "container-4bnwx9",
            "limits": {
              "cpu": 1000,
              "memory": 1000
            },
            "requests": {
              "cpu": 50,
              "memory": 10
            }
          }
        ]
      }
    ],
    "version_list": null
  }
}
```


## /v1/topke/statefulset/recreate
有状态副本集容器组重建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
statefulset|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/statefulset/recreate
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"statefulset": {
		"metadata": {
			"namespace": "default",
			"name": "aaa"
		}
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
    "static_total_count": 0,
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "StatefulSet",
        "apiVersion": "apps/v1",
        "metadata": {
          "name": "aaa",
          "namespace": "default",
          "selfLink": "/apis/apps/v1/namespaces/default/statefulsets/aaa",
          "uid": "494bd08d-5a03-4a2d-af31-e58f57851617",
          "resourceVersion": "12709298",
          "generation": 1,
          "creationTimestamp": "2021-08-25T08:20:17Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629879617",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "replicas": 1,
          "selector": {
            "matchLabels": {
              "statefulset": "statefulset-el7kibl2nmh2divcnnzuv1ek"
            }
          },
          "template": {
            "metadata": {
              "creationTimestamp": null,
              "labels": {
                "statefulset": "statefulset-el7kibl2nmh2divcnnzuv1ek"
              }
            },
            "spec": {
              "containers": [
                {
                  "name": "container-4bnwx9",
                  "image": "10.30.100.155/library/nginx:11",
                  "ports": [
                    {
                      "name": "tcp-2hsqwh",
                      "containerPort": 80,
                      "protocol": "TCP"
                    }
                  ],
                  "resources": {
                    "limits": {
                      "cpu": "1",
                      "memory": "1000Mi"
                    },
                    "requests": {
                      "cpu": "50m",
                      "memory": "10Mi"
                    }
                  },
                  "terminationMessagePath": "/dev/termination-log",
                  "terminationMessagePolicy": "File",
                  "imagePullPolicy": "IfNotPresent"
                }
              ],
              "restartPolicy": "Always",
              "terminationGracePeriodSeconds": 30,
              "dnsPolicy": "ClusterFirst",
              "serviceAccountName": "default",
              "serviceAccount": "default",
              "securityContext": {},
              "affinity": {},
              "schedulerName": "default-scheduler"
            }
          },
          "serviceName": "service-frexxrgnid00eym5k3iuv5r5",
          "podManagementPolicy": "OrderedReady",
          "updateStrategy": {
            "type": "RollingUpdate"
          },
          "revisionHistoryLimit": 10
        },
        "status": {
          "observedGeneration": 1,
          "replicas": 1,
          "readyReplicas": 1,
          "currentReplicas": 1,
          "updatedReplicas": 1,
          "currentRevision": "aaa-5dc4759c54",
          "updateRevision": "aaa-5dc4759c54",
          "collisionCount": 0
        },
        "resource_convert": [
          {
            "container": "container-4bnwx9",
            "limits": {
              "cpu": 1000,
              "memory": 1000
            },
            "requests": {
              "cpu": 50,
              "memory": 10
            }
          }
        ]
      }
    ],
    "version_list": null
  }
}
```

## /v1/topke/statefulset/update
有状态副本集更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
statefulset|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/statefulset/update
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"yaml": true,
	"statefulset": {
		"kind": "StatefulSet",
		"apiVersion": "apps/v1",
		"metadata": {
			"name": "aaa",
			"namespace": "default",
			"selfLink": "/apis/apps/v1/namespaces/default/statefulsets/aaa",
			"uid": "494bd08d-5a03-4a2d-af31-e58f57851617",
			"resourceVersion": "12709997",
			"generation": 1,
			"creationTimestamp": "2021-08-25T08:20:17Z",
			"annotations": {
				"topke.cluster.name": "111",
				"topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
				"topke.createtime.unix": "1629879617",
				"topke.desc": "",
				"topke.tenant.name": "dev",
				"topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
			}
		},
		"spec": {
			"replicas": 1,
			"selector": {
				"matchLabels": {
					"statefulset": "statefulset-el7kibl2nmh2divcnnzuv1ek"
				}
			},
			"template": {
				"metadata": {
					"creationTimestamp": null,
					"labels": {
						"statefulset": "statefulset-el7kibl2nmh2divcnnzuv1ek"
					}
				},
				"spec": {
					"containers": [{
						"name": "container-4bnwx9",
						"image": "10.30.100.155/library/nginx:11",
						"ports": [{
							"name": "tcp-2hsqwh",
							"containerPort": 801,
							"protocol": "TCP"
						}],
						"resources": {
							"limits": {
								"cpu": "1",
								"memory": "1000Mi"
							},
							"requests": {
								"cpu": "50m",
								"memory": "10Mi"
							}
						},
						"terminationMessagePath": "/dev/termination-log",
						"terminationMessagePolicy": "File",
						"imagePullPolicy": "IfNotPresent"
					}],
					"restartPolicy": "Always",
					"terminationGracePeriodSeconds": 30,
					"dnsPolicy": "ClusterFirst",
					"serviceAccountName": "default",
					"serviceAccount": "default",
					"securityContext": {},
					"affinity": {},
					"schedulerName": "default-scheduler"
				}
			},
			"serviceName": "service-frexxrgnid00eym5k3iuv5r5",
			"podManagementPolicy": "OrderedReady",
			"updateStrategy": {
				"type": "RollingUpdate"
			},
			"revisionHistoryLimit": 10
		},
		"status": {
			"observedGeneration": 1,
			"replicas": 1,
			"readyReplicas": 1,
			"currentReplicas": 1,
			"updatedReplicas": 1,
			"currentRevision": "aaa-5dc4759c54",
			"updateRevision": "aaa-5dc4759c54",
			"collisionCount": 0
		}
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
     "static_total_count": 0,
     "total_count": 1,
     "type_meta": null,
     "list_meta": null,
     "list": [
       {
         "kind": "StatefulSet",
         "apiVersion": "apps/v1",
         "metadata": {
           "name": "aaa",
           "namespace": "default",
           "selfLink": "/apis/apps/v1/namespaces/default/statefulsets/aaa",
           "uid": "494bd08d-5a03-4a2d-af31-e58f57851617",
           "resourceVersion": "12710811",
           "generation": 2,
           "creationTimestamp": "2021-08-25T08:20:17Z",
           "annotations": {
             "topke.cluster.name": "111",
             "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
             "topke.createtime.unix": "1629879617",
             "topke.desc": "",
             "topke.tenant.name": "dev",
             "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
           }
         },
         "spec": {
           "replicas": 1,
           "selector": {
             "matchLabels": {
               "statefulset": "statefulset-el7kibl2nmh2divcnnzuv1ek"
             }
           },
           "template": {
             "metadata": {
               "creationTimestamp": null,
               "labels": {
                 "statefulset": "statefulset-el7kibl2nmh2divcnnzuv1ek"
               }
             },
             "spec": {
               "containers": [
                 {
                   "name": "container-4bnwx9",
                   "image": "10.30.100.155/library/nginx:11",
                   "ports": [
                     {
                       "name": "tcp-2hsqwh",
                       "containerPort": 801,
                       "protocol": "TCP"
                     }
                   ],
                   "resources": {
                     "limits": {
                       "cpu": "1",
                       "memory": "1000Mi"
                     },
                     "requests": {
                       "cpu": "50m",
                       "memory": "10Mi"
                     }
                   },
                   "terminationMessagePath": "/dev/termination-log",
                   "terminationMessagePolicy": "File",
                   "imagePullPolicy": "IfNotPresent"
                 }
               ],
               "restartPolicy": "Always",
               "terminationGracePeriodSeconds": 30,
               "dnsPolicy": "ClusterFirst",
               "serviceAccountName": "default",
               "serviceAccount": "default",
               "securityContext": {},
               "affinity": {},
               "schedulerName": "default-scheduler"
             }
           },
           "serviceName": "service-frexxrgnid00eym5k3iuv5r5",
           "podManagementPolicy": "OrderedReady",
           "updateStrategy": {
             "type": "RollingUpdate"
           },
           "revisionHistoryLimit": 10
         },
         "status": {
           "observedGeneration": 1,
           "replicas": 1,
           "readyReplicas": 1,
           "currentReplicas": 1,
           "updatedReplicas": 1,
           "currentRevision": "aaa-5dc4759c54",
           "updateRevision": "aaa-5dc4759c54",
           "collisionCount": 0
         }
       }
     ],
     "version_list": null
   }
 }   
```


## /v1/topke/statefulset/delete
有状态副本集删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
statefulset|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/statefulset/delete
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"statefulset": {
		"metadata": {
			"name": "aaa",
			"namespace": "default"
		}
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
    "static_total_count": 0,
    "total_count": 0,
    "type_meta": null,
    "list_meta": null,
    "list": null,
    "version_list": null
  }
}
```


## /v1/topke/statefulset/get
有状态副本集详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
statefulset|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/statefulset/get
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"yaml": true,
	"statefulset": {
		"metadata": {
			"namespace": "default",
			"name": "aaa"
		}
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
    "static_total_count": 0,
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "StatefulSet",
        "apiVersion": "apps/v1",
        "metadata": {
          "name": "aaa",
          "namespace": "default",
          "selfLink": "/apis/apps/v1/namespaces/default/statefulsets/aaa",
          "uid": "494bd08d-5a03-4a2d-af31-e58f57851617",
          "resourceVersion": "12709997",
          "generation": 1,
          "creationTimestamp": "2021-08-25T08:20:17Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629879617",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "replicas": 1,
          "selector": {
            "matchLabels": {
              "statefulset": "statefulset-el7kibl2nmh2divcnnzuv1ek"
            }
          },
          "template": {
            "metadata": {
              "creationTimestamp": null,
              "labels": {
                "statefulset": "statefulset-el7kibl2nmh2divcnnzuv1ek"
              }
            },
            "spec": {
              "containers": [
                {
                  "name": "container-4bnwx9",
                  "image": "10.30.100.155/library/nginx:11",
                  "ports": [
                    {
                      "name": "tcp-2hsqwh",
                      "containerPort": 80,
                      "protocol": "TCP"
                    }
                  ],
                  "resources": {
                    "limits": {
                      "cpu": "1",
                      "memory": "1000Mi"
                    },
                    "requests": {
                      "cpu": "50m",
                      "memory": "10Mi"
                    }
                  },
                  "terminationMessagePath": "/dev/termination-log",
                  "terminationMessagePolicy": "File",
                  "imagePullPolicy": "IfNotPresent"
                }
              ],
              "restartPolicy": "Always",
              "terminationGracePeriodSeconds": 30,
              "dnsPolicy": "ClusterFirst",
              "serviceAccountName": "default",
              "serviceAccount": "default",
              "securityContext": {},
              "affinity": {},
              "schedulerName": "default-scheduler"
            }
          },
          "serviceName": "service-frexxrgnid00eym5k3iuv5r5",
          "podManagementPolicy": "OrderedReady",
          "updateStrategy": {
            "type": "RollingUpdate"
          },
          "revisionHistoryLimit": 10
        },
        "status": {
          "observedGeneration": 1,
          "replicas": 1,
          "readyReplicas": 1,
          "currentReplicas": 1,
          "updatedReplicas": 1,
          "currentRevision": "aaa-5dc4759c54",
          "updateRevision": "aaa-5dc4759c54",
          "collisionCount": 0
        }
      }
    ],
    "version_list": null
  }
}
```


## /v1/topke/statefulset/list
有状态副本集详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
tenant_uuid|string|是|""|租户uuid
fuzzy|string|否|""|模糊匹配
sort_by|string|否|""|排序字段
sort_desc|bool|否|false|是否降序
page_size|int|否|0| 页大小
page_num|int|否|0|页码
workspace|string|否|""|工作名
namespace|string|否|""|命名空间名
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/statefulset/list
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"namespace": "default",
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"fuzzy": "",
	"page_size": 10,
	"page_num": 0,
	"sort_by": "",
	"sort_desc": false
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
    "static_total_count": 0,
    "total_count": 0,
    "type_meta": null,
    "list_meta": null,
    "list": null,
    "version_list": null,
    "each_range_list_state": [
      {
        "cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
        "cluster_name": "111",
        "result": {
          "code": 0,
          "message": "",
          "messageCn": "",
          "stack": null,
          "desc": "",
          "UUID": "",
          "message_cn": "",
          "data": "",
          "scode": 0
        },
        "total_count": 0
      }
    ]
  }
}
```

## /v1/topke/daemonset/create
守护进程创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
daemonset|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/daemonset/create
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"daemonset": {
		"metadata": {
			"namespace": "aaaa",
			"labels": {},
			"annotations": {
				"topke.desc": ""
			},
			"name": "aaa"
		},
		"spec": {
			"replicas": 1,
			"selector": {
				"matchLabels": {
					"daemonset": "daemonset-ydf0wmkyqwkof9jpn2tsscc6"
				}
			},
			"template": {
				"metadata": {
					"labels": {
						"daemonset": "daemonset-ydf0wmkyqwkof9jpn2tsscc6"
					}
				},
				"spec": {
					"containers": [{
						"name": "container-jeq9sb",
						"imagePullPolicy": "IfNotPresent",
						"resources": {
							"requests": {
								"cpu": "50m",
								"memory": "10Mi"
							},
							"limits": {
								"cpu": "1000m",
								"memory": "1000Mi"
							}
						},
						"image": "10.30.100.155/library/nginx:11",
						"ports": [{
							"protocol": "TCP",
							"name": "tcp-pi6xk8",
							"containerPort": 80
						}],
						"command": [],
						"args": [],
						"env": [],
						"volumeMounts": []
					}],
					"serviceAccount": "default",
					"initContainers": [],
					"imagePullSecrets": [],
					"volumes": []
				}
			},
			"updateStrategy": {
				"type": "RollingUpdate"
			},
			"minReadySeconds": 0
		}
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
    "static_total_count": 0,
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "DaemonSet",
        "apiVersion": "apps/v1",
        "metadata": {
          "name": "aaa",
          "namespace": "aaaa",
          "selfLink": "/apis/apps/v1/namespaces/aaaa/daemonsets/aaa",
          "uid": "97f81279-3bfe-4199-9106-bf649db15e7b",
          "resourceVersion": "12713844",
          "generation": 1,
          "creationTimestamp": "2021-08-25T08:35:24Z",
          "annotations": {
            "deprecated.daemonset.template.generation": "1",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629880524",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "selector": {
            "matchLabels": {
              "daemonset": "daemonset-ydf0wmkyqwkof9jpn2tsscc6"
            }
          },
          "template": {
            "metadata": {
              "creationTimestamp": null,
              "labels": {
                "daemonset": "daemonset-ydf0wmkyqwkof9jpn2tsscc6"
              }
            },
            "spec": {
              "containers": [
                {
                  "name": "container-jeq9sb",
                  "image": "10.30.100.155/library/nginx:11",
                  "ports": [
                    {
                      "name": "tcp-pi6xk8",
                      "containerPort": 80,
                      "protocol": "TCP"
                    }
                  ],
                  "resources": {
                    "limits": {
                      "cpu": "1",
                      "memory": "1000Mi"
                    },
                    "requests": {
                      "cpu": "50m",
                      "memory": "10Mi"
                    }
                  },
                  "terminationMessagePath": "/dev/termination-log",
                  "terminationMessagePolicy": "File",
                  "imagePullPolicy": "IfNotPresent"
                }
              ],
              "restartPolicy": "Always",
              "terminationGracePeriodSeconds": 30,
              "dnsPolicy": "ClusterFirst",
              "serviceAccountName": "default",
              "serviceAccount": "default",
              "securityContext": {},
              "schedulerName": "default-scheduler"
            }
          },
          "updateStrategy": {
            "type": "RollingUpdate",
            "rollingUpdate": {
              "maxUnavailable": 1
            }
          },
          "revisionHistoryLimit": 10
        },
        "status": {
          "currentNumberScheduled": 0,
          "numberMisscheduled": 0,
          "desiredNumberScheduled": 0,
          "numberReady": 0
        },
        "resource_convert": [
          {
            "container": "container-jeq9sb",
            "limits": {
              "cpu": 1000,
              "memory": 1000
            },
            "requests": {
              "cpu": 50,
              "memory": 10
            }
          }
        ]
      }
    ],
    "version_list": null,
    "current_version": null
  }
}

```

## /v1/topke/daemonset/recreate
守护进程容器组重建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
daemonset|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/daemonset/recreate
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"daemonset": {
		"metadata": {
			"namespace": "aaaa",
			"name": "aaa"
		}
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
    "static_total_count": 0,
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "DaemonSet",
        "apiVersion": "apps/v1",
        "metadata": {
          "name": "aaa",
          "namespace": "aaaa",
          "selfLink": "/apis/apps/v1/namespaces/aaaa/daemonsets/aaa",
          "uid": "97f81279-3bfe-4199-9106-bf649db15e7b",
          "resourceVersion": "12713872",
          "generation": 1,
          "creationTimestamp": "2021-08-25T08:35:24Z",
          "annotations": {
            "deprecated.daemonset.template.generation": "1",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629880524",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "selector": {
            "matchLabels": {
              "daemonset": "daemonset-ydf0wmkyqwkof9jpn2tsscc6"
            }
          },
          "template": {
            "metadata": {
              "creationTimestamp": null,
              "labels": {
                "daemonset": "daemonset-ydf0wmkyqwkof9jpn2tsscc6"
              }
            },
            "spec": {
              "containers": [
                {
                  "name": "container-jeq9sb",
                  "image": "10.30.100.155/library/nginx:11",
                  "ports": [
                    {
                      "name": "tcp-pi6xk8",
                      "containerPort": 80,
                      "protocol": "TCP"
                    }
                  ],
                  "resources": {
                    "limits": {
                      "cpu": "1",
                      "memory": "1000Mi"
                    },
                    "requests": {
                      "cpu": "50m",
                      "memory": "10Mi"
                    }
                  },
                  "terminationMessagePath": "/dev/termination-log",
                  "terminationMessagePolicy": "File",
                  "imagePullPolicy": "IfNotPresent"
                }
              ],
              "restartPolicy": "Always",
              "terminationGracePeriodSeconds": 30,
              "dnsPolicy": "ClusterFirst",
              "serviceAccountName": "default",
              "serviceAccount": "default",
              "securityContext": {},
              "schedulerName": "default-scheduler"
            }
          },
          "updateStrategy": {
            "type": "RollingUpdate",
            "rollingUpdate": {
              "maxUnavailable": 1
            }
          },
          "revisionHistoryLimit": 10
        },
        "status": {
          "currentNumberScheduled": 1,
          "numberMisscheduled": 0,
          "desiredNumberScheduled": 1,
          "numberReady": 1,
          "observedGeneration": 1,
          "updatedNumberScheduled": 1,
          "numberAvailable": 1
        },
        "resource_convert": [
          {
            "container": "container-jeq9sb",
            "limits": {
              "cpu": 1000,
              "memory": 1000
            },
            "requests": {
              "cpu": 50,
              "memory": 10
            }
          }
        ]
      }
    ],
    "version_list": null,
    "current_version": null
  }
}
```


## /v1/topke/daemonset/update
守护进程更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
daemonset|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例


#### 正常返回示例

## /v1/topke/daemonset/delete
守护进程删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例


#### 正常返回示例

## /v1/topke/daemonset/get
守护进程详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
daemonset|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/daemonset/get
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"yaml": true,
	"daemonset": {
		"metadata": {
			"namespace": "aaaa",
			"name": "aaa"
		}
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "Secret",
        "apiVersion": "v1",
        "metadata": {
          "name": "default-token-jd42q",
          "namespace": "aaaa",
          "selfLink": "/api/v1/namespaces/aaaa/secrets/default-token-jd42q",
          "uid": "c75bddd2-a646-4f48-ae7c-30acffb75780",
          "resourceVersion": "12673813",
          "creationTimestamp": "2021-08-25T06:32:02Z",
          "annotations": {
            "kubernetes.io/service-account.name": "default",
            "kubernetes.io/service-account.uid": "0fe4819b-d786-473e-8537-72193745b7ac",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629873122",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "data": {
          "ca.crt": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUN5RENDQWJDZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwcmRXSmwKY201bGRHVnpNQjRYRFRJeE1EY3lOekF6TXpnd05Gb1hEVE14TURjeU5UQXpNemd3TkZvd0ZURVRNQkVHQTFVRQpBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUJBS2o5CjBpRW44RzVzTnBLYkVyaUhQazl0RmNNbWNhaVVzVU92QkZZYlYvYU1vZ0RFbGlwVFRIeVlKajh5ODJTQmR3TW0KZFFxRUc3eWpZY1pjdjhwWDVkeTU4emZQSU5PZFNhUWthTFJaSWp4OWVsbVpQTnlyTEZ2QmpBaE9kQUt1NXhNRQpzNjhLZ2U5b09LQVZUU0dtWXZvMDFrRm8vejFDZWZVT3A1bWpTa2xUK1Iycjl1UXVVd2RHN0lMTzd2Yllsb0FDCkdzRXBjNlRucWlqaHM2M29wby9LaWVsVFJOZ0ptd1IwN3ptb05wQ3JFNEFrazdyQlhDRlZkNG9PV0hjZ0pDWjkKWTFFWGFOZUVrRG41c1ZQa2VvSytRZmRPMVFuN1RTbjFxR09mUUFqRTJyYWQxdVFBMXo2U3gzMFpSOU1SRy9MMAp6azE5a2VvdVhwSVNRTFVXbnhzQ0F3RUFBYU1qTUNFd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWRFd0VCCi93UUZNQU1CQWY4d0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFKQjdJWjBhRENGd3BidTNpdVpzanUvRnNPSnAKc2JEa3ZraTRtMVQ4WUxaMzUzalRBd2x0Mndwd3VPbWlzVmZrbHRFemZhUUtOZEhuNU9PbnIxVCs5cTdYY3VwZQovU255dlVNa1Y3c0RKYkJ3c2tzVmpEKzZYTERkYUdGdGRDcURFdkFTTkpOZzJXR0JJYWQycXJwZGsxbXlHSzR1ClFUVW5EYXltTE1tSFNVNCt0SjV0Si93UkhQdEpEa1VJNmhMcVBjUkxSUnQ3SFlvbHRvandHZHlKbU9DR0NnT1IKNFYvYWplS2Y3NzF0QnhzL3BQZm4vNjg4bHpwWHkxOHFFYmsyMzB6NlJYNXlncS8wUCtyOVROeTFmZmFpTlpBVQpvMERvWXRLdmErcDQwaDZ6YUpBaXhCYTAzZDVoWDFVa1hzSE9sY0hYei9CdUlBS2YwQUJZR1p4SkY4dz0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=",
          "namespace": "YWFhYQ==",
          "token": "ZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNklqQmtaR00wUTNsQ2FVVnpTVWd3WmkxS2FqTnlTV2h0VGpsVGIxSXlkMmxTWW5aVE1FWkRSR0phUVdNaWZRLmV5SnBjM01pT2lKcmRXSmxjbTVsZEdWekwzTmxjblpwWTJWaFkyTnZkVzUwSWl3aWEzVmlaWEp1WlhSbGN5NXBieTl6WlhKMmFXTmxZV05qYjNWdWRDOXVZVzFsYzNCaFkyVWlPaUpoWVdGaElpd2lhM1ZpWlhKdVpYUmxjeTVwYnk5elpYSjJhV05sWVdOamIzVnVkQzl6WldOeVpYUXVibUZ0WlNJNkltUmxabUYxYkhRdGRHOXJaVzR0YW1RME1uRWlMQ0pyZFdKbGNtNWxkR1Z6TG1sdkwzTmxjblpwWTJWaFkyTnZkVzUwTDNObGNuWnBZMlV0WVdOamIzVnVkQzV1WVcxbElqb2laR1ZtWVhWc2RDSXNJbXQxWW1WeWJtVjBaWE11YVc4dmMyVnlkbWxqWldGalkyOTFiblF2YzJWeWRtbGpaUzFoWTJOdmRXNTBMblZwWkNJNklqQm1aVFE0TVRsaUxXUTNPRFl0TkRjelpTMDROVE0zTFRjeU1Ua3pOelExWWpkaFl5SXNJbk4xWWlJNkluTjVjM1JsYlRwelpYSjJhV05sWVdOamIzVnVkRHBoWVdGaE9tUmxabUYxYkhRaWZRLmlxVHhVQjRpUVUxWXB6eEFoLUFWYlRNeElIYkxtUHFVVnFjb3hfNWpuekRuTFAwT0JRZVRCejFwQmpvcXJTOGFOSlUzSE5xUU5XU3Ria1dtbUZscEdxVUNJemxmdFBFeS1mcUtxQkZ4TURRTWNMd1RfYnZkSUhLVkR3MEtjNWoyN1h2YWJVcG5UQWJfZVJPSHJ2dkRwZ3FyR01GUGhfRDJweUdUcXhKcUtwbk5vVHhvUUJYMUJZQWp0eHd2empxQ0VwcXpHTXdrcEM5RmdxaENhaEsxTWNHcUxiZnZiSVJTMThfY2hrbDhlakpRd2Z3VUN4ZER2Y3lwT2hHa1M5ZWI1cEJwLTdleFdEamxkdk43d2lIWC03ZWNzMnB3MVBUTDNpU3BQN3Axei1xUHdSbUEwRFNoZ18wb2tIdXZqOTBaNkwtS2hHTy1HUDR6U21IcDBSeXc4Zw=="
        },
        "type": "kubernetes.io/service-account-token"
      }
    ],
    "each_range_list_state": [
      {
        "cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
        "cluster_name": "111",
        "result": {
          "code": 0,
          "message": "",
          "messageCn": "",
          "stack": null,
          "desc": "",
          "UUID": "",
          "message_cn": "",
          "data": "",
          "scode": 0
        },
        "total_count": 1
      }
    ]
  }
}
```

## /v1/topke/daemonset/list
守护进程列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
tenant_uuid|string|是|""|租户uuid
fuzzy|string|否|""|模糊匹配
sort_by|string|否|""|排序字段
sort_desc|bool|否|false|是否降序
page_size|int|否|0| 页大小
page_num|int|否|0|页码
workspace|string|否|""|工作名
namespace|string|否|""|命名空间名
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/daemonset/list
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"namespace": "aaaa",
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"fuzzy": "",
	"page_size": 10,
	"page_num": 0,
	"sort_by": "TopKESortByName",
	"sort_desc": true
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
    "static_total_count": 0,
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "DaemonSet",
        "apiVersion": "apps/v1",
        "metadata": {
          "name": "aaa",
          "namespace": "aaaa",
          "selfLink": "/apis/apps/v1/namespaces/aaaa/daemonsets/aaa",
          "uid": "97f81279-3bfe-4199-9106-bf649db15e7b",
          "resourceVersion": "12713872",
          "generation": 1,
          "creationTimestamp": "2021-08-25T08:35:24Z",
          "annotations": {
            "deprecated.daemonset.template.generation": "1",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629880524",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "selector": {
            "matchLabels": {
              "daemonset": "daemonset-ydf0wmkyqwkof9jpn2tsscc6"
            }
          },
          "template": {
            "metadata": {
              "creationTimestamp": null,
              "labels": {
                "daemonset": "daemonset-ydf0wmkyqwkof9jpn2tsscc6"
              }
            },
            "spec": {
              "containers": [
                {
                  "name": "container-jeq9sb",
                  "image": "10.30.100.155/library/nginx:11",
                  "ports": [
                    {
                      "name": "tcp-pi6xk8",
                      "containerPort": 80,
                      "protocol": "TCP"
                    }
                  ],
                  "resources": {
                    "limits": {
                      "cpu": "1",
                      "memory": "1000Mi"
                    },
                    "requests": {
                      "cpu": "50m",
                      "memory": "10Mi"
                    }
                  },
                  "terminationMessagePath": "/dev/termination-log",
                  "terminationMessagePolicy": "File",
                  "imagePullPolicy": "IfNotPresent"
                }
              ],
              "restartPolicy": "Always",
              "terminationGracePeriodSeconds": 30,
              "dnsPolicy": "ClusterFirst",
              "serviceAccountName": "default",
              "serviceAccount": "default",
              "securityContext": {},
              "schedulerName": "default-scheduler"
            }
          },
          "updateStrategy": {
            "type": "RollingUpdate",
            "rollingUpdate": {
              "maxUnavailable": 1
            }
          },
          "revisionHistoryLimit": 10
        },
        "status": {
          "currentNumberScheduled": 1,
          "numberMisscheduled": 0,
          "desiredNumberScheduled": 1,
          "numberReady": 1,
          "observedGeneration": 1,
          "updatedNumberScheduled": 1,
          "numberAvailable": 1
        },
        "resource_convert": [
          {
            "container": "container-jeq9sb",
            "limits": {
              "cpu": 1000,
              "memory": 1000
            },
            "requests": {
              "cpu": 50,
              "memory": 10
            }
          }
        ]
      }
    ],
    "version_list": null,
    "current_version": null,
    "each_range_list_state": [
      {
        "cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
        "cluster_name": "111",
        "result": {
          "code": 0,
          "message": "",
          "messageCn": "",
          "stack": null,
          "desc": "",
          "UUID": "",
          "message_cn": "",
          "data": "",
          "scode": 0
        },
        "total_count": 1
      }
    ]
  }
}
```

## /v1/topke/job/create
一次性任务创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
daemonset|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/job/create
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"job": {
		"metadata": {
			"namespace": "aaaa",
			"labels": {},
			"annotations": {
				"topke.desc": ""
			},
			"name": "aaa"
		},
		"spec": {
			"template": {
				"metadata": {
					"labels": {
						"Job": "job-7w8or3grxhidjc892l4st1md"
					}
				},
				"spec": {
					"containers": [{
						"name": "container-naoq9p",
						"imagePullPolicy": "IfNotPresent",
						"resources": {
							"requests": {
								"cpu": "50m",
								"memory": "10Mi"
							},
							"limits": {
								"cpu": "1000m",
								"memory": "1000Mi"
							}
						},
						"image": "10.30.100.155/library/nginx:11",
						"ports": [{
							"protocol": "TCP",
							"name": "tcp-6h8jpr",
							"containerPort": 80
						}],
						"command": [],
						"args": [],
						"env": [],
						"volumeMounts": []
					}],
					"restartPolicy": "Never",
					"serviceAccount": "default",
					"initContainers": [],
					"imagePullSecrets": [],
					"volumes": [],
					"nodeSelector": {}
				}
			}
		}
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
    "static_total_count": 0,
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "Job",
        "apiVersion": "batch/v1",
        "metadata": {
          "name": "aaa",
          "namespace": "aaaa",
          "selfLink": "/apis/batch/v1/namespaces/aaaa/jobs/aaa",
          "uid": "f68e9c6a-f19f-48c6-9150-e7c97565bf5e",
          "resourceVersion": "12718539",
          "creationTimestamp": "2021-08-25T08:51:10Z",
          "labels": {
            "Job": "job-7w8or3grxhidjc892l4st1md",
            "controller-uid": "f68e9c6a-f19f-48c6-9150-e7c97565bf5e",
            "job-name": "aaa"
          },
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629881470",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "parallelism": 1,
          "completions": 1,
          "backoffLimit": 6,
          "selector": {
            "matchLabels": {
              "controller-uid": "f68e9c6a-f19f-48c6-9150-e7c97565bf5e"
            }
          },
          "template": {
            "metadata": {
              "creationTimestamp": null,
              "labels": {
                "Job": "job-7w8or3grxhidjc892l4st1md",
                "controller-uid": "f68e9c6a-f19f-48c6-9150-e7c97565bf5e",
                "job-name": "aaa"
              }
            },
            "spec": {
              "containers": [
                {
                  "name": "container-naoq9p",
                  "image": "10.30.100.155/library/nginx:11",
                  "ports": [
                    {
                      "name": "tcp-6h8jpr",
                      "containerPort": 80,
                      "protocol": "TCP"
                    }
                  ],
                  "resources": {
                    "limits": {
                      "cpu": "1",
                      "memory": "1000Mi"
                    },
                    "requests": {
                      "cpu": "50m",
                      "memory": "10Mi"
                    }
                  },
                  "terminationMessagePath": "/dev/termination-log",
                  "terminationMessagePolicy": "File",
                  "imagePullPolicy": "IfNotPresent"
                }
              ],
              "restartPolicy": "Never",
              "terminationGracePeriodSeconds": 30,
              "dnsPolicy": "ClusterFirst",
              "serviceAccountName": "default",
              "serviceAccount": "default",
              "securityContext": {},
              "schedulerName": "default-scheduler"
            }
          }
        },
        "status": {},
        "resource_convert": [
          {
            "container": "container-naoq9p",
            "limits": {
              "cpu": 1000,
              "memory": 1000
            },
            "requests": {
              "cpu": 50,
              "memory": 10
            }
          }
        ]
      }
    ]
  }
}
```


## /v1/topke/job/delete
一次性任务删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
job|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例


#### 正常返回示例


## /v1/topke/job/get
一次性任务详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
job|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/job/get
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"yaml": true,
	"job": {
		"metadata": {
			"namespace": "aaaa",
			"name": "aaa"
		}
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
    "static_total_count": 0,
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "Job",
        "apiVersion": "batch/v1",
        "metadata": {
          "name": "aaa",
          "namespace": "aaaa",
          "selfLink": "/apis/batch/v1/namespaces/aaaa/jobs/aaa",
          "uid": "f68e9c6a-f19f-48c6-9150-e7c97565bf5e",
          "resourceVersion": "12718547",
          "creationTimestamp": "2021-08-25T08:51:10Z",
          "labels": {
            "Job": "job-7w8or3grxhidjc892l4st1md",
            "controller-uid": "f68e9c6a-f19f-48c6-9150-e7c97565bf5e",
            "job-name": "aaa"
          },
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629881470",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "parallelism": 1,
          "completions": 1,
          "backoffLimit": 6,
          "selector": {
            "matchLabels": {
              "controller-uid": "f68e9c6a-f19f-48c6-9150-e7c97565bf5e"
            }
          },
          "template": {
            "metadata": {
              "creationTimestamp": null,
              "labels": {
                "Job": "job-7w8or3grxhidjc892l4st1md",
                "controller-uid": "f68e9c6a-f19f-48c6-9150-e7c97565bf5e",
                "job-name": "aaa"
              }
            },
            "spec": {
              "containers": [
                {
                  "name": "container-naoq9p",
                  "image": "10.30.100.155/library/nginx:11",
                  "ports": [
                    {
                      "name": "tcp-6h8jpr",
                      "containerPort": 80,
                      "protocol": "TCP"
                    }
                  ],
                  "resources": {
                    "limits": {
                      "cpu": "1",
                      "memory": "1000Mi"
                    },
                    "requests": {
                      "cpu": "50m",
                      "memory": "10Mi"
                    }
                  },
                  "terminationMessagePath": "/dev/termination-log",
                  "terminationMessagePolicy": "File",
                  "imagePullPolicy": "IfNotPresent"
                }
              ],
              "restartPolicy": "Never",
              "terminationGracePeriodSeconds": 30,
              "dnsPolicy": "ClusterFirst",
              "serviceAccountName": "default",
              "serviceAccount": "default",
              "securityContext": {},
              "schedulerName": "default-scheduler"
            }
          }
        },
        "status": {
          "startTime": "2021-08-25T08:51:10Z",
          "active": 1
        }
      }
    ]
  }
}
```

## /v1/topke/job/list
一次性任务列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
tenant_uuid|string|是|""|租户uuid
fuzzy|string|否|""|模糊匹配
sort_by|string|否|""|排序字段
sort_desc|bool|否|false|是否降序
page_size|int|否|0| 页大小
page_num|int|否|0|页码
workspace|string|否|""|工作名
namespace|string|否|""|命名空间名
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/job/list
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"namespace": "aaaa",
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"fuzzy": "",
	"page_size": 10,
	"page_num": 0,
	"sort_by": "",
	"sort_desc": false
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
    "static_total_count": 0,
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "Job",
        "apiVersion": "batch/v1",
        "metadata": {
          "name": "aaa",
          "namespace": "aaaa",
          "selfLink": "/apis/batch/v1/namespaces/aaaa/jobs/aaa",
          "uid": "f68e9c6a-f19f-48c6-9150-e7c97565bf5e",
          "resourceVersion": "12718547",
          "creationTimestamp": "2021-08-25T08:51:10Z",
          "labels": {
            "Job": "job-7w8or3grxhidjc892l4st1md",
            "controller-uid": "f68e9c6a-f19f-48c6-9150-e7c97565bf5e",
            "job-name": "aaa"
          },
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629881470",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "parallelism": 1,
          "completions": 1,
          "backoffLimit": 6,
          "selector": {
            "matchLabels": {
              "controller-uid": "f68e9c6a-f19f-48c6-9150-e7c97565bf5e"
            }
          },
          "template": {
            "metadata": {
              "creationTimestamp": null,
              "labels": {
                "Job": "job-7w8or3grxhidjc892l4st1md",
                "controller-uid": "f68e9c6a-f19f-48c6-9150-e7c97565bf5e",
                "job-name": "aaa"
              }
            },
            "spec": {
              "containers": [
                {
                  "name": "container-naoq9p",
                  "image": "10.30.100.155/library/nginx:11",
                  "ports": [
                    {
                      "name": "tcp-6h8jpr",
                      "containerPort": 80,
                      "protocol": "TCP"
                    }
                  ],
                  "resources": {
                    "limits": {
                      "cpu": "1",
                      "memory": "1000Mi"
                    },
                    "requests": {
                      "cpu": "50m",
                      "memory": "10Mi"
                    }
                  },
                  "terminationMessagePath": "/dev/termination-log",
                  "terminationMessagePolicy": "File",
                  "imagePullPolicy": "IfNotPresent"
                }
              ],
              "restartPolicy": "Never",
              "terminationGracePeriodSeconds": 30,
              "dnsPolicy": "ClusterFirst",
              "serviceAccountName": "default",
              "serviceAccount": "default",
              "securityContext": {},
              "schedulerName": "default-scheduler"
            }
          }
        },
        "status": {
          "startTime": "2021-08-25T08:51:10Z",
          "active": 1
        },
        "resource_convert": [
          {
            "container": "container-naoq9p",
            "limits": {
              "cpu": 1000,
              "memory": 1000
            },
            "requests": {
              "cpu": 50,
              "memory": 10
            }
          }
        ]
      }
    ],
    "each_range_list_state": [
      {
        "cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
        "cluster_name": "111",
        "result": {
          "code": 0,
          "message": "",
          "messageCn": "",
          "stack": null,
          "desc": "",
          "UUID": "",
          "message_cn": "",
          "data": "",
          "scode": 0
        },
        "total_count": 1
      }
    ]
  }
}
```
## /v1/topke/cronjob/create
定时任务创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
cronjob|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/cronjob/create
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"cronjob": {
		"metadata": {
			"namespace": "aaaa",
			"labels": {},
			"annotations": {
				"topke.desc": ""
			},
			"name": "aaa"
		},
		"spec": {
			"concurrencyPolicy": "Allow",
			"schedule": "* * * * *",
			"startingDeadlineSeconds": 120,
			"successfulJobsHistoryLimit": 3,
			"failedJobsHistoryLimit": 1,
			"template": {
				"spec": {
					"nodeSelector": {}
				}
			},
			"jobTemplate": {
				"metadata": {
					"labels": {
						"Cronjob": "cronjob-oqkbmtmqjy0ynqs9dav9tepm"
					}
				},
				"spec": {
					"template": {
						"spec": {
							"containers": [{
								"name": "container-qq8luq",
								"imagePullPolicy": "IfNotPresent",
								"resources": {
									"requests": {
										"cpu": "50m",
										"memory": "10Mi"
									},
									"limits": {
										"cpu": "1000m",
										"memory": "1000Mi"
									}
								},
								"image": "10.30.100.155/library/nginx:11",
								"ports": [{
									"protocol": "TCP",
									"name": "tcp-qrgldx",
									"containerPort": 80
								}],
								"command": [],
								"args": [],
								"env": [],
								"volumeMounts": []
							}],
							"restartPolicy": "Never",
							"serviceAccount": "default",
							"initContainers": [],
							"imagePullSecrets": [],
							"volumes": []
						}
					}
				}
			}
		}
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
    "static_total_count": 0,
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "CronJob",
        "apiVersion": "batch/v1beta1",
        "metadata": {
          "name": "aaa",
          "namespace": "aaaa",
          "selfLink": "/apis/batch/v1beta1/namespaces/aaaa/cronjobs/aaa",
          "uid": "e5d0b00d-7dd3-4944-9a4e-067e7386a016",
          "resourceVersion": "12720321",
          "creationTimestamp": "2021-08-25T08:57:09Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629881829",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "schedule": "* * * * *",
          "startingDeadlineSeconds": 120,
          "concurrencyPolicy": "Allow",
          "suspend": false,
          "jobTemplate": {
            "metadata": {
              "creationTimestamp": null,
              "labels": {
                "Cronjob": "cronjob-oqkbmtmqjy0ynqs9dav9tepm"
              }
            },
            "spec": {
              "template": {
                "metadata": {
                  "creationTimestamp": null
                },
                "spec": {
                  "containers": [
                    {
                      "name": "container-qq8luq",
                      "image": "10.30.100.155/library/nginx:11",
                      "ports": [
                        {
                          "name": "tcp-qrgldx",
                          "containerPort": 80,
                          "protocol": "TCP"
                        }
                      ],
                      "resources": {
                        "limits": {
                          "cpu": "1",
                          "memory": "1000Mi"
                        },
                        "requests": {
                          "cpu": "50m",
                          "memory": "10Mi"
                        }
                      },
                      "terminationMessagePath": "/dev/termination-log",
                      "terminationMessagePolicy": "File",
                      "imagePullPolicy": "IfNotPresent"
                    }
                  ],
                  "restartPolicy": "Never",
                  "terminationGracePeriodSeconds": 30,
                  "dnsPolicy": "ClusterFirst",
                  "serviceAccountName": "default",
                  "serviceAccount": "default",
                  "securityContext": {},
                  "schedulerName": "default-scheduler"
                }
              }
            }
          },
          "successfulJobsHistoryLimit": 3,
          "failedJobsHistoryLimit": 1
        },
        "status": {},
        "resource_convert": [
          {
            "container": "container-qq8luq",
            "limits": {
              "cpu": 1000,
              "memory": 1000
            },
            "requests": {
              "cpu": 50,
              "memory": 10
            }
          }
        ]
      }
    ]
  }
}
```


## /v1/topke/cronjob/delete
定时任务删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
cronjob|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/cronjob/delete
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"cronjob": {
		"metadata": {
			"name": "aaa",
			"namespace": "aaaa"
		}
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
    "static_total_count": 0,
    "total_count": 0,
    "type_meta": null,
    "list_meta": null,
    "list": null
  }
}
```


## /v1/topke/cronjob/update
定时任务更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
cronjob|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/cronjob/update
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"yaml": true,
	"cronjob": {
		"kind": "CronJob",
		"apiVersion": "batch/v1beta1",
		"metadata": {
			"name": "aaa",
			"namespace": "aaaa",
			"selfLink": "/apis/batch/v1beta1/namespaces/aaaa/cronjobs/aaa",
			"uid": "e5d0b00d-7dd3-4944-9a4e-067e7386a016",
			"resourceVersion": "12720601",
			"creationTimestamp": "2021-08-25T08:57:09Z",
			"annotations": {
				"topke.cluster.name": "111",
				"topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
				"topke.createtime.unix": "1629881829",
				"topke.desc": "",
				"topke.tenant.name": "dev",
				"topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
			}
		},
		"spec": {
			"schedule": "* * * * *",
			"startingDeadlineSeconds": 180,
			"concurrencyPolicy": "Allow",
			"suspend": false,
			"jobTemplate": {
				"metadata": {
					"creationTimestamp": null,
					"labels": {
						"Cronjob": "cronjob-oqkbmtmqjy0ynqs9dav9tepm"
					}
				},
				"spec": {
					"template": {
						"metadata": {
							"creationTimestamp": null
						},
						"spec": {
							"containers": [{
								"name": "container-qq8luq",
								"image": "10.30.100.155/library/nginx:11",
								"ports": [{
									"name": "tcp-qrgldx",
									"containerPort": 80,
									"protocol": "TCP"
								}],
								"resources": {
									"limits": {
										"cpu": "1",
										"memory": "1000Mi"
									},
									"requests": {
										"cpu": "50m",
										"memory": "10Mi"
									}
								},
								"terminationMessagePath": "/dev/termination-log",
								"terminationMessagePolicy": "File",
								"imagePullPolicy": "IfNotPresent"
							}],
							"restartPolicy": "Never",
							"terminationGracePeriodSeconds": 30,
							"dnsPolicy": "ClusterFirst",
							"serviceAccountName": "default",
							"serviceAccount": "default",
							"securityContext": {},
							"schedulerName": "default-scheduler"
						}
					}
				}
			},
			"successfulJobsHistoryLimit": 3,
			"failedJobsHistoryLimit": 1
		},
		"status": {
			"active": [{
				"kind": "Job",
				"namespace": "aaaa",
				"name": "aaa-1629881880",
				"uid": "70e34224-2ae1-4ddb-9582-a6d0ebc8ce00",
				"apiVersion": "batch/v1",
				"resourceVersion": "12720600"
			}],
			"lastScheduleTime": "2021-08-25T08:58:00Z"
		}
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
    "static_total_count": 0,
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "CronJob",
        "apiVersion": "batch/v1beta1",
        "metadata": {
          "name": "aaa",
          "namespace": "aaaa",
          "selfLink": "/apis/batch/v1beta1/namespaces/aaaa/cronjobs/aaa",
          "uid": "e5d0b00d-7dd3-4944-9a4e-067e7386a016",
          "resourceVersion": "12721795",
          "creationTimestamp": "2021-08-25T08:57:09Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629881829",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "schedule": "* * * * *",
          "startingDeadlineSeconds": 120,
          "concurrencyPolicy": "Allow",
          "suspend": false,
          "jobTemplate": {
            "metadata": {
              "creationTimestamp": null,
              "labels": {
                "Cronjob": "cronjob-oqkbmtmqjy0ynqs9dav9tepm"
              }
            },
            "spec": {
              "template": {
                "metadata": {
                  "creationTimestamp": null
                },
                "spec": {
                  "containers": [
                    {
                      "name": "container-qq8luq",
                      "image": "10.30.100.155/library/nginx:11",
                      "ports": [
                        {
                          "name": "tcp-qrgldx",
                          "containerPort": 80,
                          "protocol": "TCP"
                        }
                      ],
                      "resources": {
                        "limits": {
                          "cpu": "1",
                          "memory": "1000Mi"
                        },
                        "requests": {
                          "cpu": "50m",
                          "memory": "10Mi"
                        }
                      },
                      "terminationMessagePath": "/dev/termination-log",
                      "terminationMessagePolicy": "File",
                      "imagePullPolicy": "IfNotPresent"
                    }
                  ],
                  "restartPolicy": "Never",
                  "terminationGracePeriodSeconds": 30,
                  "dnsPolicy": "ClusterFirst",
                  "serviceAccountName": "default",
                  "serviceAccount": "default",
                  "securityContext": {},
                  "schedulerName": "default-scheduler"
                }
              }
            }
          },
          "successfulJobsHistoryLimit": 3,
          "failedJobsHistoryLimit": 1
        },
        "status": {
          "active": [
            {
              "kind": "Job",
              "namespace": "aaaa",
              "name": "aaa-1629881880",
              "uid": "70e34224-2ae1-4ddb-9582-a6d0ebc8ce00",
              "apiVersion": "batch/v1",
              "resourceVersion": "12720600"
            },
            {
              "kind": "Job",
              "namespace": "aaaa",
              "name": "aaa-1629881940",
              "uid": "ccad913a-9d0a-4198-8815-0dff3ef3db6b",
              "apiVersion": "batch/v1",
              "resourceVersion": "12720912"
            },
            {
              "kind": "Job",
              "namespace": "aaaa",
              "name": "aaa-1629882000",
              "uid": "890f5903-6753-4629-8d18-4b70bdc4a988",
              "apiVersion": "batch/v1",
              "resourceVersion": "12721218"
            },
            {
              "kind": "Job",
              "namespace": "aaaa",
              "name": "aaa-1629882060",
              "uid": "1945e9d0-4ae3-46f1-ba16-f516b006612d",
              "apiVersion": "batch/v1",
              "resourceVersion": "12721532"
            }
          ],
          "lastScheduleTime": "2021-08-25T09:01:00Z"
        }
      }
    ]
  }
}
```


## /v1/topke/cronjob/get
定时任务详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
cronjob|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/cronjob/get
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"cronjob": {
		"metadata": {
			"namespace": "aaaa",
			"name": "aaa"
		}
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
    "static_total_count": 0,
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "CronJob",
        "apiVersion": "batch/v1beta1",
        "metadata": {
          "name": "aaa",
          "namespace": "aaaa",
          "selfLink": "/apis/batch/v1beta1/namespaces/aaaa/cronjobs/aaa",
          "uid": "e5d0b00d-7dd3-4944-9a4e-067e7386a016",
          "resourceVersion": "12721533",
          "creationTimestamp": "2021-08-25T08:57:09Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629881829",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "schedule": "* * * * *",
          "startingDeadlineSeconds": 120,
          "concurrencyPolicy": "Allow",
          "suspend": false,
          "jobTemplate": {
            "metadata": {
              "creationTimestamp": null,
              "labels": {
                "Cronjob": "cronjob-oqkbmtmqjy0ynqs9dav9tepm"
              }
            },
            "spec": {
              "template": {
                "metadata": {
                  "creationTimestamp": null
                },
                "spec": {
                  "containers": [
                    {
                      "name": "container-qq8luq",
                      "image": "10.30.100.155/library/nginx:11",
                      "ports": [
                        {
                          "name": "tcp-qrgldx",
                          "containerPort": 80,
                          "protocol": "TCP"
                        }
                      ],
                      "resources": {
                        "limits": {
                          "cpu": "1",
                          "memory": "1000Mi"
                        },
                        "requests": {
                          "cpu": "50m",
                          "memory": "10Mi"
                        }
                      },
                      "terminationMessagePath": "/dev/termination-log",
                      "terminationMessagePolicy": "File",
                      "imagePullPolicy": "IfNotPresent"
                    }
                  ],
                  "restartPolicy": "Never",
                  "terminationGracePeriodSeconds": 30,
                  "dnsPolicy": "ClusterFirst",
                  "serviceAccountName": "default",
                  "serviceAccount": "default",
                  "securityContext": {},
                  "schedulerName": "default-scheduler"
                }
              }
            }
          },
          "successfulJobsHistoryLimit": 3,
          "failedJobsHistoryLimit": 1
        },
        "status": {
          "active": [
            {
              "kind": "Job",
              "namespace": "aaaa",
              "name": "aaa-1629881880",
              "uid": "70e34224-2ae1-4ddb-9582-a6d0ebc8ce00",
              "apiVersion": "batch/v1",
              "resourceVersion": "12720600"
            },
            {
              "kind": "Job",
              "namespace": "aaaa",
              "name": "aaa-1629881940",
              "uid": "ccad913a-9d0a-4198-8815-0dff3ef3db6b",
              "apiVersion": "batch/v1",
              "resourceVersion": "12720912"
            },
            {
              "kind": "Job",
              "namespace": "aaaa",
              "name": "aaa-1629882000",
              "uid": "890f5903-6753-4629-8d18-4b70bdc4a988",
              "apiVersion": "batch/v1",
              "resourceVersion": "12721218"
            },
            {
              "kind": "Job",
              "namespace": "aaaa",
              "name": "aaa-1629882060",
              "uid": "1945e9d0-4ae3-46f1-ba16-f516b006612d",
              "apiVersion": "batch/v1",
              "resourceVersion": "12721532"
            }
          ],
          "lastScheduleTime": "2021-08-25T09:01:00Z"
        }
      }
    ]
  }
}

```



## /v1/topke/cronjob/list
定时任务列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
tenant_uuid|string|是|""|租户uuid
fuzzy|string|否|""|模糊匹配
sort_by|string|否|""|排序字段
sort_desc|bool|否|false|是否降序
page_size|int|否|0| 页大小
page_num|int|否|0|页码
workspace|string|否|""|工作名
namespace|string|否|""|命名空间名
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/cronjob/list
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"namespace": "aaaa",
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"fuzzy": "",
	"page_size": 10,
	"page_num": 0,
	"sort_by": "",
	"sort_desc": false
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
    "static_total_count": 0,
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "CronJob",
        "apiVersion": "batch/v1beta1",
        "metadata": {
          "name": "aaa",
          "namespace": "aaaa",
          "selfLink": "/apis/batch/v1beta1/namespaces/aaaa/cronjobs/aaa",
          "uid": "e5d0b00d-7dd3-4944-9a4e-067e7386a016",
          "resourceVersion": "12720321",
          "creationTimestamp": "2021-08-25T08:57:09Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629881829",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "schedule": "* * * * *",
          "startingDeadlineSeconds": 120,
          "concurrencyPolicy": "Allow",
          "suspend": false,
          "jobTemplate": {
            "metadata": {
              "creationTimestamp": null,
              "labels": {
                "Cronjob": "cronjob-oqkbmtmqjy0ynqs9dav9tepm"
              }
            },
            "spec": {
              "template": {
                "metadata": {
                  "creationTimestamp": null
                },
                "spec": {
                  "containers": [
                    {
                      "name": "container-qq8luq",
                      "image": "10.30.100.155/library/nginx:11",
                      "ports": [
                        {
                          "name": "tcp-qrgldx",
                          "containerPort": 80,
                          "protocol": "TCP"
                        }
                      ],
                      "resources": {
                        "limits": {
                          "cpu": "1",
                          "memory": "1000Mi"
                        },
                        "requests": {
                          "cpu": "50m",
                          "memory": "10Mi"
                        }
                      },
                      "terminationMessagePath": "/dev/termination-log",
                      "terminationMessagePolicy": "File",
                      "imagePullPolicy": "IfNotPresent"
                    }
                  ],
                  "restartPolicy": "Never",
                  "terminationGracePeriodSeconds": 30,
                  "dnsPolicy": "ClusterFirst",
                  "serviceAccountName": "default",
                  "serviceAccount": "default",
                  "securityContext": {},
                  "schedulerName": "default-scheduler"
                }
              }
            }
          },
          "successfulJobsHistoryLimit": 3,
          "failedJobsHistoryLimit": 1
        },
        "status": {},
        "resource_convert": [
          {
            "container": "container-qq8luq",
            "limits": {
              "cpu": 1000,
              "memory": 1000
            },
            "requests": {
              "cpu": 50,
              "memory": 10
            }
          }
        ]
      }
    ],
    "each_range_list_state": [
      {
        "cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
        "cluster_name": "111",
        "result": {
          "code": 0,
          "message": "",
          "messageCn": "",
          "stack": null,
          "desc": "",
          "UUID": "",
          "message_cn": "",
          "data": "",
          "scode": 0
        },
        "total_count": 1
      }
    ]
  }
}
```
## /v1/topke/configmap/list
配置表列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
tenant_uuid|string|是|""|租户uuid
fuzzy|string|否|""|模糊匹配
sort_by|string|否|""|排序字段
sort_desc|bool|否|false|是否降序
page_size|int|否|0| 页大小
page_num|int|否|0|页码
workspace|string|否|""|工作名
namespace|string|否|""|命名空间名
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/configmap/list
```
{
	"topke_cluster_uuid": "",
	"namespace": "",
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"fuzzy": "",
	"page_size": 10,
	"page_num": 0,
	"sort_by": "",
	"sort_desc": false
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
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "ConfigMap",
        "apiVersion": "v1",
        "metadata": {
          "name": "cluster-info",
          "namespace": "kube-public",
          "selfLink": "/api/v1/namespaces/kube-public/configmaps/cluster-info",
          "uid": "72e35619-e3e9-4bf6-8c9a-c845cf9b6dec",
          "resourceVersion": "430833",
          "creationTimestamp": "2021-07-27T03:40:13Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1627357213",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "data": {
          "kubeconfig": "apiVersion: v1\nclusters:\n- cluster:\n    certificate-authority-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUN5RENDQWJDZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwcmRXSmwKY201bGRHVnpNQjRYRFRJeE1EY3lOekF6TXpnd05Gb1hEVE14TURjeU5UQXpNemd3TkZvd0ZURVRNQkVHQTFVRQpBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUJBS2o5CjBpRW44RzVzTnBLYkVyaUhQazl0RmNNbWNhaVVzVU92QkZZYlYvYU1vZ0RFbGlwVFRIeVlKajh5ODJTQmR3TW0KZFFxRUc3eWpZY1pjdjhwWDVkeTU4emZQSU5PZFNhUWthTFJaSWp4OWVsbVpQTnlyTEZ2QmpBaE9kQUt1NXhNRQpzNjhLZ2U5b09LQVZUU0dtWXZvMDFrRm8vejFDZWZVT3A1bWpTa2xUK1Iycjl1UXVVd2RHN0lMTzd2Yllsb0FDCkdzRXBjNlRucWlqaHM2M29wby9LaWVsVFJOZ0ptd1IwN3ptb05wQ3JFNEFrazdyQlhDRlZkNG9PV0hjZ0pDWjkKWTFFWGFOZUVrRG41c1ZQa2VvSytRZmRPMVFuN1RTbjFxR09mUUFqRTJyYWQxdVFBMXo2U3gzMFpSOU1SRy9MMAp6azE5a2VvdVhwSVNRTFVXbnhzQ0F3RUFBYU1qTUNFd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWRFd0VCCi93UUZNQU1CQWY4d0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFKQjdJWjBhRENGd3BidTNpdVpzanUvRnNPSnAKc2JEa3ZraTRtMVQ4WUxaMzUzalRBd2x0Mndwd3VPbWlzVmZrbHRFemZhUUtOZEhuNU9PbnIxVCs5cTdYY3VwZQovU255dlVNa1Y3c0RKYkJ3c2tzVmpEKzZYTERkYUdGdGRDcURFdkFTTkpOZzJXR0JJYWQycXJwZGsxbXlHSzR1ClFUVW5EYXltTE1tSFNVNCt0SjV0Si93UkhQdEpEa1VJNmhMcVBjUkxSUnQ3SFlvbHRvandHZHlKbU9DR0NnT1IKNFYvYWplS2Y3NzF0QnhzL3BQZm4vNjg4bHpwWHkxOHFFYmsyMzB6NlJYNXlncS8wUCtyOVROeTFmZmFpTlpBVQpvMERvWXRLdmErcDQwaDZ6YUpBaXhCYTAzZDVoWDFVa1hzSE9sY0hYei9CdUlBS2YwQUJZR1p4SkY4dz0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=\n    server: https://10.30.100.111:8443\n  name: \"\"\ncontexts: null\ncurrent-context: \"\"\nkind: Config\npreferences: {}\nusers: null\n"
        }
      }
    ],
    "each_range_list_state": [
      {
        "cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
        "cluster_name": "111",
        "result": {
          "code": 0,
          "message": "",
          "messageCn": "",
          "stack": null,
          "desc": "",
          "UUID": "",
          "message_cn": "",
          "data": "",
          "scode": 0
        },
        "total_count": 1
      }
    ]
  }
}
```

## /v1/topke/configmap/create
配置表创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
configmap|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/configmap/create
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"configmap": {
		"metadata": {
			"name": "aaa",
			"namespace": "kube-public",
			"annotations": {
				"topke.desc": ""
			}
		},
		"data": {}
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "ConfigMap",
        "apiVersion": "v1",
        "metadata": {
          "name": "aaa",
          "namespace": "kube-public",
          "selfLink": "/api/v1/namespaces/kube-public/configmaps/aaa",
          "uid": "8f779d77-9066-4c9b-8948-aa8a3befd292",
          "resourceVersion": "12725098",
          "creationTimestamp": "2021-08-25T09:12:29Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629882749",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        }
      }
    ]
  }
}
```

## /v1/topke/configmap/update
配置表更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
configmap|struct|是|{}| k8s资源描述
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例


#### 正常返回示例

## /v1/topke/configmap/delete
配置表删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
configmap|struct|是|{}| k8s资源描述
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/configmap/delete
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"configmap": {
		"metadata": {
			"name": "aaa",
			"namespace": "kube-public",
		}
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "Secret",
        "apiVersion": "v1",
        "metadata": {
          "name": "aaa",
          "namespace": "kube-public",
          "selfLink": "/api/v1/namespaces/kube-public/secrets/aaa",
          "uid": "7f7880e1-bd88-4592-9ec6-55ce7540e4ba",
          "resourceVersion": "12727075",
          "creationTimestamp": "2021-08-25T09:19:08Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629883148",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "data": {
          "aa": "YWFh"
        },
        "type": "Opaque"
      }
    ]
  }
}
```

## /v1/topke/configmap/get
配置表详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
configmap|struct|是|{}| k8s资源描述
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/configmap/get
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"configmap": {
		"metadata": {
			"namespace": "kube-public",
			"name": "aaa"
		}
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "ConfigMap",
        "apiVersion": "v1",
        "metadata": {
          "name": "aaa",
          "namespace": "kube-public",
          "selfLink": "/api/v1/namespaces/kube-public/configmaps/aaa",
          "uid": "8f779d77-9066-4c9b-8948-aa8a3befd292",
          "resourceVersion": "12725098",
          "creationTimestamp": "2021-08-25T09:12:29Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629882749",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        }
      }
    ]
  }
}
```

## /v1/topke/configmap/list
配置表列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
tenant_uuid|string|是|""|租户uuid
fuzzy|string|否|""|模糊匹配
sort_by|string|否|""|排序字段
sort_desc|bool|否|false|是否降序
page_size|int|否|0| 页大小
page_num|int|否|0|页码
workspace|string|否|""|工作名
namespace|string|否|""|命名空间名
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/configmap/list
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"namespace": "kube-public",
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"fuzzy": "",
	"page_size": 10,
	"page_num": 0
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
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "ConfigMap",
        "apiVersion": "v1",
        "metadata": {
          "name": "cluster-info",
          "namespace": "kube-public",
          "selfLink": "/api/v1/namespaces/kube-public/configmaps/cluster-info",
          "uid": "72e35619-e3e9-4bf6-8c9a-c845cf9b6dec",
          "resourceVersion": "430833",
          "creationTimestamp": "2021-07-27T03:40:13Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1627357213",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "data": {
          "kubeconfig": "apiVersion: v1\nclusters:\n- cluster:\n    certificate-authority-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUN5RENDQWJDZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwcmRXSmwKY201bGRHVnpNQjRYRFRJeE1EY3lOekF6TXpnd05Gb1hEVE14TURjeU5UQXpNemd3TkZvd0ZURVRNQkVHQTFVRQpBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUJBS2o5CjBpRW44RzVzTnBLYkVyaUhQazl0RmNNbWNhaVVzVU92QkZZYlYvYU1vZ0RFbGlwVFRIeVlKajh5ODJTQmR3TW0KZFFxRUc3eWpZY1pjdjhwWDVkeTU4emZQSU5PZFNhUWthTFJaSWp4OWVsbVpQTnlyTEZ2QmpBaE9kQUt1NXhNRQpzNjhLZ2U5b09LQVZUU0dtWXZvMDFrRm8vejFDZWZVT3A1bWpTa2xUK1Iycjl1UXVVd2RHN0lMTzd2Yllsb0FDCkdzRXBjNlRucWlqaHM2M29wby9LaWVsVFJOZ0ptd1IwN3ptb05wQ3JFNEFrazdyQlhDRlZkNG9PV0hjZ0pDWjkKWTFFWGFOZUVrRG41c1ZQa2VvSytRZmRPMVFuN1RTbjFxR09mUUFqRTJyYWQxdVFBMXo2U3gzMFpSOU1SRy9MMAp6azE5a2VvdVhwSVNRTFVXbnhzQ0F3RUFBYU1qTUNFd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWRFd0VCCi93UUZNQU1CQWY4d0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFKQjdJWjBhRENGd3BidTNpdVpzanUvRnNPSnAKc2JEa3ZraTRtMVQ4WUxaMzUzalRBd2x0Mndwd3VPbWlzVmZrbHRFemZhUUtOZEhuNU9PbnIxVCs5cTdYY3VwZQovU255dlVNa1Y3c0RKYkJ3c2tzVmpEKzZYTERkYUdGdGRDcURFdkFTTkpOZzJXR0JJYWQycXJwZGsxbXlHSzR1ClFUVW5EYXltTE1tSFNVNCt0SjV0Si93UkhQdEpEa1VJNmhMcVBjUkxSUnQ3SFlvbHRvandHZHlKbU9DR0NnT1IKNFYvYWplS2Y3NzF0QnhzL3BQZm4vNjg4bHpwWHkxOHFFYmsyMzB6NlJYNXlncS8wUCtyOVROeTFmZmFpTlpBVQpvMERvWXRLdmErcDQwaDZ6YUpBaXhCYTAzZDVoWDFVa1hzSE9sY0hYei9CdUlBS2YwQUJZR1p4SkY4dz0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=\n    server: https://10.30.100.111:8443\n  name: \"\"\ncontexts: null\ncurrent-context: \"\"\nkind: Config\npreferences: {}\nusers: null\n"
        }
      }
    ],
    "each_range_list_state": [
      {
        "cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
        "cluster_name": "111",
        "result": {
          "code": 0,
          "message": "",
          "messageCn": "",
          "stack": null,
          "desc": "",
          "UUID": "",
          "message_cn": "",
          "data": "",
          "scode": 0
        },
        "total_count": 1
      }
    ]
  }
}
```

## /v1/topke/secret/create
私密数据创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
topke_cluster_uuid|string|是|""|容器云集群uuid
configmap|struct|是|{}| k8s资源描述
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/secret/create
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"secret": {
		"metadata": {
			"namespace": "kube-public",
			"name": "aaa"
		}
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
    }
  }
}
```

## /v1/topke/secret/update
私密数据创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
secret|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"secret": {
		"metadata": {
			"namespace": "kube-public",
			"name": "aaa"
		}
	}
}
```

#### 正常返回示例

## /v1/topke/secret/delete
私密数据删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
secret|struct|是|{}| k8s资源描述
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/secret/delete
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"secret": {
		"metadata": {
			"name": "aaa",
			"namespace": "kube-public"
		}
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
    "total_count": 0,
    "type_meta": null,
    "list_meta": null,
    "list": null
  }
}
```

## /v1/topke/secret/get
私密数据详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
secret|struct|是|{}| k8s资源描述
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/secret/get
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"yaml": true,
	"secret": {
		"metadata": {
			"namespace": "kube-public",
			"name": "aaa"
		}
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "Secret",
        "apiVersion": "v1",
        "metadata": {
          "name": "aaa",
          "namespace": "kube-public",
          "selfLink": "/api/v1/namespaces/kube-public/secrets/aaa",
          "uid": "7f7880e1-bd88-4592-9ec6-55ce7540e4ba",
          "resourceVersion": "12727075",
          "creationTimestamp": "2021-08-25T09:19:08Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629883148",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "data": {
          "aa": "YWFh"
        },
        "type": "Opaque"
      }
    ]
  }
}
```

## /v1/topke/secret/list
私密数据列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
tenant_uuid|string|是|""|租户uuid
fuzzy|string|否|""|模糊匹配
sort_by|string|否|""|排序字段
sort_desc|bool|否|false|是否降序
page_size|int|否|0| 页大小
page_num|int|否|0|页码
workspace|string|否|""|工作名
namespace|string|否|""|命名空间名
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.177/v1/topke/secret/list
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"namespace": "kube-public",
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"fuzzy": "",
	"page_size": 10,
	"page_num": 0,
	"sort_by": "",
	"sort_desc": false
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
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "Secret",
        "apiVersion": "v1",
        "metadata": {
          "name": "default-token-r7mrb",
          "namespace": "kube-public",
          "selfLink": "/api/v1/namespaces/kube-public/secrets/default-token-r7mrb",
          "uid": "afb508a8-804b-4083-a5fc-53f42be1322c",
          "resourceVersion": "268",
          "creationTimestamp": "2021-07-27T03:39:56Z",
          "annotations": {
            "kubernetes.io/service-account.name": "default",
            "kubernetes.io/service-account.uid": "bbabf638-611b-4511-8d97-4ba7e13e3697",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1627357196",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "data": {
          "ca.crt": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUN5RENDQWJDZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwcmRXSmwKY201bGRHVnpNQjRYRFRJeE1EY3lOekF6TXpnd05Gb1hEVE14TURjeU5UQXpNemd3TkZvd0ZURVRNQkVHQTFVRQpBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUJBS2o5CjBpRW44RzVzTnBLYkVyaUhQazl0RmNNbWNhaVVzVU92QkZZYlYvYU1vZ0RFbGlwVFRIeVlKajh5ODJTQmR3TW0KZFFxRUc3eWpZY1pjdjhwWDVkeTU4emZQSU5PZFNhUWthTFJaSWp4OWVsbVpQTnlyTEZ2QmpBaE9kQUt1NXhNRQpzNjhLZ2U5b09LQVZUU0dtWXZvMDFrRm8vejFDZWZVT3A1bWpTa2xUK1Iycjl1UXVVd2RHN0lMTzd2Yllsb0FDCkdzRXBjNlRucWlqaHM2M29wby9LaWVsVFJOZ0ptd1IwN3ptb05wQ3JFNEFrazdyQlhDRlZkNG9PV0hjZ0pDWjkKWTFFWGFOZUVrRG41c1ZQa2VvSytRZmRPMVFuN1RTbjFxR09mUUFqRTJyYWQxdVFBMXo2U3gzMFpSOU1SRy9MMAp6azE5a2VvdVhwSVNRTFVXbnhzQ0F3RUFBYU1qTUNFd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWRFd0VCCi93UUZNQU1CQWY4d0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFKQjdJWjBhRENGd3BidTNpdVpzanUvRnNPSnAKc2JEa3ZraTRtMVQ4WUxaMzUzalRBd2x0Mndwd3VPbWlzVmZrbHRFemZhUUtOZEhuNU9PbnIxVCs5cTdYY3VwZQovU255dlVNa1Y3c0RKYkJ3c2tzVmpEKzZYTERkYUdGdGRDcURFdkFTTkpOZzJXR0JJYWQycXJwZGsxbXlHSzR1ClFUVW5EYXltTE1tSFNVNCt0SjV0Si93UkhQdEpEa1VJNmhMcVBjUkxSUnQ3SFlvbHRvandHZHlKbU9DR0NnT1IKNFYvYWplS2Y3NzF0QnhzL3BQZm4vNjg4bHpwWHkxOHFFYmsyMzB6NlJYNXlncS8wUCtyOVROeTFmZmFpTlpBVQpvMERvWXRLdmErcDQwaDZ6YUpBaXhCYTAzZDVoWDFVa1hzSE9sY0hYei9CdUlBS2YwQUJZR1p4SkY4dz0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=",
          "namespace": "a3ViZS1wdWJsaWM=",
          "token": "ZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNklqQmtaR00wUTNsQ2FVVnpTVWd3WmkxS2FqTnlTV2h0VGpsVGIxSXlkMmxTWW5aVE1FWkRSR0phUVdNaWZRLmV5SnBjM01pT2lKcmRXSmxjbTVsZEdWekwzTmxjblpwWTJWaFkyTnZkVzUwSWl3aWEzVmlaWEp1WlhSbGN5NXBieTl6WlhKMmFXTmxZV05qYjNWdWRDOXVZVzFsYzNCaFkyVWlPaUpyZFdKbExYQjFZbXhwWXlJc0ltdDFZbVZ5Ym1WMFpYTXVhVzh2YzJWeWRtbGpaV0ZqWTI5MWJuUXZjMlZqY21WMExtNWhiV1VpT2lKa1pXWmhkV3gwTFhSdmEyVnVMWEkzYlhKaUlpd2lhM1ZpWlhKdVpYUmxjeTVwYnk5elpYSjJhV05sWVdOamIzVnVkQzl6WlhKMmFXTmxMV0ZqWTI5MWJuUXVibUZ0WlNJNkltUmxabUYxYkhRaUxDSnJkV0psY201bGRHVnpMbWx2TDNObGNuWnBZMlZoWTJOdmRXNTBMM05sY25acFkyVXRZV05qYjNWdWRDNTFhV1FpT2lKaVltRmlaall6T0MwMk1URmlMVFExTVRFdE9HUTVOeTAwWW1FM1pURXpaVE0yT1RjaUxDSnpkV0lpT2lKemVYTjBaVzA2YzJWeWRtbGpaV0ZqWTI5MWJuUTZhM1ZpWlMxd2RXSnNhV002WkdWbVlYVnNkQ0o5LmZmLXpKa01XZ2hYeW85aWZSSFhtQjJBa0tYeGZEdGFweW5EeFZVUnR0ZHFmSkQzdDJYdmNZakFERFVyMFdTYnI3bk1fMXF0UW5kMEZlWVlud1d0aGhlNnJ0VDY5RUlfTDdoQWRUVWROV3p5MlFxYmNGbkZ6SDdMY19XTDl0RHg5ZDJvZVZab3NXY1hBdDZRYTk5NUJadGx0bHdjc2d6SnMwcmE4V2V1SDBiZERTdlRheWR3cVRYUHkwOHFJUlFqMmUxOEtTaV9HNzRfQmpobmdPT1JOOHVWMTQxVktQS05mMVpmbG41ZmNfUHBlM084WGNLMFk1ai1BUlRhanBkTnhIN2lTTEdkU0lRTm40SjJ2LXI1dDF6NlpBQmhIcjN6blM5dVBsODh0MldENEszODFSb09PVERLdFpWVDdWUklWRHlIQ1NhM0lMaHpZd3dadXJWR0pJdw=="
        },
        "type": "kubernetes.io/service-account-token"
      }
    ],
    "each_range_list_state": [
      {
        "cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
        "cluster_name": "111",
        "result": {
          "code": 0,
          "message": "",
          "messageCn": "",
          "stack": null,
          "desc": "",
          "UUID": "",
          "message_cn": "",
          "data": "",
          "scode": 0
        },
        "total_count": 1
      }
    ]
  }
}
```
## /v1/topke/event/list
事件列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
page_size|int|否|0| 页大小
page_num|int|否|0|页码
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.177/v1/topke/event/list
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"page_size": 10,
	"page_num": 0
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
    "total_count": 64,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "Event",
        "apiVersion": "v1",
        "metadata": {
          "name": "xxx-655648d89-6vd6d.169eb5f65be4ba11",
          "namespace": "restic",
          "selfLink": "/api/v1/namespaces/restic/events/xxx-655648d89-6vd6d.169eb5f65be4ba11",
          "uid": "57c47767-0145-4f85-b8c7-d5eb613be022",
          "resourceVersion": "13008777",
          "creationTimestamp": "2021-08-26T01:09:44Z",
          "annotations": {
            "first_timestamp": "1629940184",
            "last_timestamp": "1629940184",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629940184",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "involvedObject": {
          "kind": "Pod",
          "namespace": "restic",
          "name": "xxx-655648d89-6vd6d",
          "uid": "a555176c-11dd-43d1-8b41-74212f5d591c",
          "apiVersion": "v1",
          "resourceVersion": "13008755",
          "fieldPath": "spec.containers{container-d1nkd8}"
        },
        "reason": "Started",
        "message": "Started container container-d1nkd8",
        "source": {
          "component": "kubelet",
          "host": "xxx-10-30-100-220"
        },
        "firstTimestamp": "2021-08-26T01:09:44Z",
        "lastTimestamp": "2021-08-26T01:09:44Z",
        "count": 1,
        "type": "Normal",
        "eventTime": null,
        "reportingComponent": "",
        "reportingInstance": ""
      },
      {
        "kind": "Event",
        "apiVersion": "v1",
        "metadata": {
          "name": "xxx-57fbf8b9cf.169eb5f64031c949",
          "namespace": "restic",
          "selfLink": "/api/v1/namespaces/restic/events/xxx-57fbf8b9cf.169eb5f64031c949",
          "uid": "e7f99cbf-2046-43cf-bbca-f9d6edb95eb2",
          "resourceVersion": "13008787",
          "creationTimestamp": "2021-08-26T01:09:44Z",
          "annotations": {
            "first_timestamp": "1629940184",
            "last_timestamp": "1629940184",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629940184",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "involvedObject": {
          "kind": "ReplicaSet",
          "namespace": "restic",
          "name": "xxx-57fbf8b9cf",
          "uid": "faafd502-d9ff-42c3-9810-5d78357a86df",
          "apiVersion": "apps/v1",
          "resourceVersion": "13008782"
        },
        "reason": "SuccessfulDelete",
        "message": "Deleted pod: xxx-57fbf8b9cf-ksl7w",
        "source": {
          "component": "replicaset-controller"
        },
        "firstTimestamp": "2021-08-26T01:09:44Z",
        "lastTimestamp": "2021-08-26T01:09:44Z",
        "count": 1,
        "type": "Normal",
        "eventTime": null,
        "reportingComponent": "",
        "reportingInstance": ""
      },
      {
        "kind": "Event",
        "apiVersion": "v1",
        "metadata": {
          "name": "xxx-57fbf8b9cf-ksl7w.169eb5f6895350ae",
          "namespace": "restic",
          "selfLink": "/api/v1/namespaces/restic/events/xxx-57fbf8b9cf-ksl7w.169eb5f6895350ae",
          "uid": "daf3c127-cb07-437c-bb15-ad3f6d36eafc",
          "resourceVersion": "13008788",
          "creationTimestamp": "2021-08-26T01:09:44Z",
          "annotations": {
            "first_timestamp": "1629940185",
            "last_timestamp": "1629940185",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629940184",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "involvedObject": {
          "kind": "Pod",
          "namespace": "restic",
          "name": "xxx-57fbf8b9cf-ksl7w",
          "uid": "cec63ad3-d534-4e5d-8f97-14428c3511c6",
          "apiVersion": "v1",
          "resourceVersion": "13006669",
          "fieldPath": "spec.containers{container-d1nkd8}"
        },
        "reason": "Killing",
        "message": "Stopping container container-d1nkd8",
        "source": {
          "component": "kubelet",
          "host": "xxx-10-30-100-220"
        },
        "firstTimestamp": "2021-08-26T01:09:45Z",
        "lastTimestamp": "2021-08-26T01:09:45Z",
        "count": 1,
        "type": "Normal",
        "eventTime": null,
        "reportingComponent": "",
        "reportingInstance": ""
      },
....

```
## /v1/topke/pvc/create
存储卷声明创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
persistent_volume_claim|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/persistent_volume_claim/create
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"persistent_volume_claim": {
		"metadata": {
			"name": "aaa",
			"namespace": "default",
			"labels": {},
			"annotations": {
				"topke.desc": ""
			}
		},
		"spec": {
			"accessModes": ["ReadWriteOnce"],
			"resources": {
				"requests": {
					"storage": "5Gi"
				}
			}
		}
	},
	"cluster_uuid": "43f771ba-87b6-4f20-9633-3bc04e0dc379"
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
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "PersistentVolumeClaim",
        "apiVersion": "v1",
        "metadata": {
          "name": "aaa",
          "namespace": "default",
          "selfLink": "/api/v1/namespaces/default/persistentvolumeclaims/aaa",
          "uid": "06ea5cc4-be07-438c-bbd8-c9ccdf64c4aa",
          "resourceVersion": "12686609",
          "creationTimestamp": "2021-08-25T07:11:18Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629875478",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          },
          "finalizers": [
            "kubernetes.io/pvc-protection"
          ]
        },
        "spec": {
          "accessModes": [
            "ReadWriteOnce"
          ],
          "resources": {
            "requests": {
              "storage": "5Gi"
            }
          },
          "storageClassName": "clouddisk",
          "volumeMode": "Filesystem"
        },
        "status": {
          "phase": "Pending"
        },
        "allow_expansion": false,
        "allow_snapshot": true
      }
    ]
  }
}   
```
## /v1/topke/pvc/delete
存储卷声明删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
persistent_volume_claim|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/persistent_volume_claim/delete
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"persistent_volume_claim": {
		"metadata": {
			"namespace": "default",
			"name": "aaa"
		}
	}
}
```
#### 正常返回示例

## /v1/topke/pvc/update
存储卷声明更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
persistent_volume_claim|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/persistent_volume_claim/update
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"yaml": true,
	"persistent_volume_claim": {
		"kind": "PersistentVolumeClaim",
		"apiVersion": "v1",
		"metadata": {
			"name": "aaa",
			"namespace": "default",
			"selfLink": "/api/v1/namespaces/default/persistentvolumeclaims/aaa",
			"uid": "a574e9e8-d845-4d4c-b496-7b387a907f6c",
			"resourceVersion": "12689440",
			"creationTimestamp": "2021-08-25T07:14:38Z",
			"annotations": {
				"pv.kubernetes.io/bind-completed": "yes",
				"pv.kubernetes.io/bound-by-controller": "yes",
				"topke.cluster.name": "111",
				"topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
				"topke.createtime.unix": "1629875678",
				"topke.desc": "",
				"topke.tenant.name": "dev",
				"topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
				"volume.beta.kubernetes.io/storage-provisioner": "topsc.topke.io"
			},
			"finalizers": ["kubernetes.io/pvc-protection"]
		},
		"spec": {
			"accessModes": ["ReadWriteOnce"],
			"resources": {
				"requests": {
					"storage": "6Gi"
				}
			},
			"volumeName": "pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
			"storageClassName": "clouddisk",
			"volumeMode": "Filesystem"
		},
		"status": {
			"phase": "Bound",
			"accessModes": ["ReadWriteOnce"],
			"capacity": {
				"storage": "5Gi"
			}
		}
	}
}
```

#### 正常返回示例


## /v1/topke/pvc/get
存储卷声明详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
persistent_volume_claim|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/persistent_volume_claim/get
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"yaml": true,
	"persistent_volume_claim": {
		"metadata": {
			"namespace": "default",
			"name": "aaa"
		}
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "PersistentVolumeClaim",
        "apiVersion": "v1",
        "metadata": {
          "name": "aaa",
          "namespace": "default",
          "selfLink": "/api/v1/namespaces/default/persistentvolumeclaims/aaa",
          "uid": "a574e9e8-d845-4d4c-b496-7b387a907f6c",
          "resourceVersion": "12689493",
          "creationTimestamp": "2021-08-25T07:14:38Z",
          "annotations": {
            "pv.kubernetes.io/bind-completed": "yes",
            "pv.kubernetes.io/bound-by-controller": "yes",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629875678",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
            "volume.beta.kubernetes.io/storage-provisioner": "topsc.topke.io"
          },
          "finalizers": [
            "kubernetes.io/pvc-protection"
          ]
        },
        "spec": {
          "accessModes": [
            "ReadWriteOnce"
          ],
          "resources": {
            "requests": {
              "storage": "6Gi"
            }
          },
          "volumeName": "pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
          "storageClassName": "clouddisk",
          "volumeMode": "Filesystem"
        },
        "status": {
          "phase": "Bound",
          "accessModes": [
            "ReadWriteOnce"
          ],
          "capacity": {
            "storage": "6Gi"
          }
        }
      }
    ]
  }
}
```
## /v1/topke/pvc/list
存储卷声明列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
tenant_uuid|string|是|""|租户uuid
fuzzy|string|否|""|模糊匹配
sort_by|string|否|""|排序字段
sort_desc|bool|否|false|是否降序
page_size|int|否|0| 页大小
page_num|int|否|0|页码
workspace|string|否|""|工作名
namespace|string|否|""|命名空间名
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/persistent_volume_claim/list
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"namespace": "default",
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"fuzzy": "",
	"page_size": 10,
	"page_num": 0,
	"sort_by": "",
	"sort_desc": false
}
```
#### 正常返回示例


## /v1/topke/ingress/create
路由创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
ingress|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.177/v1/topke/ingress/create
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"ingress": {
		"metadata": {
			"namespace": "aaaa",
			"labels": {
				"app": "aaaa"
			},
			"name": "aaaa",
			"annotations": {
				"topke.desc": "",
				"kubernetes.io/ingress.class": "nginx"
			}
		},
		"spec": {
			"rules": [{
				"host": "www.goo.com",
				"http": {
					"paths": [{
						"path": "/xx",
						"backend": {
							"serviceName": "aaa",
							"servicePort": 80
						}
					}]
				}
			}]
		}
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "Ingress",
        "apiVersion": "extensions/v1beta1",
        "metadata": {
          "name": "aaaa",
          "namespace": "aaaa",
          "selfLink": "/apis/extensions/v1beta1/namespaces/aaaa/ingresses/aaaa",
          "uid": "2315652d-dfaf-408f-9247-5fa9b37295f9",
          "resourceVersion": "13010858",
          "generation": 1,
          "creationTimestamp": "2021-08-26T01:16:15Z",
          "labels": {
            "app": "aaaa"
          },
          "annotations": {
            "kubernetes.io/ingress.class": "nginx",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629940575",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "rules": [
            {
              "host": "www.goo.com",
              "http": {
                "paths": [
                  {
                    "path": "/xx",
                    "pathType": "ImplementationSpecific",
                    "backend": {
                      "serviceName": "aaa",
                      "servicePort": 80
                    }
                  }
                ]
              }
            }
          ]
        },
        "status": {
          "loadBalancer": {}
        },
        "controller": {
          "kind": "Deployment",
          "namespace": "system-router",
          "name": "router-aaaa",
          "apiVersion": "apps/v1"
        },
        "controller_healthy": true
      }
    ]
  }
}
```

## /v1/topke/ingress/delete
路由删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
ingress|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.177/v1/topke/ingress/delete
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"ingress": {
		"metadata": {
			"name": "xxxx",
			"namespace": "default"
		}
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
    "total_count": 0,
    "type_meta": null,
    "list_meta": null,
    "list": null
  }
}

```


## /v1/topke/ingress/update
路由更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
ingress|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.177/v1/topke/ingress/update
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"yaml": true,
	"ingress": {
		"kind": "Ingress",
		"apiVersion": "extensions/v1beta1",
		"metadata": {
			"name": "aaaa",
			"namespace": "aaaa",
			"selfLink": "/apis/extensions/v1beta1/namespaces/aaaa/ingresses/aaaa",
			"uid": "2315652d-dfaf-408f-9247-5fa9b37295f9",
			"resourceVersion": "13010858",
			"generation": 1,
			"creationTimestamp": "2021-08-26T01:16:15Z",
			"labels": {
				"app": "aaaa"
			},
			"annotations": {
				"kubernetes.io/ingress.class": "nginx",
				"topke.cluster.name": "111",
				"topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
				"topke.createtime.unix": "1629940575",
				"topke.desc": "",
				"topke.tenant.name": "dev",
				"topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
			}
		},
		"spec": {
			"rules": [{
				"host": "www.goo.com",
				"http": {
					"paths": [{
						"path": "/xx",
						"pathType": "ImplementationSpecific",
						"backend": {
							"serviceName": "aaa",
							"servicePort": 801
						}
					}]
				}
			}]
		},
		"status": {
			"loadBalancer": {}
		},
		"controller": {},
		"controller_healthy": false
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "Ingress",
        "apiVersion": "extensions/v1beta1",
        "metadata": {
          "name": "aaaa",
          "namespace": "aaaa",
          "selfLink": "/apis/extensions/v1beta1/namespaces/aaaa/ingresses/aaaa",
          "uid": "2315652d-dfaf-408f-9247-5fa9b37295f9",
          "resourceVersion": "13012435",
          "generation": 2,
          "creationTimestamp": "2021-08-26T01:16:15Z",
          "labels": {
            "app": "aaaa"
          },
          "annotations": {
            "kubernetes.io/ingress.class": "nginx",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629940575",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "rules": [
            {
              "host": "www.goo.com",
              "http": {
                "paths": [
                  {
                    "path": "/xx",
                    "pathType": "ImplementationSpecific",
                    "backend": {
                      "serviceName": "aaa",
                      "servicePort": 801
                    }
                  }
                ]
              }
            }
          ]
        },
        "status": {
          "loadBalancer": {}
        },
        "controller": {},
        "controller_healthy": false
      }
    ]
  }
}   
```

## /v1/topke/ingress/get
路由详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
ingress|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.177/v1/topke/ingress/get
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"ingress": {
		"metadata": {
			"namespace": "aaaa",
			"name": "aaaa"
		}
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "Ingress",
        "apiVersion": "extensions/v1beta1",
        "metadata": {
          "name": "aaaa",
          "namespace": "aaaa",
          "selfLink": "/apis/extensions/v1beta1/namespaces/aaaa/ingresses/aaaa",
          "uid": "2315652d-dfaf-408f-9247-5fa9b37295f9",
          "resourceVersion": "13010858",
          "generation": 1,
          "creationTimestamp": "2021-08-26T01:16:15Z",
          "labels": {
            "app": "aaaa"
          },
          "annotations": {
            "kubernetes.io/ingress.class": "nginx",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629940575",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "rules": [
            {
              "host": "www.goo.com",
              "http": {
                "paths": [
                  {
                    "path": "/xx",
                    "pathType": "ImplementationSpecific",
                    "backend": {
                      "serviceName": "aaa",
                      "servicePort": 80
                    }
                  }
                ]
              }
            }
          ]
        },
        "status": {
          "loadBalancer": {}
        },
        "controller": {
          "kind": "Deployment",
          "namespace": "system-router",
          "name": "router-aaaa",
          "apiVersion": "apps/v1"
        },
        "controller_healthy": true
      }
    ]
  }
}
```


## /v1/topke/ingress/list
路由列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
tenant_uuid|string|是|""|租户uuid
fuzzy|string|否|""|模糊匹配
sort_by|string|否|""|排序字段
sort_desc|bool|否|false|是否降序
page_size|int|否|0| 页大小
page_num|int|否|0|页码
workspace|string|否|""|工作名
namespace|string|否|""|命名空间名
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.177/v1/topke/ingress/list
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"namespace": "aaaa",
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"fuzzy": "",
	"page_size": 10,
	"page_num": 0,
	"sort_by": "",
	"sort_desc": false
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
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "Ingress",
        "apiVersion": "extensions/v1beta1",
        "metadata": {
          "name": "aaaa",
          "namespace": "aaaa",
          "selfLink": "/apis/extensions/v1beta1/namespaces/aaaa/ingresses/aaaa",
          "uid": "2315652d-dfaf-408f-9247-5fa9b37295f9",
          "resourceVersion": "13010858",
          "generation": 1,
          "creationTimestamp": "2021-08-26T01:16:15Z",
          "labels": {
            "app": "aaaa"
          },
          "annotations": {
            "kubernetes.io/ingress.class": "nginx",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629940575",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "rules": [
            {
              "host": "www.goo.com",
              "http": {
                "paths": [
                  {
                    "path": "/xx",
                    "pathType": "ImplementationSpecific",
                    "backend": {
                      "serviceName": "aaa",
                      "servicePort": 80
                    }
                  }
                ]
              }
            }
          ]
        },
        "status": {
          "loadBalancer": {}
        },
        "controller": {
          "kind": "Deployment",
          "namespace": "system-router",
          "name": "router-aaaa",
          "apiVersion": "apps/v1"
        },
        "controller_healthy": true
      }
    ],
    "each_range_list_state": [
      {
        "cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
        "cluster_name": "111",
        "result": {
          "code": 0,
          "message": "",
          "messageCn": "",
          "stack": null,
          "desc": "",
          "UUID": "",
          "message_cn": "",
          "data": "",
          "scode": 0
        },
        "total_count": 1
      }
    ]
  }
}
```

## /v1/topke/hpa/create
水平弹性伸缩创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
horizontal_pod_autoscaler|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.177/v1/topke/hpa/create
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"horizontal_pod_autoscaler": {
		"metadata": {
			"name": "xxxxxxxxx-deployment",
			"namespace": "restic"
		},
		"spec": {
			"scaleTargetRef": {
				"apiVersion": "apps/v1",
				"kind": "Deployment",
				"name": "xxxxxxxxx"
			},
			"minReplicas": 1,
			"maxReplicas": 1,
			"targetCPUUtilizationPercentage": 80
		}
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "HorizontalPodAutoscaler",
        "apiVersion": "autoscaling/v1",
        "metadata": {
          "name": "xxxxxxxxx-deployment",
          "namespace": "restic",
          "selfLink": "/apis/autoscaling/v1/namespaces/restic/horizontalpodautoscalers/xxxxxxxxx-deployment",
          "uid": "76ece3aa-d734-4017-979d-84fe8e09fbf3",
          "resourceVersion": "13014686",
          "creationTimestamp": "2021-08-26T01:29:08Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629941348",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "scaleTargetRef": {
            "kind": "Deployment",
            "name": "xxxxxxxxx",
            "apiVersion": "apps/v1"
          },
          "minReplicas": 1,
          "maxReplicas": 1,
          "targetCPUUtilizationPercentage": 80
        },
        "status": {
          "currentReplicas": 0,
          "desiredReplicas": 0
        }
      }
    ]
  }
}
```

## /v1/topke/hpa/delete
水平弹性伸缩删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
horizontal_pod_autoscaler|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.177/v1/topke/hpa/delete
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"horizontal_pod_autoscaler": {
		"metadata": {
			"name": "xxxxxxxxx-deployment",
			"namespace": "restic"
		}
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
    "total_count": 0,
    "type_meta": null,
    "list_meta": null,
    "list": null
  }
}
```

## /v1/topke/hpa/get
水平弹性伸缩详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
horizontal_pod_autoscaler|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.177/v1/topke/hpa/get
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"horizontal_pod_autoscaler": {
		"metadata": {
			"name": "xxxxxxxxx-deployment",
			"namespace": "restic"
		}
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "HorizontalPodAutoscaler",
        "apiVersion": "autoscaling/v1",
        "metadata": {
          "name": "xxxxxxxxx-deployment",
          "namespace": "restic",
          "selfLink": "/apis/autoscaling/v1/namespaces/restic/horizontalpodautoscalers/xxxxxxxxx-deployment",
          "uid": "76ece3aa-d734-4017-979d-84fe8e09fbf3",
          "resourceVersion": "13014686",
          "creationTimestamp": "2021-08-26T01:29:08Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629941348",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "scaleTargetRef": {
            "kind": "Deployment",
            "name": "xxxxxxxxx",
            "apiVersion": "apps/v1"
          },
          "minReplicas": 1,
          "maxReplicas": 1,
          "targetCPUUtilizationPercentage": 80
        },
        "status": {
          "currentReplicas": 0,
          "desiredReplicas": 0
        }
      }
    ]
  }
}
```

## /v1/topke/storage_class/list
存储类列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
tenant_uuid|string|是|""|租户uuid
fuzzy|string|否|""|模糊匹配
sort_by|string|否|""|排序字段
sort_desc|bool|否|false|是否降序
page_size|int|否|0| 页大小
page_num|int|否|0|页码
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.177/v1/topke/storage_class/list
```
{
	"topke_cluster_uuid": "",
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"fuzzy": "",
	"page_size": 10,
	"page_num": 0,
	"sort_by": "",
	"sort_desc": false
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
    "total_count": 3,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "StorageClass",
        "apiVersion": "storage.k8s.io/v1",
        "metadata": {
          "name": "nfs",
          "selfLink": "/apis/storage.k8s.io/v1/storageclasses/nfs",
          "uid": "67c5a0dd-d4a8-49c6-ad51-ce1a7d9307e3",
          "resourceVersion": "7068491",
          "creationTimestamp": "2021-08-13T06:24:57Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1628835897",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "provisioner": "nfs.topke.io",
        "parameters": {
          "nfs-path": "/exports/521a7445-4147-4fb2-a420-9ee67a1be9c1/data",
          "nfs-server": "10.30.100.22"
        },
        "reclaimPolicy": "Delete",
        "allowVolumeExpansion": true,
        "volumeBindingMode": "Immediate"
      },
      {
        "kind": "StorageClass",
        "apiVersion": "storage.k8s.io/v1",
        "metadata": {
          "name": "clouddisk",
          "selfLink": "/apis/storage.k8s.io/v1/storageclasses/clouddisk",
          "uid": "e04819a0-5c5a-486e-9b8c-c980a8bc6f82",
          "resourceVersion": "7068492",
          "creationTimestamp": "2021-08-05T01:42:43Z",
          "annotations": {
            "storageclass.kubernetes.io/is-default-class": "true",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1628127763",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "provisioner": "topsc.topke.io",
        "parameters": {
          "mount_perm": "0755",
          "topsc-authentication/endpoint": "http://10.30.100.177:9990,http://10.30.100.178:9990,http://10.30.100.179:9990",
          "topsc-authentication/password": "a2a20311145545e816805093629f27c6",
          "topsc-authentication/tenant": "system",
          "topsc-authentication/user": "csi",
          "topsc-volume/cluster": "cluster_name_179",
          "topsc-volume/pool": "csi",
          "topsc-volume/storageType": "topsc-nas",
          "topsc-volume/tenant": "csi",
          "topsc-volume/zone": "default"
        },
        "reclaimPolicy": "Delete",
        "allowVolumeExpansion": true,
        "volumeBindingMode": "Immediate"
      },
      {
        "kind": "StorageClass",
        "apiVersion": "storage.k8s.io/v1",
        "metadata": {
          "name": "local-disks",
          "selfLink": "/apis/storage.k8s.io/v1/storageclasses/local-disks",
          "uid": "747d3a24-0e27-4d3e-92db-c67de8d9eaa8",
          "resourceVersion": "3910258",
          "creationTimestamp": "2021-07-27T03:40:23Z",
          "annotations": {
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"storage.k8s.io/v1\",\"kind\":\"StorageClass\",\"metadata\":{\"annotations\":{\"storageclass.kubernetes.io/is-default-class\":\"true\"},\"name\":\"local-disks\"},\"provisioner\":\"kubernetes.io/no-provisioner\",\"reclaimPolicy\":\"Delete\",\"volumeBindingMode\":\"WaitForFirstConsumer\"}\n",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1627357223",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "provisioner": "kubernetes.io/no-provisioner",
        "reclaimPolicy": "Delete",
        "volumeBindingMode": "WaitForFirstConsumer"
      }
    ],
    "each_range_list_state": [
      {
        "cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
        "cluster_name": "111",
        "result": {
          "code": 0,
          "message": "",
          "messageCn": "",
          "stack": null,
          "desc": "",
          "UUID": "",
          "message_cn": "",
          "data": "",
          "scode": 0
        },
        "total_count": 3
      }
    ]
  }
}
```


## /v1/topke/storage_class/delete
存储类删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
storage_class|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.177/v1/topke/storage_class/delete
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"storage_class": {
		"metadata": {
			"name": "nfs-storageclass"
		}
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
    "total_count": 0,
    "type_meta": null,
    "list_meta": null,
    "list": null
  }
}
```

## /v1/topke/storage_class/create
存储卷创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
storage_class|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.177/v1/topke/storage_class/create
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"storage_class": {
		"kind": "StorageClass",
		"apiVersion": "storage.k8s.io/v1",
		"metadata": {
			"name": "nfs-storageclass",
			"annotations": {
				"topke.desc": ""
			}
		},
		"reclaimPolicy": "Delete",
		"allowVolumeExpansion": true,
		"volumeBindingMode": "Immediate",
		"provisioner": "nfs.topke.io",
		"parameters": {
			"nfs-path": "/nsfdata",
			"nfs-server": "10.30.100.111"
		}
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "StorageClass",
        "apiVersion": "storage.k8s.io/v1",
        "metadata": {
          "name": "nfs-storageclass",
          "selfLink": "/apis/storage.k8s.io/v1/storageclasses/nfs-storageclass",
          "uid": "c6255a6e-99f8-464b-8851-f85382bfaf65",
          "resourceVersion": "13019348",
          "creationTimestamp": "2021-08-26T01:44:51Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629942291",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "provisioner": "nfs.topke.io",
        "parameters": {
          "nfs-path": "/nsfdata",
          "nfs-server": "10.30.100.111"
        },
        "reclaimPolicy": "Delete",
        "allowVolumeExpansion": true,
        "volumeBindingMode": "Immediate"
      }
    ]
  }
}

```

## /v1/topke/storage_class/get
存储卷详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
storage_class|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.177/v1/topke/storage_class/get
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"storage_class": {
		"metadata": {
			"name": "nfs"
		}
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "StorageClass",
        "apiVersion": "storage.k8s.io/v1",
        "metadata": {
          "name": "nfs",
          "selfLink": "/apis/storage.k8s.io/v1/storageclasses/nfs",
          "uid": "67c5a0dd-d4a8-49c6-ad51-ce1a7d9307e3",
          "resourceVersion": "7068491",
          "creationTimestamp": "2021-08-13T06:24:57Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1628835897",
            "topke.desc": "",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "provisioner": "nfs.topke.io",
        "parameters": {
          "nfs-path": "/exports/521a7445-4147-4fb2-a420-9ee67a1be9c1/data",
          "nfs-server": "10.30.100.22"
        },
        "reclaimPolicy": "Delete",
        "allowVolumeExpansion": true,
        "volumeBindingMode": "Immediate"
      }
    ]
  }
}
```


## /v1/topke/storage_class/update
存储卷更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
storage_class|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.177/v1/topke/storage_class/update
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"storage_class": {
		"kind": "StorageClass",
		"apiVersion": "storage.k8s.io/v1",
		"metadata": {
			"name": "nfs",
			"selfLink": "/apis/storage.k8s.io/v1/storageclasses/nfs",
			"uid": "67c5a0dd-d4a8-49c6-ad51-ce1a7d9307e3",
			"resourceVersion": "7068491",
			"creationTimestamp": "2021-08-13T06:24:57Z",
			"annotations": {
				"topke.cluster.name": "111",
				"topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
				"topke.createtime.unix": "1628835897",
				"topke.desc": "sdfsfs",
				"topke.tenant.name": "dev",
				"topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
			}
		},
		"provisioner": "nfs.topke.io",
		"parameters": {
			"nfs-path": "/exports/521a7445-4147-4fb2-a420-9ee67a1be9c1/data",
			"nfs-server": "10.30.100.22"
		},
		"reclaimPolicy": "Delete",
		"allowVolumeExpansion": true,
		"volumeBindingMode": "Immediate"
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "StorageClass",
        "apiVersion": "storage.k8s.io/v1",
        "metadata": {
          "name": "nfs",
          "selfLink": "/apis/storage.k8s.io/v1/storageclasses/nfs",
          "uid": "67c5a0dd-d4a8-49c6-ad51-ce1a7d9307e3",
          "resourceVersion": "13018823",
          "creationTimestamp": "2021-08-13T06:24:57Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1628835897",
            "topke.desc": "sdfsfs",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "provisioner": "nfs.topke.io",
        "parameters": {
          "nfs-path": "/exports/521a7445-4147-4fb2-a420-9ee67a1be9c1/data",
          "nfs-server": "10.30.100.22"
        },
        "reclaimPolicy": "Delete",
        "allowVolumeExpansion": true,
        "volumeBindingMode": "Immediate"
      }
    ]
  }
}
```


## /v1/topke/application/create
自定义应用创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例


#### 正常返回示例

## /v1/topke/application/delete
自定义应用删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例


#### 正常返回示例


## /v1/topke/application/update
自定义应用删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例


#### 正常返回示例


## /v1/topke/application/get
自定义应用删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例


#### 正常返回示例

## /v1/topke/application/list
自定义应用删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
tenant_uuid|string|是|""|租户uuid
fuzzy|string|否|""|模糊匹配
sort_by|string|否|""|排序字段
sort_desc|bool|否|false|是否降序
page_size|int|否|0| 页大小
page_num|int|否|0|页码 

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例


#### 正常返回示例

## /v1/topke/limit_range/create
资源限制范围创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
limit_range|struct|是|{}| k8s资源描述
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/limit_range/create
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"limitrange": {
		"metadata": {
			"name": "limtrange",
			"namespace": "limtrange"
		},
		"spec": {
			"limits": [{
				"default": {},
				"defaultRequest": {},
				"min": {},
				"max": {},
				"type": "Container"
			}, {
				"min": {
					"cpu": "2000m"
				},
				"max": {},
				"type": "Pod"
			}]
		}
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "LimitRange",
        "apiVersion": "v1",
        "metadata": {
          "name": "limtrange",
          "namespace": "limtrange",
          "selfLink": "/api/v1/namespaces/limtrange/limitranges/limtrange",
          "uid": "48a88d09-41be-43aa-8708-35ad738a311c",
          "resourceVersion": "14728293",
          "creationTimestamp": "2021-08-30T01:55:19Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1630288519",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "limits": [
            {
              "type": "Container"
            },
            {
              "type": "Pod",
              "min": {
                "cpu": "2"
              }
            }
          ]
        },
        "convert": {
          "limits": [
            {
              "type": "Container"
            },
            {
              "type": "Pod",
              "min": {
                "cpu": 2000
              }
            }
          ]
        }
      }
    ]
  }
}
```

## /v1/topke/limit_range/delete
资源限制范围删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
limit_range|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例


#### 正常返回示例


## /v1/topke/limit_range/update
资源限制范围更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
limit_range|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/limit_range/update
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"limitrange": {
		"metadata": {
			"name": "limtrange",
			"namespace": "limtrange"
		},
		"spec": {
			"limits": [{
				"default": {},
				"defaultRequest": {},
				"min": {},
				"max": {},
				"type": "Container"
			}, {
				"min": {
					"cpu": "2000m"
				},
				"max": {
					"cpu": "4000m"
				},
				"type": "Pod"
			}]
		}
	}
}
```
#### 正常返回示例

## /v1/topke/limit_range/get
资源限制范围详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
limit_range|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/limit_range/get
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"limitrange": {
		"metadata": {
			"name": "limtrange",
			"namespace": "limtrange"
		}
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "LimitRange",
        "apiVersion": "v1",
        "metadata": {
          "name": "limtrange",
          "namespace": "limtrange",
          "selfLink": "/api/v1/namespaces/limtrange/limitranges/limtrange",
          "uid": "48a88d09-41be-43aa-8708-35ad738a311c",
          "resourceVersion": "14728293",
          "creationTimestamp": "2021-08-30T01:55:19Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1630288519",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "limits": [
            {
              "type": "Container"
            },
            {
              "type": "Pod",
              "min": {
                "cpu": "2"
              }
            }
          ]
        },
        "convert": {
          "limits": [
            {
              "type": "Container"
            },
            {
              "type": "Pod",
              "min": {
                "cpu": 2000
              }
            }
          ]
        }
      }
    ]
  }
}
```

## /v1/topke/limit_range/list 
资源限制范围列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
tenant_uuid|string|是|""|租户uuid
fuzzy|string|否|""|模糊匹配
sort_by|string|否|""|排序字段
sort_desc|bool|否|false|是否降序
page_size|int|否|0| 页大小
page_num|int|否|0|页码

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/limit_range/list
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1"
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
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "LimitRange",
        "apiVersion": "v1",
        "metadata": {
          "name": "limtrange",
          "namespace": "limtrange",
          "selfLink": "/api/v1/namespaces/limtrange/limitranges/limtrange",
          "uid": "48a88d09-41be-43aa-8708-35ad738a311c",
          "resourceVersion": "14728293",
          "creationTimestamp": "2021-08-30T01:55:19Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1630288519",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "limits": [
            {
              "type": "Container"
            },
            {
              "type": "Pod",
              "min": {
                "cpu": "2"
              }
            }
          ]
        },
        "convert": {
          "limits": [
            {
              "type": "Container"
            },
            {
              "type": "Pod",
              "min": {
                "cpu": 2000
              }
            }
          ]
        }
      }
    ]
  }
}
```

## /v1/topke/resource_quota/create 
资源配额创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
resource_qutoa|struct| 是|{}|k8s资源对象

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/resource_quota/create
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"resource_quota": {
		"metadata": {
			"name": "limtrange",
			"namespace": "limtrange"
		},
		"spec": {
			"hard": {
				"requests.cpu": "2000000m",
				"requests.memory": "6000Mi"
			}
		}
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "ResourceQuota",
        "apiVersion": "v1",
        "metadata": {
          "name": "limtrange",
          "namespace": "limtrange",
          "selfLink": "/api/v1/namespaces/limtrange/resourcequotas/limtrange",
          "uid": "83a9f34f-2468-4aa1-92f4-b139cff31bbf",
          "resourceVersion": "14729126",
          "creationTimestamp": "2021-08-30T01:55:19Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1630288519",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "hard": {
            "requests.cpu": "2k",
            "requests.memory": "6000Mi"
          }
        },
        "status": {
          "hard": {
            "requests.cpu": "2"
          },
          "used": {
            "requests.cpu": "0"
          }
        },
        "convert": {
          "spec": {
            "hard": {
              "requests.cpu": 2000000,
              "requests.memory": 6000
            }
          },
          "status": {
            "hard": {
              "requests.cpu": 2000
            },
            "used": {
              "requests.cpu": 0
            }
          }
        }
      }
    ]
  }
}
```



## /v1/topke/resource_quota/delete 
资源配额删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
resource_qutoa|struct| 是|{}|k8s资源对象

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/resource_quota/delete
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"resource_quota": {
		"metadata": {
			"name": "limtrange",
			"namespace": "limtrange"
		
	}
}

 ```

#### 正常返回示例


## /v1/topke/resource_quota/update 
资源配额更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
resource_quota|struct| 是|{}|k8s资源对象
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/resource_quota/update
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"resource_quota": {
		"metadata": {
			"name": "limtrange",
			"namespace": "limtrange"
		},
		"spec": {
			"hard": {
				"requests.cpu": "2000000m",
				"requests.memory": "6000Mi"
			}
		}
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "ResourceQuota",
        "apiVersion": "v1",
        "metadata": {
          "name": "limtrange",
          "namespace": "limtrange",
          "selfLink": "/api/v1/namespaces/limtrange/resourcequotas/limtrange",
          "uid": "83a9f34f-2468-4aa1-92f4-b139cff31bbf",
          "resourceVersion": "14729126",
          "creationTimestamp": "2021-08-30T01:55:19Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1630288519",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "hard": {
            "requests.cpu": "2k",
            "requests.memory": "6000Mi"
          }
        },
        "status": {
          "hard": {
            "requests.cpu": "2"
          },
          "used": {
            "requests.cpu": "0"
          }
        },
        "convert": {
          "spec": {
            "hard": {
              "requests.cpu": 2000000,
              "requests.memory": 6000
            }
          },
          "status": {
            "hard": {
              "requests.cpu": 2000
            },
            "used": {
              "requests.cpu": 0
            }
          }
        }
      }
    ]
  }
}
```

## /v1/topke/resource_quota/get 
资源配额详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
resource_quota|struct| 是|{}|k8s资源对象

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/resource_quota/get
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"resource_quota": {
		"metadata": {
			"name": "limtrange",
			"namespace": "limtrange"
		}
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "ResourceQuota",
        "apiVersion": "v1",
        "metadata": {
          "name": "limtrange",
          "namespace": "limtrange",
          "selfLink": "/api/v1/namespaces/limtrange/resourcequotas/limtrange",
          "uid": "83a9f34f-2468-4aa1-92f4-b139cff31bbf",
          "resourceVersion": "14728294",
          "creationTimestamp": "2021-08-30T01:55:19Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1630288519",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "hard": {
            "requests.cpu": "2"
          }
        },
        "status": {
          "hard": {
            "requests.cpu": "2"
          },
          "used": {
            "requests.cpu": "0"
          }
        },
        "convert": {
          "spec": {
            "hard": {
              "requests.cpu": 2000
            }
          },
          "status": {
            "hard": {
              "requests.cpu": 2000
            },
            "used": {
              "requests.cpu": 0
            }
          }
        }
      }
    ]
  }
}
```

## /v1/topke/resource_quota/list 
资源配额列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
tenant_uuid|string|否|""|租户uuid
fuzzy|string|否|""|模糊匹配
sort_by|string|否|""|排序字段
sort_desc|bool|否|false|是否降序
page_size|int|否|0| 页大小
page_num|int|否|0|页码

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/resource_quota/list
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
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
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "ResourceQuota",
        "apiVersion": "v1",
        "metadata": {
          "name": "limtrange",
          "namespace": "limtrange",
          "selfLink": "/api/v1/namespaces/limtrange/resourcequotas/limtrange",
          "uid": "83a9f34f-2468-4aa1-92f4-b139cff31bbf",
          "resourceVersion": "14728294",
          "creationTimestamp": "2021-08-30T01:55:19Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1630288519",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "hard": {
            "requests.cpu": "2"
          }
        },
        "status": {
          "hard": {
            "requests.cpu": "2"
          },
          "used": {
            "requests.cpu": "0"
          }
        },
        "convert": {
          "spec": {
            "hard": {
              "requests.cpu": 2000
            }
          },
          "status": {
            "hard": {
              "requests.cpu": 2000
            },
            "used": {
              "requests.cpu": 0
            }
          }
        }
      }
    ]
  }
}
```

## /v1/topke/resource_quota/create 
资源配额创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
resource_qutoa|struct| 是|{}|k8s资源对象

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/resource_quota/create
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"resource_quota": {
		"metadata": {
			"name": "limtrange",
			"namespace": "limtrange"
		},
		"spec": {
			"hard": {
				"requests.cpu": "2000000m",
				"requests.memory": "6000Mi"
			}
		}
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "ResourceQuota",
        "apiVersion": "v1",
        "metadata": {
          "name": "limtrange",
          "namespace": "limtrange",
          "selfLink": "/api/v1/namespaces/limtrange/resourcequotas/limtrange",
          "uid": "83a9f34f-2468-4aa1-92f4-b139cff31bbf",
          "resourceVersion": "14728292",
          "creationTimestamp": "2021-08-30T01:55:19Z",
          "annotations": {
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1630288519",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          }
        },
        "spec": {
          "hard": {
            "requests.cpu": "2"
          }
        },
        "status": {},
        "convert": {
          "spec": {
            "hard": {
              "requests.cpu": 2000
            }
          },
          "status": {}
        }
      }
    ]
  }
}
```


## /v1/topke/router/create 
路由创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例


#### 正常返回示例


## /v1/topke/persistent_volume/get 
存储卷详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
persistent_volume|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.177/v1/topke/persistent_volume/get
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"persistent_volume": {
		"metadata": {
			"name": "nfs"
		}
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "PersistentVolume",
        "apiVersion": "v1",
        "metadata": {
          "name": "pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
          "selfLink": "/api/v1/persistentvolumes/pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
          "uid": "0e3ee8f9-86d4-4ae9-a6bd-e523f63217a4",
          "resourceVersion": "13020838",
          "creationTimestamp": "2021-08-25T07:14:41Z",
          "annotations": {
            "pv.kubernetes.io/provisioned-by": "topsc.topke.io",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629875681",
            "topke.desc": "xxx",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          },
          "finalizers": [
            "kubernetes.io/pv-protection"
          ]
        },
        "spec": {
          "capacity": {
            "storage": "6Gi"
          },
          "csi": {
            "driver": "topsc.topke.io",
            "volumeHandle": "pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
            "volumeAttributes": {
              "mount_perm": "0755",
              "storage.kubernetes.io/csiProvisionerIdentity": "1629875465796-8081-topsc.topke.io",
              "topsc-authentication/endpoint": "http://10.30.100.177:9990,http://10.30.100.178:9990,http://10.30.100.179:9990",
              "topsc-authentication/password": "a2a20311145545e816805093629f27c6",
              "topsc-authentication/tenant": "system",
              "topsc-authentication/user": "csi",
              "topsc-volume-attr/DevType": "share",
              "topsc-volume-attr/DriveType": "SSD",
              "topsc-volume-attr/NFSAcl": "*",
              "topsc-volume-attr/NFSArgs": "rw,sync,no_root_squash",
              "topsc-volume-attr/ShareType": "nfs",
              "topsc-volume-attr/Zone": "010efda0-0790-4133-8e34-83ef0edf8210",
              "topsc-volume/cluster": "cluster_name_179",
              "topsc-volume/cluster-uuid": "43f771ba-87b6-4f20-9633-3bc04e0dc379",
              "topsc-volume/name": "pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
              "topsc-volume/pool": "csi",
              "topsc-volume/pool-uuid": "418740aa-7ced-4978-9acf-8f0da866448c",
              "topsc-volume/size": "5368709120",
              "topsc-volume/storageType": "topsc-nas",
              "topsc-volume/tenant": "csi",
              "topsc-volume/tenant-uuid": "196d46ac-bda9-4713-9a4c-8c2af77bb054",
              "topsc-volume/uuid": "5f33d4af-389f-4886-a705-1a4e35791520",
              "topsc-volume/zone": "default",
              "topsc-volume/zone-uuid": "010efda0-0790-4133-8e34-83ef0edf8210"
            }
          },
          "accessModes": [
            "ReadWriteOnce"
          ],
          "claimRef": {
            "kind": "PersistentVolumeClaim",
            "namespace": "default",
            "name": "aaa",
            "uid": "a574e9e8-d845-4d4c-b496-7b387a907f6c",
            "apiVersion": "v1",
            "resourceVersion": "12689420"
          },
          "persistentVolumeReclaimPolicy": "Delete",
          "storageClassName": "clouddisk",
          "volumeMode": "Filesystem"
        },
        "status": {
          "phase": "Bound"
        }
      }
    ]
  }
}
```

## /v1/topke/persistent_volume/list 
存储卷列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
topke_cluster_uuid|string|是|""|容器云集群uuid
tenant_uuid|string|是|""|租户uuid
fuzzy|string|否|""|模糊匹配
sort_by|string|否|""|排序字段
sort_desc|bool|否|false|是否降序
page_size|int|否|0| 页大小
page_num|int|否|0|页码
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.177/v1/topke/persistent_volume/list
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"fuzzy": "",
	"page_size": 10,
	"page_num": 0,
	"sort_by": "",
	"sort_desc": false
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
    "total_count": 3,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "PersistentVolume",
        "apiVersion": "v1",
        "metadata": {
          "name": "pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
          "selfLink": "/api/v1/persistentvolumes/pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
          "uid": "0e3ee8f9-86d4-4ae9-a6bd-e523f63217a4",
          "resourceVersion": "12689492",
          "creationTimestamp": "2021-08-25T07:14:41Z",
          "annotations": {
            "pv.kubernetes.io/provisioned-by": "topsc.topke.io",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629875681",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          },
          "finalizers": [
            "kubernetes.io/pv-protection"
          ]
        },
        "spec": {
          "capacity": {
            "storage": "6Gi"
          },
          "csi": {
            "driver": "topsc.topke.io",
            "volumeHandle": "pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
            "volumeAttributes": {
              "mount_perm": "0755",
              "storage.kubernetes.io/csiProvisionerIdentity": "1629875465796-8081-topsc.topke.io",
              "topsc-authentication/endpoint": "http://10.30.100.177:9990,http://10.30.100.178:9990,http://10.30.100.179:9990",
              "topsc-authentication/password": "a2a20311145545e816805093629f27c6",
              "topsc-authentication/tenant": "system",
              "topsc-authentication/user": "csi",
              "topsc-volume-attr/DevType": "share",
              "topsc-volume-attr/DriveType": "SSD",
              "topsc-volume-attr/NFSAcl": "*",
              "topsc-volume-attr/NFSArgs": "rw,sync,no_root_squash",
              "topsc-volume-attr/ShareType": "nfs",
              "topsc-volume-attr/Zone": "010efda0-0790-4133-8e34-83ef0edf8210",
              "topsc-volume/cluster": "cluster_name_179",
              "topsc-volume/cluster-uuid": "43f771ba-87b6-4f20-9633-3bc04e0dc379",
              "topsc-volume/name": "pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
              "topsc-volume/pool": "csi",
              "topsc-volume/pool-uuid": "418740aa-7ced-4978-9acf-8f0da866448c",
              "topsc-volume/size": "5368709120",
              "topsc-volume/storageType": "topsc-nas",
              "topsc-volume/tenant": "csi",
              "topsc-volume/tenant-uuid": "196d46ac-bda9-4713-9a4c-8c2af77bb054",
              "topsc-volume/uuid": "5f33d4af-389f-4886-a705-1a4e35791520",
              "topsc-volume/zone": "default",
              "topsc-volume/zone-uuid": "010efda0-0790-4133-8e34-83ef0edf8210"
            }
          },
          "accessModes": [
            "ReadWriteOnce"
          ],
          "claimRef": {
            "kind": "PersistentVolumeClaim",
            "namespace": "default",
            "name": "aaa",
            "uid": "a574e9e8-d845-4d4c-b496-7b387a907f6c",
            "apiVersion": "v1",
            "resourceVersion": "12689420"
          },
          "persistentVolumeReclaimPolicy": "Delete",
          "storageClassName": "clouddisk",
          "volumeMode": "Filesystem"
        },
        "status": {
          "phase": "Bound"
        }
      },
      {
        "kind": "PersistentVolume",
        "apiVersion": "v1",
        "metadata": {
          "name": "pvc-066bf26c-dc96-4646-9d7e-8468e5cf1c9c",
          "selfLink": "/api/v1/persistentvolumes/pvc-066bf26c-dc96-4646-9d7e-8468e5cf1c9c",
          "uid": "1f5a5017-c776-42dc-bcd8-ac57816db338",
          "resourceVersion": "9799780",
          "creationTimestamp": "2021-08-19T03:13:51Z",
          "annotations": {
            "pv.kubernetes.io/provisioned-by": "topsc.topke.io",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629342831",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          },
          "finalizers": [
            "kubernetes.io/pv-protection",
            "external-attacher/topsc-topke-io"
          ]
        },
        "spec": {
          "capacity": {
            "storage": "5Gi"
          },
          "csi": {
            "driver": "topsc.topke.io",
            "volumeHandle": "pvc-066bf26c-dc96-4646-9d7e-8468e5cf1c9c",
            "volumeAttributes": {
              "mount_perm": "0755",
              "storage.kubernetes.io/csiProvisionerIdentity": "1628479317905-8081-topsc.topke.io",
              "topsc-authentication/endpoint": "http://10.30.100.177:9990,http://10.30.100.178:9990,http://10.30.100.179:9990",
              "topsc-authentication/password": "a2a20311145545e816805093629f27c6",
              "topsc-authentication/tenant": "system",
              "topsc-authentication/user": "csi",
              "topsc-volume-attr/DevType": "share",
              "topsc-volume-attr/DriveType": "SSD",
              "topsc-volume-attr/NFSAcl": "*",
              "topsc-volume-attr/NFSArgs": "rw,sync,no_root_squash",
              "topsc-volume-attr/ShareType": "nfs",
              "topsc-volume-attr/Zone": "010efda0-0790-4133-8e34-83ef0edf8210",
              "topsc-volume/cluster": "cluster_name_179",
              "topsc-volume/cluster-uuid": "43f771ba-87b6-4f20-9633-3bc04e0dc379",
              "topsc-volume/name": "pvc-066bf26c-dc96-4646-9d7e-8468e5cf1c9c",
              "topsc-volume/pool": "csi",
              "topsc-volume/pool-uuid": "418740aa-7ced-4978-9acf-8f0da866448c",
              "topsc-volume/size": "5368709120",
              "topsc-volume/storageType": "topsc-nas",
              "topsc-volume/tenant": "csi",
              "topsc-volume/tenant-uuid": "196d46ac-bda9-4713-9a4c-8c2af77bb054",
              "topsc-volume/uuid": "5dc53707-22a1-4c3a-93a0-be8797e4f204",
              "topsc-volume/zone": "default",
              "topsc-volume/zone-uuid": "010efda0-0790-4133-8e34-83ef0edf8210"
            }
          },
          "accessModes": [
            "ReadWriteOnce"
          ],
          "claimRef": {
            "kind": "PersistentVolumeClaim",
            "namespace": "restic",
            "name": "csi",
            "uid": "066bf26c-dc96-4646-9d7e-8468e5cf1c9c",
            "apiVersion": "v1",
            "resourceVersion": "9799723"
          },
          "persistentVolumeReclaimPolicy": "Delete",
          "storageClassName": "clouddisk",
          "volumeMode": "Filesystem"
        },
        "status": {
          "phase": "Bound"
        }
      },
      {
        "kind": "PersistentVolume",
        "apiVersion": "v1",
        "metadata": {
          "name": "pvc-52d045d7-7816-4040-82a7-269423fb754c",
          "selfLink": "/api/v1/persistentvolumes/pvc-52d045d7-7816-4040-82a7-269423fb754c",
          "uid": "ef339cc9-ad70-4f63-9340-2e6c0a2dd5f8",
          "resourceVersion": "3921234",
          "creationTimestamp": "2021-08-05T02:15:17Z",
          "annotations": {
            "pv.kubernetes.io/provisioned-by": "topsc.topke.io",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1628129717",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          },
          "finalizers": [
            "kubernetes.io/pv-protection",
            "external-attacher/topsc-topke-io"
          ]
        },
        "spec": {
          "capacity": {
            "storage": "1Gi"
          },
          "csi": {
            "driver": "topsc.topke.io",
            "volumeHandle": "pvc-52d045d7-7816-4040-82a7-269423fb754c",
            "volumeAttributes": {
              "mount_perm": "0755",
              "storage.kubernetes.io/csiProvisionerIdentity": "1627357483581-8081-topsc.topke.io",
              "topsc-authentication/endpoint": "http://10.30.100.177:9990,http://10.30.100.178:9990,http://10.30.100.179:9990",
              "topsc-authentication/password": "a2a20311145545e816805093629f27c6",
              "topsc-authentication/tenant": "system",
              "topsc-authentication/user": "csi",
              "topsc-volume-attr/DevType": "share",
              "topsc-volume-attr/DriveType": "SSD",
              "topsc-volume-attr/NFSAcl": "*",
              "topsc-volume-attr/NFSArgs": "rw,sync,no_root_squash",
              "topsc-volume-attr/ShareType": "nfs",
              "topsc-volume-attr/Zone": "d64d8ec8-eefd-4ba9-b5b2-f04162a7b6bf",
              "topsc-volume/cluster": "cluster_name_179",
              "topsc-volume/cluster-uuid": "8f1b08ac-cb7e-4a5d-8fff-7bd24f8c495f",
              "topsc-volume/name": "pvc-52d045d7-7816-4040-82a7-269423fb754c",
              "topsc-volume/pool": "csi",
              "topsc-volume/pool-uuid": "4ef89cdd-108b-4969-b1d7-2e66eae203b0",
              "topsc-volume/size": "1073741824",
              "topsc-volume/storageType": "topsc-nas",
              "topsc-volume/tenant": "csi",
              "topsc-volume/tenant-uuid": "51a24216-2627-42b6-9140-2c890b82029a",
              "topsc-volume/uuid": "f7d86c13-7f83-478c-8307-a474620f2eda",
              "topsc-volume/zone": "default",
              "topsc-volume/zone-uuid": "d64d8ec8-eefd-4ba9-b5b2-f04162a7b6bf"
            }
          },
          "accessModes": [
            "ReadWriteOnce"
          ],
          "claimRef": {
            "kind": "PersistentVolumeClaim",
            "namespace": "nginx-example",
            "name": "nginx-logs",
            "uid": "52d045d7-7816-4040-82a7-269423fb754c",
            "apiVersion": "v1",
            "resourceVersion": "3921190"
          },
          "persistentVolumeReclaimPolicy": "Delete",
          "storageClassName": "clouddisk",
          "volumeMode": "Filesystem"
        },
        "status": {
          "phase": "Bound"
        }
      }
    ],
    "each_range_list_state": [
      {
        "cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
        "cluster_name": "111",
        "result": {
          "code": 0,
          "message": "",
          "messageCn": "",
          "stack": null,
          "desc": "",
          "UUID": "",
          "message_cn": "",
          "data": "",
          "scode": 0
        },
        "total_count": 3
      }
    ]
  }
}s
```
## /v1/topke/persistent_volume/create 
存储卷创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
persistent_volume|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.177/v1/topke/persistent_volume/create
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"persistent_volume": {
		"kind": "PersistentVolume",
		"apiVersion": "v1",
		"metadata": {
			"name": "pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
			"selfLink": "/api/v1/persistentvolumes/pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
			"uid": "0e3ee8f9-86d4-4ae9-a6bd-e523f63217a4",
			"resourceVersion": "12689492",
			"creationTimestamp": "2021-08-25T07:14:41Z",
			"annotations": {
				"pv.kubernetes.io/provisioned-by": "topsc.topke.io",
				"topke.cluster.name": "111",
				"topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
				"topke.createtime.unix": "1629875681",
				"topke.tenant.name": "dev",
				"topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
				"topke.desc": "xxx"
			},
			"finalizers": ["kubernetes.io/pv-protection"]
		},
		"spec": {
			"capacity": {
				"storage": "6Gi"
			},
			"csi": {
				"driver": "topsc.topke.io",
				"volumeHandle": "pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
				"volumeAttributes": {
					"mount_perm": "0755",
					"storage.kubernetes.io/csiProvisionerIdentity": "1629875465796-8081-topsc.topke.io",
					"topsc-authentication/endpoint": "http://10.30.100.177:9990,http://10.30.100.178:9990,http://10.30.100.179:9990",
					"topsc-authentication/password": "a2a20311145545e816805093629f27c6",
					"topsc-authentication/tenant": "system",
					"topsc-authentication/user": "csi",
					"topsc-volume-attr/DevType": "share",
					"topsc-volume-attr/DriveType": "SSD",
					"topsc-volume-attr/NFSAcl": "*",
					"topsc-volume-attr/NFSArgs": "rw,sync,no_root_squash",
					"topsc-volume-attr/ShareType": "nfs",
					"topsc-volume-attr/Zone": "010efda0-0790-4133-8e34-83ef0edf8210",
					"topsc-volume/cluster": "cluster_name_179",
					"topsc-volume/cluster-uuid": "43f771ba-87b6-4f20-9633-3bc04e0dc379",
					"topsc-volume/name": "pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
					"topsc-volume/pool": "csi",
					"topsc-volume/pool-uuid": "418740aa-7ced-4978-9acf-8f0da866448c",
					"topsc-volume/size": "5368709120",
					"topsc-volume/storageType": "topsc-nas",
					"topsc-volume/tenant": "csi",
					"topsc-volume/tenant-uuid": "196d46ac-bda9-4713-9a4c-8c2af77bb054",
					"topsc-volume/uuid": "5f33d4af-389f-4886-a705-1a4e35791520",
					"topsc-volume/zone": "default",
					"topsc-volume/zone-uuid": "010efda0-0790-4133-8e34-83ef0edf8210"
				}
			},
			"accessModes": ["ReadWriteOnce"],
			"claimRef": {
				"kind": "PersistentVolumeClaim",
				"namespace": "default",
				"name": "aaa",
				"uid": "a574e9e8-d845-4d4c-b496-7b387a907f6c",
				"apiVersion": "v1",
				"resourceVersion": "12689420"
			},
			"persistentVolumeReclaimPolicy": "Delete",
			"storageClassName": "clouddisk",
			"volumeMode": "Filesystem"
		}
	}
}

```

#### 正常返回示例

## /v1/topke/persistent_volume/delete 
存储卷删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
persistent_volume|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.177/v1/topke/persistent_volume/delete
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"persistent_volume": {
		"metadata": {
			"name": "nfs"
		}
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "PersistentVolume",
        "apiVersion": "v1",
        "metadata": {
          "name": "pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
          "selfLink": "/api/v1/persistentvolumes/pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
          "uid": "0e3ee8f9-86d4-4ae9-a6bd-e523f63217a4",
          "resourceVersion": "13020838",
          "creationTimestamp": "2021-08-25T07:14:41Z",
          "annotations": {
            "pv.kubernetes.io/provisioned-by": "topsc.topke.io",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629875681",
            "topke.desc": "xxx",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          },
          "finalizers": [
            "kubernetes.io/pv-protection"
          ]
        },
        "spec": {
          "capacity": {
            "storage": "6Gi"
          },
          "csi": {
            "driver": "topsc.topke.io",
            "volumeHandle": "pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
            "volumeAttributes": {
              "mount_perm": "0755",
              "storage.kubernetes.io/csiProvisionerIdentity": "1629875465796-8081-topsc.topke.io",
              "topsc-authentication/endpoint": "http://10.30.100.177:9990,http://10.30.100.178:9990,http://10.30.100.179:9990",
              "topsc-authentication/password": "a2a20311145545e816805093629f27c6",
              "topsc-authentication/tenant": "system",
              "topsc-authentication/user": "csi",
              "topsc-volume-attr/DevType": "share",
              "topsc-volume-attr/DriveType": "SSD",
              "topsc-volume-attr/NFSAcl": "*",
              "topsc-volume-attr/NFSArgs": "rw,sync,no_root_squash",
              "topsc-volume-attr/ShareType": "nfs",
              "topsc-volume-attr/Zone": "010efda0-0790-4133-8e34-83ef0edf8210",
              "topsc-volume/cluster": "cluster_name_179",
              "topsc-volume/cluster-uuid": "43f771ba-87b6-4f20-9633-3bc04e0dc379",
              "topsc-volume/name": "pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
              "topsc-volume/pool": "csi",
              "topsc-volume/pool-uuid": "418740aa-7ced-4978-9acf-8f0da866448c",
              "topsc-volume/size": "5368709120",
              "topsc-volume/storageType": "topsc-nas",
              "topsc-volume/tenant": "csi",
              "topsc-volume/tenant-uuid": "196d46ac-bda9-4713-9a4c-8c2af77bb054",
              "topsc-volume/uuid": "5f33d4af-389f-4886-a705-1a4e35791520",
              "topsc-volume/zone": "default",
              "topsc-volume/zone-uuid": "010efda0-0790-4133-8e34-83ef0edf8210"
            }
          },
          "accessModes": [
            "ReadWriteOnce"
          ],
          "claimRef": {
            "kind": "PersistentVolumeClaim",
            "namespace": "default",
            "name": "aaa",
            "uid": "a574e9e8-d845-4d4c-b496-7b387a907f6c",
            "apiVersion": "v1",
            "resourceVersion": "12689420"
          },
          "persistentVolumeReclaimPolicy": "Delete",
          "storageClassName": "clouddisk",
          "volumeMode": "Filesystem"
        },
        "status": {
          "phase": "Bound"
        }
      }
    ]
  }
}
```

## /v1/topke/persistent_volume/update 
存储卷更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
persistent_volume|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.177/v1/topke/persistent_volume/update
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"persistent_volume": {
		"kind": "PersistentVolume",
		"apiVersion": "v1",
		"metadata": {
			"name": "pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
			"selfLink": "/api/v1/persistentvolumes/pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
			"uid": "0e3ee8f9-86d4-4ae9-a6bd-e523f63217a4",
			"resourceVersion": "12689492",
			"creationTimestamp": "2021-08-25T07:14:41Z",
			"annotations": {
				"pv.kubernetes.io/provisioned-by": "topsc.topke.io",
				"topke.cluster.name": "111",
				"topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
				"topke.createtime.unix": "1629875681",
				"topke.tenant.name": "dev",
				"topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
				"topke.desc": "xxx"
			},
			"finalizers": ["kubernetes.io/pv-protection"]
		},
		"spec": {
			"capacity": {
				"storage": "6Gi"
			},
			"csi": {
				"driver": "topsc.topke.io",
				"volumeHandle": "pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
				"volumeAttributes": {
					"mount_perm": "0755",
					"storage.kubernetes.io/csiProvisionerIdentity": "1629875465796-8081-topsc.topke.io",
					"topsc-authentication/endpoint": "http://10.30.100.177:9990,http://10.30.100.178:9990,http://10.30.100.179:9990",
					"topsc-authentication/password": "a2a20311145545e816805093629f27c6",
					"topsc-authentication/tenant": "system",
					"topsc-authentication/user": "csi",
					"topsc-volume-attr/DevType": "share",
					"topsc-volume-attr/DriveType": "SSD",
					"topsc-volume-attr/NFSAcl": "*",
					"topsc-volume-attr/NFSArgs": "rw,sync,no_root_squash",
					"topsc-volume-attr/ShareType": "nfs",
					"topsc-volume-attr/Zone": "010efda0-0790-4133-8e34-83ef0edf8210",
					"topsc-volume/cluster": "cluster_name_179",
					"topsc-volume/cluster-uuid": "43f771ba-87b6-4f20-9633-3bc04e0dc379",
					"topsc-volume/name": "pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
					"topsc-volume/pool": "csi",
					"topsc-volume/pool-uuid": "418740aa-7ced-4978-9acf-8f0da866448c",
					"topsc-volume/size": "5368709120",
					"topsc-volume/storageType": "topsc-nas",
					"topsc-volume/tenant": "csi",
					"topsc-volume/tenant-uuid": "196d46ac-bda9-4713-9a4c-8c2af77bb054",
					"topsc-volume/uuid": "5f33d4af-389f-4886-a705-1a4e35791520",
					"topsc-volume/zone": "default",
					"topsc-volume/zone-uuid": "010efda0-0790-4133-8e34-83ef0edf8210"
				}
			},
			"accessModes": ["ReadWriteOnce"],
			"claimRef": {
				"kind": "PersistentVolumeClaim",
				"namespace": "default",
				"name": "aaa",
				"uid": "a574e9e8-d845-4d4c-b496-7b387a907f6c",
				"apiVersion": "v1",
				"resourceVersion": "12689420"
			},
			"persistentVolumeReclaimPolicy": "Delete",
			"storageClassName": "clouddisk",
			"volumeMode": "Filesystem"
		},
		"status": {
			"phase": "Bound"
		}
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
    "total_count": 1,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "PersistentVolume",
        "apiVersion": "v1",
        "metadata": {
          "name": "pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
          "selfLink": "/api/v1/persistentvolumes/pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
          "uid": "0e3ee8f9-86d4-4ae9-a6bd-e523f63217a4",
          "resourceVersion": "13020838",
          "creationTimestamp": "2021-08-25T07:14:41Z",
          "annotations": {
            "pv.kubernetes.io/provisioned-by": "topsc.topke.io",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1629875681",
            "topke.desc": "xxx",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee"
          },
          "finalizers": [
            "kubernetes.io/pv-protection"
          ]
        },
        "spec": {
          "capacity": {
            "storage": "6Gi"
          },
          "csi": {
            "driver": "topsc.topke.io",
            "volumeHandle": "pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
            "volumeAttributes": {
              "mount_perm": "0755",
              "storage.kubernetes.io/csiProvisionerIdentity": "1629875465796-8081-topsc.topke.io",
              "topsc-authentication/endpoint": "http://10.30.100.177:9990,http://10.30.100.178:9990,http://10.30.100.179:9990",
              "topsc-authentication/password": "a2a20311145545e816805093629f27c6",
              "topsc-authentication/tenant": "system",
              "topsc-authentication/user": "csi",
              "topsc-volume-attr/DevType": "share",
              "topsc-volume-attr/DriveType": "SSD",
              "topsc-volume-attr/NFSAcl": "*",
              "topsc-volume-attr/NFSArgs": "rw,sync,no_root_squash",
              "topsc-volume-attr/ShareType": "nfs",
              "topsc-volume-attr/Zone": "010efda0-0790-4133-8e34-83ef0edf8210",
              "topsc-volume/cluster": "cluster_name_179",
              "topsc-volume/cluster-uuid": "43f771ba-87b6-4f20-9633-3bc04e0dc379",
              "topsc-volume/name": "pvc-a574e9e8-d845-4d4c-b496-7b387a907f6c",
              "topsc-volume/pool": "csi",
              "topsc-volume/pool-uuid": "418740aa-7ced-4978-9acf-8f0da866448c",
              "topsc-volume/size": "5368709120",
              "topsc-volume/storageType": "topsc-nas",
              "topsc-volume/tenant": "csi",
              "topsc-volume/tenant-uuid": "196d46ac-bda9-4713-9a4c-8c2af77bb054",
              "topsc-volume/uuid": "5f33d4af-389f-4886-a705-1a4e35791520",
              "topsc-volume/zone": "default",
              "topsc-volume/zone-uuid": "010efda0-0790-4133-8e34-83ef0edf8210"
            }
          },
          "accessModes": [
            "ReadWriteOnce"
          ],
          "claimRef": {
            "kind": "PersistentVolumeClaim",
            "namespace": "default",
            "name": "aaa",
            "uid": "a574e9e8-d845-4d4c-b496-7b387a907f6c",
            "apiVersion": "v1",
            "resourceVersion": "12689420"
          },
          "persistentVolumeReclaimPolicy": "Delete",
          "storageClassName": "clouddisk",
          "volumeMode": "Filesystem"
        },
        "status": {
          "phase": "Bound"
        }
      }
    ]
  }
}

```
## /v1/topke/node/add
添加已存在的节点
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
node|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例


#### 正常返回示例


## /v1/topke/node/label/update
更新节点标签
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例


#### 正常返回示例 

## /v1/topke/node/schedule/update
启动/暂停节点调度
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
node|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例


#### 正常返回示例 

## /v1/topke/node/update
更新节点配置
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
node|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/node/update
```
{
 	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
 	"node": {
 		"metadata": {
 			"name": "xxx-10-30-100-105"
 		}
 	}
}
```

#### 正常返回示例 

## /v1/topke/node/gateway/update
更新网关节点配置
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
persistent_volume|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例


#### 正常返回示例 


## /v1/topke/node/delete
删除节点
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
node|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/node/delete
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"node": {
		"metadata": {
			"name": "xxx-10-30-100-105"
		}
	}
}
```

#### 正常返回示例 


## /v1/topke/node/get
获取节点详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
node|struct|是|{}| k8s资源描述

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/node/get
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"node": {
		"metadata": {
			"name": "xxx-10-30-100-105"
		}
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
    "node_master": 0,
    "node_work": 0,
    "node_gateway": 0,
    "Status": {
      "code": 0,
      "message": "",
      "messageCn": "",
      "stack": null,
      "desc": "",
      "UUID": ""
    },
    "total_count": 0,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "Node",
        "apiVersion": "v1",
        "metadata": {
          "name": "xxx-10-30-100-105",
          "selfLink": "/api/v1/nodes/xxx-10-30-100-105",
          "uid": "dcb281bf-6306-4157-85e5-d9e379c545f7",
          "resourceVersion": "13525301",
          "creationTimestamp": "2021-07-27T03:40:12Z",
          "labels": {
            "beta.kubernetes.io/arch": "amd64",
            "beta.kubernetes.io/os": "linux",
            "kubernetes.io/arch": "amd64",
            "kubernetes.io/hostname": "xxx-10-30-100-105",
            "kubernetes.io/os": "linux",
            "node-role.kubernetes.io/master": ""
          },
          "annotations": {
            "kubeadm.alpha.kubernetes.io/cri-socket": "/var/run/dockershim.sock",
            "node.alpha.kubernetes.io/ttl": "0",
            "projectcalico.org/IPv4Address": "10.30.100.105/24",
            "projectcalico.org/IPv4IPIPTunnelAddr": "192.168.198.192",
            "topke.cluster.name": "111",
            "topke.cluster.uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
            "topke.createtime.unix": "1627357212",
            "topke.tenant.name": "dev",
            "topke.tenant.uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
            "volumes.kubernetes.io/controller-managed-attach-detach": "true"
          }
        },
        "spec": {
          "taints": [
            {
              "key": "node-role.kubernetes.io/master",
              "effect": "NoSchedule"
            }
          ]
        },
        "status": {
          "capacity": {
            "cpu": "4",
            "ephemeral-storage": "102094168Ki",
            "hugepages-2Mi": "0",
            "memory": "4044008Ki",
            "pods": "110"
          },
          "allocatable": {
            "cpu": "4",
            "ephemeral-storage": "94089985074",
            "hugepages-2Mi": "0",
            "memory": "3941608Ki",
            "pods": "110"
          },
          "conditions": [
            {
              "type": "NetworkUnavailable",
              "status": "False",
              "lastHeartbeatTime": "2021-08-25T07:15:08Z",
              "lastTransitionTime": "2021-08-25T07:15:08Z",
              "reason": "CalicoIsUp",
              "message": "Calico is running on this node"
            },
            {
              "type": "MemoryPressure",
              "status": "False",
              "lastHeartbeatTime": "2021-08-27T06:12:35Z",
              "lastTransitionTime": "2021-08-25T07:13:52Z",
              "reason": "KubeletHasSufficientMemory",
              "message": "kubelet has sufficient memory available"
            },
            {
              "type": "DiskPressure",
              "status": "False",
              "lastHeartbeatTime": "2021-08-27T06:12:35Z",
              "lastTransitionTime": "2021-08-25T07:13:52Z",
              "reason": "KubeletHasNoDiskPressure",
              "message": "kubelet has no disk pressure"
            },
            {
              "type": "PIDPressure",
              "status": "False",
              "lastHeartbeatTime": "2021-08-27T06:12:35Z",
              "lastTransitionTime": "2021-08-25T07:13:52Z",
              "reason": "KubeletHasSufficientPID",
              "message": "kubelet has sufficient PID available"
            },
            {
              "type": "Ready",
              "status": "True",
              "lastHeartbeatTime": "2021-08-27T06:12:35Z",
              "lastTransitionTime": "2021-08-25T07:13:52Z",
              "reason": "KubeletReady",
              "message": "kubelet is posting ready status. AppArmor enabled"
            }
          ],
          "addresses": [
            {
              "type": "InternalIP",
              "address": "10.30.100.105"
            },
            {
              "type": "Hostname",
              "address": "xxx-10-30-100-105"
            }
          ],
          "daemonEndpoints": {
            "kubeletEndpoint": {
              "Port": 10250
            }
          },
          "nodeInfo": {
            "machineID": "0a8466e453e2063f7905743b6087b621",
            "systemUUID": "3FEC00C7-081B-409C-A6E9-1380AF360EB6",
            "bootID": "45236a40-08c6-4b3b-acf5-c8aca15dca74",
            "kernelVersion": "4.4.0-142-generic",
            "osImage": "Ubuntu 16.04.6 LTS",
            "containerRuntimeVersion": "docker://20.10.6",
            "kubeletVersion": "v1.18.0",
            "kubeProxyVersion": "v1.18.0",
            "operatingSystem": "linux",
            "architecture": "amd64"
          },
          "images": [
            {
              "names": [
                "10.30.100.155/newk8s/k8s.gcr.io/etcd@sha256:4198ba6f82f642dfd18ecf840ee37afb9df4b596f06eef20e44d0aec4ea27216",
                "10.30.100.155/newk8s/k8s.gcr.io/etcd:3.4.3-0"
              ],
              "sizeBytes": 288426917
            },
            {
              "names": [
                "10.30.100.155/newk8s/docker.io/calico/node@sha256:1a09c7f76600dc9087c251e8cb00c62416fc26babefb8d50888b0f956eb544fd",
                "10.30.100.155/newk8s/docker.io/calico/node:v3.14.1"
              ],
              "sizeBytes": 263082460
            },
            {
              "names": [
                "10.30.100.155/newk8s/docker.io/calico/cni@sha256:b35ff34b3d45999752579fd64afe3d897ff83bea0811edd261e16442e3609b0a",
                "10.30.100.155/newk8s/docker.io/calico/cni:v3.14.1"
              ],
              "sizeBytes": 225067482
            },
            {
              "names": [
                "10.30.100.155/newk8s/k8s.gcr.io/kube-apiserver@sha256:39b3d5a305ec4e340204ecfc81e8cfce87aada5832eb8ee51ef2165b8b31abe3",
                "10.30.100.155/newk8s/k8s.gcr.io/kube-apiserver:v1.18.0"
              ],
              "sizeBytes": 172964371
            },
            {
              "names": [
                "10.30.100.155/newk8s/k8s.gcr.io/kube-controller-manager@sha256:8e9f80f5de8a78e84b0f61325b00628276c56aaee281e5f58c6300ef12dbf3a8",
                "10.30.100.155/newk8s/k8s.gcr.io/kube-controller-manager:v1.18.0"
              ],
              "sizeBytes": 162368019
            },
            {
              "names": [
                "10.30.100.155/newk8s/topke.io/component/registry-distribute-node@sha256:d19bda809f4862f67da3bbf507d14c44f48d91b86750401f347b2be2e07f3647",
                "10.30.100.155/newk8s/topke.io/component/registry-distribute-node:v1.0.0"
              ],
              "sizeBytes": 125775162
            },
            {
              "names": [
                "10.30.100.155/newk8s/k8s.gcr.io/kube-proxy@sha256:b832454a96a848ad5c51ad8a499ef2173b627ded2c225e3a6be5aad9446cb211",
                "10.30.100.155/newk8s/k8s.gcr.io/kube-proxy:v1.18.0"
              ],
              "sizeBytes": 116534263
            },
            {
              "names": [
                "10.30.100.155/newk8s/docker.io/calico/pod2daemon-flexvol@sha256:9011620daeffc4824bfab956de181f677db597a7e86cfebb7bafd581bdaf844d",
                "10.30.100.155/newk8s/docker.io/calico/pod2daemon-flexvol:v3.14.1"
              ],
              "sizeBytes": 112413732
            },
            {
              "names": [
                "10.30.100.155/newk8s/k8s.gcr.io/kube-scheduler@sha256:7c242783ca2bbd9f85fbef785ed7c492d4aaa96e3808740a6fb9fb14babfa700",
                "10.30.100.155/newk8s/k8s.gcr.io/kube-scheduler:v1.18.0"
              ],
              "sizeBytes": 95275539
            },
            {
              "names": [
                "10.30.100.155/newk8s/docker.io/haproxy/haproxy@sha256:6e4ce09a67fce7634fa85a80df92398c14ed24d68412bd2d354a5969808da516",
                "10.30.100.155/newk8s/docker.io/haproxy/haproxy:2.1.4"
              ],
              "sizeBytes": 92386980
            },
            {
              "names": [
                "10.30.100.155/newk8s/docker.io/osixia/keepalived@sha256:de9cdb72abdfe24df0b8b50422c94dc57087c843660c558bbe7adea9b9c5d73d",
                "10.30.100.155/newk8s/docker.io/osixia/keepalived:1.3.5-1"
              ],
              "sizeBytes": 53407074
            },
            {
              "names": [
                "10.30.100.155/newk8s/docker.io/calico/kube-controllers@sha256:050abffec836225ca49417e974a9f5fb8b4860755c7ab9dae9d3f1d0246b7897",
                "10.30.100.155/newk8s/docker.io/calico/kube-controllers:v3.14.1"
              ],
              "sizeBytes": 52823823
            },
            {
              "names": [
                "10.30.100.155/newk8s/k8s.gcr.io/coredns@sha256:695a5e109604331f843d2c435f488bf3f239a88aec49112d452c1cbf87e88405",
                "10.30.100.155/newk8s/k8s.gcr.io/coredns:1.6.7"
              ],
              "sizeBytes": 43794147
            },
            {
              "names": [
                "10.30.100.155/newk8s/quay.io/coreos/kube-rbac-proxy@sha256:6c915d948d4781d366300d6e75d67a7830a941f078319f0fecc21c7744053eff",
                "10.30.100.155/newk8s/quay.io/coreos/kube-rbac-proxy:v0.4.1"
              ],
              "sizeBytes": 41317870
            },
            {
              "names": [
                "10.30.100.155/newk8s/quay.io/prometheus/node-exporter@sha256:b630fb29d99b3483c73a2a7db5fc01a967392a3d7ad754c8eccf9f4a67e7ee31",
                "10.30.100.155/newk8s/quay.io/prometheus/node-exporter:v0.18.1"
              ],
              "sizeBytes": 22933477
            },
            {
              "names": [
                "10.30.100.155/newk8s/k8s.gcr.io/pause@sha256:4a1c4b21597c1b4415bdbecb28a3296c6b5e23ca4f9feeb599860a1dac6a0108",
                "10.30.100.155/newk8s/k8s.gcr.io/pause:3.2"
              ],
              "sizeBytes": 682696
            }
          ]
        }
      }
    ]
  }
}
```
## /v1/topke/node/list
获取节点列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|容器云集群uuid
topke_cluster_uuid|string|是|""|容器云集群uuid
tenant_uuid|string|是|""|租户uuid
fuzzy|string|否|""|模糊匹配
sort_by|string|否|""|排序字段
sort_desc|bool|否|false|是否降序
page_size|int|否|0| 页大小
page_num|int|否|0|页码
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
 https://10.30.100.178/v1/topke/node/list
```
{
	"topke_cluster_uuid": "d5c5cfd6-0a1e-4666-bd44-0aa0072e8ce1",
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"fuzzy": "",
	"show_resource_usage": true,
	"page_size": 10,
	"page_num": 0,
	"sort_by": "",
	"sort_desc": false
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
    "node_master": 3,
    "node_work": 1,
    "node_gateway": 0,
    "Status": {
      "code": 0,
      "message": "",
      "messageCn": "",
      "stack": null,
      "desc": "",
      "UUID": ""
    },
    "total_count": 4,
    "type_meta": null,
    "list_meta": null,
    "list": [
      {
        "kind": "Node",
        "apiVersion": "v1",
        "metadata": {
          "name": "xxx-10-30-100-220",
          "selfLink": "/api/v1/nodes/xxx-10-30-100-220",
          "uid": "a4465f54-3cd3-4ae7-83eb-0c38e363ded7",
          "resourceVersion": "12233357",
          "creationTimestamp": "2021-07-27T03:42:30Z",
          "labels": {
            "aaa": "",
            "beta.kubernetes.io/arch": "amd64",
            "beta.kubernetes.io/os": "linux",
            "kubernetes.io/arch": "amd64",
            "kubernetes.io/hostname": "xxx-10-30-100-220",
            "kubernetes.io/os": "linux"
          },
  ...

```