#Task1
def triangle_area(a, b):
	'''The area of a triangle is equal to half the multiplied of the base and height'''
	area = (a * b)/2
	print(f"\n\t\tTriangle's area is {area}")

side = int(input("\n\t\tTell me one side of triangle\n\t\t\t\t"))
height = int(input("\n\t\tTell me the height  of triangle\n\t\t\t\t"))
triangle_area(side, height)

#Task2
s = " "
word = input("\n\t\tTell me something and I'll reverse it\n\t\t\t\t")
'''We should know the lenght of the string, then reverse it with arranging it's indexes from the end to the beginning'''
lenn =len(word)
for i in range(lenn-1,-1,-1):
	m = word[i]
	s += f"{m}"
print(s)

#or second version with function
def reverse(k):
	s = " "
	lenn = len(k)
	for i in range(lenn-1,-1,-1):
		m = k[i]
		s +=f"{m}"
	print(s)

j = input("\n\t\tTell me something and I'll reverse it\n\t\t\t")
reverse(j)

#Task3
def letters(m):
	'''Upper case letters are numbered 65-90 and lower case letters are 97-122. With (ord) we campere their numbers'''
	k = len(m)
	z = 0
	n = 0
	for i in range(0,k):
			j = m[i]
			if 65 <= ord(j) <= 90:
				z +=1
			elif 97 <= ord(j) <= 122:
				n +=1
			else:
				pass
	print(f"\n\t\tThere are {z} upper case letters and {n} lower case latters")

k = input("\n\t\tTell me something and I'll calculate the number of upper case letters and lower case letters\n\t\t")
letters(k)


#Task4
def paliandrome(k):
	'''We need to compare the word from the beginning to the end and from the end to the beginning. We can do it with indexes'''
	s = ""
	c = ""
	m = len(k)
	for i in range(0,m):
 		n = k[i]
 		s += f"{n}"
	for j in range(m-1,-1,-1):
 		p = k[j]
 		c += f"{p}"
	if c == s:
 		print("\n\t\tIt's paliandrome")
	else:
 		print("\n\t\tIt isn't paliandrome")
 		

f = input("\n\t\tTell me a word and I'll say is it paliandrome or no\n\t\t\t\t")
paliandrome(f)

