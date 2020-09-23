Employees = {
"emp1":{"name":"John","salary":7500},
"emp2":{"name":"Emma","salary":8000},
"emp3":{"name":"Brad","salary":6500}
}
m = 0
for i in Employees:
	if type(Employees[i]) == dict:
		for j in Employees[i]:
			k = Employees[i]
			m += k["salary"]
		m /=3
		Employees.uptade(m)
