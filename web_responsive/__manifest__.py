# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Web Responsive',
    'category': 'Hidden',
    'version': '1.0',
    'description':
        """
Odoo Responsive Web Client.
===========================

This module modifies the web addon to provide responsiveness.
        """,
    'depends': ['web'],
    'auto_install': False,
    'data': [
        'views/webclient_templates.xml',
    ],
    'qweb': [
        "static/src/xml/*.xml",
    ],
}
