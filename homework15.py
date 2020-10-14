class Country:
	def __init__(self, country_name, continent):
		self.country_name = country_name
		self.continent = continent

	def country_presentation(self):
		country_ = f"This brand is produced in {self.country_name} it's in {self.continent}"
		return(country_)


class Brand:
	def __init__(self, brand_name, start_date):
		self.brand_name = brand_name
		self.start_date = start_date

	def brand_presentation(self):
		brand_ = f"The name of this brand is {self.brand_name} it has been sold since {self.start_date}"
		return(brand_)


class Season:
	def __init__(self, season_name, temperature):
		self.season_name = season_name
		self.temperature = temperature


	def season_presentation(self):
		season_ = f"This brand is useful espacialy in {self.season_name} You can use it during the temperature {self.temperature}"
		return(season_)


class Product(Country, Brand, Season):
	def __init__(self, country_name, continent, brand_name, start_date, season_name, temperature, product_name, product_type, price, quantiy):
		Country.__init__(self, country_name, continent)
		Brand.__init__(self, brand_name, start_date)
		Season.__init__(self, season_name, temperature)
		self.product_name = product_name
		self.product_type = product_type
		self.price = price
		self.quantiy = quantiy


	def product_presentation(self):
		product_ = f"We want to present the new product of the brand {self.brand_name} which produced in the country {self.country_name} of {self.continent} continent since the year {self.start_date}. So our new product is {self.product_name} we can say it's type is {self.product_type}. You can use it in {self.season_name} during the temperature {self.temperature}. It's price is only {self.price} AMD and there is limited quantiy: only {self.quantiy} we have"
		return(product_)


	def discont(self):
		self.percent = input("Tell me the percent\n\t")
		new_price = self.price * int(self.percent) / 100
		return(new_price)


	def increase(self):
		self.quantity_1 = input("Tell me how many of this product do you want to increase?\n\t")
		new_quantity = self.quantiy + int(self.quantity_1)
		return(f"We can increase the quantity and send you {new_quantity} of this product")


	
