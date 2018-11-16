# -*- coding: utf-8 -*-

from openerp import models, fields, api, osv
from datetime import datetime
import openerp.addons.decimal_precision as dp
from openerp.addons.stock import stock


class BtTask(models.Model):
    _name = 'bt.task'
    _description = "bt task"

    no = fields.Char("任务编号")
    name = fields.Char("任务名称")
    plan_start_time = fields.Datetime("计划开始时间")
    plan_end_time = fields.Datetime("计划结束时间")
    plan_work_hours = fields.Float("计划工时", compute='_compute_plan_hours')
    actual_work_hours = fields.Float("实际工时")
    done_rate = fields.Char("完成度", compute='_compute_rate')
    state = fields.Selection([('undo', '未开始'), ('doing', '进行中'), ('done', '已完成')], string="状态", compute='_compute_state')

# todo 要循环list来计算，不能self; 有计算得，先完善代码，再新建，不然会报错

    @api.multi
    def _compute_plan_hours(self):
        #todo xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        for record in self:
            if record.plan_start_time is None or record.plan_end_time is None:
                record.plan_work_hours = 0
            else:
                record.plan_work_hours = 10

    @api.multi
    def _compute_rate(self):
        for record in self:
            if record.plan_work_hours == 0:
                record.done_rate = '0.0%'
            else:
                rate = record.actual_work_hours/record.plan_work_hours
                record.done_rate = str(rate*100) + '%'

    @api.multi
    def _compute_state(self):
        for record in self:
            if record.done_rate == '0.0%' or record.done_rate is None:
                record.state = 'undo'
            elif record.done_rate != '0.0%' and record.done_rate != '100.0%' and record.done_rate is not None:
                record.state = 'doing'
            else:
                record.state = 'done'
    _defaults = {

    }











