# 获取单个采购订单的详细内容

### URL

`http://host/api/warehouse/purchase-order/<name>?database=<database>&access_token=<access_token>&location_id=<location_id>`

##### HTTP 方法:
GET

#####参数详细:

**database**: 当前openerp启动使用的数据名字, 请咨询API开发者。

**access_token**:  用户登陆token， 请咨询API开发者

**location_id**: 当前一体机id

**order_id**: 采购订单id/采购订单二维码

** 返回 **:

参考一下

**supplier** 供应商
**purchaser** 采购人
**date_order** 订购时间
**date_received** 到货时间
**picking_state** 订单入库状态
{
  assigned：未入库
  done：已入库
}
#####lines内容
**product_no** 物料编号
**product_name** 产品名称
**project_name** 项目名称
**product_specification** 规格参数
**product_qty_planned** 采购数量
**product_uom** //计数单位
**product_uom_qty** 入库数量
**move_id** 调拨id
**state**

```
{
    "supplier": "供应商1",
    "purchaser": "采购人",
    "date_order": "2015-06-10 06:58:43",
    "date_received": "2015-06-10 06:58:43",
    "picking_state": "draft"
    "lines": [
         {
            "product_specification": ""
            "project_name": ""
            "product_uom": "件"
            "state": "done"
            "product_qty_planned": 21
            "product_uom_qty": 0
            "product_name": "原材料2"
            "move_id": 13
            "product_no": "N12323"
         },
        {
            "product_no": "N0002",
            "product_name": "电视机",
            "project_name": "1111",
            "product_specification": "111",
            "product_uom_qty": 100,
            "product_uom": "件"
            "product_qty_planned": 100  
            "move_id": 2
            "state":"done"
        }
    ]
}

```

