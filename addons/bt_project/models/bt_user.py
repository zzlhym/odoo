# -*- coding: utf-8 -*-

from openerp import models, fields, api, osv
from datetime import datetime
import openerp.addons.decimal_precision as dp
from openerp.addons.stock import stock


class BtUser(models.Model):
    _name = 'bt.user'
    _description = "bt user"

    name = fields.Char("姓名")
    partner = fields.One2many('bt.partner', 'user_id', "所属部门")
    type = fields.Selection([('pm', 'PM'), ('pmo', 'PMO'), ('pd', 'PD')], string="职位")
    project = fields.One2many('bt.project', 'user_id')
    _defaults = {

    }











