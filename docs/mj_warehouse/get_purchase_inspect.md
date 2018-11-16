# 物料检测详情

### URL

`http://host/api/warehouse/purchase-inspect/<order_name>?database=<database>&access_token=<access_token>&location_id=<location_id>`

##### HTTP 方法:
GET

#####参数详细:

**database**: 当前openerp启动使用的数据名字, 请咨询API开发者。

**access_token**:  用户登陆token， 请咨询API开发者

**location_id**: 当前一体机id

**order_name**:订单编号

** 返回 **:

参考一下


**purchaser**: 采购人
**supplier**: 供应商
**inspect_state**检测状态
{
  "0":未检测
  "1":检测中
  "2":检测完成
}
**date_order**:订购日期
**order_no**:订单编号 例"PO00002"
**order_id**:订单ID（内部属性）
**date_received**:收货日期
#####lines内容
**inspection_state**:检测状态
{
  "0":未检测
  "1":检测完成
}
**product_specification**:规格型号
**project_name**:项目名称
**product_uom**:计量单位
**state**:状态（内部属性）
**product_qty_planned**:计划数量
**product_uom_qty**:合格数量
**product_name**:产品名称
**move_id**:moveID（内部属性）
**product_no**:产品编号
#####检测返回信息
{
  "inspect_code":success
  "inspect_code_id"
}

```
[
   {
    purchaser: "Administrator"
    picking_state: "assigned"
    order_id: 2
    date_received: "2015-06-16"
    order_name: "PO00002"
    supplier: "供应商"
    date_order: "2015-06-16 10:26:42"
    "lines":[
               {
                inspection_state: 0
                product_specification: ""
                project_name: ""
                product_uom: "件"
                state: "assigned"
                product_qty_planned: 1
                product_uom_qty: 0
                product_name: "产品15"
                move_id: 31
                product_no: false
                inspect_code:"success"
                }
                .....

           ]


    "inspect_type_list":[
                            {
                            inspect_code: "success"
                            inspect_code_id: 0
                            }
                            {
                            inspect_code: "error1"
                            inspect_code_id: 11
                            }
                            {
                            inspect_code: "error2"
                            inspect_code_id: 12
                            }
                            {
                            inspect_code: "error3"
                            inspect_code_id: 13
                            }
                            {
                            inspect_code: "error4"
                            inspect_code_id: 14
                            }
                         ]
    }

]

```

