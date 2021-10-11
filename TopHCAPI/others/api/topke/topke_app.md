[back to api overview](../api_overview.md#topke_app)

### 容器云集群应用接口
## /v1/topke/app_template/create
创建应用模板
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群uuid
workspace|string|是|""|工作区
type|string|是|""|类型
package_data|string|是|""|模板包数据  
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/parse
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"workspace": "aaa",
	"type": "helm",
	"package_data": "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",
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "data": {
      "tenant": "",
      "workspace": "aaa",
      "name": "myapp",
      "uuid": "d9d10646-aac8-4ea0-9922-b08775fe934c",
      "type": "helm",
      "create_time": 1629859584,
      "creator": "",
      "description": "A Helm chart for Kubernetes",
      "status": "developing",
      "status_time": 1629859584,
      "update_time": 1629859584,
      "icon": "",
      "keywords": null,
      "home": "",
      "tags": "",
      "category_set": null,
      "latest_version": {
        "tenant": "",
        "workspace": "aaa",
        "type": "",
        "uuid": "1e82da37-874d-4dd5-9617-30c9bad1d5fd",
        "name": "0.1.0 [1.16.0]",
        "template_uuid": "d9d10646-aac8-4ea0-9922-b08775fe934c",
        "create_time": 1629859584,
        "update_time": 1629859584,
        "description": "A Helm chart for Kubernetes",
        "state_operator": "",
        "status": "developing",
        "status_time": 1629859584,
        "package_name": "myapp",
        "package_version": "0.1.0"
      },
      "version_num": 1,
      "instance_num": 0
    }
  }
}
```

## /v1/topke/app_template/delete
删除应用模板
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群uuid
workspace|string|是|""|工作区uuid
uuid|string|是|""| 模板UUID
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/delete
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"workspace": "aaa",
	"uuid": "2ffa7014-fa2e-464a-90ac-a969d3074b66"
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "data": null
  }
}
```

## /v1/topke/app_template/get
应用模板详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群uuid
workspace|string|是|""|工作区uuid
uuid|string|是|""| 模板UUID
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/get
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"workspace": "aaa",
	"uuid": "2ffa7014-fa2e-464a-90ac-a969d3074b66"
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "data": {
      "tenant": "",
      "workspace": "aaa",
      "name": "myapp",
      "uuid": "d9d10646-aac8-4ea0-9922-b08775fe934c",
      "type": "helm",
      "create_time": 1629859584,
      "creator": "",
      "description": "A Helm chart for Kubernetes",
      "status": "developing",
      "status_time": 1629859584,
      "update_time": 1629859584,
      "icon": "",
      "keywords": null,
      "home": "",
      "tags": "",
      "category_set": null,
      "latest_version": {
        "tenant": "",
        "workspace": "aaa",
        "type": "",
        "uuid": "1e82da37-874d-4dd5-9617-30c9bad1d5fd",
        "name": "0.1.0 [1.16.0]",
        "template_uuid": "d9d10646-aac8-4ea0-9922-b08775fe934c",
        "create_time": 1629859584,
        "update_time": 1629860729,
        "description": "A Helm chart for Kubernetes",
        "state_operator": "",
        "status": "rejected",
        "status_time": 1629860729,
        "package_name": "myapp",
        "package_version": "0.1.0"
      },
      "version_num": 1,
      "instance_num": 0
    }
  }
}
```

## /v1/topke/app_template/list
应用模板列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群UUID
page_size|int|否|0|分页页大小
page_num|int|否|0|分页也数
fuzzy|string|否|""|模糊搜索
category|string|否|""|分类过滤
workspace|string|否|""|工作区过滤
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/list
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"page_size": 10,
	"page_num": 0,
	"fuzzy": "",
	"type": "helm",
	"category": "",
	"workspace": "aaa"
}
```

#### 正常返回示例

