# 物料检测详情

### URL

`http://host/api/warehouse/move/<move_id>/<action>?database=<database>&access_token=<access_token>&location_id=<location_id>`

##### HTTP 方法:
PATCH

#####参数详细:

**database**: 当前openerp启动使用的数据名字, 请咨询API开发者。

**access_token**:  用户登陆token， 请咨询API开发者

**location_id**: 当前一体机id

**move_id**:moveID

**action**:inspect

**inspect_res_code**: 错误类型别号

**product_uom_qty**:通过质检数量

** 返回 **:

参考一下


```

