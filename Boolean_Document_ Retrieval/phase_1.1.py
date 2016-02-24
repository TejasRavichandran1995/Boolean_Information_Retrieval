'''
phase_1.py prog implements phase 1 of project and is supposed to be executed first i.e. before
search_query.py
processes done->
tokenizing
normalizing(stemming using porterstemmer)
building index,dictionary,posting list
making required data structures persistent
'''
#
#
#
import nltk,glob,os,pickle,codecs          #nltk module for tokenizing,using stemmer ; 
                                           #glob module for finding all pathnames matching a specific pattern according to ruels by unix ;
                                           #os module used to check list of files;
                                           #pickle is used for object serialization
                                           #codecs for using codecs.open() to decode encoding of .txt files

from nltk.stem import PorterStemmer    #PorterStemmer for performing stemming
from nltk import word_tokenize         #word_tokenize for tokenizing
print("Processing data...");                          
stemmer=PorterStemmer()                #create new porterstemmer
path="C:\\Users\\ndsharath\\Desktop\\data\\*\\*.txt"      #this is the path from where corpus is obtained (1-level deep .txt files)
files=glob.glob(path)   #stores list of pathnames obtained that match pattern specified in path
tokeind=[]              #list to store tokens of individual file
dict_filerev={}         #dictionary key:docID    value:filepath
index=0                 #initial docID
for file in files:                                                                               #for filepath present in list(files)
    tokeind.append(word_tokenize(codecs.open(file,'rU',"utf-8-sig",errors='ignore').read()))     #open and read file given by filepath(file),tokenize it,append in tokeind the tokens for that file                                      
    dict_filerev[index]=file                                                                     #store filepath,docID in dictionary dict_filerev
    index=index+1                                                                                #increment index

x=[]                                         #empty temporary list
index=0                                      #index specifing index of tokeind which is also docID of the corresponding file used to get tokeind[index]
dict_word={}                                 #the posting list key:word pointing to a value:list (the doc's in which word is present)
k=set()                                      #empty temporary set
for item in tokeind:                         #for each list of tokens in tokeind
    for y in item:                           #for each word(y) in list(item)
        x.append(stemmer.stem(y.lower()))    #convert word to lowercase,perform stemming,append to temporary list(x)
                                             #x (now contains stemmed,tokenized list of words of file having docID:index)
    k=set(x)                                 #store words present in x as a set in k
    for word in k:                           #for each word in k
        if word not in dict_word.keys():     #if  word not present in dictionary(posting list) add empty list as value and append
            dict_word[word]=[]               #index into it
            dict_word[word].append(index)
        else:                                #else append index into the list already present as value for key:word
            dict_word[word].append(index)
    index=index+1                            #increment index of tokeind
    x=[]                                     #change x back to empty set
            

a_file=open(r'C:\dict_word.pkl','wb')        #making data persistent (pickling or serializing) dict_word,dict_filerev,
pickle.dump(dict_word,a_file)                #set(dict_word.keys()) for use by programs in phase 2
a_file.close()
c_file=open(r'C:\dict_filerev.pkl','wb')
pickle.dump(dict_filerev,c_file)
c_file.close()
d_file=open(r'C:\set_dict_wordkeys.pkl','wb')
pickle.dump(set(dict_word.keys()),d_file)
d_file.close()

print("Completed!")

###END###

        


        
    
