from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import Website
# from odoo.addons.http_routing.models.ir_http import slug
from odoo import http
from odoo.addons.web.controllers.home import Home as WebHome
from odoo.addons.web.controllers.utils import is_user_internal
from odoo.http import request


class ArchLightWebsite(Website):
    @http.route('/', type='http', auth='public', website=True)
    def index(self, **kw):
        """Home Page"""
        company_id = request.env.company
        return request.render('website_arclight_infotech.home_page', {'company_id': company_id})

    @http.route('/about-us', type='http', auth='public', website=True)
    def arclight_about_us(self):
        """Render About Us Page"""
        company_id = request.env.company
        return request.render('website_arclight_infotech.about_us', {'company_id': company_id})

    @http.route('/our-services', type='http', auth='public', website=True)
    def arclight_our_services(self):
        """Render About Us Page"""
        company_id = request.env.company
        return request.render('website_arclight_infotech.our_services', {'company_id': company_id})
