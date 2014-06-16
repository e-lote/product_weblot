from openerp.osv import osv,fields

class res_partner(osv.osv):
	_name = "res.partner"
	_inherit = "res.partner"

	_columns = {
		'production_center': fields.boolean('Production Center'),
		}
       
res_partner()