## /v1/topke/app_template/parse
应用模板包解析
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群uuid
workspace|string|是|""|工作区
type|string|是|""|类型
package_data|string|是|""|模板包数据，base64加密
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/parse
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"workspace": "aaa",
	"type": "helm",
	"package_data": "H4sIFAAAAAAA/ykAK2FIUjBjSE02THk5NWIzVjBkUzVpWlM5Nk9WVjZNV2xqYW5keVRRbz1IZWxtAOw8/W/buJL9WX/FnJuHflwty4mbFAJ6QC7t7QtemxpJtw+LxaKgpbHNDUVqScqJ18397QeS+rYcp9s06R7CHxJbGg5nhpwPzkySLEmaDo7mRGp/SRL26DuMIAiC/dHI/g6CoP07GB4Ej4Z7By9f7gZ7o+Huo2C4uzc8eATB9yCmPTKliXwUfPNabeb+JoOk9BNKRQUPYbHrkTQtvw794b4feDGqSNJU22eH8E9kCUTmvMBUSPhXNkHJUaPyOEkwBHugPL1MMQSSpoxGxEz1FgXawB/6gXfffD8MN5z+LwjLUH0vA7BF//dGwX5b/1/u7z7o/12Mx/AGpyRjGtwZsEptD4XvPYaPc6qAKiDwy+H7d/2pkAnRGmOYUoYG4A1GjEiEBZGUTBgq0AImCClRCmOgXAtYikyCxiRlRKPyPU+iNQtHIuM6hKHn0YTMMPQAJKZCUS3kMgQ+o/zSA0gzxsaC0WgZwvH0ROixRIVcewCP4cMCpaSxWXeOYPGAJjO4mAuFEOesUffaWa3KxPkeGOAQer2chnHG2BlGErUK4dffrEkrlrBg04yxtYeeQrmgER5GkWXJUnaWYkSnFBVczFHPUQKBHA6IAwQ1FxmLjbwiiURj7EH+KQQtM7SIDjkX2tpQK1wSx+aX4aeFzgMgFWwIqys7/+McwZAMYto1yyDLFPoW9ngKXGhQqIHwOKfFik9m+AKIQ0QVzJCjNBRDpiifWcSFbMq99gCcTzAySkV82KLOPDvDKJNUL48E13ipS6qn6icpsjSE3SAIjIS7wSKSkgllVFNUTu4AsRRp8bkPh+/e2c8SSfyBs+WpEPp/KEO1VBqTmpxlxg/VieAGoP34Z4UyhGFOipWfWcF5uSOWKY3yeGwOq5A6hFeB51E+k6gsUciNasQhTAlT2LlNZqXz0pX6VAzy+X7EiFKVNqwDaqb6JLJiNkT3PIC5UNqubARgvoTu7PfxkiQpQ5+JiDD7HiAleu5OO4BmxafHZqqyqnBi97CBoK+ZyiVcLfbY4et3ruVJVCKTEVYH898ImcoIY0uQGIkkQR7b46cFKKs9y1KDy9n2XGoBDMkCQRv7RIx9igRXERWZIyuaC3PEjS0zJzNTKH1nzAhTAig3J1uhMqTyyP2WWpnNBsEB+YJKwRPkWsEF1XNgVGuWH4iClBegsmhuln9POTWb4hsFWooMYgEXhDc4qU3LuONWO7URjIkLymcWO6PcgJD490zZ94lZgGOEShG5fGH5l5gIyz1ClEm2hIkkVjZTjRKeVKJ+4udIE1rtUZRm9iwn+fcEE2twh7uv3tOcxT8yVDed4ZFMCxURRvms87gnlJ86k6+MuQdIyGXtQRBYOyxnqI/GP/+sKaN/WuUYo4yQa+MbjEqZtR3Ye7v+ZkiPixjPkGGkhXSmRgtmDJZTuV9/8zwynVJO9dK+vm8vfH/DxX+ldx6cfPj49szXl/oW19gW/+0FB634bxTs7j/Ef3cxhj78hM4Q1W5r8PPpO5gsjT3kuXtXCMZqER6r0Fut+kCn4H9y94bCV+WaD1dXFkISPkPYMQ4Cwtdr0NZxGFiACtq37sg9nWudrlZmoZ32XM0MjFqtwDiNq6twMFit3FIWL1xdrVbgV9gdmNf+yBQa/JHgmlCuoHciYhwLqXslubm/942zd/jw0rh5OPnw5u3n8YfTj693nhrrH2kGM9TQ75uoR6UkQjBEnCIzzsY/KZ9eXUFfwO9KcMPt697KN17CN1jVr8FvPs+JuOoV0ZoymCiPWBYj9Fx8XsRbPcvnsxZhx+MWWQap+kvEUY2JpUtpojPlkzg2m4D2Wf7lqmcJiObCbls4GOzkZIQ7paA2yPydIPF/E2Y8sbxO7gBgzFMIxxoSsgRNzhEITPHCuJhM57cXc5brKOF4nN9KyIJQZo6on8c+dvwiMogIhwuio7kLkS2fJmCu6cCTr95jtYigf7F1555UO3f29vTT8VHH5llUN1lz22LQ7xfGHnqrVW+1yhXvKeUxXkKxx6wmwELrIHhm9cq3yuXUqHfVsfMVG6EhtLWhltONClhG0zfQwPGHN59PDt+/bQkrFfFNDzqDnpFRM6I2E1+vC7IS4ov1OZQrbYT1ur2WkdFGhUpQk5hoYnHngnSsHX04+Xh4fPL2tMvCpCK+GX87hYQ67U0udJSWltL6lI+dCSp3t/eJKqqLTR7uHviBH/jD8FXwKshvke6uX3Mk5jZSUH4jig0V/amQF0TGNfLNGuFOUyh1Y37fbvRvO9rx3+c5shSl8nV6a6nArfHfaLcd/x0MH+K/Oxmr1eC59/YytdfqVqbIXop97/kgN9YxTilvmcN+9c5e1H1XSrKWr7Df9YQZfAEtMx7B/p79SJOzbDqll9Dr91oBmmdpO3I5KFKuYPzZEv7ICKNTirGxNpZq3/s3OtwWXpsVDAcKJhgRY5yUSLBWsHC8TimyWAGR6K7JmKfXqIKnk6WVw5uTMwNrggBjN5/53vEUpLNeDknpvlyK0WXJNFxQxkzckSlDpzKxSsZYTu0GsVbuuhBtLdBupx8LiW18fxNpGxecf96xlIevb76dFY2lDBySthN0dDYefiVxqaRcT6H3D9X/h+q1cLlFb364uj82jlxtL4125AUss492P/PD4aAYmSDbuKcWptrQNiN1GbvPeYIavoDElBnX2PvPHvQ+975efUSSCO7oU5voc28dgXNkia/mA0tz2BFP5sz4brn2W5VnXd7lKP3aCcmZOywT8ObdeihVVgpNkLA25Qv8kQmNLWbXsSSEkxnG/ckybEQbZ3n6u0tYRcpoi7jaPPY7CXCp7+vCyI5JRRgZrkVI153UtuHuTvFvZqdevTjZZHuaYH5eG2iZ/6ebLx/PNmHide5q+l7g7OUf1i4EnQjWdPq+PeyPPdrxX4wpE8sE+S22g2yt/67Ffy9Ho+FD/HcXo97/QdJUDRZD75zyOIQ35UnwimtqWFb0tqUZPMhtqKtCWVPShGelg/gCnPIYuYaRmWlCrDDP2lFXjyz0vlZoqOcabd04rybU8g31MvNaIhCgsOKOwoToaP6uRnIn0everSJ+36EtVClHW5NcgdMWlAoim2XRMs/VKBGWySozW4tfSMIaK7+qpjU4NIM1WPpqpkrUxa50MtGunVfLr1XVv4WXdUfVdRC73JlfR9KsJHcSVG1Oqz7dTWmVSKnQ9StNqQd45ZxradlAj9pIzHC3idl1VECvpg72kV91WMDVVbj2WpMZfGlH/42ArddeZVzrz1jDVzVvNOmzyaYmv4XA5lqnjRc1+Y6L8nrzfSqFFpFgIXw8GtfeMbpAjkqNpZhgczWzyk/YErkrhocwaD+1y7YIk0hi+h2xFzXcbYeiKo13H4c1ba0XRyuwRsn0W7R0bb2i0lozbkXt9VbXqZV4K6h63fevrXbfHvr7jnb8N0/JrbcBbon/hvvDdv/fKNh76P+7k9G65G2IsBpRYgUyWOxOUJMiYvynkPRPY6rZWMSHORjK+wkf7dofbbvIKU4dnq5g1zxfC3itQbwppY32lpoHrMuyBpNPqrfAbJpUweSTUEsa1YXSvXPXN9MUVq6f96+d5g7Ea3qeylw6SURpVj5xCxwuUJIZ1hbZyMrNKGrZ+K0cXtMH9BeZdJ1N38rnDej6UXIVbftfNFjcpg/YYv93g73233+MDnb3Huz/XYwtnTxFHnDHWL2TvDhwjUEs4dUiMsF6ve+nUf+vJRgVJguURyJJiUTo/dfroT8c9YMe+Ee17l7/X9kEi8btn6gubiT9lnviqC+EPDfKeP7K5ZOHzkmV+cX2FLzUyM1H1YR1Oumcw7ETTLcvq6TzTa6r62ad7wdp5wjW8gMbYtrRWuajlV/p7qzKe4FLzHlz1ibYos+4FWPns2qNXm70rfmsp/Lrs1p3/qoF2Uyqvnc6jcYXmTHcykODuKJb2qxk28jWSLTdDyW5rnfaa97P1hvZKr7dDbBqTavGhETnyOP2lTFXmpMNR60D1N2RDWihgw3IDh/bJb37tksP425G2/8XRvoO/X/wcrS37v+DB/9/F6Px95/FRS6vkd7Pxc3F6x19g1X7Xy172M/TZ9f0GdZD+XE719aVOmzkIZtlgq9Mn49+eFO6Qf/zyvHtmIFt+j86GLX0f38veND/Oxk3KvK3A+a2ocjBb2QvrinP3GLc3OLjFsPn/2cxUlv/NSrtfvYjwTlGRkbfaAa2+v/9ly39P3g5esj/3snoVOuxiDt0ubfN+fdbx6b3TTq9pqK9ojVtLsR5LwSzWhk1tEuwRTXxYoa6XosOYZKp5URclqVb+zdNIfz6xIA++a0oUcmZMg+38XzNHzhYXBLN+dJFgfQEFyh/JMPh9N83oqUzLiR+hzW26v9eW/93X+499P/cyXgMY6I1SvfPBdwRgIs5cphklMWUzyAl0TmZoSr/IYTKUhuBg5ojYzBjYuL6ZyifvQCJjGi6QJvrqD0nPPYeA8eZ+wvDp6nEKb3E2Dnu/3jmwwfOliC4nWlIghSl/YNo3/PfnH0+00Ki9xjyltZPR2cQU6k8f0b1wP505Hv+5E85sD+LB/PZwPwovqoFH1SIJiQ6z1L7Ly2U99xXF6n33J+Qc++5rxPzWUg6857/r/cYPhFJRabg+M1b5fmpFL9jpD2fxkgGDlyK3z1/oSIR4+BH0vOH8TAexsNoj/8LAAD//9vzhBMATgAA",
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "files": [
      {
        "Name": "Chart.yaml",
        "Data": "YXBpVmVyc2lvbjogdjIKYXBwVmVyc2lvbjogMS4xNi4wCmRlc2NyaXB0aW9uOiBBIEhlbG0gY2hhcnQgZm9yIEt1YmVybmV0ZXMKbmFtZTogbXlhcHAKdHlwZTogYXBwbGljYXRpb24KdmVyc2lvbjogMC4xLjAK"
      },
      {
        "Name": "values.yaml",
        "Data": "IyBEZWZhdWx0IHZhbHVlcyBmb3IgbXlhcHAuCiMgVGhpcyBpcyBhIFlBTUwtZm9ybWF0dGVkIGZpbGUuCiMgRGVjbGFyZSB2YXJpYWJsZXMgdG8gYmUgcGFzc2VkIGludG8geW91ciB0ZW1wbGF0ZXMuCgpyZXBsaWNhQ291bnQ6IDEKCmltYWdlOgogIHJlcG9zaXRvcnk6IG5naW54CiAgcHVsbFBvbGljeTogSWZOb3RQcmVzZW50CiAgIyBPdmVycmlkZXMgdGhlIGltYWdlIHRhZyB3aG9zZSBkZWZhdWx0IGlzIHRoZSBjaGFydCBhcHBWZXJzaW9uLgogIHRhZzogIiIKCmltYWdlUHVsbFNlY3JldHM6IFtdCm5hbWVPdmVycmlkZTogIiIKZnVsbG5hbWVPdmVycmlkZTogIiIKCnNlcnZpY2VBY2NvdW50OgogICMgU3BlY2lmaWVzIHdoZXRoZXIgYSBzZXJ2aWNlIGFjY291bnQgc2hvdWxkIGJlIGNyZWF0ZWQKICBjcmVhdGU6IHRydWUKICAjIEFubm90YXRpb25zIHRvIGFkZCB0byB0aGUgc2VydmljZSBhY2NvdW50CiAgYW5ub3RhdGlvbnM6IHt9CiAgIyBUaGUgbmFtZSBvZiB0aGUgc2VydmljZSBhY2NvdW50IHRvIHVzZS4KICAjIElmIG5vdCBzZXQgYW5kIGNyZWF0ZSBpcyB0cnVlLCBhIG5hbWUgaXMgZ2VuZXJhdGVkIHVzaW5nIHRoZSBmdWxsbmFtZSB0ZW1wbGF0ZQogIG5hbWU6ICIiCgpwb2RBbm5vdGF0aW9uczoge30KCnBvZFNlY3VyaXR5Q29udGV4dDoge30KICAjIGZzR3JvdXA6IDIwMDAKCnNlY3VyaXR5Q29udGV4dDoge30KICAjIGNhcGFiaWxpdGllczoKICAjICAgZHJvcDoKICAjICAgLSBBTEwKICAjIHJlYWRPbmx5Um9vdEZpbGVzeXN0ZW06IHRydWUKICAjIHJ1bkFzTm9uUm9vdDogdHJ1ZQogICMgcnVuQXNVc2VyOiAxMDAwCgpzZXJ2aWNlOgogIHR5cGU6IENsdXN0ZXJJUAogIHBvcnQ6IDgwCgppbmdyZXNzOgogIGVuYWJsZWQ6IGZhbHNlCiAgYW5ub3RhdGlvbnM6IHt9CiAgICAjIGt1YmVybmV0ZXMuaW8vaW5ncmVzcy5jbGFzczogbmdpbngKICAgICMga3ViZXJuZXRlcy5pby90bHMtYWNtZTogInRydWUiCiAgaG9zdHM6CiAgICAtIGhvc3Q6IGNoYXJ0LWV4YW1wbGUubG9jYWwKICAgICAgcGF0aHM6IFtdCiAgdGxzOiBbXQogICMgIC0gc2VjcmV0TmFtZTogY2hhcnQtZXhhbXBsZS10bHMKICAjICAgIGhvc3RzOgogICMgICAgICAtIGNoYXJ0LWV4YW1wbGUubG9jYWwKCnJlc291cmNlczoge30KICAjIFdlIHVzdWFsbHkgcmVjb21tZW5kIG5vdCB0byBzcGVjaWZ5IGRlZmF1bHQgcmVzb3VyY2VzIGFuZCB0byBsZWF2ZSB0aGlzIGFzIGEgY29uc2Npb3VzCiAgIyBjaG9pY2UgZm9yIHRoZSB1c2VyLiBUaGlzIGFsc28gaW5jcmVhc2VzIGNoYW5jZXMgY2hhcnRzIHJ1biBvbiBlbnZpcm9ubWVudHMgd2l0aCBsaXR0bGUKICAjIHJlc291cmNlcywgc3VjaCBhcyBNaW5pa3ViZS4gSWYgeW91IGRvIHdhbnQgdG8gc3BlY2lmeSByZXNvdXJjZXMsIHVuY29tbWVudCB0aGUgZm9sbG93aW5nCiAgIyBsaW5lcywgYWRqdXN0IHRoZW0gYXMgbmVjZXNzYXJ5LCBhbmQgcmVtb3ZlIHRoZSBjdXJseSBicmFjZXMgYWZ0ZXIgJ3Jlc291cmNlczonLgogICMgbGltaXRzOgogICMgICBjcHU6IDEwMG0KICAjICAgbWVtb3J5OiAxMjhNaQogICMgcmVxdWVzdHM6CiAgIyAgIGNwdTogMTAwbQogICMgICBtZW1vcnk6IDEyOE1pCgphdXRvc2NhbGluZzoKICBlbmFibGVkOiBmYWxzZQogIG1pblJlcGxpY2FzOiAxCiAgbWF4UmVwbGljYXM6IDEwMAogIHRhcmdldENQVVV0aWxpemF0aW9uUGVyY2VudGFnZTogODAKICAjIHRhcmdldE1lbW9yeVV0aWxpemF0aW9uUGVyY2VudGFnZTogODAKCm5vZGVTZWxlY3Rvcjoge30KCnRvbGVyYXRpb25zOiBbXQoKYWZmaW5pdHk6IHt9Cg=="
      },
      {
        "Name": "templates/NOTES.txt",
        "Data": "MS4gR2V0IHRoZSBhcHBsaWNhdGlvbiBVUkwgYnkgcnVubmluZyB0aGVzZSBjb21tYW5kczoKe3stIGlmIC5WYWx1ZXMuaW5ncmVzcy5lbmFibGVkIH19Cnt7LSByYW5nZSAkaG9zdCA6PSAuVmFsdWVzLmluZ3Jlc3MuaG9zdHMgfX0KICB7ey0gcmFuZ2UgLnBhdGhzIH19CiAgaHR0cHt7IGlmICQuVmFsdWVzLmluZ3Jlc3MudGxzIH19c3t7IGVuZCB9fTovL3t7ICRob3N0Lmhvc3QgfX17eyAuIH19CiAge3stIGVuZCB9fQp7ey0gZW5kIH19Cnt7LSBlbHNlIGlmIGNvbnRhaW5zICJOb2RlUG9ydCIgLlZhbHVlcy5zZXJ2aWNlLnR5cGUgfX0KICBleHBvcnQgTk9ERV9QT1JUPSQoa3ViZWN0bCBnZXQgLS1uYW1lc3BhY2Uge3sgLlJlbGVhc2UuTmFtZXNwYWNlIH19IC1vIGpzb25wYXRoPSJ7LnNwZWMucG9ydHNbMF0ubm9kZVBvcnR9IiBzZXJ2aWNlcyB7eyBpbmNsdWRlICJteWFwcC5mdWxsbmFtZSIgLiB9fSkKICBleHBvcnQgTk9ERV9JUD0kKGt1YmVjdGwgZ2V0IG5vZGVzIC0tbmFtZXNwYWNlIHt7IC5SZWxlYXNlLk5hbWVzcGFjZSB9fSAtbyBqc29ucGF0aD0iey5pdGVtc1swXS5zdGF0dXMuYWRkcmVzc2VzWzBdLmFkZHJlc3N9IikKICBlY2hvIGh0dHA6Ly8kTk9ERV9JUDokTk9ERV9QT1JUCnt7LSBlbHNlIGlmIGNvbnRhaW5zICJMb2FkQmFsYW5jZXIiIC5WYWx1ZXMuc2VydmljZS50eXBlIH19CiAgICAgTk9URTogSXQgbWF5IHRha2UgYSBmZXcgbWludXRlcyBmb3IgdGhlIExvYWRCYWxhbmNlciBJUCB0byBiZSBhdmFpbGFibGUuCiAgICAgICAgICAgWW91IGNhbiB3YXRjaCB0aGUgc3RhdHVzIG9mIGJ5IHJ1bm5pbmcgJ2t1YmVjdGwgZ2V0IC0tbmFtZXNwYWNlIHt7IC5SZWxlYXNlLk5hbWVzcGFjZSB9fSBzdmMgLXcge3sgaW5jbHVkZSAibXlhcHAuZnVsbG5hbWUiIC4gfX0nCiAgZXhwb3J0IFNFUlZJQ0VfSVA9JChrdWJlY3RsIGdldCBzdmMgLS1uYW1lc3BhY2Uge3sgLlJlbGVhc2UuTmFtZXNwYWNlIH19IHt7IGluY2x1ZGUgIm15YXBwLmZ1bGxuYW1lIiAuIH19IC0tdGVtcGxhdGUgInt7Int7IHJhbmdlIChpbmRleCAuc3RhdHVzLmxvYWRCYWxhbmNlci5pbmdyZXNzIDApIH19e3sufX17eyBlbmQgfX0ifX0iKQogIGVjaG8gaHR0cDovLyRTRVJWSUNFX0lQOnt7IC5WYWx1ZXMuc2VydmljZS5wb3J0IH19Cnt7LSBlbHNlIGlmIGNvbnRhaW5zICJDbHVzdGVySVAiIC5WYWx1ZXMuc2VydmljZS50eXBlIH19CiAgZXhwb3J0IFBPRF9OQU1FPSQoa3ViZWN0bCBnZXQgcG9kcyAtLW5hbWVzcGFjZSB7eyAuUmVsZWFzZS5OYW1lc3BhY2UgfX0gLWwgImFwcC5rdWJlcm5ldGVzLmlvL25hbWU9e3sgaW5jbHVkZSAibXlhcHAubmFtZSIgLiB9fSxhcHAua3ViZXJuZXRlcy5pby9pbnN0YW5jZT17eyAuUmVsZWFzZS5OYW1lIH19IiAtbyBqc29ucGF0aD0iey5pdGVtc1swXS5tZXRhZGF0YS5uYW1lfSIpCiAgZXhwb3J0IENPTlRBSU5FUl9QT1JUPSQoa3ViZWN0bCBnZXQgcG9kIC0tbmFtZXNwYWNlIHt7IC5SZWxlYXNlLk5hbWVzcGFjZSB9fSAkUE9EX05BTUUgLW8ganNvbnBhdGg9Insuc3BlYy5jb250YWluZXJzWzBdLnBvcnRzWzBdLmNvbnRhaW5lclBvcnR9IikKICBlY2hvICJWaXNpdCBodHRwOi8vMTI3LjAuMC4xOjgwODAgdG8gdXNlIHlvdXIgYXBwbGljYXRpb24iCiAga3ViZWN0bCAtLW5hbWVzcGFjZSB7eyAuUmVsZWFzZS5OYW1lc3BhY2UgfX0gcG9ydC1mb3J3YXJkICRQT0RfTkFNRSA4MDgwOiRDT05UQUlORVJfUE9SVAp7ey0gZW5kIH19Cg=="
      },
      {
        "Name": "templates/_helpers.tpl",
        "Data": "e3svKgpFeHBhbmQgdGhlIG5hbWUgb2YgdGhlIGNoYXJ0LgoqL319Cnt7LSBkZWZpbmUgIm15YXBwLm5hbWUiIC19fQp7ey0gZGVmYXVsdCAuQ2hhcnQuTmFtZSAuVmFsdWVzLm5hbWVPdmVycmlkZSB8IHRydW5jIDYzIHwgdHJpbVN1ZmZpeCAiLSIgfX0Ke3stIGVuZCB9fQoKe3svKgpDcmVhdGUgYSBkZWZhdWx0IGZ1bGx5IHF1YWxpZmllZCBhcHAgbmFtZS4KV2UgdHJ1bmNhdGUgYXQgNjMgY2hhcnMgYmVjYXVzZSBzb21lIEt1YmVybmV0ZXMgbmFtZSBmaWVsZHMgYXJlIGxpbWl0ZWQgdG8gdGhpcyAoYnkgdGhlIEROUyBuYW1pbmcgc3BlYykuCklmIHJlbGVhc2UgbmFtZSBjb250YWlucyBjaGFydCBuYW1lIGl0IHdpbGwgYmUgdXNlZCBhcyBhIGZ1bGwgbmFtZS4KKi99fQp7ey0gZGVmaW5lICJteWFwcC5mdWxsbmFtZSIgLX19Cnt7LSBpZiAuVmFsdWVzLmZ1bGxuYW1lT3ZlcnJpZGUgfX0Ke3stIC5WYWx1ZXMuZnVsbG5hbWVPdmVycmlkZSB8IHRydW5jIDYzIHwgdHJpbVN1ZmZpeCAiLSIgfX0Ke3stIGVsc2UgfX0Ke3stICRuYW1lIDo9IGRlZmF1bHQgLkNoYXJ0Lk5hbWUgLlZhbHVlcy5uYW1lT3ZlcnJpZGUgfX0Ke3stIGlmIGNvbnRhaW5zICRuYW1lIC5SZWxlYXNlLk5hbWUgfX0Ke3stIC5SZWxlYXNlLk5hbWUgfCB0cnVuYyA2MyB8IHRyaW1TdWZmaXggIi0iIH19Cnt7LSBlbHNlIH19Cnt7LSBwcmludGYgIiVzLSVzIiAuUmVsZWFzZS5OYW1lICRuYW1lIHwgdHJ1bmMgNjMgfCB0cmltU3VmZml4ICItIiB9fQp7ey0gZW5kIH19Cnt7LSBlbmQgfX0Ke3stIGVuZCB9fQoKe3svKgpDcmVhdGUgY2hhcnQgbmFtZSBhbmQgdmVyc2lvbiBhcyB1c2VkIGJ5IHRoZSBjaGFydCBsYWJlbC4KKi99fQp7ey0gZGVmaW5lICJteWFwcC5jaGFydCIgLX19Cnt7LSBwcmludGYgIiVzLSVzIiAuQ2hhcnQuTmFtZSAuQ2hhcnQuVmVyc2lvbiB8IHJlcGxhY2UgIisiICJfIiB8IHRydW5jIDYzIHwgdHJpbVN1ZmZpeCAiLSIgfX0Ke3stIGVuZCB9fQoKe3svKgpDb21tb24gbGFiZWxzCiovfX0Ke3stIGRlZmluZSAibXlhcHAubGFiZWxzIiAtfX0KaGVsbS5zaC9jaGFydDoge3sgaW5jbHVkZSAibXlhcHAuY2hhcnQiIC4gfX0Ke3sgaW5jbHVkZSAibXlhcHAuc2VsZWN0b3JMYWJlbHMiIC4gfX0Ke3stIGlmIC5DaGFydC5BcHBWZXJzaW9uIH19CmFwcC5rdWJlcm5ldGVzLmlvL3ZlcnNpb246IHt7IC5DaGFydC5BcHBWZXJzaW9uIHwgcXVvdGUgfX0Ke3stIGVuZCB9fQphcHAua3ViZXJuZXRlcy5pby9tYW5hZ2VkLWJ5OiB7eyAuUmVsZWFzZS5TZXJ2aWNlIH19Cnt7LSBlbmQgfX0KCnt7LyoKU2VsZWN0b3IgbGFiZWxzCiovfX0Ke3stIGRlZmluZSAibXlhcHAuc2VsZWN0b3JMYWJlbHMiIC19fQphcHAua3ViZXJuZXRlcy5pby9uYW1lOiB7eyBpbmNsdWRlICJteWFwcC5uYW1lIiAuIH19CmFwcC5rdWJlcm5ldGVzLmlvL2luc3RhbmNlOiB7eyAuUmVsZWFzZS5OYW1lIH19Cnt7LSBlbmQgfX0KCnt7LyoKQ3JlYXRlIHRoZSBuYW1lIG9mIHRoZSBzZXJ2aWNlIGFjY291bnQgdG8gdXNlCiovfX0Ke3stIGRlZmluZSAibXlhcHAuc2VydmljZUFjY291bnROYW1lIiAtfX0Ke3stIGlmIC5WYWx1ZXMuc2VydmljZUFjY291bnQuY3JlYXRlIH19Cnt7LSBkZWZhdWx0IChpbmNsdWRlICJteWFwcC5mdWxsbmFtZSIgLikgLlZhbHVlcy5zZXJ2aWNlQWNjb3VudC5uYW1lIH19Cnt7LSBlbHNlIH19Cnt7LSBkZWZhdWx0ICJkZWZhdWx0IiAuVmFsdWVzLnNlcnZpY2VBY2NvdW50Lm5hbWUgfX0Ke3stIGVuZCB9fQp7ey0gZW5kIH19Cg=="
      },
      {
        "Name": "templates/deployment.yaml",
        "Data": "YXBpVmVyc2lvbjogYXBwcy92MQpraW5kOiBEZXBsb3ltZW50Cm1ldGFkYXRhOgogIG5hbWU6IHt7IGluY2x1ZGUgIm15YXBwLmZ1bGxuYW1lIiAuIH19CiAgbGFiZWxzOgogICAge3stIGluY2x1ZGUgIm15YXBwLmxhYmVscyIgLiB8IG5pbmRlbnQgNCB9fQpzcGVjOgogIHt7LSBpZiBub3QgLlZhbHVlcy5hdXRvc2NhbGluZy5lbmFibGVkIH19CiAgcmVwbGljYXM6IHt7IC5WYWx1ZXMucmVwbGljYUNvdW50IH19CiAge3stIGVuZCB9fQogIHNlbGVjdG9yOgogICAgbWF0Y2hMYWJlbHM6CiAgICAgIHt7LSBpbmNsdWRlICJteWFwcC5zZWxlY3RvckxhYmVscyIgLiB8IG5pbmRlbnQgNiB9fQogIHRlbXBsYXRlOgogICAgbWV0YWRhdGE6CiAgICAgIHt7LSB3aXRoIC5WYWx1ZXMucG9kQW5ub3RhdGlvbnMgfX0KICAgICAgYW5ub3RhdGlvbnM6CiAgICAgICAge3stIHRvWWFtbCAuIHwgbmluZGVudCA4IH19CiAgICAgIHt7LSBlbmQgfX0KICAgICAgbGFiZWxzOgogICAgICAgIHt7LSBpbmNsdWRlICJteWFwcC5zZWxlY3RvckxhYmVscyIgLiB8IG5pbmRlbnQgOCB9fQogICAgc3BlYzoKICAgICAge3stIHdpdGggLlZhbHVlcy5pbWFnZVB1bGxTZWNyZXRzIH19CiAgICAgIGltYWdlUHVsbFNlY3JldHM6CiAgICAgICAge3stIHRvWWFtbCAuIHwgbmluZGVudCA4IH19CiAgICAgIHt7LSBlbmQgfX0KICAgICAgc2VydmljZUFjY291bnROYW1lOiB7eyBpbmNsdWRlICJteWFwcC5zZXJ2aWNlQWNjb3VudE5hbWUiIC4gfX0KICAgICAgc2VjdXJpdHlDb250ZXh0OgogICAgICAgIHt7LSB0b1lhbWwgLlZhbHVlcy5wb2RTZWN1cml0eUNvbnRleHQgfCBuaW5kZW50IDggfX0KICAgICAgY29udGFpbmVyczoKICAgICAgICAtIG5hbWU6IHt7IC5DaGFydC5OYW1lIH19CiAgICAgICAgICBzZWN1cml0eUNvbnRleHQ6CiAgICAgICAgICAgIHt7LSB0b1lhbWwgLlZhbHVlcy5zZWN1cml0eUNvbnRleHQgfCBuaW5kZW50IDEyIH19CiAgICAgICAgICBpbWFnZTogInt7IC5WYWx1ZXMuaW1hZ2UucmVwb3NpdG9yeSB9fTp7eyAuVmFsdWVzLmltYWdlLnRhZyB8IGRlZmF1bHQgLkNoYXJ0LkFwcFZlcnNpb24gfX0iCiAgICAgICAgICBpbWFnZVB1bGxQb2xpY3k6IHt7IC5WYWx1ZXMuaW1hZ2UucHVsbFBvbGljeSB9fQogICAgICAgICAgcG9ydHM6CiAgICAgICAgICAgIC0gbmFtZTogaHR0cAogICAgICAgICAgICAgIGNvbnRhaW5lclBvcnQ6IDgwCiAgICAgICAgICAgICAgcHJvdG9jb2w6IFRDUAogICAgICAgICAgbGl2ZW5lc3NQcm9iZToKICAgICAgICAgICAgaHR0cEdldDoKICAgICAgICAgICAgICBwYXRoOiAvCiAgICAgICAgICAgICAgcG9ydDogaHR0cAogICAgICAgICAgcmVhZGluZXNzUHJvYmU6CiAgICAgICAgICAgIGh0dHBHZXQ6CiAgICAgICAgICAgICAgcGF0aDogLwogICAgICAgICAgICAgIHBvcnQ6IGh0dHAKICAgICAgICAgIHJlc291cmNlczoKICAgICAgICAgICAge3stIHRvWWFtbCAuVmFsdWVzLnJlc291cmNlcyB8IG5pbmRlbnQgMTIgfX0KICAgICAge3stIHdpdGggLlZhbHVlcy5ub2RlU2VsZWN0b3IgfX0KICAgICAgbm9kZVNlbGVjdG9yOgogICAgICAgIHt7LSB0b1lhbWwgLiB8IG5pbmRlbnQgOCB9fQogICAgICB7ey0gZW5kIH19CiAgICAgIHt7LSB3aXRoIC5WYWx1ZXMuYWZmaW5pdHkgfX0KICAgICAgYWZmaW5pdHk6CiAgICAgICAge3stIHRvWWFtbCAuIHwgbmluZGVudCA4IH19CiAgICAgIHt7LSBlbmQgfX0KICAgICAge3stIHdpdGggLlZhbHVlcy50b2xlcmF0aW9ucyB9fQogICAgICB0b2xlcmF0aW9uczoKICAgICAgICB7ey0gdG9ZYW1sIC4gfCBuaW5kZW50IDggfX0KICAgICAge3stIGVuZCB9fQo="
      },
      {
        "Name": "templates/hpa.yaml",
        "Data": "e3stIGlmIC5WYWx1ZXMuYXV0b3NjYWxpbmcuZW5hYmxlZCB9fQphcGlWZXJzaW9uOiBhdXRvc2NhbGluZy92MmJldGExCmtpbmQ6IEhvcml6b250YWxQb2RBdXRvc2NhbGVyCm1ldGFkYXRhOgogIG5hbWU6IHt7IGluY2x1ZGUgIm15YXBwLmZ1bGxuYW1lIiAuIH19CiAgbGFiZWxzOgogICAge3stIGluY2x1ZGUgIm15YXBwLmxhYmVscyIgLiB8IG5pbmRlbnQgNCB9fQpzcGVjOgogIHNjYWxlVGFyZ2V0UmVmOgogICAgYXBpVmVyc2lvbjogYXBwcy92MQogICAga2luZDogRGVwbG95bWVudAogICAgbmFtZToge3sgaW5jbHVkZSAibXlhcHAuZnVsbG5hbWUiIC4gfX0KICBtaW5SZXBsaWNhczoge3sgLlZhbHVlcy5hdXRvc2NhbGluZy5taW5SZXBsaWNhcyB9fQogIG1heFJlcGxpY2FzOiB7eyAuVmFsdWVzLmF1dG9zY2FsaW5nLm1heFJlcGxpY2FzIH19CiAgbWV0cmljczoKICAgIHt7LSBpZiAuVmFsdWVzLmF1dG9zY2FsaW5nLnRhcmdldENQVVV0aWxpemF0aW9uUGVyY2VudGFnZSB9fQogICAgLSB0eXBlOiBSZXNvdXJjZQogICAgICByZXNvdXJjZToKICAgICAgICBuYW1lOiBjcHUKICAgICAgICB0YXJnZXRBdmVyYWdlVXRpbGl6YXRpb246IHt7IC5WYWx1ZXMuYXV0b3NjYWxpbmcudGFyZ2V0Q1BVVXRpbGl6YXRpb25QZXJjZW50YWdlIH19CiAgICB7ey0gZW5kIH19CiAgICB7ey0gaWYgLlZhbHVlcy5hdXRvc2NhbGluZy50YXJnZXRNZW1vcnlVdGlsaXphdGlvblBlcmNlbnRhZ2UgfX0KICAgIC0gdHlwZTogUmVzb3VyY2UKICAgICAgcmVzb3VyY2U6CiAgICAgICAgbmFtZTogbWVtb3J5CiAgICAgICAgdGFyZ2V0QXZlcmFnZVV0aWxpemF0aW9uOiB7eyAuVmFsdWVzLmF1dG9zY2FsaW5nLnRhcmdldE1lbW9yeVV0aWxpemF0aW9uUGVyY2VudGFnZSB9fQogICAge3stIGVuZCB9fQp7ey0gZW5kIH19Cg=="
      },
      {
        "Name": "templates/ingress.yaml",
        "Data": "e3stIGlmIC5WYWx1ZXMuaW5ncmVzcy5lbmFibGVkIC19fQp7ey0gJGZ1bGxOYW1lIDo9IGluY2x1ZGUgIm15YXBwLmZ1bGxuYW1lIiAuIC19fQp7ey0gJHN2Y1BvcnQgOj0gLlZhbHVlcy5zZXJ2aWNlLnBvcnQgLX19Cnt7LSBpZiBzZW12ZXJDb21wYXJlICI+PTEuMTQtMCIgLkNhcGFiaWxpdGllcy5LdWJlVmVyc2lvbi5HaXRWZXJzaW9uIC19fQphcGlWZXJzaW9uOiBuZXR3b3JraW5nLms4cy5pby92MWJldGExCnt7LSBlbHNlIC19fQphcGlWZXJzaW9uOiBleHRlbnNpb25zL3YxYmV0YTEKe3stIGVuZCB9fQpraW5kOiBJbmdyZXNzCm1ldGFkYXRhOgogIG5hbWU6IHt7ICRmdWxsTmFtZSB9fQogIGxhYmVsczoKICAgIHt7LSBpbmNsdWRlICJteWFwcC5sYWJlbHMiIC4gfCBuaW5kZW50IDQgfX0KICB7ey0gd2l0aCAuVmFsdWVzLmluZ3Jlc3MuYW5ub3RhdGlvbnMgfX0KICBhbm5vdGF0aW9uczoKICAgIHt7LSB0b1lhbWwgLiB8IG5pbmRlbnQgNCB9fQogIHt7LSBlbmQgfX0Kc3BlYzoKICB7ey0gaWYgLlZhbHVlcy5pbmdyZXNzLnRscyB9fQogIHRsczoKICAgIHt7LSByYW5nZSAuVmFsdWVzLmluZ3Jlc3MudGxzIH19CiAgICAtIGhvc3RzOgogICAgICAgIHt7LSByYW5nZSAuaG9zdHMgfX0KICAgICAgICAtIHt7IC4gfCBxdW90ZSB9fQogICAgICAgIHt7LSBlbmQgfX0KICAgICAgc2VjcmV0TmFtZToge3sgLnNlY3JldE5hbWUgfX0KICAgIHt7LSBlbmQgfX0KICB7ey0gZW5kIH19CiAgcnVsZXM6CiAgICB7ey0gcmFuZ2UgLlZhbHVlcy5pbmdyZXNzLmhvc3RzIH19CiAgICAtIGhvc3Q6IHt7IC5ob3N0IHwgcXVvdGUgfX0KICAgICAgaHR0cDoKICAgICAgICBwYXRoczoKICAgICAgICAgIHt7LSByYW5nZSAucGF0aHMgfX0KICAgICAgICAgIC0gcGF0aDoge3sgLiB9fQogICAgICAgICAgICBiYWNrZW5kOgogICAgICAgICAgICAgIHNlcnZpY2VOYW1lOiB7eyAkZnVsbE5hbWUgfX0KICAgICAgICAgICAgICBzZXJ2aWNlUG9ydDoge3sgJHN2Y1BvcnQgfX0KICAgICAgICAgIHt7LSBlbmQgfX0KICAgIHt7LSBlbmQgfX0KICB7ey0gZW5kIH19Cg=="
      },
      {
        "Name": "templates/service.yaml",
        "Data": "YXBpVmVyc2lvbjogdjEKa2luZDogU2VydmljZQptZXRhZGF0YToKICBuYW1lOiB7eyBpbmNsdWRlICJteWFwcC5mdWxsbmFtZSIgLiB9fQogIGxhYmVsczoKICAgIHt7LSBpbmNsdWRlICJteWFwcC5sYWJlbHMiIC4gfCBuaW5kZW50IDQgfX0Kc3BlYzoKICB0eXBlOiB7eyAuVmFsdWVzLnNlcnZpY2UudHlwZSB9fQogIHBvcnRzOgogICAgLSBwb3J0OiB7eyAuVmFsdWVzLnNlcnZpY2UucG9ydCB9fQogICAgICB0YXJnZXRQb3J0OiBodHRwCiAgICAgIHByb3RvY29sOiBUQ1AKICAgICAgbmFtZTogaHR0cAogIHNlbGVjdG9yOgogICAge3stIGluY2x1ZGUgIm15YXBwLnNlbGVjdG9yTGFiZWxzIiAuIHwgbmluZGVudCA0IH19Cg=="
      },
      {
        "Name": "templates/serviceaccount.yaml",
        "Data": "e3stIGlmIC5WYWx1ZXMuc2VydmljZUFjY291bnQuY3JlYXRlIC19fQphcGlWZXJzaW9uOiB2MQpraW5kOiBTZXJ2aWNlQWNjb3VudAptZXRhZGF0YToKICBuYW1lOiB7eyBpbmNsdWRlICJteWFwcC5zZXJ2aWNlQWNjb3VudE5hbWUiIC4gfX0KICBsYWJlbHM6CiAgICB7ey0gaW5jbHVkZSAibXlhcHAubGFiZWxzIiAuIHwgbmluZGVudCA0IH19CiAge3stIHdpdGggLlZhbHVlcy5zZXJ2aWNlQWNjb3VudC5hbm5vdGF0aW9ucyB9fQogIGFubm90YXRpb25zOgogICAge3stIHRvWWFtbCAuIHwgbmluZGVudCA0IH19CiAge3stIGVuZCB9fQp7ey0gZW5kIH19Cg=="
      },
      {
        "Name": "templates/tests/test-connection.yaml",
        "Data": "YXBpVmVyc2lvbjogdjEKa2luZDogUG9kCm1ldGFkYXRhOgogIG5hbWU6ICJ7eyBpbmNsdWRlICJteWFwcC5mdWxsbmFtZSIgLiB9fS10ZXN0LWNvbm5lY3Rpb24iCiAgbGFiZWxzOgogICAge3stIGluY2x1ZGUgIm15YXBwLmxhYmVscyIgLiB8IG5pbmRlbnQgNCB9fQogIGFubm90YXRpb25zOgogICAgImhlbG0uc2gvaG9vayI6IHRlc3QKc3BlYzoKICBjb250YWluZXJzOgogICAgLSBuYW1lOiB3Z2V0CiAgICAgIGltYWdlOiBidXN5Ym94CiAgICAgIGNvbW1hbmQ6IFsnd2dldCddCiAgICAgIGFyZ3M6IFsne3sgaW5jbHVkZSAibXlhcHAuZnVsbG5hbWUiIC4gfX06e3sgLlZhbHVlcy5zZXJ2aWNlLnBvcnQgfX0nXQogIHJlc3RhcnRQb2xpY3k6IE5ldmVyCg=="
      },
      {
        "Name": ".helmignore",
        "Data": "IyBQYXR0ZXJucyB0byBpZ25vcmUgd2hlbiBidWlsZGluZyBwYWNrYWdlcy4KIyBUaGlzIHN1cHBvcnRzIHNoZWxsIGdsb2IgbWF0Y2hpbmcsIHJlbGF0aXZlIHBhdGggbWF0Y2hpbmcsIGFuZAojIG5lZ2F0aW9uIChwcmVmaXhlZCB3aXRoICEpLiBPbmx5IG9uZSBwYXR0ZXJuIHBlciBsaW5lLgouRFNfU3RvcmUKIyBDb21tb24gVkNTIGRpcnMKLmdpdC8KLmdpdGlnbm9yZQouYnpyLwouYnpyaWdub3JlCi5oZy8KLmhnaWdub3JlCi5zdm4vCiMgQ29tbW9uIGJhY2t1cCBmaWxlcwoqLnN3cAoqLmJhawoqLnRtcAoqLm9yaWcKKn4KIyBWYXJpb3VzIElERXMKLnByb2plY3QKLmlkZWEvCioudG1wcm9qCi52c2NvZGUvCg=="
      }
    ],
    "chart_metadata": {
      "name": "myapp",
      "version": "0.1.0",
      "description": "A Helm chart for Kubernetes",
      "apiVersion": "v2",
      "appVersion": "1.16.0",
      "type": "application"
    }
  }
}
```


## /v1/topke/app_template/categorize
上架应用模板设置分类
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
category|string|是|""|分类uuid
templates|array|是|nil|模板列表
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/categorize
```
{
	"category": "324339f9-0b0b-4426-a020-78e66bba81be",
	"templates": ["4efcf80d-7617-4e01-a906-306011b2e007"]
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "data": null
  }
}
```


## /v1/topke/app_template/on_shelves
应用模板上架
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant_uuid|string|是|""|租户uuid
uuid|string|是|""| 模板uuid
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/on_shelves
```
{
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"uuid": "dac87134-3eb2-430e-975b-f0b30c36d1d4"
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "data": {
      "tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
      "tenant_name": "",
      "type": "",
      "uuid": "dac87134-3eb2-430e-975b-f0b30c36d1d4",
      "name": "4.12.14 [6.0.7]",
      "template_uuid": "23399a2f-7018-4ba3-912b-ce4890e07ceb",
      "create_time": 1628649306,
      "update_time": 1629870268,
      "description": "This Helm chart provides a highly available Redis implementation with a master/slave configuration and uses Sentinel sidecars for failover management",
      "operator": "ndq",
      "state_operator": "",
      "status": "on_shelves",
      "status_time": 1629870268,
      "package_name": "redis-ha",
      "package_version": "4.12.14",
      "update_log": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
  }
}
```

## /v1/topke/app_template/off_shelves
应用模板下架
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant_uuid|string|是|""|租户uuid
uuid|string|是|""| 模板uuid
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/on_shelves
```
{
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"uuid": "dac87134-3eb2-430e-975b-f0b30c36d1d4"
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "data": {
      "tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
      "tenant_name": "",
      "type": "",
      "uuid": "dac87134-3eb2-430e-975b-f0b30c36d1d4",
      "name": "4.12.14 [6.0.7]",
      "template_uuid": "23399a2f-7018-4ba3-912b-ce4890e07ceb",
      "create_time": 1628649306,
      "update_time": 1629870268,
      "description": "This Helm chart provides a highly available Redis implementation with a master/slave configuration and uses Sentinel sidecars for failover management",
      "operator": "ndq",
      "state_operator": "",
      "status": "on_shelves",
      "status_time": 1629870268,
      "package_name": "redis-ha",
      "package_version": "4.12.14",
      "update_log": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
  }
}
```

## /v1/topke/app_template/version/create
应用模板版本创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群uuid
type|String|是|""|模板类型
package_data|string|是|""|模板类型
template|string|是|""|应用模板uuid
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/app_template/version/create
```
{
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"type": "helm",
	"package_data": "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",
	"template": "23399a2f-7018-4ba3-912b-ce4890e07ceb"
}
```

#### 正常返回示例

## /v1/topke/app_template/version/delete
应用模板版本删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群uuid
workspace|string|是|""|工作区uuid
uuid|string|是|""| 版本UUID
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/version/delete
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"workspace": "aaa",
	"uuid": "2ffa7014-fa2e-464a-90ac-a969d3074b66"
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "data": null
  }
}
```

