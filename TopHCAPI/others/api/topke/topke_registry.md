[back to api overview](../api_overview.md#topke_registry)

### 容器云镜像仓库接口
## /v1/container_registry/dockerhub/repository/search
从docker hub搜索镜像
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
page_num|int|否|0| 页数
page_size|int|否|0|页大小
sort|string|否|""|排序
q|string|否|""|搜索
type|string|否|""|搜索类型，'image'
architecture|string|否|""|架构，'amd64'
operating_system|string|否|""|操作系统, "os"
image_filter|string|否|""|镜像过滤
source|string|否|""|来源,'community'

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/dockerhub/repository/search?page_size=25&q=nginx&type=image

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "count": 87182,
    "next": "https://store.docker.com/api/content/v1/products/search/?q=nginx\u0026type=image\u0026page=2\u0026page_size=25",
    "page": 1,
    "page_size": 25,
    "previous": "",
    "summaries": [
      {
        "architectures": [
          {
            "label": "IBM Z",
            "name": "s390x"
          },
          {
            "label": "x86-64",
            "name": "amd64"
          },
          {
            "label": "mips64le",
            "name": "mips64le"
          },
          {
            "label": "386",
            "name": "386"
          },
          {
            "label": "ARM 64",
            "name": "arm64"
          },
          {
            "label": "ARM",
            "name": "arm"
          },
          {
            "label": "PowerPC 64 LE",
            "name": "ppc64le"
          }
        ],
        "certification_status": "not_certified",
        "created_at": "2017-04-19T13:50:01.539699Z",
        "filter_type": "official",
        "id": "",
        "logo_url": {
          "large": "https://d1q6f0aelx0por.cloudfront.net/product-logos/library-nginx-logo.png"
        },
        "name": "nginx",
        "operating_systems": [
          {
            "label": "Linux",
            "name": "linux"
          }
        ],
        "popularity": 0,
        "publisher": {
          "id": "docker",
          "name": "Docker"
        },
        "short_description": "Official build of Nginx.",
        "slug": "nginx",
        "source": "store",
        "pull_count": "10M+",
        "star_count": 15358,
        "type": "image",
        "updated_at": "2021-08-23T23:18:51.028247Z",
        "update_time": 0,
        "create_time": 0
      },
      {
        "architectures": [
          {
            "label": "x86-64",
            "name": "amd64"
          }
        ],
        "certification_status": "not_certified",
        "created_at": "2018-08-23T10:55:17.524285Z",
        "filter_type": "verified_publisher",
        "id": "",
        "logo_url": {
          "large": "https://secure.gravatar.com/avatar/b6d982581a58a6a39d12c5d5355dde23.jpg?s=80\u0026r=g\u0026d=mm"
        },
        "name": "bitnami/nginx-ingress-controller",
        "operating_systems": [
          {
            "label": "Linux",
            "name": "linux"
          }
        ],
        "popularity": 0,
        "publisher": {
          "id": "d028386af9cc44c28214360d7c682d8a",
          "name": "bitnami"
        },
        "short_description": "Bitnami Docker Image for NGINX Ingress Controller",
        "slug": "bitnami/nginx-ingress-controller",
        "source": "verified_publisher",
        "pull_count": "",
        "star_count": 0,
        "type": "image",
        "updated_at": "2021-08-23T12:31:09.410366Z",
        "update_time": 0,
        "create_time": 0
      },
    ]
  }
}
```


## /v1/container_registry/dockerhub/repository/get
获取docker hub镜像详情
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
repo|string|是|""|搜索镜像
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/dockerhub/repository/get?repo=ubuntu

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "user": "library",
    "name": "ubuntu",
    "namespace": "library",
    "repository_type": "image",
    "status": 1,
    "description": "Ubuntu is a Debian-based Linux operating system based on free software.",
    "is_private": false,
    "is_automated": false,
    "can_edit": false,
    "star_count": 12671,
    "pull_count": 4556520888,
    "last_updated": "2021-07-27T00:06:01.621456Z",
    "is_migrated": false,
    "has_starred": false,
    "full_description": "# Quick reference\n\n-\t**Maintained by**:  \n\t[Canonical](https://partner-images.canonical.com/core/) and [Tianon (Debian Developer)](https://github.com/tianon/docker-brew-ubuntu-core)\n\n-\t**Where to get help**:  \n\t[the Docker Community Forums](https://forums.docker.com/), [the Docker Community Slack](https://dockr.ly/slack), or [Stack Overflow](https://stackoverflow.com/search?tab=newest\u0026q=docker)\n\n# Supported tags and respective `Dockerfile` links\n\n-\t[`18.04`, `bionic-20210723`, `bionic`](https://github.com/tianon/docker-brew-ubuntu-core/blob/a967c2b8734c77f7f89449d0b87c2e1eebf8b26e/bionic/Dockerfile)\n-\t[`20.04`, `focal-20210723`, `focal`, `latest`](https://github.com/tianon/docker-brew-ubuntu-core/blob/a967c2b8734c77f7f89449d0b87c2e1eebf8b26e/focal/Dockerfile)\n-\t[`21.04`, `hirsute-20210723`, `hirsute`, `rolling`](https://github.com/tianon/docker-brew-ubuntu-core/blob/a967c2b8734c77f7f89449d0b87c2e1eebf8b26e/hirsute/Dockerfile)\n-\t[`21.10`, `impish-20210722`, `impish`, `devel`](https://github.com/tianon/docker-brew-ubuntu-core/blob/a967c2b8734c77f7f89449d0b87c2e1eebf8b26e/impish/Dockerfile)\n-\t[`14.04`, `trusty-20191217`, `trusty`](https://github.com/tianon/docker-brew-ubuntu-core/blob/a967c2b8734c77f7f89449d0b87c2e1eebf8b26e/trusty/Dockerfile)\n-\t[`16.04`, `xenial-20210722`, `xenial`](https://github.com/tianon/docker-brew-ubuntu-core/blob/a967c2b8734c77f7f89449d0b87c2e1eebf8b26e/xenial/Dockerfile)\n\n# Quick reference (cont.)\n\n-\t**Where to file issues**:  \n\t[the cloud-images bug tracker](https://bugs.launchpad.net/cloud-images) (include the `docker` tag)\n\n-\t**Supported architectures**: ([more info](https://github.com/docker-library/official-images#architectures-other-than-amd64))  \n\t[`amd64`](https://hub.docker.com/r/amd64/ubuntu/), [`arm32v7`](https://hub.docker.com/r/arm32v7/ubuntu/), [`arm64v8`](https://hub.docker.com/r/arm64v8/ubuntu/), [`i386`](https://hub.docker.com/r/i386/ubuntu/), [`ppc64le`](https://hub.docker.com/r/ppc64le/ubuntu/), [`riscv64`](https://hub.docker.com/r/riscv64/ubuntu/), [`s390x`](https://hub.docker.com/r/s390x/ubuntu/)\n\n-\t**Published image artifact details**:  \n\t[repo-info repo's `repos/ubuntu/` directory](https://github.com/docker-library/repo-info/blob/master/repos/ubuntu) ([history](https://github.com/docker-library/repo-info/commits/master/repos/ubuntu))  \n\t(image metadata, transfer size, etc)\n\n-\t**Image updates**:  \n\t[official-images repo's `library/ubuntu` label](https://github.com/docker-library/official-images/issues?q=label%3Alibrary%2Fubuntu)  \n\t[official-images repo's `library/ubuntu` file](https://github.com/docker-library/official-images/blob/master/library/ubuntu) ([history](https://github.com/docker-library/official-images/commits/master/library/ubuntu))\n\n-\t**Source of this description**:  \n\t[docs repo's `ubuntu/` directory](https://github.com/docker-library/docs/tree/master/ubuntu) ([history](https://github.com/docker-library/docs/commits/master/ubuntu))\n\n# What is Ubuntu?\n\nUbuntu is a Debian-based Linux operating system that runs from the desktop to the cloud, to all your internet connected things. It is the world's most popular operating system across public clouds and OpenStack clouds. It is the number one platform for containers; from Docker to Kubernetes to LXD, Ubuntu can run your containers at scale. Fast, secure and simple, Ubuntu powers millions of PCs worldwide.\n\nDevelopment of Ubuntu is led by Canonical Ltd. Canonical generates revenue through the sale of technical support and other services related to Ubuntu. The Ubuntu project is publicly committed to the principles of open-source software development; people are encouraged to use free software, study how it works, improve upon it, and distribute it.\n\n\u003e [wikipedia.org/wiki/Ubuntu](https://en.wikipedia.org/wiki/Ubuntu)\n\n![logo](https://raw.githubusercontent.com/docker-library/docs/01c12653951b2fe592c1f93a13b4e289ada0e3a1/ubuntu/logo.png)\n\n# What's in this image?\n\nThis image is built from official rootfs tarballs provided by Canonical (specifically, https://partner-images.canonical.com/core/).\n\nThe `ubuntu:latest` tag points to the \"latest LTS\", since that's the version recommended for general use. The `ubuntu:rolling` tag points to the latest release (regardless of LTS status).\n\nAlong a similar vein, the `ubuntu:devel` tag is an alias for whichever release the \"devel\" suite on the mirrors currently points to, as determined by the following one-liner: `wget -qO- http://archive.ubuntu.com/ubuntu/dists/devel/Release | awk -F ': ' '$1 == \"Codename\" { print $2; exit }'`\n\n## Locales\n\nGiven that it is a minimal install of Ubuntu, this image only includes the `C`, `C.UTF-8`, and `POSIX` locales by default. For most uses requiring a UTF-8 locale, `C.UTF-8` is likely sufficient (`-e LANG=C.UTF-8` or `ENV LANG C.UTF-8`).\n\nFor uses where that is not sufficient, other locales can be installed/generated via the `locales` package. [PostgreSQL has a good example of doing so](https://github.com/docker-library/postgres/blob/69bc540ecfffecce72d49fa7e4a46680350037f9/9.6/Dockerfile#L21-L24), copied below:\n\n```dockerfile\nRUN apt-get update \u0026\u0026 apt-get install -y locales \u0026\u0026 rm -rf /var/lib/apt/lists/* \\\n\t\u0026\u0026 localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8\nENV LANG en_US.utf8\n```\n\n# License\n\nView [license information](https://www.ubuntu.com/about/about-ubuntu/licensing) for the software contained in this image.\n\nAs with all Docker images, these likely also contain other software which may be under other licenses (such as Bash, etc from the base distribution, along with any direct or indirect dependencies of the primary software being contained).\n\nSome additional license information which was able to be auto-detected might be found in [the `repo-info` repository's `ubuntu/` directory](https://github.com/docker-library/repo-info/tree/master/repos/ubuntu).\n\nAs for any pre-built image usage, it is the image user's responsibility to ensure that any use of this image complies with any relevant licenses for all software contained within.",
    "affiliation": null,
    "permissions": {
      "read": true,
      "write": false,
      "admin": false
    }
  }
}
```

## /v1/container_registry/dockerhub/repository/tags
获取docker hub镜像标签列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
repo|string|是|""|镜像

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/dockerhub/repository/tags?repo=ubuntu

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "count": 453,
    "next": "https://hub.docker.com/v2/repositories/library/ubuntu/tags?page=2\u0026page_size=20\u0026repo=library%2Fubuntu",
    "previous": null,
    "results": [
      {
        "creator": 7,
        "id": 2343,
        "image_id": null,
        "images": [
          {
            "architecture": "s390x",
            "features": "",
            "variant": null,
            "digest": "sha256:0f745a413c7886d6dc4f1e6a1d45a5cf5a9a85f72e6243b307e17d67e2e1fe10",
            "os": "linux",
            "os_features": "",
            "os_version": null,
            "size": 27149898
          },
          {
            "architecture": "arm",
            "features": "",
            "variant": "v7",
            "digest": "sha256:d1289429d09bf5ce27d87ecb83b391201dfbb71434794bffde98cef5b400dcc6",
            "os": "linux",
            "os_features": "",
            "os_version": null,
            "size": 24064238
          },
          {
            "architecture": "ppc64le",
            "features": "",
            "variant": null,
            "digest": "sha256:95fe2abc7046ea97e9100e5df15e34fdcc269aa385686ba44541684a534a2b34",
            "os": "linux",
            "os_features": "",
            "os_version": null,
            "size": 33290427
          },
          {
            "architecture": "riscv64",
            "features": "",
            "variant": null,
            "digest": "sha256:a15ccba7f1ffe496b48587d67e5a49388e0d2031fb7a760eacb2aa1c722cc6c7",
            "os": "linux",
            "os_features": "",
            "os_version": null,
            "size": 24227867
          },
          {
            "architecture": "arm64",
            "features": "",
            "variant": "v8",
            "digest": "sha256:c0dd38485ed8b6e149d2fc935d1c61a3b750cda3b3eace0ad6df4abe33fa2b90",
            "os": "linux",
            "os_features": "",
            "os_version": null,
            "size": 27170255
          },
          {
            "architecture": "amd64",
            "features": "",
            "variant": null,
            "digest": "sha256:1e48201ccc2ab83afc435394b3bf70af0fa0055215c1e26a5da9b50a1ae367c9",
            "os": "linux",
            "os_features": "",
            "os_version": null,
            "size": 28567944
          }
        ],
        "last_updated": "2021-07-27T00:05:18.237334Z",
        "last_updater": 1156886,
        "last_updater_username": "doijanky",
        "name": "latest",
        "repository": 130,
        "full_size": 28567944,
        "v2": true
      },
     ...
    ]
  }
}
```
## /v1/container_registry/dockerhub/repository/tag
获取docker hub镜像标签详情
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
repo|string|是|""|镜像
name|string|是|""|tag名

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/dockerhub/repository/tag?repo=ubuntu&name=latest

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "manifests": {
      "schemaVersion": 2,
      "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
      "total_size": 28569406,
      "config": {
        "mediaType": "application/vnd.docker.container.image.v1+json",
        "size": 1462,
        "digest": "sha256:1318b700e415001198d1bf66d260b07f67ca8a552b61b0da02b3832c778f221b"
      },
      "layers": [
        {
          "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
          "size": 28567944,
          "digest": "sha256:16ec32c2132b43494832a05f2b02f7a822479f8250c173d0ab27b3de78b2f058"
        }
      ]
    },
    "blobs": {
      "architecture": "amd64",
      "config": {
        "Hostname": "",
        "Domainname": "",
        "User": "",
        "AttachStdin": false,
        "AttachStdout": false,
        "AttachStderr": false,
        "ExposedPorts": null,
        "Tty": false,
        "OpenStdin": false,
        "StdinOnce": false,
        "Env": [
          "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
        ],
        "Cmd": [
          "bash"
        ],
        "ArgsEscaped": false,
        "Image": "sha256:93c06ad94bc63e5c8fb978d605468c4507f82d92b9ba0dad33c9a80b137163cd",
        "Volumes": null,
        "WorkingDir": "",
        "Entrypoint": null,
        "OnBuild": null,
        "Labels": {
          "maintainer": ""
        },
        "StopSignal": ""
      },
      "container": "c956fe828128e93f86f7628bff7449517519f8ed8dc87285077108eefb8d16ac",
      "container_config": {
        "Hostname": "c956fe828128",
        "Domainname": "",
        "User": "",
        "AttachStdin": false,
        "AttachStdout": false,
        "AttachStderr": false,
        "ExposedPorts": null,
        "Tty": false,
        "OpenStdin": false,
        "StdinOnce": false,
        "Env": [
          "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
        ],
        "Cmd": [
          "/bin/sh",
          "-c",
          "#(nop) ",
          "CMD [\"bash\"]"
        ],
        "ArgsEscaped": false,
        "Image": "sha256:93c06ad94bc63e5c8fb978d605468c4507f82d92b9ba0dad33c9a80b137163cd",
        "Volumes": null,
        "WorkingDir": "",
        "Entrypoint": null,
        "OnBuild": null,
        "Labels": {
          "maintainer": ""
        },
        "StopSignal": ""
      },
      "created": "2021-07-26T21:21:40.307832875Z",
      "docker_version": "20.10.7",
      "history": [
        {
          "created": "2021-07-26T21:21:39.951432409Z",
          "created_by": "/bin/sh -c #(nop) ADD file:524e8d93ad65f08a0cb0d144268350186e36f508006b05b8faf2e1289499b59f in / "
        },
        {
          "created": "2021-07-26T21:21:40.307832875Z",
          "created_by": "/bin/sh -c #(nop)  CMD [\"bash\"]",
          "empty_layer": true
        }
      ],
      "os": "linux",
      "rootfs": {
        "type": "layers",
        "diff_ids": [
          "sha256:7555a8182c42c7737a384cfe03a3c7329f646a3bf389c4bcd75379fc85e6c144"
        ]
      }
    }
  }
}   
```

## /v1/container_registry/list
本地harbor镜像仓库列表
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
https://10.30.100.178/v1/container_registry/list?tenant_uuid=ca0179d2-d5cb-4731-aca2-2309fe382fee&page_size=10&fuzzy=&page_num=0 

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
        "uuid": "9cbd63e0-2d42-4e52-bb5e-80b861cc868a",
        "tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
        "tenant_name": "dev",
        "name": "155",
        "server_address": "https://10.30.100.155",
        "create_time": 1628498676,
        "description": "",
        "user_name": "admin",
        "password": "",
        "status": "healthy",
        "status_detail": "",
        "registry_info": {
          "with_notary": false,
          "with_clair": false,
          "with_admiral": false,
          "admiral_endpoint": "",
          "auth_mode": "db_auth",
          "registry_url": "10.30.100.155",
          "project_creation_restriction": "everyone",
          "self_registration": false,
          "has_ca_root": false,
          "harbor_version": "v1.10.3-6990ccaa",
          "next_scan_all": 0,
          "registry_storage_provider_name": "filesystem",
          "read_only": false,
          "with_chartmuseum": false
        },
        "registry_statistic": {
          "private_project_count": 4,
          "private_repo_count": 139,
          "public_project_count": 1,
          "public_repo_count": 9,
          "total_project_count": 5,
          "total_repo_count": 148
        },
        "tls_config": {
          "ca_data": "-----BEGIN CERTIFICATE-----\nMIIFdzCCA1+gAwIBAgIJAOCiGfMFqTCMMA0GCSqGSIb3DQEBDQUAMFIxCzAJBgNV\nBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5nMRAwDgYDVQQHDAdCZWlqaW5nMQ4wDAYD\nVQQKDAVUb3BrZTEPMA0GA1UECwwGVG9wc2VjMB4XDTIxMDYyNTAxMTUzNFoXDTMx\nMDYyMzAxMTUzNFowUjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAO\nBgNVBAcMB0JlaWppbmcxDjAMBgNVBAoMBVRvcGtlMQ8wDQYDVQQLDAZUb3BzZWMw\nggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQDMzl8t+v4LVuk7Qau9rzYR\n/KdIVPXV1ITf88tsXIyC9KB9vGTeAUYXFJCaRPFSj36RMBVj5bzZSFrM0+8yUJDq\nyzYjQqsEpGIlXHyWtKvwgeeYMxOMi/nk5Z9QMgfWXiVouz1fDejQ+Mg4UVXwCqF4\nrlKhNY9DtDAFaXcQitIWPB7NjOSJYJmhbR27SRNQhPIT4OqdZQ2KKrQfQK5m8h3X\nO54dPrcy6XnaeTrXNiNt/GabC5RywJKGu6c+Nbtwki+IzZz9C9QHQe9EYhQHkl2Z\n6azolzYgOtjACjcvr1MQsdsjuENRknDrmbb/ZqW4RTU/O+UDZLi44wDDPzWNkCNa\ngpTkS4Jk7U/KuHiGOATNMCJXhWPkWGsBrJ6HZba1X6rd4n2H7FFZ0JSmIF+bHw/o\nehS0f67Hj48xbyPZHQt/q57WB3lu6E+1gBavIUjJ5Pp46d10Rc/03waLTW9/sro8\nb4Ylw97gBPdLZT5invtEmEIwtMdVTxmYLHnUNIUTEAqIfg1jIkHsKPMcVuBRwMFP\nGV9SnWCuHq6l9cVmDAwtKhI5wxwcpqSoMyEH9HwrBZbsYH93KkrTVAEd1VEJcYnU\na6rAPLc74uFPdFMwyc/OyOZBv2/xks2jPpB0aftWYK8A0Y4sO4wjq/fbOYLgMEEQ\nMCWzKRqUTVC+PF0qCEAu+QIDAQABo1AwTjAdBgNVHQ4EFgQU6A7V4O4S7PKM6J0y\ni6dO1Kx9kJAwHwYDVR0jBBgwFoAU6A7V4O4S7PKM6J0yi6dO1Kx9kJAwDAYDVR0T\nBAUwAwEB/zANBgkqhkiG9w0BAQ0FAAOCAgEAjrMO6+6/iDhDhdjqtNNB6ZwrjFwh\nd3CGVWNTkBFsBHdjaEHN/tUeAsRERdKTFl4jAMRwqkttMU4hOY8FNG7eKqW363hK\nPSKdPFXFH4pGrBN+hZn0uXQuc0kcxJ37m4K3y1OLrQv+jetWc4qBVVIWkoPryP1C\nJ9BRPOD8HaixCVVATZLVLnCXDhsCSV6sCbJOUtyeBJh0HbdlnRsSW8TT4Zy7wSzf\nAG/grjAe+SEQscRE5xvX9ma4OvndUGci0QasLCUgfCW/9uvmJEODLkQVUPrIO8IV\npVsyUSFqA6waSu4PdN+dYCAKLmHiMJRSnrLFUSpHp4qFOo0G9vQ82ArsU3AOXv2y\nAEVgPVohku1Ja/q3pFgNFz5TrZvgGAvvzwNoNyuEsYemrPYuFYliAvlW8Yro/zD9\n76kThjb8jUEGIbWo5bAmIGeK9Rl081zvPLyRZo+0RxaoRuHzoZz0D/HDlzBZLJQz\ngtWR6B8vSLIE9yvqJAPwkdK7pgNXLPGCKjLsbO3PZSYGJxReVmDh3cBLR4A8rnYF\nNRgfSYVrjpIyOioLOMZ7N2n0jU98VdchWD0x+/NYFWGUM/X/d/75z2pLcV1ZusTO\n68u5RDVK1solne4R4KRjyQo+zPo2o2KsDSbRpPmnMVEhbTQWlPf8/FpxjaZlJBs3\nZ7K7uX2I1junXKc=\n-----END CERTIFICATE-----\n",
          "cert_data": "-----BEGIN CERTIFICATE-----\nMIIFiDCCA3CgAwIBAgIJAPQ1aCJBU+diMA0GCSqGSIb3DQEBDQUAMFIxCzAJBgNV\nBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5nMRAwDgYDVQQHDAdCZWlqaW5nMQ4wDAYD\nVQQKDAVUb3BrZTEPMA0GA1UECwwGVG9wc2VjMB4XDTIxMDYyNTAxMTUzNVoXDTMx\nMDYyMzAxMTUzNVowUjELMAkGA1UEBhMCQ04xEDAOBgNVBAgMB0JlaWppbmcxEDAO\nBgNVBAcMB0JlaWppbmcxDjAMBgNVBAoMBVRvcGtlMQ8wDQYDVQQLDAZUb3BzZWMw\nggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQCyJ8Abk8syuaH42jG4MjAR\nS6O5F5IL49xBszdKsKo2cu3AxKJi6TNmpQC7KG69Gi4vJm8mfoUGwE45v8/z+maF\nV5tRVFm3SmkPW1ZyWdTK50fA7J7MoA82McgzCkW41cpLwcYjpaYG8+d453lqcR2i\n5DJNTj0v3cLUP9kMKGg2w5nnotLQI56I5S/QUjWQzg+SFBAx6HNcKca3hAJjUCR2\ny1n+SNswBgHpXO4UF475xlqOHoOFhJRMh/E6DLCr91hGRWkT5i/SkYML5+r9Xtmf\nRQLinionJWgdtwIJZHCjg6Goyt54he3nrxA+iBvX1cMrW0kYIIjz6WkLi+I13kN9\nmClMdOjfl2Aqo4ZCq2D+0+blbwvU9oG1W1zynqYs7kG8fDYEpXnptXyGL+Q4ugwJ\nLyPI0WUGG3WkasUcKHYmcONK85PcaJ3lFC8nxadJO7YIW+MABzIr129cT0HzRHln\n0dVf8gB6GjPaMvCJwAR3wdfQl7Ni9Ja6LTKkdrXf1VNGBVsJNzKsPa7qz0G8nOW6\ni8LmETkUenIa3KwLOR1Fua5wRLdsQo2yJahJO7QGEJOs3cS1G2i7WoTq9KtW7j6B\nfFG+wh+iUbTgie6NLZ9F5Amuror3BysYxFN1hmL2hbsa4wjXkWaimDZyLWxUjlsD\nSk1lPBNkO4/VCtxTCw5VLwIDAQABo2EwXzAfBgNVHSMEGDAWgBToDtXg7hLs8ozo\nnTKLp07UrH2QkDAJBgNVHRMEAjAAMAsGA1UdDwQEAwIE8DATBgNVHSUEDDAKBggr\nBgEFBQcDATAPBgNVHREECDAGhwQKHmSbMA0GCSqGSIb3DQEBDQUAA4ICAQAHpr0o\n7xterKXn1pWF7k5jkR63wseowFQf/y9xX98nBcn8cYtFGrzM+msTzd7kLhXBfrNX\nIZhzzc3VTJufmpz6/76WGzo0cU1lDc10Os3oi+51MESq6y2UO3f+rJX4jbxCMXe2\nERl/5WsK6qYeD7LvI/BimGALcKZJYL3cvhbH220CqcqygkhV23SovmepFdQdAnkb\n9+gyq/Wtu11vc/n+FY7Ls4IrzSqQ41CQpT4Jm614RA7TuOEQ3an2dORW8CRPuxVl\nwdXGfT+DwuSMYsnHF248mE0vInWnjO4emCO7ZsZsSPcV5YJW8892Zt/Vewo7zzpQ\ncXC7pgb4pF5fgxsNI82uhqTepAgfGq6Q4Ujluoa/THAQlUfuWU63Qx/H4bRG4fX0\n/ffvHrg7v64vyLlMU5FYexCir/U/g0YTYEKT//1mds8CMlgC0f0rSLeSMftG2tti\nebr7UXtyHeDeaQ+7aFgRhXEZjqas59KFYLndMgMyQp7co6eZffsf1ZPBVT6/HDsN\nhVHlLIrvjgmRE7/W58LAvaAwDBIg8GXyh9SSGsUoeox0C1fM1CBZK5PBVRj5TZz1\nm6HOeEIpiJYdacKChtpKLkx3S+Z6h7nP9Prpg1dRNQ5zHMIrHbWZQyx3TUIWvdxD\nkkmP/Ivxn/1O09/XidYAWuz/X83Uvq59GzCuBw==\n-----END CERTIFICATE-----\n",
          "key_data": "-----BEGIN RSA PRIVATE KEY-----\n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\n-----END RSA PRIVATE KEY-----\n"
        },
        "timezone_adaptive": true,
        "function_support": {
          "distribute_allow": false,
          "helm_chart_allow": false
        }
      },
      {
        "uuid": "4659b9b6-b1b4-4c41-90c7-15c497f71f56",
        "tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
        "tenant_name": "dev",
        "name": "176",
        "server_address": "https://10.30.100.176",
        "create_time": 1628498204,
        "description": "",
        "user_name": "admin",
        "password": "",
        "status": "connect-error",
        "status_detail": "registry client create fail",
        "registry_info": {
          "with_notary": true,
          "with_clair": false,
          "with_admiral": false,
          "admiral_endpoint": "",
          "auth_mode": "db_auth",
          "registry_url": "10.30.100.176",
          "project_creation_restriction": "everyone",
          "self_registration": false,
          "has_ca_root": false,
          "harbor_version": "v2.1.0-a3eca103",
          "next_scan_all": 0,
          "registry_storage_provider_name": "filesystem",
          "read_only": false,
          "with_chartmuseum": true
        },
        "registry_statistic": {
          "private_project_count": 3,
          "private_repo_count": 0,
          "public_project_count": 3,
          "public_repo_count": 27,
          "total_project_count": 6,
          "total_repo_count": 27
        },
        "tls_config": {
          "ca_data": "-----BEGIN CERTIFICATE-----\nMIIFfzCCA2egAwIBAgIJALKh8hsYB7LzMA0GCSqGSIb3DQEBDQUAMFYxCzAJBgNV\nBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYD\nVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQZXJzb25hbDAeFw0yMTA2MDkwNzAxMDda\nFw0zMTA2MDcwNzAxMDdaMFYxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYDVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQ\nZXJzb25hbDCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAKgfwbrdYPTK\nWuFhj9iBORU8qq/+R6HkPE4oXkeGZ9t4AYLLF4MkiW0kGC8t+22flSuQPtq/WQYI\nQL8/xzrlRUTLwnGpIb3E4UIR6xVy8Sn1SLep3FrZqxO7yJBxRBEUxovswK9jCdwG\nfsCMXU7HcEPT81XYVzTs8Fa6rKUcalCp2KSDpQVD1QqstIs0ckqRGD87gP9sH1GM\n1W13F2hGFQLoom8ZYC9g/agjHrKrTT8mYNCxNjLB+XCZPXbtQ2lxQWNkPLe9dKW4\nxY/lWEYb1gV6jPJ+AbgSf1I2j5Hry2nZ8/GYAu/qIj915+jq7QEuaKpXq3s9nN44\nZemNg7a5ucbw69CHgVOM37lorfxMcLHjt8Y4egAiepxD04ZG8QUQKyNw2TEB1/TB\ne5XWhWJ0FhXZzeE/tsrfn6SK07gEeJKkDpxvuPlw0PZM2K/iIgY71ChQy5cpuVjg\npzGRhJlcBLPgm25w6JLcF8B+xIUhSUyMrSjsru0Jqhzl0tWXRTIIB8u2e1Yjjl5D\npgSeIrGiuO5sRK2FdULToEF0Han5+Jzi1WgCjBGAyLPrIr//B4OIa3sdYr+05t5v\n838gGVGbfpMxrndMPcOmIFIsZ+a1jO8Uau5qNJkYGeVQ7l2QgZ3+sX6oMRGRfcBJ\nSlYSX0w19Q7YxWmDkLnVOTCyjIWugPNnAgMBAAGjUDBOMB0GA1UdDgQWBBR4VTp9\ngQdX7a3yeJL+2n6Y67bPmTAfBgNVHSMEGDAWgBR4VTp9gQdX7a3yeJL+2n6Y67bP\nmTAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBDQUAA4ICAQAsiDKDuA14GcabCTu3\nZDLczzZAEbBw+NOB1a9knj9teFn8FkJ8wQPoW2o6P1OnhuynPtrXuFtlKDTXWl5v\nciPH9TsOxv1Ld2cP8qSezCiAiGwRPFYMJgB/Lw8EVCVmFzwmqLq4OwTBfcJKQGPp\nvpgr57FoiG7sG6b9iAFgsPNccu9Kga3CllPcmnNA/STBzEaiJGPE3GM76jVZiM0R\nu55f620k8/jycGaoL2mYxMm8eBh8ptVQAPnzyzsajaXbbqXZxpAe4rwHWC3RhTWi\nknHWcnpoHZkPZmh+L1S5s7odVdj7/ktfL0r+n38mWkud7be+N2cdI2TDEVlmP4G3\nF67BjcHw+avsq3xXsLbDDCmJwsI5u/sy5sTVHBapTB36m0TTpw+p41mNePaWFjfx\nxmyteoO+fbMp5CgayILn4qjcr/etrDg7mjYZTR9s1M+uujI/acwnfKlziOe7yFf0\nDo4+Sgg1FSwAiVT38VGwg1GTRbNAJDImwNelhdYki5Drb/OIZ0jAJUM8OXmFG2yG\n3++5wkh/55+7SqryZ0f1+EIYvaDxk1Nt4PjOydySIySMbKsdlQsjyfOdCAMp8m+G\nibx4YswUyCVrB4I88RVoM72OXnQIFPcrt/RBJWAFnxXX9kKle8rKjjVvNEXY6OTr\nsCJPs00rNU8HhHpRL8Xoe2NZmQ==\n-----END CERTIFICATE-----\n",
          "cert_data": "-----BEGIN CERTIFICATE-----\nMIIFkDCCA3igAwIBAgIJANnNHhmiYduqMA0GCSqGSIb3DQEBDQUAMFYxCzAJBgNV\nBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYD\nVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQZXJzb25hbDAeFw0yMTA2MDkwNzAxMDha\nFw0zMTA2MDcwNzAxMDhaMFYxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYDVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQ\nZXJzb25hbDCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBANfnQSp4RYYb\nOZxhvSNpD9dywuY6Gy73rfsVrztxTfF8RPZOQNpjIWq0DYm6vnNSF2Kdxwz+PaQC\nlznJW+bA7JVONmmBK/diqFh4tKGJw0cru9tyFMWO5yuVnyfy99vjmByneWX6gTxe\nEI4612TClFYvaS2FunbgbLmlocywAjr///wSaTucMt6quY5f08xz/UOiPLx/0Ip5\nzOk32VSVQbWpcE9JwK1y7Q+4y09Av5U8JCkhBxCIgWLyjdILPTsvvwiOiwrFhdSg\n1olguadmP8a050rRN1N+65iwOpL8Et8f6J8W8sv3RuEGO8oOe9wwRjdSimC/fOrp\nQwKOP6oBT3D/+2ZykLCm3T30DlhQLVwkkoIy5OA6QfKvygMZPjmxTQ40ZIG46cwc\nJaBK/Ezpm3ZE4RpjORsuD5zcjreIYPi1NkWpeq6XceDDe4vaqEdCXW7V2ooSMgxh\n6uuwN1wmBeJnyLeTXB5RO73bocXrvUv1Zxi0+vpdBf6QETYYwg6XJY8YywLdQLmG\nrmXVQlYGSX8KbLUYColEowwhsPrHOfb4BhxecS1hhockfFximcr5P7ed8hTBF4Bm\nveHNf0eYq2TkgQevQrUHiHmoBXli79Pwbw8/EKktt60AgKWo6tNXNjWH2ZQFkwQ9\nODCHhDvRI/sXX2ei6I6CK1i3ll1eNVibAgMBAAGjYTBfMB8GA1UdIwQYMBaAFHhV\nOn2BB1ftrfJ4kv7afpjrts+ZMAkGA1UdEwQCMAAwCwYDVR0PBAQDAgTwMBMGA1Ud\nJQQMMAoGCCsGAQUFBwMBMA8GA1UdEQQIMAaHBAoeZLAwDQYJKoZIhvcNAQENBQAD\nggIBACm7hniZHMAgbB9bAWcPDOFLDxEj2CBsPRIu6cZTozYKUZ8ePYbyqCB9RyAr\nd8EbeYrgee8pkYgxoge8uD9MczqNR6vuJBuTn/f2iIiF1/FU1VtO/JM1LTv49oLm\niyl74JiNya9DavO+LX2OYKq3ydL+zGNvZgkhuR0gGOqzVUIapFIJQpsKrdEwooEv\nBpmSUq8D0e9ZUO7gwzT36k8RplI3kbwRFDaZ3c6EvAvaOrQmQl9wiLegYR57qdgg\nBOKDAW5kYwzatpdW+qjShwo3LISk8esofjolMUgPIprMey5jXtmonN3xXbcB3Bz8\nBrHkTDHdFTL1mLte5Q9eEl1/yLlec4VZySNrWMB9XGm4auyD6IhziaZZ2q7Y+QU0\nxh0ycFV2YZxV/wo59mlB/HD6zhfREeNMuheUx5vTzyQ7hsb3mrHLxNeZeHbvvsBF\noEs+O8XkalkrB/yBdEnugw0LKlD3RSELk4IT349IxOkbzH/1WYt2jMnnvMTh5P0W\nD1gMqciZwnN+EX0w9MnoLvorwbW+v042tA5eCTkSEIcp6zvfHARXhsKFVYsY80tx\n4mZkuNEe+5BuKcdDH3mKelG21bYKMJ82f4RzjDUSqyzmjPcj/3afkm0QHCvYTZpP\n2OVMACMjado9Gcv3kJwN/vSCooz3hMoMczfyNQpXs8JvAWAy\n-----END CERTIFICATE-----\n",
          "key_data": "-----BEGIN RSA PRIVATE KEY-----\nMIIJJgIBAAKCAgEA1+dBKnhFhhs5nGG9I2kP13LC5jobLvet+xWvO3FN8XxE9k5A\n2mMharQNibq+c1IXYp3HDP49pAKXOclb5sDslU42aYEr92KoWHi0oYnDRyu723IU\nxY7nK5WfJ/L32+OYHKd5ZfqBPF4QjjrXZMKUVi9pLYW6duBsuaWhzLACOv///BJp\nO5wy3qq5jl/TzHP9Q6I8vH/QinnM6TfZVJVBtalwT0nArXLtD7jLT0C/lTwkKSEH\nEIiBYvKN0gs9Oy+/CI6LCsWF1KDWiWC5p2Y/xrTnStE3U37rmLA6kvwS3x/onxby\ny/dG4QY7yg573DBGN1KKYL986ulDAo4/qgFPcP/7ZnKQsKbdPfQOWFAtXCSSgjLk\n4DpB8q/KAxk+ObFNDjRkgbjpzBwloEr8TOmbdkThGmM5Gy4PnNyOt4hg+LU2Ral6\nrpdx4MN7i9qoR0JdbtXaihIyDGHq67A3XCYF4mfIt5NcHlE7vduhxeu9S/VnGLT6\n+l0F/pARNhjCDpcljxjLAt1AuYauZdVCVgZJfwpstRgKiUSjDCGw+sc59vgGHF5x\nLWGGhyR8XGKZyvk/t53yFMEXgGa94c1/R5irZOSBB69CtQeIeagFeWLv0/BvDz8Q\nqS23rQCApajq01c2NYfZlAWTBD04MIeEO9Ej+xdfZ6LojoIrWLeWXV41WJsCAwEA\nAQKCAgB87DGogS65Ccer1GG7u26PGrfqvnQ8GNNyFHnvyv9uWpkMavrbYcBUHRo4\nNvU7hKRDS0eBHRpNa7JUnU2vlrFNMpQJN9RYr5z4k97wGOYEqClqL/gU1zqq3UfZ\ntZv0fxvkeIKlnuxoIYUyxpkak/uAYq5YyKe7YN+IC24zISQpPza+g2igNSC59c6n\nsoq6IeLI33aFGu9vMEqAJvB5IGOE2SVCu0nhEj5YenQoxy4TC1lg8ttDlbhHqFCm\n2Bn1xQqjyNZqxR9KiEWZ9310fpUoREQP5j488ZMgJde+dFv2/l96rayOl+VLDnBJ\n2VeRb90w5XFryWBeC9naALSViWyMxXlHWZynJLmpp2r3+wFsMIfRurrLbn69pAZC\nG/vCWHZRLLatqSwT1JQknh1nreAQAMt+ZwFhi3oT8a9OSgEEmjIO3Nwvx/O/zvV5\nsUAv9gLOY6F0Cq3Uxl4MgWgGCpR80YCHAKgE9Fu7PiT14LYqtiHKqrQKPp56rJFO\nv5lCl/B61pYNoCUxR5n77QfcHZSvdWd0tY5FdEWUPeq7urOGZF4GR3Doe+z7WleX\nzZO4nIAfvYjBML2GMelmZkbLTqr7Et/FzGRRdiiNVO6Ug7IyYe1KgQcXrwwmDAo3\nONgJ53vUStTFajeMlMMKjTPpIXqjMSV2AzPwTFVj2QcPZFueAQKCAQEA7oxNwD1B\nww/8NljmOhIlhQHzHt806/bDssKBkSf1wdtjCDuNOll0N8wexFWcFNAJiPdLqZ75\nLFaFRqSAIf0G/5gxY1Vc3+PtDGBwOxLfOv0QXLs3dMbdnX8GX2092oiXwwwUqI+Y\n4/dzJQO9oBw/1FuJsQD1auTJLoVgzkW4K7vYg4KfAqJBETxm9K/ZXSKltpA9aN1Z\nwQNWprv5es971Nrq5kEy+w0rPfctngMz00m778P0tlWMS//msYlnWKEDS/XWXV0v\nOAf7Kt1oSAe/Ehbpvh5sh5W1Xgccld96dOgNmp3biUFzvNUCl2z9xBHJX1PQakAY\n8o3yAOhvQNYrOQKCAQEA57LYMOUI6aEWvje30y4s/yHvMi6sihD9EODLZmZs2GDA\nwWLj3F1hLVCxy1YSL7FMigo3zv2qq1bM+XwKE/przQMfMOZeOBIcvk6uex1/29Oz\njAbARzVk2vpZwu7LNlrka0owaUsUP+UhtVHadT4G3Hpg6n5OfMO2EAVGmDQq4XRj\nXMiviC7hJhW5svaqNQc4UHdLojHBiSqPpppQVIWxofNieOUfeLEnkiOhA87u9uog\nbAQ5JValXSzbrbG05gUhcsXJiqUovL9WG4lvLCTanp3XazlcePSsgfW7mwrlhnPG\nPAZAKWHUQMSdhIQwS+lVEaQP7Pqi7R567GXvHilecwKB/33LfzThGMzEoTwHpWD6\nMM7zOEIPctj8SDb8W1cwu2h/SLoOrWsXwTGrco4WlzhifKS9xCiurLe06JNYLDnA\nNPCUUXcQjOmESH0+XfDJAu8YhIhiMdxjAnsLgVDRSszzOxSgSkSZdQbCdvYOAvFr\n9D0ICJRO7RxxiaX+sA4WtghaBtNTDodVCPsN3z0pfnaezsR3S+sAz1P5brh+aBFb\nWPHmf/jsaPX6+9KxhlzNU4cYWwMVUvbUJiftyrnUu6sBPbvQ6DpT6ZKiotD38QYL\nD7d6XcjkQlc9m2b6WRivwOPle0cN97dpzJ7HtZYk462Bs6+Rg1aEdqNyNyxDZmfK\niQKCAQAYwFE5/+2Qz6WXUmpvw9oIsz5TNQs3gJMYL3trB/wOrV9KCV9gFhWgeqNT\nnnE46Q7NHERT92M5BH/HEwockj7b2r6FQcbE5KJvbgZTnpYfDKF8jugRc1G/1sip\n+0p4FwOZtoYvaVbTcI3GSeU1axfei7A4vJ9z0pBra7Tb447FIOLQcZvWx3ND10RM\nKu+J1KieZ/ALdpc/KO3JlWiJbvLH4zEcyxUulnYstWOo/X0noWEvSNA1/eiSaI1b\nI8W4YMnu8dQS3IvahfIT5P2cUJ+OHDx79te7ECAxjeepq2NTlqCRnvVRtmKvPJG7\nK0fhhB6TUNxmq2umOwBUqpr9tNujAoIBAQDPtUjgoN8K4yJiZ9Tjj5p4E2p/ftyE\njBtWqFZAYWw9xO6BknnF7M7o2HnOTU+joQg7QZkRQ0TzojwRtDnQazjXq+Ecjvpb\nSJDCic8s8hqHGA8rhdAY9f/A8ufYkqneX2tlL0hjxffaQGi+KqREwqaV7knkxfL3\ngFG3w4Od8DGmwym9zudLOIA2P8olpzlJ5aFrVhI6rUWPEyEYPj+dMC83TscifbQ9\nBF/yXdNPVYQiqb0JVMkuXcNu6PJJWMRK1dXGK2zI43FMCUdLq/AvUMlagweuNqec\nakUmMM5u8/4mQZ+JcjO6f2ihQu/GIjQaFdowIe1e1th61vuW3kwDMuOs\n-----END RSA PRIVATE KEY-----\n"
        },
        "timezone_adaptive": true,
        "function_support": {
          "distribute_allow": true,
          "helm_chart_allow": true
        }
      }
    ],
    "total_count": 2
  }
}
```

