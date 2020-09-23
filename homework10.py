#Task1
my_list = [[10, 20], [40], [30, 56, 25], [10,20], [33], [40]]
my_list.sort()
new_list = []
for i in my_list:
	if not i in new_list:
		new_list.append(i)
print(new_list)

# #Task2
original_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110,120]]
k = []
m = []
for i in original_list:
	if type(i) != list: 
		k.append(i)
	else:
		for j in i:
			m.append(j)

flatten_list = k+m
flatten_list.sort()
print(flatten_list)


#Task3
given_list = [1, 1, 2, 3, 4, 4, 5, 1]
m = ""

for i in given_list:
	m += f"{str(i)}"
k = m[0:3]
s = m[3:]
splited_list1 = list(k)
splited_list2 = list(s)
print(f"{splited_list1}, {splited_list2} ")
 

#Task4

#Task5
print("  --- --- ---", "\n","|   |   |   |", "\n", " --- --- ---", "\n","|   |   |   |", "\n", " --- --- ---", "\n","|   |   |   |", "\n", " --- --- ---")  