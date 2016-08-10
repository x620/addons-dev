# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp import SUPERUSER_ID


class mail_compose_message(models.TransientModel):
    _inherit = 'mail.compose.message'

    private = fields.Boolean('Send Internal Message')


class mail_thread(models.Model):
    _inherit = 'mail.thread'

    def message_get_suggested_private_recipients(self, cr, uid, ids, context=None):
        result = dict((res_id, []) for res_id in ids)
        current_partner = self.pool.get('res.users').browse(cr, uid, uid, context=context).partner_id
        if 'message_follower_ids' in self._fields:
            for obj in self.browse(cr, SUPERUSER_ID, ids, context=context):
                for fol_obj in obj.message_follower_ids:
                    if current_partner != fol_obj:
                        result[obj.id].append((fol_obj.id, '%s<%s>' % (fol_obj.name, fol_obj.email)))
        return result


    @api.cr_uid_ids_context
    def message_post(self, cr, uid, thread_id, body='', subject=None, type='notification',
                     subtype=None, parent_id=False, attachments=None, context=None,
                     content_subtype='html', **kwargs):
        msg_id = super(mail_thread, self).message_post(cr, uid, thread_id, body, subject, type, subtype, parent_id, attachments, context, content_subtype, **kwargs)
        if context.get('default_private'):
            message = self.pool.get('mail.message').browse(cr, uid, msg_id, context=context)
            message.notified_partner_ids = message.partner_ids
        return msg_id
