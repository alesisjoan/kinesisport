# -*- coding: utf-8 -*-

from openerp import fields, models, api
from openerp.exceptions import Warning, ValidationError


class TipoEstudio(models.Model):

    _name = 'kinesisport.tipo_estudio'

    name = fields.Char(required=True)
    codigo = fields.Char()
    estudio_ids = fields.One2many('kinesisport.estudio', 'tipo_estudio_id')


class Estudio(models.Model):

    _name = 'kinesisport.estudio'
    _inherit = 'kinesisport.revisacion'

    tipo_estudio_id = fields.Many2one('kinesisport.tipo_estudio', required=True)

    retirado = fields.Boolean(default=False)
    attachments = fields.One2many('ir.attachment', 'estudio_id', string="Adjuntos")





