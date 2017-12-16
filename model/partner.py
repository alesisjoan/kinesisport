# -*- coding: utf-8 -*-

from openerp import fields, models, api
from datetime import datetime
from dateutil.relativedelta import relativedelta


class evolucion(models.Model):
    _name = 'kinesisport.evolucion'
    _order = 'paciente_id desc, fecha desc, create_date desc'

    apto = fields.Selection([('no_apto', 'No apto'), ('apto', 'Apto')], required=True)
    fecha = fields.Date(default=fields.Date.today)
    paciente_id = fields.Many2one('res.partner', default=lambda self: self._context.get('paciente_id'),
                                  domain=[('paciente', '=', True)], string="Paciente", required=True, ondelete='cascade')


class res_partner(models.Model):
    # _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'Partner'

    @api.one
    def get_edad(self):
        if self.fecha_nacimiento:
            fecha_nacimiento = datetime.strptime(
                str(self.fecha_nacimiento),
                '%Y-%m-%d')
            now = datetime.now()
            delta = relativedelta(now, fecha_nacimiento)

            years_months_days = delta.years
            self.edad = str(years_months_days)
            return self.edad

    paciente = fields.Boolean("Paciente", default=False)
    documento = fields.Char(string="Documento")
    tipo_documento = fields.Selection([
        (None, ''),
        ('CI', 'CI'),
        ('DP', 'DP'),
        ('AC', 'AC'),
        ('PAS', 'PAS'),
        ('CE', 'CE'),
        ('DNI', 'DNI'),
        ('DU', 'DU'),
        ('LC', 'LC'),
        ('LE', 'LE'),
        ('RN', 'RN'),
        ('CUIT', 'CUIT'),
        ('CUIL', 'CUIL'),
    ], 'Tipo de Documento', help="Tipo de documento del paciente", default='DNI', sort=True)
    fecha_nacimiento = fields.Date()

    afiliacion_ids = fields.One2many(
        'kinesisport.afiliacion',
        'paciente_id', string="Afiliaciones")

    medico = fields.Boolean(default=False)
    matricula_provincial = fields.Char()

    planes_ofrecidos_ids = fields.One2many(
        'kinesisport.plan', 'institucion_id', string='Planes ofrecidos'
    )

    edad = fields.Char(compute='get_edad', default='')
    sexo = fields.Selection([
        ('', ''),
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino')
    ], string='Género', default='masculino')

    estudios_ids = fields.One2many(
        'kinesisport.estudio',
        'paciente_id', string="Estudios realizados")

    consultas_ids = fields.One2many(
        'kinesisport.consulta',
        'paciente_id', string="Consultas realizadas")

    apto = fields.Selection([('no_apto', 'No apto'), ('apto', 'Apto')], readonly=True)

    realiza_actividades_ids = fields.Many2many('kinesisport.actividad', 'paciente_actividad', 'paciente_id',
                                               'actividad_id',
                                               string="Realiza Actividades")

    realiza_actividades_club_ids = fields.Many2many('kinesisport.actividad.club', 'paciente_actividad_club', 'paciente_id',
                                               'actividad_club_id',
                                               string="Realiza Actividades")

    ofrece_actividades_ids = fields.Many2many('kinesisport.actividad', 'institucion_actividad', 'institucion_id',
                                              'actividad_id',
                                              string="Ofrece Actividades")

    juega_en_ids = fields.Many2many('res.partner', 'jugadores', 'jugador_id', 'club_id',
                                       string="Juega en clubes")

    jugadores_ids = fields.Many2many('res.partner', 'jugadores', 'club_id',
                                       'jugador_id',
                                       string="Tiene jugadores")

    is_institution = fields.Boolean("Es Institucion", default=False)

    is_club = fields.Boolean("Es Club", default=False)

    is_federation = fields.Boolean("Es Federacion", default=False)

    federacion_ids = fields.Many2many('res.partner', 'federacion_club', 'federacion_id', 'club_id',
                                      domain=[('is_federation', '=', 1)])

    club_ids = fields.Many2many('res.partner', 'federacion_club', 'club_id', 'federacion_id',
                                domain=[('is_club', '=', 1)], string="Agrupa clubes")

    evolucion_ids = fields.One2many(
        'kinesisport.evolucion',
        'paciente_id', string="Evoluciones")

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        # if vals.get('paciente_id', 0):
        #     self.env['kinesisport.evolucion'].create({
        #         'apto': vals['apto'],
        #         'paciente_id': vals['paciente_id'],
        #         'fecha': vals['fecha'],
        #     })
        #     self.env['res.partner'].search([('id', '=', vals['paciente_id'])])[0].apto = vals['apto']
        return models.Model.create(self, vals)

    @api.multi
    def write(self, vals):
        if self.paciente and vals.get('realiza_actividades_club_ids', 0):
            # si borra una actividad y solo registra uno, tengo que sacarla
            # si borra un club y solo registra uno, tengo que sacarlo
            # si agrega una actividad y no habia antes, tengo que agregarla
            # si agrega un club y no habia antes, tengo que agregarlo
        # if self.paciente_id and vals.get('apto', 0):
        #     self.env['kinesisport.evolucion'].create({
        #         'apto': vals['apto'],
        #         'paciente_id': self.paciente_id.id,
        #         'fecha': self.fecha or False,
        #     })
        #     self.paciente_id.apto = vals['apto']
        return models.Model.write(self, vals)
        # pacientes = []
        # for paciente in self.paciente_ids:
        #     paciente.juega_en_ids = [(4, self.institucion_id.id)]
        #     paciente.realiza_actividades_ids = [(4, self.actividad.id)]
        #     pacientes.append((4, paciente.id))
        # self.actividad_id.participante_ids = pacientes
        # self.institucion_id.jugadores_ids = pacientes
