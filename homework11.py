#Task1
dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50, 6:60}
dict4 = {6:50, 7:60}
list_dict = [dict1, dict2, dict3, dict4]
result = {}
for i in list_dict:
	for j in i:
		result[j] = i[j]
print(result)

#Task2
dict_ = {}
for i in range(1,6):
	dict_[i] = i * i
print(dict_)

#Task3 
original_dict = {"c1":"Red", "c2":"Green","c3":None}
new_dict = {}
for i in original_dict:
	if original_dict[i] != None:
		new_dict[i] = original_dict[i]		
		
print(new_dict)	

	
