from odoo import http
from odoo.http import request


class DynamicServiceController(http.Controller):

    @http.route('/services/<path:subroute>', type='http', auth='public', website=True)
    def render_dynamic_page(self, subroute, **kwargs):
        full_route = f'/services/{subroute}'.rstrip('/')
        service = request.env['custom.service.menu'].sudo().search(
            [('route', '=', full_route)], limit=1
        )
        company_id = request.env.company
        return request.render('website_arclight_infotech.dynamic_service_template', {
            'service': service,
            'company_id': company_id
        })
