from odoo import models,fields

class RealEstate(models.Model):
    _name ="real.estate"
    _description = "Test model"

    name = fields.Char(default ="House", required=True)
    price = fields.Float()

    active = fields.Boolean(default=True)#, invisible=True)
    name = fields.Char(required=True)
    state = fields.Selection(
        [
            ("new","New"),
            ("received","Offer Received"),
            ("accepted","Offer Accepted"),
            ("sold","Sold"),
            ("cancelled","Cancelled"),
        ],
        required = True,
        copy = False,
        default = "new"

    )
    postcode=fields.Char()

    def _default_date(self):
        return fields.Date.today()

    date_availability = fields.Date(default=_default_date)
    expected_price = fields.Float()
    best_offer = fields.Float()
    selling_price =fields.Float()

    description = fields.Text()
    bedrooms = fields.Integer()
    living_area = fields.Integer()

    property_type_id = fields.Many2one("real.estate.type", string="NameType")
    