'''
search_query.py is program to be run for giving query input and displaying
output.
NOTE: few data serialized from other program are used in this so make sure to
run this after creating dictionary and other required data by running phase_1.py
(and testing evaluate.py (optional))
'''
#
#
#
import pickle                           #pickle module imported for deserialization
import evaluate                         #imported to use evaluate()
import nltk                             #imported to use stemming 
import sys                              #imported to use sys.exit()
from nltk.stem import PorterStemmer     #import PorterStemmer program to perform stemming for normalization
from evaluate import *                  #import everything from evaluate.py

stemmer=PorterStemmer()                 #create new Porter Stemmer

query=input("ENTER SEARCH QUERY:")      #prompt user for input and stores input to query

                                        #deserializing serialized items created when initial file was run
file_a=open(r'C:\dict_word.pkl','rb')   
dict_word=pickle.load(file_a)           #deserialize dict_word
file_a.close()
file_c=open(r'C:\dict_filerev.pkl','rb')
dict_filerev=pickle.load(file_c)        #deserialize dict_filerev
file_c.close()
file_d=open(r'C:\set_dict_wordkeys.pk1','rb') 
dict_wordkey=pickle.load(file_d)        #deserialize set(dict_word.keys())
file_d.close()

query=query.split()                     #split string in query to indivdual words in list and save it as query

index=0                                 #index of query initialized to 0

ss=[]                                   #list for processing substring operation
flag=0                                  #to check if only 'AND' operation is present
citem=0                                 #count of item for checking if expression valid
cand=0                                  #count of 'AND' for checking if expression valid
for item in query:                      #for each element in query process-> 
        if item!='AND' and item!='(' and item!='NOT' and item!='OR' and item!=')':     #if item is not a special character ['(',')','AND','OR','NOT']
            if item[0]!='*':
                    item=stemmer.stem(item.lower())                                            #convert item to lowercase then perform stem except for substring action

            if item[0]=='*':                                                                   #if 1st letter in item in query is * perform substring action
                    item=item[1:].lower()                                                      #remove '*' from item and convert to lower case
                    for word in dict_wordkey:                                                  #check if item is substring in list of
                            if item in word:                                                   #words in dictionary, if present add posting list of that word,
                                    ss=sort_or(ss,dict_word[word])                             #ss and perform sort_or on both till end of words in dictionary reached   
                    query[index]=ss                                                            #store the final ss in query[index]
            elif item in dict_word:
                    query[index]=dict_word[item]                                               #store in query[index] the posting list dict_word[item]
            else:
                    query[index]=[]                                                            #else put in empty list
        elif item=='OR' or item=='NOT':
                flag=flag+1
        index=index+1                                                                  #increment index
if flag==0:                                                                            #QUERY PROCESS OPTIMIZATION if only 'AND' operation present
        query=sorted(query,key=len)                                                    #sort query based on len of elements
        Ans=f                                                                          #list of all doc id's stored in Ans
        for item in query:                                                             #for each item in query as long as it isnt of type str sort_and with Ans
                if type(item)!=str:                                                    #and update Ans ,increment count of item or 'AND'
                        Ans=sort_and(Ans,item)
                        citem+=1
                elif item=='AND':
                        cand+=1
        if cand>=citem:                                   #if expression invalid output message and exit
                print("ERROR:NOT VALID EXPRESSION")
                sys.exit()
else:                                                           #when operations other than all 'AND' is present      
        try:                                            
                Ans=calculate(query)                            #calculate expression obtained as list in query
        except IndexError:
                print("ERROR:NOT VALID EXPRESSION")             #if index error occurs output error message and exit
                sys.exit()
print('DOCID   PATH')                                           #print out put as 2 columns DOCID and file Path
for item in Ans:
        print("%d       %s"%(item,dict_filerev[item]))

###END###
