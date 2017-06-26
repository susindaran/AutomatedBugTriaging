class TossingGraph:
	def __init__(self):
		self.developers = []
		self.graph = []
		pass

	def prepare_graph(self):

		file1 = open("OutputFiles/toss_data", "r")

		devs = set()
		for line in file1:
			parts = line.split(" , ")
			for part in parts:
				devs.add(part)
		self.developers = list(devs)
		file1.close()

		self.graph = [[0] * len(self.developers) for i in range(len(self.developers))]

		file1 = open("OutputFiles/toss_data", "r")
		for line in file1:
			parts = line.split(" , ")
			for i in range(0, len(parts) - 2, 1):
				self.graph[self.developers.index(parts[i])][self.developers.index(parts[i + 1])] += 1

		for i in range(0, len(self.developers), 1):
			sum1 = sum(self.graph[i])
			for j in range(0, len(self.developers), 1):
				if self.graph[i][j] != 0:
					self.graph[i][j] = float(float(self.graph[i][j]) / float(sum1))
		file1.close()

	def calculate_toss_possibility(self, developer):
		index = self.developers.index(developer)
		print max(self.graph[index])
		print self.graph[index].index(max(self.graph[index]))
		print "Max possibility is for tossing from " + self.developers[index] + " -> " + \
			self.developers[self.graph[index].index(max(self.graph[index]))]
