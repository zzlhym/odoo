# -*- coding: utf-8 -*-

from openerp import models, fields, api, osv
from datetime import datetime
import openerp.addons.decimal_precision as dp
from openerp.addons.stock import stock



class BtWorkHours(models.Model):
    _name = 'bt.work.hours'
    _description = "bt work hours"

    plan_hours = fields.Float("计划工时")
    actual_hours = fields.Float("实际工时")
    task = fields.Char("任务")
    task_log = fields.Text("任务日志")
    done_rate = fields.Char("完成度", compute='_compute_rate')

    def _compute_rate(self):
        if self.plan_hours == 0:
            self.done_rate = '0%'
        else:
            rate = self.actual_hours/self.plan_hours
            self.done_rate = str(rate*100) + '%'
    _defaults = {
        'done_rate': '0%',
    }











