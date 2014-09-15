from collections import defaultdict
import nltk
import pickle

beta=1000
def nb(ws,wf,s,w,pf,af,bf,wm,alfa2):
    pws={}
    for num in wm[w]:
        pws[num] = (float(wm[w][num])/wf[w])                
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
        
    

def test(ws,wf,s,pf,wm,alfa2=beta):
    f1=open('test_data.data','rb')
    f3=open('Submission_nbTest2'+str(beta)+'.csv','wb')
    val_text=f1.read()
    f3.write("id,prediction\n") 
    val_lines=val_text.splitlines()
    acc=0
    lc=0
    for line in val_lines:
        token = line.split(' | ')
        token[2]="<S> "+token[2]+" <E>"
        t_t =token[2].split(' %% ')
        if t_t[0]!="<S>":
            bff = nltk.pos_tag(t_t[0].split(".")[-1].split(" "))[-1][1]
        else:
            bff="<S>"
        if t_t[2]!="<E>":
            aff = nltk.pos_tag(t_t[2].split(".")[0].split(" "))[0][1]
        else:
            aff="<E>"
        val_label = nb(ws,wf,s,token[0],pf,aff,bff,wm,alfa2)
        if val_label==token[1]:
            acc+=1
        lc+=1
        f3.write(str(lc)+","+val_label+"\n") 
    return float(acc)/len(val_lines)
    f1.close()
    f3.close()



p1 = open('wsense.pkl', 'rb')
p2 = open('wfreq.pkl', 'rb')
p3 = open('sense.pkl', 'rb')
p4 = open('pos.pkl', 'rb')
p5 = open('model.pkl', 'rb')
word_sense=pickle.load(p1)
word_freq=pickle.load(p2)
sense=pickle.load(p3)
pos_feature=pickle.load(p4)
word_model=pickle.load(p5)
p1.close()
p2.close()
p3.close()
print "Models Loaded"
test(word_sense,word_freq,sense,pos_feature,word_model)
    