## /v1/container_registry/get
本地harbor镜像仓库详情
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
 

#### 正常返回示例

## /v1/container_registry/create
纳管harbor镜像仓库
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant_uuid|string|是|""|租户UUID
name|string|是|""|仓库名
server_address|string|是|""|仓库地址
user_name|string|是|""|仓库验证用户名
password|string|是|""|仓库验证密码
description|string|否|""|描述
tls_config|struct|是|{}|TLS验证
timezone_adpative|bool|否|false|时区适配
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/create

```
{
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"name": "12_169",
	"server_address": "https://10.30.12.169",
	"user_name": "admin",
	"password": "Harbor12345",
	"description": "",
	"tls_config": {
		"ca_data": "-----BEGIN CERTIFICATE-----\nMIIFfzCCA2egAwIBAgIJAJbOuXW9WPh/MA0GCSqGSIb3DQEBDQUAMFYxCzAJBgNV\nBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYD\nVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQZXJzb25hbDAeFw0yMDEwMjkxMzQ2NTRa\nFw0zMDEwMjcxMzQ2NTRaMFYxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYDVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQ\nZXJzb25hbDCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAKSCaaI28DUH\nNUVvpLX5BtUmhohqDlDgTKViHgU1Yf5zyi/bVDkMnhuAUbGItAcEwrIYDn63bjIr\nETFuRNM35D5+5iMon79U1LSqE1v8BTSPi0lwYZBADtQMtFscgzXbXzgOJgGfXfRI\n9jXgV7wrCEpwnWBWbyRt9Y3xKLqay/6znrTm4oFySAXuHytPhD6JmfDZzEZ16Y/h\nCigUDm2NfXOuIksUwSTxztLovCLq+OGWJvItOpQ2F03ZFUoAB0JMllR5s46tvTZZ\nl1kH71UD8vhO30ndlkHIUzT5kfsMYDzJR9foi5QuBk8x2w2utryYhSoQAL6UQF3h\nWQkuZg3svvw3ow00jGkJRRawNhuRST3ehiSsY9g70npjg+etwcATUG/16Ws7Fvfd\nliH9cHMRvM9Jfd1iSBVrQeS+ZUV/m4vuMukJH5+Jj739vD/alI+8tKxaB8HHvqqW\njSd4aI0aXwsmUT/pQU1QztIaB/3eJf3aC1LdRRVZNGARQ1EYjLWnuyJMioxFGol2\nKGYf8bDz0ODrBsjzcIpLmWTkuVWPLhEiDJeKLAgLxpCzDLqI5uDJxSXvG31YMxGB\nBCC9pO4oUwCmKgh/mwqN4NYN9N5BYnsrfcl7WXzDdgriOU8SjmmAZGkR9R+O8wbC\ncK4/qAsR3woE0TBghVSUxiWH8Ov/dVgdAgMBAAGjUDBOMB0GA1UdDgQWBBT/42rI\n/rlTJ5PYC8/XFApCNZNuWTAfBgNVHSMEGDAWgBT/42rI/rlTJ5PYC8/XFApCNZNu\nWTAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBDQUAA4ICAQAQfW+OVjGkIKQoAgjF\nDhBN7MlbrH3G5x26MGw/4NUGDI0iVcVHmIR0VM+3Sq7IzTvsdM5KJtUX2ZEPop3K\n/uLimnpbQPuwaE99H7h/Suvf+zkgSbor+rpB6otwnPe41/jX0/JsncN6oatN23NV\nrU92SdZBHJ8oTDZjgjYpUoco2oF0RWn7ihYqfChQ2o7pFA+B1ElSnA8SPnfcAXEv\nRIeSYDDchaInlgVjZsjv/fwUoNBOyv2xm0hU1d7Lh6gge/JCVN/sufh8s1g/l8b8\nfBKRvz4jcyQcB647rvzkKw/PpcHhNeIm+TJudf9nkH9REmeAUt4SA9u31hV3C0fU\nFKBRXOLrGZjKWCPC85K5bJqhfuRgn/o+cmwxwm7Kkz3lDQ4j71LljWQ1z7ArrmI2\nDIerJ/aVMdEw8Js3YZI8nOiHW4FB01WCVY7cSMVuIFx4fiLSNl/q8qDV28/wjDbV\nQQzX75C/Q4aVCFOsryq0EfAVg16WqEIZlkcjH1D5xx4L58SY+aI08ZeHGg8G6rrH\nZfk9FuHU/gDA+BcpZ+lZhFSm4Kp5benRcERbwai5a6vmzYLfIZN9iwnrYiLSRPJc\n3iCy23b6N8ZNbQiLK7WU2c4fu1Wy2UndXOJmg+NyGstF0HSiaOeUDS41+8nRls2K\nySuHzlhTHTBPvzfNwW5zx9/oFw==\n-----END CERTIFICATE-----\n",
		"key_data": "-----BEGIN RSA PRIVATE KEY-----\n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\n-----END RSA PRIVATE KEY-----\n",
		"cert_data": "-----BEGIN CERTIFICATE-----\nMIIFkDCCA3igAwIBAgIJAJTttkM9W9UiMA0GCSqGSIb3DQEBDQUAMFYxCzAJBgNV\nBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYD\nVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQZXJzb25hbDAeFw0yMDEwMjkxMzQ2NTRa\nFw0zMDEwMjcxMzQ2NTRaMFYxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYDVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQ\nZXJzb25hbDCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAMvzWr4jhWbh\nReyipxxyDxjhculCujyh2D4VDnP1pw1Vel+pD81gzt0dk9dOHrCoDZzGtZ7S016r\nRc9Xt/TeIyxctDwtRZXZ5hE9UMTmJdcZEfvuc1lvv1GuMELT65y8TBaw1+RuCLKQ\niq0tifeiqZOgabAI2f2h62eIS8KZdvg9LtfwU/aaP3rBUA1l4nzKebujeZasp6CB\nebVEKjN3Go8B/yCp5dkYn707vO9VrmIADLEC8JmjnPWdTqKkVjVAPJ47c62OibEj\nFSFiLk3AOv3aBQFOp/b5GcidtFmSDkR51XEeVthjxNAlHeI970KVT+ffQ8dyo63/\nBsoRwe9ywwtEyLuw0fTMbf7IN6QRbP+cc8cIoDw0H4w5TDV5SZNhVmRWfZFfvary\n9GS1+hUp334R7HHELVHDuVfZApHyhNvv8o8ZaWi/PNVP1RqcUAhlMR5pi4ErPj2C\niKrKzIfwI07UmL0ASWUw4ctz+J7OgiyTBo048VgoThVq0Mdq0zIhLEUBErMgTig2\nBAoFas45Rxf8cw/8577pKbyVd1vm3hRtHp1Y0PcEXG340KkrG1i1YY83mphWgb+J\niNHNL1rR6iC/wQV7oGBY98QXAYsR/i6bfdU/2vUQLZT9XLzvgSiBKOyFlw1tsAyf\nI698laoXOJEvqxiDjOUpfciL6i09TFrBAgMBAAGjYTBfMB8GA1UdIwQYMBaAFP/j\nasj+uVMnk9gLz9cUCkI1k25ZMAkGA1UdEwQCMAAwCwYDVR0PBAQDAgTwMBMGA1Ud\nJQQMMAoGCCsGAQUFBwMBMA8GA1UdEQQIMAaHBAoeDKkwDQYJKoZIhvcNAQENBQAD\nggIBACfooUrULCRcetYrLHDgYYJip5NA9lSvyxrUvUoYYK6JRtSiR34NOqNiWlN+\n4yJ9D5m87y/hC+gqvx696djz3L5Y+9e1v7SAgP/2uKTHWrvnHwyaVhL6CfJL+Qlh\nxm+nwT1M/y6h+sviwR1MASBvbKIp9PbnJnJ4u3UwEhNEzosbmwPpT+0QqkWFPM2w\nCPd6gTLi0hQZa43sqOG/IsCHhf81LOAjdd9yBlWCWnwp0P6lfKpYX/eximgFSLtj\nX/8s9P5x9gRXC8M669zfeaIZkdUHCVqHMMh2ppeRsLZPqVSns5dzoQE4oCi3mn3U\ns6dsPihmabJU9hBxEjUtYbO67ZOMKDvdwBjYPqUxhV/9Pnf7XmpsWPvM/V+OhM4u\nK27yWtKXFpndXvI1DFuQKSNGawwvVOCfj1jq2b0mUQzVaYusbtBziBygR9lkCKUy\nDZcTy/WYJNt4mLSIoIUu3OF/V0yjMQ8EG9Hvzp53BboKYxqNbP2kRQtLuVgcS0ir\nj2F+Vcdg25uvPdUz6bB7MxZbYd3Ax0PoNEfurqaa5BzlEx0Cd7ei7p5fyhfF5rgZ\nfQmcr2T3UkKjndsVb2xpk9nJltnrspl6HFi/sTnCPheawuxa9oP1FH/M21SR9TA4\nqXxIOVk28HPsXSuEaZjGKQMQbodKGCwNr9mDs3qAKXVp57Mg\n-----END CERTIFICATE-----\n"
	},
	"timezone_adaptive": true,
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
    "uuid": "aa67f46f-2565-437e-9a7e-fba2d6f46d48",
    "tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
    "tenant_name": "dev",
    "name": "12_169",
    "server_address": "https://10.30.12.169",
    "create_time": 1629786029,
    "description": "",
    "user_name": "admin",
    "password": "",
    "status": "healthy",
    "status_detail": "",
    "tls_config": {
      "ca_data": "-----BEGIN CERTIFICATE-----\nMIIFfzCCA2egAwIBAgIJAJbOuXW9WPh/MA0GCSqGSIb3DQEBDQUAMFYxCzAJBgNV\nBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYD\nVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQZXJzb25hbDAeFw0yMDEwMjkxMzQ2NTRa\nFw0zMDEwMjcxMzQ2NTRaMFYxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYDVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQ\nZXJzb25hbDCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAKSCaaI28DUH\nNUVvpLX5BtUmhohqDlDgTKViHgU1Yf5zyi/bVDkMnhuAUbGItAcEwrIYDn63bjIr\nETFuRNM35D5+5iMon79U1LSqE1v8BTSPi0lwYZBADtQMtFscgzXbXzgOJgGfXfRI\n9jXgV7wrCEpwnWBWbyRt9Y3xKLqay/6znrTm4oFySAXuHytPhD6JmfDZzEZ16Y/h\nCigUDm2NfXOuIksUwSTxztLovCLq+OGWJvItOpQ2F03ZFUoAB0JMllR5s46tvTZZ\nl1kH71UD8vhO30ndlkHIUzT5kfsMYDzJR9foi5QuBk8x2w2utryYhSoQAL6UQF3h\nWQkuZg3svvw3ow00jGkJRRawNhuRST3ehiSsY9g70npjg+etwcATUG/16Ws7Fvfd\nliH9cHMRvM9Jfd1iSBVrQeS+ZUV/m4vuMukJH5+Jj739vD/alI+8tKxaB8HHvqqW\njSd4aI0aXwsmUT/pQU1QztIaB/3eJf3aC1LdRRVZNGARQ1EYjLWnuyJMioxFGol2\nKGYf8bDz0ODrBsjzcIpLmWTkuVWPLhEiDJeKLAgLxpCzDLqI5uDJxSXvG31YMxGB\nBCC9pO4oUwCmKgh/mwqN4NYN9N5BYnsrfcl7WXzDdgriOU8SjmmAZGkR9R+O8wbC\ncK4/qAsR3woE0TBghVSUxiWH8Ov/dVgdAgMBAAGjUDBOMB0GA1UdDgQWBBT/42rI\n/rlTJ5PYC8/XFApCNZNuWTAfBgNVHSMEGDAWgBT/42rI/rlTJ5PYC8/XFApCNZNu\nWTAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBDQUAA4ICAQAQfW+OVjGkIKQoAgjF\nDhBN7MlbrH3G5x26MGw/4NUGDI0iVcVHmIR0VM+3Sq7IzTvsdM5KJtUX2ZEPop3K\n/uLimnpbQPuwaE99H7h/Suvf+zkgSbor+rpB6otwnPe41/jX0/JsncN6oatN23NV\nrU92SdZBHJ8oTDZjgjYpUoco2oF0RWn7ihYqfChQ2o7pFA+B1ElSnA8SPnfcAXEv\nRIeSYDDchaInlgVjZsjv/fwUoNBOyv2xm0hU1d7Lh6gge/JCVN/sufh8s1g/l8b8\nfBKRvz4jcyQcB647rvzkKw/PpcHhNeIm+TJudf9nkH9REmeAUt4SA9u31hV3C0fU\nFKBRXOLrGZjKWCPC85K5bJqhfuRgn/o+cmwxwm7Kkz3lDQ4j71LljWQ1z7ArrmI2\nDIerJ/aVMdEw8Js3YZI8nOiHW4FB01WCVY7cSMVuIFx4fiLSNl/q8qDV28/wjDbV\nQQzX75C/Q4aVCFOsryq0EfAVg16WqEIZlkcjH1D5xx4L58SY+aI08ZeHGg8G6rrH\nZfk9FuHU/gDA+BcpZ+lZhFSm4Kp5benRcERbwai5a6vmzYLfIZN9iwnrYiLSRPJc\n3iCy23b6N8ZNbQiLK7WU2c4fu1Wy2UndXOJmg+NyGstF0HSiaOeUDS41+8nRls2K\nySuHzlhTHTBPvzfNwW5zx9/oFw==\n-----END CERTIFICATE-----\n",
      "cert_data": "-----BEGIN CERTIFICATE-----\nMIIFkDCCA3igAwIBAgIJAJTttkM9W9UiMA0GCSqGSIb3DQEBDQUAMFYxCzAJBgNV\nBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYD\nVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQZXJzb25hbDAeFw0yMDEwMjkxMzQ2NTRa\nFw0zMDEwMjcxMzQ2NTRaMFYxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYDVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQ\nZXJzb25hbDCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAMvzWr4jhWbh\nReyipxxyDxjhculCujyh2D4VDnP1pw1Vel+pD81gzt0dk9dOHrCoDZzGtZ7S016r\nRc9Xt/TeIyxctDwtRZXZ5hE9UMTmJdcZEfvuc1lvv1GuMELT65y8TBaw1+RuCLKQ\niq0tifeiqZOgabAI2f2h62eIS8KZdvg9LtfwU/aaP3rBUA1l4nzKebujeZasp6CB\nebVEKjN3Go8B/yCp5dkYn707vO9VrmIADLEC8JmjnPWdTqKkVjVAPJ47c62OibEj\nFSFiLk3AOv3aBQFOp/b5GcidtFmSDkR51XEeVthjxNAlHeI970KVT+ffQ8dyo63/\nBsoRwe9ywwtEyLuw0fTMbf7IN6QRbP+cc8cIoDw0H4w5TDV5SZNhVmRWfZFfvary\n9GS1+hUp334R7HHELVHDuVfZApHyhNvv8o8ZaWi/PNVP1RqcUAhlMR5pi4ErPj2C\niKrKzIfwI07UmL0ASWUw4ctz+J7OgiyTBo048VgoThVq0Mdq0zIhLEUBErMgTig2\nBAoFas45Rxf8cw/8577pKbyVd1vm3hRtHp1Y0PcEXG340KkrG1i1YY83mphWgb+J\niNHNL1rR6iC/wQV7oGBY98QXAYsR/i6bfdU/2vUQLZT9XLzvgSiBKOyFlw1tsAyf\nI698laoXOJEvqxiDjOUpfciL6i09TFrBAgMBAAGjYTBfMB8GA1UdIwQYMBaAFP/j\nasj+uVMnk9gLz9cUCkI1k25ZMAkGA1UdEwQCMAAwCwYDVR0PBAQDAgTwMBMGA1Ud\nJQQMMAoGCCsGAQUFBwMBMA8GA1UdEQQIMAaHBAoeDKkwDQYJKoZIhvcNAQENBQAD\nggIBACfooUrULCRcetYrLHDgYYJip5NA9lSvyxrUvUoYYK6JRtSiR34NOqNiWlN+\n4yJ9D5m87y/hC+gqvx696djz3L5Y+9e1v7SAgP/2uKTHWrvnHwyaVhL6CfJL+Qlh\nxm+nwT1M/y6h+sviwR1MASBvbKIp9PbnJnJ4u3UwEhNEzosbmwPpT+0QqkWFPM2w\nCPd6gTLi0hQZa43sqOG/IsCHhf81LOAjdd9yBlWCWnwp0P6lfKpYX/eximgFSLtj\nX/8s9P5x9gRXC8M669zfeaIZkdUHCVqHMMh2ppeRsLZPqVSns5dzoQE4oCi3mn3U\ns6dsPihmabJU9hBxEjUtYbO67ZOMKDvdwBjYPqUxhV/9Pnf7XmpsWPvM/V+OhM4u\nK27yWtKXFpndXvI1DFuQKSNGawwvVOCfj1jq2b0mUQzVaYusbtBziBygR9lkCKUy\nDZcTy/WYJNt4mLSIoIUu3OF/V0yjMQ8EG9Hvzp53BboKYxqNbP2kRQtLuVgcS0ir\nj2F+Vcdg25uvPdUz6bB7MxZbYd3Ax0PoNEfurqaa5BzlEx0Cd7ei7p5fyhfF5rgZ\nfQmcr2T3UkKjndsVb2xpk9nJltnrspl6HFi/sTnCPheawuxa9oP1FH/M21SR9TA4\nqXxIOVk28HPsXSuEaZjGKQMQbodKGCwNr9mDs3qAKXVp57Mg\n-----END CERTIFICATE-----\n",
      "key_data": "-----BEGIN RSA PRIVATE KEY-----\n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\n-----END RSA PRIVATE KEY-----\n"
    },
    "timezone_adaptive": true,
    "function_support": {
      "distribute_allow": false,
      "helm_chart_allow": false
    }
  }
}   
```

