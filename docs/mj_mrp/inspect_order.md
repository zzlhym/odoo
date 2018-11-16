# 检验订单合格状态

### URL

`http://host/api/mrp/order/<order_id>/inspect?database=<database>&access_token=<access_token>`

##### HTTP 方法:
POST

#####参数详细:

#####URL参数
**order_id** 订单id

**database**: 当前openerp启动使用的数据名字, 请咨询API开发者。

**access_token**:  用户登陆token， 请咨询API开发者


#####POST表单参数
**inspect_state**: 审核状态，可选值:passed(通过), failed(未通过)

**failed_reason**: 如果inspect_state等于failed，此字段不能为空
** 返回 **:
如果成功，返回状态为200

