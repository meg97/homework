class HouseHeating:
	def __init__(self, room1, room2, room3, room4):
		self.room1 = room1
		self.room2 = room2
		self.room3 = room3
		self.room4 = room4

		self.goal_1 = 24
		self.goal_2 = 25
		self.goal_3 = 26
		self.goal_4 = 27
		self.room = 0

	def compare(self):
		if self.room1 == self.goal_1:
			self.room += 1	
		elif self.room1 < self.goal_1:
			print("You should increase the temperature of the first room")
		elif self.room1 > self.goal_1:
			print("You should make lower the temperature of the first room")
		
		if self.room2 == self.goal_2:
			self.room +=1
		elif self.room2 < goal_2:
			print("You should increase the temperature of the second room")
		elif self.room2 > self.goal_2:
			print("You should make lower the temperature of the second room")

		if self.room3 == self.goal_3:
			self.room += 1
		elif self.room3 < self.goal_3:
			print("You should increase the temperature of the third room")
		elif self.room3 > self.goal_3:
			print("You should make lower the temperature of the third room")
			
		if self.room4 == self.goal_4:
			self.room +=1
		elif self.room4 < self.goal_4:
			print("You should increase the temperature of the fourth room")
		elif self.room4 > self.goal_4:
			print("You should make lower the temperature of the fourth room")
		print(f"{self.room} of 4 have normal temperature, the rest you should change")
			

a = HouseHeating(26,25,26,27)
a.compare()