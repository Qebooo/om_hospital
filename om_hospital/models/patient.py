from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name="hospital.patient"
    _description="Hospital Patient"

    name=fields.Char(string="Name")
    name=fields.Integer(string="Age")
    name=fields.Selection([("male", "Male"), ("female", "Female")], string="gender")