## /v1/topke/app_template/version/list
应用模板版本列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant_uuid|string|是|""|租户uuid
page_size|int|否|0|页大小
page_num|int|否|0|页码
fuzzy|string|否|""|模糊搜索
template|string|是|""|模板
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/topke/app_template/version/list
```
{
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"page_size": 5,
	"page_num": 0,
	"fuzzy": "",
	"template": "23399a2f-7018-4ba3-912b-ce4890e07ceb"
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "total_count": 1,
    "list": [
      {
        "tenant": "",
        "workspace": "aaa",
        "type": "",
        "uuid": "6b712caf-556f-48f7-9952-cc3da93b6553",
        "name": "1.2.0 [1.17.5]",
        "template_uuid": "89dc65d5-bf9a-48e9-83c4-8bede60a0879",
        "create_time": 1629862731,
        "update_time": 1629862765,
        "description": "nginx is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server, originally written by Igor Sysoev.",
        "state_operator": "",
        "status": "on_shelves",
        "status_time": 1629862765,
        "package_name": "nginx",
        "package_version": "1.2.0"
      }
    ]
  }
}
```

## /v1/topke/app_template/version/manifests
应用模板版本清单
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群uuid
uuid|string|是|""| 版本UUID
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/version/manifest
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"uuid": "6b712caf-556f-48f7-9952-cc3da93b6553"
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "data": {
      "tenant": "",
      "workspace": "aaa",
      "type": "",
      "uuid": "6b712caf-556f-48f7-9952-cc3da93b6553",
      "name": "1.2.0 [1.17.5]",
      "template_uuid": "89dc65d5-bf9a-48e9-83c4-8bede60a0879",
      "create_time": 1629862731,
      "update_time": 1629862765,
      "description": "nginx is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server, originally written by Igor Sysoev.",
      "state_operator": "",
      "status": "on_shelves",
      "status_time": 1629862765,
      "package_name": "nginx",
      "package_version": "1.2.0"
    },
    "files": [
      {
        "Name": ".helmignore",
        "Data": "# Patterns to ignore when building packages.\n# This supports shell glob matching, relative path matching, and\n# negation (prefixed with !). Only one pattern per line.\n.DS_Store\n# Common VCS dirs\n.git/\n.gitignore\n.bzr/\n.bzrignore\n.hg/\n.hgignore\n.svn/\n# Common backup files\n*.swp\n*.bak\n*.tmp\n*~\n# Various IDEs\n.project\n.idea/\n*.tmproj\n.vscode/\n"
      },
      {
        "Name": "templates/cm-extra-configs.yaml",
        "Data": "{{- if .Values.extraConfigurationFiles }}\napiVersion: v1\nkind: ConfigMap\nmetadata:\n  name: {{ template \"nginx.fullname\" . }}-extra-configs\n  namespace: {{ .Release.Namespace }}\ndata:\n{{- range $key, $val := .Values.extraConfigurationFiles }}\n  {{ $key }}: |-\n{{ $val | indent 4}}\n{{- end }}\n{{- end -}}\n"
      },
      {
        "Name": "templates/NOTES.txt",
        "Data": "1. Get the application URL by running these commands:\n{{- if .Values.ingress.enabled }}\n{{- range $host := .Values.ingress.hosts }}\n  {{- range $.Values.ingress.paths }}\n  http{{ if $.Values.ingress.tls }}s{{ end }}://{{ $host }}{{ . }}\n  {{- end }}\n{{- end }}\n{{- else if contains \"NodePort\" .Values.service.type }}\n  export NODE_PORT=$(kubectl get --namespace {{ .Release.Namespace }} -o jsonpath=\"{.spec.ports[0].nodePort}\" services {{ include \"nginx.fullname\" . }})\n  export NODE_IP=$(kubectl get nodes --namespace {{ .Release.Namespace }} -o jsonpath=\"{.items[0].status.addresses[0].address}\")\n  echo http://$NODE_IP:$NODE_PORT\n{{- else if contains \"LoadBalancer\" .Values.service.type }}\n     NOTE: It may take a few minutes for the LoadBalancer IP to be available.\n           You can watch the status of by running 'kubectl get svc -w {{ include \"nginx.fullname\" . }}'\n  export SERVICE_IP=$(kubectl get svc --namespace {{ .Release.Namespace }} {{ include \"nginx.fullname\" . }} -o jsonpath='{.status.loadBalancer.ingress[0].ip}')\n  echo http://$SERVICE_IP:{{ .Values.service.port }}\n{{- else if contains \"ClusterIP\" .Values.service.type }}\n  export POD_NAME=$(kubectl get pods --namespace {{ .Release.Namespace }} -l \"app.kubernetes.io/name={{ include \"nginx.name\" . }},app.kubernetes.io/instance={{ .Release.Name }}\" -o jsonpath=\"{.items[0].metadata.name}\")\n  echo \"Visit http://127.0.0.1:8080 to use your application\"\n  kubectl port-forward $POD_NAME 8080:80\n{{- end }}\n"
      },
      {
        "Name": "templates/cm-main-config.yaml",
        "Data": "{{- if .Values.configurationFile }}\napiVersion: v1\nkind: ConfigMap\nmetadata:\n  name: {{ template \"nginx.fullname\" . }}-main-config\n  namespace: {{ .Release.Namespace }}\ndata:\n  nginx.conf: |-\n{{ tpl .Values.configurationFile . | indent 4 }}\n{{- end -}}\n"
      },
      {
        "Name": "templates/deployment.yaml",
        "Data": "apiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: {{ include \"nginx.fullname\" . }}\n  labels:\n    app.kubernetes.io/name: {{ include \"nginx.name\" . }}\n    helm.sh/chart: {{ include \"nginx.chart\" . }}\n    app.kubernetes.io/instance: {{ .Release.Name }}\n    app.kubernetes.io/managed-by: {{ .Release.Service }}\nspec:\n  replicas: {{ .Values.replicaCount }}\n  selector:\n    matchLabels:\n      app.kubernetes.io/name: {{ include \"nginx.name\" . }}\n      app.kubernetes.io/instance: {{ .Release.Name }}\n  template:\n    metadata:\n      labels:\n        app.kubernetes.io/name: {{ include \"nginx.name\" . }}\n        app.kubernetes.io/instance: {{ .Release.Name }}\n    spec:\n      initContainers:\n      {{- if .Values.image.html }}\n      - name: copy-html\n        image: {{ .Values.image.html.repository }}:{{ .Values.image.html.tag }}\n        imagePullPolicy: {{ .Values.image.html.pullPolicy }}\n        command:\n        - sh\n        - -c\n        - cp -r /html/* /nginx-html\n        volumeMounts:\n        - name: html\n          mountPath: /nginx-html\n        resources:\n          requests:\n            memory: 10Mi\n            cpu: 10m\n      {{- end }}\n      {{- with .Values.extraInitContainers }}\n      {{- toYaml . | nindent 6 }}\n      {{- end }}\n\n      containers:\n        - name: {{ .Chart.Name }}\n          image: \"{{ .Values.image.nginx.repository }}:{{ .Values.image.nginx.tag }}\"\n          imagePullPolicy: {{ .Values.image.nginx.pullPolicy }}\n          ports:\n            - name: http\n              containerPort: {{ .Values.service.port }}\n              protocol: TCP\n          livenessProbe:\n            httpGet:\n              path: {{ .Values.livenessProbe.path }}\n              port: {{ .Values.service.port }}\n            initialDelaySeconds: {{ .Values.livenessProbe.initialDelaySeconds }}\n            periodSeconds: {{ .Values.livenessProbe.periodSeconds }}\n          readinessProbe:\n            httpGet:\n              path: {{ .Values.readinessProbe.path }}\n              port: {{ .Values.service.port }}\n            initialDelaySeconds: {{ .Values.readinessProbe.initialDelaySeconds }}\n            periodSeconds: {{ .Values.readinessProbe.periodSeconds }}\n            failureThreshold: {{ .Values.readinessProbe.failureThreshold }}\n          resources:\n            {{- toYaml .Values.resources | nindent 12 }}\n          volumeMounts:\n          {{- if .Values.configurationFile }}\n          - name: main-config\n            mountPath: /etc/nginx/nginx.conf\n            subPath: nginx.conf\n          {{- end }}\n          {{- if .Values.extraConfigurationFiles }}\n          - name: extra-configs\n            mountPath: /etc/nginx/conf.d\n          {{- end }}\n          {{- if .Values.image.html }}\n          - name: html\n            mountPath: /usr/share/nginx/html\n          {{- end }}\n          {{- with .Values.extraVolumeMounts }}\n          {{- toYaml . | nindent 10 }}\n          {{- end }}\n\n      volumes:\n      - name: html\n        emptyDir: {}\n      {{- if .Values.configurationFile }}\n      - name: main-config\n        configMap:\n          name: {{ template \"nginx.fullname\" . }}-main-config\n      {{- end }}\n      {{- if .Values.extraConfigurationFiles }}\n      - name: extra-configs\n        configMap:\n          name: {{ template \"nginx.fullname\" . }}-extra-configs\n      {{- end }}\n      {{- with .Values.extraVolumes }}\n      {{- toYaml . | nindent 6 }}\n      {{- end }}\n      {{- with .Values.nodeSelector }}\n      nodeSelector:\n        {{- toYaml . | nindent 8 }}\n      {{- end }}\n    {{- with .Values.affinity }}\n      affinity:\n        {{- toYaml . | nindent 8 }}\n    {{- end }}\n    {{- with .Values.tolerations }}\n      tolerations:\n        {{- toYaml . | nindent 8 }}\n    {{- end }}\n"
      },
      {
        "Name": "templates/ingress.yaml",
        "Data": "{{- if .Values.ingress.enabled -}}\n{{- $fullName := include \"nginx.fullname\" . -}}\n{{- $ingressPaths := .Values.ingress.paths -}}\napiVersion: extensions/v1beta1\nkind: Ingress\nmetadata:\n  name: {{ $fullName }}\n  labels:\n    app.kubernetes.io/name: {{ include \"nginx.name\" . }}\n    helm.sh/chart: {{ include \"nginx.chart\" . }}\n    app.kubernetes.io/instance: {{ .Release.Name }}\n    app.kubernetes.io/managed-by: {{ .Release.Service }}\n  {{- with .Values.ingress.annotations }}\n  annotations:\n    {{- toYaml . | nindent 4 }}\n  {{- end }}\nspec:\n{{- if .Values.ingress.tls }}\n  tls:\n  {{- range .Values.ingress.tls }}\n    - hosts:\n      {{- range .hosts }}\n        - {{ . | quote }}\n      {{- end }}\n      secretName: {{ .secretName }}\n  {{- end }}\n{{- end }}\n  rules:\n  {{- range .Values.ingress.hosts }}\n    - host: {{ . | quote }}\n      http:\n        paths:\n          {{- range $ingressPaths }}\n          - path: {{ . }}\n            backend:\n              serviceName: {{ $fullName }}\n              servicePort: http\n          {{- end }}\n  {{- end }}\n{{- end }}\n"
      },
      {
        "Name": "templates/service.yaml",
        "Data": "apiVersion: v1\nkind: Service\nmetadata:\n  name: {{ include \"nginx.fullname\" . }}\n  labels:\n    app.kubernetes.io/name: {{ include \"nginx.name\" . }}\n    helm.sh/chart: {{ include \"nginx.chart\" . }}\n    app.kubernetes.io/instance: {{ .Release.Name }}\n    app.kubernetes.io/managed-by: {{ .Release.Service }}\nspec:\n  type: {{ .Values.service.type }}\n  ports:\n    - port: {{ .Values.service.port }}\n      targetPort: http\n      protocol: TCP\n      name: {{ .Values.service.name }}\n      {{- if eq .Values.service.type \"NodePort\" }}\n      nodePort: {{ .Values.service.nodePort }}\n      {{- end }}\n  selector:\n    app.kubernetes.io/name: {{ include \"nginx.name\" . }}\n    app.kubernetes.io/instance: {{ .Release.Name }}\n"
      },
      {
        "Name": "templates/tests/test-connection.yaml",
        "Data": "apiVersion: v1\nkind: Pod\nmetadata:\n  name: \"{{ include \"nginx.fullname\" . }}-test-connection\"\n  labels:\n    app.kubernetes.io/name: {{ include \"nginx.name\" . }}\n    helm.sh/chart: {{ include \"nginx.chart\" . }}\n    app.kubernetes.io/instance: {{ .Release.Name }}\n    app.kubernetes.io/managed-by: {{ .Release.Service }}\n  annotations:\n    \"helm.sh/hook\": test-success\nspec:\n  containers:\n    - name: wget\n      image: busybox\n      command: ['wget']\n      args:  ['{{ include \"nginx.fullname\" . }}:{{ .Values.service.port }}']\n  restartPolicy: Never\n"
      },
      {
        "Name": "Chart.yaml",
        "Data": "apiVersion: v1\nappVersion: 1.17.5\ndescription: nginx is an HTTP and reverse proxy server, a mail proxy server, and a\n  generic TCP/UDP proxy server, originally written by Igor Sysoev.\nicon: https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Nginx_logo.svg/500px-Nginx_logo.svg.png\nmaintainers:\n- email: kubesphere@yunify.com\n  name: KubeSphere\nname: nginx\nsources:\n- https://github.com/kubesphere/helm-charts/tree/master/src/qingcloud/nginx\nversion: 1.2.0\n"
      },
      {
        "Name": "templates/_helpers.tpl",
        "Data": "{{/* vim: set filetype=mustache: */}}\n{{/*\nExpand the name of the chart.\n*/}}\n{{- define \"nginx.name\" -}}\n{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix \"-\" -}}\n{{- end -}}\n\n{{/*\nCreate a default fully qualified app name.\nWe truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).\nIf release name contains chart name it will be used as a full name.\n*/}}\n{{- define \"nginx.fullname\" -}}\n{{- if .Values.fullnameOverride -}}\n{{- .Values.fullnameOverride | trunc 63 | trimSuffix \"-\" -}}\n{{- else -}}\n{{- $name := default .Chart.Name .Values.nameOverride -}}\n{{- if contains $name .Release.Name -}}\n{{- .Release.Name | trunc 63 | trimSuffix \"-\" -}}\n{{- else -}}\n{{- printf \"%s-%s\" .Release.Name $name | trunc 63 | trimSuffix \"-\" -}}\n{{- end -}}\n{{- end -}}\n{{- end -}}\n\n{{/*\nCreate chart name and version as used by the chart label.\n*/}}\n{{- define \"nginx.chart\" -}}\n{{- printf \"%s-%s\" .Chart.Name .Chart.Version | replace \"+\" \"_\" | trunc 63 | trimSuffix \"-\" -}}\n{{- end -}}\n"
      },
      {
        "Name": "README.md",
        "Data": "# Nginx\n\n## TL;DR;\n\n```console\nhelm install qingcloud/nginx\n```\n\n## Installing\n\nTo install the chart with the release name `my-release`:\n\n```console\nhelm install --name my-release qingcloud/nginx\n```\n\nThe command deploys the nginx chart on the Kubernetes cluster in the default configuration. The configuration section lists the parameters that can be configured during installation.\n\n## Uninstalling\n\nTo uninstall/delete the `my-release` deployment:\n\n```console\nhelm delete my-release\n```\n\nThe command removes all the Kubernetes components associated with the chart and deletes the release.\n\n## Configuration\n\nThe following table lists the configurable parameters of the nginx chart and their default values.\n\nParameter | Description | Default\n--- | --- | ---\n`image.html.repository` | The image holding static files to serve on Nginx, which locate in `/html` within the container; if specified, an initContainer will copy files under `/html` to `/usr/share/nginx/html` in Nginx container | none\n`image.html.tag` | The tag of the image holding static files to serve on Nginx | none\n`image.html.pullPolicy` | The pull policy of the image holding static files to serve on Nginx | none\n`image.nginx.repository` | The image of Nginx container | `nginx`\n`image.nginx.tag` | The tag of the Nginx image | `1.16.0-alpine`\n`image.nginx.pullPolicy` | The pull policy of the Nginx image | `IfNotPresent`\n`service.type` | The service type, can be `ClusterIP`, `NodePort` | `ClusterIP`\n`service.port` | The service port within the pod container | `80`\n`service.nodePort` | If `service.type` is `NodePort`, this value will be used | none\n`extraVolumes` | Extra volumes | []\n`extraMountVolumes` | Extra mount volumes | []\n`extraInitContainers` | Extra init containers | []\n`configurationFile` | Custom configuration file to override `/etc/nginx/nginx.conf` | none\n`extraConfigurationFiles` | Custom configuration files to put under `/etc/nginx/conf.d` | none\n"
      },
      {
        "Name": "LICENSE",
        "Data": "                                 Apache License\n                           Version 2.0, January 2004\n                        http://www.apache.org/licenses/\n\n   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION\n\n   1. Definitions.\n\n      \"License\" shall mean the terms and conditions for use, reproduction,\n      and distribution as defined by Sections 1 through 9 of this document.\n\n      \"Licensor\" shall mean the copyright owner or entity authorized by\n      the copyright owner that is granting the License.\n\n      \"Legal Entity\" shall mean the union of the acting entity and all\n      other entities that control, are controlled by, or are under common\n      control with that entity. For the purposes of this definition,\n      \"control\" means (i) the power, direct or indirect, to cause the\n      direction or management of such entity, whether by contract or\n      otherwise, or (ii) ownership of fifty percent (50%) or more of the\n      outstanding shares, or (iii) beneficial ownership of such entity.\n\n      \"You\" (or \"Your\") shall mean an individual or Legal Entity\n      exercising permissions granted by this License.\n\n      \"Source\" form shall mean the preferred form for making modifications,\n      including but not limited to software source code, documentation\n      source, and configuration files.\n\n      \"Object\" form shall mean any form resulting from mechanical\n      transformation or translation of a Source form, including but\n      not limited to compiled object code, generated documentation,\n      and conversions to other media types.\n\n      \"Work\" shall mean the work of authorship, whether in Source or\n      Object form, made available under the License, as indicated by a\n      copyright notice that is included in or attached to the work\n      (an example is provided in the Appendix below).\n\n      \"Derivative Works\" shall mean any work, whether in Source or Object\n      form, that is based on (or derived from) the Work and for which the\n      editorial revisions, annotations, elaborations, or other modifications\n      represent, as a whole, an original work of authorship. For the purposes\n      of this License, Derivative Works shall not include works that remain\n      separable from, or merely link (or bind by name) to the interfaces of,\n      the Work and Derivative Works thereof.\n\n      \"Contribution\" shall mean any work of authorship, including\n      the original version of the Work and any modifications or additions\n      to that Work or Derivative Works thereof, that is intentionally\n      submitted to Licensor for inclusion in the Work by the copyright owner\n      or by an individual or Legal Entity authorized to submit on behalf of\n      the copyright owner. For the purposes of this definition, \"submitted\"\n      means any form of electronic, verbal, or written communication sent\n      to the Licensor or its representatives, including but not limited to\n      communication on electronic mailing lists, source code control systems,\n      and issue tracking systems that are managed by, or on behalf of, the\n      Licensor for the purpose of discussing and improving the Work, but\n      excluding communication that is conspicuously marked or otherwise\n      designated in writing by the copyright owner as \"Not a Contribution.\"\n\n      \"Contributor\" shall mean Licensor and any individual or Legal Entity\n      on behalf of whom a Contribution has been received by Licensor and\n      subsequently incorporated within the Work.\n\n   2. Grant of Copyright License. Subject to the terms and conditions of\n      this License, each Contributor hereby grants to You a perpetual,\n      worldwide, non-exclusive, no-charge, royalty-free, irrevocable\n      copyright license to reproduce, prepare Derivative Works of,\n      publicly display, publicly perform, sublicense, and distribute the\n      Work and such Derivative Works in Source or Object form.\n\n   3. Grant of Patent License. Subject to the terms and conditions of\n      this License, each Contributor hereby grants to You a perpetual,\n      worldwide, non-exclusive, no-charge, royalty-free, irrevocable\n      (except as stated in this section) patent license to make, have made,\n      use, offer to sell, sell, import, and otherwise transfer the Work,\n      where such license applies only to those patent claims licensable\n      by such Contributor that are necessarily infringed by their\n      Contribution(s) alone or by combination of their Contribution(s)\n      with the Work to which such Contribution(s) was submitted. If You\n      institute patent litigation against any entity (including a\n      cross-claim or counterclaim in a lawsuit) alleging that the Work\n      or a Contribution incorporated within the Work constitutes direct\n      or contributory patent infringement, then any patent licenses\n      granted to You under this License for that Work shall terminate\n      as of the date such litigation is filed.\n\n   4. Redistribution. You may reproduce and distribute copies of the\n      Work or Derivative Works thereof in any medium, with or without\n      modifications, and in Source or Object form, provided that You\n      meet the following conditions:\n\n      (a) You must give any other recipients of the Work or\n          Derivative Works a copy of this License; and\n\n      (b) You must cause any modified files to carry prominent notices\n          stating that You changed the files; and\n\n      (c) You must retain, in the Source form of any Derivative Works\n          that You distribute, all copyright, patent, trademark, and\n          attribution notices from the Source form of the Work,\n          excluding those notices that do not pertain to any part of\n          the Derivative Works; and\n\n      (d) If the Work includes a \"NOTICE\" text file as part of its\n          distribution, then any Derivative Works that You distribute must\n          include a readable copy of the attribution notices contained\n          within such NOTICE file, excluding those notices that do not\n          pertain to any part of the Derivative Works, in at least one\n          of the following places: within a NOTICE text file distributed\n          as part of the Derivative Works; within the Source form or\n          documentation, if provided along with the Derivative Works; or,\n          within a display generated by the Derivative Works, if and\n          wherever such third-party notices normally appear. The contents\n          of the NOTICE file are for informational purposes only and\n          do not modify the License. You may add Your own attribution\n          notices within Derivative Works that You distribute, alongside\n          or as an addendum to the NOTICE text from the Work, provided\n          that such additional attribution notices cannot be construed\n          as modifying the License.\n\n      You may add Your own copyright statement to Your modifications and\n      may provide additional or different license terms and conditions\n      for use, reproduction, or distribution of Your modifications, or\n      for any such Derivative Works as a whole, provided Your use,\n      reproduction, and distribution of the Work otherwise complies with\n      the conditions stated in this License.\n\n   5. Submission of Contributions. Unless You explicitly state otherwise,\n      any Contribution intentionally submitted for inclusion in the Work\n      by You to the Licensor shall be under the terms and conditions of\n      this License, without any additional terms or conditions.\n      Notwithstanding the above, nothing herein shall supersede or modify\n      the terms of any separate license agreement you may have executed\n      with Licensor regarding such Contributions.\n\n   6. Trademarks. This License does not grant permission to use the trade\n      names, trademarks, service marks, or product names of the Licensor,\n      except as required for reasonable and customary use in describing the\n      origin of the Work and reproducing the content of the NOTICE file.\n\n   7. Disclaimer of Warranty. Unless required by applicable law or\n      agreed to in writing, Licensor provides the Work (and each\n      Contributor provides its Contributions) on an \"AS IS\" BASIS,\n      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or\n      implied, including, without limitation, any warranties or conditions\n      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A\n      PARTICULAR PURPOSE. You are solely responsible for determining the\n      appropriateness of using or redistributing the Work and assume any\n      risks associated with Your exercise of permissions under this License.\n\n   8. Limitation of Liability. In no event and under no legal theory,\n      whether in tort (including negligence), contract, or otherwise,\n      unless required by applicable law (such as deliberate and grossly\n      negligent acts) or agreed to in writing, shall any Contributor be\n      liable to You for damages, including any direct, indirect, special,\n      incidental, or consequential damages of any character arising as a\n      result of this License or out of the use or inability to use the\n      Work (including but not limited to damages for loss of goodwill,\n      work stoppage, computer failure or malfunction, or any and all\n      other commercial damages or losses), even if such Contributor\n      has been advised of the possibility of such damages.\n\n   9. Accepting Warranty or Additional Liability. While redistributing\n      the Work or Derivative Works thereof, You may choose to offer,\n      and charge a fee for, acceptance of support, warranty, indemnity,\n      or other liability obligations and/or rights consistent with this\n      License. However, in accepting such obligations, You may act only\n      on Your own behalf and on Your sole responsibility, not on behalf\n      of any other Contributor, and only if You agree to indemnify,\n      defend, and hold each Contributor harmless for any liability\n      incurred by, or claims asserted against, such Contributor by reason\n      of your accepting any such warranty or additional liability.\n\n   END OF TERMS AND CONDITIONS\n\n   APPENDIX: How to apply the Apache License to your work.\n\n      To apply the Apache License to your work, attach the following\n      boilerplate notice, with the fields enclosed by brackets \"[]\"\n      replaced with your own identifying information. (Don't include\n      the brackets!)  The text should be enclosed in the appropriate\n      comment syntax for the file format. We also recommend that a\n      file or class name and description of purpose be included on the\n      same \"printed page\" as the copyright notice for easier\n      identification within third-party archives.\n\n   Copyright [yyyy] [name of copyright owner]\n\n   Licensed under the Apache License, Version 2.0 (the \"License\");\n   you may not use this file except in compliance with the License.\n   You may obtain a copy of the License at\n\n       http://www.apache.org/licenses/LICENSE-2.0\n\n   Unless required by applicable law or agreed to in writing, software\n   distributed under the License is distributed on an \"AS IS\" BASIS,\n   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n   See the License for the specific language governing permissions and\n   limitations under the License.\n"
      },
      {
        "Name": "values.yaml",
        "Data": "replicaCount: 1\n\nimage:\n  # html:\n  #   repository: nginx\n  #   tag: 1.16.0-alpine\n  #   pullPolicy: IfNotPresent\n  nginx:\n    repository: nginx\n    tag: 1.17.5-alpine\n    pullPolicy: IfNotPresent\n\nnameOverride: \"\"\nfullnameOverride: \"\"\n\nservice:\n  name: http\n  type: ClusterIP\n  port: 80\n\ningress:\n  enabled: false\n  annotations: {}\n    # kubernetes.io/ingress.class: nginx\n    # kubernetes.io/tls-acme: \"true\"\n  paths: []\n  hosts:\n    - nginx.local\n  tls: []\n  #  - secretName: nginx-tls\n  #    hosts:\n  #      - nginx.local\n\nextraVolumes: []\n  # - name: extra\n  #   emptyDir: {}\n\nextraVolumeMounts: []\n  # - name: extras\n  #   mountPath: /usr/share/nginx/html\n  #   readOnly: true\n\nextraInitContainers: []\n  # - name: do-something\n  #   image: busybox\n  #   imagePullPolicy: IfNotPresent\n  #   command: ['do', 'something']\n\nreadinessProbe:\n  path: \"/\"\n  initialDelaySeconds: 5\n  periodSeconds: 3\n  failureThreshold: 6\nlivenessProbe:\n  path: \"/\"\n  initialDelaySeconds: 5\n  periodSeconds: 3\n\nresources: {}\n  # limits:\n  #  cpu: 100m\n  #  memory: 128Mi\n  # requests:\n  #  cpu: 100m\n  #  memory: 128Mi\n\nconfigurationFile: {}\n#  nginx.conf: |-\n#  http {\n#    server {\n#      listen 80;\n#      location / {\n#        root /usr/share/nginx/html;\n#      }\n#    }\n#  }\n\nextraConfigurationFiles: {}\n#  default.conf: |-\n#    server {\n#      listen 80;\n#      location / {\n#        root /usr/share/nginx/html;\n#      }\n#    }\n\nnodeSelector: {}\n\ntolerations: []\n\naffinity: {}\n"
      }
    ],
    "manifests": "---\n# Source: nginx/templates/service.yaml\napiVersion: v1\nkind: Service\nmetadata:\n  name: -nginx\n  labels:\n    app.kubernetes.io/name: nginx\n    helm.sh/chart: nginx-1.2.0\n    app.kubernetes.io/instance: \n    app.kubernetes.io/managed-by: Helm\nspec:\n  type: ClusterIP\n  ports:\n    - port: 80\n      targetPort: http\n      protocol: TCP\n      name: http\n  selector:\n    app.kubernetes.io/name: nginx\n    app.kubernetes.io/instance:\n---\n# Source: nginx/templates/deployment.yaml\napiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: -nginx\n  labels:\n    app.kubernetes.io/name: nginx\n    helm.sh/chart: nginx-1.2.0\n    app.kubernetes.io/instance: \n    app.kubernetes.io/managed-by: Helm\nspec:\n  replicas: 1\n  selector:\n    matchLabels:\n      app.kubernetes.io/name: nginx\n      app.kubernetes.io/instance: \n  template:\n    metadata:\n      labels:\n        app.kubernetes.io/name: nginx\n        app.kubernetes.io/instance: \n    spec:\n      initContainers:\n\n      containers:\n        - name: nginx\n          image: \"nginx:1.17.5-alpine\"\n          imagePullPolicy: IfNotPresent\n          ports:\n            - name: http\n              containerPort: 80\n              protocol: TCP\n          livenessProbe:\n            httpGet:\n              path: /\n              port: 80\n            initialDelaySeconds: 5\n            periodSeconds: 3\n          readinessProbe:\n            httpGet:\n              path: /\n              port: 80\n            initialDelaySeconds: 5\n            periodSeconds: 3\n            failureThreshold: 6\n          resources:\n            {}\n          volumeMounts:\n\n      volumes:\n      - name: html\n        emptyDir: {}\n",
    "package_data": "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"
  }
}
```

## /v1/topke/app_template/version/approval/submit
应用模板版本审核提交
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群uuid
workspace|string|是|""|工作区uuid
uuid|string|是|""| 版本UUID
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/version/approval/submit
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"workspace": "aaa",
	"uuid": "1e82da37-874d-4dd5-9617-30c9bad1d5fd"
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "data": {
      "tenant": "",
      "workspace": "aaa",
      "type": "",
      "uuid": "1e82da37-874d-4dd5-9617-30c9bad1d5fd",
      "name": "0.1.0 [1.16.0]",
      "template_uuid": "d9d10646-aac8-4ea0-9922-b08775fe934c",
      "create_time": 1629859584,
      "update_time": 1629860488,
      "description": "A Helm chart for Kubernetes",
      "state_operator": "",
      "status": "approving",
      "status_time": 1629860488,
      "package_name": "myapp",
      "package_version": "0.1.0"
    }
  }
}
```

