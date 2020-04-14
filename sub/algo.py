from .constant import Messages
from datetime import datetime
import xlrd


def get_fission_balance_list(*lst):
	"""

	:param lst: list with count(*args) // 3 == 0
	:return: answer (type - list) with [[1, 2 ,3], [1, 2, 3], ... etc]
	"""
	answer = []
	for x in range(1, len(lst) // 3 + 1):
		answer.append([lst[x * 3 - 3], lst[x * 3 - 2], lst[x * 3 - 1]])
	return answer


def get_parts_of_list(*lst):
	"""

	:param lst: get list with different count of args
	:return: answer list - type where maximum of args are [1,2,3], [1,2,3] and fission is [1,2] or [1]
	"""
	if len(lst) > 3:
		if len(lst) % 3 == 2:
			answer = get_fission_balance_list(*lst[:-2])
			answer.append([lst[-2], lst[-1]])
		elif len(lst) % 3 == 1:
			answer = get_fission_balance_list(*lst[:-1])
			answer.append([lst[-1]])
		elif len(lst) % 3 == 0:
			answer = get_fission_balance_list(*lst)
	elif len(lst) <= 3:
		answer = [list(lst)]

	return answer


def get_list_of_colors(where, what):
	"""

	:param where: dictionary where we search
	:param what: what we search
	:return: list
	"""
	return [x[0] for x in where[what]] if what != '' else []


def get_photo_link(where, what, color):
	for row in where[what]:
		if row[0] == color:
			return row[2], row[1]


def get_color_select_message(brand, model):
	return f'Выбирете цвет для модели "{brand} - {model}"'


def get_buy_message(description):
	return f'Вы выбрали <b>{description}</b>' \
	       f'\nОтличный выбор!' \
	       f'\nНажмите <b>{Messages.SHOW_PHONE_BUTTON}</b>' \
	       f'\nНаш менеджер свяжется с вами для уточнения размера модели и обсудит остальные детали'


def send_message_to_host(*args):

	phone = args[0]
	message = ' / '.join(args[1:])
	today = datetime.today()
	current_time = today.strftime("дата: %Y-%m-%d\nвремя: %H:%M")
	return f'✅ Поступила заявка❗️\n{current_time}\n\n📞: {phone}\n👟: {message}'


def generate_model_list(dictionary):
	"""

	:param dictionary: get dictionary with brands - keys
	:return: list with all values all keys from input dictionary
	"""
	return [model for key in dictionary.keys() for model in dictionary[key]]


def generate_brands_dictionary(file, option='Brands'):
	"""

	:param file: path to opened files
	:param option: default = "Brands" to return dictionary with {brand_name:(model1, model2), bran_dname2:(...)};
					"Colors" to return dictionary with all models colors and other params {model1:[(color1, price, ref),
																									(color2, ...)]}
	:return: dictionary due to selected option
	"""
	wb = xlrd.open_workbook(file)
	sheet_names = wb.sheet_names()[1:]

	# create dictionary "Brands"
	Brands = {}

	for sheet in sheet_names:
		current_sheet = wb.sheet_by_name(sheet)
		Brands[sheet] = tuple(
			set([model.capitalize() for model in current_sheet.col_values(1) if model not in ['', 'MODEL']]))

	# create dictionary "Colors"
	Colors = {model: [] for brand in Brands.keys() for model in Brands[brand]}

	for sheet in sheet_names:
		current_sheet = wb.sheet_by_name(sheet)
		for row_index in range(2, len(current_sheet.col(0))):
			if current_sheet.row_values(row_index)[1] != '':
				Colors[current_sheet.row_values(row_index)[1].capitalize()].append(
					(current_sheet.row_values(row_index)[2],
					 current_sheet.row_values(row_index)[3],
					 current_sheet.row_values(row_index)[4]))

	if option == 'Brands':
		return Brands
	if option == 'Colors':
		return Colors
