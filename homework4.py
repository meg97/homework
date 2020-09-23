#Task1
print("\nPplease tell me with price what do you want. In our menu pizza is 1000AMD, kebab-1500, ketchup-200 and mayonez-300")
m = int(input("\nWhat do you want pizza or kebab?"))
n = int(input("\nand which addition do you prefer ketchup or mayonez?"))

print("\nYou have ordered pizza and ketchup and your price is 1200",m+n == 1200)
print("\nYou have ordered pizza and mayonez and your price is 1300",m+n == 1300)
print("\nYou have ordered kebab and ketchup and your price is 1700",m+n == 1700)
print("\nYou have ordered kebab and mayonez and your price is 1800",m+n == 1800)

#Task2
print("\n\nAssume the days of the week are numbered 0,1,2,3,4,5,6 from Sudnay to Saturday")
k=int(input("\n\tTell me the day's number and I'll say what day is it"))
if k==0:
	print("\n\t\tToday is Sunday")
elif k==1:
	print("\n\t\tToday is Monday")
elif k==2:
	print("\n\t\tToday is Tuesday")
elif k==3:
	print("\n\t\tTodauy is Wednesday")
elif k==4:
	print("\n\t\tToday is Thursday")
elif k==5:
	print("\n\t\tToday is Friday")
else:
	print("\n\t\tToday is Saturday")

#Task3
f = input("\n\t\tTell me something and I'll say it's a word or sentence\n\t\t")
if " " in f:
	print("\n\t\tIt's sentence")
else:
	print("\n\t\tIt's only one word")
#Task4
h = input("\n\t\ttell me a word\n\t\t")
if len(h)>2:
	if h [-3:] =="ing":
		print("\n\t\t",h+"ly")
	elif h[-3] !="ing":
		print("\n\t\t",h+"ing")
else:
	print("\n\t\t", h)