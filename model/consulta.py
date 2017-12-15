# -*- coding: utf-8 -*-

from openerp import fields, models, api
from openerp.exceptions import Warning, ValidationError


class Archivo(models.Model):
    _inherit = 'ir.attachment'
    consulta_id = fields.Many2one('kinesisport.consulta', default=lambda self: self._context.get('consulta_id'))
    estudio_id = fields.Many2one('kinesisport.estudio', default=lambda self: self._context.get('estudio_id'))


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
    attachments = fields.One2many('ir.attachment', 'consulta_id', string="Adjuntos")


