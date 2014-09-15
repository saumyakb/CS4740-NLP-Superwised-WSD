from collections import defaultdict
import nltk
import pickle

beta=1000
def nb(ws,wf,s,w,pf,wm,af,bf,cf,df,alfa2):
    pws={}
    for num in wm[w]:
        pws[num] = (float(wm[w][num])/wf[w])                
        try:
            pws[num]*=(float(pf[num]["c1-"+af]+alfa2)/float(s[num]+len(wf)*alfa2))
        except:
            pws[num]*=(float(alfa2)/float(s[num]+len(wf)*alfa2))
        try:
            pws[num]*=(float(pf[num]["c2-"+bf]+alfa2)/float(s[num]+len(wf)*alfa2))
        except:
            pws[num]*=(float(alfa2)/float(s[num]+len(wf)*alfa2))
        try:
            pws[num]*=(float(pf[num]["c3-"+cf]+alfa2)/float(s[num]+len(wf)*alfa2))
        except:
            pws[num]*=(float(alfa2)/float(s[num]+len(wf)*alfa2))
        try:
            pws[num]*=(float(pf[num]["c4-"+df]+alfa2)/float(s[num]+len(wf)*alfa2))
        except:
            pws[num]*=(float(alfa2)/float(s[num]+len(wf)*alfa2))
    try:
        label=max(((pws[n],n) for n in pws))[1]
    except:
        label=max(s)
    return label  
        
    

def test(ws,wf,s,pf,wm,alfa2=beta):
    f1=open('test_data.data','rb')
    f3=open('Submission_nbTestw.csv','wb')
    val_text=f1.read()
    val_lines=val_text.splitlines()
    acc=0
    lc=0
    f3.write("id,prediction\n") 
    for line in val_lines:
        token = line.split(' | ')
        token[2]="<S> "+token[2]+" <E>"
        t_t =token[2].split(' %% ')
        if len(t_t[0].split(" "))<=2:
            tmp =t_t[2].split(" ")
            c1=tmp[0]
            c2=tmp[1]
            c3=tmp[2]
            c4=tmp[3]
        elif len(t_t[2].split(" "))<=2:
            tmp = t_t[0].split(" ")
            c1=tmp[-1]
            c2=tmp[-2]
            c3=tmp[-3]
            c4=tmp[-4]
        else:
            tmp = t_t[0].split(" ")
            c1=tmp[-1]
            c2=tmp[-2]
            tmp = t_t[2].split(" ")
            c3=tmp[0]
            c4=tmp[1]            
        val_label = nb(ws,wf,s,token[0],pf,wm,c1,c2,c3,c4,alfa2)
        if val_label==token[1]:
            acc+=1
        lc+=1
        f3.write(str(lc)+","+val_label+"\n") 
    return float(acc)/len(val_lines)
    f1.close()
    f3.close()



p1 = open('wsense3.pkl', 'rb')
p2 = open('wfreq3.pkl', 'rb')
p3 = open('sense3.pkl', 'rb')
p4 = open('pos3.pkl', 'rb')
p5 = open('model3.pkl', 'rb')
word_sense=pickle.load(p1)
word_freq=pickle.load(p2)
sense=pickle.load(p3)
pos_feature=pickle.load(p4)
word_model=pickle.load(p5)
p1.close()
p2.close()
p3.close()
p4.close()
p5.close()
print "Models Loaded"

#print max((i,test(word_sense,word_freq,sense,pos_feature,word_model,i)) for i in range(10000,100000,1000))
print test(word_sense,word_freq,sense,pos_feature,word_model)
    




