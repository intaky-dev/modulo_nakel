from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    # This field will be a computed field based on supplier info
    previous_price = fields.Float(
        string='Precio Anterior',
        compute='_compute_previous_price',
        store=False,
        digits='Product Price',
        help="Previous supplier price"
    )
    
    def _compute_previous_price(self):
        for product in self:
            # Find the first supplier info with a previous price
            supplier_info = self.env['product.supplierinfo'].search([
                ('product_tmpl_id', '=', product.id),
                ('previous_price', '>', 0),
            ], limit=1)
            
            if supplier_info:
                product.previous_price = supplier_info.previous_price
            else:
                product.previous_price = 0.0
