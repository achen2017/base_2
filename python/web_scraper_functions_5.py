#### This version only picks up the first 100 words of text
from bs4 import BeautifulSoup
import requests
import json
import time
from google import search
from google import search_news
from google import get_page
from random import randint
from nltk.corpus import stopwords
import re

ops = 'ops'
stop_limit = 5
def rando():
    rando_num = randint(0 , 329)/101
    return rando_num


def wordlist(article_text):
    letters_only = re.sub("[^a-zA-Z]", " ", article_text)
    lower_case = letters_only.lower()
    full_wordset = lower_case.split(' ')
    if len(full_wordset) > 100:
        n = 100
    else:
        n = len(full_wordset)
    article_words = [w for w in full_wordset[0:n] if w not in stopwords.words("english") and w not in ['', ' '] and len(w) > 1]

    return article_words






########Extract article_title
def get_title_nyt(article_request):
    article_soup = BeautifulSoup(article_request.text,'html.parser')
    article_title = ''
    try:
        article_title = article_soup.find("h1", {"class" : 'headline'}).text
    except AttributeError:
        print(ops)
    return article_title

########Extract article_authors
def get_authors_nyt(article_request):
    article_soup = BeautifulSoup(article_request.text,'html.parser')
    article_author = ''
    try:
        article_author = article_soup.find("span", {"class" : 'byline_author'}).text
    except AttributeError:
        print(ops)
    return article_author


def get_content_nyt(article_request):
    article_soup = BeautifulSoup(article_request.text,'html.parser')
    article_text = ''

    try:
        for item in article_soup.find_all("p", {"class" : 'story-body-text story-content'}):
            article_text += item.text

        # article_text= article_soup.find("div", {"class" : 'story-body'}).text
    except AttributeError:
        print(ops)


    return article_text

##### NYT webscraper function
def nyt(query_subject):
    links = []
    for url in search_news(query_subject + ' site:https://www.nytimes.com', pause = rando(), stop = stop_limit):
        links.append(url)

    article_list = []
    target_article = []

    for link in links:
        try:
            target_article.append(requests.get(link))

        except requests.exceptions.ConnectionError:
            print('something messed up')




    for request in target_article:
        article = {'Title' : '' , 'Authors' : [], 'Text' : [], 'Date' : '', 'Publication' : 'New York Times'}

        article['Title'] = get_title_nyt(request)
        article['Authors'] = get_authors_nyt(request)
        article['Text'] = wordlist(get_content_nyt(request))

        article_list.append(article)

    return  article_list




############################    ABC News Functions
def get_content_abc(article_request):
    article_text=''
    article_soup = BeautifulSoup(article_request.text,'html.parser')

    for part in article_soup.find_all('p', {"itemprop" : 'articleBody'}):
        try:
            article_text += part.get_text()
        except:
            print(ops)
    return article_text

def get_title_abc(article_request):
    article_soup = BeautifulSoup(article_request.text,'html.parser')
    article_title = ''
    try:
        article_title = article_soup.find('header', {"class" : 'article-header'}).h1.get_text()
    except:
        print(ops)

    return article_title

def get_date_abc(article_request):
    article_soup = BeautifulSoup(article_request.text,'html.parser')
    date_abc = ''

    try:
        date_abc = article_soup.find('span', {"class" : 'timestamp'}).get_text()
    except:
        print(ops)
    return date_abc

def get_authors_abc(article_request):
    article_soup = BeautifulSoup(article_request.text,'html.parser')
    authors_abc = ''
    try:
        authors_abc = article_soup.find('ul', {"class" : 'authors'}).get_text()
    except:
        print(ops)
    return authors_abc


##### ABC webscraper function
def abc(query_subject):
    links = []
    for url in search_news(query_subject + ' site:http://www.abcnews.com',  pause = rando(), stop = stop_limit):
        links.append(url)

    article_list = []
    target_article = []

    for link in links:
        try:
            target_article.append(requests.get(link))

        except requests.exceptions.ConnectionError:
            print('something messed up')




    for request in target_article:
        article = {'Title' : '' , 'Authors' : [], 'Text' : [], 'Date' : '', 'Publication' : 'ABC News'}

        article['Text'] = wordlist(get_content_abc(request))
        article['Title'] = get_title_abc(request)
        article['Date'] = get_date_abc(request)
        article['Authors'] = get_authors_abc(request)

        article_list.append(article)

    return  article_list






