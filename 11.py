# user_answer = input("tell something")
# try:
# 	my_number = int(user_answer)
# 	value = 10 / my_number  
# except ValueError:
# 	print("Wrong value it is not a digit")
# 	my_number = 0
# except ZeroDivisionError:
# 	print("the number couldn't be 0")
# 	value = 10
# my_number += 5
# try:
# 	print(value)
# except NameError:
# 	print("You didn't give a number thats why you couldn't see the VALUE")


dict_1 = {"key1":1, "key2":2}
dict_2 = {"key1":10, "key3":1, "key4":2}
dict_3 = {}
# for i in dict_1:

# 	dict_3[i] = dict_1[i]
# for j in dict_2:
# 	dict_3[j] = dict_2[j]
# print(dict_3)

for key in dict_2:
	dict_1[key] = dict_2[key]
print(dict_1)
print(dict_2)