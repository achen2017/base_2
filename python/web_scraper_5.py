### should include if statement such that if there's a space in subject, it's replaced by _
### We should put all files produced by a query in a temporary folder
#### This version only picks up the first 100 words of text
from bs4 import BeautifulSoup
import requests
import json
import time
from google import search
from google import search_news
from google import get_page
from random import randint
from web_scraper_functions_5 import nyt, abc, cnn, nbc, hp, cbs
from network_maker_5 import network_main
import time
from gensim import corpora, models
import gensim
import sys
import sqlite3 as lite
from collections import Counter

def word_counter(article_dump):
# In this method, we're creating a list of unique words. Based off of words that are most frequently used in the corpus.
# limiting to most common words may not be necessary given the limits of the corpus (just the lede)
    all_words = []
    for item in article_dump:
        for eachword in item['Text']:
            all_words.append(eachword)
        counted_words = Counter(all_words)
    return(counted_words)

def packager(complete_array, query_id, subject, date, the_time, counter):
    conn = lite.connect("db/development.sqlite3") #Live
    # conn = lite.connect("/Users/abrahamchen/Documents/NETWORKS/ind_study_code/base_2/db/development.sqlite3")
    cursor = conn.cursor()
    # cursor.execute("INSERT INTO queries VALUES (?, ?, ?, ?, ?, ?);", (1, 'subject', 'subject', 'subject', date, the_time))

    for item in complete_array:
        ### I have yet to get freq working. Don't know how to call it here effectively #change
        ### Not really sure how to deal with updated_at #change
        cursor.execute("INSERT INTO data VALUES (?, ?, ?, ?, ?, ?, ?, ?);", (counter, query_id, item[4], item[0], item[5], item[1], the_time, the_time))
        conn.commit()
        counter += 1
### complete_array's elements look like this:
### ['14:4', '0.00643449', '"0.0"', 417, 'said']


def main():
    # subject = the_subject
    # subject = input("what do you want to look up? ")
    subject = str(sys.argv[1])
    counter = int(sys.argv[2])+1
    query_id = int(sys.argv[3])
    date = time.strftime("%d_%m_%Y")
    the_time = time.strftime("%H_%M_%S")
    article_content = open(subject + '_on_' + date + '_at_' + the_time + '.json', 'w')
    art_cont_name = str(subject + '_on_' + date + '_at_' + the_time + '.json')
    # Create the file inwhich to store the

    article_holder = {'Title' : '' , 'Authors' : [], 'Text' : '', 'Date' : '', 'Publication' : 'New York Times'}


    # articles_nyt = nyt(subject)   ##where we call NYT webscraper function and put it into a dict with other NYT content
    # articles_abc = abc(subject)
    article_dump = []

    # abc_list = abc(subject)
    nyt_list = nyt(subject)
    # cnn_list = cnn(subject)
    # nbc_list = nbc(subject)
    # hp_list = hp(subject)
    # cbs_list = cbs(subject)

    # article_dump.extend(abc_list + nyt_list + cnn_list + nbc_list + hp_list + cbs_list)
    article_dump.extend(nyt_list)

    # print('number of ABC articles collected : ' + str(len(abc_list)))
    print('number of New York Times articles collected : ' + str(len(nyt_list)))
    # print('number of CNN articles collected : ' + str(len(cnn_list)))
    # print('number of NBC articles collected : ' + str(len(nbc_list)))
    # print('number of Huffington Post articles collected : ' + str(len(hp_list)))
    # print('number of CBS articles collected : ' + str(len(cbs_list)))

    json.dump(article_dump, article_content, indent=4)

    complete_array = network_main(subject, article_dump)

    packager(complete_array, query_id, subject, date, the_time, counter)







########################## THIS IS WHERE WE RUN MAIN ###########################
main()
###################################################################
