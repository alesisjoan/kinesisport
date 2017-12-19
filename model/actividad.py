# -*- coding: utf-8 -*-

from openerp import fields, models, api
from openerp.exceptions import Warning, ValidationError


class Actividad(models.Model):
    _name = 'kinesisport.actividad'

    name = fields.Char(required=True)

    # institucion_ids = fields.One2many('res.partner', 'ofrece_actividades_ids', string="Instituciones que la ofrecen")
    # paciente_ids = fields.One2many('res.partner', 'realiza_actividades_ids', string="Pacientes que la realizan")

    # participante_ids = fields.Many2many('res.partner', 'paciente_actividad', 'actividad_id', 'paciente_id',
    #                                     domain=[('paciente', '=', True)], string="Participan")
    #
    # institucion_ids = fields.Many2many('res.partner', 'institucion_actividad', 'actividad_id', 'institucion_id',
    #                                    domain=[('&'), ('is_institution', '=', True), ('is_club', '=', True)],
    #                                    string="Se realiza en", required=True)


class ActividadClub(models.Model):
    _name = 'kinesisport.actividad.club'

    _sql_constraints = [('institucion_actividad_unique','UNIQUE(institucion_id, actividad_id)',
                         'Ya existe la actividad con esa institucion.')]


    @api.onchange('actividad_id')
    def onchange_actividad(self):
        self.institucion_id = False
        if self.actividad_id:
            res = {}
            institucion_ids = [i.name for i in self.actividad_id.institucion_ids]
            res['domain'] = {'institucion_id': [('name', 'in', institucion_ids)]}
            return res

    institucion_id = fields.Many2one('res.partner',
                                     domain=[('&'), ('is_institution', '=', True), ('is_club', '=', True)],
                                     string="Se realiza en", required=True)

    actividad_id = fields.Many2one('kinesisport.actividad', string="Actividad", required=True)

    paciente_ids = fields.Many2many('res.partner', 'paciente_actividad_club', 'actividad_club_id', 'paciente_id',
                                    domain=[('paciente', '=', True)], string="Jugador")

    name = fields.Char(compute='onchange_actividad', string="Nombre", store=True)

    @api.one
    @api.depends('actividad_id', 'institucion_id')
    def onchange_actividad(self):
        if self.actividad_id and self.institucion_id:
            # TODO buscar si las actividades son compatibles
            #if self.actividad_id.id not in self.institucion_id.ofrece_actividades_ids.ids:
            #raise Warning("La actividad no se encuentra registrada en la institucion")
            self.name = self.actividad_id.name + ' @ ' + self.institucion_id.name



