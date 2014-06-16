from openerp.osv import osv,fields
import openerp.addons.decimal_precision as dp


class product_paper_colour(osv.osv):
        _name = "product.paper_colour"
        _description = "Paper Colour"

        _columns = {
                'name': fields.char('Name',size=32),
                }
product_paper_colour()


class product_colour_pages(osv.osv):
        _name = "product.colour_pages"
        _description = "Colour Pages"

        _columns = {
                'name': fields.char('Colour Pages',size=32),
                }
product_colour_pages()

class product_pub_bs(osv.osv):
        _name = "product.publishing_bs"
        _description = "Publishing BS"

        _columns = {
                'name': fields.char('Name',size=32),
                }
product_pub_bs()

class product_endsheets(osv.osv):
	_name = "product.endsheets"
	_description = "Product Endsheets"

	_columns = {
		'name': fields.char('Name',size=32),
		}
product_endsheets()

class product_weight_gsmpp(osv.osv):
	_name = "product.weight.gsmpp"
	_description = "Product Weight GSMPP"

	_columns = {
		'name': fields.char('Name',size=32),
		}
product_weight_gsmpp()

class product_ribbons(osv.osv):
	_name = "product.ribbons"
	_description = "Product Ribbons"

	_columns = {
		'name': fields.char('Name',size=32),
		}
product_ribbons()

class product_edge(osv.osv):
	_name = "product.edge"
	_description = "Product Edge"

	_columns = {
		'name': fields.char('Name',size=32),
		}
product_edge()

class product_size(osv.osv):
	_name = "product.size"
	_description = "Product Size"

	_columns = {
		'name': fields.char('Name',size=32),
		}
product_size()

class product_colour(osv.osv):
	_name = "product.colour"
	_description = "Product Paper Colour"

	_columns = {
		'name': fields.char('Name',size=32),
		}
product_colour()

class product_binding(osv.osv):
	_name = "product.binding"
	_description = "Product Binding"

	_columns = {
		'name': fields.char('Name',size=32),
		}
product_binding()

class product_language(osv.osv):
	_name = "product.language"
	_description = "Product language"

	_columns = {
		'name': fields.char('Name',size=32),
		}
product_language()

class product_familia(osv.osv):
	_name = "product.familia"
	_description = "Familia a la que pertenece el producto"

	_columns = {
		'name': fields.char('Name',size=32),
		}
product_familia()

class product_categoria(osv.osv):
	_name = "product.categoria"
	_description = "Categoria a la que pertenece el producto"

	_columns = {
		'name': fields.char('Name',size=32),
		}
product_categoria()

class product_version(osv.osv):
	_name = "product.version"
	_description = "Version a la que pertenece el producto"

	_columns = {
		'name': fields.char('Name',size=32),
		}
product_version()

class product_subcategoria(osv.osv):
	_name = "product.subcategoria"
	_description = "SubCategoria a la que pertenece el producto"

	_columns = {
		'name': fields.char('Name',size=32),
		}
product_subcategoria()

