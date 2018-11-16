# -*- coding: utf-8 -*-

from openerp import models, fields, api, osv
from datetime import datetime
import openerp.addons.decimal_precision as dp
from openerp.addons.stock import stock


class BtProject(models.Model):
    _name = 'bt.project'
    _description = "bt project"

    name = fields.Char("项目名称")
    no = fields.Char("项目编号")
    date = fields.Date("项目日期")
    user_id = fields.Many2one('bt.user', "负责人")
    pmo = fields.Char("PMO")
    note = fields.Text("备注")


    _defaults = {

    }











