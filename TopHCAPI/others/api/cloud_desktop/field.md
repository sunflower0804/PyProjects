##VDCAgentMessageControlData
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 Message|string|是|-| 消息

##VDCAgentMachineControlData
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
HostIP|[]string|是|-| 主机ip
UpdateFilePath|string|否|-| 主机ip
UpdateFileName|string|否|-| 主机ip

##PrivateDiskInfo
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 DiskSizeByte|uint64|是|-|磁盘大小
 SecretKey|string|是|-|磁盘秘钥
 DuplicateNumber|int|是|-|磁盘副本
 PoolUuid|string|是|-| 存储池UUID
 PoolName|string|是|-| 存储池名称
 DiskType|string|是|-| 磁盘类型    //HDD/SSD
 DiskDrive|string|是|-|磁盘驱动类型  //scsi,sata,ide,virtio可选
 	
##UserGroupData
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 UserGroupName|string|是|-|用户组名称
 UserGroupUuid|string|是|-|用户组UUID
 TenantName|string|是|-|租户名称
 TenantUuid|string|是|-|租户UUID
 
##UserData
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 UserName|string|是|-|用户名称
 UserUuid|string|是|-|用户UUID
 TenantName|string|是|-|租户名称
 TenantUuid|string|是|-|租户UUID
 
##ADDomainServerConfig
 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 Enable|bool|是|-|是否开启
 StartIP|string|是|-|起始ip
 EndIP|string|是|-|终止ip
 NetMask|string|是|-|子网掩码
 GateWay|string|是|-|网关
 TimeZone|string|是|-|时区
 ADServerDNS|string|是|-|AD域DNS
 ADServerName|string|是|-|AD域服务器
 ADServerAdministrator|string|是|-|AD域管理员
 ADServerAdministratorPassword|string|是|-|AD域管理员密码