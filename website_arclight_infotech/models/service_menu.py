from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ServiceSection(models.Model):
    """Service Section"""
    _name = "service.section"
    _description = __doc__

    title = fields.Char()
    service_menu_ids = fields.One2many('custom.service.menu', 'service_section_id')
    company_id = fields.Many2one('res.company')


class CustomServiceMenu(models.Model):
    _name = 'custom.service.menu'
    _description = 'Dynamic Service Menu Configuration'

    name = fields.Char('Menu Name', required=True)
    route = fields.Char('Route Link', compute="_compute_route_link",store=True)
    is_published = fields.Boolean('Published', default=True)
    section_id = fields.Many2one('service.section')
    service_section_id = fields.Many2one('service.section')
    content = fields.Html()
    main_image = fields.Image()


    @api.depends('name')
    def _compute_route_link(self):
        for rec in self:
            route= None
            if rec.name:
                link = rec.name.strip().replace(' ', '-').lower()
                route = f"/services/{link}"
            rec.route = route