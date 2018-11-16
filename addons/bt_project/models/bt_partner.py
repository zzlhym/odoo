# -*- coding: utf-8 -*-

from openerp import models, fields, api, osv
from datetime import datetime
import openerp.addons.decimal_precision as dp
from openerp.addons.stock import stock


class BtPartner(models.Model):
    _name = 'bt.partner'
    _description = "bt partner"

    name = fields.Char("部门名称")
    no = fields.Char("部门编号")
    duty = fields.Char("职位")
    user_id = fields.Many2one('bt.user', string="员工")
    _defaults = {

    }











