# -*- coding: utf-8 -*-

#AARTHI SHUNMUGAM -10411286
# Hw8  -Clinton emails

# In[2]:

import pandas as pd


# In[4]:
# reading the file into a pandas dataframe
df = pd.read_csv('H_Clinton-emails.csv')
df.head()


# In[44]:

# creating a list of stopwords from 'stopwords_en.txt' file
import csv
stopwords = []
with open('stopwords_en.txt', 'r') as file:
    stopword_reader = csv.reader(file)
    for word in stopword_reader:
        stopwords.append(word.pop())
        

RawText = df['RawText']
RawText_list = list(RawText)
cleaned_list =[]
#removing the stopwords from RawText and adding the remaining words into the cleaned list
for word in RawText_list:
    if word not in stopwords:
        cleaned_list.append(word)
        


# In[45]:

#Generating the word cloud for top words
 
import matplotlib.pyplot as plt
from wordcloud import WordCloud

bag_of_words_str = ",".join(map(str,cleaned_list))


wordcloud2 = WordCloud(max_words = 2000).generate(bag_of_words_str)
# Generate plot
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()


# In[46]:


#creating the list of senders
from collections import Counter
senders = df['MetadataFrom']
senders_list = list(senders)
# finding the top 15 senders
top15_senders = Counter(senders_list).most_common(17)
print ('The top 15 senders are:','\n', top15_senders)


# In[61]:
#visualization graphs for top senders 
df1 = pd.DataFrame({'count':df.groupby(['MetadataFrom']).size()}).reset_index()
df2 = df1.sort_values(['count'], ascending=False)[:15]
df2.plot(x="MetadataFrom", y=['count'], kind="bar")
plt.show() 


# In[ ]:




# In[ ]:



