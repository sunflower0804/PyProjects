[back to api overview](../api_overview.md#api)

## /v1/vsphere/vm/create
虚拟机创建
### 请求类型
POST

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 vsphere_uuid|string| 是|-  | vsphere uuid
 datacenter_reference|string|是|-|数据中心的唯一标识
 host_reference|string|是|-|主机的唯一标识
 vm_config|vm_config object|是|-|虚拟机配置参数

#### vm_config Object
名称  | 数据类型| 是否必填 | 默认值 | 描述
---|---|---|---|---
vm_name|string|是|- |虚拟机名称
num_cpu|int32|是|- |cpu数量
memory_mb|int64|是|- |内存，单位MB
files|files Object|是|- |虚拟机文件配置
version|string|否|- |此虚拟机的版本,例如:ESXi 5.5 虚拟机，该接口 /v1/vsphere/vm/support/version下有数据（该接口暂时没参数）
guest_id|string|否|- |简短的客户操作系统标识符，例如：Microsoft Windows Server 2016 (64 位)，该接口  /v1/vsphere/vm/support/os 下有数据（该接口暂时没参数）
firmware|string|否|- |引导固件，BIOS/EFI 可选
num_cores_per_socket|int32|是|1 |每个插槽内核数，cpu数量=每个插槽内核数*插槽数
memory_hot_add_enabled|bool|否|-|内存热添加（虚拟机运行时修改内存），只能在虚拟机关机状态才能设置
cpu_hot_add_enabled|bool|否|-|cpu热添加（虚拟机运行时修改cpu），只能在虚拟机关机状态才能设置
virtual_ich_7m_present|bool|否|-|此虚拟机是否具有虚拟Intel I / O控制器中枢
virtual_smc_present|bool|否|-|此虚拟机是否具有系统管理控制器
max_mks_connections|int32|否|-|会话数上限
annotation|string|否|-|虚拟机备注
cpu_allocation|allocation object|否|{}|cpu资源配置
memory_allocation|allocation object|否|{}|内存资源配置
tools|tools object|否|{}|虚拟机工具的配置
power_op_info|power_op_info object|否|{}|电源操作配置
flags|flags object|否|{}|虚拟机的附加标志
video_card|video_card object|否|{}|显卡配置，显卡不能移除，不填会自动添加
ethernet_card|ethernet_card_list object|否|[]|网络,可填多个
virtual_usb_controller|virtual_usb_controller object|否|[]|usb控制器，可填多个
virtual_disk|virtual_disk object|否|[]|硬盘，可填多个

##### files Object
名称  | 数据类型| 是否必填 | 默认值 | 描述
---|---|---|---|---
vm_path_name|string|是|- |虚拟机数据存储名称

##### allocation Object
名称  | 数据类型| 是否必填 | 默认值 | 描述
---|---|---|---|---
reservation|int64|否|0|预留(>=0)，cpu单位为MHz,memory单位为MB;预留不能大于限制,当limit=-1时，reservation范围为0—num_cpu*2200或预留范围为0—memory_mb*1024
limit|int64|否|-1|限制(>=-1)，单位是内存MB, CPU MHz，-1 表示不受限制，
shares|shares object|是|- |份额

##### shares Object
名称  | 数据类型| 是否必填 | 默认值 | 描述
---|---|---|---|---
level|string|是|- |low,normal,high,custom可选
shares|int32|否|0 |当level为custom时，cpu和内存范围为：0-1000000；硬盘范围为200-4000

##### tools Object
名称  | 数据类型| 是否必填 | 默认值 | 描述
---|---|---|---|---
after_power_on|bool|否|false|运行 VMware Tools 脚本,打开电源后
after_resume|bool|否|false|运行 VMware Tools 脚本,恢复后
before_guest_shutdown|bool|否|false|运行 VMware Tools 脚本,关闭客户机前
before_guest_standby|bool|否|false|运行 VMware Tools 脚本,挂起前
tools_upgrade_policy|string|否|-|工具升级方式;manual,upgradeAtPowerCycle可选
before_guest_standby|bool|否|false|同步客户机时间与主机时间

##### power_op_info Object
名称  | 数据类型| 是否必填 | 默认值 | 描述
---|---|---|---|---
power_Off_type|string|否|preset|关机操作;soft,hard，preset可选
suspend_type|string|否|preset|挂起操作;soft,hard，preset可选
reset_type|string|否|preset|重置操作;soft,hard，preset可选
default_power_off_type|string|否|-|默认关机操作;soft,hard可选
default_suspend_type|string|否|-|默认挂起操作;soft,hard可选
default_reset_type|string|否|-|默认重置操作;soft,hard可选

##### flags Object
名称  | 数据类型| 是否必填 | 默认值 | 描述
---|---|---|---|---
enable_logging|bool|否|false|是否启用虚拟机日志记录

##### video_card Object
名称  | 数据类型| 是否必填 | 默认值 | 描述
---|---|---|---|---
operation|string|是|-|add,remove,edit 可选，设备的操作类型
video_ram_size_in_kb|int64|否|-|显卡内存，1.172-128MB之间
num_displays|int32|否|-|显示器数量，大于0
use_auto_detect|bool|否|false|是否自动确定显卡设置
enable_3d_support|bool|否|false|是否开启3D图像
use_3d_renderer|string|否|-|3D渲染器，automatic，software，hardware可选
graphics_memory_size_in_kb|int64|否|false|3D显存

##### ethernet_card_list Object
名称  | 数据类型| 是否必填 | 默认值 | 描述
---|---|---|---|---
operation|string|是|-|add,remove,edit 可选，设备的操作类型
network_type|string|是|-|vmxnet3,e1000e可选，网络类型
address_type|string|否|-|mac地址生成类型，assigned,manual,generated可选，不是必填字段，填了manual mac_address字段必填
mac_address|string|否|-|配合address_type使用，address_type 为manual时才填
wake_on_lan_enabled|bool|否|false|启用或禁用lan上的唤醒
network_backing|network_backing object|否|{}|网络支持

##### network_backing Object
名称  | 数据类型| 是否必填 | 默认值 | 描述
---|---|---|---|---
device_name|string|否|-|网络名称
use_auto_detect|bool|否|false|是否应自动检测设备

##### virtual_usb_controller Object
名称  | 数据类型| 是否必填 | 默认值 | 描述
---|---|---|---|---
operation|string|是|-|add,remove,edit 可选，设备的操作类型
usb_type|string|是|-|USB 2.0，USB 3.0可选
virtual_device|virtual_device Object|否|-|

##### virtual_disk Object
名称  | 数据类型| 是否必填 | 默认值 | 描述
---|---|---|---|---
operation|string|是|-|add,remove,edit 可选，设备的操作类型
file_operation|string|是|-|create,destroy,replace可选，create会在数据存储创建一个capacity_in_bytes大小的文件
capacity_in_bytes|int64|是|-|磁盘容量，单位字节
disk_backing|disk_backing object|是|-|
virtual_device|virtual_device Object|是|-|
storage_io_allocation|storage_io_allocation Object|是|-|
v_flash_cache_config_info|v_flash_cache_config_info Object|是|-|

##### disk_backing Object
名称  | 数据类型| 是否必填 | 默认值 | 描述
---|---|---|---|---
disk_mode|string|是|-|磁盘模式 persistent（218页面对应从属），independent_persistent（独立持久），independent_nonpersistent（独立非持久）
thin_provisioned|bool|是|-|磁盘置备 ，true 表示精简置备（218页面）
eagerly_scrub|bool|是|-|磁盘置备，true表示后置备快速置零 ，false表示后置备延迟置零
sharing|string|否|-|sharingNone，sharingMultiWriter可选
datastore_reference|string|是|-|指定数据存储

##### storage_io_allocation Object
名称  | 数据类型| 是否必填 | 默认值 | 描述
---|---|---|---|---
limit|int64|否|-|限制IOPs：-1表示不受限制，自定义为大于16小于2147483647
shares|shares object|是|- |份额

##### v_flash_cache_config_info Object
名称  | 数据类型| 是否必填 | 默认值 | 描述
---|---|---|---|---
reservation_in_mb|int64|是|-|虚拟闪存读取缓存；单位MB

##### virtual_device Object
名称  | 数据类型| 是否必填 | 默认值 | 描述
---|---|---|---|---
key|int32|否|-|该虚拟设备在虚拟机中的标识，添加的时候不用(系统自己分配)，卸载或修改是要传
controller_key|int32|否|-|要用的控制器的标识，例如添加硬盘时一定要填控制器的key,
unit_number|int32|否|-|单元节点，例如添加硬盘时要填（范围时0-15）

### 返回参数

名称|参数类型|描述
---|---|---


### 示例

#### 请求示例
```
http://192.168.201.57:9990/v1/vsphere/vm/create
```
Body:
```
{
	"vsphere_uuid": "{{ vsphere_uuid  }}",
	"datacenter_reference": "Datacenter:datacenter-2",
	"host_reference": "HostSystem:host-9",
	"vm_config": {
		"vm_name": "vm_042401",
		"version": "ESXi 5.5 虚拟机",
		"guest_id": "Microsoft Windows Server 2016 (64 位)",
		"firmware": "EFI",
		"num_cpu": 2,
		"memory_mb": 24,
		"num_cores_per_socket": 3,
		"cpu_allocation": {
			"reservation": 3000,
			"limit": -1,
			"shares": {
				"shares": 1000,
				"level": "high"
			}
		},
		"memory_allocation": {
			"shares": {
				"shares": 40960,
				"level": "normal"
			},
			"limit": 2048,
			"reservation": 112
		},
		"files": {
			"vm_path_name": "datastore1"
		},
		"tools": {
			"after_power_on": true,
			"after_resume": true,
			"before_guest_shutdown": true,
			"before_guest_standby": true,
			"tools_upgrade_policy": "manual",
			"sync_time_with_host": true
		},
		"power_op_info": {
			"power_Off_type": "preset",
			"suspend_type": "preset",
			"reset_type": "preset",
			"standby_action": "checkpoint"
		},
		"flags": {
			"monitor_type": "release",
			"enable_logging": true
		},
		"video_card": {
			"operation": "add",
			"video_ram_size_in_kb": 2048,
			"num_displays": 3,
			"use_auto_detect": false,
			"enable_3d_support": false,
			"use_3d_renderer": "automatic",
			"graphics_memory_size_in_kb": 262144
		}
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
  "data": ""
}
```

#### 异常返回示例

### 状态码