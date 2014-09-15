from collections import defaultdict
import nltk
import pickle

beta=45

def nb(ws,wf,s,w,pf,af,bf,wm,alfa2):
    pws={}
    for num in wm[w]:
        pws[num] = (float(ws[num][w])/s[num])*(float(wm[w][num])/wf[w])                
        try:
            pws[num]*=(float(pf[num]["bf-"+bf]+alfa2)/float(s[num]+len(wf)*alfa2))
        except:
            pws[num]*=(float(alfa2)/float(s[num]+len(wf)*alfa2))
        try:
            pws[num]*=(float(pf[num]["af-"+af]+alfa2)/float(s[num]+len(wf)*alfa2))
        except:
            pws[num]*=(float(alfa2)/float(s[num]+len(wf)*alfa2))        
    label=max(((pws[n],n) for n in pws))[1]
    return label  
        
    

def test(ws,wf,s,pf,wm,alfa2):
    f1=open('test_data.data','rb')
    f2=open('test.csv','rb')
    val_text=f1.read()
    comt=f2.read().splitlines()
    val_lines=val_text.splitlines()
    acc=0
    lc=0
    for line in val_lines:
        token = line.split(' | ')
        token[2]="<S> "+token[2]+" <E>"
        t_t =token[2].split(' %% ')
        if t_t[0]!="<S> ":
            bff = nltk.pos_tag(t_t[0].split(".")[-1].split(" "))[-1][1]
        else:
            bff="<S>"
        if t_t[2]!=" <E>":
            aff = nltk.pos_tag(t_t[2].split(".")[0].split(" "))[0][1]
        else:
            aff="<E>"
        val_label = nb(ws,wf,s,token[0],pf,aff,bff,alfa2)
        if val_label==comt[lc].split(",")[1]:
            acc+=1
        lc+=1
    print float(acc)/len(val_lines)
    f1.close()
    f2.close()

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
    if text[0]!="<S>":
        posbf = nltk.pos_tag(text[0].split(".")[-1].split(" "))[-1][1]
    else:
        posbf = "<S>"
    try:
        pos_feature[token[1]]["bf-"+posbf]+=1    
    except:
        pos_feature[token[1]]["bf-"+posbf]=1
    if text[2]!="<E>":
        posaf = nltk.pos_tag(text[2].split(".")[0].split(" "))[0][1]
    else:
        posaf ="<E>"
    try:
        pos_feature[token[1]]["af-"+posaf]+=1     
    except:
        pos_feature[token[1]]["af-"+posaf]=1

print "Training Completed"

p1 = open('wsense.pkl', 'wb')
p2 = open('wfreq.pkl', 'wb')
p3 = open('sense.pkl', 'wb')
p4 = open('pos.pkl', 'wb')
p5 = open('model.pkl', 'wb')
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

    




