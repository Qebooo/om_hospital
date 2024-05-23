{
    
    'name': 'Hospital Management',
    'version': '1.0.0',
    'Category': 'Hospital', 
    "author": "Odoo Mates",
    'sequence': - 100,
    'summary': 'Hospital management system',
    'description': """Hospital management system""",
    "depends": [],
    'data':  [
         "security/ir.model.access.csv",
         "views/menu.xml",
         "views/patient_view.xml",
    ],
    'demo' :[],
    'application': True,
    'auto install': False,
    'license': "LGPL-3",
}