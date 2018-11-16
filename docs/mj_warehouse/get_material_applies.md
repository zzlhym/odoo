# 出货清单

### URL

`http://host/api/warehouse/mat-applies?database=<database>&access_token=<access_token>&location_id=<location_id>`

##### HTTP 方法:
GET

#####参数详细:

**database**: 当前openerp启动使用的数据名字, 请咨询API开发者。

**access_token**:  用户登陆token， 请咨询API开发者

**location_id**: 当前一体机id



** 返回 **:

参考一下

**project_name** 项目名称
**picking_name**取货编号
**date_done** 取货时间
**project_id** 项目编号
**picking_id**取货ID（内部属性）
**picking_loader** 取货人
**waiting_cancel**取消备货确认标志：
{
    1：显示取消备货确认
    0：已取消
}
**state** 状态:
{
    draft:    未备货
    confirmed:备货中
    assigned: 备货完成
    done:     完成取货
    cancel:   已取消
}

```
[
    {
     project_name: ""
     picking_name: "bz/PICK/00001"
     date_done: false
     state: ""
     project_id: ""
     picking_id: 1
     picking_loader: "admin"
     waiting_cancel：true/false
    }
    ...
]

```

