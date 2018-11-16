# 修改生产订单状态为已完成

### URL

`http://host/api/mrp/order/<id>/action/done?database=<database>&access_token=<access_token>`

##### HTTP 方法:
POST

#####参数详细:

**database**: 当前openerp启动使用的数据名字, 请咨询API开发者。

**access_token**:  用户登陆token， 请咨询API开发者

** 返回 **:
成功返回 200

