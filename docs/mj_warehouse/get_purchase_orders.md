# 获取一体机所在仓库所有采购订单

### URL

`http://host/api/warehouse/purchase-orders?database=<database>&access_token=<access_token>&location_id=<location_id>`

##### HTTP 方法:
GET

#####参数详细:

**database**: 当前openerp启动使用的数据名字, 请咨询API开发者。

**access_token**:  用户登陆token， 请咨询API开发者

**location_id**: 当前一体机id

** 返回 **:

参考一下

**purchaser** 采购员
**supplier** 供应商
**state**采购单状态（内部属性）
**picking_state** 订单入库状态
{
  assigned：未入库
  done：已入库
}
**project_name** 项目名称
**project_id**项目编号
**date_order** 订购时间
**date_received** 到货时间
**order_id** 订单id
**order_no** 订单编号

```
[
    {
    "purchaser": "Administrator"
    "supplier": "原材料供应商1"
    "state": "approved"
    "picking_state": "done"
    "project_name": ""
    "date_order": "2015-06-13 05:44:21"
    "date_received": "2015-06-13"
    "order_no": "PO00001"
    "order_id": 1
    "project_id": ""

    },
    ...
]

```

