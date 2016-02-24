'''
This py file processes given data to usable form
*Should be run 1st or need not be, since CF_1b runs this file before execution)
'''
import pickle
import codecs
path="C:\\Users\\tejas\\Downloads\\study3\\cs f469\\ml-100k\\ml-100k\\u.item"
tokeind=[]
tokens=''
count=0
k=0
data=(codecs.open(path,'rU',"utf-8-sig",errors='ignore').read())
for i in data:    
    if count==0 and i!='|' and i!='\n' and i!=' ':
        tokeind.append([])
        tokens=tokens+i
    elif count==23 and i!='|':
        tokeind[k].append(i)
        k=k+1
        count=0
    elif i=='|':
        count=count+1;
        if(len(tokens)!=0):
            tokeind[k].append(tokens)
        tokens=''
    elif i!='|'and i!='\n':
            tokens=tokens+str(i)
mov_id={}
i=0
while(i<1682):
    mov_id[int(tokeind[i][0])-1]=tokeind[i][1]
    i=i+1
m_file=open(r'C:\Movie.pkl','wb')
pickle.dump(mov_id,m_file)
m_file.close()

#data source
path="C:\\Users\\tejas\\Downloads\\study3\\cs f469\\ml-100k\\ml-100k\\u.data"

data=[[0 for x in range(1682)] for x in range(943)] #to store rating user x movie

mov_usr=[set() for x in range(1682)]                #to store set of users that
                                                    #rated movie

usr_avg=[[0 for x in range(2)] for x in range(943)] #to store sum of ratings,
                                                    # count of ratings of each user

usr_av=[0 for x in range(943)]                      #to store avg of user                     

usr_mov=[set() for x in range(943)]                 #to store list of movies rated
                                                    #by user

mov_set=set(x for x in range(1682))                 #to store all ids of the movie

#Processing the data
#format- user_id(\t)movie_id(\t)rating(\t)timestab(\n)
d=(codecs.open(path,'rU',"utf-8-sig",errors='ignore').read())
c=0           #stores word count in present line
row_c=0       #to store row count for data
col_c=0       #to store column count for data
in_c=0        #to store rating
for i in d:
    if(i!='\n'):
        if(c==0 and i!='\t'):
            row_c=row_c*10+int(i)          #calculate row count
        if(c==1 and i!='\t'):
            col_c=col_c*10+int(i)          #calculate column count
        if(c==2 and i!='\t'):
            in_c=in_c*10+int(i)            #calculate rating
    if(i=='\t' or i=='\n'):
        if(c==3):
            data[row_c-1][col_c-1]=in_c                  #store rating

            mov_usr[col_c-1].add(row_c-1)                #add user that rated movie
            usr_mov[row_c-1].add(col_c-1)                #add movie that was rated by user
            usr_avg[row_c-1][0]=usr_avg[row_c-1][0]+in_c #to find total rating points by user
            usr_avg[row_c-1][1]=usr_avg[row_c-1][1]+1    #to find no. of movies rated by user

            row_c=0                                      #reset temporary data
            col_c=0
            in_c=0
            c=0
        else:                                            #increment word count
            c=c+1
            
sim=[[0 for x in range(1682)] for x in range(1682)] #to store each similarity 

for x in range(943):                                #calculate avg
    usr_av[x]=usr_avg[x][0]/usr_avg[x][1]
    
        


        
    
