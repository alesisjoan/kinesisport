# -*- coding: utf-8 -*-

from openerp import fields, models, api
from openerp.exceptions import Warning, ValidationError


class Actividad(models.Model):

    _name = 'kinesisport.actividad'

    name = fields.Char(required=True)
    participan_ids = fields.Many2many('res.partner', 'paciente_actividad', 'actividad_id', 'partner_id')