 # -*- coding: utf-8 -*-
{
    'name': "ProximaNova Font",

    'summary': """
        ProximaNova Font""",

    'description': """
        Change the default english font of the all interfaces with a beautiful one preferred by the english user
 ,
    """,
    'author': "DXB CODER",
    'website': "http://dxbcoder.com",
    'category': '',
    'version': '1.0.0',
    'depends': ['web'],
    'qweb': [],

    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'auto_install': True,
    'installable': True,
    'assets': {
        'web.assets_common': [
            'proxima_nova_font/static/src/scss/proxima.scss',
            'proxima_nova_font/static/css/web_style.css',
        ],
    },
}