## /v1/container_registry/delete
删除harbor镜像仓库
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant_uuid|string|是|""|租户UUID
uuid|string|是|""|仓库uuid
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/delete
```
{
"tenant_uuid":"ca0179d2-d5cb-4731-aca2-2309fe382fee",
"uuid":"aa67f46f-2565-437e-9a7e-fba2d6f46d48"
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
    "uuid": "aa67f46f-2565-437e-9a7e-fba2d6f46d48",
    "tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
    "tenant_name": "dev",
    "name": "12_169",
    "server_address": "https://10.30.12.169",
    "create_time": 1629786029,
    "description": "sdfsfs",
    "user_name": "admin",
    "password": "",
    "status": "healthy",
    "status_detail": "",
    "tls_config": {
      "ca_data": "-----BEGIN CERTIFICATE-----\nMIIFfzCCA2egAwIBAgIJAJbOuXW9WPh/MA0GCSqGSIb3DQEBDQUAMFYxCzAJBgNV\nBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYD\nVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQZXJzb25hbDAeFw0yMDEwMjkxMzQ2NTRa\nFw0zMDEwMjcxMzQ2NTRaMFYxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYDVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQ\nZXJzb25hbDCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAKSCaaI28DUH\nNUVvpLX5BtUmhohqDlDgTKViHgU1Yf5zyi/bVDkMnhuAUbGItAcEwrIYDn63bjIr\nETFuRNM35D5+5iMon79U1LSqE1v8BTSPi0lwYZBADtQMtFscgzXbXzgOJgGfXfRI\n9jXgV7wrCEpwnWBWbyRt9Y3xKLqay/6znrTm4oFySAXuHytPhD6JmfDZzEZ16Y/h\nCigUDm2NfXOuIksUwSTxztLovCLq+OGWJvItOpQ2F03ZFUoAB0JMllR5s46tvTZZ\nl1kH71UD8vhO30ndlkHIUzT5kfsMYDzJR9foi5QuBk8x2w2utryYhSoQAL6UQF3h\nWQkuZg3svvw3ow00jGkJRRawNhuRST3ehiSsY9g70npjg+etwcATUG/16Ws7Fvfd\nliH9cHMRvM9Jfd1iSBVrQeS+ZUV/m4vuMukJH5+Jj739vD/alI+8tKxaB8HHvqqW\njSd4aI0aXwsmUT/pQU1QztIaB/3eJf3aC1LdRRVZNGARQ1EYjLWnuyJMioxFGol2\nKGYf8bDz0ODrBsjzcIpLmWTkuVWPLhEiDJeKLAgLxpCzDLqI5uDJxSXvG31YMxGB\nBCC9pO4oUwCmKgh/mwqN4NYN9N5BYnsrfcl7WXzDdgriOU8SjmmAZGkR9R+O8wbC\ncK4/qAsR3woE0TBghVSUxiWH8Ov/dVgdAgMBAAGjUDBOMB0GA1UdDgQWBBT/42rI\n/rlTJ5PYC8/XFApCNZNuWTAfBgNVHSMEGDAWgBT/42rI/rlTJ5PYC8/XFApCNZNu\nWTAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBDQUAA4ICAQAQfW+OVjGkIKQoAgjF\nDhBN7MlbrH3G5x26MGw/4NUGDI0iVcVHmIR0VM+3Sq7IzTvsdM5KJtUX2ZEPop3K\n/uLimnpbQPuwaE99H7h/Suvf+zkgSbor+rpB6otwnPe41/jX0/JsncN6oatN23NV\nrU92SdZBHJ8oTDZjgjYpUoco2oF0RWn7ihYqfChQ2o7pFA+B1ElSnA8SPnfcAXEv\nRIeSYDDchaInlgVjZsjv/fwUoNBOyv2xm0hU1d7Lh6gge/JCVN/sufh8s1g/l8b8\nfBKRvz4jcyQcB647rvzkKw/PpcHhNeIm+TJudf9nkH9REmeAUt4SA9u31hV3C0fU\nFKBRXOLrGZjKWCPC85K5bJqhfuRgn/o+cmwxwm7Kkz3lDQ4j71LljWQ1z7ArrmI2\nDIerJ/aVMdEw8Js3YZI8nOiHW4FB01WCVY7cSMVuIFx4fiLSNl/q8qDV28/wjDbV\nQQzX75C/Q4aVCFOsryq0EfAVg16WqEIZlkcjH1D5xx4L58SY+aI08ZeHGg8G6rrH\nZfk9FuHU/gDA+BcpZ+lZhFSm4Kp5benRcERbwai5a6vmzYLfIZN9iwnrYiLSRPJc\n3iCy23b6N8ZNbQiLK7WU2c4fu1Wy2UndXOJmg+NyGstF0HSiaOeUDS41+8nRls2K\nySuHzlhTHTBPvzfNwW5zx9/oFw==\n-----END CERTIFICATE-----\n",
      "cert_data": "-----BEGIN CERTIFICATE-----\nMIIFkDCCA3igAwIBAgIJAJTttkM9W9UiMA0GCSqGSIb3DQEBDQUAMFYxCzAJBgNV\nBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYD\nVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQZXJzb25hbDAeFw0yMDEwMjkxMzQ2NTRa\nFw0zMDEwMjcxMzQ2NTRaMFYxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYDVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQ\nZXJzb25hbDCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAMvzWr4jhWbh\nReyipxxyDxjhculCujyh2D4VDnP1pw1Vel+pD81gzt0dk9dOHrCoDZzGtZ7S016r\nRc9Xt/TeIyxctDwtRZXZ5hE9UMTmJdcZEfvuc1lvv1GuMELT65y8TBaw1+RuCLKQ\niq0tifeiqZOgabAI2f2h62eIS8KZdvg9LtfwU/aaP3rBUA1l4nzKebujeZasp6CB\nebVEKjN3Go8B/yCp5dkYn707vO9VrmIADLEC8JmjnPWdTqKkVjVAPJ47c62OibEj\nFSFiLk3AOv3aBQFOp/b5GcidtFmSDkR51XEeVthjxNAlHeI970KVT+ffQ8dyo63/\nBsoRwe9ywwtEyLuw0fTMbf7IN6QRbP+cc8cIoDw0H4w5TDV5SZNhVmRWfZFfvary\n9GS1+hUp334R7HHELVHDuVfZApHyhNvv8o8ZaWi/PNVP1RqcUAhlMR5pi4ErPj2C\niKrKzIfwI07UmL0ASWUw4ctz+J7OgiyTBo048VgoThVq0Mdq0zIhLEUBErMgTig2\nBAoFas45Rxf8cw/8577pKbyVd1vm3hRtHp1Y0PcEXG340KkrG1i1YY83mphWgb+J\niNHNL1rR6iC/wQV7oGBY98QXAYsR/i6bfdU/2vUQLZT9XLzvgSiBKOyFlw1tsAyf\nI698laoXOJEvqxiDjOUpfciL6i09TFrBAgMBAAGjYTBfMB8GA1UdIwQYMBaAFP/j\nasj+uVMnk9gLz9cUCkI1k25ZMAkGA1UdEwQCMAAwCwYDVR0PBAQDAgTwMBMGA1Ud\nJQQMMAoGCCsGAQUFBwMBMA8GA1UdEQQIMAaHBAoeDKkwDQYJKoZIhvcNAQENBQAD\nggIBACfooUrULCRcetYrLHDgYYJip5NA9lSvyxrUvUoYYK6JRtSiR34NOqNiWlN+\n4yJ9D5m87y/hC+gqvx696djz3L5Y+9e1v7SAgP/2uKTHWrvnHwyaVhL6CfJL+Qlh\nxm+nwT1M/y6h+sviwR1MASBvbKIp9PbnJnJ4u3UwEhNEzosbmwPpT+0QqkWFPM2w\nCPd6gTLi0hQZa43sqOG/IsCHhf81LOAjdd9yBlWCWnwp0P6lfKpYX/eximgFSLtj\nX/8s9P5x9gRXC8M669zfeaIZkdUHCVqHMMh2ppeRsLZPqVSns5dzoQE4oCi3mn3U\ns6dsPihmabJU9hBxEjUtYbO67ZOMKDvdwBjYPqUxhV/9Pnf7XmpsWPvM/V+OhM4u\nK27yWtKXFpndXvI1DFuQKSNGawwvVOCfj1jq2b0mUQzVaYusbtBziBygR9lkCKUy\nDZcTy/WYJNt4mLSIoIUu3OF/V0yjMQ8EG9Hvzp53BboKYxqNbP2kRQtLuVgcS0ir\nj2F+Vcdg25uvPdUz6bB7MxZbYd3Ax0PoNEfurqaa5BzlEx0Cd7ei7p5fyhfF5rgZ\nfQmcr2T3UkKjndsVb2xpk9nJltnrspl6HFi/sTnCPheawuxa9oP1FH/M21SR9TA4\nqXxIOVk28HPsXSuEaZjGKQMQbodKGCwNr9mDs3qAKXVp57Mg\n-----END CERTIFICATE-----\n",
      "key_data": "-----BEGIN RSA PRIVATE KEY-----\nMIIJKQIBAAKCAgEAy/NaviOFZuFF7KKnHHIPGOFy6UK6PKHYPhUOc/WnDVV6X6kP\nzWDO3R2T104esKgNnMa1ntLTXqtFz1e39N4jLFy0PC1FldnmET1QxOYl1xkR++5z\nWW+/Ua4wQtPrnLxMFrDX5G4IspCKrS2J96Kpk6BpsAjZ/aHrZ4hLwpl2+D0u1/BT\n9po/esFQDWXifMp5u6N5lqynoIF5tUQqM3cajwH/IKnl2RifvTu871WuYgAMsQLw\nmaOc9Z1OoqRWNUA8njtzrY6JsSMVIWIuTcA6/doFAU6n9vkZyJ20WZIORHnVcR5W\n2GPE0CUd4j3vQpVP599Dx3Kjrf8GyhHB73LDC0TIu7DR9Mxt/sg3pBFs/5xzxwig\nPDQfjDlMNXlJk2FWZFZ9kV+9qvL0ZLX6FSnffhHsccQtUcO5V9kCkfKE2+/yjxlp\naL881U/VGpxQCGUxHmmLgSs+PYKIqsrMh/AjTtSYvQBJZTDhy3P4ns6CLJMGjTjx\nWChOFWrQx2rTMiEsRQESsyBOKDYECgVqzjlHF/xzD/znvukpvJV3W+beFG0enVjQ\n9wRcbfjQqSsbWLVhjzeamFaBv4mI0c0vWtHqIL/BBXugYFj3xBcBixH+Lpt91T/a\n9RAtlP1cvO+BKIEo7IWXDW2wDJ8jr3yVqhc4kS+rGIOM5Sl9yIvqLT1MWsECAwEA\nAQKCAgAZ6qq1Tr48/JNuJp0luDjC6KM5kQkpe0eHXBWiFq1LvHj4fvtLFeoznvaS\nfZLY0AIq0fVyYUgK16jfWD5AF5pQoNcmbnpROIdL2YbR/o0AcGcgpIRz8QdW0dPA\nKj3ehO8GUyKcHH9ucX+t0gOePEVgRRopDHbnDBRl66P07pt3oA670gZZZ/B5IOeT\nTEcjpHcjqPpicz453zogFrFmKNRvJ8nL1Msoc0CZQ2YW48RtH6R9OeppG6lubLb5\nY/iwe6E4WkWw4FQO9m5Q97D6oFretz27lMszTyQ/ogqw9yZo/TJqVXijtsnjyVOq\n1EP7Kg4lYPGz/pVeHvI161vBmcu/AJWbUhuup5eU0aJkgvmfczOW96x8CUWHlqul\ny+uWvezw/BEplR/myk18D7ZPkMUiaDCNHrbCOkbUUxzFlZAhzfJHcryPeStiTsuC\nO0Iu13hphamRRJq9kuPD9KSFXkPa8zVi6y4Cwjd1xaB9OUTkQM1calSzNTjgRmYw\nmLMg+GdXign43376TCbeLsvwgtVHEXldfPmhoXXHq5xJHVCuwieE8IqCPp6ib6Z4\ng1H0hZHTEZIhop21AuD2kU0kr38OH2zTcvWVyrg6dTzW7FGiuN2YUxYHKYiSvVnE\n4HerEG6iGvkTsk/ckwJoFIqHHFvzEFX3Fzg1nh69KVPd9UfpgQKCAQEA90WnSVVp\n+sGtM3unmSX8OtlJB7+p3mtk3OZVHpK+P5B9f0nWF+eEaaPZS/oTMEHfnGTQPdj1\nMC7r9Cbtz3yjSxz6IEEvj43NMka+hEI8Va1hwbAESENLSBvv91IYuPPD8Mu1ZlWc\nt+HQ+Q+Mytgu31YqwZbBD6lin+DpcPdHv5hcVnpnHbPMmvD/POw3eemBsHol/8xs\n1j+Qv8v5lh81jtltT26h+P7OCoilyVJGWrQZT33SQEh72HoZaMri32Mzs5Ib4+mu\nPJZCcj0HpHmoL9EAMnciXB3HN0eo2L8IRTsqgj8ATKCvRzdAl91KlmvxdEkDB+/i\n04OkqgYUCcd3BQKCAQEA0yY/scjA0fknvNfU9ULCEJps70+cu3cjyfpF7nfLvZJK\n5eQgZ8KaS7QxAKyp9wMVz7DIKAYhhjqKku8MFo9+yhaVjo06PV4EmwqEN2VHddbT\nlc94hC3IvbQU0b3/+asznjIoyGbvkQgYFGqUyc70bY2MxgNdfhTp5obkKHgFkcSa\nLSFt5tGiVXGmB2JUYzbrbCyWrHkO1+mlB3gWhg3uRhmwKGL7/NRe0L5LYXaxuSkj\nLJBBoyeR4BcJeaxWmxyEVWBA5mAcF4X9LAs1rqsp4PfM6oUy3twHoM9qVk+qb8Pf\nuD3HbiswAaNM/TtVs109uaFNZITCsdD4mVBS9OApjQKCAQEA8NAL8DZX5RbTqAzo\nFxVQRLuyDPLS60Lp0twaz5CX6W29Wsa800DsyrkAeabNIzU0Iapox6LQfqFjt75l\n4aj/mrpYuirht8ugqDMPfdzHx6T4TFowgXPQECTtGY8BdrYoAA1T15rO6qHoE3ba\nZf4OAAF52FkKIkeTPiMbFaItZOFsI+hHHj0pqUfFOz7NdFQ9snHzKeCbqjfzr2Zl\n5pb0YO9NLouPAOCeJtIXqy4OSG2XLLxbk7FDs3qN3mmgc2+4PUyxDtBYmLa5dWoM\nVFkKu66uo3c0pkN17VdDj/rTgiDx8DCNCROAQDoGFSA1cLMlTluAsS0lWVqedds/\njpqMRQKCAQAwXOtr6kKYFYyPiZQilSbkLKrU6ZRJsBFHewa3h0LoafCz1VvCyGUU\n//HVaLcJd/BwANrnp/fXyeLhotVO+ZEd8qxQ2XJEihtd87uzAISsrgcKolnFVMNN\nCElYfT97TUZmbrC+ri0jOApj6sGns7pyuWBMHos0jM/CWJU727nS2IhD3AtTOiMH\nlR9lQ5V2oCauQUxFtvi6Za7CFjR6gghYkBu0NG/pSi9pepzDdy9f7Nc8ptIR78dO\n35fxAZNYteBtub1DxzHIBY2mn+6s0lGmULvj35x2RUmOANQnbtnn/aJpjeT3C/dT\n+LZyrjuD+NBhi1uxsWLy3Z2DaE2H/ywlAoIBAQDchSiP1gzYDX94+y7dAT/msOam\nZYd0UXEMg5svrdWPUBv4yIgfuuhUMzBh88d2SUqTlaJ/bpoND+7wrWlc5h4tr/X4\nIpR5ZJw3VKUVaqiVp2HR5m72PHCROn5HL0KmY8oj9yGACgpSMdso/xH5b6H1j/bE\nWB35o52VsPu6I3hiUHuvUH+QXFxMGYnV7fpjk/0cC65VilnOxMMgMDLDP57Jr2sD\nsOLhituyB4EFahE+EoOMY99vLpb0vQJkG+4TVVp+Z4KM9yW6zyhTBtaYo1Jyn/dx\n+OPsiniTL1qWdN/bkUmCmF2CltegT7ULXyjEthxVB0XiVJwBnQSA3Go8M81X\n-----END RSA PRIVATE KEY-----\n"
    },
    "timezone_adaptive": true,
    "function_support": {
      "distribute_allow": false,
      "helm_chart_allow": false
    }
  }
}
```

