import nltk
import sklearn
import numpy
import os
import pandas
import random
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, HashingVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC, SVC
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV
import math

##################
##DATA RETRIEVAL##
##################
tags = os.listdir('training_emails')

def get_stripped_filenames(categories):
    #gets a list of all pre-labled file names
    files = []
    for cat in [x for x in os.listdir(categories) if ".DS_Store" not in x]:
        for file in [x for x in os.listdir(categories + "/" + cat) if ".DS_Store" not in x]:
            uid = os.listdir(categories + "/" + cat + "/" + file)[0]
            if uid[0] == "t" or uid[0] == ".DS_Store":
                #removes .DS_Store or tickets with directory structure errors
                continue
            files.append((categories + "/" + cat + "/" + file + "/" + uid + "/" + "body_stripped.txt", cat))
            #adds the whole path to files
    random.shuffle(files)
    return files

def load_files(directory, stripped = None):
    if stripped == None:
        files = get_stripped_filenames(directory)
        #loads all files
    else:
        files = stripped
        #loads only specified files

    filedict = {"ticket": [], "tag": []}
    for i in files:
        #print(i[0])
        if ".DS_Store" in i[0]:
            continue
        file = open(i[0])
        filedict['ticket'].append(file.read())
        filedict['tag'].append(i[1])
        file.close()

    df = pandas.DataFrame.from_dict(filedict)
    #creates a dataframe with keys of df.ticket and df.tag
    return df


#############
##UTILITIES##
#############

def odd(n):
    if n % 2 == 0:
        return n + 1
    return n
    #returns n or n + 1, whichever is odd

def print_plot(index, df):
    example = df[df.index == index][['ticket', 'tag']].values[0]
    if len(example) > 0:
        print(example[0])
        print('Tag:', example[1])
    #prints index of df

###############
##CLASSIFIERS##
###############

def testmnnb(df):
    trainedx, testx, trainedy, testy = sklearn.model_selection.train_test_split(df.ticket, df.tag, test_size=.1)
    nb = Pipeline([('vect', CountVectorizer(ngram_range=(1,3), analyzer='word')),
                   ('tfidf', TfidfTransformer()),
                   ('clf', MultinomialNB(alpha=1)),
                  ])
    #Naive Bayes classifier using tfidf and ngrams
    nb.fit(trainedx, trainedy)

    y_pred = nb.predict(testx)
    d = accuracy_score(y_pred, testy)
    #print('accuracy %s' % d)
    #print(classification_report(testy, y_pred,target_names=tags))
    return d

def testbnb(df):
    trainedx, testx, trainedy, testy = sklearn.model_selection.train_test_split(df.ticket, df.tag, test_size=.1)
    nb = Pipeline([('vect', CountVectorizer(ngram_range=(1,3), analyzer='word')),
                   ('tfidf', TfidfTransformer()),
                   ('clf', BernoulliNB(alpha=1.0, binarize=0.0, class_prior=None, fit_prior=True)),
                  ])
    #Bernoulli Naive Bayes using tfidf and ngrams
    nb.fit(trainedx, trainedy)

    y_pred = nb.predict(testx)
    d = accuracy_score(y_pred, testy)
    #print('accuracy %s' % d)
    #print(classification_report(testy, y_pred,target_names=tags))
    return d

def testrf(df, split):
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform(df.ticket)
    trainedx, testx, trainedy, testy = sklearn.model_selection.train_test_split(df.ticket, df.tag, test_size=split)
    cls = Pipeline([('vect', CountVectorizer()),
                   ('chi', SelectKBest(chi2, k='all')),
                   ('clf', RandomForestClassifier(max_depth=32)),
                  ])
    #Random Forest clasisifer

    model = cls.fit(trainedx, trainedy)
    print("done")
    y_pred = cls.predict(testx)
    d = accuracy_score(y_pred, testy)
    #print('accuracy %s' % d)
    #print(classification_report(testy, y_pred,target_names=tags))
    return d

def trainlsvm(df):
    #Training function, returns the trained lsvm classifier
    trainedx, testx, trainedy, testy = sklearn.model_selection.train_test_split(df.ticket, df.tag, test_size=0)
    nb = Pipeline([('vect', CountVectorizer(ngram_range=(1,3), analyzer='word')),
                   ('tfidf', TfidfTransformer()),
                   ('clf', LinearSVC(class_weight="balanced")),
                  ])
    #LSvm Classifier using tfidf and ngrams
    model = nb.fit(trainedx, trainedy)
    return nb

def testlsvm(df, testsplit):
    trainx, testx, trainy, testy = sklearn.model_selection.train_test_split(df.ticket, df.tag, test_size=testsplit)
    nb = Pipeline([('vect', CountVectorizer(ngram_range=(1,2), analyzer='word')),
                   ('tfidf', TfidfTransformer()),
                   #('clf', LinearSVC(class_weight="balanced"))
                   ('clf-svm', SGDClassifier(class_weight="balanced", max_iter=1000, loss='hinge', penalty='l2'))
                  ])
    #LSvm Classifier using tfidf and ngrams
    model = nb.fit(trainx, trainy)
    #print(testy.tolist())
    predy = nb.predict(testx)
    d = accuracy_score(predy, testy)
    #print('accuracy %s' % d)
    #rint(classification_report(testy, y_pred,target_names=tags))
    return d