## /v1/topke/app_template/version/approval/reject
应用模板版本审核拒绝
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群uuid
workspace|string|是|""|工作区uuid
uuid|string|是|""| 版本UUID
reason|string|是|""|原因
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/version/approval/reject
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"workspace": "aaa",
	"uuid": "1e82da37-874d-4dd5-9617-30c9bad1d5fd",
        "reason":""
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "data": {
      "tenant": "",
      "workspace": "aaa",
      "type": "",
      "uuid": "1e82da37-874d-4dd5-9617-30c9bad1d5fd",
      "name": "0.1.0 [1.16.0]",
      "template_uuid": "d9d10646-aac8-4ea0-9922-b08775fe934c",
      "create_time": 1629859584,
      "update_time": 1629860488,
      "description": "A Helm chart for Kubernetes",
      "state_operator": "",
      "status": "approving",
      "status_time": 1629860488,
      "package_name": "myapp",
      "package_version": "0.1.0"
    }
  }
}
```

## /v1/topke/app_template/version/approval/pass
应用模板版本审核通过
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群uuid
workspace|string|是|""|工作区uuid
uuid|string|是|""| 版本UUID
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/version/approval/pass
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"workspace": "aaa",
	"uuid": "1e82da37-874d-4dd5-9617-30c9bad1d5fd",
        "reason":""
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "data": {
      "tenant": "",
      "workspace": "aaa",
      "type": "",
      "uuid": "1e82da37-874d-4dd5-9617-30c9bad1d5fd",
      "name": "0.1.0 [1.16.0]",
      "template_uuid": "d9d10646-aac8-4ea0-9922-b08775fe934c",
      "create_time": 1629859584,
      "update_time": 1629860488,
      "description": "A Helm chart for Kubernetes",
      "state_operator": "",
      "status": "approving",
      "status_time": 1629860488,
      "package_name": "myapp",
      "package_version": "0.1.0"
    }
  }
}
```
## /v1/topke/app_template/version/approval/cancel
应用模板版本审核撤销
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群uuid
workspace|string|是|""|工作区uuid
uuid|string|是|""| 版本UUID
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/version/approval/cancel
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"workspace": "aaa",
	"uuid": "1e82da37-874d-4dd5-9617-30c9bad1d5fd",
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "data": {
      "tenant": "",
      "workspace": "aaa",
      "type": "",
      "uuid": "1e82da37-874d-4dd5-9617-30c9bad1d5fd",
      "name": "0.1.0 [1.16.0]",
      "template_uuid": "d9d10646-aac8-4ea0-9922-b08775fe934c",
      "create_time": 1629859584,
      "update_time": 1629860488,
      "description": "A Helm chart for Kubernetes",
      "state_operator": "",
      "status": "approving",
      "status_time": 1629860488,
      "package_name": "myapp",
      "package_version": "0.1.0"
    }
  }
}
```

## /v1/topke/app_template/version/release
应用模板版本发布到应用商店
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群uuid
workspace|string|是|""|工作区uuid
uuid|string|是|""| 版本UUID
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/version/release
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"workspace": "aaa",
	"uuid": "1e82da37-874d-4dd5-9617-30c9bad1d5fd",
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "data": {
      "tenant": "",
      "workspace": "aaa",
      "type": "",
      "uuid": "1e82da37-874d-4dd5-9617-30c9bad1d5fd",
      "name": "0.1.0 [1.16.0]",
      "template_uuid": "d9d10646-aac8-4ea0-9922-b08775fe934c",
      "create_time": 1629859584,
      "update_time": 1629860488,
      "description": "A Helm chart for Kubernetes",
      "state_operator": "",
      "status": "approving",
      "status_time": 1629860488,
      "package_name": "myapp",
      "package_version": "0.1.0"
    }
  }
}
```
## /v1/topke/app_template/version/on_shelves
应用模板版本上架
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群uuid
workspace|string|是|""|工作区uuid
uuid|string|是|""| 版本UUID
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/version/on_shelves
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"workspace": "aaa",
	"uuid": "1e82da37-874d-4dd5-9617-30c9bad1d5fd",
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "data": {
      "tenant": "",
      "workspace": "aaa",
      "type": "",
      "uuid": "1e82da37-874d-4dd5-9617-30c9bad1d5fd",
      "name": "0.1.0 [1.16.0]",
      "template_uuid": "d9d10646-aac8-4ea0-9922-b08775fe934c",
      "create_time": 1629859584,
      "update_time": 1629860488,
      "description": "A Helm chart for Kubernetes",
      "state_operator": "",
      "status": "approving",
      "status_time": 1629860488,
      "package_name": "myapp",
      "package_version": "0.1.0"
    }
  }
}
```
## /v1/topke/app_template/version/off_shelves
应用模板版本下架
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群uuid
workspace|string|是|""|工作区uuid
uuid|string|是|""| 版本UUID
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/version/off_shelves
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"workspace": "aaa",
	"uuid": "1e82da37-874d-4dd5-9617-30c9bad1d5fd",
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "data": {
      "tenant": "",
      "workspace": "aaa",
      "type": "",
      "uuid": "1e82da37-874d-4dd5-9617-30c9bad1d5fd",
      "name": "0.1.0 [1.16.0]",
      "template_uuid": "d9d10646-aac8-4ea0-9922-b08775fe934c",
      "create_time": 1629859584,
      "update_time": 1629860488,
      "description": "A Helm chart for Kubernetes",
      "state_operator": "",
      "status": "approving",
      "status_time": 1629860488,
      "package_name": "myapp",
      "package_version": "0.1.0"
    }
  }
}
```

