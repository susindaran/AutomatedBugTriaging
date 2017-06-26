# Automated Bug Triaging to Developer
A Machine Learning Approach to automatically suggest potential developers for fixing a bug, based upon predicting the most probable software component in which the bug may reside in, using the extracted keywords from the bug description. The approach was validated on Eclipse Bugzilla, achieving up to 75% prediction accuracy in bug assignment, thus significantly reducing re-assignment of bugs. More details can be found in the [report](https://github.com/susindaran/AutomatedBugTriaging/raw/master/Report/AutomaticBugTriaging.pdf)




## Usage

Clone the repository and navigate to _***AutomatedBugTriaging/Code/***_ folder

```sh
$ git clone https://github.com/susindaran/AutomatedBugTriaging.git
$ cd AutomatedBugTriaging/Code/
$ python run.py
```

The dataset is present in the _***Dataset***_ directory.

## Dependencies
* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [pip](https://pip.pypa.io/en/stable/installing/)

#### Python packages

```sh
$ sudo pip install nltk
$ sudo pip install pandas
$ sudo pip install sklearn
$ sudo pip install scipy
$ sudo pip install matplotlib
```

### Intermediate files generated

* `formatted_input` - Consolidated input from different files into a format that is convenient to feed the classifier
* `stemmed_input` - After stemming and stop-word removal of input data
* `data.pkl` - Storage file for Panda's DataFrame object
* `toss_data` - Bug reassignment(tossing) information extracted from assignment history of bugs
