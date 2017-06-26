import nltk
from nltk.stem.porter import *
from nltk.corpus import stopwords


class Preprocessor:
	def __init__(self):
		try:
			self.stop_words = stopwords.words('english')
		except LookupError:
			nltk.download('stopwords')
			self.stop_words = stopwords.words('english')
		self.stemmer = PorterStemmer()

	def stem_and_stop(self, line):
		result = []
		for word in line.split():
			if word not in self.stop_words:
				result.append("%s " % self.stemmer.stem(word))
		return ''.join(result)

	def process_file(self):
		input_file = open('OutputFiles/formatted_input')
		output_file = open('OutputFiles/stemmed_input', 'w')

		final_lines = []

		# TODO: Split the lines and perform the stemming and stop-word removal in multiple threads
		for line in input_file:
			line = line.decode('utf-8')
			developer_split_index = line.rfind(" , ")
			final_lines.append(self.stem_and_stop(line[:developer_split_index]))
			final_lines.append("{0}".format(line[developer_split_index+1:]))
		output_file.write(''.join(final_lines).encode('utf-8'))

		input_file.close()
		output_file.close()
