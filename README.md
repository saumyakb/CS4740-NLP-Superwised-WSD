CS4740-Natural-Language-Processing
==================================
Project 2
2 Supervised WSD
 2.1Approach:
 
1) In supervised WSD the first implementation was to configure a baseline. The baseline is the measure of the sense which occurs maximum number of times for a specific word. For example: the word end occurred maximum times in sense 1 and hence in the test data for every occurrence of the word end the sense predicted was 1.
This gave us an accuracy of 0.75884244373 on the validation set.
 
We made various dictionaries for the purpose of calculating the probability:
Word frequency: frequency of a given word occurring [word][frequency]
Word sense : the frequency of a sense occurring [sense][count]
A model (dictionary) was created for each word which kept a count of sense given word
word_model: [word][sense]
 
The next two methods involved using pos tagging.
 
2)In the second method the context considered for the word included the previous word and the next word.
Then pos tagging of the previous word and the next word in context was done. The dictionary looks like:
[word] [bf-pos tag of previous word]
[word] [af-pos tag of the next word]
 
The above features are used to calculate the probability of sense occurring given word using Bayes rule.
 

alpha2	Accuracy
1	0.768488745981
3	0.771704180064
25	0.787781350482
50	0.79421221865
100	0.8038585209
125	0.801714898178
200	0.802786709539
 
This method improved our accuracy on the validation function from the baseline.
 
Thus we decided to increase the pos tags of the context words of the words being considered for the feature set.
 
3)Thus we included the pos tags of two previous words and two following word in the training set. Hence making the dictionary look like
[word][bf_1][bf_2][af_1][af_2]
 
This when used to calculate the probability of the sense occurring given word and features gave a lower accuracy than the previous method which was opposite to what we had expected as having higher context should have helped the accuracy, the reason for this that the words occurring in a single sense have different kinds of pos tags. For eg:
Lead  1  [WDT][MD] [TO][NNS]
Lead  1  [IN] [NN] [TO][RBR]
 
In this example it is obvious that the same word in the same sense can occur with different pos tags in the previous and post context and in the previous method since the dictionary had a feature of splitting :- 
[lead] [to] 
[lead] [to] it would have marked both in sense 1.
 
4) The next method is a dictionary made using context word rather than pos tags. Which as expected gave poor results with the test and validation data. This is due to the fact that a word would not be surrounded with the same words just because it is in the same sense. Hence the dictionary is made
 
Software:

No software was used in the above approaches.
We only used the NLTK for the purpose of doing pos tagging.
The probabilities are being predicted using Bayes rule and various values were tried to figure out the smoothing factor.
 
 Results :
 
On the test set:
The best performance was given by the second method in which we had only the word and either a previous or prior word with pos tag.
The next best result was given by considering two prior and two previous post tags.
The next best result is with the fourth method using the previous two and next two context words.
The baseline is giving the lowest accuracy on the validation set.
 
We expect to get better results as we include more context to our features, however increasing context after a threshold may result in a drop in accuracy due to over fitting. We donot have equal number of examples for each class as a result the classes with more statistically prominent  features will have higher weightage as compared to other classes.
 
Method	Accuracy on Validation	Accuracy on Test set(Kaggle)
Baseline	0.75884244373	0.73124
Pos tag for one word	0.802786709539	0.78560
Pos tag for two words	0.78651220218	0.77795
Two context words	0.82109567362	0.74502
 
 
The effect of smoothing:
Smoothing is done as in the test data we might see features which are not present in the training data and in bayes algorithm coming across new features gives a zero probability; in order to avoid getting zeros a smoothing value is added. Smoothing is very sensitive to the data set. We observed that increasing values for smoothing factor increased the accuracy. This is because our data has a limited vocabulary and hence it makes more sense to have large values of alpha which even out the distribution and allows classes with not very informative features an equal chance to compete. The following table show the accuracy achieved with the change in smoothing factor.


alpha2	Accuracy
1	0.768488745981
3	0.771704180064
25	0.787781350482
50	0.79421221865
100	0.8038585209
125	0.801714898178
200	0.802786709539
 
Extension:
In our extension we have worked on studying the varying the size of training data on the accuracy of our system. With the appropriate smoothing these are the results observed on the validation set.
Training Data Size	Accuracy
20%	16.5
40%	33.7
60%	50.2
80%	76.4
100%	82.1

