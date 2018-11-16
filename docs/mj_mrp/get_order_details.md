# 获取单个生产订单的详细内容（包括工序列表)

### URL

`http://host/api/mrp/order/<order_id>?database=<database>&access_token=<access_token>`

##### HTTP 方法:
GET

#####参数详细:

**database**: 当前openerp启动使用的数据名字, 请咨询API开发者。

**access_token**:  用户登陆token， 请咨询API开发者

** 返回 **:

参考一下
**project_name** 项目名称
**project_id** 项目编号
**bom_id** 物料清单id
**bom_name** 物料清单名称
**inspect_state** 检验状态
**inspect_failed_reason** 检验为未通过时的原因
#####lines内容
**name** 工序名称
**hour** 加工工时
**date_finished** 完成时间
**state** 加工状态
**responsible** 负责人
**id** 工序id
**date_start** 开始时间

``` 
{
    "project_name": "项目1",
    "project_id": "222",
    "bom_id": 1
    "bom_name": "电视机1"
    "lines": [
        {
            "name": "操作1 - 电视机1",
            "hour": 1111,
            "date_finished": "2015-06-10 06:58:43",
            "state": "done",
            "responsible_id": "",
            "id": 1
        },
        {
            "name": "操作2 - 电视机1",
            "hour": 2222,
            "date_finished": "2015-06-10 06:58:43",
            "state": "done",
            "responsible_id": "",
            "id": 2
        }
    ],
}

```

