
# 获取某个用户的信息

### URL

`http://host/api/base/users/<access_token>?database=<database>`

##### HTTP 方法:
GET

#####参数详细:

**database**: 当前openerp启动使用的数据名字, 请咨询API开发者。

**access_token**:  用户登陆token， 请咨询API开发者


** 返回 **:

参考一下



``` json
{
    "id": 1,
    "name": "Administrator"
}
```

