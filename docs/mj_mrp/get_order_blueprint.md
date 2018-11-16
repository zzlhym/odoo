# 获取订单的图纸图片

### URL

`http://host/api/mrp/order/<order_id>/blueprint?database=<database>&access_token=<access_token>&size=big`

##### HTTP 方法:
GET

#####参数详细:

**database**: 当前openerp启动使用的数据名字, 请咨询API开发者。

**access_token**:  用户登陆token， 请咨询API开发者

**order_id**: 订单id

**size**: 可选选项(big, small, medium)

** 返回 **:
图片数据
参考一下

