import random

text = "python"

original_dict = {}

for i in text:
	for j in str(random.randint(0,4)):
		original_dict[i] = j
	
print(original_dict)

new_dict = {}
n = []
for key,val in original_dict.items():
	if val not in n:
		n.append(val)
		new_dict[key] = val
print(new_dict)




