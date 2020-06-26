#ashwin baluja (azbxx) initial implementation of naive bayes
import os
import math
import operator
import random
from datetime import datetime

ids = {}
for cat in [x for x in os.listdir('training_emails') if ".DS_Store" not in x]:
        ids[cat] = [x.split("#")[-1].strip() for x in os.listdir('training_emails' + "/" + cat) if (x and ".DS_Store" not in x)]
#global variable with all the trained email ids

def ngramify(splitbody, n):
    #given a list of all the words in a body_stripped.txt, it splits it introductori
    #chunks of n size. For example, with n = 2, ['hi', 'my', 'name', 'is', 'ashwin']
    #would turn into ["hi my", "my name", "name is", "is ashwin"]
    output = []
    for i in range(len(splitbody)-n+1):
        output.append(" ".join(sorted(splitbody[i:i+n])))

    return output

def get_information(docs, cats, n):
    #takes in a list of all the file names of all the body_stripped.txt files
    #and a list of the categories. it then finds the frequency of each word in each
    #category, the number of tickets in each category, and the total number of words
    totalwordcount = 0

    wordCounts = {catname:{} for catname in cats}
    #creates a dict with the name of each category as key and a dict as the value
    categoryCounts = {catname:0 for catname in cats}
    #creates a dict with the name of each category as key and 0 as the value
    wordDocCounts = {}
    #creates an empty dict for the count of how many docs each word appears in
    for doc in docs:
        try:
            if '.DS_Store' in doc[0] or doc[0].count('ticket') > 1:
                #checks if it is .DS_Store, a hidden file on macos not related to the project
                #also checks for some incorrectly parsed tickets that created more than 1 ticket folder
                continue
            
            f = open(doc[0])
            words = ngramify(f.read().split(" "), n)
            #splits into ngrams
            f.close()
            for word in words:
                if word in wordCounts[doc[1]]:
                    wordCounts[doc[1]][word] += 1 / len(words)
                    #divides by len(words) to weight words less based on how long the document is
                else:
                    wordCounts[doc[1]][word] = 1 / len(words)
                categoryCounts[doc[1]] += 1
                totalwordcount += 1

            for word in list(set(words)):
                if word in wordDocCounts:
                    wordDocCounts[word] += 1
                else:
                    wordDocCounts[word] = 1

        except FileNotFoundError as e:
            print("FILE NOT FOUND")
            print(e)
            pass

    return wordCounts, categoryCounts, totalwordcount, wordDocCounts

def tf(word, fullbody):
    #tf is text frequency. it works on a per ticket basis,
    #and weights a word directly proportionally to how often it occurs
    numpresent = 0
    for i in fullbody:
        if word == i:
            numpresent += 1
    #counts the number of times the word appears in the doc

    return numpresent/len(fullbody)
    #return math.log(numpresent + 1)


def idf(word, wordcounts, num, worddoccounts, doccount):
    #idf is inverse document frequency. it works looking
    #at every document. it weights a word less based on how many documents it
    #appears in.

    return math.log(doccount/(worddoccounts[word] + 1))

def tfidf(word, wordcounts, fullbody, worddoccounts, doccount):
    #combines tf and idf by multiplying them
    numcats = len(list(wordcounts.keys()))
    return tf(word, fullbody) * idf(word, wordcounts, numcats, worddoccounts, doccount)

