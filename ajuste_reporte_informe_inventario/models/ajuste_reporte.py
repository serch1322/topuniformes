# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AjustarReporte(models.Model):
    _inherit = 'stock.quant'

    product_category = fields.Char(related='product_id.categ_id.complete_name', string="Categoría de Producto",store=True)