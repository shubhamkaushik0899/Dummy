from odoo import fields, models, api


class School(models.Model):
    _name = 'tcb.school'


    name = fields.Many2one('res.partner',string='Name')
    class_id = fields.Integer(string='Class')
    division = fields.Char(string='Division')
