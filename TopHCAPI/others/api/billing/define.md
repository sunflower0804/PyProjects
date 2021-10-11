#### speficiation_resp
名称|参数类型|描述 
---|---|---
 tenant_uuid|string| 租户uuid
 tenant_name|string| 租户名称
 specification_uuid|string| 规格uuid
 type|string| 类型
 price|float64| 价格
 quantity_unit|string| 数量单位
 time_unit|string| 时间单位
 start_time|int64| 开始时间
 end_time|int64| 结束时间
 description|string| 描述信息



#### month_resp
名称|参数类型|描述 
---|---|---
 uuid|string| 账单的uuid
 name|string| 账单的name
 status|string| 账单的状态
 update_time|int| 修改时间
 create_time|int| 创建时间
 tenant_uuid|string| 租户uuid
 tenant_name|string| 租户name
 operator_tenant_uuid|string| 操作者所属租户uuid
 operator_tenant_name|string| 操作者所属租户name
 operator_uuid|string| 操作者uuid
 operator_name|string| 操作者name
 operator_time|int| 操作时间
 total_fee|float| 总价
 cpu_fee|float| cpu总价
 memory_fee|float| mem总价
 disk_fee|float| disk总价
 cpu_detail_list|[record 列表](define.md#record_resp)| cpu详情列表
 memory_detail_list|[record 列表](define.md#record_resp)| mem详情列表
 disk_detail_list|[record 列表](define.md#record_resp)| disk详情列表

 
 #### record_resp
 名称|参数类型|描述 
 ---|---|---
  record_uuid|string| 记录uuid
  tenant_uuid|string| 租户uuid
  tenant_name|string| 租户name
  start_time|int| 开始时间
  end_time|int| 结束时间
  type|string| 记录的类型，和规格的类型对应
  qos|int| cpu，mem，disk大小
  quantity_unit|string| 数量单位，M G T
  time_unit|string| 时间单位，小时 天
  price|float| 价格
  fee|float| 价钱
  specification_tenant_uuid|string| 对一个的规格的租户uuid
  specification_tenant_name|string| 对一个的规格的租户name
  specification_uuid|string| 规格uuid
  specification_name|string| 规格name
  
  
  
 
 
 
 
 
 
 