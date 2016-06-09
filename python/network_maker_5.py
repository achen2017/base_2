### In cleaner() (not currently used), you should get the CSV saved to the temp folder

import json #
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import csv
import os

import shutil

base_dir = '/Users/abrahamchen/Documents/NETWORKS/ind_study_code/base_2/' #LIVE

#makes a new folder
def makemydir():
  try:
    os.makedirs('python/temporary_folder')
  except OSError:
    pass

class Big:


    def unique_words(self, article_dump, numb_most):
    # In this method, we're creating a list of unique words. Based off of words that are most frequently used in the corpus.
    # limiting to most common words may not be necessary given the limits of the corpus (just the lede)
        all_words = []
        for item in article_dump:
            for eachword in item['Text']:
                all_words.append(eachword)

        # self.counted_words = Counter(all_words)
        self.counted_words = Counter(all_words)

        # common_words = self.counted_words.most_common(numb_most)
        common_words = self.counted_words.most_common(numb_most)

        self.wlist = []
        for item in common_words:
            self.wlist.append(item[0])   #wlist is a list of top numb_most most frequently used words in all the articles

        self.zero_matrix = np.zeros((numb_most, numb_most))  # this Zero_matrix is one way of writing the edgelist. It's a giant two dimensional matrix where each side is a word and the weights linking two words is written into the entries
        # return(self.counted_words)


    def network_links(self, article_dump):
        ## in the following block, we make the network links
        temp = []
        self.edgelist = []
        z = len(self.wlist)

        for i, word_a in enumerate(self.wlist):
            a = i + 1
            if a != z - 1:                       #checking that we're not at end of wlist
                portion_wlist = self.wlist[a:z]   #checking word_a against only the words that haven't been checked yet
                for word_b in portion_wlist:
                    temp.extend([word_a, word_b])
                    link_count = 0          #number of shared articles between word_a and word_b
                    j = self.wlist.index(word_b)
                    for article in article_dump:
                        if (word_a in article['Text'])&(word_b in article['Text']): #feel free to suggest a more parsimonious solution
                            link_count += 1
                        else:
                            link_count += 0
                    temp.append({'weight' : link_count})
                    self.zero_matrix[i][j] = link_count
                    self.edgelist.append(temp)         #Note: we can always convert to tuple via b = tuple(temp)
                    temp = []


    def normalizer(self):
    # This method normalizes the weights of the zero_matrix network. We can easily impliment for edgelist.
        sum_all = 0
        for item in self.zero_matrix:
            sum_all += sum(item)
        print(sum_all)

        for i, line in enumerate(self.zero_matrix):
            for j, row in enumerate(line):
                self.zero_matrix[i][j] = self.zero_matrix[i][j]/sum_all




    def grapher(self, infomap_command, file_name):
    ### this Method produces two files that are useful: a .net file and a .tree file.
    ### .net a) connects nodes names to ids b) lists vertices with weights
    ### .tree contains modularity information via ids

        #here we write graph data into pajek form from edgelist, which can be used by infomap to do more network analysis.
        G = nx.Graph()
        G.add_edges_from(self.edgelist)
        nx.write_pajek(G, 'python/temporary_folder/' + file_name + '.net')   ### #change would have to change #LIVE

        #here, we're executing infomap in the shell to get infomap's capability (access to modularity)
        os.system(infomap_command)




    def tree_to_array(self, file_name):
        ### This method takes the .tree output of infomaps and turns it into an array,
        ### where each each element contains information about each node. Information is:
        ### module name in the form "1:2" where 1 is larger module, and 2 is smaller module
        ### then there are two items that I don't understand and a final entry that is the id of the node.
        tree_text = open('python/temporary_folder/' + file_name +'.tree').readlines()    ### #change, should change dynamically #LIVE

        line_array = []
        self.final_array = []
        for line in tree_text:

            line_array.append([line])

        del line_array[0:2]

        for item in line_array:
            item = item[0].split(" ")
            item[3] = item[3].rstrip('\n')
            item[3] = int(item[3])
            self.final_array.append(item)


    def completer(self, file_name):
        ### this block opens the pajeks file back up, and reads it (we probably don't need to write Pajeks to a file) and then
        node_net = open('python/temporary_folder/' + file_name +'.net').readlines() #LIVE
        self.node_array = []
        for line in node_net:
            self.node_array.append(line.split(' '))
        del self.node_array[0]

        ### this block appends the actual name of the node (a word) to the end of the item in final_array
        ### that contains the module information.
        self.complete_array =[]
        for item_final in self.final_array:

            for item_node in self.node_array[0:len(self.final_array)]:
                item_node[0] = int(item_node[0])
                if item_final[-1] == item_node[0]:
                    item_final.append(item_node[1])

                    ###Abe Fucking around
                    # item_final.append(Counter(self.all_words())[item_node[1]])
                    item_final.append(self.counted_words[item_node[1]])
                    ###End of Abe fucking around

                    self.complete_array.append(item_final)

    ### complete_array's elements look like this:
    ### ['14:4', '0.00643449', '"0.0"', 417, 'said']
    ### 14 in the first element of the above is the major module, and 4 is the submodule
    ### the second, third, and fourth modules mean something that I don't care about
    ### and the 'said' is the name of the node with the given modularity


    def cleaner(self):
    #This method creates a list that can be easily transmitted into CSV. This is good for moving information to Gephi
        self.clean_list = []
        for item in self.edgelist:
            self.clean_list.extend([[item[0],item[1],item[2]['weight']]])

        myfile = open('clean_data_' + file_name + '.csv', 'w')
        myfile.write('Target,Source,Weight' + '\n')
        for item in self.clean_list:
            myfile.write(item[0] + ',' + item[1] + ',' + str(item[2]) + '\n')
        myfile.close



