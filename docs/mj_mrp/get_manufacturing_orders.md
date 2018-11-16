# 获取所有生产订单

### URL

`http://host/api/mrp/orders?database=<database>&access_token=<access_token>`

##### HTTP 方法:
GET

#####参数详细:

**database**: 当前openerp启动使用的数据名字, 请咨询API开发者。

**access_token**:  用户登陆token， 请咨询API开发者

** 返回 **:

参考一下

**hour_total** 工时
**project_name** 项目名称
**responsible** 负责人
**production_state** 订单状态
**project_id** 项目编号
**date_planned** 计划时间
**id** 订单编号
**date_start** 开始时间
**material_state** 物料状态

####可选订单状态值
**draft** 新建 
**confirmed** 已确定生产(等待投料)
**ready** 准备生产
**in_production** 已开始生产（生产中)
**done** 完成
**cancel** 已取消
**name** 工艺卡名称

####可选物料状态值
**preparation**: 备货中
**complete**: 已投料
``` 
[
    {
        "hour_total": 3333,
        "project_name": "项目1",
        "responsible_id": 1,
        "production_state": "done",
        "project_id": "222",
        "date_planned": "2015-06-10 06:22:27",
        "id": 1,
        "date_start": "2015-06-10 06:58:37",
        "material_state": "preparation",
        "name": "TC00003",
    },
    ...
]

```

