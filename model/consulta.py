# -*- coding: utf-8 -*-

from openerp import fields, models, api
from openerp.exceptions import Warning, ValidationError


class Consulta(models.Model):

    _name = 'kinesisport.consulta'

    fecha = fields.Date(default=fields.Date.today)
    paciente_id = fields.Many2one('res.partner', domain=[('paciente', '=', True)], default=lambda self: self._context.get('paciente_id'), string="Paciente", required=True)
    efector_id = fields.Many2one('res.partner', domain=[('medico', '=', True)], string="Efector")
    informe = fields.Text(string='Informe')
    solicitante_id = fields.Many2one('res.partner', domain=[('is_institution', '=', True)], string="Solicitado por")

    afiliacion_id = fields.Many2one('kinesisport.afiliacion', string="Afiliacion",)
    plan_id = fields.Many2one('kinesisport.plan', string="Plan", related='afiliacion_id.plan_id')

    adjunto_ids = fields.One2many('kinesisport.adjunto', 'consulta_id')


