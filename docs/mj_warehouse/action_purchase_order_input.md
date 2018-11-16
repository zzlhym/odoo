# 采购订单入库确认

### URL

`http://host/api/warehouse/purchase-orders/<name>/input?database=<database>&access_token=<access_token>&location_id=<location_id>`

##### HTTP 方法:
PATCH

#####参数详细:

**database**: 当前openerp启动使用的数据名字, 请咨询API开发者。

**access_token**:  用户登陆token， 请咨询API开发者

**location_id**: 当前一体机id

**name** 采购订单名称
#####lines内容
**move_id**
**product_qty_in**

```
[
    "lines":
    {
        "move_id": 1,
        "product_qty_in": 100,
    },
    {
        "move_id": 2,
        "product_qty_in": 50,
    },
    ...
]

```

** 返回 **:
如果成功，返回状态为200


