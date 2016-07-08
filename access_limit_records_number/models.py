# -*- coding: utf-8 -*-

from openerp import models, fields, api, SUPERUSER_ID


class BaseLimitRecordsNumber(models.Model):
    _name = 'base.limit.records_number'

    model_id = fields.Many2one('ir.model', 'Model', required=True)
    max_records = fields.Integer(string='Maximum Records')
    domain = fields.Char(string='Domain')
