# 备货取消确认标志

### URL

`http://host/api/warehouse/mat-apply<picking_name>/<action>?database=<database>&access_token=<access_token>&location_id=<location_id>`

##### HTTP 方法:
PATCH

#####参数详细:

**database**: 当前openerp启动使用的数据名字, 请咨询API开发者。

**access_token**:  用户登陆token， 请咨询API开发者

**location_id**: 当前一体机id

**picking_name**:picking_name

**action**:cancel

** 返回 **:

参考一下




```

