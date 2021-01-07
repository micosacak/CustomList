from numpy import *
class CustomList:
	def __init__(self, *args):
		self.my_list = CustomList.get_list(args)
	def __getitem__(self, key = None):
		if key == None:
			return self.my_list
		return CustomList.getitem(self, key)
	def __setitem__(self, key, value):
		the_keys = CustomList.get_list(key)
		value = CustomList.get_list(value)
		the_min = min(the_keys)
		the_max = max(the_keys)
		if len(the_keys) != len(value):
			raise ValueError("the_length of the key ({}) must be equal to the length of the value ({})".format(len(the_keys), len(value)))
		if the_max >= len(self.my_list):
			diff = the_max - (len(self.my_list)-1)
			self.my_list.extend([0]*diff)
		ii = 0
		for idx in the_keys:
			self.my_list[idx] = value[ii]
			ii += 1
	def __delitem__(self, key):
		the_keys = CustomList.get_list(key)
		CustomList.check_keys(self, the_keys)
		for key in the_keys:
			if 0 <= key < len(self.my_list):
				del self.my_list[key]
			else:
				raise IndexError("Index error ...")
	def check_keys(self, the_keys):
		the_min = min(the_keys)
		the_max = max(the_keys)
		if the_min < 0 or the_max < 0:
			raise IndexError("the index cannot be negative value; the_min: {}, the_max: {} ".format(the_min, the_max))
		if type(the_min) in [str, float] or type(the_max) in [str, float]:
			raise IndexError("the index cannot be the_min: {} and the_max: {} values".format(type(the_min),type(the_max)))
		if the_max >= len(self.my_list):
			raise IndexError("the index ({}) cannot be bigger than the list length ({})".format(the_max,len(self.my_list)))
	def getitem(self, key):
		the_keys = CustomList.get_list(key)
		CustomList.check_keys(self, the_keys)
		res = []
		for x in the_keys:
			res.append(self.my_list[x])
		return res
	def get_list(values):
		my_list = []
		if type(values) in [range, slice]:
			the_start = values.start
			the_stop = values.stop
			the_step = values.step
			if the_start == None:
				the_start = 0
			if the_step == None:
				the_step = 1
			values = range(the_start, the_stop, the_step)
		if type(values) in [int, float, str]:
			my_list.append(values)
		elif type(values) in [range, slice]:
			for x in range(values.start, values.stop, values.step):
				my_list.append(x)
		else:
			for x in values:
				for y in CustomList.get_list(x):
					my_list.append(y)
		return my_list
	def get_values(self, *args):
		if len(args) == 0:
			return self.my_list
		if len(args[0]) == 0:
			return self.my_list
		else:
			return CustomList.getitem(self, args)
	def sum(self, *args):
		res = CustomList.get_values(self,args)
		return sum(res)
	def mean(self, *args):
		res = CustomList.get_values(self,args)
		return sum(res)/len(res)
	def len(self, *args):
		res = CustomList.get_values(self, args)
		return len(res)
	def var(self, *args):
		res = CustomList.get_values(self,args)
		mn = mean(res)
		return mean([(x-mn)**2 for x in res])
	def std(self, *args):
		res = CustomList.get_values(self,args)
		mn = mean(res)
		return sqrt(mean([(x-mn)**2 for x in res]))
	def __repr__(self):
		if isinstance(self.my_list, int):
			return str([self.my_list])
		return str(self.my_list)
