{
    'name': 'TCB School Module',
    'version': '1.0.1',
    'summary': 'School Module for students',
    'description': 'We are looking for students in the TCB University',
    'category': 'Uncategorized',
    'author': 'TCB University',
    'website': 'www.tcb.org',
    'depends': ['base', 'contacts', 'hr', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/school.xml'
    ],
    'installable': True,
    'auto_install': False
}
