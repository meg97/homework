#1
# number = input("tell me number")
# try:
# 	half = int(number) / 2
# 	print(half)
# except ValueError:
# 	print("please tell me only number")


#2
# num_1 = int(input("tell me number to divide 4 with"))
# try:
# 	new_value = 4 / num_1
# 	print(new_value)
# except ZeroDivisionError:
# 	print("Dont't tell me 0")


#3
# try:
# 	print(a)
# except NameError:
# 	print("Please first say me the veriable")


#4
# num = int(input("Tell me a number"))
# try:
# 	num = num + "2"
# except TypeError:
# 	print("We can't add int to str")

#5

# my_list = [1,2, "hello"]
# try:
# 	intem = my_list[3]
# except IndexError:
# 	print("Index isn't in the list")

check = True

while check:
	try:
		password = input("Tell me the password")
		if len(password) < 8:
			raise ValueError("It should be great than 8")

		check_number = False
		for i in password:
			if i.isdigit():
				check_number = True
			if not i.isalpha():
				if i !=" ":
					break
				else:
					raise NameError("The password could not contain a space")
		
	
		if not check_number:
			raise TypeError("Should cantain number")
		if password[0].islower():
			raise Exception("Should start with a capital letter")
		check = False
	except TypeError as t:
		print(t) 
	except ValueError as e:
		print(e)
	except NameError as n:
		print(n)
	except Exception as exc:
		print(exc)

print(F"{password} is strong one")
