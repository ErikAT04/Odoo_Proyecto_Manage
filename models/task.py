import datetime
from odoo import models, fields, api

class task(models.Model):
    _name = 'manageerik.task'
    _description = 'manageerik.task'

    id = fields.Char()
    name = fields.Char()
    code = fields.Char(compute="_get_code", store = False)
    description = fields.Text()
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    is_paused = fields.Boolean()
    sprint = fields.Many2one("manageerik.sprint", ondelete = "cascade", 
                             string="Sprint", compute = "_get_sprint", store=True)
    technologies = fields.Many2many("manageerik.technology", string="Techs", 
                                    relation = "techs_tasks", 
                                    column1 = "technologies", column2 = "tasks")
    history = fields.Many2one("manageerik.history", required = True, ondelete = "cascade", string="History")
    project = fields.Many2one('manage.project', related='history.project', readonly=True)

    @api.depends('name')
    def _get_code(self):
        for task in self:
            if task.name == False:
                task.code = "TSK_noCode"
            else:
                task.code = f"TSK_{task.name}"

    @api.depends('code')
    def _get_sprint(self):
        for task in self:
            sprints = self.env['manageerik.sprint'].search([('project.id', '=', task.history.project.id)])
            found = False
            for sprint in sprints:
                if isinstance(sprint.end_date, datetime.datetime) and sprint.end_date > datetime.datetime.now():
                    task.sprint = sprint
                    found = True
            if not found:
                task.sprint = False