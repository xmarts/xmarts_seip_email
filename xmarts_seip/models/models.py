# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class xmarts_seip(models.Model):
    _inherit = 'oeh.medical.lab.test'

    def action_sent(self):
    	
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        template = self.env.ref('xmarts_seip.email_estudio', False)
        
        try:
            compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False
        ctx = dict(self.env.context or {})
        ctx.update({
            'default_model': 'oeh.medical.lab.test',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template),
            'default_template_id': template and template.id or False,
            'default_composition_mode': 'comment',
            'custom_layout': "mail.mail_notification_paynow",
            'force_email': True,
            'mark_rfq_as_sent': True,
        })


        return {
            'name': _('Compose Email'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
        }

        