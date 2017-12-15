{
    'name': "Kinesisport",

    'summary': """
        Módulo Odoo para Kinesisport""",
    'sequence': 1,

    'description': """
EN DESARROLLO
    """,

    'author': "Alesis Manzano",
    'website': "https://github.com/alesisjoan",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/consulta.xml',
        'views/efectores.xml',
        # 'views/estudios.xml',
        'views/instituciones.xml',
        'views/pacientes.xml',
        'views/plan.xml',
        'views/tipo_estudio.xml',
        'views/menu_principal.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo.xml',
    ],
    'installable': True,
    'application': True,
}
# -*- coding: utf-8 -*-