## /v1/container_registry/update
更新harbor镜像仓库
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant_uuid|string|是|""|租户UUID
uuid|string|是|""|仓库uuid
name|string|是|""|仓库名
server_address|string|是|""|仓库地址
user_name|string|是|""|仓库验证用户名
password|string|是|""|仓库验证密码
description|string|否|""|描述
tls_config|struct|是|{}|TLS验证
timezone_adpative|bool|否|false|时区适配
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/update
```
{
	"tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
	"name": "12_169",
	"server_address": "https://10.30.12.169",
	"user_name": "admin",
	"password": "Harbor12345",
	"description": "",
	"tls_config": {
		"ca_data": "-----BEGIN CERTIFICATE-----\nMIIFfzCCA2egAwIBAgIJAJbOuXW9WPh/MA0GCSqGSIb3DQEBDQUAMFYxCzAJBgNV\nBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYD\nVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQZXJzb25hbDAeFw0yMDEwMjkxMzQ2NTRa\nFw0zMDEwMjcxMzQ2NTRaMFYxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYDVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQ\nZXJzb25hbDCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAKSCaaI28DUH\nNUVvpLX5BtUmhohqDlDgTKViHgU1Yf5zyi/bVDkMnhuAUbGItAcEwrIYDn63bjIr\nETFuRNM35D5+5iMon79U1LSqE1v8BTSPi0lwYZBADtQMtFscgzXbXzgOJgGfXfRI\n9jXgV7wrCEpwnWBWbyRt9Y3xKLqay/6znrTm4oFySAXuHytPhD6JmfDZzEZ16Y/h\nCigUDm2NfXOuIksUwSTxztLovCLq+OGWJvItOpQ2F03ZFUoAB0JMllR5s46tvTZZ\nl1kH71UD8vhO30ndlkHIUzT5kfsMYDzJR9foi5QuBk8x2w2utryYhSoQAL6UQF3h\nWQkuZg3svvw3ow00jGkJRRawNhuRST3ehiSsY9g70npjg+etwcATUG/16Ws7Fvfd\nliH9cHMRvM9Jfd1iSBVrQeS+ZUV/m4vuMukJH5+Jj739vD/alI+8tKxaB8HHvqqW\njSd4aI0aXwsmUT/pQU1QztIaB/3eJf3aC1LdRRVZNGARQ1EYjLWnuyJMioxFGol2\nKGYf8bDz0ODrBsjzcIpLmWTkuVWPLhEiDJeKLAgLxpCzDLqI5uDJxSXvG31YMxGB\nBCC9pO4oUwCmKgh/mwqN4NYN9N5BYnsrfcl7WXzDdgriOU8SjmmAZGkR9R+O8wbC\ncK4/qAsR3woE0TBghVSUxiWH8Ov/dVgdAgMBAAGjUDBOMB0GA1UdDgQWBBT/42rI\n/rlTJ5PYC8/XFApCNZNuWTAfBgNVHSMEGDAWgBT/42rI/rlTJ5PYC8/XFApCNZNu\nWTAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBDQUAA4ICAQAQfW+OVjGkIKQoAgjF\nDhBN7MlbrH3G5x26MGw/4NUGDI0iVcVHmIR0VM+3Sq7IzTvsdM5KJtUX2ZEPop3K\n/uLimnpbQPuwaE99H7h/Suvf+zkgSbor+rpB6otwnPe41/jX0/JsncN6oatN23NV\nrU92SdZBHJ8oTDZjgjYpUoco2oF0RWn7ihYqfChQ2o7pFA+B1ElSnA8SPnfcAXEv\nRIeSYDDchaInlgVjZsjv/fwUoNBOyv2xm0hU1d7Lh6gge/JCVN/sufh8s1g/l8b8\nfBKRvz4jcyQcB647rvzkKw/PpcHhNeIm+TJudf9nkH9REmeAUt4SA9u31hV3C0fU\nFKBRXOLrGZjKWCPC85K5bJqhfuRgn/o+cmwxwm7Kkz3lDQ4j71LljWQ1z7ArrmI2\nDIerJ/aVMdEw8Js3YZI8nOiHW4FB01WCVY7cSMVuIFx4fiLSNl/q8qDV28/wjDbV\nQQzX75C/Q4aVCFOsryq0EfAVg16WqEIZlkcjH1D5xx4L58SY+aI08ZeHGg8G6rrH\nZfk9FuHU/gDA+BcpZ+lZhFSm4Kp5benRcERbwai5a6vmzYLfIZN9iwnrYiLSRPJc\n3iCy23b6N8ZNbQiLK7WU2c4fu1Wy2UndXOJmg+NyGstF0HSiaOeUDS41+8nRls2K\nySuHzlhTHTBPvzfNwW5zx9/oFw==\n-----END CERTIFICATE-----\n",
		"key_data": "-----BEGIN RSA PRIVATE KEY-----\n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\n-----END RSA PRIVATE KEY-----\n",
		"cert_data": "-----BEGIN CERTIFICATE-----\nMIIFkDCCA3igAwIBAgIJAJTttkM9W9UiMA0GCSqGSIb3DQEBDQUAMFYxCzAJBgNV\nBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYD\nVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQZXJzb25hbDAeFw0yMDEwMjkxMzQ2NTRa\nFw0zMDEwMjcxMzQ2NTRaMFYxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYDVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQ\nZXJzb25hbDCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAMvzWr4jhWbh\nReyipxxyDxjhculCujyh2D4VDnP1pw1Vel+pD81gzt0dk9dOHrCoDZzGtZ7S016r\nRc9Xt/TeIyxctDwtRZXZ5hE9UMTmJdcZEfvuc1lvv1GuMELT65y8TBaw1+RuCLKQ\niq0tifeiqZOgabAI2f2h62eIS8KZdvg9LtfwU/aaP3rBUA1l4nzKebujeZasp6CB\nebVEKjN3Go8B/yCp5dkYn707vO9VrmIADLEC8JmjnPWdTqKkVjVAPJ47c62OibEj\nFSFiLk3AOv3aBQFOp/b5GcidtFmSDkR51XEeVthjxNAlHeI970KVT+ffQ8dyo63/\nBsoRwe9ywwtEyLuw0fTMbf7IN6QRbP+cc8cIoDw0H4w5TDV5SZNhVmRWfZFfvary\n9GS1+hUp334R7HHELVHDuVfZApHyhNvv8o8ZaWi/PNVP1RqcUAhlMR5pi4ErPj2C\niKrKzIfwI07UmL0ASWUw4ctz+J7OgiyTBo048VgoThVq0Mdq0zIhLEUBErMgTig2\nBAoFas45Rxf8cw/8577pKbyVd1vm3hRtHp1Y0PcEXG340KkrG1i1YY83mphWgb+J\niNHNL1rR6iC/wQV7oGBY98QXAYsR/i6bfdU/2vUQLZT9XLzvgSiBKOyFlw1tsAyf\nI698laoXOJEvqxiDjOUpfciL6i09TFrBAgMBAAGjYTBfMB8GA1UdIwQYMBaAFP/j\nasj+uVMnk9gLz9cUCkI1k25ZMAkGA1UdEwQCMAAwCwYDVR0PBAQDAgTwMBMGA1Ud\nJQQMMAoGCCsGAQUFBwMBMA8GA1UdEQQIMAaHBAoeDKkwDQYJKoZIhvcNAQENBQAD\nggIBACfooUrULCRcetYrLHDgYYJip5NA9lSvyxrUvUoYYK6JRtSiR34NOqNiWlN+\n4yJ9D5m87y/hC+gqvx696djz3L5Y+9e1v7SAgP/2uKTHWrvnHwyaVhL6CfJL+Qlh\nxm+nwT1M/y6h+sviwR1MASBvbKIp9PbnJnJ4u3UwEhNEzosbmwPpT+0QqkWFPM2w\nCPd6gTLi0hQZa43sqOG/IsCHhf81LOAjdd9yBlWCWnwp0P6lfKpYX/eximgFSLtj\nX/8s9P5x9gRXC8M669zfeaIZkdUHCVqHMMh2ppeRsLZPqVSns5dzoQE4oCi3mn3U\ns6dsPihmabJU9hBxEjUtYbO67ZOMKDvdwBjYPqUxhV/9Pnf7XmpsWPvM/V+OhM4u\nK27yWtKXFpndXvI1DFuQKSNGawwvVOCfj1jq2b0mUQzVaYusbtBziBygR9lkCKUy\nDZcTy/WYJNt4mLSIoIUu3OF/V0yjMQ8EG9Hvzp53BboKYxqNbP2kRQtLuVgcS0ir\nj2F+Vcdg25uvPdUz6bB7MxZbYd3Ax0PoNEfurqaa5BzlEx0Cd7ei7p5fyhfF5rgZ\nfQmcr2T3UkKjndsVb2xpk9nJltnrspl6HFi/sTnCPheawuxa9oP1FH/M21SR9TA4\nqXxIOVk28HPsXSuEaZjGKQMQbodKGCwNr9mDs3qAKXVp57Mg\n-----END CERTIFICATE-----\n"
	},
	"timezone_adaptive": true,
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
    "uuid": "aa67f46f-2565-437e-9a7e-fba2d6f46d48",
    "tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
    "tenant_name": "dev",
    "name": "12_169",
    "server_address": "https://10.30.12.169",
    "create_time": 1629786029,
    "description": "sdfsfs",
    "user_name": "admin",
    "password": "",
    "status": "healthy",
    "status_detail": "",
    "tls_config": {
      "ca_data": "-----BEGIN CERTIFICATE-----\nMIIFfzCCA2egAwIBAgIJAJbOuXW9WPh/MA0GCSqGSIb3DQEBDQUAMFYxCzAJBgNV\nBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYD\nVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQZXJzb25hbDAeFw0yMDEwMjkxMzQ2NTRa\nFw0zMDEwMjcxMzQ2NTRaMFYxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYDVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQ\nZXJzb25hbDCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAKSCaaI28DUH\nNUVvpLX5BtUmhohqDlDgTKViHgU1Yf5zyi/bVDkMnhuAUbGItAcEwrIYDn63bjIr\nETFuRNM35D5+5iMon79U1LSqE1v8BTSPi0lwYZBADtQMtFscgzXbXzgOJgGfXfRI\n9jXgV7wrCEpwnWBWbyRt9Y3xKLqay/6znrTm4oFySAXuHytPhD6JmfDZzEZ16Y/h\nCigUDm2NfXOuIksUwSTxztLovCLq+OGWJvItOpQ2F03ZFUoAB0JMllR5s46tvTZZ\nl1kH71UD8vhO30ndlkHIUzT5kfsMYDzJR9foi5QuBk8x2w2utryYhSoQAL6UQF3h\nWQkuZg3svvw3ow00jGkJRRawNhuRST3ehiSsY9g70npjg+etwcATUG/16Ws7Fvfd\nliH9cHMRvM9Jfd1iSBVrQeS+ZUV/m4vuMukJH5+Jj739vD/alI+8tKxaB8HHvqqW\njSd4aI0aXwsmUT/pQU1QztIaB/3eJf3aC1LdRRVZNGARQ1EYjLWnuyJMioxFGol2\nKGYf8bDz0ODrBsjzcIpLmWTkuVWPLhEiDJeKLAgLxpCzDLqI5uDJxSXvG31YMxGB\nBCC9pO4oUwCmKgh/mwqN4NYN9N5BYnsrfcl7WXzDdgriOU8SjmmAZGkR9R+O8wbC\ncK4/qAsR3woE0TBghVSUxiWH8Ov/dVgdAgMBAAGjUDBOMB0GA1UdDgQWBBT/42rI\n/rlTJ5PYC8/XFApCNZNuWTAfBgNVHSMEGDAWgBT/42rI/rlTJ5PYC8/XFApCNZNu\nWTAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBDQUAA4ICAQAQfW+OVjGkIKQoAgjF\nDhBN7MlbrH3G5x26MGw/4NUGDI0iVcVHmIR0VM+3Sq7IzTvsdM5KJtUX2ZEPop3K\n/uLimnpbQPuwaE99H7h/Suvf+zkgSbor+rpB6otwnPe41/jX0/JsncN6oatN23NV\nrU92SdZBHJ8oTDZjgjYpUoco2oF0RWn7ihYqfChQ2o7pFA+B1ElSnA8SPnfcAXEv\nRIeSYDDchaInlgVjZsjv/fwUoNBOyv2xm0hU1d7Lh6gge/JCVN/sufh8s1g/l8b8\nfBKRvz4jcyQcB647rvzkKw/PpcHhNeIm+TJudf9nkH9REmeAUt4SA9u31hV3C0fU\nFKBRXOLrGZjKWCPC85K5bJqhfuRgn/o+cmwxwm7Kkz3lDQ4j71LljWQ1z7ArrmI2\nDIerJ/aVMdEw8Js3YZI8nOiHW4FB01WCVY7cSMVuIFx4fiLSNl/q8qDV28/wjDbV\nQQzX75C/Q4aVCFOsryq0EfAVg16WqEIZlkcjH1D5xx4L58SY+aI08ZeHGg8G6rrH\nZfk9FuHU/gDA+BcpZ+lZhFSm4Kp5benRcERbwai5a6vmzYLfIZN9iwnrYiLSRPJc\n3iCy23b6N8ZNbQiLK7WU2c4fu1Wy2UndXOJmg+NyGstF0HSiaOeUDS41+8nRls2K\nySuHzlhTHTBPvzfNwW5zx9/oFw==\n-----END CERTIFICATE-----\n",
      "cert_data": "-----BEGIN CERTIFICATE-----\nMIIFkDCCA3igAwIBAgIJAJTttkM9W9UiMA0GCSqGSIb3DQEBDQUAMFYxCzAJBgNV\nBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYD\nVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQZXJzb25hbDAeFw0yMDEwMjkxMzQ2NTRa\nFw0zMDEwMjcxMzQ2NTRaMFYxCzAJBgNVBAYTAkNOMRAwDgYDVQQIDAdCZWlqaW5n\nMRAwDgYDVQQHDAdCZWlqaW5nMRAwDgYDVQQKDAdleGFtcGxlMREwDwYDVQQLDAhQ\nZXJzb25hbDCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAMvzWr4jhWbh\nReyipxxyDxjhculCujyh2D4VDnP1pw1Vel+pD81gzt0dk9dOHrCoDZzGtZ7S016r\nRc9Xt/TeIyxctDwtRZXZ5hE9UMTmJdcZEfvuc1lvv1GuMELT65y8TBaw1+RuCLKQ\niq0tifeiqZOgabAI2f2h62eIS8KZdvg9LtfwU/aaP3rBUA1l4nzKebujeZasp6CB\nebVEKjN3Go8B/yCp5dkYn707vO9VrmIADLEC8JmjnPWdTqKkVjVAPJ47c62OibEj\nFSFiLk3AOv3aBQFOp/b5GcidtFmSDkR51XEeVthjxNAlHeI970KVT+ffQ8dyo63/\nBsoRwe9ywwtEyLuw0fTMbf7IN6QRbP+cc8cIoDw0H4w5TDV5SZNhVmRWfZFfvary\n9GS1+hUp334R7HHELVHDuVfZApHyhNvv8o8ZaWi/PNVP1RqcUAhlMR5pi4ErPj2C\niKrKzIfwI07UmL0ASWUw4ctz+J7OgiyTBo048VgoThVq0Mdq0zIhLEUBErMgTig2\nBAoFas45Rxf8cw/8577pKbyVd1vm3hRtHp1Y0PcEXG340KkrG1i1YY83mphWgb+J\niNHNL1rR6iC/wQV7oGBY98QXAYsR/i6bfdU/2vUQLZT9XLzvgSiBKOyFlw1tsAyf\nI698laoXOJEvqxiDjOUpfciL6i09TFrBAgMBAAGjYTBfMB8GA1UdIwQYMBaAFP/j\nasj+uVMnk9gLz9cUCkI1k25ZMAkGA1UdEwQCMAAwCwYDVR0PBAQDAgTwMBMGA1Ud\nJQQMMAoGCCsGAQUFBwMBMA8GA1UdEQQIMAaHBAoeDKkwDQYJKoZIhvcNAQENBQAD\nggIBACfooUrULCRcetYrLHDgYYJip5NA9lSvyxrUvUoYYK6JRtSiR34NOqNiWlN+\n4yJ9D5m87y/hC+gqvx696djz3L5Y+9e1v7SAgP/2uKTHWrvnHwyaVhL6CfJL+Qlh\nxm+nwT1M/y6h+sviwR1MASBvbKIp9PbnJnJ4u3UwEhNEzosbmwPpT+0QqkWFPM2w\nCPd6gTLi0hQZa43sqOG/IsCHhf81LOAjdd9yBlWCWnwp0P6lfKpYX/eximgFSLtj\nX/8s9P5x9gRXC8M669zfeaIZkdUHCVqHMMh2ppeRsLZPqVSns5dzoQE4oCi3mn3U\ns6dsPihmabJU9hBxEjUtYbO67ZOMKDvdwBjYPqUxhV/9Pnf7XmpsWPvM/V+OhM4u\nK27yWtKXFpndXvI1DFuQKSNGawwvVOCfj1jq2b0mUQzVaYusbtBziBygR9lkCKUy\nDZcTy/WYJNt4mLSIoIUu3OF/V0yjMQ8EG9Hvzp53BboKYxqNbP2kRQtLuVgcS0ir\nj2F+Vcdg25uvPdUz6bB7MxZbYd3Ax0PoNEfurqaa5BzlEx0Cd7ei7p5fyhfF5rgZ\nfQmcr2T3UkKjndsVb2xpk9nJltnrspl6HFi/sTnCPheawuxa9oP1FH/M21SR9TA4\nqXxIOVk28HPsXSuEaZjGKQMQbodKGCwNr9mDs3qAKXVp57Mg\n-----END CERTIFICATE-----\n",
      "key_data": "-----BEGIN RSA PRIVATE KEY-----\n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\n-----END RSA PRIVATE KEY-----\n"
    },
    "timezone_adaptive": true,
    "function_support": {
      "distribute_allow": false,
      "helm_chart_allow": false
    }
  }
}
```
## /v1/container_registry/search
搜素harbor镜像仓库
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
tenant_uuid|string|是|""|租户uuid
query|string|是|""|查询镜像名

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/search?tenant_uuid=ca0179d2-d5cb-4731-aca2-2309fe382fee&query=ngin

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "results": [
      {
        "registry": {
          "uuid": "4659b9b6-b1b4-4c41-90c7-15c497f71f56",
          "tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
          "tenant_name": "dev",
          "name": "176",
          "server_address": "https://10.30.100.176",
          "create_time": 1628498204,
          "description": "",
          "user_name": "admin",
          "password": "",
          "status": "connect-error",
          "status_detail": "registry client create fail",
          "tls_config": null,
          "timezone_adaptive": true,
          "function_support": {
            "distribute_allow": false,
            "helm_chart_allow": false
          }
        },
        "result": null,
        "error": {
          "code": 17030,
          "message": "registry is unhealthy",
          "messageCn": "镜像仓库不健康",
          "stack": [
            "host:10.30.100.178,pid:4031,module:manager,code:17030,filename:registry.go,func:func1,line:413"
          ],
          "desc": "registry client create fail",
          "UUID": "bd8ac076-5508-4f86-9aab-f1b7f035d24b"
        }
      },
      {
        "registry": {
          "uuid": "9cbd63e0-2d42-4e52-bb5e-80b861cc868a",
          "tenant_uuid": "ca0179d2-d5cb-4731-aca2-2309fe382fee",
          "tenant_name": "dev",
          "name": "155",
          "server_address": "https://10.30.100.155",
          "create_time": 1628498676,
          "description": "",
          "user_name": "admin",
          "password": "",
          "status": "healthy",
          "status_detail": "",
          "tls_config": null,
          "timezone_adaptive": true,
          "function_support": {
            "distribute_allow": false,
            "helm_chart_allow": false
          }
        },
        "result": {
          "project": [],
          "repository": [
            {
              "description": "",
              "id": 0,
              "name": "",
              "project_id": 2,
              "project_name": "k8s",
              "repository_name": "k8s/k8s.gcr.io/ingress-nginx/controller",
              "artifact_count": 0,
              "pull_count": 5,
              "star_count": 0,
              "tags_count": 1
            },
            {
              "description": "",
              "id": 0,
              "name": "",
              "project_id": 1,
              "project_name": "library",
              "repository_name": "library/nginx",
              "artifact_count": 0,
              "pull_count": 0,
              "star_count": 0,
              "tags_count": 4
            },
            {
              "description": "",
              "id": 0,
              "name": "",
              "project_id": 5,
              "project_name": "newk8s",
              "repository_name": "newk8s/k8s.gcr.io/ingress-nginx/controller",
              "artifact_count": 0,
              "pull_count": 0,
              "star_count": 0,
              "tags_count": 1
            }
          ]
        },
        "error": null
      }
    ]
  }
}
```

## /v1/container_registry/project/list
harbor镜像仓库项目列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
page_num|int|否|0|页数
page_size|int|否|0|页大小
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/project/list?page_size=10&registry_uuid=9cbd63e0-2d42-4e52-bb5e-80b861cc868a&page_num=0&fuzzy=

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
        "project_id": 2,
        "owner_id": 1,
        "name": "k8s",
        "creation_time": "2021-06-25T01:20:36Z",
        "update_time": "2021-06-25T01:20:36Z",
        "creation_time_unix": 1624584036,
        "update_time_unix": 1624584036,
        "deleted": false,
        "owner_name": "",
        "current_user_role_id": 1,
        "current_user_role_ids": [
          1
        ],
        "repo_count": 81,
        "chart_count": 0,
        "metadata": {
          "auto_scan": "false",
          "enable_content_trust": "false",
          "prevent_vul": "false",
          "public": "false",
          "reuse_sys_cve_whitelist": "false"
        },
        "cve_whitelist": {
          "id": 0,
          "project_id": 0,
          "items": null,
          "creation_time": "0001-01-01T00:00:00Z",
          "update_time": "0001-01-01T00:00:00Z",
          "creation_time_unix": 0,
          "update_time_unix": 0
        }
      },
      {
        "project_id": 1,
        "owner_id": 1,
        "name": "library",
        "creation_time": "2021-06-25T01:16:38.347037Z",
        "update_time": "2021-06-25T01:16:38.347037Z",
        "creation_time_unix": 1624583798,
        "update_time_unix": 1624583798,
        "deleted": false,
        "owner_name": "",
        "current_user_role_id": 1,
        "current_user_role_ids": [
          1
        ],
        "repo_count": 9,
        "chart_count": 0,
        "metadata": {
          "auto_scan": "false",
          "enable_content_trust": "false",
          "prevent_vul": "false",
          "public": "true",
          "reuse_sys_cve_whitelist": ""
        },
        "cve_whitelist": {
          "id": 0,
          "project_id": 0,
          "items": null,
          "creation_time": "0001-01-01T00:00:00Z",
          "update_time": "0001-01-01T00:00:00Z",
          "creation_time_unix": 0,
          "update_time_unix": 0
        }
      },
      {
        "project_id": 5,
        "owner_id": 1,
        "name": "newk8s",
        "creation_time": "2021-07-07T07:38:01Z",
        "update_time": "2021-07-07T07:38:01Z",
        "creation_time_unix": 1625643481,
        "update_time_unix": 1625643481,
        "deleted": false,
        "owner_name": "",
        "current_user_role_id": 1,
        "current_user_role_ids": [
          1
        ],
        "repo_count": 41,
        "chart_count": 0,
        "metadata": {
          "auto_scan": "false",
          "enable_content_trust": "false",
          "prevent_vul": "false",
          "public": "false",
          "reuse_sys_cve_whitelist": ""
        },
        "cve_whitelist": {
          "id": 0,
          "project_id": 0,
          "items": null,
          "creation_time": "0001-01-01T00:00:00Z",
          "update_time": "0001-01-01T00:00:00Z",
          "creation_time_unix": 0,
          "update_time_unix": 0
        }
      },
      {
        "project_id": 3,
        "owner_id": 1,
        "name": "shop",
        "creation_time": "2021-06-29T12:22:44Z",
        "update_time": "2021-06-29T12:22:44Z",
        "creation_time_unix": 1624969364,
        "update_time_unix": 1624969364,
        "deleted": false,
        "owner_name": "",
        "current_user_role_id": 1,
        "current_user_role_ids": [
          1
        ],
        "repo_count": 17,
        "chart_count": 0,
        "metadata": {
          "auto_scan": "false",
          "enable_content_trust": "false",
          "prevent_vul": "false",
          "public": "false",
          "reuse_sys_cve_whitelist": ""
        },
        "cve_whitelist": {
          "id": 0,
          "project_id": 0,
          "items": null,
          "creation_time": "0001-01-01T00:00:00Z",
          "update_time": "0001-01-01T00:00:00Z",
          "creation_time_unix": 0,
          "update_time_unix": 0
        }
      },
      {
        "project_id": 4,
        "owner_id": 1,
        "name": "xxx",
        "creation_time": "2021-07-07T05:58:31Z",
        "update_time": "2021-07-07T05:58:31Z",
        "creation_time_unix": 1625637511,
        "update_time_unix": 1625637511,
        "deleted": false,
        "owner_name": "",
        "current_user_role_id": 1,
        "current_user_role_ids": [
          1
        ],
        "repo_count": 0,
        "chart_count": 0,
        "metadata": {
          "auto_scan": "false",
          "enable_content_trust": "false",  
          "prevent_vul": "false",
          "public": "false",
          "reuse_sys_cve_whitelist": ""
        },
        "cve_whitelist": {
          "id": 0,
          "project_id": 0,
          "items": null,
          "creation_time": "0001-01-01T00:00:00Z",
          "update_time": "0001-01-01T00:00:00Z",
          "creation_time_unix": 0,
          "update_time_unix": 0
        }
      }
    ],
    "total_count": 5
  }
}
```

