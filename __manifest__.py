{
    'name': 'Precio Anterior',
    'version': '1.0',
    'summary': 'Track previous supplier prices',
    'description': 'This module adds a field to track previous supplier prices',
    'category': 'Sales',
    'author': 'Nakel',
    'depends': ['product'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}