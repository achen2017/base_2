
from bs4 import BeautifulSoup
import requests
import json
import time
from google import search
from google import search_news
from google import get_page
from random import randint
from web_scraper_functions_5 import nyt, abc, cnn, nbc, hp, cbs
import time
from gensim import corpora, models
import gensim
import sys
import sqlite3 as lite


import shutil


### I want to create a function to put into network_maker that takes the node name and the modules of complete array.

def packager(complete_array, subject, date, the_time, counter):
    conn = lite.connect("/Users/abrahamchen/Documents/NETWORKS/ind_study_code/base_2/db/development.sqlite3")
    cursor = conn.cursor()


    for item in complete_array:
        counter += 1
        cursor.execute("INSERT INTO queries VALUES (?, ?, ?, ?, ?, ?);", (counter, subject, item[0], item[4], date, the_time))            conn.commit()

    ### Reminder: complete_array's elements look like this:
    ### ['14:4', '0.00643449', '"0.0"', 417, 'said']



def main():
    subject = str(sys.argv[1])
    date = time.strftime("%d_%m_%Y")
    the_time = time.strftime("%H_%M_%S")

    # blahblah = [['beta','b','c','d','e'],['dos','1','1','1','1']]
    # conn = lite.connect("/Users/abrahamchen/Documents/NETWORKS/ind_study_code/base_2/db/development.sqlite3")
    # cursor = conn.cursor()


    # Counter pulls in from Rails' controller's @latest_id as a string. This maintains the id
    # counter = sys.argv[2]
    counter = sys.argv[2] + 1
    packager(complete_array, subject, date, the_time, counter)


    # counter = int(counter)
    # for item in blahblah:
    #     counter += 1
    #     cursor.execute("INSERT INTO queries VALUES (?, ?, ?, ?, ?, ?);", (counter, item[0], item[1], item[2], date, the_time))
    #     conn.commit()








########################## THIS IS WHERE WE RUN MAIN ###########################
main()
###################################################################
