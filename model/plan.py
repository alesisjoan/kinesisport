# -*- coding: utf-8 -*-

from openerp import models, fields


class Plan(models.Model):
    _name = 'kinesisport.plan'

    name = fields.Char('Plan', required=True)
    descripcion = fields.Text()
    afiliacion_ids = fields.One2many('kinesisport.afiliacion', 'plan_id')
    institucion_id = fields.Many2one('res.partner', domain=[('is_institution', '=', True)], string='Institución oferente', required=True)

    regimen = fields.Selection([
        ('OS', 'Obligatorio'),
        ('PR', 'Voluntario'), ], string='Régimen')

    estado = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Habilitado'), ], default='1', string='Estado')

    observaciones = fields.Text(help='Condiciones especiales, observaciones, notas, etc.')