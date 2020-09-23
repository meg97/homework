from random import randint
# def my_function(a):
# 	b = f"Happy birthday dear {a}"
# 	return b

# b = my_function("Mane")
# print(b)


# help(randint)
#print(randint.__doc__)


# def my_function(a):
# 	k = "1x"
# 	c = 1
# 	a = int(input("Tell me number"))
# 	for i in range (1,a):
# 			c *= i
# 			k += f"x{i}"
# 			d = f"{k}={c}"
# 			return d
# m = my_function(5)
# print(m)

def function(a,b,c=1):
	d = a*b*c
	print(d)
a_input = int(input("tell me the parameter"))
b_input = int(input("Tell me the parameter"))
c_input = int(input("Tell me the parameter"))
function(a_input, b_input, c_input)




# check = "yes"
# score_user = 0
# score_computer = 0
# roundd = 0
# while check =="yes":
# 	user_choice = int(input("1 for Scissors,2 for Paper, 3 for Rock"))
# 	computer_coice = randint(1,3)
# 	if (user_choice == 1 and user_choice == 2) or (user_choice == 2 and user_choice == 3) or (user_choice == 3 and user_choice == 1):
# 		score_user +=1
# 	elif user_choice == computer_coice:
# 		print("Tie")
# 	else:
# 		score_computer +=1 
# 	roundd +=1
# 	check = ""
# 	while check != "no" or check != "yes":
# 		check = input("Do tou want to play again?say yes for yes")

# print(f"Hope you enjoyed\n your score is {score_user}, computer score {score_computer}, rounds are {roundd}")