## /v1/topke/app_template/category/create
应用模板分类创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群UUID
name|string|是|""|分类名
icon|string|否|""|图标
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/category/create
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"name": "aa",
	"icon": "sg-iconfont im-icon-xuniyuechi_kaiqidingwei",
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "uuid": "3bec2fbc-3313-40a0-8d01-36f9dd63c373",
    "name": "aa",
    "create_time": 1629860029,
    "description": "",
    "template_num": 0,
    "templates": null,
    "icon": "sg-iconfont im-icon-xuniyuechi_kaiqidingwei"
  }
}
```

## /v1/topke/app_template/category/list
应用模板分类列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群UUID
state_set|string array|是|[]|状态集
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/category/list
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"state_set": ["on_shelves"],
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "total_count": 1,
    "list": [
      {
        "uuid": "3bec2fbc-3313-40a0-8d01-36f9dd63c373",
        "name": "aa",
        "create_time": 1629860029,
        "description": "",
        "template_num": 0,
        "templates": null,
        "icon": "sg-iconfont im-icon-xuniyuechi_kaiqidingwei"
      }
    ]
  }
}
```

## /v1/topke/app_template/category/delete
应用模板分类删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群UUID
uuid|string|是|""|分类uuid
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/category/delete 
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"uuid": "3bec2fbc-3313-40a0-8d01-36f9dd63c373",
}
```

#### 正常返回示例
    
## /v1/topke/app_template/version/category/update
应用模板分类更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群UUID
uuid|string|是|""|分类uuid
name|string|是|""|分类名
ico|string|否|""|分类图标
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/category/update 
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"name": "aa",
	"icon": "sg-iconfont im-icon-icon_yuechi",
	"uuid": "3bec2fbc-3313-40a0-8d01-36f9dd63c373",
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "uuid": "3bec2fbc-3313-40a0-8d01-36f9dd63c373",
    "name": "aa",
    "create_time": 1629860029,
    "description": "",
    "template_num": 0,
    "templates": null,
    "icon": "sg-iconfont im-icon-icon_yuechi"
  }
}
```

