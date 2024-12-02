from odoo import models, fields, api
import datetime

class sprint(models.Model):
    _name = 'manageerik.sprint'
    _description = 'manageerik.sprint'

    id = fields.Char()
    name = fields.Char()
    description = fields.Text()
    start_date = fields.Datetime()
    duration = fields.Integer()
    end_date = fields.Datetime(compute="_get_end_date", store=True)
    tasks = fields.One2many(string="tasks", comodel_name="manageerik.task", inverse_name="sprint")
    project = fields.Many2one("manageerik.project", string="project", required = False, ondelete = "cascade")

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for sprint in self:
            if isinstance(sprint.start_date, datetime.datetime) and sprint.duration > 0:
                sprint.end_date = sprint.start_date + datetime.timedelta(days=sprint.duration)
            else:
                sprint.end_date = sprint.start_date