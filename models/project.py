from odoo import models, fields, api


class project(models.Model):
    _name = 'manageerik.project'
    _description = 'manageerik.project'

    id = fields.Char()
    name = fields.Char()
    description = fields.Text()
    histories = fields.One2many(string="Histories", comodel_name="manageerik.history", inverse_name="project")
    sprints = fields.One2many(string="Sprints", comodel_name="manageerik.sprint", inverse_name="project")