## /v1/topke/app_template/version/audit/list
应用模板审计列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群UUID
workspace|string|是|""|工作区名
version|string|是|""|应用版本名
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/audit/list
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"workspace": "aaa",
	"version": "6b712caf-556f-48f7-9952-cc3da93b6553"
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "total_count": 4,
    "list": [
      {
        "uuid": "33c7850b-b5c9-4cc2-9a89-f399269a2cba",
        "tenant": "",
        "tenant_name": "",
        "operator": "",
        "operator_name": "",
        "template": "89dc65d5-bf9a-48e9-83c4-8bede60a0879",
        "template_name": "nginx",
        "version": "6b712caf-556f-48f7-9952-cc3da93b6553",
        "version_name": "1.2.0 [1.17.5]",
        "state": "on_shelves",
        "state_time": 1629862765,
        "reason": ""
      },
      {
        "uuid": "ab13099e-31e8-4996-b69f-06f72a1983e9",
        "tenant": "",
        "tenant_name": "",
        "operator": "",
        "operator_name": "",
        "template": "89dc65d5-bf9a-48e9-83c4-8bede60a0879",
        "template_name": "nginx",
        "version": "6b712caf-556f-48f7-9952-cc3da93b6553",
        "version_name": "1.2.0 [1.17.5]",
        "state": "approved",
        "state_time": 1629862754,
        "reason": ""
      },
      {
        "uuid": "63feb767-a928-41d5-91b3-6ff6b615a09d",
        "tenant": "",
        "tenant_name": "",
        "operator": "",
        "operator_name": "",
        "template": "89dc65d5-bf9a-48e9-83c4-8bede60a0879",
        "template_name": "nginx",
        "version": "6b712caf-556f-48f7-9952-cc3da93b6553",
        "version_name": "1.2.0 [1.17.5]",
        "state": "approving",
        "state_time": 1629862748,
        "reason": ""
      },
      {
        "uuid": "24410cbe-c932-4f9a-a564-3ddf05ae9aec",
        "tenant": "",
        "tenant_name": "",
        "operator": "",
        "operator_name": "",
        "template": "89dc65d5-bf9a-48e9-83c4-8bede60a0879",
        "template_name": "nginx",
        "version": "6b712caf-556f-48f7-9952-cc3da93b6553",
        "version_name": "1.2.0 [1.17.5]",
        "state": "create",
        "state_time": 1629862732,
        "reason": ""
      }
    ]
  }
}
```



## /v1/topke/app_template/instance/list
应用实例列表
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群uuid
namespace|string|是|""|命名空间
template|string|是|""|模板uuid
fuzzy|string|是|""| 模糊匹配
values_data|string|是|""|模板值
description|string|否|""|描述
name|string|是|""|实例名
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"workspace": "aaa",
	"template": "89dc65d5-bf9a-48e9-83c4-8bede60a0879",
	"fuzzy": "",
	"page_size": 5,
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "static_total_count": 1,
    "total_count": 1,
    "list": [
      {
        "uuid": "98ac9d28-612a-45da-b258-149767ed8bb3",
        "topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
        "namespace": "aaa",
        "tenant": "",
        "state": "active",
        "name": "nginx-ylnsxn",
        "config": null,
        "info": null,
        "version": 1,
        "create_time": 1629871381,
        "update_time": 1629871381,
        "package_data": "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",
        "template": {
          "tenant": "",
          "workspace": "aaa",
          "name": "nginx",
          "uuid": "89dc65d5-bf9a-48e9-83c4-8bede60a0879",
          "type": "helm",
          "create_time": 1629862731,
          "creator": "",
          "description": "nginx is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server, originally written by Igor Sysoev.",
          "status": "on_shelves",
          "status_time": 1629862765,
          "update_time": 1629862765,
          "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Nginx_logo.svg/500px-Nginx_logo.svg.png",
          "keywords": null,
          "home": "",
          "tags": "",
          "category_set": null,
          "latest_version": null,
          "version_num": 0,
          "instance_num": 0
        },
        "template_version": {
          "tenant": "",
          "workspace": "aaa",
          "type": "",
          "uuid": "6b712caf-556f-48f7-9952-cc3da93b6553",
          "name": "1.2.0 [1.17.5]",
          "template_uuid": "89dc65d5-bf9a-48e9-83c4-8bede60a0879",
          "create_time": 1629862731,
          "update_time": 1629862765,
          "description": "nginx is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server, originally written by Igor Sysoev.",
          "state_operator": "",
          "status": "on_shelves",
          "status_time": 1629862765,
          "package_name": "nginx",
          "package_version": "1.2.0"
        }
      }
    ]
  }
}
```
## /v1/topke/app_template/instance/get
应用实例详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群uuid
namespace|string|是|""|命名空间
workspace|string|是|""|工作区
uuid|string|是|""|实例uuid
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/instance/get
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"namespace": "aaa",
	"workspace": "aaa",
	"uuid": "98ac9d28-612a-45da-b258-149767ed8bb3"
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "data": {
      "uuid": "98ac9d28-612a-45da-b258-149767ed8bb3",
      "topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
      "namespace": "aaa",
      "tenant": "",
      "state": "active",
      "name": "nginx-ylnsxn",
      "config": null,
      "info": null,
      "version": 1,
      "create_time": 1629871381,
      "update_time": 1629871381,
      "package_data": "H4sIAAAAAAAA/+x9/XPcNrLg/sy/ot8oW7ZyM5yR/PmUStV5JWVX7zmSSpKTy6VSEYbsmcGKBBgAlDRr6/72KzQAEuSMPmxnnds98QdbQwKNRqO/GwRZVV2O3haTo5+W1X9d/+8XJ+N0gUXJ50Iq/NPvc00mk8mrFy/o/8lk0v9/8mL7ZfM33d96/nz7+Z9g8juNf+dVa8PUnyafPVZ/cv8i1wYcM2NQCQ1Gglt2uFqggGnNi5yLOVQsu2Bz1GmyAWcLrkHXVSWV0aAXWBQwL+QUSmayBRfzISgsmOGXCBUzi+g+E3myAQLnzHAp4GmlcMavMYcrbhbwH5spHIliCVJQT4sSVKig4ALTJN07/fXUSIXJBuzKspQCftg9hZwrnaRzbsb0r0M/Saf/UGP6N9xYzMf2n/BTX4pxC2jKsou6ghkvUCdfp/qqSr5Op+wi+To1ZZV8/X+SDfiBKS5rDQd7+zpJKyX/jplJUp4jG7t2Sv49SS91JnMcJ3/0qj78WpV/g2VVMIN6nJUjvDaKjTIpZnyu0yUri08Y4z75f/7iVVf+tyfPtl88yv+XuN6/HwGfQfoDK2rUKa33Li13rUhQv7NiATc3Cav4D6g0l2IHLreSCy7yHXBNv2dVUqJhOTNsJwEQrMQdeP8eAi/BQMy5uE5ndVHYhwNI4eamy12+n65Y5jqnJ1gg05gehtsWDTeGRVsxMUf46gKXQ/jqkhWw8+1D5gEWtu0FNzc78GGU2J+2+wfgIkdh4PnNDQ2AIofoz9HNzb+QYD/wukv+D4/O9k9Tc20+c4x75H/71eRFz/6/eLW9/Sj/X+LaSuGvaMAsEFhVFTxz1vndyVuYLkHVQlgXwCxQI2SyLJnItRO/SGtwMVeodYqCTQtshMYL6EJqE8tmaG3vNxLZtO63sl6Eb7Uwpnr/3g680soUto1+/94L7c54bMWahr65scqkHagn1uHPQqMFnUlhGBcaBocyx2OpzKDBXKO65BmmZlmhg4fX1hOCw6O9/V+Pj07Ovv3q6UU9xcwUMEcDo1Gj0m7VaDCS8HcthZ3ot4P3qa4wS8m/+nnySyo8EjcD8KNrC4mLrKjzW/TqZg+xg+MeWhao/iTkuMGS8NKGmVqnLM8t/ZHu+R83A0IgW0hasZ3x+CuPxs5XDaFuoflbyfK/sIKJDNVddAcAq5124MBAyZZg2AUCgxleQclFbVDDTCpi6xgkHBxbN3eKwC4ZLyy3pg6au36SNWRMwJX1Wqm3myfIWSwOT2Ji6ssMRlf3LsqTdlFO909+ONhdsy4E6iGrct9gnWV78j6sVhGRIoiOXThe3TxZWbMWyx2LR28paCK3is5uUWuD6uD4AbJzfLT36+Gb7/d7tKhk/lAWLWDAqiq1vZVAY9WCHNuO367SqaXRcLUPF9pY4nzbHwtubga3ikLwfAh2xPyDH7jmJtBza/tVOkkn6dbO68nrieXCWiMsZa1ixTtIAAIVLHVGM6mumMrhq0AmsN13Xk9i/fUZ+v8e/79kXHgH7VO9//v9/2ev+vb/1avnj/b/i1w9S571XeZ/kucf8dVH+f0ADpztGpx3UxV34J9Gfv2/vTf/8ddd8p9jVchlicJ8uuz/6X75f7X16nlf/p89yv+XuWLZZlWlx42A7zWrv17C73RAEoCCTbHQO+RerTfP68B0QAAssChTvRhnC6bMuvb0IOpwu1Ff1S239ymZYHPMR9Nlt9epc2JsR+um28kpJOOtXUOvhvzNXVkL40bRWGBmpHL0oKzo24hAn0GiT5lzkHGPTbS89io6iH0Wap+2IIG29uKCm13nWKJqkOoHoCWbY7owZdEOPfKsmslqObKPGpSodWe92v526aTmRirKD61vY9g8niI9Oa6L4lgWPFveBrlqWsSdfVDdUnsEehH9GGXRj6yCkYKxBTf+GsZE9O7cLmVRl/i9ZTwdw3S06DQFKG2zY2YWO2thKdSyVhlGgOzN32rUpnPPslAp1XIHtibf886DrKrt3TJaN++0tjeoANDJ3B10Fr3b2sifWFmQXRfesL/stvADJIHAfeZp6WEXatdqkA77dbhksLKYjtXv4RPXyDHKoA/1Tl5xPdczC1BQ0KN9u7im6jyI5n4svfq8LY7r9quUNDKTxQ6c7R5Hzwp+iQK1PlZyil0s7Oh/RbPTh0TcFQ3cAUHZnTXDfwy2VkFwVuxhwZanmEmR6zsGXNO6D7BCxWV+P6hOuy4QhSznn0moLowvQaneiJ9Fqj72t9MKYMZ4USs8WyjUC1nkdwHqt+3TfY3G6qqNBqxvGamRre0utPW6dMX4rI2Z2tZBPLshT3vFShhN5hTxuA1zOo11PXVN1z5f0a5rsL2zMtLHuV+guQ9r2zLNPxKjdcYbbjda3bFrrcZ6wRR6DHqNbx1/1eb8EK32avs1Vmdrstqsa3ocAzW8s3ZCWFZmucfVDry/We/c3MFfd/FWFgL0mHU/LT5fS8mP5au7eeqzsF0H8oGehlv1T3UxboEsZI6n3uFvm8V321neMt7rW8dbGY3NZlZVR45CuPPwUe4bw8gC3apGpIpuftJIf3Ts+3jdnf8JxbXPSv48oP47ed7P/758+bj/68tc91RyRz5j+pXVuBQj7Xx7V+anae8BHVP1dk3x15V1R73sMl4bFPZPPb7cmqJhIRl14Lqtz0S1yP3/kHhao50DUZkQ0sRaOrqxk9yhnZ+vVMddCuYW7nDV9gTAODq35ftbW1r7TwX/OIPj+0QbAYKrQBX7D/BbLQ3eYXk1ZgrNYRPLt7/vKvcDqLrAezDvIOVw37kFLarwNcgTZ/fDBb+5oSMVPWe3DQD78dGUZRcYp4jC5IknDm8RgzVNXRaglyfoEGY9wf5oJfV4/dOuu+x/yCX8k+3/1rOtyYr9nzza/y9yra3temvzWPe5o+5jlhWuzby1G1yiXO3ooZk6w9QczYqiXpeQbVPYPYiiYwO8Dcff1mMabXPrRKq3ZozDw1vMcrfQ9ckM8LHr+UfL0b/qdZf+N6iN+3eUSSEws47kJ1iD+/T/Svy3vfV8+9Wj/v8S11r9fyzzNbp/cJ/yH/VYZfDvbw3WhFiDgO1CyovBDhBRdJ1lNn4N1qNflAzJ0as5mlD4dvXHaa2XU3ndFDNdtRh+fmKbPvklZPzUXO8A/PzkvjW6Yy8nAVNo5cGE6uQhXqJ6VK7/vteq/nf18M/1+ePrHv0/ebX1qv/+5/b21qP+/xJXT/+zqmp+bqVbr9IXSY46U7wydI9UCnANTMDfzs6OgYkclFUSGq2Ter2kXAOqITAoGS/6N0UOLAGYo0DFM+vNjt/tHfdaScXnXLCiWMKV4saggOkSDuZSwelSS7xME55ZdKyHrHfG47oqJMvTK37BS8w5S6Waj+2vyv4aZ/Sipx6bRV1Ox9k4ezE+tBP5tZBzmerL+fjFZFJdj7o300rMk5LxVlOPAO2cdmiLtq4WqPB/LmvBZ8s0k2VjKP+7nuIpPU3cDaJa0pSmRw3ec24W9dR2Hrcgx9aAjMik6bFRiOOSaYNqrFU2/o2LeVbIOnf1zuSyXa3tdPLxmvou/+/XBRYVKp2a6p+b/1+R/5cvJ4/+3xe53r8ffw2XvNwBjYbegbZR4belJUu2wB34eky5wPHXyf51ZcXXLJD4HOSM/iZGTRPfbgQ5zrjoeXKj9hmrC9PZdNUUTVmJR5eoFM8RPoBRtcjg5TP6k5en9WzGr2EwaoGFXdwOu12FzCCwZgzr9yzht5oVfMYxt/4d4Z0mP6KDTu2NHcPOQcMUM1ZrBC1LJCF2rqCb7YxjkWtgCqHgJTeYg5FgFlzD0+mSKLF3eGrbcjGnHYybaXIwA+WcRgekeUOGiObucQNXvChgilBri6cGRsh7bG8hbOvWBXpEifrwsKFnaHNrgwcRvNAtpK+ErwY9eE0jPBs6OChdf7zBtXP3oxGsFBdmBoM/69Gf9aAHzY37MVx2298d7ouW1YqKV852SWlpPZ+4VhQZ3bq8PqK5bTIxrd3f3mzDB9qRzDKEwf8YwODXwUfN8o9WR4/XF75W7f/J/pu97/fTMv/dxrjH/j97+WyrZ/+fvXjx6P9/kWsDyOlNko0NOHv7zd7JN0lyfn6eSaFlgYl1RYFyJ0UBfd/z/Pyc+h2451zMk+RMNs1bVUfFavuzYwzPy+XI3zjfuX1U9w4otI3X43G2aF5QB/fiknauCkUsDg8p6FZk2jP3oipw9yTYss6WuxQc7OgWaJfhgoJr48apmGIlGlT2JzP0GvG07YY55LWyroGflwNN9HsneJeCdbgxzrFAgzRATC5oX81aQznfqW2/SiGFpbxEDWGdYpLIspIChdHAtJYZZyYc0tOuqKNyQR2ihXXz6ewCdOPOZFHIKzpKgE0LjOjW0NXejojovct4+bz3yVWzTpfOzUiS49ARPsBeG7DSL2qajEYj+ADNv8n52nc+zuEDrTY9hIV0JyBpwwzP3AlB1uujONVyE8nOEK4WPFtAIcmj5ALOaRvqORHNc1aT8PvG+j/WPSSv1EbE3VdcnDOYyWrpx6tFjqoBaSScr930em4HPnTUamB9ACEFduZq2DxM0rB5IPPHzHcd1PZ1hQDc3oHKvcHw+YP037norpOcrZn5OfU570JYP3vX2cH6AOdb6dbLdDJiRcUF9gA8aKI9eAezQ2mOFWoU5jw5j8tvAYi/R1XFYdAd581r9OdDOA91OtsletLCq/zDGB6ldiM2rGTeJdLrSQRBREMczKCHKdcREkMX+pAAduOXsHDx9loLcN/+Dlui4QP8/ItvQ1uuVxrSJu91zbvvBrUdrBRFeXXfZWXztO2wW2sjy55Kt4xo+VCGeOV87Xb88+4EV3c83zkAcXpVm0aq+3vnG/BfyP6v+n9vD3b3D0/3f8cx7vb/tl9uPevv/3z2bPLs0f/7Ehfcd72pWLZAeMszFBqTO1qGCHQ7nQzhv5iomVrC9mTy/NZO/miMq6urlNEwlLct3FB6TK9RnO2ffH8Kbw73YPfocO/g7ODo8BS+OzqBd6f7QzjZPz452nu3a28PqdXewenZycFf3tk7BGArtT4AvcwkhfUV3NgDP6MB6IX1gkpkTkUaVKUmXyOTIne96DCZWuPQBtdK5jV5f8NQfLPOENdG8WltfLzvonkK+U+dr6hhC8xCyXq+gP90loJryGVW0xv2PbykWkHM+gSKzxcG5JXV3lIBCsPNElhtFlLxf9B4YSPJmh7kmHINc8WE8ec6hZWNEMA5K2CfQK8gUQs7QW/nWEZQAhYit/6kByPNAj2CHINPLIVRshhSFs3/KAjpoZ2Nvev0okvYRy9wKlkEF5QZP2AK3/kjfqpaVVKjbqnaLHhYo4GHMqCpaHjKN71BvEI1hJwrzIxFggv399BqapcPNIvA9+4RUUCBKw/bxbPj6jpbeMSsQ4g0/enSYc8IdkyZK265SSp4yvmmWx694JWFNOMzs4QKVWZBP30x+fMmDSdVyLkGQLXRhgnnTVl3UAeIfBOmKHDGM86KLvQIz3bJf5L1AJ5KRX+pwWa86uSg5vyS57WFpSDmDw8Ar1FlXNNpoahKrmkPt+OzkPfiepXVTqkkMrDiVfY5rVI4Q2UDJ3o6I4pf2CFKmfOZPzBHhwV2VW/7eFobENLEaVotZ+bKsperwUAmcxw2sufiFAfGNRgG+e+b7xb1o+nfMTOrqDOxdPcU6rog+ZgpWUKJ2YIJnrEgIEYxoW1LFhiK7hT+5wwYOPIQuGF3gs1Grc40bejGrUBJQs5Pk2ptFMR1Jhxrr0wKn6skB8XJLlXSyCONpv2jVBcrSuFKqgvCmPSQ5bRWBLgI02gEwJHOT6tkeXQal5f/SC8NrTa1DJgxz0qs0QtBuwlpyHn26s1vgMjt2FatGCpl+Hy9w9aDeMoE4DUrqwJtx0rJS+472pZvqgpFzq9hioW82mypsIeKX7pTbi1B9KDPAXaM9TTws/eQHA0C4lNmHWgpSBRzO4blfiVLp6vsULRcVhZczNkqA8xtYGTFXeElp6UcxptThoAFm0oVfkkVljmWJg/MWjkKV4auHHG1kAUJRVOaXbPmq/o46KlZR/yH0Cefp57l5rB55YruE2EUlow38okVc7kCSxeaRokKiyUUXFwQ4aZcEJ8IVuJmWHQuDKoZy8hIDCMb2RB1BSlLHZSzdtVt1BFs/NoV78tAI7LReA0BQ3HA29IGDwussybEw7n3RJpX7xxtqJdUtyI/jITCWK0vqaweiFlPS2688gh+B3EXYU7oeVGggUL9outWhFUmc3entYgdFauVaXjL71NcsGIGcna78/Iwaw+DZk7h1AVn7xu1LGdAO1SVFDwb2lWYsoL4KGw1sM5HLcJJmFYKYqJjSyhLJ6NbYSH66+Gdpijax9WOIUWEE22bsJ0pRzaMTVbjCumlNljqWIVzrWu0JiQjG+lbuOW3ls9vZgu+Vkz0YaRGOlwQUdvSLec6qzVZeRqxJH3p3cgfSeO1pgmvAxG6cw38mEmhK57VstbFEkqmLqzqU613FFwu1HwuSPdzQWtEhF3LiVZZDQ6lAQaxrKaDVRHu+dfNtIME3uvyxAS0+rHsDQoLpmGKKEBhhqTJp8vOOK0QavytRmEKO2wmVSVVk3ONxM8pou0U/mrdKjvsbjP94FnBae2Mq+fVtcFMJGaxVkaWLSAiEFgVMl06L478gp9kDcx6eBWamhWB/a6kKvIrbn0NIcWIVl7zS/pJ+1jmNnCSS1aY5WimEIfAlcJLmVlFvmLNffxnBwzRFg6tO1hZPl7RdK06r+ppwbNiaRm1Kthy2N6pUDlTq+mOdyziuC128xtdTM7yyohrzDnpFrdAz6IFOmZW6f4brM5TvM6wMlbAtAnCSAj6SsgmVG6u0eqV7AKHsGCXSF5eQIjiaDmbWT9PgsaiGPp/eVlJZdzCNHrAO8reKyQ1E2ZmSeDWKIxKR2la0yCKpaOy1V0etaxgvNS+bTS56dIBianb6E2BGWrNFCfpnCku5k0lnwfbFwv+U70JrJACvUXMZDnlovHqXQGj1yFMKBRZiAGN9E5eFzk/xJVdimDrUjiY2fVvYiFtuLE83SyK4f67C2zO7GNScj5wf9oarMa3VlLrERHMTiOTtfWf3G8ugEHBrnTNjZ1qgXNnBJhpkG99gp5WvEvBkU1wiGsfardwsnZxlmFaYT1K8lTNAp0r1uXE4DKFYNRLSgg0WhnzJi94Vc46WBG1qxd4hTWVqZyZhvka6nJNcWLuVMHzFE4wzgylNHTJlq1m62uhTFY8+DYdfXSHl0dLYt1GzHldDh0fWY+Gm4VsLHI3bHYm/BZNNmxDISJIy1ol+tPC24peq7t2kiau2nQzrbWBucXXoufiDYUZrzjVF2PXt4kO7bUyUeYqYr1I4hsyo2HMaTSmS9y0rrSNo0L6PWPKspCSJReWT1z0GB9vQ6WpwNJ0JvSCkdjTxC2c7shZNLJCw7gYBr85CuEpOhDLlclFAzcDtgwxpBptYx2HnruHVi3maP2mYeRMEIuaVtz83FwKYg0+fZXa9dyc9gwwCLlckkNbobLTtOR0EqdMa7jAe/D9iXaJlm9apdWsvw/87FIPDo/ODnb3B2Dw2u1JtGLnx7AudzROLF2RClgjKSuUpfWKQIXQk9HxXRRjtkyHa8kayk0x+b1SI83gJkJTGD6ErhGY9RReS1diNmagQKZtOBVn6X2XVlppb5jeCWiygGNL65ZCHa7Sd+LwTazMO0wWy3U3AQV81uoZazLnrQVchS/VcJXKLPh6UZYr7MZcpdKsJynkQFyicotlFlzlIzvJZbM2QqqS9qGzqkKmmq0gVgT1Kpmj9SbnwYXSTZKPFVHwaj2ULjpetkhjLTu5+cZssDy3fysb78QcGUEJqHsKPUQSho76mucd1qF4igk7KIq8LoPb2uGYoFhc/BeWs6/TiMAhicGK9cJE2Sq/aUYbVff5zxHmtrrFWhK1UQW5rZSsdw5AL/EVLYUF4ucRoywV5Nx6rR0vd40H36b21pSMHJioViRna7AZtmIzo2BxeUsoEmfnGlEieHboKJvXIrBSrepY4cbrzmTpXGnLR520TBOp9CKBzoK8oGDHVwJcrNp6gTqFd6JArWnR8LoqeMZt+EsQowJJk99Y9r3IKJkVpbFuTV21nr4dsZ/Ica7eNM4+f0xo5t0sQjNiGAfCua55qD66/ofS2E5N9Ybsy1S6oMyK7ZzCO2tGCDVdV6g05ugKQVYMoiXxAznvwiVIDbYh0VyhY/yllxCKyPAas0jFk+JtCKJwzpSrK/VjD18LeJnCWXBAdOq+Cxf86FyS5jTO5Y4qQuGrB4S07R3KGKxEHXk0ethsYPE/pQLPw65xYNqA8bDNOvkwVeFvNffVI2vQtaQjjdyS0vYMppaEDRfg3nGa+qVogg4+56v52SBNYd28NVhjAhylXqWwxzWFTqhsqx+ZsnRZNkLQoDpdhm9B0B45dtWqAVpFCl7aLNiwXTAv+7pF9anFFVm26IeocWtudHdxN0FSxW/w5hQOTgfwlzenB6eBuD8enP3t6N0Z/Pjm5OTN4dnB/ikcncRl+aPv4M3hT/DfB4d7Q0DuKsDXlbKTbGbCSa/kUZq0lSDKk7Kgp5Zw5UhFAZFaVbFyBmcHZ2/3h3B4dDg6OPzu5ODwr/vf7x+eDeH7/ZPdv705PHvzl4O3B2c/EQt9d3B2uH/qtg+88TCO35ycHey+e/vmBI7fnRwfne47a+uqhQUWNlbTlRSaU9WBKjMuKuyyC6sqJSvFrXtOE55BTblS4r9W40b5Updt1Lqm9wWCSCuuL1b3XpJS93VWysbGhdbVYNbx3usU3jYktZ3ecjblBRXPD6zlBby0vGvxcDCEhIKSnWaBUi2jVEuoZBmpTJwyEDgv+BxFhpvDpto97KRym8zPvfz+1DkKGnIs+JQcOkJurqTWTd0iDGmAZUZTdXy9fDjt2TEfUsE0LFnBaWCfEaClZSWbd3P4tnfYEtBuDqAdnG2SjYuM59axdaUE68C4nC5nRQAaNHS2YJZEqIApVzO3Vryx1bouTD/QJWrWjY6p3R0u/GJGejXOGDy9syYesLLTLqRj2LmU+RUv4tzhBWgjq4rNcUg+QW0R96fwul0QxawWrXNDRnDNTpBMlqVl3pgebmDUm0PiQ9oZ20vEeRhNMp3ll5yKpDO/fUNr7okQNjd48E4C/jOFN5m1CZYKQfPakd+0hjoSih8X1nXvimu/WHhnuS14odlCSpcFpUxnp9hOOVf6WhXpkyEwwpCJDN0kKpcG9dpvSXyHpeCmkcemelsE3EFOC5+FIr9lbNWO9XxdqYVrMlI+vuK6U+7BFP4mr5DevbVBVUMwomcEuJ0f7WgRRVQNaXxuXxahJK6/bRVpq0YJX/J02ipKq9HbTFHEBj4nbGMmPnP62Qq8k3eizayhTY4zFLnrQUdEr6bOmSpJEwXnuqFiK861Um21zGeOmdaorPj4JOpwNW88XXpno52Q+8ZTQ9PGmb+KuDFyGxtcHAPvH+5Zu7puGxw9f3N8vH+4d/C/duwSUragqoql374Qb92zzwiVq6aWBABnD+ww9NsoutmE4FZLXqByJ/S6aG7YRvL+xUkUWSH9S3BTxbILNBoGP/8yaIOUgmXB2i0DM5FW9VFfFEmn8HRPiifNfoFIRgPw/9gEt8/bhql6Iesity5+g4ePDiKzHdVmrazopTDsuimEUlDvEEjhRwRWaAkKXWufJw1anNo6vtG6fR8wepWeLLgvrU6x3bLiXlEJpUHbcUDv/mEOVgcPrK3oVj795heLJjLNm3q8p1youzbpmTbJwVS24JdBU7bFxJ+Xy+XyF/g5vOXbq7L+Qs09k+RRzNRln2G8IRSe2gbNnsvNbyyIEI9YReDMl0+fBzeeCx+GkmpsOKpxcaKoX04pW8Y6KbvAyMwEdr9vy6nf/DzaTifU5SEe+m2+h99zlsRZyg69Anpcdxrc5oF/pvsdHG8i2yliB4XA5P7FlAwKJuY1myPM5SUq0d/Z57Mlrb+uV+eVPr5N+v/+tbr/379T9TseAHPf+Q8vX/XPf3z+/MXj+Q9f5Iq/VLUDW0nijp1KADboOwXuLzLP/tWrcJyJu2/YnE6KaV+Y8g+q6Bs38QtQ4RN+7tyrdWBboK/SFy3QO0Am8TkDOzAYJP3zDehm4pNK7ZFm/oRFd5Zj805VEr6r8nqSJP7IXtvHH4q9AzNW0P6k+Oyv8PmGDegfPObOEyZXIJ5kv6Ep9IhldNCaUTVav8gdJQw//5JAfHjyyH/9o5BuN7EpQqMN+nxUdCiy+6qTKbRflRbMhrOHXVhJ/NJWA7Pz5QbftfPZimTlAxrr+wYsHvABjw3/FZ0jUSx3wBLEj9J9/WtlnFyOtCyRcqgezMpBahvrvsPU49GN7mFruXwyhCcN5Ce/JMnqN37cCc6DsV26td/aeZGsfDLnWbLu+zcvk5UvLX0a8KT9Io5j0A1nswML+M9z0fe5NqLPeG2/pu94bXQ+93Vf+2TlZTsadGPlo50bzg+D9wlxoTv2KfwC2viIAl5PvmnuSO/FjttWAEpKs56Bmo437g/6L/Dp6it7AU3/WnEH0S+DXtL5OAjJVPx1DcvlSfNVD/v4j7Ybj9fj9Xj961//NwAA//+EFJZ8AIwAAA==",
      "value_data": "replicaCount: 1\n\nimage:\n  # html:\n  #   repository: nginx\n  #   tag: 1.16.0-alpine\n  #   pullPolicy: IfNotPresent\n  nginx:\n    repository: nginx\n    tag: 1.17.5-alpine\n    pullPolicy: IfNotPresent\n\nnameOverride: \"\"\nfullnameOverride: \"\"\n\nservice:\n  name: http\n  type: ClusterIP\n  port: 80\n\ningress:\n  enabled: false\n  annotations: {}\n    # kubernetes.io/ingress.class: nginx\n    # kubernetes.io/tls-acme: \"true\"\n  paths: []\n  hosts:\n    - nginx.local\n  tls: []\n  #  - secretName: nginx-tls\n  #    hosts:\n  #      - nginx.local\n\nextraVolumes: []\n  # - name: extra\n  #   emptyDir: {}\n\nextraVolumeMounts: []\n  # - name: extras\n  #   mountPath: /usr/share/nginx/html\n  #   readOnly: true\n\nextraInitContainers: []\n  # - name: do-something\n  #   image: busybox\n  #   imagePullPolicy: IfNotPresent\n  #   command: ['do', 'something']\n\nreadinessProbe:\n  path: \"/\"\n  initialDelaySeconds: 5\n  periodSeconds: 3\n  failureThreshold: 6\nlivenessProbe:\n  path: \"/\"\n  initialDelaySeconds: 5\n  periodSeconds: 3\n\nresources: {}\n  # limits:\n  #  cpu: 100m\n  #  memory: 128Mi\n  # requests:\n  #  cpu: 100m\n  #  memory: 128Mi\n\nconfigurationFile: {}\n#  nginx.conf: |-\n#  http {\n#    server {\n#      listen 80;\n#      location / {\n#        root /usr/share/nginx/html;\n#      }\n#    }\n#  }\n\nextraConfigurationFiles: {}\n#  default.conf: |-\n#    server {\n#      listen 80;\n#      location / {\n#        root /usr/share/nginx/html;\n#      }\n#    }\n\nnodeSelector: {}\n\ntolerations: []\n\naffinity: {}\n",
      "template": {
        "tenant": "",
        "workspace": "aaa",
        "name": "nginx",
        "uuid": "89dc65d5-bf9a-48e9-83c4-8bede60a0879",
        "type": "helm",
        "create_time": 1629862731,
        "creator": "",
        "description": "nginx is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server, originally written by Igor Sysoev.",
        "status": "on_shelves",
        "status_time": 1629862765,
        "update_time": 1629862765,
        "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Nginx_logo.svg/500px-Nginx_logo.svg.png",
        "keywords": null,
        "home": "",
        "tags": "",
        "category_set": null,
        "latest_version": null,
        "version_num": 0,
        "instance_num": 0
      },
      "template_version": {
        "tenant": "",
        "workspace": "aaa",
        "type": "",
        "uuid": "6b712caf-556f-48f7-9952-cc3da93b6553",
        "name": "1.2.0 [1.17.5]",
        "template_uuid": "89dc65d5-bf9a-48e9-83c4-8bede60a0879",
        "create_time": 1629862731,
        "update_time": 1629862765,
        "description": "nginx is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server, originally written by Igor Sysoev.",
        "state_operator": "",
        "status": "on_shelves",
        "status_time": 1629862765,
        "package_name": "nginx",
        "package_version": "1.2.0"
      }
    }
  }
}

