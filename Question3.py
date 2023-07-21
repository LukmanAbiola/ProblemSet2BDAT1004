class Marsupial:
	def __init__(self):
		self.pouch_list = list()
	def put_in_pouch(self, pouch_item):
		self.pouch_list.append(pouch_item)
	def pouch_contents(self):
		return self.pouch_list

class Kangaroo(Marsupial):
	def __init__(self , x_coord, y_coord):
		super().__init__()
		self.x_coord = x_coord
		self.y_coord = y_coord
	def jump(self, dx, dy):
		self.x_coord += dx
		self.y_coord += dy
	def __str__(self):
		return "I am a Kangaroo located at coordinates (" + str(self.x_coord) + ","+ str(self.y_coord) + ")"