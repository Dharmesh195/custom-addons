# -*- coding: utf-8 -*-
{
    "name": "Archlight Infotech",
    "summary": "Archlight Infotech Website",
    "version": "18.0.2.0.0",
    'author' : "Arclight Infotech",
    "category": "Theme",
    "license": "LGPL-3",
    "depends": ["website", "web"],
    "data": [
        # Security
        'security/ir.model.access.csv',
        # Views
        'views/website_menu.xml',
        'views/res_company_website_inherit_view.xml',
        # Template
        'views/templates/web_header.xml',
        'views/templates/web_footer.xml',
        'views/templates/home_page.xml',
        'views/templates/about_us_page.xml',
        'views/templates/dynamic_pages.xml',
        'views/templates/login_page.xml',
        'views/templates/contact_us_inherit_view.xml',
    ],
    "assets": {
        "web.assets_frontend": [
            'website_arclight_infotech/static/src/css/animate.css',
            'website_arclight_infotech/static/src/js/lib/owlcarousel/assets/owl.carousel.min.css',
            'website_arclight_infotech/static/src/css/style.css',
            # Lib JS
            'website_arclight_infotech/static/src/js/lib/waypoints/waypoints.min.js',
            'website_arclight_infotech/static/src/js/lib/owlcarousel/owl.carousel.min.js',
            'website_arclight_infotech/static/src/js/lib/counterup/counterup.min.js',
            # Main JS
            'website_arclight_infotech/static/src/js/main.js',
        ],
    },
    "installable": True,
    "application": False,
}