def get_content_cnn(article_request):
    article_text=''
    article_soup = BeautifulSoup(article_request.text,'html.parser')


#################   ##################   ########
#################   ##################   ########
    for part in article_soup.find_all('', {"class" : 'zn-body__paragraph'}):

        article_text += part.get_text()
    return article_text

def get_title_cnn(article_request):
    article_soup = BeautifulSoup(article_request.text,'html.parser')
    title_cnn = ''
    try:
        title_cnn = article_soup.find('h1', {"class" : 'pg-headline'}).get_text()
    except:
        print(ops)
    return title_cnn

def get_authors_cnn(article_request):
    article_soup = BeautifulSoup(article_request.text,'html.parser')
    authors_cnn = ''
    try:
        authors_cnn = article_soup.find('span', {"class" : 'metadata__byline__author'}).get_text()
    except:
        print(ops)
    return authors_cnn

def get_date_cnn(article_request):
    article_soup = BeautifulSoup(article_request.text,'html.parser')
    date_cnn = ''

    try:
        date_cnn = article_soup.find('p', {"class" : 'update-time'}).get_text()
    except:
        print(ops)
    return date_cnn

def cnn(query_subject):
    links = []

#################   ##################   ########
#################   ##################   ########
    for url in search_news(query_subject + ' site:http://www.cnn.com/',  pause = rando(), stop = stop_limit):
        links.append(url)

    article_list = []
    target_article = []

    for link in links:
        try:
            target_article.append(requests.get(link))

        except requests.exceptions.ConnectionError:
            print('something messed up')




    for request in target_article:
        article = {'Title' : '' , 'Authors' : [], 'Text' : [], 'Date' : '', 'Publication' : 'CNN'}

        article['Text'] = wordlist(get_content_cnn(request))
        article['Title'] = get_title_cnn(request)
        article['Date'] = get_date_cnn(request)
        article['Authors'] = get_authors_cnn(request)

        article_list.append(article)

    return  article_list


################### CNN







################## nbcnews


def get_title_nbc(article_request):
    article_soup = BeautifulSoup(article_request.text,'html.parser')
    title_nbc = ''
    try:
        # title_nbc = article_soup.find('h1', {"class" : 'pg-headline'}).get_text()
        title_nbc = article_soup.find('h1', {"itemprop" : 'headline'}).get_text()
    except:
        print(ops)
    return title_nbc

def get_authors_nbc(article_request):
    article_soup = BeautifulSoup(article_request.text,'html.parser')
    authors_nbc = ''
    try:
        authors_nbc = article_soup.find('span', {'class' : 'byline_author'}).get_text()
    except:
        print(ops)
    return authors_nbc

def get_date_nbc(article_request):
    article_soup = BeautifulSoup(article_request.text,'html.parser')
    date_nbc = ''
    try:
        date_nbc = article_soup.find('time', {'class' : 'timestamp_article'}).get_text()
    except:
        print(ops)
    return date_nbc

def get_content_nbc(article_request):
    article_text=''
    article_soup = BeautifulSoup(article_request.text,'html.parser')

    #################   ##################   ########
    #################   ##################   ########
    for part in article_soup.find_all('div', {"itemprop" : 'articleBody'}):

         for paragraph in part.find_all('p'):
             article_text += paragraph.get_text()
    return article_text

def nbc(query_subject):
    links = []

    #################   ##################   ########
    #################   ##################   ########
    for url in search_news(query_subject + ' site:http://www.nbcnews.com',  pause = rando(), stop = stop_limit):
        links.append(url)

    article_list = []
    target_article = []

    for link in links:
        try:
            target_article.append(requests.get(link))

        except requests.exceptions.ConnectionError:
            print('something messed up')


    for request in target_article:
        article = {'Title' : '' , 'Authors' : [], 'Text' : [], 'Date' : '', 'Publication' : 'NBC'}

        article['Text'] = wordlist(get_content_nbc(request))
        article['Title'] = get_title_nbc(request)
        article['Date'] = get_date_nbc(request)
        article['Authors'] = get_authors_nbc(request)
        article_list.append(article)

    return  article_list


