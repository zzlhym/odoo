# 获取图纸相关的工单信息

### URL

`http://host/api/mrp/work_orders/search_with/<blueprint_id>?database=<database>&access_token=<access_token>`

##### HTTP 方法:
GET

#####参数详细:
**blueprint_id**: 图纸id

**database**: 当前openerp启动使用的数据名字, 请咨询API开发者。

**access_token**:  用户登陆token， 请咨询API开发者

** 返回 **:
**project_name**: 项目编号
**project_id**: 项目id
**bom_name**: 物料清单名称
**bom_id**: 物料id
**work_lines**: 工单列表
**work_lines:name**: 工单名称
**work_lines:date_planned**: 计划时间

参考一下


``` 
{
    "project_name": "项目1",
    "project_id": "2222",
    "bom_name": "电视机1",
    "bom_id": 1,
    "work_lines": [
        {
            "name": "操作13 - 电视机1",
            "hour": 0,
            "date_planned": "2015-06-23 08:56:50",
            "date_finished": false,
            "responsible": false,
            "state": "draft",
            "id": 5
        },
	...
    ]
}
```

