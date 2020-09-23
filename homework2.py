#task1
c = 3
f = c*9/5+32 
print(f)
#we can write so
f = 1.8*c+32
print(f)
#or the opposite function. we can also express <<C>> with <<F>>
f = 100
c = (f-32)*5/9
print(c)
print("\n\n\n")
#task2
a = 5
b = 6
c = 7
#1
average_value = (a+b+c)/3
print(average_value,"\n\n") 
#2
e = a**c+b**c
print(e,"\n\n")
#3
m = (a+b)**c
print(m,"\n\n")
#4
abc = 567
n = (abc)+a*b*c
print(n, "\n\n\n") #I know it's wrong, but I can't find another way
#task3
#there is a formula for triangular area, if we have 3 sides of it (Heron's formula)
formula_name = ("Heron's formula")
a = 2
b = 3
c = 4
p = (a+b+c)/2
s = (p*(p-a)*(p-b)*(p-c))**1/2
print('When we have 3 sides of the trianugle, we can use', formula_name, 'for tringular area',end="\n\n")
print("\t\t\t\ts=(p*(p-a)*(p-b)*(p-c))**1/2,", "where p=(a+b+c)/2," "in this case","\t\t\t\ta=2,","\t\t\t\tb=3,","\t\t\t\tc=4,","we can calculate the triangular area",sep="\n\n",end="\n\n")
print("\t\t\t\ts=",s)


