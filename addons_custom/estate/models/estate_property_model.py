from odoo import models, fields


class EstatePropertyModel(models.Model):

    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char(string="Name", required=True, default="Unknown")
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(
        string="Date Availability", copy=False, default=fields.Date.today
    )
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price", readonly=True, copy=False)
    bedrooms = fields.Integer(string="Bed Rooms", default=2)
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection(
        string="Garden Orientation",
        selection=[
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West"),
        ],
        help="Type is used to separate Leads and Opportunities",
    )
    state = fields.Selection(
        string="Status",
        selection=[
            ("new", "New"),
            ("offer received", "Offer Received"),
            ("offer accepted", "Offer Accepted"),
            ("sold and canceled", "Sold and Canceled"),
        ],
        help="Status is used to condition",
    )
    active = fields.Boolean("Active", readonly=False, default=True)
    property_type_id=fields.Many2one("estate.property.type","Property Type")
    buyer_id=fields.Many2one("res.partner", string="Buyer")
    salesmen_id = fields.Many2one('res.users', string='Salesperson', index=True, tracking=2, default=lambda self: self.env.user)
    tag_ids=fields.Many2many('estate.property.tag',string="Tag")
    offer_ids=fields.Many2many('estate.property.offer',string='Offer')