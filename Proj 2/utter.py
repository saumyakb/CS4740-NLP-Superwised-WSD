from collections import defaultdict
import nltk
import pickle

'''f=open('training_data.data','rb')
text=f.read()
lines=text.splitlines()
training=[]
f.close() 

for line in lines:
    features={}
    token = line.split(' | ')
    features["word"]=token[0]
    text="<S> "+token[2]+" <E>"
    text = text.split(' %% ')
    features["before"]=nltk.pos_tag(text[0].split(" "))[-1][1]
    features["after"]=nltk.pos_tag(text[2].split(" "))[0][1]
    training.append((features,token[1]))

classifier = nltk.NaiveBayesClassifier.train(training)
print "Training Completed"

f=open('validation_data.data','rb')
text=f.read()
lines=text.splitlines()
valid=[]
f.close()

for line in lines:
    features={}
    token = line.split(' | ')
    features["word"]=token[0]
    text="<S> "+token[2]+" <E>"
    text = text.split(' %% ')
    features["before"]=nltk.pos_tag(text[0].split(" "))[-1][1]
    features["after"]=nltk.pos_tag(text[2].split(" "))[0][1]
    valid.append((features,token[1]))

print nltk.classify.accuracy(classifier, valid)'''

p=open("good.pkl",'rb')
classifier=pickle.load(p)
p.close()
print "Model loaded"
f=open('test_data.data','rb')
w=open('nbsub.csv','wb')
w.write("id,prediction\n")
text=f.read()
lines=text.splitlines()
f.close()
lc=1

for line in lines:
    features={}
    token = line.split(' | ')
    features["word"]=token[0]
    text="<S> "+token[2]+" <E>"
    text = text.split(' %% ')
    features["before"]=nltk.pos_tag(text[0].split(" "))[-1][1]
    features["after"]=nltk.pos_tag(text[2].split(" "))[0][1]
    w.write(str(lc)+","+classifier.classify(features)+"\n")
    lc+=1
w.close()




