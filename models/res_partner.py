from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    distributor_code = fields.Char()