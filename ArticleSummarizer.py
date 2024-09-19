# GUI
import tkinter as tk

# NLP
import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt_tab')

url = 'https://www.cbc.ca/news/world/secret-service-gunshots-trump-golf-club-1.7324106'

article = Article(url)

article.download()
article.parse()

# NLP without libraries involves complex mathematics and algorithms
article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')