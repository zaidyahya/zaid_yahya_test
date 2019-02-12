class VersionComparator:
	def __init__(self, v1, v2):
		self.v1 = v1;
		self.v2 = v2;
		self.flag = 0;

		x1 = self.v1.split('.')
		x2 = self.v2.split('.')

		m = max(len(x1), len(x2));

		x1 = x1 + [0] * (m-len(x1))
		x2 = x2 + [0] * (m-len(x2))
		
		for i in range(m):
			if(int(x1[i]) > int(x2[i])):
				self.flag = 1
				break
			elif(int(x1[i]) < int(x2[i])):
				self.flag = -1
				break

	def compare(self):
		if self.flag == 1:
			return 	"{0} is greater than {1}".format(self.v1, self.v2)
		elif self.flag == -1:
			return "{0} is lesser than {1}".format(self.v1, self.v2)
		else:
			 return "{0} is equal to {1}".format(self.v1, self.v2)