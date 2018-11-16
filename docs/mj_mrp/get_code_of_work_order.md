# 获取工单相关的代码

### URL

`http://host/api/mrp/work_orders/<work_order_id>/code?database=<database>&access_token=<access_token>`

##### HTTP 方法:
GET

#####参数详细:
**work_order_id**: 工单id

**database**: 当前openerp启动使用的数据名字, 请咨询API开发者。

**access_token**:  用户登陆token， 请咨询API开发者

** 返回 **:
http返回body内容为代码内容
参考一下

