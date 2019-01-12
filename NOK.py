def choice_input_method ():
	'''Выбор способа ввода данных'''
	choice = 0
	while True:
		try:
			choice = int(input("Введи 1, если хочешь задать диапазон чисел, или 2 если список конкретных чисел: "))
			if choice == 1 or choice == 2:
				break
			else:
				print ("(ಠ_ಠ) Введи 1 или 2")
		except:
			print ("(ಠ_ಠ) Введи 1 или 2")
	return choice

def create_list (choice):
	"""Создаем список из нужных цифр"""
	input_list = []
	input_number = 0
	if choice == 1:
		while True:
			try:
				home = int(input("(•ิ_•ิ)? Введите начало диапазона: "))
				end = int(input("(•ิ_•ิ)? Введите конец диапазона: "))
				break
			except:
				print ("Введите натуральное число, никаких букв!", 'ლ(¯ロ¯"ლ)')
		if home <= end:
			input_list = [i for i in range(home, end + 1)]
		elif home > end:
			input_list = [i for i in range(end, home + 1)]
	elif choice == 2:
		print("Вводите числа, разделяя их клавишей Enter. По окончании ввода введите 0")
		while True:
			try:
				input_number = int(input())
				if input_number != 0:
					input_list.append(input_number)
					print ("Вы уже ввели следующие числа:", end = " ")
					for i in input_list:
						print (i, end = " ")
				else:
					break
			except:
				print ("Введите натуральное число, никаких букв!", 'ლ(¯ロ¯"ლ)')
	return input_list

def nod_fun (a, b):
	"""Находим наибольший общий делитель"""
	while b:
		a, b = b, a % b
	return a

def nok (input_list):
	"""Вычисление наименьшего общего кратного"""
	input_list_positive = []
	for i in input_list:    # обеспечиваем работу со списком, включающим 
		if i > 0:			# отрицательные значения
			input_list_positive.append(i)
		else:
			i = i * (-1)
			input_list_positive.append(i)
	input_list_positive.sort(reverse=True)
	try:
		input_list_positive.remove(0)
	except:
		True
	try:
		answer = input_list_positive [0]
	except:
		answer = (' ...\nНа ноль делить нельзя, дурачок')
	nod = 0
	for i in range(0, len(input_list_positive)+1):
		try:
			nod = nod_fun(answer, input_list_positive[i + 1])
			answer = int((answer * input_list_positive[i+1]) / nod)
		except:
			print("\n(-_-;)・・・")
	return answer

############### ===MAIN=== ###############


print('''(´• ω •`)ﾉ\nПривет, я помогу тебе найти наименьшее общее кратное
нескольких чисел\n===========================================\n''')
print('наименьшее общее кратное равно ', nok(create_list(choice_input_method())))
