class Choice:
	brand = ''
	model = ''
	color = ''

	@staticmethod
	def set_brand(brand=False):
		if brand:
			Choice.brand = brand
		else:
			Choice.brand = ''

	@staticmethod
	def set_model(model=False):
		if model:
			Choice.model = model
		else:
			Choice.model = ''

	@staticmethod
	def set_color(color=False):
		if color:
			Choice.color = color
		else:
			Choice.color = ''
