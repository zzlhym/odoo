# 获取检验出错原因

### URL

`http://host/api/mrp/failed_reasons?database=<database>&access_token=<access_token>`

##### HTTP 方法:
GET

#####参数详细:

**database**: 当前openerp启动使用的数据名字, 请咨询API开发者。

**access_token**:  用户登陆token， 请咨询API开发者

** 返回 **:

参考一下
**reason** 检验出错原因

``` 
[
    {
    "reason": "出错原因1"
    },
    ...
]

```

