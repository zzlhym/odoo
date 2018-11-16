# 获取所有批次

### URL

`http://host/api/iqc/batches?database=<database>&access_token=<access_token>&state=<state>&offset=<offset>&limit=<limit>`

##### HTTP 方法:
GET

#####参数详细:

**database**: 当前openerp启动使用的数据名字, 请咨询API开发者。

**access_token**:  用户登陆token， 请咨询API开发者

**state**: 状态，可取：draft,packaging,packaged,inspected
分别对应 初始状态，分拣中，分拣完成，检测完成

**offset**: 偏移多少

**limit**: 限制取多少

** 返回 **:

参考一下



``` 

[
    {
        "inspection_quantity": 1,
        "order_no": "1",
        "pos": "1",
        "arrival_date_str": "20121011",
        "part": {
            "remark": "Remark....",
            "image_medium": "/api/iqc/part_images/1?size=medium",
            "name": "name 1",
            "rules": [
                {
                    "tool": "tool",
                    "standard": 11,
                    "down": 10,
                    "step": 1,
                    "part_id": 1,
                    "id": 1,
                    "name": "name 1",
                    "coord_y": 21,
                    "coord_x": 11,
                    "up": 15,
                    "type": "quantitative"
                },
                {
                    "tool": "tool",
                    "standard": 1,
                    "down": 11,
                    "step": 2,
                    "part_id": 1,
                    "id": 2,
                    "name": "name 1",
                    "coord_y": 21,
                    "coord_x": 11,
                    "up": 15,
                    "type": "quantitative"
                },
                {
                    "tool": "tool",
                    "standard": 11,
                    "down": 10,
                    "step": 3,
                    "part_id": 1,
                    "id": 3,
                    "name": "name 1",
                    "coord_y": 21,
                    "coord_x": 11,
                    "up": 15,
                    "type": "quantitative"
                }
            ],
            "image": "/api/iqc/part_images/1?size=big",
            "unit_en": "package",
            "image_small": "/api/iqc/part_images/1?size=small",
            "machine": "machine name",
            "instruction": {
                "name": "name 1",
                "file": null
            },
            "c3": "c3",
            "c2": "c2",
            "name_en": "name en 1",
            "c1": "c1",
            "id": 1,
            "unit": "package",
            "c4": "c4"
        },
        "id": 1,
        "work_no": 1,
        "ok_quantity": 1,
        "state": "packaged",
        "ng_quantity": 1,
        "supplier": {
            "name": "name 1",
            "no": "123456"
        },
        "is_urgent": false,
        "inspection_datetime": false,
        "quantity": 1
    },
    {
        "inspection_quantity": 1,
        "order_no": "1",
        "pos": "1",
        "arrival_date_str": "20121011",
        "part": {
            "remark": "Remark....",
            "image_medium": "/api/iqc/part_images/1?size=medium",
            "name": "name 1",
            "rules": [
                {
                    "tool": "tool",
                    "standard": 11,
                    "down": 10,
                    "step": 1,
                    "part_id": 1,
                    "id": 1,
                    "name": "name 1",
                    "coord_y": 21,
                    "coord_x": 11,
                    "up": 15,
                    "type": "quantitative"
                },
                {
                    "tool": "tool",
                    "standard": 1,
                    "down": 11,
                    "step": 2,
                    "part_id": 1,
                    "id": 2,
                    "name": "name 1",
                    "coord_y": 21,
                    "coord_x": 11,
                    "up": 15,
                    "type": "quantitative"
                },
                {
                    "tool": "tool",
                    "standard": 11,
                    "down": 10,
                    "step": 3,
                    "part_id": 1,
                    "id": 3,
                    "name": "name 1",
                    "coord_y": 21,
                    "coord_x": 11,
                    "up": 15,
                    "type": "quantitative"
                }
            ],
            "image": "/api/iqc/part_images/1?size=big",
            "unit_en": "package",
            "image_small": "/api/iqc/part_images/1?size=small",
            "machine": "machine name",
            "instruction": {
                "name": "name 1",
                "file": null
            },
            "c3": "c3",
            "c2": "c2",
            "name_en": "name en 1",
            "c1": "c1",
            "id": 1,
            "unit": "package",
            "c4": "c4"
        },
        "id": 2,
        "work_no": 1,
        "ok_quantity": 1,
        "state": "packaged",
        "ng_quantity": 1,
        "supplier": {
            "name": "name 1",
            "no": "123456"
        },
        "is_urgent": false,
        "inspection_datetime": false,
        "quantity": 1
    },
    {
        "inspection_quantity": 1,
        "order_no": "1",
        "pos": "1",
        "arrival_date_str": "20121011",
        "part": {
            "remark": "Remark....",
            "image_medium": "/api/iqc/part_images/1?size=medium",
            "name": "name 1",
            "rules": [
                {
                    "tool": "tool",
                    "standard": 11,
                    "down": 10,
                    "step": 1,
                    "part_id": 1,
                    "id": 1,
                    "name": "name 1",
                    "coord_y": 21,
                    "coord_x": 11,
                    "up": 15,
                    "type": "quantitative"
                },
                {
                    "tool": "tool",
                    "standard": 1,
                    "down": 11,
                    "step": 2,
                    "part_id": 1,
                    "id": 2,
                    "name": "name 1",
                    "coord_y": 21,
                    "coord_x": 11,
                    "up": 15,
                    "type": "quantitative"
                },
                {
                    "tool": "tool",
                    "standard": 11,
                    "down": 10,
                    "step": 3,
                    "part_id": 1,
                    "id": 3,
                    "name": "name 1",
                    "coord_y": 21,
                    "coord_x": 11,
                    "up": 15,
                    "type": "quantitative"
                }
            ],
            "image": "/api/iqc/part_images/1?size=big",
            "unit_en": "package",
            "image_small": "/api/iqc/part_images/1?size=small",
            "machine": "machine name",
            "instruction": {
                "name": "name 1",
                "file": null
            },
            "c3": "c3",
            "c2": "c2",
            "name_en": "name en 1",
            "c1": "c1",
            "id": 1,
            "unit": "package",
            "c4": "c4"
        },
        "id": 3,
        "work_no": 1,
        "ok_quantity": 1,
        "state": "packaged",
        "ng_quantity": 1,
        "supplier": {
            "name": "name 1",
            "no": "123456"
        },
        "is_urgent": false,
        "inspection_datetime": false,
        "quantity": 1
    }
]

```

