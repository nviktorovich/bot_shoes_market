from .constant import Messages
from datetime import datetime


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