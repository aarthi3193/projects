# importing required libraries
import nltk 
from collections import Counter # for finding frequency of words
from wordcloud import WordCloud # for generating word cloud
import matplotlib.pyplot as plt # for generating an image or a graph

# reading the input file New York Times and remove end of line
NewString = open('DemocraticDebate_NYT.txt').read().replace('\n','').replace('\t','')
#print NewString
# reading the input file Wall Street Journal and remove end of line
NewString1 = open('DemocraticDebate_WSJ.txt').read().replace('\n','').replace('\t','')
#print NewString1



# opening the stopword file and reading it into a list
Stopword_List = open("stopwords_en.txt").read().splitlines()
stopword=[]
for x in Stopword_List:
    stopword.append(x.strip('\n')) 
    


# filtering out stop words for New york Times file and creating a list
Filtered_list = [word for word in NewString.lower().split() if word not in Stopword_List]
#print '\n------words in the text that are not stopwords (as a list):'
#print Filtered_list

 
# filtering out stop words for Wall Street Journal file and creating a list
Filtered_list1 = [word for word in NewString1.lower().split() if word not in Stopword_List]
# printing results
#print '\n------words in the text that are not stopwords (as a list):'
#print Filtered_list1

Filtered_string = ' '.join(Filtered_list)
#print '\n------words in the text that are not stopwords (as a string):',Filtered_string

Filtered_string1 = ' '.join(Filtered_list1)
#print '\n------words in the text that are not stopwords (as a string):',Filtered_string1


# extract tokens from the text
tokens = nltk.word_tokenize(Filtered_string) #for NYT file
tokens1 = nltk.word_tokenize(Filtered_string1) #for WSJ file



# calculate and print the most frequent words/tokens
freqdist = nltk.FreqDist(tokens).most_common(10)
print '\n------the 10 most frequent words are:'
print freqdist
# calculate and print the most frequent words/tokens
freqdist1 = nltk.FreqDist(tokens1).most_common(10)
print '\n------the 10 most frequent words are:'
print freqdist1


#Identifying the repeated words in the 2 top 10 words lists and adding them to the stopwords list
while 1>0:
    for i in Counter(Filtered_list).most_common(10):
        for j in Counter(Filtered_list1).most_common(10):
            if i[0] == j[0]:
                stopword.append(i[0])
                flag = 1; index = stopword.index(i[0])
    if flag == 1:
        flag = 0
        for k in stopword[index:]:
            while k in Filtered_list:
                Filtered_list.remove(k)
                while k in Filtered_list1:
                    Filtered_list1.remove(k)
    else: break
    




# calculate bigrams
bigrammed = list(nltk.bigrams(tokens)) #for NYT file
bigrammed1 = list(nltk.bigrams(tokens1)) #for WSJ file
# calculate and print the most frequent bigrams
freqdist2 = nltk.FreqDist(bigrammed).most_common(10)
print '\n------the most frequent bigramms are:'
print freqdist2

freqdist3 = nltk.FreqDist(bigrammed1).most_common(10)
print '\n------the most frequent bigramms are:'
print freqdist3

# creating an object with maximum no. of stop words as 2000 
wc = WordCloud(background_color="white", max_words=2000,stopwords=stopword)
# generating word cloud for each file and saving their image in NYT_file.png and WSJ_file.png
wc.generate(Filtered_string); wc.to_file("NYT_file.png")
plt.imshow(wc); plt.axis('off'); plt.show()

wc.generate(Filtered_string1); wc.to_file("WSJ_file.png")
plt.imshow(wc); plt.axis('off'); plt.show()

# Sentiment Analysis of NYT file is -24.9 depicting overall a negative tone of the article
# Sentiment Analysis of WSJ file is -11.4 depicting overall a negative tone of the article
