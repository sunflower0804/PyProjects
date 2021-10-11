[back to api overview](../api_overview.md#api)

## /v1/tencent/billing/project/inspct
#### 功能：按照项目汇总费用分布
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
EndTime | int64|是|- |结束时间
StartTime | int64|是|- |开始时间
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
PageNum | int|否|0 |页数
PageSize | int|否|0 |页大小


### 返回参数
名称|参数类型|描述
---|---|---
Ready | uint64 | 数据是否准备好，0未准备好，1准备好
SummaryOverview |array|各项目花费分布详情
Total|int|各项目花费分布总数
RequestId|string|唯一请求 ID

### SummaryOverview 对象
ProjectId|string|项目ID
ProjectName||项目名称
RealTotalCost|string|实际花费
RealTotalCostRatio|string|费用所占百分比
CashPayAmount|string|现金金额
IncentivePayAmount|string|赠送金金额
VoucherPayAmount|string|代金券金额
BillMonth|string|账单月份

### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/billing/project/inspct
```
Body:
```
{
    "BeginTime": "2021-08",
    "EndTime": "2021-08",
    "PageNum": null,
    "TenantUuid": "system",
    "ClusterUuid": "72db4b34-1473-418f-ade4-de00b956f16b"
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
    "Response": {
      "Ready": 1,
      "SummaryOverview": [
        {
          "ProjectId": "1196468",
          "ProjectName": "薛定谔的猫",
          "RealTotalCost": "1.42",
          "RealTotalCostRatio": "85.83",
          "CashPayAmount": "1.42",
          "IncentivePayAmount": "0.00",
          "VoucherPayAmount": "0.00",
          "BillMonth": "2021-08"
        },
        {
          "ProjectId": "0",
          "ProjectName": "默认项目",
          "RealTotalCost": "0.24",
          "RealTotalCostRatio": "14.17",
          "CashPayAmount": "0.24",
          "IncentivePayAmount": "0.00",
          "VoucherPayAmount": "0.00",
          "BillMonth": "2021-08"
        }
      ],
      "Total": 2,
      "RequestId": "0c1c5c21-a833-46ce-b2fa-b285e56a65**"
    }
  }
}
```

#### 异常返回示例

### 状态码


## /v1/tencent/describe/account/balance
#### 功能：获取账号余额
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid

### 返回参数
名称|参数类型|描述
Balance|int64|可用余额
Freezing|int64|冻结余额
Incentive|int64|赠送金余额
Cash|int64|现金余额
Arrears|int64|欠费

### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/describe/account/balance
```
Body:
```
{
    "TenantUuid": "system",
    "ClusterUuid": "72db4b34-1473-418f-ade4-de00b956f16*"
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
    "Balance": 24,
    "Freezing": null,
    "Incentive": null,
    "Cash": null,
    "Arrears": 0
  }
}
```

#### 异常返回示例

### 状态码


## /v1/tencent/describe/bill/list
#### 功能：获取收支明细列表
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
EndTime | int64|是|- |结束时间
StartTime | int64|是|- |开始时间
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Offset | int|否|0 |翻页偏移量
Limit | int|否|10 |每页的限制数量
PayType |array string|是|- |交易类型
SubPayType |array string|是|- |扣费模式
WithZeroAmount |uint64|否|0 |是否返回0元交易金额的交易项

### 返回参数
名称|参数类型|描述
TransactionList|struct|收支明细列表
Total|int64|总条数
ReturnAmount|float64|退费总额
RechargeAmount|float64|充值总额
BlockAmount|float64|冻结总额
UnblockAmount|float64|解冻总额
DeductAmount|float64|扣费总额
AgentInAmount|float64|资金转入总额
AdvanceRechargeAmount|float64|垫付充值总额
WithdrawAmount|float64|提现扣减总额
AgentOutAmount|float64|资金转出总额
AdvancePayAmount|float64|还垫付总额
EntryTotal|float64|入账总数
LogoutTotal|float64|出账总数
RequestId|string|唯一请求 ID

### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/describe/bill/list
```
Body:
```
{
    "StartTime": "2021-08-01 00:00:00",
    "EndTime": "2021-08-26 15:45:35",
    "Offset": 0,
    "PayType": [
        "all"
    ],
    "SubPayType": [
        "all"
    ],
    "WithZeroAmount": 0,
    "Limit": 10,
    "TenantUuid": "system",
    "ClusterUuid": "72db4b34-1473-418f-ade4-de00b956f1**"
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
    "Response": {
      "TransactionList": [
        {
          "ActionType": "deduct",
          "Amount": -1,
          "Balance": 129,
          "BillId": "20210805673043426690542",
          "OperationInfo": "云硬盘CBS-广州-08月按小时结算扣费",
          "OperationTime": "2021-08-05 23:05:15.873",
          "Cash": 130,
          "Incentive": 0,
          "Freezing": 1,
          "PayChannel": "用户余额",
          "DeductMode": "hourh"
        },
      ],
      "Total": 7,
      "ReturnAmount": 0,
      "RechargeAmount": 0,
      "BlockAmount": -1,
      "UnblockAmount": 0,
      "DeductAmount": -6,
      "AgentInAmount": 0,
      "AdvanceRechargeAmount": 0,
      "WithdrawAmount": 0,
      "AgentOutAmount": 0,
      "AdvancePayAmount": 0,
      "EntryTotal": 0,
      "logoutTotal": -7,
      "RequestId": "5e151eed-e16b-4e78-a9d1-ec9851ac06**"
    }
  }
}
```

#### 异常返回示例

### 状态码


## /v1/tencent/describe/orders/data
#### 功能：查询订单数据
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Offset | int|否|0 |翻页偏移量
Limit | int|否|10 |每页的限制数量
EndTime | string|是|- |结束时间
StartTime | string|是|- |开始时间
Status | int64|否|4 |订单状态

### 返回参数
名称|参数类型|描述
Deals|array|订单列表
TotalCount|int64|订单总数
RequestId|string|唯一请求 ID

### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/describe/orders/data
```
Body:
```
{
    "Status": 1,
    "Limit": 999,
    "StartTime": "2016-01-01 00:00:00",
    "EndTime": "2021-08-26 16:01:29",
    "TenantUuid": "system",
    "ClusterUuid": "72db4b34-1473-418f-ade4-de00b956f16b"
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
    "Response": {
      "TotalCount": 0,
      "RequestId": "fbdfa57c-0471-44b4-8dcd-52723fbe267*"
    }
  }
}
```

#### 异常返回示例

### 状态码


## /v1/tencent/cost/summary/product
#### 功能：获取按产品汇总消耗详情
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Offset | int|否|0 |翻页偏移量
Limit | int|否|10 |每页的限制数量
EndTime | string|是|- |结束时间
StartTime | string|是|- |开始时间

### 返回参数
名称|参数类型|描述
Ready|uint64|数据是否准备好，0未准备好，1准备好
Total|struct|消耗详情
Data|array |消耗按产品汇总详情
RecordNum|uint64|记录数量
RequestId|string|唯一请求 ID

### Data 参数
BusinessCode |string|产品码
BusinessCodeName |string|产品名称
RealTotalCost |string|折后总价
Trend |struct|费用趋势

### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/describe/summary/product
```
Body:
```
{
    "BeginTime": "2021-08-01 00:00:00",
    "EndTime": "2021-08-31 23:59:59",
    "TenantUuid": "system",
    "ClusterUuid": "72db4b34-1473-418f-ade4-de00b956f16b"
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
    "Response": {
      "Ready": 1,
      "SummaryTotal": {
        "RealTotalCost": "1.66",
        "VoucherPayAmount": "0.00",
        "IncentivePayAmount": "0.00",
        "CashPayAmount": "1.66"
      },
      "SummaryOverview": [
        {
          "BusinessCode": "p_cbs",
          "BusinessCodeName": "云硬盘CBS",
          "RealTotalCost": "1.42",
          "RealTotalCostRatio": "85.83",
          "CashPayAmount": "1.42",
          "IncentivePayAmount": "0.00",
          "VoucherPayAmount": "0.00",
          "BillMonth": "2021-08"
        },
        {
          "BusinessCode": "billVirtualId",
          "BusinessCodeName": "月度计费精度差异",
          "RealTotalCost": "0.15",
          "RealTotalCostRatio": "9.09",
          "CashPayAmount": "0.15",
          "IncentivePayAmount": "0.00",
          "VoucherPayAmount": "0.00",
          "BillMonth": "2021-08"
        },
        {
          "BusinessCode": "p_cos",
          "BusinessCodeName": "COS 对象存储",
          "RealTotalCost": "0.08",
          "RealTotalCostRatio": "5.08",
          "CashPayAmount": "0.08",
          "IncentivePayAmount": "0.00",
          "VoucherPayAmount": "0.00",
          "BillMonth": "2021-08"
        }
      ],
      "Total": 3,
      "RequestId": "dda32ce6-e16f-4f8b-8c7f-d8c17943f0f7"
    }
  }
}
```

#### 异常返回示例

### 状态码


## /v1/tencent/cost/summary/region
#### 功能：获取按地域汇总消耗详情
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TenantUuid | string|是|- |租户uuid
 ClusterUuid | string|是|- |集群uuid
 PageNum | int|否|0 |翻页偏移量
 PageSize | int|否|0 |每页的限制数量
 EndTime | string|是|- |结束时间
 StartTime | string|是|- |开始时间

### 返回参数
名称|参数类型|描述
---|---|---
Ready|uint64|数据是否准备好，0未准备好，1准备好
Total|struct|消耗详情
Data|array |消耗按地域汇总详情
RecordNum|uint64|记录数量
RequestId|string|唯一请求 ID

### Data 参数
BusinessCode |string|产品码
BusinessCodeName |string|产品名称
RealTotalCost |string|折后总价
Trend |struct|费用趋势

### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/describe/summary/region
```
Body:
```
{
    "BeginTime": "2021-08",
    "EndTime": "2021-08",
    "PageSize": 10,
    "PageNum": 0,
    "TenantUuid": "system",
    "ClusterUuid": "72db4b34-1473-418f-ade4-de00b956f16b"
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
    "Response": {
      "Ready": 1,
      "SummaryOverview": [
        {
          "RegionId": "1",
          "RegionName": "华南地区（广州）",
          "RealTotalCost": "1.42",
          "RealTotalCostRatio": "85.83",
          "CashPayAmount": "1.42",
          "IncentivePayAmount": "0.00",
          "VoucherPayAmount": "0.00",
          "BillMonth": "2021-08"
        },
        {
          "RegionId": "0",
          "RegionName": "其他",
          "RealTotalCost": "0.15",
          "RealTotalCostRatio": "9.09",
          "CashPayAmount": "0.15",
          "IncentivePayAmount": "0.00",
          "VoucherPayAmount": "0.00",
          "BillMonth": "2021-08"
        },
        {
          "RegionId": "11",
          "RegionName": "华南地区（深圳金融）",
          "RealTotalCost": "0.08",
          "RealTotalCostRatio": "5.08",
          "CashPayAmount": "0.08",
          "IncentivePayAmount": "0.00",
          "VoucherPayAmount": "0.00",
          "BillMonth": "2021-08"
        },
        {
          "RegionId": "23",
          "RegionName": "亚太地区（泰国）",
          "RealTotalCost": "0.00",
          "RealTotalCostRatio": "0.00",
          "CashPayAmount": "0.00",
          "IncentivePayAmount": "0.00",
          "VoucherPayAmount": "0.00",
          "BillMonth": "2021-08"
        }
      ],
      "Total": 4,
      "RequestId": "e1342cb3-60c8-49c2-914e-ae3f099c0e48"
    }
  }
}
```

#### 异常返回示例

### 状态码


