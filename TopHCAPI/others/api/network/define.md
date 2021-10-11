
### router_resp
create_time|int64|创建时间
update_time|int64|修改时间
router_uuid|string| 的uuid
enable|bool|是否启用
extra_info|map[string]string|额外信息，包含路由器名字等信息
load_balancer_info | []string| 负载均衡信息
router_name|string| 路由器别名，由租户名字+路由器名字,如CaiXS_lr100
nat|[]string|路由器SNAT信息
options|map[string]string |可选项
ports|[]string| 路由器端口信息
static_routes |[]string | 静态路由信息
port_mappings |[]string | 端口映射信息


#### TopoVM_object 对象
名称|参数类型|描述
---|---|---
vm_uuid|string|虚拟机uuid
vm_mac|string|虚拟机mac地址
network_node|NetworkNode_object|虚拟机在拓扑中的信息

#### NetworkNode_object 对象
名称|参数类型|描述
---|---|---
node_uuid|string|节点uuid
node_type|string|节点类型
coordinate_x|int32|横坐标
coordinate_y|int32|纵坐标
node_macs|[]string |节点的mac地址列表 

#### TopoGateway_object 对象
名称|参数类型|描述
---|---|---
gateway|Gateway_object|网关信息
network_node|NetworkNode_object|网关在拓扑中的信息

#### Gateway_object 对象
名称|参数类型|描述
---|---|---
create_time|int64|创建时间
update_time|int64|更新时间
gateway_uuid|string|网关uuid
gateway_name|string|网关名称
extra_info|map[string]string|额外信息，包括出口ip、网关名字等信息
ports|[]string|网关端口列表
other_config|map[string]string|其他配置信息

#### TopoSwitch_object 对象
名称|参数类型|描述
---|---|---
switch|Switch_object|交换机信息
network_node|NetworkNode_object|交换机在拓扑中的信息


#### Switch_object 对象
名称|参数类型|描述
---|---|---
create_time|int64|交换机创建时间
update_time|int64|交换机修改时间
switch_uuid|string|交换机uuid
switch_name|string|交换机名称
ACLs|[]string|交换机包含的acl规则
extra_info|[]string|交换机额外信息
ports|[]string|交换机端口列表
qos_rules|[]string|qos规则信息
other_config|map[string]string|其他配置信息，如exclude_ips,子网信息等


#### TopoRouter_object 对象
名称|参数类型|描述
---|---|---
router|Router_object|路由器信息
network_node|NetworkNode_object|交换机在拓扑中的信息

#### Router_object 对象
名称|参数类型|描述
---|---|---
create_time|int64|路由器创建时间
update_time|int64|路由器更新时间
router_uuid|string|路由器uuid
router_name|string|路由器名称
enable|bool|是否启用
extra_info|map[string]string|额外信息，包含路由器名字等信息
loadbalance_info|[]string|负载均衡信息
nats|[]string|路由器SNAT信息
options|map[string]string|可选项
ports|[]string|路由器端口信息
static_routes|[]string|静态路由信息
portmapping_info|[]string|端口映射信息


#### Links_object 对象
名称|参数类型|描述
---|---|---
from|TopoNode_object|连线的起始节点的信息
to|TopoNode_object|连线的结束节点的信息


#### Acl Object
名称|参数类型|描述
---|---|---
 priority|int| 优先级
 direction|string| 入口或出口
 action|string| 允许动作或拒绝动作等（allow or drop or reject or allow-related）
 protocol|string| 协议类型
 port |int| acl端口
 address_set_name|string| acl地址集名称
 remote_cidr_address|string| 指定的cidr_address，当remote指定为地址集时为空
 remote|string| 远程地址，地址集或cidr_address
 switch_port|int| 交换机端口
 
 
 #### Acl Object
 名称 | 参数类型 | 是否必填 | 默认值 | 描述 
 --- |---|---|--- |---
  priority|int| 是|- | 优先级
  direction|string| 是|""  | 入口或出口
  action|string| 是|""  | 允许动作或拒绝动作等（allow or drop or reject or allow-related）
  protocol|string| 是|""  | 协议类型
  port |int| 是|-  | acl端口
  address_set_name|string| 否| - | acl地址集名称
  remote_cidr_address|string| 否|""  | 指定的cidr_address，当remote指定为地址集时为空
  remote|string| 是|""  | 远程地址，地址集或cidr_address
  switch_port|int| 是|""  | 交换机端口