def classify(bodytext, wordcounts, totalwordcount, catcounts, cats, smoothingm, smoothingp, n, worddoccounts, numdocs):
    #this is the function that actually classifies them
    catscores = {catname: 0 for catname in cats}
    vocab = set(sum([[x for x in wordcounts[x]] for x in wordcounts], []))
    #generates a dict with each category set to 0 at the beginning
    words = [] + ngramify(bodytext.split(" "), n) #+ ngramify(bodytext.split(" "), 1) + ngramify(bodytext.split(" "), 2)
    #splits the doc into ngrams of n size

    for i in words:
        print(i, 'word')
        for x in catscores:
            try:
                if i in wordcounts[x]:
                    tfidfval = tfidf(i, wordcounts, words, worddoccounts, numdocs)
                    #computes tfidf

                    #print(i, x, ": ", wordcounts[x][i], len(wordcounts[x]), len(vocab), tfidfval)
                    catscores[x] -= math.log((wordcounts[x][i] + 100)/(len(wordcounts[x]) + len(vocab)))# + math.log(tfidfval)
                    #using + 100 here because a larger number seemed to increae performance
                    #i expected + 1 to be the best as that would make sense, but performance says otherwise
                #this is the actual naive bayes right here. im using logs
                #to keep the numbers at a reasonable size, as they were
                #really tiny before. also, it allows me to add them instead of
                #multiplying them
            except Exception as e:
                #print('wordnotfound\n\n\n\n\n\n\n')
                print(str(e), 'error')

                pass
    for i in catscores:
        x = math.log(catcounts[i]/sum(catcounts.values())) #* 10
        catscores[i] -= x
        #catcounts[i]/totalwordcount is the probability of any document being in
        #that category. i add .000...1 to it to prevent errors with the log of 0
    return max(catscores, key=catscores.get), sorted(catscores.items(), key=operator.itemgetter(1), reverse=True)

def check_category(emailuid, ids):
    #given a uid, if finds the category it belongs to

    for i in ids:
        if emailuid in ids[i]:
            return i

def get_categorized_ids(categories):
    #gets a list of all the pre-labled files ids
    files = []
    cats = []
    for cat in [x for x in os.listdir(categories) if ".DS_Store" not in x]:
        cats.append(cat)
        files += [x.split("#")[-1].strip() for x in os.listdir(categories + "/" + cat) if (x and ".DS_Store" not in x)]

    return files, cats

def get_stripped_filenames(categories):
    #gets a list of all pre-labled file names
    files = []
    for cat in [x for x in os.listdir(categories) if ".DS_Store" not in x]:
        for file in [x for x in os.listdir(categories + "/" + cat) if ".DS_Store" not in x]:
            uid = os.listdir(categories + "/" + cat + "/" + file)[0]
            files.append((categories + "/" + cat + "/" + file + "/" + uid + "/" + "body_stripped.txt", cat))

    return files

def auto_classify(email_directory, output_directory):
    #essentially just a wrapper for the classify function to make it work with
    #what the last group expected this file to do.
    filesSkipped = []
    files = os.listdir(email_directory)
    a = open("data/wordcounts.txt" , 'r')
    wc = eval(a.read())
    a.close()
    b = open("data/categorycounts.txt", 'r')
    cc = eval(b.read())
    b.close()
    c = open('data/totalwords', 'r')
    tw = eval(c.read())
    c.close()
    #this section reads all the trained data, which is just the information generated
    #by get_information
    for i in files:
        #runs for every file in the email directory
        try:
            #print(i)
            uid = os.listdir(email_directory + "/" + i)
            name = email_directory + "/" + i + "/" + uid[0] + "/body_stripped.txt"
            #print(name)
            f = open(name)
            result, info = classify(f.read(), wc, tw, cc, [x.split(".")[0] for x in os.listdir('training_emails')], 1, .5, 3)
            #print(email_directory + "/" + i, output_directory + "/" + result + "/" + i)
            os.rename(email_directory + "/" + i, output_directory + "/" + result + "/" + i)
            #moves each ticket into a classified directory
        except Exception as e:
            filesSkipped.append(i)
            #print(str(e))
    return filesSkipped

    #classify(bodytext, wordcounts, totalwordcount, catcounts, cats, smoothingm, smoothingp, n):
def train(n, files = None):
    #gets all the file data it needs, then writes the results from get_information to a file
    nvalue = n
    categorized, categories= get_categorized_ids('training_emails')
    strippedfiles = get_stripped_filenames('training_emails')
    emails = []
    if files == None:
        for i in os.listdir("training_emails"):
            for x in os.listdir('training_emails/' + i):
                emails.append("training_emails/" + i + "/" + x)
    else:
        emails = files

    random.shuffle(emails)
    numfiles = len(emails)
    filestotrain = numfiles
    files = [x for x in emails[0:filestotrain]]

    wordcounts, categorycounts, totalwords, worddoccounts = get_information(strippedfiles, categories, nvalue)
    f = open("data/wordcounts.txt" , 'w+')
    f.write(str(wordcounts))
    f.close()
    f = open("data/categorycounts.txt", 'w+')
    f.write(str(categorycounts))
    f.close()
    f = open('data/totalwords', 'w+')
    f.write(str(totalwords))
    f.close()
    f = open('data/worddoccounts', 'w+')
    f.write(str(worddoccounts))
    f.close()
    #writes all the information to file

