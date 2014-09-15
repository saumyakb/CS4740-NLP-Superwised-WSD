from collections import defaultdict
import nltk
f=open('training_data.data','rb')
text=f.read()
lines=text.splitlines()

bftext=[]
aftext=[]
text=[]
text0=[]

for line in lines:
    token = line.split(' | ')
    text =token[2].split(' %% ')
    posbf = nltk.pos_tag(text[0].split(".")[-1].split(" "))[-1][1]
    print text[1]
    posaf = nltk.pos_tag(text[2].split(".")[0].split(" "))[0][1]
    break
