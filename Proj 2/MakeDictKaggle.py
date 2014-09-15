from collections import defaultdict
import nltk

alfa=3
alfa2=0.00005
def nb(ws,wf,s,w):
    pws={}
    for num in s:
        try:
            pws[num] = (float(ws[num][w]+alfa)/float(wf[w]+len(wf)*alfa))*(float(s[num])/total)
            #print pws[num]
        except:
            pws[num] = (float(alfa)/float(len(wf)*alfa))*(float(s[num])/total)
            #print pws[num]
    label=max(((pws[n],n) for n in pws))[1]
    return label

def nb(ws,wf,s,w,pf,af,bf):
    pws={}
    for num in s:
        try:
            pws[num] = (float(ws[num][w]+alfa)/float(wf[w]+len(wf)*alfa))*(float(s[num])/total)
            #print pws[num]
        except:
            pws[num] = (float(alfa)/float(len(wf)*alfa))*(float(s[num])/total)
            #print pws[num]
        try:
            pws[num]*=(float(pf[num]["bf-"+bf]+alfa2)/float(s[num]+len(wf)*alfa2))
        except:
            pws[num]*=(float(alfa2)/float(s[num]+len(wf)*alfa2))
        try:
            pws[num]*=(float(pf[num]["af-"+bf]+alfa2)/float(s[num]+len(wf)*alfa2))
        except:
            pws[num]*=(float(alfa2)/float(s[num]+len(wf)*alfa2))        
    label=max(((pws[n],n) for n in pws))[1]
    return label  
        
    

def test(ws,wf,s,pf):
    f1=open('validation_data.data','rb')
    #f2=open('test_data.csv','w')
    val_text=f1.read()
    val_lines=val_text.splitlines()
    acc=0

    for line in val_lines:
        token = line.split(' | ')
        t_t =token[2].split(' %% ')
        if t_t[0]!="<S>":
            bff = nltk.pos_tag(t_t[0].split(".")[-1].split(" "))[-1][1]
        else:
            bff="<S>"
        if t_t[2]!="<\S>":
            aff = nltk.pos_tag(t_t[2].split(".")[0].split(" "))[0][1]
        else:
            aff="<\S>"
        val_label = nb(ws,wf,s,token[0],pf,aff,bff)
        #f2.write(token[0]+" | "+val_label+" | "+token[2])
    #f1.close()
    #f2.close()
    #print "Done"
    
        

        if val_label==token[1]:
            acc+=1
    print float(acc)/len(val_lines)
    
f=open('training_data.data','rb')
text=f.read()
lines=text.splitlines()
word_freq = defaultdict(int)
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

for k in word_sense:
    sense[k]=sum((word_sense[k][w] for w in word_sense[k]))

for line in lines:
    token = line.split(' | ')
    text="<S> "+token[2]+" <\S>"
    text = text.split(' %% ')
    if text[0]!="<S>":
        posbf = nltk.pos_tag(text[0].split(".")[-1].split(" "))[-1][1]
    else:
        posbf = "<S>"
    try:
        pos_feature[token[1]]["bf-"+posbf]+=1    
    except:
        pos_feature[token[1]]["bf-"+posbf]=1
    if text[2]!="<\S>":
        posaf = nltk.pos_tag(text[2].split(".")[0].split(" "))[0][1]
    else:
        posaf ="<\S>"
    try:
        pos_feature[token[1]]["af-"+posaf]+=1     
    except:
        pos_feature[token[1]]["af-"+posaf]=1

print "Training Completed"
test(word_sense,word_freq,sense,pos_feature)
    




