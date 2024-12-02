from odoo import models, fields, api


class technology(models.Model):
    _name = 'manageerik.technology'
    _description = 'manageerik.technology'

    id = fields.Char()
    name = fields.Char()
    description = fields.Text()
    photo = fields.Image()
    tasks = fields.Many2many("manageerik.task", string="Tasks", relation = "techs_tasks", 
                             column1 = "tasks", column2 = "technologies")