## /v1/container_registry/project/get
harbor镜像仓库项目详情
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
project_id|int|是|0|项目id
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例

https://10.30.100.178/v1/container_registry/project/get?registry_uuid=9cbd63e0-2d42-4e52-bb5e-80b861cc868a&project_id=2
#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "project_id": 2,
    "owner_id": 1,
    "name": "k8s",
    "creation_time": "2021-06-25T01:20:36Z",
    "update_time": "2021-06-25T01:20:36Z",
    "creation_time_unix": 1624584036,
    "update_time_unix": 1624584036,
    "deleted": false,
    "owner_name": "",
    "current_user_role_id": 1,
    "current_user_role_ids": [
      1
    ],
    "repo_count": 81,
    "chart_count": 0,
    "metadata": {
      "auto_scan": "false",
      "enable_content_trust": "false",
      "prevent_vul": "false",
      "public": "false",
      "reuse_sys_cve_whitelist": "false"
    },
    "cve_whitelist": {
      "id": 1,
      "project_id": 2,
      "items": [
        {
          "cve_id": "sdfsfsf"
        },
        {
          "cve_id": "sdfsfsdfsd"
        },
        {
          "cve_id": "xxxxxx"
        }
      ],
      "creation_time": "2021-08-09T08:45:21.158913Z",
      "update_time": "2021-08-09T08:45:21.158914Z",
      "creation_time_unix": 0,
      "update_time_unix": 0
    }
  }
}
```

## /v1/container_registry/project/create
harbor镜像仓库项目创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
project_name|string|是|""|项目名
metadata|struct|是|{}|项目配置
storage_limit|int|是|0|项目存储容量配额
count_limit|int|是|0|项目镜像配额
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/project/create
```
{
	"registry_uuid": "9cbd63e0-2d42-4e52-bb5e-80b861cc868a",
	"project_name": "test",
	"metadata": {
		"public": "true"
	},
	"storage_limit": -1,
	"count_limit": 1000
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

## /v1/container_registry/project/delete
harbor镜像仓库项目删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
project_id|int|是|0|项目id
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/project/delete
```
{
	"project_id": 12,
	"registry_uuid": "9cbd63e0-2d42-4e52-bb5e-80b861cc868a"
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

## /v1/container_registry/project/update
harbor镜像仓库项目更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
project_id|int|是|0|项目id
metadata|struct|是|{}|项目配置
cve_whitelist|array|否|[]|漏洞白名单

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/project/update
```
{
	"registry_uuid": "9cbd63e0-2d42-4e52-bb5e-80b861cc868a",
	"project_id": 13,
	"metadata": {
		"public": "false",
		"prevent_vul": "false",
		"auto_scan": "false",
		"enable_content_trust": "false",
		"reuse_sys_cve_whitelist": "true"
	},
	"cve_whitelist": {
		"items": [],
		"expires_at": null
	}
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
## /v1/container_registry/project/summary
harbor镜像仓库项目汇总
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
project_id|int|是|0|项目id
project_name|string|是|""|项目名
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/project/summary?registry_uuid=9cbd63e0-2d42-4e52-bb5e-80b861cc868a&project_id=2&project_name=k8s

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "repo_count": 81,
    "chart_count": 0,
    "project_admin_count": 1,
    "master_count": 0,
    "developer_count": 0,
    "guest_count": 0,
    "limited_guest_count": 0,
    "quota": {
      "hard": {
        "count": -1,
        "storage": -1
      },
      "used": {
        "count": 93,
        "storage": 1991200726
      }
    }
  }
}
```
## /v1/container_registry/log
harbor镜像仓库日志
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
page_num|int|否|0|页数
page_size|int|否|0|页大小
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/log?page_size=10&registry_uuid=9cbd63e0-2d42-4e52-bb5e-80b861cc868a&page_num=0

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
        "log_id": 1643,
        "username": "admin",
        "project_id": 13,
        "repo_name": "test/",
        "repo_tag": "N/A",
        "guid": "",
        "operation": "create",
        "op_time": "2021-08-24T06:35:45.637644Z",
        "op_time_unix": 0,
        "id": 0,
        "resource": "",
        "resource_type": ""
      },
      {
        "log_id": 1642,
        "username": "admin",
        "project_id": 12,
        "repo_name": "test/",
        "repo_tag": "N/A",
        "guid": "",
        "operation": "delete",
        "op_time": "2021-08-24T06:33:48.987429Z",
        "op_time_unix": 0,
        "id": 0,
        "resource": "",
        "resource_type": ""
      },
      {
        "log_id": 1641,
        "username": "admin",
        "project_id": 12,
        "repo_name": "test/",
        "repo_tag": "N/A",
        "guid": "",
        "operation": "create",
        "op_time": "2021-08-24T06:32:29.926777Z",
        "op_time_unix": 0,
        "id": 0,
        "resource": "",
        "resource_type": ""
      },
      {
        "log_id": 1640,
        "username": "admin",
        "project_id": 5,
        "repo_name": "newk8s/quay.io/external_storage/nfs-subdir-external-provisioner",
        "repo_tag": "",
        "guid": "",
        "operation": "pull",
        "op_time": "2021-08-13T06:24:35.11607Z",
        "op_time_unix": 0,
        "id": 0,
        "resource": "",
        "resource_type": ""
      },
      {
        "log_id": 1639,
        "username": "admin",
        "project_id": 5,
        "repo_name": "newk8s/quay.io/external_storage/nfs-subdir-external-provisioner",
        "repo_tag": "v4.0.0",
        "guid": "",
        "operation": "pull",
        "op_time": "2021-08-13T06:24:35.040418Z",
        "op_time_unix": 0,
        "id": 0,
        "resource": "",
        "resource_type": ""
      },
      {
        "log_id": 1638,
        "username": "admin",
        "project_id": 1,
        "repo_name": "library/ubuntu-debug",
        "repo_tag": "",
        "guid": "",
        "operation": "pull",
        "op_time": "2021-08-11T06:09:49.411614Z",
        "op_time_unix": 0,
        "id": 0,
        "resource": "",
        "resource_type": ""
      },
      {
        "log_id": 1637,
        "username": "admin",
        "project_id": 1,
        "repo_name": "library/ubuntu-debug",
        "repo_tag": "1",
        "guid": "",
        "operation": "pull",
        "op_time": "2021-08-11T06:09:49.334937Z",
        "op_time_unix": 0,
        "id": 0,
        "resource": "",
        "resource_type": ""
      },
      {
        "log_id": 1636,
        "username": "harbor-jobservice",
        "project_id": 1,
        "repo_name": "library/golang",
        "repo_tag": "1.13.9-alpine",
        "guid": "",
        "operation": "push",
        "op_time": "2021-08-11T06:08:44.063905Z",
        "op_time_unix": 0,
        "id": 0,
        "resource": "",
        "resource_type": ""
      },
      {
        "log_id": 1635,
        "username": "harbor-jobservice",
        "project_id": 1,
        "repo_name": "library/golang",
        "repo_tag": "1.13",
        "guid": "",
        "operation": "push",
        "op_time": "2021-08-11T06:08:39.072809Z",
        "op_time_unix": 0,
        "id": 0,
        "resource": "",
        "resource_type": ""
      },
      {
        "log_id": 1634,
        "username": "harbor-jobservice",
        "project_id": 1,
        "repo_name": "library/mysql",
        "repo_tag": "v12",
        "guid": "",
        "operation": "push",
        "op_time": "2021-08-11T06:08:36.959988Z",
        "op_time_unix": 0,
        "id": 0,
        "resource": "",
        "resource_type": ""
      }
    ],
    "total_count": 1643
  }
}
```

