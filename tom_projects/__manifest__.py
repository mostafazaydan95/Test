# -*- coding: utf-8 -*-
{
    'name': "Tom Projects",
    'description': """Organize and plan tom projects""",

    'author': "Mostafa Zaydan",
    'category': 'Project',
    'version': '0.1',
    'depends': ['project', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/project_project.xml',
        'views/tree_configurator.xml',
    ],
}
