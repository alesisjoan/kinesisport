# -*- coding: utf-8 -*-

from openerp import fields, models, api
from openerp.exceptions import Warning, ValidationError


class Adjunto(models.Model):
    _name = 'kinesisport.adjunto'

    estudio_id = fields.Many2one('kinesisport.estudio','Estudio')
    consulta_id = fields.Many2one('kinesisport.consulta','Consulta')

    file = fields.Binary(string="Archivo", required=True)
    filename = fields.Char(string="Nombre de Archivo")
    name = fields.Char(string="Nombre de Archivo", related='filename')
    descripcion = fields.Char(string='Comentarios',)


class TipoEstudio(models.Model):

    _name = 'kinesisport.tipo_estudio'

    name = fields.Char(required=True)
    codigo = fields.Char()
    estudio_ids = fields.One2many('kinesisport.estudio', 'tipo_estudio_id')


class Estudio(models.Model):

    _name = 'kinesisport.estudio'
    _inherit = 'kinesisport.consulta'

    tipo_estudio_id = fields.Many2one('kinesisport.tipo_estudio', required=True)
    adjunto_ids = fields.One2many('kinesisport.adjunto', 'estudio_id')





