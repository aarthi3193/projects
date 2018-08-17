# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import urllib as ulibr
from operator import itemgetter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv
#defining the grade score categories into dictionary
grade_dict = {"A+" : 1, "A" : 0.96, "A-" : 0.92, "B+" : 0.89, "B" : 0.86, "B-" : 0.82, 
            "C+" : 0.79, "C" : 0.76, "C-" : 0.72, "D+" : 0.69, "D" : 0.66, "D-" : 0.62}

#reading the html file from the rottentomatoes.com movie page source
html = ulibr.urlopen("https://www.rottentomatoes.com/m/the_star_2017/reviews/")

#loading the page into the beautiful soup
soup = BeautifulSoup(html,'lxml')

#identifying the total number of pages
Number_pages = soup.find('span',{'class':re.compile('pageInfo')}).text.strip().split(' ')[3]
present_page = 1

#creating a list of ratings from each review for the movie
rw_score = []
#Loop through each page creating a new soup every time
while present_page <= int(Number_pages):
    
    html = ulibr.urlopen("https://www.rottentomatoes.com/m/the_star_2017/reviews/?page="+
                      str(present_page))
    soup = BeautifulSoup(html,'lxml')
#collecting the reviews
    reviews = soup.findAll('div',{'class':re.compile('review_desc')})
    for review in reviews:
        rev = review.find('div',{'class':re.compile('the_review')}).text.strip() 
#collecting the ratings
        try:
            rating = review.find('div',{'class':re.compile('small subtle')}).text.strip() 
            if "Original Score" in rating:
                rating = re.split('[|:/]',rating)
                rating = float(rating[2].strip())/float(rating[3].strip())
            else: continue
        except:
#            print("Rating tag not found")
            continue
        rw_score.append([rev, rating]) #adding the reviews and ratings to the list
    present_page += 1 #incrementing the page
    
#sorting the list of reviews based on ratings to find the top 20 reviews
rev_score = sorted(rw_score, key=itemgetter(1), reverse = True)
top_20 = rev_score[:20]
print("Top 20 reviews:\n", rev_score[:20])

#sorting the sorted list again to find the bottom 20 reviews
rev_score = sorted(rev_score, key=itemgetter(1))
bottom_20 = rev_score[:20]
print("Bottom 20 reviews:\n", rev_score[:20])

#creating word cloud 1 for top 20 reviews

stopwords = []
with open('stopwords_en.txt', 'r') as file:
    stopword_reader = csv.reader(file)
    for word in stopword_reader:
        stopwords.append(word.pop())
        
wclist=[]
for review in top_20:
    words = review[0].split(' ')
    for word in words:
        if word not in stopwords:
            wclist.append(word)    
wc = WordCloud(max_words=20)
wc.generate(" ".join(wclist)); wc.to_file("wordcloud file.png")
plt.imshow(wc); plt.axis('off'); plt.show()

#creating word cloud 2 for bottom 20 reviews
wclist_b = []
for review in bottom_20:
    words = review[0].split(' ')
    for word in words:
        if word not in stopwords:
            wclist_b.append(word)    
wc = WordCloud(max_words=20)
wc.generate(" ".join(wclist_b)); wc.to_file("wordcloud file1.png")
plt.imshow(wc); plt.axis('off'); plt.show()