## /v1/container_registry/remote_registry/list
harbor远端镜像仓库列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
page_num|int|否|0|页数
page_size|int|否|0|页大小
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/remote_registry/list?page_size=10&registry_uuid=9cbd63e0-2d42-4e52-bb5e-80b861cc868a&page_num=0

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
        "id": 1,
        "name": "169",
        "description": "",
        "type": "harbor",
        "url": "https://10.30.12.169",
        "credential": {
          "type": "basic",
          "access_key": "admin",
          "access_secret": "*****"
        },
        "insecure": true,
        "status": "healthy",
        "creation_time": "2021-06-29T12:22:04.043795Z",
        "update_time": "2021-08-24T06:33:40.416366Z",
        "creation_time_unix": 1624969324,
        "update_time_unix": 1629786820
      },
      {
        "id": 2,
        "name": "aaa",
        "description": "",
        "type": "harbor",
        "url": "https://10.30.100.185",
        "credential": {
          "type": "basic",
          "access_key": "admin",
          "access_secret": "*****"
        },
        "insecure": true,
        "status": "healthy",
        "creation_time": "2021-08-03T08:53:21.556692Z",
        "update_time": "2021-08-24T06:33:40.493831Z",
        "creation_time_unix": 1627980801,
        "update_time_unix": 1629786820
      },
      {
        "id": 3,
        "name": "bbb",
        "description": "",
        "type": "harbor",
        "url": "https://10.30.100.185",
        "credential": {
          "type": "",
          "access_key": "",
          "access_secret": ""
        },
        "insecure": true,
        "status": "healthy",
        "creation_time": "2021-08-03T08:54:06.022394Z",
        "update_time": "2021-08-24T06:33:40.511893Z",
        "creation_time_unix": 1627980846,
        "update_time_unix": 1629786820
      }
    ],
    "total_count": 3
  }
}
```

## /v1/container_registry/remote_registry/create
harbor远端镜像仓库添加
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
name|string|是|""|镜像仓库名
description|string|否|""|镜像仓库描述
url|string|是|""|镜像仓库url
type|string|是|""|镜像仓库类型
credential|struct|否|{}|镜像仓库验证
insecure|bool|否|false|不安全连接
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/remote_registry/create
```
{
	"registry_uuid": "9cbd63e0-2d42-4e52-bb5e-80b861cc868a",
	"name": "169",
	"description": "",
	"url": "https://10.30.12.169",
	"type": "harbor",
	"credential": {
		"access_key": "admin",
		"access_secret": "Harbor12345"
	},
	"insecure": true
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

## /v1/container_registry/remote_registry/delete
harbor远端镜像仓库删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
id|int|是|0|镜像仓库id

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/remote_registry/delete
```
{
	"registry_uuid": "9cbd63e0-2d42-4e52-bb5e-80b861cc868a",
	"id": 3
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

## /v1/container_registry/remote_registry/update
harbor远端镜像仓库更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
name|string|是|""|镜像仓库名
description|string|否|""|镜像仓库描述
url|string|是|""|镜像仓库url
type|string|是|""|镜像仓库类型
credential|struct|否|{}|镜像仓库验证
insecure|bool|否|false|不安全连接
id|int|是|0|镜像仓库id

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/remote_registry/update
```
{
	"registry_uuid": "9cbd63e0-2d42-4e52-bb5e-80b861cc868a",
	"name": "169",
	"description": "sdffssdfsfs",
	"url": "https://10.30.12.169",
	"type": "harbor",
	"credential": {
		"access_key": "admin",
		"access_secret": "Harbor12345"
	},
	"insecure": true,
	"id": 1
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


## /v1/container_registry/remote_registry/ping
harbor远端镜像仓库连接测试
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
name|string|是|""|镜像仓库名
description|string|否|""|镜像仓库描述
url|string|是|""|镜像仓库url
type|string|是|""|镜像仓库类型
credential|struct|否|{}|镜像仓库验证
insecure|bool|否|false|不安全连接
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/remote_registry/ping
```
{
	"registry_uuid": "9cbd63e0-2d42-4e52-bb5e-80b861cc868a",
	"name": "169",
	"description": "sdffs",
	"url": "https://10.30.12.169",
	"type": "harbor",
	"credential": {
		"access_key": "admin",
		"access_secret": "Harbor12345"
	},
	"insecure": true
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

## /v1/container_registry/replication/adapter/names
复制适配器列表
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


## /v1/container_registry/replication/adapter/infos
复制适配器详情
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


## /v1/container_registry/replication/policy/list
复制策略列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
page_num|int|否|0|页数
page_size|int|否|0|页大小
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/replication/policy/list?page_size=10&page_num=0&registry_uuid=9cbd63e0-2d42-4e52-bb5e-80b861cc868a    

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
        "id": 2,
        "name": "169-newk8s",
        "description": "",
        "creator": "",
        "src_registry": {
          "id": 1,
          "name": "169",
          "description": "sdffssdfsfs",
          "type": "harbor",
          "url": "https://10.30.12.169",
          "credential": {
            "type": "basic",
            "access_key": "admin",
            "access_secret": "*****"
          },
          "insecure": true,
          "status": "healthy",
          "creation_time": "2021-06-29T12:22:04.043795Z",
          "update_time": "2021-08-24T06:48:40.49839Z",
          "creation_time_unix": 0,
          "update_time_unix": 0
        },
        "dest_registry": {
          "id": 0,
          "name": "Local",
          "description": "",
          "type": "harbor",
          "url": "http://core:8080",
          "token_service_url": "http://core:8080/service/token",
          "credential": {
            "type": "secret",
            "access_key": "",
            "access_secret": "*****"
          },
          "insecure": true,
          "status": "healthy",
          "creation_time": "0001-01-01T00:00:00Z",
          "update_time": "0001-01-01T00:00:00Z",
          "creation_time_unix": 0,
          "update_time_unix": 0
        },
        "dest_namespace": "k8s",
        "filters": [
          {
            "type": "name",
            "value": "newk8s/**"
          },
          {
            "type": "label",
            "value": []
          }
        ],
        "trigger": {
          "type": "manual",
          "trigger_settings": {
            "cron": "* * * * * *"
          }
        },
        "deletion": false,
        "override": true,
        "enabled": true,
        "creation_time": "2021-07-07T07:22:50.112397Z",
        "update_time": "2021-07-22T08:47:54.90451Z",
        "creation_time_unix": 1625642570,
        "update_time_unix": 1626943674
      },
      {
        "id": 1,
        "name": "169",
        "description": "",
        "creator": "",
        "src_registry": {
          "id": 1,
          "name": "169",
          "description": "sdffssdfsfs",
          "type": "harbor",
          "url": "https://10.30.12.169",
          "credential": {
            "type": "basic",
            "access_key": "admin",
            "access_secret": "*****"
          },
          "insecure": true,
          "status": "healthy",
          "creation_time": "2021-06-29T12:22:04.043795Z",
          "update_time": "2021-08-24T06:48:40.49839Z",
          "creation_time_unix": 0,
          "update_time_unix": 0
        },
        "dest_registry": {
          "id": 0,
          "name": "Local",
          "description": "",
          "type": "harbor",
          "url": "http://core:8080",
          "token_service_url": "http://core:8080/service/token",
          "credential": {
            "type": "secret",
            "access_key": "",
            "access_secret": "*****"
          },
          "insecure": true,
          "status": "healthy",
          "creation_time": "0001-01-01T00:00:00Z",
          "update_time": "0001-01-01T00:00:00Z",
          "creation_time_unix": 0,
          "update_time_unix": 0
        },
        "dest_namespace": "",
        "filters": [
          {
            "type": "name",
            "value": "shop/**"
          },
          {
            "type": "label",
            "value": []
          }
        ],
        "trigger": {
          "type": "manual",
          "trigger_settings": {
            "cron": "* * * * * *"
          }
        },
        "deletion": false,
        "override": true,
        "enabled": true,
        "creation_time": "2021-06-29T12:22:32.943625Z",
        "update_time": "2021-08-03T08:33:37.015447Z",
        "creation_time_unix": 1624969352,
        "update_time_unix": 1627979617
      },
      {
        "id": 3,
        "name": "library",
        "description": "",
        "creator": "",
        "src_registry": {
          "id": 1,
          "name": "169",
          "description": "sdffssdfsfs",
          "type": "harbor",
          "url": "https://10.30.12.169",
          "credential": {
            "type": "basic",
            "access_key": "admin",
            "access_secret": "*****"
          },
          "insecure": true,
          "status": "healthy",
          "creation_time": "2021-06-29T12:22:04.043795Z",
          "update_time": "2021-08-24T06:48:40.49839Z",
          "creation_time_unix": 0,
          "update_time_unix": 0
        },
        "dest_registry": {
          "id": 0,
          "name": "Local",
          "description": "",
          "type": "harbor",
          "url": "http://core:8080",
          "token_service_url": "http://core:8080/service/token",
          "credential": {
            "type": "secret",
            "access_key": "",
            "access_secret": "*****"
          },
          "insecure": true,
          "status": "healthy",
          "creation_time": "0001-01-01T00:00:00Z",
          "update_time": "0001-01-01T00:00:00Z",
          "creation_time_unix": 0,
          "update_time_unix": 0
        },
        "dest_namespace": "",
        "filters": [
          {
            "type": "name",
            "value": "library/**"
          },
          {
            "type": "label",
            "value": []
          }
        ],
        "trigger": {
          "type": "manual",
          "trigger_settings": {
            "cron": "* * * * * *"
          }
        },
        "deletion": false,
        "override": true,
        "enabled": true,
        "creation_time": "2021-08-11T06:08:04.514345Z",
        "update_time": "2021-08-11T06:08:12.53239Z",
        "creation_time_unix": 1628662084,
        "update_time_unix": 1628662092
      }
    ],
    "total_count": 3
  }
}
```

## /v1/container_registry/replication/policy/create
复制策略创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
name|string|是|""|策略名
description|string|否 |""|描述
trigger|struct|是|""|触发策略
filters|struct|是|""|过滤
deletion|bool|否|false| 是否删除
override|bool|是|false|覆盖已存在的镜像
dest_registry|struct|是|{}|目的镜像仓库id
enabled|bool|是|false|镜像仓库uid
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/replication/policy/create
```
{
	"registry_uuid": "9cbd63e0-2d42-4e52-bb5e-80b861cc868a",
	"name": "pull",
	"description": "",
	"dest_namespace": "",
	"trigger": {
		"type": "manual",
		"trigger_settings": {
			"cron": "* * * * * *"
		}
	},
	"filters": [{
		"type": "label",
		"value": []
	}],
	"deletion": false,
	"override": true,
	"dest_registry": {
		"id": 2
	}
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
## /v1/container_registry/replication/policy/update
复制策略更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
name|string|是|""|策略名
description|string|否 |""|描述
trigger|struct|是|""|触发策略
filters|struct|是|""|过滤
deletion|bool|否|false| 是否删除
override|bool|是|false|覆盖已存在的镜像
dest_registry|struct|是|{}|目的镜像仓库id
id|string|是|""|策略id
enabled|bool|是|false|镜像仓库uid
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/replication/policy/update
```
{
	"registry_uuid": "9cbd63e0-2d42-4e52-bb5e-80b861cc868a",
	"name": "pull",
	"description": "",
	"dest_namespace": "",
	"trigger": {
		"type": "manual",
		"trigger_settings": {
			"cron": "* * * * * *"
		}
	},
	"filters": [{
		"type": "label",
		"value": []
	}],
	"deletion": false,
	"override": true,
	"dest_registry": {
		"id": 2
	},
	"id": 4,
	"enabled": true
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

## /v1/container_registry/replication/policy/delete
复制策略删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---

### 返回参数

名称|参数类型|描述
---|---|---
registry_uuid|string|是|""|镜像仓库uid
id|string|是|""|策略id
### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/replication/policy/delete
```
{
	"registry_uuid": "9cbd63e0-2d42-4e52-bb5e-80b861cc868a",
	"id": 4
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

## /v1/container_registry/replication/policy/execute
复制策略执行
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
project_id|string|是|""|项目id
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/replication/policy/execute
```
{
	"registry_uuid": "9cbd63e0-2d42-4e52-bb5e-80b861cc868a",
	"policy_id": 3
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

## /v1/container_registry/replication/policy/execute/result
复制策略执行结果
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
project_id|string|是|""|项目id
page_num|int|否|0|页数
page_size|int|否|0|页大小
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/replication/policy/execute/result?page_size=10&status=&page_num=0&registry_uuid=9cbd63e0-2d42-4e52-bb5e-80b861cc868a&policy_id=3

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
        "id": 14,
        "policy_id": 3,
        "status": "InProgress",
        "status_text": "",
        "total": 9,
        "failed": 0,
        "succeed": 0,
        "in_progress": 9,
        "stopped": 0,
        "trigger": "manual",
        "start_time": "2021-08-24T07:01:43.350125Z",
        "end_time": "0001-01-01T00:00:00Z",
        "start_time_unix": 1629788503,
        "end_time_unix": -62135596800
      },
      {
        "id": 13,
        "policy_id": 3,
        "status": "Succeed",
        "status_text": "",
        "total": 9,
        "failed": 0,
        "succeed": 9,
        "in_progress": 0,
        "stopped": 0,
        "trigger": "manual",
        "start_time": "2021-08-11T06:08:18.557551Z",
        "end_time": "2021-08-11T06:08:44Z",
        "start_time_unix": 1628662098,
        "end_time_unix": 1628662124
      }
    ],
    "total_count": 2
  }
}
```

## /v1/container_registry/repository/list
harbor镜像仓库镜像列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
project_id|string|是|""|项目id
project_name|string|是|""|项目名
page_num|int|否|0|页数
page_size|int|否|0|页大小
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/repository/list?fuzzy=&page_size=10&registry_uuid=9cbd63e0-2d42-4e52-bb5e-80b861cc868a&project_id=1&project_name=library&page_num=0

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
        "description": "",
        "id": 145,
        "name": "library/centos-ssh",
        "project_id": 1,
        "repository_name": "library/centos-ssh",
        "artifact_count": 0,
        "pull_count": 0,
        "star_count": 0,
        "tags_count": 1,
        "creation_time": "2021-08-11T06:08:31.897759Z",
        "update_time": "2021-08-11T06:08:31.897759Z",
        "creation_time_unix": 1628662111,
        "update_time_unix": 1628662111
      },
      {
        "description": "",
        "id": 146,
        "name": "library/centos-stress",
        "project_id": 1,
        "repository_name": "library/centos-stress",
        "artifact_count": 0,
        "pull_count": 0,
        "star_count": 0,
        "tags_count": 1,
        "creation_time": "2021-08-11T06:08:33.391516Z",
        "update_time": "2021-08-11T06:08:33.391516Z",
        "creation_time_unix": 1628662113,
        "update_time_unix": 1628662113
      },
      {
        "description": "",
        "id": 142,
        "name": "library/docker.io/library/httpd",
        "project_id": 1,
        "repository_name": "library/docker.io/library/httpd",
        "artifact_count": 0,
        "pull_count": 0,
        "star_count": 0,
        "tags_count": 1,
        "creation_time": "2021-08-11T06:08:28.898475Z",
        "update_time": "2021-08-11T06:08:28.898475Z",
        "creation_time_unix": 1628662108,
        "update_time_unix": 1628662108
      },
      {
        "description": "",
        "id": 148,
        "name": "library/golang",
        "project_id": 1,
        "repository_name": "library/golang",
        "artifact_count": 0,
        "pull_count": 0,
        "star_count": 0,
        "tags_count": 2,
        "creation_time": "2021-08-11T06:08:39.073844Z",
        "update_time": "2021-08-11T06:08:39.073844Z",
        "creation_time_unix": 1628662119,
        "update_time_unix": 1628662119
      },
      {
        "description": "",
        "id": 143,
        "name": "library/ingresstest",
        "project_id": 1,
        "repository_name": "library/ingresstest",
        "artifact_count": 0,
        "pull_count": 0,
        "star_count": 0,
        "tags_count": 1,
        "creation_time": "2021-08-11T06:08:30.504554Z",
        "update_time": "2021-08-11T06:08:30.504554Z",
        "creation_time_unix": 1628662110,
        "update_time_unix": 1628662110
      },
      {
        "description": "",
        "id": 147,
        "name": "library/mysql",
        "project_id": 1,
        "repository_name": "library/mysql",
        "artifact_count": 0,
        "pull_count": 0,
        "star_count": 0,
        "tags_count": 2,
        "creation_time": "2021-08-11T06:08:34.532967Z",
        "update_time": "2021-08-11T06:08:34.532967Z",
        "creation_time_unix": 1628662114,
        "update_time_unix": 1628662114
      },
      {
        "description": "",
        "id": 141,
        "name": "library/nginx",
        "project_id": 1,
        "repository_name": "library/nginx",
        "artifact_count": 0,
        "pull_count": 0,
        "star_count": 0,
        "tags_count": 4,
        "creation_time": "2021-08-11T06:08:26.688865Z",
        "update_time": "2021-08-11T06:08:26.688865Z",
        "creation_time_unix": 1628662106,
        "update_time_unix": 1628662106
      },
      {
        "description": "",
        "id": 140,
        "name": "library/ubuntu",
        "project_id": 1,
        "repository_name": "library/ubuntu",
        "artifact_count": 0,
        "pull_count": 0,
        "star_count": 0,
        "tags_count": 1,
        "creation_time": "2021-08-11T06:08:25.562199Z",
        "update_time": "2021-08-11T06:08:25.562199Z",
        "creation_time_unix": 1628662105,
        "update_time_unix": 1628662105
      },
      {
        "description": "",
        "id": 144,
        "name": "library/ubuntu-debug",
        "project_id": 1,
        "repository_name": "library/ubuntu-debug",
        "artifact_count": 0,
        "pull_count": 2,
        "star_count": 0,
        "tags_count": 2,
        "creation_time": "2021-08-11T06:08:31.063103Z",
        "update_time": "2021-08-11T06:09:49.412544Z",
        "creation_time_unix": 1628662111,
        "update_time_unix": 1628662189
      }
    ],
    "total_count": 9
  }
}
```

