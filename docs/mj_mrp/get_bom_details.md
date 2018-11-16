# 获取检验出错原因

### URL

`http://host/api/mrp/bom/<bom_id>?database=<database>&access_token=<access_token>`

##### HTTP 方法:
GET

#####参数详细:
**bom_id**: 物料清单id

**database**: 当前openerp启动使用的数据名字, 请咨询API开发者。

**access_token**:  用户登陆token， 请咨询API开发者

** 返回 **:

参考一下
**bom_id**: 物料清单id
**bom_lines**: 物料单列表
**bom_lines id**: 列表id
**bom_lines product_name**: 产品名称
**bom_lines product_qty**: 产品数量
**bom_lines product_uom**: 产品单位
**variants**: 产品型号(这里可以有多个型号)

``` 
{
    "bom_id": 1,
    "bom_lines": [
        {
            "variants": [
                {
                    "name": "型号1"
                },
                {
                    "name": "型号2"
                }
            ],
            "product_qty": 1,
            "id": 1,
            "product_uom": "件",
            "product_name": "显示器1"
        }
    ]
}

```

