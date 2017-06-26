from pandas import DataFrame
import numpy
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import KFold
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import SGDClassifier
from numpy import *
import matplotlib.pyplot as plt
from pylab import *
from sklearn.externals import joblib


def confusion_matrix(conf_arr, file_name):
	norm_conf = []
	for i in conf_arr:
		a = 0
		tmp_arr = []
		a = sum(i, 0)
		for j in i:
			tmp_arr.append(float(j) / float(a))
		norm_conf.append(tmp_arr)

	plt.clf()
	fig = plt.figure()
	ax = fig.add_subplot(111)
	res = ax.imshow(array(norm_conf), cmap = cm.jet, interpolation = 'nearest')
	for i, cas in enumerate(conf_arr):
		for j, c in enumerate(cas):
			if c > 0:
				plt.text(j - .2, i + .2, c, fontsize = 14)
	cb = fig.colorbar(res)
	savefig(file_name, format = "png")


class Classifier:
	def __init__(self, tossing_graph, developers, preprocessor):
		self.tossing_graph = tossing_graph
		self.developers = developers
		self.preprocessor = preprocessor

	def run(self):
		data = joblib.load('OutputFiles/data.pkl')

		df_new1, df_new2 = data[13344:], data[:13344]
		print "Training dataset :", len(df_new1)
		print "Testing Dataset :", len(df_new2)

		# Using pipeline and no bigram
		pipeline = Pipeline([
			('vectorizer', CountVectorizer()),
			('classifier', MultinomialNB())])
		pipeline.fit(numpy.asarray(df_new1['text']), numpy.asarray(df_new1['class']))
		# predicted=pipeline.predict(df_new2['text'])
		print "The accuracy for MultinomialNB is : ", pipeline.score(numpy.asarray(df_new2['text']),
																	numpy.asarray(df_new2['class']))
		# conf_arr=metrics.confusion_matrix(df_new2['class'], predicted)
		# print conf_arr
		# confusion_matrix(conf_arr,"mnb.png")

		# using bigram count and pipeline
		# pipeline = Pipeline([
		# ('count_vectorizer',   CountVectorizer(ngram_range=(1, 2))),
		# ('classifier',         MultinomialNB()) ])
		# pipeline.fit(numpy.asarray(df_new1['text']), numpy.asarray(df_new1['class']))
		# print "The accuracy using pipeline and bigram count for MultinomialNB is : ",pipeline.score(numpy.asarray(df_new2['text']), numpy.asarray(df_new2['class']))

		# cross validate using kfold =>folded into 10 samples
		pipeline = Pipeline([
			('count_vectorizer', CountVectorizer()),
			('classifier', MultinomialNB())])

		k_fold = KFold(n_splits = 10, shuffle = True)
		scores = []
		for train_indices, test_indices in k_fold.split(data):
			train_text = numpy.asarray(data['text'][train_indices])
			train_y = numpy.asarray(data['class'][train_indices])

			test_text = numpy.asarray(data['text'][train_indices])
			test_y = numpy.asarray(data['class'][train_indices])

			pipeline.fit(train_text, train_y)
			score = pipeline.score(test_text, test_y)
			scores.append(score)
		avg_score = sum(scores) / len(scores)
		print "The accuracy for Kfold MultinomialNB Classifier is : ", (avg_score)

		# Linear SVM Classifier
		# svm_clf = Pipeline([
		# 	('count_vectorizer', CountVectorizer()),
		# 	('classifier', SGDClassifier(loss = 'hinge', alpha = 1e-3, n_iter = 5))])
		# svm_clf.fit(numpy.asarray(data['text']), numpy.asarray(data['class']))
		# joblib.dump(svm_clf, 'OutputFiles/trained_data.pkl', compress = 9)
		# predicted = svm_clf.predict(df_new2['text'])
		# print "The accuracy of LinearSVM is : ", svm_clf.score(numpy.asarray(df_new2['text']),
		#                                                        numpy.asarray(df_new2['class']))

		# Give input here
		print ("Enter bug description : ")
		examples = [self.preprocessor.stem_and_stop(raw_input())]
		predictions = pipeline.predict(examples)
		# predictions = svm_clf.predict(examples)
		predictions.astype(int)
		print ("The predicted developer is : " + self.developers[int(predictions[0])])  # [1, 0]
		self.tossing_graph.calculate_toss_possibility(self.developers[int(predictions[0])])

	# conf_arr=metrics.confusion_matrix(df_new2['class'], predicted)
	# confusion_matrix(conf_arr,"svm.png")
