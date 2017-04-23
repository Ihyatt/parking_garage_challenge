
class Garage: 
	def __init__(self, rows, moto_spots, comp_spots, large_spots):
		self.rows = rows
		self.moto_spots = moto_spots
		self.comp_spots = comp_spots
		self.large_spots = large_spots
		self.capacity = self.rows * (self.moto_spots + self.comp_spots + self.large_spots)
		self.spaces_taken = 0 
		self.garage = {}
		self.populate_garage()

	def populate_garage(self):

		for i in range(self.rows):
			self.garage[i] = [self.moto_spots, self.comp_spots, self.large_spots]



	def park_vehicle(self, vehicle):
		if self.capacity == self.spaces_taken:
			return vehicle + " cannot be parked in this garage."

		if vehicle == "motorcycle":
			return self.find_moto_spots(vehicle)
		elif vehicle == "car":
			return self.find_comp_spots(vehicle)
		elif vehicle == "bus":
			return self.find_large_spots(vehicle)
		else:
			return vehicle + " cannot be parked in this garage."


	def find_moto_spots(self, vehicle):
		parked = False
		for i in range(self.rows):
			if self.garage[i][0] > 0:
				self.garage[i][0] -= 1
				self.spaces_taken += 1
				parked = True
				return vehicle + " has been parked."
		if parked == False:
			return self.find_comp_spots(vehicle)

	def find_comp_spots(self, vehicle):
		parked = False
		for i in range(self.rows):
			if self.garage[i][1] > 0:
				self.garage[i][1] -= 1
				self.spaces_taken += 1
				parked = True
				return vehicle + " has been parked."
		if parked == False:
			return self.find_large_spots(vehicle)

	def find_large_spots(self, vehicle):
		parked = False
		for i in range(self.rows):
			if vehicle == "bus":
				if self.garage[i][2] >= 5:
					self.garage[i][2] -= 5
					self.spaces_taken += 5
					parked = True
					return vehicle + " has been parked."
			else:
				if self.garage[i][2] > 0:
					self.garage[i][2] -= 1
					self.spaces_taken += 1
					parked = True
					return vehicle + " has been parked."

		if parked == False:
			return vehicle + " will not fit in this garage."


	def view_lot(self):
		print "Spaces Available:"
		for i in range(self.rows):
			print "level: " + str(i) + ": " + "Motorcycle Spaces " + str(self.garage[i][0]) + " Compact Spaces "+ str(self.garage[i][1]) + " Large Spots " + str(self.garage[i][2])




if __name__ == '__main__':
	lot = Garage(2, 2, 2 , 5)
	print lot.park_vehicle("motorcycle")
	print lot.park_vehicle("car")
	print lot.park_vehicle("bus")
	print lot.park_vehicle("motorcycle")
	print lot.park_vehicle("car")
	print lot.park_vehicle("bus")
	print lot.park_vehicle("motorcycle")
	print lot.park_vehicle("car")
	print lot.park_vehicle("bus")
	print lot.park_vehicle("motorcycle")
	print lot.park_vehicle("car")
	print lot.park_vehicle("bus")
	print lot.park_vehicle("motorcycle")
	print lot.park_vehicle("car")
	print lot.park_vehicle("bus")

	print lot.view_lot()


