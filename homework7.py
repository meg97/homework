# import random
# #Task1
# s = ""
# k = 1
# m = int(input("Tell me a number and I'll caculate it's !\n\t\t"))
# print("\n\t\t",m,"!", "=", k, end=s)
# for i in range(2, m+1):
# 	k *= i  
# 	print(f"x {i}", end=s) 
# print("=", k)
	
# #Task2
# score = 0
# i = "sure"
# while i == "sure":
# 	users_answer1 = input("\n\tDo you want to go travel?\n\t")
# 	users_answer2 = input("\n\nDo tou preffer rain?\n\t")
# 	random_number = random.randint(0,1)
# 	yes = 1
# 	no = 0
# 	if users_answer1 == random_number:
# 		score += 1
# 	elif users_answer2 == random_number:
# 		score += 1
# 	i = input("Do you want to continue? sure for yes\n\t")
# if score >=1:
# 		print("you can go travel")
# else:
# 		print("you should be at home")

# #Task3
a = 0
b = 1
c = 1
while c < 50:
	a = b
	b = c
	c = a + b
	print(c)
	#print(f"{a},{b}")

# #Task4  
# score = 0
# rounds = 0
# i = "yes"
# while i == "yes":
# 	answer = int(input("\n\t\tRock_Paper_Sceasors\n\t\t"))
# 	random_number = random.randint(1,3)
# 	Rock = 1
# 	Paper =2
# 	Sceasors = 3
# 	if answer > random_number:
# 		score +=1
# 	i = input("\n\t\tdo you want continut?\n\t\t")
# 	rounds +=1
# if score > rounds:
# 	print("\n\t\tYou winn!")
# else:
# 	print("\n\t\tLet's try again")


# #Task5
# for i in range(0,10):
# 	print((10-i)*" "+2*i*"*")
# for j in range(10,0,-1):
# 	print((10-j)*" "+ 2*j*"*")