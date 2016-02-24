'''
This py file calculates item based similarity
between items for given data set
*Should be run 1st(or 2nd)
'''

import pickle          #for storing object
import math            #perform math operations
import codecs          #to open the file
from CF_1a import *    #process the data 
def simi(i,j):                                      #calculate similarity
    n=0.0                    #numerator
    dsq1=0.0                 #denominator1
    dsq2=0.0                 #denominator2
    s=mov_usr[i]&mov_usr[j]  #list of users that rated both movie i and j
    
    for k in s:
        if data[k][i]!=0 and data[k][j]!=0:
            n=n+(data[k][i]-usr_av[k])*(data[k][j]-usr_av[k])          #numerator
            dsq1=dsq1+(data[k][i]-usr_av[k])*(data[k][i]-usr_av[k])    #denominator1
            dsq2=dsq2+(data[k][j]-usr_av[k])*(data[k][j]-usr_av[k])    #denominator2
    if(dsq1!=0 and dsq2!=0):
        sim[i][j]=n/(math.sqrt(dsq1)*math.sqrt(dsq2))                  #store similarity
        sim[j][i]=sim[i][j]

for i in range(1682):   #calculate similarity for all i,j
    j=i+1
    while j<1682:
        simi(i,j)
        j=j+1
    simi(i,i)

#make necessary data persistent
a_file=open(r'C:\Similarity.pkl','wb')    
pickle.dump(sim,a_file)
a_file.close()
b_file=open(r'C:\Data.pkl','wb')
pickle.dump(data,b_file)
b_file.close()
c_file=open(r'C:\movset.pkl','wb')
pickle.dump(mov_set,c_file)
c_file.close()
d_file=open(r'C:\usrmov.pkl','wb')
pickle.dump(usr_mov,d_file)
d_file.close()
