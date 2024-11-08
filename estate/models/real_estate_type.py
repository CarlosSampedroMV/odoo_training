from odoo import models,fields

class PropertyType(models.Model):
    _name ="real.estate.type"
    _description = "test"

    name = fields.Char(string ="NameType")
