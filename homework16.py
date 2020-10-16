class Hotel:
	def __init__(self, hotel_name, place):
		self.hotel_name = hotel_name
		self.place = place
		self.rooms_mid = {"room1":"free", "room2":"free", "room3":"free"}
		self.mid_room_price = 10000
		self.rooms_lux = {"room1":"free", "room2":"free", "room3":"free"}
		self.lux_room_price = 20000
		self.new_room_mid = {}
		self.new_room_lux = {}
		self.new_room_mid1 = {}
		self.new_room_lux1 = {}
	
	def presentation(self):
		hotel_ = f"We are {self.hotel_name} hotel our location is {self.place}"
		return hotel_

	def check_mid(self):
		for i,m in self.rooms_mid.items():
			if m == "free":
				self.new_room_mid[i] = m
		return self.new_room_mid

	def check_lux(self):
		for j,k in self.rooms_lux.items():
			if k == "free":
				self.new_room_lux[j] = k
		return self.new_room_lux

	def booking_mid(self):
		for l,n in self.new_room_mid.items():
			if n == "free":
				self.new_room_mid1[l] = "busy"
		return self.new_room_mid1

	def booking_lux(self):
		for q,w in self.new_room_lux.items():
			if w == "free":
				self.new_room_lux1[q] = "busy"
		return self.new_room_lux1



class Taxi:
	def __init__(self, taxi_name, car_types):
		self.taxi_name = taxi_name
		self.car_types = car_types
		self.price_for_tour = 25000

	def presentation(self):
		taxi_ = f"We can suggest you our {self.taxi_name} taxi, we have {self.car_types} and our bill is {self.price_for_tour}"
		return taxi_


class Tour(Hotel, Taxi):
	def __init__(self, hotel_name, place, taxi_name, car_types)
	Hotel.__init__(self, hotel_name, place)
	Taxi.__init__(self, taxi_name, car_types)

def discount(self):
	price.lux = lux_room_price + price_for_tour
	price.mid = mid_room_price + price_for_tour
	return price.lux, price.mid

def presentation(self):
	text = f"We have two types of suggestion for the tour to {self.taxi_name}. Our lux suggest's bill is {self.price_lux} and mid is {self.price_mid}. You can travel with {self.car_types} and you will stay in {self.hotel_name}. Have a good Day."
