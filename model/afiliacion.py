# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import datetime


class Afiliacion(models.Model):
    _name = 'kinesisport.afiliacion'

    name = fields.Char(string="Numero afiliado", required=True)
    #fecha_asociacion = fields.Date(string="Fecha asociacion", default=fields.Date.today())
    #fecha_fin_asociacion = fields.Date(string="Fecha vencimiento", required=True)
    plan_id = fields.Many2one('kinesisport.plan', required=True)
    paciente_id = fields.Many2one(
        'res.partner',
        default=lambda self: self._context.get('paciente_id'),  domain=[('paciente', '=', 1)],required=True, string="Paciente")
    regimen = fields.Selection(
        [('obligatorio', 'Obligatorio'), ('voluntario', 'Voluntario')], 'Régimen')
    active = fields.Boolean(default=True)
    institucion_id = fields.Many2one('res.partner', related='plan_id.institucion_id')
    observaciones = fields.Text()
    fecha = fields.Datetime(default=fields.Datetime.now)

    # verificar quizás si es del hospital español que se indique fecha de asociación

    @api.multi
    def name_get(self):
        return [(afiliacion.id, (afiliacion.institucion_id.name + ' - ' + afiliacion.plan_id.name) + ' - Nro: ' + afiliacion.name) for afiliacion in self]
