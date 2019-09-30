import random
import string
import time


number_list = range(1, 27)
letter_list = [x for x in string.ascii_lowercase]
caps_list = [x for x in string.ascii_uppercase]

num_to_alph = dict(zip(number_list, letter_list)) # dictionary of numbered lowercase letters
num_to_caps = dict(zip(number_list, caps_list)) # dictionary of numbered uppercase letters

symbol_list = ['#', '!', '@', '%']
number_list2 = range(1, 5)

num_to_symbols = dict(zip(number_list2, symbol_list)) # dictionary of numbers to symbols 


def random_list(password_length):
	list_of_letters = []

	for k in range(0, a):
		list_of_letters.append(num_to_caps[random.randint(1, 26)])

	for k in range(0, b):
		list_of_letters.append(num_to_symbols[random.randint(1, 4)])

	for k in range(0, c):
		list_of_letters.append(str(range(0, c)[random.randint(1, c-1)]))

	for k in range(0, password_length - a - b - c):
		list_of_letters.append(num_to_alph[random.randint(1, 26)])

	password = ''.join(random.sample(list_of_letters, password_length)) # Shuffle the letters

	return password


def main():
	a = 0
	b = 0
	c = 0


	print("""has_uppercase = 
	1. True
	2. False""")

	answer1 = input("> ")
	
	if answer1 == '1':
		has_uppercase = True

	elif answer1 == '2':
		has_uppercase = False

	else:
		print("This is not an option. Try again.")
		prompt_conditions()

	if has_uppercase == True:
		a = random.randint(1, 3)

	elif has_uppercase == False:
		a = 0

	else:
		pass

	print("""has_symbols = 
	1. True
	2. False""")

	answer2 = input("> ")

	if answer2 == '1':
		has_symbols = True

	elif answer2 == '2':
		has_symbols = False

	else:
		print("This is not an option. Try again.")
		main()


	if has_symbols == True:
		b = random.randint(1, 3)
		
	elif has_symbols == False:
		b = 0
		
	else:
		pass

	print("""has_numbers = 
	1. True
	2. False""")

	answer3 = input("> ")

	if answer3 == "1":
		has_numbers = True
	elif answer3 == "2":
		has_numbers = False
	else:
		print("This is not an option. Try again.")
		main()

	if has_numbers == True:
		c = random.randint(1, 3)

	elif has_numbers == False:
		c = 0

	else:
		pass

	password_len = int(input("""password_length = """))

	
	list_of_letters = []

	for k in range(0, a):
		list_of_letters.append(num_to_caps[random.randint(1, 26)])

	for k in range(0, b):
		list_of_letters.append(num_to_symbols[random.randint(1, 4)])

	for k in range(0, c):
		list_of_letters.append(str(range(0, c + 1)[random.randint(1, c)]))

	for k in range(0, password_len - a - b - c):
		list_of_letters.append(num_to_alph[random.randint(1, 26)])
	# Shuffle the letters
	password_ = ''.join(random.sample(list_of_letters, password_len)) 

	print('Your new password is:', password_)
	
	time.sleep(3)


if __name__ == "__main__":
	main()
else:
	pass