def testknn(df):
    #NOT FUNCTIONAL!
    trainx, testx, trainy, testy = sklearn.model_selection.train_test_split(df.ticket, df.tag, test_size=.1)
    vect = TfidfVectorizer(ngram_range=(1,3), analyzer="word")
    X = vect.fit_transform(trainx)
    knn = KNeighborsClassifier(n_neighbors=5, weights="distance")
    #K Nearest Neighbors Classifier, using tfidf and ngrams
    knn.fit(X,trainy)

    predy = knn.predict(vect.transform(testx))
    d = accuracy_score(predy, testy)
    return d

####################
##PARAMETER TUNING##
####################

def depth_tuningrf(df, r):
    #determines the best depth for rf
    results = []
    for i in range(1, r + 1):
        results.append((i, sum([testrf(df, i, 'all') for x in range(10)])/10))
    return results

def gridsearchsvm(df):
    #tests lots of different parameters to determine the best combination of parameters for svm
    params = {}
    params['clf__C'] = [1, 2, 3, 4, 10, 100]
    params['clf__penalty'] = ['l2']
    params['clf__loss'] = ['hinge', 'squared_hinge']
    #params['clf__dual'] = [False]
    params['vect__ngram_range'] = [(1,2), (1,3)]
    params['clf__fit_intercept'] = [True, False]

    #params['clf__degree'] = [1, 2, 3, 4, 5, 6]
    lsvm = Pipeline([('vect', CountVectorizer(ngram_range=(1,2), analyzer='word')),
                   ('tfidf', TfidfTransformer(sublinear_tf=True)),
                   ('clf', LinearSVC(class_weight="balanced")),
                  ])

    CV = GridSearchCV(lsvm, params, scoring = 'accuracy', n_jobs= 4)
    CV.fit(df.ticket, df.tag)

    print('Best score and parameter combination = ')

    print(CV.best_score_)
    print(CV.best_params_)

##################
##MAIN.PY COMPAT##
##################

def accuracy_test_lsvm(test, train):
    #compatability with main.py crsv
    lsvm = Pipeline([('vect', CountVectorizer(ngram_range=(1,3), analyzer='word')),
                   ('tfidf', TfidfTransformer(sublinear_tf=True)),
                   ('clf', LinearSVC(class_weight="balanced", C=2, loss="hinge", fit_intercept=False)),
                  ])

    traindataf = load_files('training_emails', train)
    testdataf = load_files('training_emails', test)

    model = lsvm.fit(traindataf.ticket, traindataf.tag)
    pred = lsvm.predict(testdataf.ticket)

    return accuracy_score(pred, testdataf.tag), [pred.tolist(), testdataf.tag.tolist()]

def accuracy_test_rf(test, train):
    #compatability with main.py crsv
    traindataf = load_files('training_emails', train)
    testdataf = load_files('training_emails', test)


    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform(traindataf.ticket)
    cls = Pipeline([('vect', CountVectorizer()),
                   ('chi', SelectKBest(chi2, k='all')),
                   ('clf', RandomForestClassifier(max_depth=100, n_estimators=32)),
                  ])

    model = cls.fit(traindataf.ticket, traindataf.tag)

    y_pred = cls.predict(testdataf.ticket)
    d = accuracy_score(y_pred, testdataf.tag)

    return d, [y_pred.tolist(), testdataf.tag.tolist()]


def accuracy_test(test, train):
    #compatability with main.py crsv
    traindataf = load_files('training_emails', train)
    cls = train(lsvm, traindataf)
    testdataf = load_files('training_emails', test)
    trainedx, testx, trainedy, testy = sklearn.model_selection.train_test_split(testdataf.ticket, testdataf.tag, test_size=1)

    pred = cls.predict(test)
    return accuracy_score(pred, testy), [pred, testy]

########
##MAIN##
########

if __name__ == "__main__":
    df = load_files('training_emails')
    #print(df.to_string())
    #print_plot(11, df)
    #gridsearchsvm(df)
    #print(depth_tuningr(df, 32))
    trials = 20

    #
    #   Tests a classifier with a train ratio over trials times
    #
    print("Multinomial Naive Bayes: ", str(sum([testmnnb(df) for x in range(trials)])/trials * 100) + "%")
    #print("Bernoulli Naive Bayes: ", str(sum([tesbnb(df) for x in range(trials)])/trials * 100) + "%")
    #print("Random Forest: ", str(sum([testrf(df, .5) for x in range(trials)])/trials * 100) + "%")
    #print("Random Forest: ", str(sum([testrf(df, .4) for x in range(trials)])/trials * 100) + "%")
    #print("Random Forest: ", str(sum([testrf(df, .3) for x in range(trials)])/trials * 100) + "%")
    #print("Random Forest: ", str(sum([testrf(df, .2) for x in range(trials)])/trials * 100) + "%")
    #print("Random Forest: ", str(sum([testrf(df, .1) for x in range(trials)])/trials * 100) + "%")

    #print("K Nearest Neighbors: ", str(sum([testknn(df) for x in range(trials)])/trials * 100) + "%")
    for z in [55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]:
        print(100 - z, "Multiclass SVM: ", str(sum([testlsvm(df, z/100) for x in range(trials)])/trials * 100) + "%")