## /v1/tencent/describe/bill/detail
#### 功能：查询账单明细数据
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
TenantUuid | string|是|- |租户uuid
ClusterUuid | string|是|- |集群uuid
Offset | int|否|0 |翻页偏移量
Limit | int|否|10 |每页的限制数量
PeriodType|string|是|- |计费模式
ShowZeroCost|bool|否|0 |是否显示0元
NeedRecordNum|int64|否|0 |是否需要访问列表的总记录数，1-表示需要， 0-表示不需要
Month|string|是|- |月份

### 返回参数
名称|参数类型|描述
---|---|---
DetailSet|array|详情列表
Total|uint64|总记录数
RealTotalCost|float64|月度汇总使用金额
VoucherPayAmount|float64|代金券支付金额
CashPayAmount|float64|现金账户支付金额
IncentivePayAmount|float64|赠送账户支付金额
RequestId|string|唯一请求 ID

### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/describe/bill/detail
```
Body:
```
{
    "PeriodType": "byPayTime",
    "Offset": 0,
    "ShowZeroCost": false,
    "Limit": 10,
    "NeedRecordNum": 1,
    "Month": "2021-02",
    "TenantUuid": "system",
    "ClusterUuid": "72db4b34-1473-418f-ade4-de00b956f16b"
}
```
#### 正常返回示例
```
"data": {
    "Response": {
      "DetailSet": [
        {
          "BusinessCodeName": "COS 对象存储",
          "ProductCodeName": "COS 标准存储",
          "PayModeName": "按量计费",
          "ProjectName": "默认项目",
          "RegionName": "华南地区（深圳金融）",
          "ZoneName": "深圳金融一区",
          "ResourceId": "100015007673-std_read-17",
          "ResourceName": "",
          "ActionTypeName": "按量计费月结",
          "OrderId": "202102",
          "BillId": "20210201000000760502821286626783",
          "PayTime": "2021-02-01 08:02:57",
          "FeeBeginTime": "2021-01-01 00:00:00",
          "FeeEndTime": "2021-01-31 23:59:59",
          "ComponentSet": [
            {
              "ComponentCodeName": "标准存储请求",
              "ItemCodeName": "COS 标准存储读请求",
              "SinglePrice": "0.01",
              "SpecifiedPrice": "0.01",
              "PriceUnit": "元/万次请求/月",
              "UsedAmount": "0.0024",
              "UsedAmountUnit": "万次请求",
              "TimeSpan": "1",
              "TimeUnitName": "月",
              "Cost": "2.4E-5",
              "Discount": "1",
              "ReduceType": "折扣",
              "RealCost": "2.4E-5",
              "VoucherPayAmount": "0",
              "CashPayAmount": "2.4E-5",
              "IncentivePayAmount": "0",
              "ItemCode": "sv_cos_std_req_r",
              "ComponentCode": "v_cos_std_req",
              "ContractPrice": "0.01"
            }
          ],
          "PayerUin": "100015007673",
          "OwnerUin": "100015007673",
          "OperateUin": "100015007673",
          "BusinessCode": "p_cos",
          "ProductCode": "sp_cos_std",
          "ActionType": "postpay_deduct_m",
          "RegionId": "11",
          "ProjectId": 0
        },
        "Total": 8,
        "RealTotalCost": 1.3552527156068805e-20,
        "VoucherPayAmount": 0,
        "CashPayAmount": 0,
        "IncentivePayAmount": 0,
        "RequestId": "61f6280e-e364-461d-bee2-ec9acfaaf47a"
        }
     }
```

#### 异常返回示例

### 状态码


## /v1/tencent/describe/bill/summary
#### 功能：查询账单汇总数据
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TenantUuid | string|是|- |租户uuid
 ClusterUuid | string|是|- |集群uuid
 Offset | int|否|0 |翻页偏移量
 Limit | int|否|10 |每页的限制数量
 PeriodType|string|是|- |计费模式
 ShowZeroCost|bool|否|0 |是否显示0元
 NeedRecordNum|int64|否|0 |是否需要访问列表的总记录数，1-表示需要， 0-表示不需要
 Month|string|是|- |月份

### 返回参数
名称|参数类型|描述
---|---|---
ResourceSummarySet|array|资源汇总列表
Total|int64|资源汇总列表总数
RealTotalCost|float64|月度汇总使用金额
VoucherPayAmount|float64|代金券支付金额
CashPayAmount|float64|现金账户支付金额
IncentivePayAmount|float64|赠送账户支付金额
RequestId|string|唯一请求 ID

### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/describe/bill/summary
```
Body:
```
{
    "PeriodType": "byPayTime",
    "Offset": 0,
    "Limit": 10,
    "ShowZeroCost": false,
    "NeedRecordNum": 1,
    "Month": "2021-02",
    "TenantUuid": "system",
    "ClusterUuid": "72db4b34-1473-418f-ade4-de00b956f16b"
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
    "Response": {
      "ResourceSummarySet": [
        {
          "BusinessCodeName": "COS 对象存储",
          "ProductCodeName": "COS 标准存储",
          "PayModeName": "按量计费",
          "ProjectName": "默认项目",
          "RegionName": "华南地区（深圳金融）",
          "ZoneName": "深圳金融一区",
          "ResourceId": "100015007673-std_read-17",
          "ResourceName": "",
          "ActionTypeName": "按量计费月结",
          "OrderId": "-",
          "PayTime": "-",
          "FeeBeginTime": "2021-01-01 00:00:00",
          "FeeEndTime": "2021-01-31 23:59:59",
          "ConfigDesc": "标准存储请求: 0.0024万次请求; ",
          "ExtendField1": "-",
          "ExtendField2": "-",
          "TotalCost": "2.4E-5",
          "Discount": "1",
          "ReduceType": "折扣",
          "RealTotalCost": "2.4E-5",
          "VoucherPayAmount": "0",
          "CashPayAmount": "2.4E-5",
          "IncentivePayAmount": "0",
          "ExtendField3": "-",
          "ExtendField4": "-",
          "ExtendField5": "-",
          "PayerUin": "100015007673",
          "OwnerUin": "100015007673",
          "OperateUin": "100015007673",
          "BusinessCode": "p_cos",
          "ProductCode": "sp_cos_std",
          "RegionId": 11
        },
      ],
      "Total": 7,
      "RealTotalCost": -6.776263578034403e-21,
      "VoucherPayAmount": 0,
      "CashPayAmount": -6.776263578034403e-21,
      "IncentivePayAmount": 0,
      "RequestId": "17406bfd-dd2b-424d-a0db-96924f1de420"
    }
  }
}
```

#### 异常返回示例

### 状态码


## /v1/tencent/bill/month/cost
#### 功能：查询月度账单金额
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TenantUuid | string|是|- |租户uuid
 ClusterUuid | string|是|- |集群uuid

### 返回参数
名称|参数类型|描述
---|---|---
CostList |array|月度账单金额

### CostList
---|---|---
Month |string|月份
RealTotalCost|string|总花费
VoucherPayAmount|string|代金券金额
IncentivePayAmount|string|赠送金金额
CashPayAmount|string|现金金额

### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/bill/month/cost
```
Body:
```
{
    "TenantUuid": "system",
    "ClusterUuid": "72db4b34-1473-418f-ade4-de00b956f16b"
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
    "CostList": [
      {
        "Month": "2020-09",
        "RealTotalCost": "3.56",
        "VoucherPayAmount": "0.00",
        "IncentivePayAmount": "0.00",
        "CashPayAmount": "3.56"
      },
     ]
  }
}
```

#### 异常返回示例

### 状态码


## /v1/tencent/describe/summary/paymode
#### 功能：获取按付费模式汇总费用分布
#### 请求类型：post

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TenantUuid | string|是|- |租户uuid
 ClusterUuid | string|是|- |集群uuid
Offset | int|否|0 |翻页偏移量
Limit | int|否|10 |每页的限制数量
EndTime | string|是|- |结束时间
StartTime | string|是|- |开始时间

### 返回参数
名称|参数类型|描述
---|---|---
Ready|uint64|数据是否准备好，0未准备好，1准备好
SummaryOverview|array|各付费模式花费分布详情
Total|int|总数
RequestId|string|唯一请求 ID

### SummaryOverview
---|---|---
PayMode|string|付费模式
PayModeName|string|付费模式名称
RealTotalCost|string|实际花费
RealTotalCostRatio|string|费用所占百分比
Detail|array|按交易类型
CashPayAmount|string|现金金额
IncentivePayAmount|string|赠送金金额
VoucherPayAmount|string|代金券金额

### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/describe/summary/paymode
```
Body:
```
{
    "BeginTime": "2021-08",
    "EndTime": "2021-08",
    "Limit": 10,
    "Offset": 0,
    "TenantUuid": "system",
    "ClusterUuid": "72db4b34-1473-418f-ade4-de00b956f16b"
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
    "Response": {
      "Ready": 1,
      "SummaryOverview": [
        {
          "PayMode": "prePay",
          "PayModeName": "包年包月",
          "RealTotalCost": "0.00",
          "RealTotalCostRatio": "0.00",
          "CashPayAmount": "0.00",
          "IncentivePayAmount": "0.00",
          "VoucherPayAmount": "0.00"
        },
        {
          "PayMode": "postPay",
          "PayModeName": "按量计费",
          "RealTotalCost": "1.66",
          "RealTotalCostRatio": "100.00",
          "Detail": [
            {
              "ActionType": "postpay_deduct_h",
              "ActionTypeName": "按量计费小时结",
              "RealTotalCost": "1.42",
              "RealTotalCostRatio": "85.83",
              "CashPayAmount": "1.42",
              "IncentivePayAmount": "0.00",
              "VoucherPayAmount": "0.00",
              "BillMonth": "2021-08"
            },
          ],
          "CashPayAmount": "1.66",
          "IncentivePayAmount": "0.00",
          "VoucherPayAmount": "0.00"
        }
      ],
      "Total": 2,
      "RequestId": "2148e830-8345-4bdb-aeb4-e497080bfc17"
    }
  }
}
```