## /v1/container_registry/repository/delete
harbor镜像仓库镜像删除
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
repo_name|string|是|""|镜像名
project_name|string|是|""|项目名
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/repository/delete
```
{
	"repo_name": "library/docker.io/library/httpd",
	"project_name": "library",
	"registry_uuid": "9cbd63e0-2d42-4e52-bb5e-80b861cc868a"
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

## /v1/container_registry/repository/tag/list
harbor镜像仓库镜像标签列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
repo_name|string|是|""|镜像名
page_num|int|否|0|页数
page_size|int|否|0|页大小
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/repository/tag/list?registry_uuid=9cbd63e0-2d42-4e52-bb5e-80b861cc868a&repo_name=library%2Fcentos-ssh&page_size=10&page_num=0

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
        "digest": "sha256:cc70ccf1d00deebd6240e2fe8ffc1a5e2e9fd4ab813e641f1365ecfaef4b35ba",
        "name": "latest",
        "size": 130339412,
        "architecture": "amd64",
        "os": "linux",
        "os.version": "",
        "docker_version": "19.03.9",
        "author": "",
        "created": "2021-03-25T08:11:02.303194391Z",
        "created_unix": 1616659862,
        "config": {
          "labels": {
            "org.label-schema.build-date": "20201204",
            "org.label-schema.license": "GPLv2",
            "org.label-schema.name": "CentOS Base Image",
            "org.label-schema.schema-version": "1.0",
            "org.label-schema.vendor": "CentOS"
          }
        },
        "immutable": false,
        "labels": [],
        "push_time": "2021-08-11T06:08:31.904225Z",
        "pull_time": "0001-01-01T00:00:00Z",
        "push_time_unix": 1628662111,
        "pull_time_unix": -62135596800,
        "artifact_digest": ""
      }
    ],
    "total_count": 1,
    "scanners": [
      {
        "uuid": "fe0a7e16-d552-11eb-8db6-0242ac120008",
        "name": "Clair",
        "description": "The clair scanner adapter",
        "url": "http://clair-adapter:8080",
        "disabled": false,
        "is_default": true,
        "auth": "",
        "skip_certVerify": false,
        "use_internal_addr": true,
        "create_time": "2021-06-25T01:16:39.106757Z",
        "update_time": "2021-06-25T01:16:39.106761Z",
        "create_time_unix": 0,
        "update_time_unix": 0,
        "access_credential": "",
        "metadata": null,
        "loadingMetadata": false
      }
    ]
  }
}
```
## /v1/container_registry/repository/tag/get
harbor镜像仓库镜像标签详情
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---