################### NBC







################## hp or Huffington Post


def get_content_hp(article_request):
    article_text=''
    article_soup = BeautifulSoup(article_request.text,'html.parser')


    for part in article_soup.find_all('div', {"class" : 'content-list-component text'}):
        article_text += part.get_text()

    return article_text

def get_authors_hp(article_request):
    authors_hp =''
    article_soup = BeautifulSoup(article_request.text,'html.parser')

    try:
        authors_hp = article_soup.find('a', {'class' : 'author-card__details__name'}).get_text()
    except:
        print(ops)

    return authors_hp

def get_title_hp(article_request):
    title_hp =''
    article_soup = BeautifulSoup(article_request.text,'html.parser')

    try:
        title_hp = article_soup.find('h1', {'class' : 'headline__title'}).get_text()
    except:
        print(ops)

    return title_hp

def get_date_hp(article_request):
    date_hp =''
    article_soup = BeautifulSoup(article_request.text,'html.parser')

    try:
        date_hp = article_soup.find('span', {'class' : 'timestamp__date--published'}).get_text()
    except:
        print(ops)

    return date_hp

def hp(query_subject):
    links = []


    for url in search_news(query_subject + ' site:http://www.huffingtonpost.com',  pause = rando(), stop = stop_limit):
        links.append(url)

    article_list = []
    target_article = []

    for link in links:
        try:
            target_article.append(requests.get(link))

        except requests.exceptions.ConnectionError:
            print('something messed up')


    for request in target_article:
        article = {'Title' : '' , 'Authors' : [], 'Text' : [], 'Date' : '', 'Publication' : 'Huffington Post'}

        article['Text'] = wordlist(get_content_hp(request))
        article['Title'] = get_title_hp(request)
        article['Date'] = get_date_hp(request)
        article['Authors'] = get_authors_hp(request)
        article_list.append(article)

    return  article_list


################## hp or Huffington Post






################## CBS


def get_content_cbs(article_request):
    article_text=''
    article_soup = BeautifulSoup(article_request.text,'html.parser')


#################   ##################   ########
#################   ##################   ########
    for part in article_soup.find_all('div', {"itemprop" : 'articleBody'}):
        for paragraph in part.find_all('p'):
            article_text += paragraph.get_text()

    return article_text

def get_authors_cbs(article_request):
    authors_cbs =''
    article_soup = BeautifulSoup(article_request.text,'html.parser')

    try:
        authors_cbs = article_soup.find('span', {'class' : 'author'}).get_text()
    except:
        print(ops)

    return authors_cbs

def get_title_cbs(article_request):
    title_cbs =''
    article_soup = BeautifulSoup(article_request.text,'html.parser')

    try:
        title_cbs = article_soup.find('h1', {'itemprop' : 'headline'}).get_text()
    except:
        print(ops)

    return title_cbs

def get_date_cbs(article_request):
    date_cbs =''
    article_soup = BeautifulSoup(article_request.text,'html.parser')

    try:
        date_cbs = article_soup.find('span', {'class' : 'time'}).get_text()
    except:
        print(ops)

    return date_cbs


def cbs(query_subject):
    links = []

#################   ##################   ########
#################   ##################   ########
    for url in search_news(query_subject + ' site:http://www.cbsnews.com',  pause = rando(), stop = stop_limit):
        links.append(url)

    article_list = []
    target_article = []

    for link in links:
        try:
            target_article.append(requests.get(link))

        except requests.exceptions.ConnectionError:
            print('something messed up')


    for request in target_article:
        article = {'Title' : '' , 'Authors' : [], 'Text' : [], 'Date' : '', 'Publication' : 'CBS News'}

        article['Text'] = wordlist(get_content_cbs(request))
        article['Date'] = get_date_cbs(request)
        article['Authors'] = get_authors_cbs(request)
        article['Title'] = get_title_cbs(request)
        article_list.append(article)

    return  article_list