```



## /v1/topke/app_template/instance/workloads
应用实例工作负载详情
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群uuid
namespace|string|是|""|命名空间
workspace|string|是|""|工作区
uuid|string|是|""|实例uuid
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/instance/workloads
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"namespace": "aaa",
	"workspace": "aaa",
	"uuid": "98ac9d28-612a-45da-b258-149767ed8bb3"
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "data": {
      "uuid": "98ac9d28-612a-45da-b258-149767ed8bb3",
      "topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
      "namespace": "aaa",
      "tenant": "",
      "state": "active",
      "name": "nginx-ylnsxn",
      "config": null,
      "info": null,
      "version": 1,
      "create_time": 1629871381,
      "update_time": 1629871381,
      "package_data": "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",
      "template": {
        "tenant": "",
        "workspace": "aaa",
        "name": "nginx",
        "uuid": "89dc65d5-bf9a-48e9-83c4-8bede60a0879",
        "type": "helm",
        "create_time": 1629862731,
        "creator": "",
        "description": "nginx is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server, originally written by Igor Sysoev.",
        "status": "on_shelves",
        "status_time": 1629862765,
        "update_time": 1629862765,
        "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Nginx_logo.svg/500px-Nginx_logo.svg.png",
        "keywords": null,
        "home": "",
        "tags": "",
        "category_set": null,
        "latest_version": null,
        "version_num": 0,
        "instance_num": 0
      },
      "template_version": {
        "tenant": "",
        "workspace": "aaa",
        "type": "",
        "uuid": "6b712caf-556f-48f7-9952-cc3da93b6553",
        "name": "1.2.0 [1.17.5]",
        "template_uuid": "89dc65d5-bf9a-48e9-83c4-8bede60a0879",
        "create_time": 1629862731,
        "update_time": 1629862765,
        "description": "nginx is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server, originally written by Igor Sysoev.",
        "state_operator": "",
        "status": "on_shelves",
        "status_time": 1629862765,
        "package_name": "nginx",
        "package_version": "1.2.0"
      },
      "workloads": [
        {
          "apiVersion": "apps/v1",
          "kind": "Deployment",
          "metadata": {
            "annotations": {
              "deployment.kubernetes.io/revision": "1",
              "meta.helm.sh/release-name": "nginx-ylnsxn",
              "meta.helm.sh/release-namespace": "aaa"
            },
            "creationTimestamp": "2021-08-25T06:03:30Z",
            "generation": 1,
            "labels": {
              "app.kubernetes.io/instance": "nginx-ylnsxn",
              "app.kubernetes.io/managed-by": "Helm",
              "app.kubernetes.io/name": "nginx",
              "helm.sh/chart": "nginx-1.2.0"
            },
            "managedFields": [
              {
                "apiVersion": "apps/v1",
                "fieldsType": "FieldsV1",
                "fieldsV1": {
                  "f:metadata": {
                    "f:annotations": {
                      ".": {},
                      "f:meta.helm.sh/release-name": {},
                      "f:meta.helm.sh/release-namespace": {}
                    },
                    "f:labels": {
                      ".": {},
                      "f:app.kubernetes.io/instance": {},
                      "f:app.kubernetes.io/managed-by": {},
                      "f:app.kubernetes.io/name": {},
                      "f:helm.sh/chart": {}
                    }
                  },
                  "f:spec": {
                    "f:progressDeadlineSeconds": {},
                    "f:replicas": {},
                    "f:revisionHistoryLimit": {},
                    "f:selector": {
                      "f:matchLabels": {
                        ".": {},
                        "f:app.kubernetes.io/instance": {},
                        "f:app.kubernetes.io/name": {}
                      }
                    },
                    "f:strategy": {
                      "f:rollingUpdate": {
                        ".": {},
                        "f:maxSurge": {},
                        "f:maxUnavailable": {}
                      },
                      "f:type": {}
                    },
                    "f:template": {
                      "f:metadata": {
                        "f:labels": {
                          ".": {},
                          "f:app.kubernetes.io/instance": {},
                          "f:app.kubernetes.io/name": {}
                        }
                      },
                      "f:spec": {
                        "f:containers": {
                          "k:{\"name\":\"nginx\"}": {
                            ".": {},
                            "f:image": {},
                            "f:imagePullPolicy": {},
                            "f:livenessProbe": {
                              ".": {},
                              "f:failureThreshold": {},
                              "f:httpGet": {
                                ".": {},
                                "f:path": {},
                                "f:port": {},
                                "f:scheme": {}
                              },
                              "f:initialDelaySeconds": {},
                              "f:periodSeconds": {},
                              "f:successThreshold": {},
                              "f:timeoutSeconds": {}
                            },
                            "f:name": {},
                            "f:ports": {
                              ".": {},
                              "k:{\"containerPort\":80,\"protocol\":\"TCP\"}": {
                                ".": {},
                                "f:containerPort": {},
                                "f:name": {},
                                "f:protocol": {}
                              }
                            },
                            "f:readinessProbe": {
                              ".": {},
                              "f:failureThreshold": {},
                              "f:httpGet": {
                                ".": {},
                                "f:path": {},
                                "f:port": {},
                                "f:scheme": {}
                              },
                              "f:initialDelaySeconds": {},
                              "f:periodSeconds": {},
                              "f:successThreshold": {},
                              "f:timeoutSeconds": {}
                            },
                            "f:resources": {},
                            "f:terminationMessagePath": {},
                            "f:terminationMessagePolicy": {}
                          }
                        },
                        "f:dnsPolicy": {},
                        "f:restartPolicy": {},
                        "f:schedulerName": {},
                        "f:securityContext": {},
                        "f:terminationGracePeriodSeconds": {},
                        "f:volumes": {
                          ".": {},
                          "k:{\"name\":\"html\"}": {
                            ".": {},
                            "f:emptyDir": {},
                            "f:name": {}
                          }
                        }
                      }
                    }
                  }
                },
                "manager": "Go-http-client",
                "operation": "Update",
                "time": "2021-08-25T06:03:30Z"
              },
              {
                "apiVersion": "apps/v1",
                "fieldsType": "FieldsV1",
                "fieldsV1": {
                  "f:metadata": {
                    "f:annotations": {
                      "f:deployment.kubernetes.io/revision": {}
                    }
                  },
                  "f:status": {
                    "f:availableReplicas": {},
                    "f:conditions": {
                      ".": {},
                      "k:{\"type\":\"Available\"}": {
                        ".": {},
                        "f:lastTransitionTime": {},
                        "f:lastUpdateTime": {},
                        "f:message": {},
                        "f:reason": {},
                        "f:status": {},
                        "f:type": {}
                      },
                      "k:{\"type\":\"Progressing\"}": {
                        ".": {},
                        "f:lastTransitionTime": {},
                        "f:lastUpdateTime": {},
                        "f:message": {},
                        "f:reason": {},
                        "f:status": {},
                        "f:type": {}
                      }
                    },
                    "f:observedGeneration": {},
                    "f:readyReplicas": {},
                    "f:replicas": {},
                    "f:updatedReplicas": {}
                  }
                },
                "manager": "kube-controller-manager",
                "operation": "Update",
                "time": "2021-08-25T06:03:48Z"
              }
            ],
            "name": "nginx-ylnsxn",
            "namespace": "aaa",
            "resourceVersion": "12664607",
            "selfLink": "/apis/apps/v1/namespaces/aaa/deployments/nginx-ylnsxn",
            "uid": "ba5af6a0-5579-42ef-a6f0-08077026be29"
          },
          "spec": {
            "progressDeadlineSeconds": 600,
            "replicas": 1,
            "revisionHistoryLimit": 10,
            "selector": {
              "matchLabels": {
                "app.kubernetes.io/instance": "nginx-ylnsxn",
                "app.kubernetes.io/name": "nginx"
              }
            },
            "strategy": {
              "rollingUpdate": {
                "maxSurge": "25%",
                "maxUnavailable": "25%"
              },
              "type": "RollingUpdate"
            },
            "template": {
              "metadata": {
                "creationTimestamp": null,
                "labels": {
                  "app.kubernetes.io/instance": "nginx-ylnsxn",
                  "app.kubernetes.io/name": "nginx"
                }
              },
              "spec": {
                "containers": [
                  {
                    "image": "nginx:1.17.5-alpine",
                    "imagePullPolicy": "IfNotPresent",
                    "livenessProbe": {
                      "failureThreshold": 3,
                      "httpGet": {
                        "path": "/",
                        "port": 80,
                        "scheme": "HTTP"
                      },
                      "initialDelaySeconds": 5,
                      "periodSeconds": 3,
                      "successThreshold": 1,
                      "timeoutSeconds": 1
                    },
                    "name": "nginx",
                    "ports": [
                      {
                        "containerPort": 80,
                        "name": "http",
                        "protocol": "TCP"
                      }
                    ],
                    "readinessProbe": {
                      "failureThreshold": 6,
                      "httpGet": {
                        "path": "/",
                        "port": 80,
                        "scheme": "HTTP"
                      },
                      "initialDelaySeconds": 5,
                      "periodSeconds": 3,
                      "successThreshold": 1,
                      "timeoutSeconds": 1
                    },
                    "resources": {},
                    "terminationMessagePath": "/dev/termination-log",
                    "terminationMessagePolicy": "File"
                  }
                ],
                "dnsPolicy": "ClusterFirst",
                "restartPolicy": "Always",
                "schedulerName": "default-scheduler",
                "securityContext": {},
                "terminationGracePeriodSeconds": 30,
                "volumes": [
                  {
                    "emptyDir": {},
                    "name": "html"
                  }
                ]
              }
            }
          },
          "status": {
            "availableReplicas": 1,
            "conditions": [
              {
                "lastTransitionTime": "2021-08-25T06:03:52Z",
                "lastUpdateTime": "2021-08-25T06:03:52Z",
                "message": "Deployment has minimum availability.",
                "reason": "MinimumReplicasAvailable",
                "status": "True",
                "type": "Available"
              },
              {
                "lastTransitionTime": "2021-08-25T06:03:30Z",
                "lastUpdateTime": "2021-08-25T06:03:52Z",
                "message": "ReplicaSet \"nginx-ylnsxn-54dbcf9c97\" has successfully progressed.",
                "reason": "NewReplicaSetAvailable",
                "status": "True",
                "type": "Progressing"
              }
            ],
            "observedGeneration": 1,
            "readyReplicas": 1,
            "replicas": 1,
            "updatedReplicas": 1
          }
        },
        {
          "apiVersion": "v1",
          "kind": "Service",
          "metadata": {
            "annotations": {
              "meta.helm.sh/release-name": "nginx-ylnsxn",
              "meta.helm.sh/release-namespace": "aaa"
            },
            "creationTimestamp": "2021-08-25T06:03:30Z",
            "labels": {
              "app.kubernetes.io/instance": "nginx-ylnsxn",
              "app.kubernetes.io/managed-by": "Helm",
              "app.kubernetes.io/name": "nginx",
              "helm.sh/chart": "nginx-1.2.0"
            },
            "managedFields": [
              {
                "apiVersion": "v1",
                "fieldsType": "FieldsV1",
                "fieldsV1": {
                  "f:metadata": {
                    "f:annotations": {
                      ".": {},
                      "f:meta.helm.sh/release-name": {},
                      "f:meta.helm.sh/release-namespace": {}
                    },
                    "f:labels": {
                      ".": {},
                      "f:app.kubernetes.io/instance": {},
                      "f:app.kubernetes.io/managed-by": {},
                      "f:app.kubernetes.io/name": {},
                      "f:helm.sh/chart": {}
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
                      "f:app.kubernetes.io/instance": {},
                      "f:app.kubernetes.io/name": {}
                    },
                    "f:sessionAffinity": {},
                    "f:type": {}
                  }
                },
                "manager": "Go-http-client",
                "operation": "Update",
                "time": "2021-08-25T06:03:30Z"
              }
            ],
            "name": "nginx-ylnsxn",
            "namespace": "aaa",
            "resourceVersion": "12664463",
            "selfLink": "/api/v1/namespaces/aaa/services/nginx-ylnsxn",
            "uid": "c679be7e-b2c7-47cd-b16b-c7651badb6b0"
          },
          "spec": {
            "clusterIP": "10.98.61.3",
            "ports": [
              {
                "name": "http",
                "port": 80,
                "protocol": "TCP",
                "targetPort": "http"
              }
            ],
            "selector": {
              "app.kubernetes.io/instance": "nginx-ylnsxn",
              "app.kubernetes.io/name": "nginx"
            },
            "sessionAffinity": "None",
            "type": "ClusterIP"
          },
          "status": {
            "loadBalancer": {}
          }
        }
      ]
    }
  }
}

```

