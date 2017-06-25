import nltk
from nltk.stem.porter import *
from nltk.corpus import stopwords


def stem_and_remove_stopwords():
	try:
		stop_words = stopwords.words('english')
		stemmer = PorterStemmer()

		input_file = open('OutputFiles/formatted_input')
		output_file = open('OutputFiles/stemmed_input.txt', 'w')

		final_lines = []

		# TODO: Split the lines and perform the stemming and stop-word removal in multiple threads
		for line in input_file:
			line = line.decode('utf-8')
			developer_split_index = line.rfind(" , ")
			for word in line[:developer_split_index].split():
				if word not in stop_words:
					final_lines.append("%s " % stemmer.stem(word))

			final_lines.append("{0}\n".format(line[developer_split_index+1:]))
		output_file.write(''.join(final_lines).encode('utf-8'))

		input_file.close()
		output_file.close()
	except LookupError:
		nltk.download('stopwords')