def testitout(n, trainpercent=90):
    global ids
    #simple way to run it on already classified information to test if it worksself.
    #by default, it trains on 90% of the data, and tests on the other 10% of it.
    nvalue = n
    categorized, categories= get_categorized_ids('training_emails')
    #print(categorized, categories)
    strippedfiles = get_stripped_filenames('training_emails')
    random.shuffle(strippedfiles)

    numfiles = len(strippedfiles)
    filestotrain = math.ceil(numfiles / 100 * trainpercent)

    wordcounts, categorycounts, totalwords, worddoccounts = get_information(strippedfiles[0:filestotrain], categories, nvalue)
    correct, incorrect, total = 0, 0, 0
    for i in strippedfiles[filestotrain:]:
        #print(i)
        try:
            filename = i[0]
            text = open(filename)
            body = text.read()
            #print(body)

            predicted, extras = classify(body, wordcounts, totalwords, categorycounts, categories, 1, .5, nvalue, worddoccounts, numfiles)
            #print(extras, 'HERE')


            expected = check_category(i[0].split("/")[-3].split("#")[-1], ids)
            if predicted == expected:
                correct += 1
                total += 1
            else:
                incorrect += 1
                total += 1

            text.close()
        except Exception as e:
            print(e)
            pass
            #print(str(e))
    #print("CORRECT:" + str(correct))
    #print("INCORRECT:" + str(incorrect))
    #print(str(correct/(numfiles - filestotrain)) + "% CORRECT")
    return correct/total

def evaluate(trainpercent, trials = 100, n = 2):
    #evaluates the performance of the algorithm by running it trials amount of times
    #with n sized ngrams
    finalresults = []
    for perc in trainpercent:
        results = []
        for _ in range(trials):
            d = testitout(n, perc)
            results.append(d)
            print(d)

        finalresults.append(sum(results)/len(results))
        print(finalresults)

    return finalresults

def determineNgram(trials = 1):
    #used to determine the best size for ngrams. the answer is 3
    results = [evaluate([90], trials, x) for x in range(1,11)]
    print(results)

def accuracy_test(testing_emails, n):
    a = open("data/wordcounts.txt" , 'r')
    wc = eval(a.read())
    a.close()
    b = open("data/categorycounts.txt", 'r')
    cc = eval(b.read())
    b.close()
    c = open('data/totalwords', 'r')
    tw = eval(c.read())
    c.close()
    d = open('data/worddoccounts', 'r')
    wdc = eval(d.read())
    d.close()
    correct,total = 0, 0
    predicted = []
    actual = []
    for i in testing_emails:
        print(i)
        try:
            f = open(i[0], 'r')
            result, info =  classify(f.read(), wc, tw, cc, [x for x in os.listdir('training_emails')], 1, .5, n, wdc, len(wdc))
            print(info)
            f.close()
            print(i)
            answer = i[1]
            print(result, answer)
            if result == answer:
                correct += 1
                print('correct', correct)
                print(total)
            else:
                print('incorrect')
            total += 1
            predicted.append(answer)
            actual.append(result)
        except Exception as e:
            print(str(e), 'ERROR')
    print(correct, total)
    print(str(correct/total * 100) + "%")
    return correct/total, [predicted, actual]

#determineNgram()
#print(sorted(evaluate([45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95], 5, 2)))

#print(sorted(evaluate([90], 5, 2)))

#PROCEDURE TO RUN
#Use evaluate() when testing. runs trials amount of times, over n train/test split ratios in []. 
#Use auto_classify() to classify unlabled data. first call train() to train on all labled data