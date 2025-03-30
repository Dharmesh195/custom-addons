from odoo import fields, api, models


class ArchResCompany(models.Model):
    _inherit = "res.company"

    # HOME PAGE START-----------------------------------------
    # Home Page
    main_cover_image = fields.Image()
    is_font_match_logo = fields.Boolean("Font Match With logo ?")
    is_add_img_to_header = fields.Boolean(string="Add Image to Header")
    main_title = fields.Text(string="Main Title")
    main_sub_title = fields.Text(string="Main Sub Title")

    # 4 Point
    point_1_icon = fields.Char()
    point_1_title = fields.Char()
    point_1_desc = fields.Html()
    point_2_icon = fields.Char()
    point_2_title = fields.Char()
    point_2_desc = fields.Html()
    point_3_icon = fields.Char()
    point_3_title = fields.Char()
    point_3_desc = fields.Html()
    point_4_icon = fields.Char()
    point_4_title = fields.Char()
    point_4_desc = fields.Html()

    # Fact Section
    fact_title = fields.Char(string="Fact Title")
    fact_desc = fields.Html(string="Fact Description")
    fact_point_1 = fields.Char(string="Fact Highlight 1")
    fact_point_1_desc = fields.Html(string="Fact Highlight 1 Description")
    fact_point_2 = fields.Char(string="Fact Highlight 2")
    fact_point_2_desc = fields.Html(string="Fact Highlight 2 Description")
    fact_point_3 = fields.Char(string="Fact Highlight 3")
    fact_point_3_desc = fields.Html(string="Fact Highlight 3 Description")
    fact_point_4 = fields.Char(string="Fact Highlight 4")
    fact_point_4_desc = fields.Html(string="Fact Highlight 4 Description")
    fact_bg_image = fields.Image(string="Fact Image")

    # Testimonials
    testimonial_title = fields.Char(string="Testimonial Main Title")
    testimonials_ids = fields.One2many(
        comodel_name="arc.testimonials",
        inverse_name="company_id"
    )

    # Technologies
    technologies_title = fields.Char(string="Technologies Main Title")
    technologies_ids = fields.One2many(
        comodel_name="arc.technologies",
        inverse_name="company_id"
    )

    # D Start
    # Frequently Asked Questions
    question_ids = fields.One2many(
        comodel_name='arch.frequent.que',
        inverse_name='company_id'
    )
    q_and_a_section_title = fields.Char(string="FAQ Title")
    # D End

    # HOME PAGE END-----------------------------------------

    # ABOUT US START -----------------------------------------
    # _________Section 1_________
    about_main_title = fields.Char()
    about_desc = fields.Text()
    about_img = fields.Image()
    banner1_image = fields.Image()
    banner1_title = fields.Char()
    banner2_image = fields.Image()
    banner2_title = fields.Char()
    banner3_image = fields.Image()
    banner3_title = fields.Char()
    banner4_image = fields.Image()
    banner4_title = fields.Char()

    # __________Section 2_______
    count_fact_title = fields.Char()
    count_fact_desc = fields.Text()
    count_fact_bg = fields.Image(string="Fact Background Image")
    achievement_title = fields.Char()
    achievement_desc = fields.Text()
    achievement_bg = fields.Image(string="Achievement Background Image")
    achievement_count_1 = fields.Char()
    achievement_title_1 = fields.Char()
    achievement_image_1 = fields.Image()
    achievement_count_2 = fields.Char()
    achievement_title_2 = fields.Char()
    achievement_image_2 = fields.Image()
    achievement_count_3 = fields.Char()
    achievement_title_3 = fields.Char()
    achievement_image_3 = fields.Image()
    achievement_count_4 = fields.Char()
    achievement_title_4 = fields.Char()
    achievement_image_4 = fields.Image()

    # ---------Team Section-------------
    show_team = fields.Boolean()
    team_member_ids = fields.One2many('arc.team', 'company_id')
    # ABOUT US END -----------------------------------------

    # SERVICES START --------------------------------------
    arc_partners_title = fields.Char(string="Partner Section Title")
    arc_partner_ids = fields.One2many(
        comodel_name="arc.partners",
        inverse_name="company_id"
    )
    service_title = fields.Char(string="Service Title")
    is_icon_bg = fields.Boolean(string="Is Icon Background")
    icon_bg = fields.Char(string="Icon Background Color")
    arc_service_ids = fields.One2many(
        comodel_name="arc.services",
        inverse_name="company_id"
    )
    # SERVICES END --------------------------------------

    # Custom Menu ids
    service_section_ids = fields.One2many('service.section', 'company_id')

    # Industries
    arc_industries_title = fields.Char(string="Industry Main Title")
    arc_industries_ids = fields.One2many(
        comodel_name='arc.industries',
        inverse_name='company_id',
    )

    # Development process
    development_process_sec_title = fields.Char(string="Title")
    development_process_img = fields.Image(string="Development Process Image")


class ArcTestimonials(models.Model):
    _name = "arc.testimonials"
    _description = "Testimonials Info"
    _rec_name = "title"

    title = fields.Char(string="Title")
    desc = fields.Html(string="Description")
    testimonial_from = fields.Char(string="Testimonials From")
    testimonial_role = fields.Char(string="Testimonials Role")
    image = fields.Image(string="Image")
    company_id = fields.Many2one(comodel_name="res.company")


class ArcTechnologies(models.Model):
    _name = "arc.technologies"
    _description = "Arc Technologies"

    name = fields.Char(string="Title")
    image = fields.Image(string="Image")
    company_id = fields.Many2one(comodel_name="res.company")


class ArcPartners(models.Model):
    _name = "arc.partners"
    _description = "Arc Partners"

    name = fields.Char(string="Title")
    image = fields.Image(string="Image")
    company_id = fields.Many2one(comodel_name="res.company")


class ArcTeams(models.Model):
    _name = "arc.team"
    _description = "Arc Team Members"

    full_name = fields.Char()
    image = fields.Image(string="Image")
    designation = fields.Char()
    company_id = fields.Many2one(comodel_name="res.company")


class ArcServices(models.Model):
    """Arc Services"""
    _name = "arc.services"
    _description = "Arc Services"

    name = fields.Char(string="Title")
    subtitle = fields.Text(string="Sub Title")
    image = fields.Image(string="Icon")
    extra_desc = fields.Html(string="Extra Description")
    company_id = fields.Many2one(comodel_name="res.company")


class ArcIndustries(models.Model):
    """Are Industries"""
    _name = "arc.industries"
    _description = "Arc Industries"

    name = fields.Char(string="Title")
    company_id = fields.Many2one(comodel_name="res.company")
    image = fields.Image(string="Icon")


class ArcFrequentlyAskedQue(models.Model):
    """Arch Frequently Asked Questions"""
    _name = 'arch.frequent.que'
    _description = __doc__

    question = fields.Char()
    answer = fields.Text()
    company_id = fields.Many2one('res.company')
