# 取货清单--未备货

### URL

`http://host/api/warehouse/mat-apply<picking_name>?database=<database>&access_token=<access_token>&location_id=<location_id>`

##### HTTP 方法:
GET

#####参数详细:

**database**: 当前openerp启动使用的数据名字, 请咨询API开发者。

**access_token**:  用户登陆token， 请咨询API开发者

**location_id**: 当前一体机id

**picking_name**:<picking_name>

** 返回 **:

参考一下

**product_qty_planned** 数量
**project_name**项目名称
**product_uom** 计量单位
**material_specification** 规格型号
**project_id** 项目编号
**product_uom_qty**备货数量
**product_name** 产品名称
**product_no**物料编号
**move_id**


```
[
    {
     product_qty_planned: 33
     project_name: ""
     product_uom: "件"
     material_specification: ""
     project_id: ""
     product_uom_qty: 0
     product_name: "产品2"
     move_id: 2
     product_no: false
    }
    ...
]

```

