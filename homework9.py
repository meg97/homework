# #Task1
# my_list = [1,2,3,2,1,1,3,5,7]
# my_list1 = []
# for i in my_list:
# 	if not i in my_list1:
# 		my_list1.append(i)
# print(my_list1)

	

# #Task2
# first_list = [1,1,2,3,5,8,13,21,34,55,89]
# second_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# new_one = []
# for i in first_list:
# 	if i in second_list and i not in new_one:
# 		new_one.append(i)
# print(new_one)

# #Task3
# k = ""
# a = [1,1,2,3,5,8,13,21,34,55,89]
# for i in a:
# 	if i < 3:
# 		k += f"{i}"
# print(list(k))

# #Task4
# def my_funktion(m):
# 	n = ""
# 	lenn = len(m)
# 	for i in range(lenn-1, -1, -1):
# 		s = m[i]
# 		n += f"{s}"
# 	print(n)

# k = input("\n\t\tTell me something\n\t\t")
# my_funktion(k)

# #Task5
# def reverse_funktion(a):
# 	j = ""
# 	m = len(a)
# 	for i in range(m-1,-1,-1):
# 		s = a[i]
# 		j += f"{s}"
# 	print(tuple(j))

# my_tuple = (1,2,3,2,5)
# reverse_funktion(my_tuple)



def my_funktion(m):
	k = ""
	n = m.split()
	n.reverse()
	for i in n:
		k += f" {i}"
	print(k)
k = input("Tell me something")
my_funktion(k)




