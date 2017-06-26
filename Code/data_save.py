from sklearn.externals import joblib
from pandas import DataFrame
import numpy


def save():
	f = open('OutputFiles/stemmed_input')
	pairs = []
	developers = set()

	for line in f:
		pair = line.decode('UTF-8').rstrip().rsplit(' , ', 1)
		if len(pair) == 2:
			developers.add(pair[1])
			pairs.append((pair[0], pair[1]))

	developers_list = list(developers)
	pairs = [(text, developers_list.index(developer)) for (text, developer) in pairs]

	data = DataFrame(pairs, columns = ['text', 'class'])

	data = data.reindex(numpy.random.permutation(data.index))
	joblib.dump(data, 'OutputFiles/data.pkl', compress = 9)

	f.close()

	return developers_list
