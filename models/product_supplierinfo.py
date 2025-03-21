from odoo import api, fields, models

class SupplierInfo(models.Model):
    _inherit = 'product.supplierinfo'
    
    previous_price = fields.Float(
        string='Precio Anterior',
        digits='Product Price', 
        readonly=True,
        help="Stores the previous price value before changes"
    )
    
    @api.model_create_multi
    def create(self, vals_list):
        # When creating new records, set previous_price same as price
        for vals in vals_list:
            if 'price' in vals:
                vals['previous_price'] = vals['price']
        return super().create(vals_list)
    
    def write(self, vals):
        # Before updating, store the current price as previous price
        if 'price' in vals:
            for record in self:
                # Only update previous_price when price is actually changing
                if record.price != vals['price']:
                    vals['previous_price'] = record.price
        return super().write(vals)
