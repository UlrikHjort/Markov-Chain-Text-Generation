########################################################################
#                                                                           
#                                                                    
#                      Markov Chain Text generation                                                           
#                           MarkovChainTextGen.py                                      
#                                                                           
#                                MAIN                                      
#                                                                           
#                 Copyright (C) 2004 Ulrik Hoerlyk Hjort                   
#                                                                        
#  Markov Chain Text generation is free software;  you can  redistribute it                          
#  and/or modify it under terms of the  GNU General Public License          
#  as published  by the Free Software  Foundation;  either version 2,       
#  or (at your option) any later version.                                   
#  Markov Chain Text generation is distributed in the hope that it will be                           
#  useful, but WITHOUT ANY WARRANTY;  without even the  implied warranty    
#  of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                  
#  See the GNU General Public License for  more details.                    
#  You should have  received  a copy of the GNU General                     
#  Public License  distributed with Yolk.  If not, write  to  the  Free     
#  Software Foundation,  51  Franklin  Street,  Fifth  Floor, Boston,       
#  MA 02110 - 1301, USA.                                                    
########################################################################        


import random
import sys

########################################################################################
#
# Generate Markov chain dictionary. Each word is saved as key with a list of subsequent 
# found in the learning text. The same word can exist several times in the list which 
# will works as the probability of the occurrence of the actual word.
#
########################################################################################

############################################################
#
#
#
############################################################
def dump_dict(d):
    keys = d.keys()
    keys.sort()
    for k in keys:
        print k + " : " + str(d[k])



############################################################
#
#
#
############################################################
def strip_str(s):
    chars = "\"',:-_()"
    for c in chars:
        s = s.replace(c,"")
        s = s.lower()
    return s



############################################################
#
#
#
############################################################
def generate_dict_lines(fname):
    word_dict = {"S->":[]}
    with open(fname) as f:
        for line in iter(f):
            if len(line) < 2:
                continue
            index = 0
            sentence = line.rstrip().split()
            for word in sentence:
                if index == len(sentence)-1:
                    break
                if index == 0:
                    word_dict["S->"].append(word)
                if word_dict.has_key(word):
                    word_dict[word].append(sentence[index+1])
                else:
                    word_dict[word] = [sentence[index+1]]
                index += 1
        f.close()

    return word_dict


############################################################
#
# G E N E R A T E   D I C T I O N A R Y
#
############################################################
def generate_dict(fname):
    word_dict = {"S->":[]}
    sentence=""
    with open(fname, 'r') as f:
        sentence=f.read().replace('\n', '')
    f.close()
    sentence = strip_str(sentence)
    index = 0
    sentence = sentence.rstrip().split()
    new_sentence = True

    for word in sentence:
        if index == len(sentence)-1:
            break
        if new_sentence:
            word_dict["S->"].append(word)
            new_sentence = False
        if '.' in word or '?' in word or '!' in word:
            new_sentence = True
            index += 1
            continue
        if word_dict.has_key(word):
            word_dict[word].append(sentence[index+1])
        else:
            word_dict[word] = [sentence[index+1]]
        index += 1

    return word_dict


############################################################
#
# G E N E R A T E   S E N T E N C E
#
############################################################
def generate_sentence(word_dict, s_length):

    while True:
        word = random.choice(word_dict["S->"])
        sentence = ""
        sentence +=  (word.title() + " ")

        ret = ""
        word_cnt = 0

        while word_dict.has_key(word):
            word =  random.choice(word_dict[word])

            sentence +=  (word + " ")
            word_cnt += 1
            if '?' in word or '.' in word or '!' in word:
                ret =  sentence
            else:
                ret = (sentence[:-1] + '.')

        if word_cnt <=s_length:
            return ret



############################################################
#
#  M A I N
#
############################################################
if  len(sys.argv) != 3:
    print "Error: Wrong number of arguments"
    print "Usage: python MarkovChainTextGen.py <text file> <sentence length>"
    sys.exit(1)



wd = generate_dict(sys.argv[1])


print generate_sentence(wd,int(sys.argv[2]))


