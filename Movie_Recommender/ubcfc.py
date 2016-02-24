'''
This py file computes the 10 recommended movies for user
id that is given as input.
*Should be run after running the first 2 files
'''
import pickle
#from CF_1a import required data
file_a=open(r'C:\Similarity.pkl','rb')
sim=pickle.load(file_a)
file_a.close()
file_b=open(r'C:\Data.pkl','rb')
data=pickle.load(file_b)
file_b.close()
file_c=open(r'C:\movset.pkl','rb')
mov_set=pickle.load(file_c)
file_c.close()
file_d=open(r'C:\usrmov.pkl','rb')
usr_mov=pickle.load(file_d)
file_d.close()
file_m=open(r'C:\Movie.pkl','rb')
mov_id=pickle.load(file_m)
file_m.close()

#calculating recommendation

dict_premov={}                #store prediction->movie dictionary
z=int(input("Enter user id:"))#input query
k=set()                       #for storing set of predictions
l=mov_set-usr_mov[z-1]        #find movies not rated by user
np=0                          #numerator of prediction
dp=0                          #denominator of prediction
pre=0                         #store prediction
#calculate prediction
for e in l:
    np=0                      #set to 0
    dp=0                      #set to 0
    for s in usr_mov[z-1]:
        np=np+sim[s][e]*data[z-1][s]
        dp=dp+abs(sim[s][e])
    if(dp!=0):
        pre=np/dp             #store prediction of usr for movie e
        if(pre) not in dict_premov.keys(): #store movie as list for key "pre"
            dict_premov[pre]=[]
            dict_premov[pre].append(e)
        else:
            dict_premov[pre].append(e)
        k.add(pre)

k=list(k)                     #convert set k to list
k.sort(reverse=True)          #sort k

min_len= min(10,len(l))       #find max movie recommendation
                              #that can be found (default 10)

i=0
while i < min_len:            #print recommende movies
    for z in range(min(min_len-i,len(dict_premov[k[i]]))):
        print(mov_id[dict_premov[k[i]][z]])
    i=i+len(dict_premov[k[i]])