class product_product(osv.osv):
	_name = "product.product"
	_inherit = "product.product"

	_columns = {
	        # 'ean13': fields.related('product_variant_ids', 'ean13', type='char', string='ISBN Barcode'),
	        'ean13': fields.char('ISBN', type='char', size=13),
		# 'publishing_bs': fields.char('Publishing BS',size=3),
		'publishing_bs': fields.many2one('product.publishing_bs','Publishing BS'),
		'isbn': fields.char('ISBN',size=13),
		'ubs_code_prefix': fields.char('UBS Code Prefix'),
		'ubs_code_no': fields.integer('UBS Code No'),
		'ubs_code_suffix': fields.char('UBS Code Suffix'),
		'producto_nuevo': fields.boolean('Producto Nuevo'),
		# 'events_ids': fields.many2many('product.event','product_event_rel','product_id','event_id','Eventos'),
		'language': fields.many2one('product.language','Language'),
		'familia': fields.many2one('product.familia','Familia'),
		'categoria': fields.many2one('product.categoria','UBS Category'),
		'version': fields.many2one('product.version','Version'),
		'subcategoria': fields.many2one('product.subcategoria','UBS SubCategory'),
		# Product attributes
		'tps_width': fields.float('Width',digits_compute=dp.get_precision('Product Price')),
		'tps_height': fields.float('Height',digits_compute=dp.get_precision('Product Price')),
		'image_area_width': fields.float('Width',digits_compute=dp.get_precision('Product Price')),
		'image_area_height': fields.float('Height',digits_compute=dp.get_precision('Product Price')),
		'maps_area_width': fields.float('Width',digits_compute=dp.get_precision('Product Price')),
		'maps_area_height': fields.float('Height',digits_compute=dp.get_precision('Product Price')),
		'maps_area_colored_end_pages': fields.float('Colored End pages',digits_compute=dp.get_precision('Product Price')),
		'maps_area_colored_section_pages': fields.float('Colored Section pages',digits_compute=dp.get_precision('Product Price')),
		# 'paper_colour_pages': fields.char('Colour pages'),
		'paper_colour_pages': fields.many2one('product.colour_pages','Colour Pages'),
		'paper_weight_pages': fields.float('Weight',digits_compute=dp.get_precision('Product Price')),
		'paper_gsm_pp': fields.char('GSM/PP'),
		# 'paper_colour': fields.integer('Colour'),
		'paper_colour': fields.many2one('product.paper_colour','Paper Colour'),
		'bible_binding': fields.many2one('product.binding','Binding'),
		# 'bible_binding': fields.selection((('Rustica','Rustica'),('Tapa Dura','Tapa Dura'),('Jean','Jean'),('Bonded Lethear','Bonded Lethear'),('PU','PU')),'Binding'),
		'bible_colour': fields.many2one('product.colour','Colour'),
		
		# 'bible_colour': fields.selection((('Blanco','Blanco'),('Crema','Crema'),('Periodico','Periodico'),('Directorio','Directorio')),'Colour'),
		# 'bible_size': fields.integer('Size'),
		'bible_size': fields.many2one('product.size','Size'),

		# 'endsheets': fields.selection((('Blancas','Blancas'),('Color','Color')),'Endsheets'),
		'endsheets': fields.many2one('product.endsheets','Endsheets'),
		# 'weight_gsm_pp': fields.selection((('Papel Obra','Papel Obra'),('Papel Ilustracion','Papel Ilustracion'),('50 gsm','50 gsm')),'Weigth gsm/pp'),
		'weight_gsm_pp': fields.many2one('product.weight.gsmpp','Weight gsm/pp'),
		'ribbons': fields.float('Ribbons',digits=(16,2)),
		# 'edge': fields.selection((('stained red','stained red'),('stained blue','stained blue'),('Gold','Gold'),('Silver','Silver'),('Other','Other')),'Edge'),
		'edge': fields.many2one('product.edge','Edge'),
		#'familia': fields.selection((('BIBLIAS','BIBLIAS'),('LIBROS','LIBROS'),('SELECCIONES NL','SELECCIONES NL'),\
		#	('SELECCIONES','SELECCIONES'),('PORCIONES NL','PORCIONES NL'),('PORCIONES','PORCIONES'),('NT','NT'),\
		#	('MEDIA','MEDIA'),('OTROS','OTROS')),'Familias'),
		#'categoria': fields.selection((('ACADEMICO','ACADEMICO'),('LUJO','LUJO'),('MISIONERA','MISIONERA'),('PRECIO MEDIO','PRECIO MEDIO'),\
		#		('LIBROS','LIBROS'),('EDUC DIFUSION','EDUC DIFUSION'),('JUEGOS','JUEGOS'),('MUSICA','MUSICA'),('REPLICA','REPLICA'),\
		#		('VARIOS','VARIOS'),('SELECCION','SELECCION')),'Categoria'),
		#'version': fields.selection((('Dios Habla Hoy','Dios Habla Hoy'),
		#			     ('Dios Habla Hoy con Deutero','Dios Habla Hoy con Deutero'),
		#			     ('Nueva Version Internacional','Nueva Version Internacional'),
		#			     ('Reina Valera 1909','Reina Valera 1909'),
		#			     ('Reina Valera 1960','Reina Valera 1960'),
		#			     ('Reina Valera 1995','Reina Valera 1995'),
		#			     ('Reina Valera Contemporanea','Reina Valera Contemporanea'),
		#			     ('Traduccion Lenguaje Actual','Traduccion Lenguaje Actual'),
		#			     ('Traduccion Lenguaje Actual con Deutero','Traduccion Lenguaje Actual con Deutero'),
		#			     ('Multiversion','Multiversion'),
		#			     ('Ninguna','Ninguna')),'Version'),
		#'subcategoria': fields.selection((('Digital','Digital'),('Especializado','Especializado'),\
		#				 ('Especializado-Jovenes','Especializado-Jovenes'),('Especializado-Mujeres','Especializado-Mujeres'),\
		#				 ('Estandar','Estandar'),('Estandar Economico','Estandar Economico'),\
		#				 ('Estandar-Letra Grande','Estandar-Letra Grande'),('Estudio','Estudio'),\
		#				 ('Ninios','Ninios')),'Sub-Categoria'),
		}

		#'familia': fields.selection((('BIBLIAS','BIBLIAS'),('LIBROS','LIBROS'),('SELECCIONES NL','SELECCIONES NL'),\
		#	('SELECCIONES','SELECCIONES'),('PORCIONES NL','PORCIONES NL'),('PORCIONES','PORCIONES'),('NT','NT'),\
		#	('MEDIA','MEDIA'),('OTROS','OTROS')),'Familias'),
		#	}
		# 'categoria': fields.selection((('ACADEMICO','ACADEMICO'),('LUJO','LUJO'),('MISIONERA','MISIONERA'),('PRECIO MEDIO','PRECIO MEDIO'),\
		#		('LIBROS','LIBROS'),('EDUC DIFUSION','EDUC DIFUSION'),('JUEGOS','JUEGOS'),('MUSICA','MUSICA'),('REPLICA','REPLICA'),\
		#		('VARIOS','VARIOS'),('SELECCION','SELECCION')),'Categoria'),
	
product_product()


