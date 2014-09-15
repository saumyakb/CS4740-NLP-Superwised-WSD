from collections import defaultdict
import nltk
import pickle

beta=45

f=open('training_data.data','rb')
text=f.read()
lines=text.splitlines()
word_freq = defaultdict(int)
word_model=defaultdict(dict)
word_sense = defaultdict(dict)
total = len(lines)
sense = defaultdict(int)
pos_feature = defaultdict(dict)
bftext=[]
aftext=[]
text=[]
text0=[]
    

for line in lines:
    token = line.split(' | ')
    #making a dictionary of word frequecy
    if token[0] in word_freq:
        word_freq[token[0]]+=1    
    else:
        word_freq[token[0]]=1

    #making a dictionary of the number of times a word occures in a sense
    try:
        word_sense[token[1]][token[0]]+=1
        
    except:
        word_sense[token[1]][token[0]]=1

    try:
        word_model[token[0]][token[1]]+=1
        
    except:
        word_model[token[0]][token[1]]=1

for k in word_sense:
    sense[k]=sum((word_sense[k][w] for w in word_sense[k]))

for line in lines:
    token = line.split(' | ')
    text="<S> "+token[2]+" <E>"
    text = text.split(' %% ')
    if len(text[0].split(" "))<=2:
        tmp = nltk.pos_tag(text[2].split(" "))
        c1=tmp[0][1]
        c2=tmp[1][1]
        c3=tmp[2][1]
        c4=tmp[3][1]
    elif len(text[2].split(" "))<=2:
        tmp = nltk.pos_tag(text[0].split(" "))
        c1=tmp[-1][1]
        c2=tmp[-2][1]
        c3=tmp[-3][1]
        c4=tmp[-4][1]
    else:
        tmp = nltk.pos_tag(text[0].split(" "))
        c1=tmp[-1][1]
        c2=tmp[-2][1]
        tmp = nltk.pos_tag(text[2].split(" "))
        c3=tmp[0][1]
        c4=tmp[1][1]            
    try:
        pos_feature[token[1]]["c1-"+c1]+=1    
    except:
        pos_feature[token[1]]["c1-"+c1]=1
    try:
        pos_feature[token[1]]["c2-"+c2]+=1    
    except:
        pos_feature[token[1]]["c2-"+c2]=1
    try:
        pos_feature[token[1]]["c3-"+c3]+=1    
    except:
        pos_feature[token[1]]["c3-"+c3]=1
    try:
        pos_feature[token[1]]["c4-"+c4]+=1    
    except:
        pos_feature[token[1]]["c4-"+c4]=1

print "Training Completed"

p1 = open('wsense2.pkl', 'wb')
p2 = open('wfreq2.pkl', 'wb')
p3 = open('sense2.pkl', 'wb')
p4 = open('pos2.pkl', 'wb')
p5 = open('model2.pkl', 'wb')
pickle.dump(word_sense,p1)
pickle.dump(word_freq,p2)
pickle.dump(sense,p3)
pickle.dump(pos_feature,p4)
pickle.dump(word_model,p5)
p1.close()
p2.close()
p3.close()
p4.close()
p5.close()

    




