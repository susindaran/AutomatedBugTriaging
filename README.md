# Automated-Bug-Triaging-to-Developer
For popular software systems, the number of daily submitted bug reports is high. Triaging these incoming bugs is a time consuming task. Major part of bug triaging is the assignment of a bug report to a developer with the appropriate expertise, who can resolve/fix the bug without reassigning to some other developer. We present an approach to automatically suggest developers who have the appropriate expertise for handling a bug report based on the identified software component the bug may reside in, obtained from the short description of the bug report. Our work is first to examine the impact of multiple machine learning dimensions( classifiers and training history) along with the ranked list of developers for prediction accuracy in bug assignment. We validate our approach on Eclipse Bugzilla covering 2,868,000 bug reports consisting of 253 components. We demonstrate that our techniques can achieve up to 93% prediction accuracy in bug assignment and significantly reduce the aberrant assignment of bugs. We compared the prediction time for our dataset using various algorithms such as Naive Bayes Text Classifier, Multinomial Naive Bayes and Linear SVM. We arrived at a conclusion that SVM provides higher prediction time and less learning time.
