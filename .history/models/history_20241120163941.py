from odoo import models, fields, api


class history(models.Model):
    _name = 'manageerik.history'
    _description = 'manageerik.history'

    name = fields.Char()
    description = fields.Text()
    project = fields.Many2one("manageerik.project", required = True, ondelete = "cascade", 
                             string="Project")
    tasks = fields.One2many(string = "Tasks", comodel_name="manageerik.task", inverse_name="history")
    
def funciones_CRUD():
    modelo2:Modelo1 = self.env['modulo.modelo'].search([('atributo1', '=', 'Hola')])
    modelo2.