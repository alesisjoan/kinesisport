# -*- coding: utf-8 -*-

from openerp import fields, models, api
from openerp.exceptions import Warning, ValidationError


class Archivo(models.Model):
    _inherit = 'ir.attachment'
    _name = 'ir.attachment'

    # consulta_id = fields.Many2one('kinesisport.consulta', default=lambda self: self._context.get('consulta_id'))
    consulta_id = fields.Many2one('kinesisport.consulta', )
    # estudio_id = fields.Many2one('kinesisport.estudio', default=lambda self: self._context.get('estudio_id'))
    estudio_id = fields.Many2one('kinesisport.estudio', )


class Consulta(models.Model):
    _name = 'kinesisport.consulta'

    fecha = fields.Date(default=fields.Date.today)
    paciente_id = fields.Many2one('res.partner', domain=[('paciente', '=', True)],
                                  default=lambda self: self._context.get('paciente_id'), string="Paciente",
                                  required=True)
    efector_id = fields.Many2one('res.partner', domain=[('medico', '=', True)], string="Efector")
    informe = fields.Text(string='Informe')
    solicitante_id = fields.Many2one('res.partner',
                                     domain=[('|'), ('is_institution', '=', True), ('medico', '=', True)],
                                     string="Solicitado por")

    afiliacion_id = fields.Many2one('kinesisport.afiliacion', string="Afiliacion", )
    plan_id = fields.Many2one('kinesisport.plan', string="Plan", related='afiliacion_id.plan_id')

    attachments = fields.One2many('ir.attachment', 'consulta_id', string="Adjuntos")
    apto = fields.Selection([('no_apto', 'No apto'), ('apto', 'Apto')])

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        if vals.get('paciente_id',0):
            self.env['kinesisport.evolucion'].create({
                'apto': vals['apto'],
                'paciente_id': vals['paciente_id'],
                'fecha': vals['fecha'],
            })
            self.env['res.partner'].search([('id', '=', vals['paciente_id'])])[0].apto = vals['apto']
        return models.Model.create(self, vals)

    @api.multi
    def write(self, vals):
        if self.paciente_id and vals.get('apto', 0):
            self.env['kinesisport.evolucion'].create({
                'apto': vals['apto'],
                'paciente_id': self.paciente_id.id,
                'fecha': self.fecha or False,
            })
            self.paciente_id.apto = vals['apto']
        return models.Model.write(self, vals)

