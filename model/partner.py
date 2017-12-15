# -*- coding: utf-8 -*-

from openerp import fields, models, api
from datetime import datetime
from dateutil.relativedelta import relativedelta


class evolucion(models.Model):
    _name = 'kinesisport.evolucion'
    _order = 'paciente_id desc, fecha desc, create_date desc'

    apto = fields.Boolean()
    fecha = fields.Date(default=fields.Date.today)
    paciente_id = fields.Many2one('res.partner', default=lambda self: self._context.get('paciente_id'),
                                  domain=[('paciente', '=', True)], string="Paciente", required=True)

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        paciente_id = self.env['res.partner'].search([('id', '=', vals['paciente_id'])])[0]
        if paciente_id:
            paciente_id.apto = vals.get('apto', 0)
        return models.Model.create(self, vals)


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
        'paciente_id')

    medico = fields.Boolean(default=False)

    planes_ofrecidos_ids = fields.One2many(
        'kinesisport.plan', 'institucion_id', string='Planes ofrecidos'
    )

    edad = fields.Char(compute='get_edad', default='')
    sexo = fields.Selection([
        ('', ''),
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino')
    ], string='Género')

    estudios_ids = fields.One2many(
        'kinesisport.estudio',
        'paciente_id')

    consultas_ids = fields.One2many(
        'kinesisport.consulta',
        'paciente_id')

    apto = fields.Boolean(readonly=True)

    actividades_ids = fields.Many2many('kinesisport.actividad', 'paciente_actividad', 'partner_id', 'actividad_id',
                                       string="Actividades")

    is_institution = fields.Boolean("Es Institucion", default=False)

    evolucion_ids = fields.One2many(
        'kinesisport.evolucion',
        'paciente_id')
