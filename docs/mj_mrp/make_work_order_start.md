# 修改工单状态为开始

### URL

`http://host/api/mrp/work_order/<work_order_id>/action/start?database=<database>&access_token=<access_token>`

##### HTTP 方法:
POST

#####参数详细:
**work_order_id**: 工单id

**database**: 当前openerp启动使用的数据名字, 请咨询API开发者。

**access_token**:  用户登陆token， 请咨询API开发者

** 返回 **:

参考一下
**注**只有'草稿'状态的工单能开始
200

