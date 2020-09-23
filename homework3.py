#Task1
from variables_mane import *
a = int(input("How many kilometers is the road?"))
m = 1.6*a
print("\n\tIt will be equal to", m, "Miles",end="\n\n\n")
#Task2
c = int(input("How many AMD do you have?"))
d = c*usd
print("\n\tAnd if we turn it into dollars, it will be", d, "USD", end="\n\n\n")
#Task3
b = int(input("How old are you?"))
k = int(year)-b+100
print("\n\tYou will become 100 years old in", k, end="\n\n\n")
#Task4
s = int(input("How many centimeters is your height?"))
weigh = (s-110)*index
print("\n\tDoctors adwise", weigh, "kilograms with your height", end="\n\n\n")
#Task5
year1 = int(input("What year is it?"))
month1 = int(input("What month is Oktober?"))
day1 = int(input("Which day is the middle of the April?"))
mm = (year1//1000)+(month1//10)+(day1//10)
print("\n\tAnd the value of the first symbols will be", mm, end="\n\n\n")
#Task6
bb = int(input("When were you born?"))
kk = (year-bb)*525600+minute
print("\n\tYou have lived", kk, "minutes until now")