### 返回参数

名称|参数类型|描述
---|---|---
registry_uuid|string|是|""|镜像仓库uid
repo_name|string|是|""|镜像名
tag_name|string|是|""|tag名
### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/repository/tag/get?registry_uuid=9cbd63e0-2d42-4e52-bb5e-80b861cc868a&repo_name=library%2Fcentos-ssh&tag_name=latest

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "digest": "sha256:cc70ccf1d00deebd6240e2fe8ffc1a5e2e9fd4ab813e641f1365ecfaef4b35ba",
    "name": "latest",
    "size": 130339412,
    "architecture": "amd64",
    "os": "linux",
    "os.version": "",
    "docker_version": "19.03.9",
    "author": "",
    "created": "2021-03-25T08:11:02.303194391Z",
    "created_unix": 1616659862,
    "config": {
      "labels": {
        "org.label-schema.build-date": "20201204",
        "org.label-schema.license": "GPLv2",
        "org.label-schema.name": "CentOS Base Image",
        "org.label-schema.schema-version": "1.0",
        "org.label-schema.vendor": "CentOS"
      }
    },
    "immutable": false,
    "labels": [],
    "push_time": "2021-08-11T06:08:31.904225Z",
    "pull_time": "0001-01-01T00:00:00Z",
    "push_time_unix": 1628662111,
    "pull_time_unix": -62135596800,
    "artifact_digest": "",
    "scanners": [
      {
        "uuid": "fe0a7e16-d552-11eb-8db6-0242ac120008",
        "name": "Clair",
        "description": "The clair scanner adapter",
        "url": "http://clair-adapter:8080",
        "disabled": false,
        "is_default": true,
        "auth": "",
        "skip_certVerify": false,
        "use_internal_addr": true,
        "create_time": "2021-06-25T01:16:39.106757Z",
        "update_time": "2021-06-25T01:16:39.106761Z",
        "create_time_unix": 0,
        "update_time_unix": 0,
        "access_credential": "",
        "metadata": null,
        "loadingMetadata": false
      }
    ]
  }
}
```


## /v1/container_registry/repository/tag/manifests
harbor镜像仓库镜像标签镜像清单
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
repo_name|string|是|""|镜像名
tag_name|string|是|""|tag名

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/repository/tag/manifests?registry_uuid=9cbd63e0-2d42-4e52-bb5e-80b861cc868a&repo_name=library%2Fcentos-ssh&tag_name=latest

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "manifest": {
      "schemaVersion": 2,
      "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
      "config": {
        "mediaType": "application/vnd.docker.container.image.v1+json",
        "size": 2337,
        "digest": "sha256:4a7a65a7d57c9a76572daf1f0c6f05551198b595fa62af64172ac2a8f9ee952e"
      },
      "layers": [
        {
          "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
          "size": 75181999,
          "digest": "sha256:7a0437f04f83f084b7ed68ad9c4a4947e12fc4e1b006b38129bac89114ec3621"
        },
        {
          "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
          "size": 23453034,
          "digest": "sha256:a3dc4a3afd037d054cc4ffc4d437ea1bf17e59c02ce38729cd216515e6b02701"
        },
        {
          "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
          "size": 31701089,
          "digest": "sha256:dbffbd386e204ef1380e275464a1878796aaa85d275c1fcebf8ff5661a448239"
        }
      ]
    },
    "config": "{\"architecture\":\"amd64\",\"config\":{\"Hostname\":\"6275a68c8c92\",\"Domainname\":\"\",\"User\":\"\",\"AttachStdin\":false,\"AttachStdout\":false,\"AttachStderr\":false,\"Tty\":true,\"OpenStdin\":true,\"StdinOnce\":false,\"Env\":[\"PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\"],\"Cmd\":[\"/bin/bash\"],\"Image\":\"10.30.35.211/library/centos_ssh:latest\",\"Volumes\":null,\"WorkingDir\":\"\",\"Entrypoint\":null,\"OnBuild\":null,\"Labels\":{\"org.label-schema.build-date\":\"20201204\",\"org.label-schema.license\":\"GPLv2\",\"org.label-schema.name\":\"CentOS Base Image\",\"org.label-schema.schema-version\":\"1.0\",\"org.label-schema.vendor\":\"CentOS\"}},\"container\":\"6275a68c8c92f171f4b7b2b82d823b7cb0a02fc49c9647ffb291d46a93da851f\",\"container_config\":{\"Hostname\":\"6275a68c8c92\",\"Domainname\":\"\",\"User\":\"\",\"AttachStdin\":false,\"AttachStdout\":false,\"AttachStderr\":false,\"Tty\":true,\"OpenStdin\":true,\"StdinOnce\":false,\"Env\":[\"PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\"],\"Cmd\":[\"/bin/bash\"],\"Image\":\"10.30.35.211/library/centos_ssh:latest\",\"Volumes\":null,\"WorkingDir\":\"\",\"Entrypoint\":null,\"OnBuild\":null,\"Labels\":{\"org.label-schema.build-date\":\"20201204\",\"org.label-schema.license\":\"GPLv2\",\"org.label-schema.name\":\"CentOS Base Image\",\"org.label-schema.schema-version\":\"1.0\",\"org.label-schema.vendor\":\"CentOS\"}},\"created\":\"2021-03-25T08:11:02.303194391Z\",\"docker_version\":\"19.03.9\",\"history\":[{\"created\":\"2020-12-08T00:22:52.526672082Z\",\"created_by\":\"/bin/sh -c #(nop) ADD file:bd7a2aed6ede423b719ceb2f723e4ecdfa662b28639c8429731c878e86fb138b in / \"},{\"created\":\"2020-12-08T00:22:52.895811646Z\",\"created_by\":\"/bin/sh -c #(nop)  LABEL org.label-schema.schema-version=1.0 org.label-schema.name=CentOS Base Image org.label-schema.vendor=CentOS org.label-schema.license=GPLv2 org.label-schema.build-date=20201204\",\"empty_layer\":true},{\"created\":\"2020-12-08T00:22:53.076477777Z\",\"created_by\":\"/bin/sh -c #(nop)  CMD [\\\"/bin/bash\\\"]\",\"empty_layer\":true},{\"created\":\"2021-03-24T02:21:45.491260751Z\",\"created_by\":\"/bin/bash\"},{\"created\":\"2021-03-25T08:11:02.303194391Z\",\"created_by\":\"/bin/bash\"}],\"os\":\"linux\",\"rootfs\":{\"type\":\"layers\",\"diff_ids\":[\"sha256:2653d992f4ef2bfd27f94db643815aa567240c37732cae1405ad1c1309ee9859\",\"sha256:412a09511a8bdf5ada97fe5842e2569e55d53a5cb8f2d75a6b18f883b49fdcb5\",\"sha256:47b3a8a199e66a316571643d6f40aefff259ddf7ba70ed0dcbfbf883a4d62fa9\"]}}",
    "conf": {
      "architecture": "amd64",
      "config": {
        "Hostname": "6275a68c8c92",
        "Domainname": "",
        "User": "",
        "AttachStdin": false,
        "AttachStdout": false,
        "AttachStderr": false,
        "ExposedPorts": null,
        "Tty": true,
        "OpenStdin": true,
        "StdinOnce": false,
        "Env": [
          "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
        ],
        "Cmd": [
          "/bin/bash"
        ],
        "ArgsEscaped": false,
        "Image": "10.30.35.211/library/centos_ssh:latest",
        "Volumes": null,
        "WorkingDir": "",
        "Entrypoint": null,
        "OnBuild": null,
        "Labels": {
          "org.label-schema.build-date": "20201204",
          "org.label-schema.license": "GPLv2",
          "org.label-schema.name": "CentOS Base Image",
          "org.label-schema.schema-version": "1.0",
          "org.label-schema.vendor": "CentOS"
        }
      },
      "container": "6275a68c8c92f171f4b7b2b82d823b7cb0a02fc49c9647ffb291d46a93da851f",
      "container_config": {
        "Hostname": "6275a68c8c92",
        "Domainname": "",
        "User": "",
        "AttachStdin": false,
        "AttachStdout": false,
        "AttachStderr": false,
        "ExposedPorts": null,
        "Tty": true,
        "OpenStdin": true,
        "StdinOnce": false,
        "Env": [
          "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
        ],
        "Cmd": [
          "/bin/bash"
        ],
        "ArgsEscaped": false,
        "Image": "10.30.35.211/library/centos_ssh:latest",
        "Volumes": null,
        "WorkingDir": "",
        "Entrypoint": null,
        "OnBuild": null,
        "Labels": {
          "org.label-schema.build-date": "20201204",
          "org.label-schema.license": "GPLv2",
          "org.label-schema.name": "CentOS Base Image",
          "org.label-schema.schema-version": "1.0",
          "org.label-schema.vendor": "CentOS"
        }
      },
      "created": "2021-03-25T08:11:02.303194391Z",
      "docker_version": "19.03.9",
      "history": [
        {
          "created": "2020-12-08T00:22:52.526672082Z",
          "created_by": "/bin/sh -c #(nop) ADD file:bd7a2aed6ede423b719ceb2f723e4ecdfa662b28639c8429731c878e86fb138b in / "
        },
        {
          "created": "2020-12-08T00:22:52.895811646Z",
          "created_by": "/bin/sh -c #(nop)  LABEL org.label-schema.schema-version=1.0 org.label-schema.name=CentOS Base Image org.label-schema.vendor=CentOS org.label-schema.license=GPLv2 org.label-schema.build-date=20201204",
          "empty_layer": true
        },
        {
          "created": "2020-12-08T00:22:53.076477777Z",
          "created_by": "/bin/sh -c #(nop)  CMD [\"/bin/bash\"]",
          "empty_layer": true
        },
        {
          "created": "2021-03-24T02:21:45.491260751Z",
          "created_by": "/bin/bash"
        },
        {
          "created": "2021-03-25T08:11:02.303194391Z",
          "created_by": "/bin/bash"
        }
      ],
      "os": "linux",
      "rootfs": {
        "type": "layers",
        "diff_ids": [
          "sha256:2653d992f4ef2bfd27f94db643815aa567240c37732cae1405ad1c1309ee9859",
          "sha256:412a09511a8bdf5ada97fe5842e2569e55d53a5cb8f2d75a6b18f883b49fdcb5",
          "sha256:47b3a8a199e66a316571643d6f40aefff259ddf7ba70ed0dcbfbf883a4d62fa9"
        ]
      }
    }
  }
}
```

## /v1/container_registry/repository/tag/scan
harbor镜像仓库镜像标签镜像扫描
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
https://10.30.100.178/v1/container_registry/repository/tag/scan
```
{
	"registry_uuid": "9cbd63e0-2d42-4e52-bb5e-80b861cc868a",
	"repo_name": "library/centos-ssh",
	"tag_name": "latest",
	"cluster_uuid": "43f771ba-87b6-4f20-9633-3bc04e0dc379"
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

## /v1/container_registry/repository/tag/scan/result
harbor镜像仓库镜像标签镜像扫描结果
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
https://10.30.100.178/v1/container_registry/repository/tag/scan/result?registry_uuid=9cbd63e0-2d42-4e52-bb5e-80b861cc868a&repo_name=library%2Fcentos-ssh&tag_name=latest

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0": {
      "generated_at": "2021-08-24T07:23:59.571145585Z",
      "generated_at_unix": 1629789839,
      "scanner": {
        "name": "Clair",
        "vendor": "CoreOS",
        "version": "2.x"
      },
      "severity": "None",
      "vulnerabilities": null,
      "vulnerabilities_total": 0
    }
  }
}
```

## /v1/container_registry/repository/tag/scan/logs
harbor镜像仓库镜像标签镜像扫描日志
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

## /v1/container_registry/scanner/list
harbor镜像仓库扫描器列表
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


## /v1/container_registry/scanner/ping
harbor镜像仓库扫描器连接测试
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



## /v1/container_registry/system/gc/list
harbor镜像仓库垃圾清理策略列表
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
page_num|int|否|0|页数
page_size|int|否|0|页大小

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/system/gc/list?page_size=10&page_num=0&registry_uuid=9cbd63e0-2d42-4e52-bb5e-80b861cc868a

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
        "id": 6,
        "job_name": "IMAGE_GC",
        "job_kind": "Generic",
        "schedule": {
          "type": "Manual",
          "cron": ""
        },
        "job_status": "finished",
        "deleted": false,
        "creation_time": "2021-08-24T07:44:59Z",
        "update_time": "2021-08-24T07:45:02.747452Z"
      },
      {
        "id": 2,
        "job_name": "IMAGE_GC",
        "job_kind": "Periodic",
        "schedule": {
          "type": "Daily",
          "cron": "0 0 16 * * *"
        },
        "job_status": "finished",
        "deleted": false,
        "creation_time": "2021-08-04T06:05:11Z",
        "update_time": "2021-08-07T16:00:05.324609Z"
      }
    ],
    "total_count": 2
  }
}
```



## /v1/container_registry/system/gc/log
harbor镜像仓库垃圾清理策略日志
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/system/gc/log?id=6&registry_uuid=9cbd63e0-2d42-4e52-bb5e-80b861cc868a

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "log": "2021-08-24T07:45:00Z [INFO] [/jobservice/job/impl/gc/job.go:87]: start to run gc in job.\n2021-08-24T07:45:02Z [INFO] [/jobservice/job/impl/gc/job.go:99]: GC results: status: true, message: k8s/alertmanager\nk8s/alertmanager: marking manifest :30287d8996563077ca1aeb138cb8d7b6b80d8c50b2cc6f3422b950c9f280277b\n, start: 2021-08-24 07:45:00.878762666 +0000 UTC, end: 2021-08-24 07:45:02.284347956 +0000 UTC.\n2021-08-24T07:45:02Z [INFO] [/jobservice/job/impl/gc/job.go:100]: success to run gc in job.\n"
  }
}
```

## /v1/container_registry/system/gc/manual
harbor镜像仓库垃圾清理立即执行
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/system/gc/manual

```
{
	"registry_uuid": "9cbd63e0-2d42-4e52-bb5e-80b861cc868a",
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

## /v1/container_registry/system/gc/schedule/get
harbor镜像仓库垃圾清理调度详情

### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/system/gc/schedule/get?registry_uuid=9cbd63e0-2d42-4e52-bb5e-80b861cc868a

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "schedule": {
      "type": "Daily",
      "cron": "0 0 0 * * *"
    }
  }
}   
```


## /v1/container_registry/system/scanall/manual
harbor镜像仓库镜像扫描立即执行
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/system/scanall/manual
```
{
	"registry_uuid": "9cbd63e0-2d42-4e52-bb5e-80b861cc868a",
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
## /v1/container_registry/system/scanall/metrics
harbor镜像仓库镜像扫描状态
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/system/scanall/metrics?registry_uuid=9cbd63e0-2d42-4e52-bb5e-80b861cc868a


#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "total": 43,
    "completed": 43,
    "metrics": {
      "Pending": 0,
      "Running": 0,
      "Success": 43
    },
    "requester": "1",
    "ongoing": false
  }
}
```

## /v1/container_registry/system/scanall/schedule/get
harbor镜像仓库镜像扫描调度策略详情
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/system/scanall/schedule/get?registry_uuid=9cbd63e0-2d42-4e52-bb5e-80b861cc868a

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "schedule": {
      "type": "Weekly",
      "cron": "0 0 0 * * 0"
    }
  }
}
```

## /v1/container_registry/system/scanall/schedule/update
harbor镜像仓库镜像扫描调度策略更新
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
schedule|struct|是|{}|调度规则

### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/system/scanall/schedule/update
```
{
	"registry_uuid": "9cbd63e0-2d42-4e52-bb5e-80b861cc868a",
	"schedule": {
		"type": "None",
		"cron": "0 0 0 * * 0"
	},
}
```
#### 正常返回示例
```{
     "scode": 0,
     "desc": "",
     "message": "success",
     "message_cn": "成功",
     "stack": null,
     "data": null
   }
```
## /v1/container_registry/system/cve_whitelist
harbor镜像仓库漏洞白名单
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
registry_uuid|string|是|""|镜像仓库uid
### 返回参数

名称|参数类型|描述
---|---|---

### 示例

#### 请求示例
https://10.30.100.178/v1/container_registry/system/cve_whitelist?registry_uuid=9cbd63e0-2d42-4e52-bb5e-80b861cc868a&project_id=2

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "id": 0,
    "project_id": 0,
    "items": [],
  }
}
```