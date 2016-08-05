# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class mail_compose_message(models.TransientModel):
#     _inherit = 'mail.compose.message'


class res_partner(models.Model):
    _inherit = 'res.partner'

    to_send = fields.Boolean(compute="_to_send", store=True)

    @api.one
    def _to_send(self):
        self.to_send = False
        # TODO: Если пользователь среди подписантов, то True
        pass

