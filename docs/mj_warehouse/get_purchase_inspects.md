# 物料检测

### URL

`http://host/api/warehouse/purchase-inspects?database=<database>&access_token=<access_token>&location_id=<location_id>`

##### HTTP 方法:
GET

#####参数详细:

**database**: 当前openerp启动使用的数据名字, 请咨询API开发者。

**access_token**:  用户登陆token， 请咨询API开发者

**location_id**: 当前一体机id



** 返回 **:

参考一下


**purchaser**: 采购人
**supplier**: 供应商
**state**: 状态（内部属性）
**project_name**:项目名称
**date_order**:订购日期
**order_no**:订单编号 例"PO00002"
**order_id**:订单ID（内部属性）
**project_id**: 项目ID（内部属性）
**date_received**:收货日期
**inspect_state**:检测状态
{
  "0":未检测
  "1":检测中
  "2":检测完成
}


```
[
    {
    purchaser: "Administrator"
    supplier: "供应商"
    state: "approved"
    project_name: ""
    date_order: "2015-06-16 10:26:42"
    order_no: "PO00002"
    order_id: 2
    project_id: ""
    inspect_state: 1
    date_received: "2015-06-16"
    }
    ...
]

```

