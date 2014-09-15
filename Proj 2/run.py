from collections import defaultdict
import nltk
import re
text='''Adult beavers have long flat tails that are about a foot long. Beavers slap their tails on the water surface as an alarm to alert the colony when they sense danger. Female beavers are larger than male beavers of the same age. Prior to European immigration there were over 60 million beavers in North America. Due primarily to over trapping beavers were an endangered species in the early part of the 20th Century. Beavers are very active on Pinterest and often are considered social media mavens. '''
word_freq = defaultdict(int)
text = re.sub("[^a-zA-Z]", " ", text)

tokens= text.split(" ")
for token in tokens:
    if token in word_freq:
        word_freq[token]+=1
    else:
        word_freq[token]=1
        

