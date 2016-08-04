# -*- coding: utf-8 -*-
from openerp import models, fields, api


class PosConfig(models.Model):
    _inherit = 'pos.config'

    @api.model
    def _discount_total_user(self):
        return self.env.ref('point_of_sale.group_pos_manager')

    discount_total_group_id = fields.Many2one(
        'res.groups', string='Total Discount Group', default=_discount_total_user,
        help='Group allows to set total discount for POS Orders.')
