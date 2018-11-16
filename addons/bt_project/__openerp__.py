# -*- coding: utf-8 -*-
{
    'name': "bt_project",

    'summary': """
        Warehouse Management for MJ
    """,

    'description': """
        Warehouse Management for MJ
    """,

    'author': "MJ",
    'website': "http://www.shmingjiang.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'miangjiang',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'auth_token'],

    # always loaded
    'data': [
        'views/bt_project.xml',
        'views/bt_partner.xml',
        'views/bt_user.xml',
        'security/security.xml',
        'security/ir.model.access.csv',

    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}