def network_main(subject, article_dump):
    # data_json = "vr.json"

    file_name = subject  # this is future file name
    numb_most = 500  #sets how many words go into the network. It can definitely handle 500

    # infomap_command = "../packages/Infomap/Infomap temporary_folder/another_test.net temporary_folder/ -N 10 --tree --bftree" ### #change we have to change the paths used here

    # infomap_command = "python/Infomap/Infomap python/temporary_folder/" + file_name + ".net python/temporary_folder/ -N 10 --tree" ### #change we have to change the paths used here
    # /Users/abrahamchen/Documents/NETWORKS/ind_study_code/base_2/python/temporary_folder/Hilary.net
    # infomap_command = "/Users/abrahamchen/Documents/NETWORKS/ind_study_code/base_2/python/Infomap/Infomap /Users/abrahamchen/Documents/NETWORKS/ind_study_code/base_2/python/temporary_folder/" + file_name + ".net /Users/abrahamchen/Documents/NETWORKS/ind_study_code/base_2/python/temporary_folder/ -N 10 --tree"   #LIVE
    infomap_command = "python/Infomap/Infomap python/temporary_folder/" + file_name + ".net python/temporary_folder/ -N 10 --tree"   #LIVE


    # /Users/abrahamchen/Documents/NETWORKS/ind_study_code/base_2/python/Infomap/Infomap

    # with open(art_cont_name, 'r') as wfile: # this is file pulled
        # article_dump = json.load(wfile)

    makemydir()

    b = Big()

    ##list of functions that do stuff
    # b.counted_words = b.unique_words(article_dump, numb_most)
    b.unique_words(article_dump, numb_most)
    b.network_links(article_dump)

    b.grapher(infomap_command, file_name)
    b.tree_to_array(file_name)
    b.completer(file_name)



    return(b.complete_array)
    ### Unused functions
    # b.cleaner()
    # b.normalizer()

    # shutil.rmtree('temporary_folder')
