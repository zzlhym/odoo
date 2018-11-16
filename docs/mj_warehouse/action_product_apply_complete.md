# 备货中---备货完成

### URL

`http://host/api/warehouse/product-apply<picking_name>/<action>?database=<database>&access_token=<access_token>&location_id=<location_id>`

##### HTTP 方法:
PATCH

#####参数详细:

**database**: 当前openerp启动使用的数据名字, 请咨询API开发者。

**access_token**:  用户登陆token， 请咨询API开发者

**location_id**: 当前一体机id

**picking_name**:picking_name

**action**:complete

PATCH
**moves**

```
[
    {
        move_id: 1,
        product_uom_qty: 99
    }
    ...
]
```
表单形式传入如下
**moves.1.id**
**moves.1.product_uom_qty**
**moves.2.id**
**moves.2.product_uom_qty**
...

** 返回 **:

参考一下




```

