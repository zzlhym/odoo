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
    tasks = fields.One2many('bt.task', 'project_id', '所有任务')

    p1 = fields.One2many('bt.project', 'p1_id')
    p1_id = fields.Many2one('bt.project')

    task_id = fields.Many2many('bt.task')

    file = fields.Binary('附件')


    _defaults = {

    }