## /v1/topke/app_template/instance/create
应用实例创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群uuid
namespace|string|是|""|命名空间
template|string|是|""|模板uuid
version|string|是|""|版本uuid
values_data|string|是|""|模板值
description|string|否|""|描述
name|string|是|""|实例名
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/instance/create
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"namespace": "aaa",
	"template": "89dc65d5-bf9a-48e9-83c4-8bede60a0879",
	"version": "6b712caf-556f-48f7-9952-cc3da93b6553",
	"values_data": "replicaCount: 1\n\nimage:\n  # html:\n  #   repository: nginx\n  #   tag: 1.16.0-alpine\n  #   pullPolicy: IfNotPresent\n  nginx:\n    repository: nginx\n    tag: 1.17.5-alpine\n    pullPolicy: IfNotPresent\n\nnameOverride: \"\"\nfullnameOverride: \"\"\n\nservice:\n  name: http\n  type: ClusterIP\n  port: 80\n\ningress:\n  enabled: false\n  annotations: {}\n    # kubernetes.io/ingress.class: nginx\n    # kubernetes.io/tls-acme: \"true\"\n  paths: []\n  hosts:\n    - nginx.local\n  tls: []\n  #  - secretName: nginx-tls\n  #    hosts:\n  #      - nginx.local\n\nextraVolumes: []\n  # - name: extra\n  #   emptyDir: {}\n\nextraVolumeMounts: []\n  # - name: extras\n  #   mountPath: /usr/share/nginx/html\n  #   readOnly: true\n\nextraInitContainers: []\n  # - name: do-something\n  #   image: busybox\n  #   imagePullPolicy: IfNotPresent\n  #   command: ['do', 'something']\n\nreadinessProbe:\n  path: \"/\"\n  initialDelaySeconds: 5\n  periodSeconds: 3\n  failureThreshold: 6\nlivenessProbe:\n  path: \"/\"\n  initialDelaySeconds: 5\n  periodSeconds: 3\n\nresources: {}\n  # limits:\n  #  cpu: 100m\n  #  memory: 128Mi\n  # requests:\n  #  cpu: 100m\n  #  memory: 128Mi\n\nconfigurationFile: {}\n#  nginx.conf: |-\n#  http {\n#    server {\n#      listen 80;\n#      location / {\n#        root /usr/share/nginx/html;\n#      }\n#    }\n#  }\n\nextraConfigurationFiles: {}\n#  default.conf: |-\n#    server {\n#      listen 80;\n#      location / {\n#        root /usr/share/nginx/html;\n#      }\n#    }\n\nnodeSelector: {}\n\ntolerations: []\n\naffinity: {}\n",
	"description": "",
	"name": "nginx-ylnsxn"
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "data": {
      "uuid": "98ac9d28-612a-45da-b258-149767ed8bb3",
      "topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
      "namespace": "aaa",
      "tenant": "",
      "state": "active",
      "name": "nginx-ylnsxn",
      "config": null,
      "info": null,
      "version": 1,
      "create_time": 1629871381,
      "update_time": 1629871381,
      "package_data": "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",
      "template": {
        "tenant": "",
        "workspace": "aaa",
        "name": "nginx",
        "uuid": "89dc65d5-bf9a-48e9-83c4-8bede60a0879",
        "type": "helm",
        "create_time": 1629862731,
        "creator": "",
        "description": "nginx is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server, originally written by Igor Sysoev.",
        "status": "on_shelves",
        "status_time": 1629862765,
        "update_time": 1629862765,
        "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Nginx_logo.svg/500px-Nginx_logo.svg.png",
        "keywords": null,
        "home": "",
        "tags": "",
        "category_set": null,
        "latest_version": null,
        "version_num": 0,
        "instance_num": 0
      },
      "template_version": {
        "tenant": "",
        "workspace": "aaa",
        "type": "",
        "uuid": "6b712caf-556f-48f7-9952-cc3da93b6553",
        "name": "1.2.0 [1.17.5]",
        "template_uuid": "89dc65d5-bf9a-48e9-83c4-8bede60a0879",
        "create_time": 1629862731,
        "update_time": 1629862765,
        "description": "nginx is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server, originally written by Igor Sysoev.",
        "state_operator": "",
        "status": "on_shelves",
        "status_time": 1629862765,
        "package_name": "nginx",
        "package_version": "1.2.0"
      }
    }
  }
}
```
## /v1/topke/app_template/instance/delete
应用实例删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
topke_cluster_uuid|string|是|""|集群uuid
namespace|string|是|""|命名空间
workspace|string|是|""|工作区
uuid|string|是|""|实例uuid
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
http://10.30.100.117:8080/v1/topke/app_template/instance/delete
```
{
	"topke_cluster_uuid": "9ff0b9f0-4937-4470-8088-9d783cb9cd0c",
	"namespace": "aaa",
	"workspace": "aaa",
	"uuid": "98ac9d28-612a-45da-b258-149767ed8bb3"
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
    "code": 0,
    "message": "",
    "messageCn": "",
    "stack": null,
    "desc": "",
    "UUID": "",
    "data": null
  }
}
```