



#### ticketInfo
名称|参数类型|描述 
---|---|---
 ticket_uuid|string| 工单uuid
 ticket_name|string| 工单name
 type|string| 工单类型
 reason|string| 申请原因
 process_uuid|string| 路程uuid
 compute | compute 对象| 虚拟机相关
 
 #### compute
 名称|参数类型|描述 
 ---|---|---
 vm_specification | [vm_specificatoin 对象](define.md#vm_specificatoin)| 规格申请虚拟机
 vm_template | [vm_template 对象](define.md#vm_template)| 模板申请虚拟机
 vm_cpu_update | [vm_cpu_update 对象](define.md#VmCpuUpdate) | 修改虚拟机cpu大小
 vm_memory_update | [vm_memory_update 对象](define.md#VmMemoryUpdate) | 修改虚拟机memory大小
 vm_disk_exist_mount | [ vm_disk_exist_mount 对象](define.md#VmDiskExistMount) | 虚拟机挂载已存在磁盘
 vm_disk_not_exist_mount | [vm_disk_not_exist_mount 对象](define.md#VmDiskNotExistMount) | 创建磁盘并挂载
 vm_network_card_add | [vm_network_card_add 对象](define.md#VmNetworkCardAdd) | 虚拟机添加网卡
 vm_security | [vm_security 对象](define.md#vm_security) | 申请安全虚拟机
 
 #### vm_specificatoin
 名称|参数类型|描述 
 ---|---|---
 specification_uuid | string| 规格uuid
 specification_name | string| 规格name
 specification_info | spefication 对象| 当保存或者提交申请之后，规格信息会保存在此对象中，具体参考虚拟机规格
 vm_name | string | 虚拟机的名称
 vm_info | map[string]string | 创建的虚拟机的uuid和name
 apply_count | int | 批量创建多少个虚拟机
 success_count | int | 成功创建的虚拟机数量有多少个
 failed_count | int | 创建失败的虚拟机有多少个
 faild_info | string 列表 | 如果创建虚拟机失败，那么失败原因是什么
 
 #### vm_template
 名称|参数类型|描述 
 ---|---|---
 template_uuid | string| 模板uuid
 template_name | string| 模板name
 vm_uuid | string| 虚拟机uuid
 vm_name | string| 虚拟机name
 teplate_info | template 对象| 当保存或者提交申请之后，模板信息会保存在此对象中，具体参考虚拟机模板
 
 
 #### VmCpuUpdate
  名称|参数类型|描述 
  ---|---|---
  vm_uuid | string| 虚拟机uuid
  cpu_count | int| 虚拟机cpu数量
  cpu_max_count | int| 虚拟机最大cpu数量
 
 
 #### VmMemoryUpdate 
  名称|参数类型|描述 
  ---|---|---
  vm_uuid | string| 虚拟机uuid
  vm_memory_size | string| 虚拟机内存大小(数字字符串)。
  
  
 #### VmDiskExistMount
  名称|参数类型|描述 
  ---|---|---
  vm_uuid | string| 虚拟机uuid
  target_device | string| 指定驱动时该项为空,ide盘为hda~hdc，scsi盘为sda~sdo
  target_bus | string| 有效值：scsi, ide
  inner_volume |[inner_volume 对象](define.md#inner_volume) | 内置卷参数
  external_volume | [external_volume 对象](define.md#external_volume) | 外置卷参数
  
 #### inner_volume 
  名称|参数类型|描述 
  ---|---|---
  volume_uuid | string| 卷uuid
  
 #### external_volume 
  名称|参数类型|描述 
  ---|---|---
  pool_uuid | string| 池uuid
  volume_uuid | string| 卷uuid
 
 ####  VmDiskNotExistMount
  名称|参数类型|描述 
  ---|---|---
  vm_uuid | string| 虚拟机uuid
  target_device | string| 指定驱动时该项为空,ide盘为hda~hdc，scsi盘为sda~sdo
  target_bus | string| 有效值：scsi, ide
  volume_specification_uuid | string| 卷规格uuid
  
 #### VmNetworkCardAdd
  名称|参数类型|描述 
  ---|---|---
  vm_uuid | string| 虚拟机uuid
  switch_uuid | string| 交换机uuid
  network_card_type | string| 网卡类型
  interface_type | string| 网络类型
  interface_name | string| 二层网络名称
  port_group | string| 端口组uuid
  port_group_name | string| 端口组名称
  
 #### vm_security
  名称|参数类型|描述 
  ---|---|---
  vm_security_type | int32| 安全虚拟机类型
  image_path | string| 镜像路径
  image_size | uint64| 镜像大小
  pool_uuid | string| 池uuid
  security_vm_ip | string| 安全虚拟机ip
  
  
 #### storage
  名称|参数类型|描述 
  ---|---|---
  volume_specification | [volume_specification 对象](define.md#volume_specification) | 通过规格申请卷
  tenant_quota | [tenant_quota 对象](define.md#TenantQuota) | 租户扩容
  volume_expantion | [volume_expantion 对象](define.md#VolumeExpantion) | 卷扩容参数
  
  
 #### volume_specification
  名称|参数类型|描述 
  ---|---|---
  specification_uuid | string | 卷规格uuid
  specification_name | string | 卷规格name
  volume_name | string | 卷name
  volume_uuid | string | 卷uuid
  specification_info | specification_info 对象 | 当保存或者提交申请后，规格参数会保存在此对象中，请参考卷规格
  
 #### TenantQuota
 名称|参数类型|描述 
 ---|---|---
 cpu_count | uint32 | cpu配额
 memory_size | uint64 | memory配额
 disk_size | uint64 | 磁盘配额
 switch_count | int | 交换机配额
 router_count | int | 路由器配额
 gateway_count | int | 网关配额
 
 #### VolumeExpantion
  名称|参数类型|描述 
  ---|---|---
  volume_uuid | string | 卷uuid
  capacity | uint64 | 卷大小
  
  
 #### network
 名称|参数类型|描述 
 ---|---|---
 vip | [vip 对象](define.md#vip) | 虚拟ip申请相关的参数
 gateway | [ gateway 对象](define.md#Gateway) | 网关申请相关的参数
  
  
 #### vip
 名称|参数类型|描述 
 ---|---|---
  vip_count | int | 申请的虚拟ip的数量
  vip_list | [vipInfo 列表](define.md#vip_Info) | 分配的vip信息


 #### vip_Info
   名称|参数类型|描述 
   ---|---|---
   ip | string | ip地址
   gateway | string | 网关地址
   mask | string | 掩码


 #### Gateway
 名称|参数类型|描述 
 ---|---|---
 name | string | 网关名称
 out_ipv_4 | string | ipv4
 out_ipv_6 | string | ipv6
 enable_vlan | bool | 是否开启vlan
 vlan_label | string 列表 | vlan标签列表
 ip_type | int64 | ip类型
 network_name | string | 网卡名称
  
 #### container
 名称|参数类型|描述 
 ---|---|---
 auto_container | [auto_container 对象](define.md#auto_container) | 自定义创建容器
  

 #### auto_container
  名称|参数类型|描述 
  ---|---|---
  apply_container_info | apply_container_info 对象 |  参考创建容器参数
  apply_count | int |  需要创建的容器的数量
  container_info | map[string]string |  创建的容器的uuid和name
  success_count | int | 成功创建的容器的数量有多少个
  failed_count | int | 创建失败的容器有多少个
  faild_info | string 列表 | 如果创建容器失败，那么失败原因是什么
  
 
  #### Common
  名称|参数类型|描述 
  ---|---|---
  trash_delete | [trash_delete 对象](define.md#trash_delete)  | 回收站数据删除
  trash_restore | [trash_restore 对象](define.md#trash_restore) | 回收站数据恢复
 
 
 #### trash_delete
  名称|参数类型|描述 
  ---|---|---
  filter_object_type | int32 | 过滤的资源类型
  filter_object_name | string | 过滤的资源name
  start | int64 | 开始时间
  end | int64 | 结束时间
  object_list | TrashObjectUnit 列表 | 要删除的对象列表
 
 #### trash_restore
  名称|参数类型|描述 
  ---|---|---
  filter_object_type | int32 | 过滤的资源类型
  filter_object_name | string | 过滤的资源name
  start | int64 | 开始时间
  end | int64 | 结束时间
  object_list | TrashObjectUnit 列表 | 要删除的对象列表
  
 #### TrashObjectUnit
  名称|参数类型|描述 
  ---|---|---
  uuid | string | 资源对象uuid 
  name | string | 资源对象name 
  type | int32 | 资源对象类型  
  
  
  
  
  
  
  
  