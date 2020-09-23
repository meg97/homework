# #Task1
# a = int(input("\nSay me what is the year and I'll say is it a leap year or no\n\t\t"))
# if a % 100 == 0 and a % 400 != 0:
# 		print("It isn't a leap year")
# elif a % 4 == 0:
# 	print("It's a leap year")
# else:
# 	print("It isn't a leap year")	

# #Task2
# m = int(input("\n\tTell me a number"))
# if m % 5 == 0 and m % 11 == 0:
# 	print("\n\tIt's divisible by 5 and 11")
# elif m % 5 == 0: 
# 	print("\n\tIt's divisible by 5")
# elif m % 11 == 0:
# 	print("It's divisible by 11")
# else:
# 	print("Your number isn't for our task")

# #Task3
# k = int(input("\n\t\tLet's try again. Tell me number\n\t\t"))
# if k % 3 == 0 and k % 5 == 0:
# 	print("\n\t\tFizzBuzz")
# elif k % 3 == 0:
# 	print("\n\t\tFizz")
# elif k % 5 == 0:
# 	print("\n\t\tBuzz") 
# else:
# 	print("\n\t\t", k)

# #Task4
# f = "\nThe lytics is not that poor\n\t\t"
# new = "good"
# m = f.index("not")
# n = f.index("poor") 
# k = (f[m:n+4])
# new_sentence = f.replace(k,new)
# if f.index("not") < f.index("poor"):
# 	print(new_sentence) 

#Task5
word = "return"
my_input = input("\n\tTell me a letter\n\t\t")
s = word.index(my_input)
f = word[s+1:].index(my_input)
print(f)
# #Task6
# p = input("\n\tTell me first letter")
# j = input("\n\tTell me second letter")
# v = input("\n\tTell me thirth letter") 
# if ord(p) < ord(j) and ord(j) < ord(v):
# 	print("these letters are in order")
# else:
# 	print("\n\tPlease order the letters")