#### 异常返回示例

### 状态码


## /v1/tencent/describe/summary/region
#### 功能：获取按地域汇总费用分布
#### 请求类型：post/get

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 TenantUuid | string|是|- |租户uuid
  ClusterUuid | string|是|- |集群uuid
 PageNum | int|否|0 |翻页偏移量
 PageSize | int|否|0 |每页的限制数量
 EndTime | string|是|- |结束时间
 StartTime | string|是|- |开始时间

### 返回参数
名称|参数类型|描述
Ready|uint64|数据是否准备好，0未准备好，1准备好
SummaryOverview|array|各付费模式花费分布详情
Total|int|总数
RequestId|string|唯一请求 ID

### SummaryOverview
---|---|---
RegionId|string|地域ID
RegionName|string|地域名称
RealTotalCost|string|实际花费
RealTotalCostRatio|string|费用所占百分比
Detail|array|按交易类型
CashPayAmount|string|现金金额
IncentivePayAmount|string|赠送金金额
VoucherPayAmount|string|代金券金额

### 示例

#### 请求示例
```
http://10.30.12.97:8080/v1/tencent/describe/summary/region
```
Body:
```
{
    "BeginTime": "2021-08",
    "EndTime": "2021-08",
    "PageSize": 10,
    "PageNum": 0,
    "TenantUuid": "system",
    "ClusterUuid": "72db4b34-1473-418f-ade4-de00b956f16b"
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
    "Response": {
      "Ready": 1,
      "SummaryOverview": [
        {
          "RegionId": "1",
          "RegionName": "华南地区（广州）",
          "RealTotalCost": "1.42",
          "RealTotalCostRatio": "85.83",
          "CashPayAmount": "1.42",
          "IncentivePayAmount": "0.00",
          "VoucherPayAmount": "0.00",
          "BillMonth": "2021-08"
        },
      ],
      "Total": 4,
      "RequestId": "366ddf38-ff40-4f73-82b5-e817d00e0755"
    }
  }
}
```

#### 异常返回示例

### 状态码