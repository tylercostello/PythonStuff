import os
import re

def addtoemailssubject():
    pattern = r'Subject:(.*)'
    for dir in os.listdir('emails'):
        uid = os.listdir('emails/' + dir)[0]
        f = open('emails/{}/{}/body.txt'.format(dir, uid), 'r')
        subject = re.findall(pattern, f.read())
        f.close()
        subjecttoadd = " ".join(subject[0].split(" ") * 2)
        f = open('emails/{}/{}/body.txt'.format(dir, uid), 'a')
        f.write(" " + subjecttoadd)
        f.close()

def addtocategorized():
    #Adds the subject to the body_stripped files. Didn't end up being useful.
    pattern = r'Subject:(.*)'
    for dir in [x for x in os.listdir('training_emails') if ".DS_Store" not in x]:
        for ticket in [x for x in os.listdir('training_emails/{}'.format(dir)) if ".DS_Store" not in x]:
            try:
                uid = [x for x in os.listdir('training_emails/{}/{}'.format(dir, ticket)) if ".DS_Store" not in x][0]
                f = open('training_emails/{}/{}/{}/body.txt'.format(dir, ticket, uid), 'r')
                subject = re.findall(pattern, f.read())
                f.close()
                subjecttoadd = " ".join(subject[0].split(" ") * 2)
                f = open('training_emails/{}/{}/{}/body_stripped.txt'.format(dir, ticket, uid), 'a')
                f.write(" " + subjecttoadd)
                f.close()
            except:
                pass

def create_categoryfiles(catdir, traindir):
    #Recreates the categories directory given training_emails directory
    for cat in [x for x in os.listdir(traindir) if x[0] != "."]:
        ids = [x.split("#")[1] for x in os.listdir(traindir + "/" + cat) if x.strip()]
        f = open(catdir + '/' + cat, 'w+')
        f.write("\n".join(ids))
        f.close()

addtocategorized()