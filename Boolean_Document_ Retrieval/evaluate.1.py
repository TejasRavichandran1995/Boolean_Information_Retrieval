'''
evaluate.py this contains following functions that will be used for query processing
sort_or()
sort_and()
sort_not()
calculate()
it also deserializes dict_filerev (which was serialized after running phase_1.py)
file to use in sort_not() and imported to execute in calculate.py
'''
#
#
#
import sys
import pickle                               #pickle module imported for object deserialization

file_s=open(r'C:\dict_filerev.pkl','rb')    #serialized object dict_filerev source file opened
dict_filerev=pickle.load(file_s)            #dict_filerev is loaded
file_s.close()                              
f=list(dict_filerev.keys())                 #list of all keys in dict_filerev (DOC id's) is stored as list in f
#
#
#
def sort_or (x,y):
    '''(list1,list2)->list3
    list1 and list2 should not have repeating elements and are sorted
    returns list(list3) equal to merging of list1 and list 2 WITHOUT REPETITON if element present in both

    Complexity- O(len(list1)+len(list2))

    >>>sort_or([1,2,3,4,5],[3,4,6,7])
    [1,2,3,4,5,6,7]
    '''
    z=[]                                        #list that is returned (list3)
    i=0                                         #index of list1 (x)
    j=0                                         #index of list2 (y)
    while(i<len(x) and j<len(y)):               #while end of list1 and list2 not reached process loop
          if x[i]<y[j]:             
              z.append(x[i])                    #add list1 element to z if list1 element smaller than list2 element and increment index of list1
              i+=1
          elif x[i]>y[j]:
              z.append(y[j])                    #add list2 element to z if list2 element smaller than list1 element and increment index of list2
              j+=1
          else:
              z.append(x[i])                    #add list1 element(or list2 element) if list1 element equals to list2 element and increment both indexes
              i+=1
              j+=1
    while(i<len(x)):
          z.append(x[i])                        #if end of list1 not reached add remaining elements to z
          i+=1
    while(j<len(y)):
          z.append(y[j])                        #if end of list1 not reached add remaining elements to z
          j+=1
    return z                                    #return list3(z)
#
#
#
def sort_and (x,y):
    '''(list1,list2)->list3
    list1 and list2 should not have repeating elements and are sorted
    returns list(list3) having common elements of list1 and list2 maintaining order

    Complexity- O(min(len(list1),len(list2))

    >>>sort_and([1,2,3,4,5],[3,4,6,7])
    [3,4]
    '''
    z=[]                                        #list that is returned (list3)
    i=0                                         #index of list1
    j=0                                         #index of list2            
    while(i<len(x) and j<len(y)):               #while end of list1 and list2 not reached process 
          if x[i]<y[j]:
              i+=1                              #increment index of list1 if element in list1 smaller than element in list2
          elif x[i]>y[j]:
              j+=1                              #increment index of list2 if element in list2 smaller than element in list1
          else:
              z.append(x[i])                    #add element in list1(or list2) if both elements are equal increment both indexes
              i+=1
              j+=1
    return z                                    #return list3(z)
#
#
#
def sort_not (y):
    '''(list1)->list2
    list1 should not have repeating elements and is sorted
    returns list(list2) equal to list of all elements present in list(f)(containing all dict_filerev keys) and NOT present in list1

    Complexity-O(len(f))

    >>>sort_not([1,2,3,4,7])
    [0,5,6,8,.....,2263]
    '''
    z=[]                                        #list that is returned (list2)
    y=set(y)                                    #list1 is converted to set data type because lookup in set(O(1)) is faster than list (O(n))
    z=[i for i in f if i not in y]              #if element in f is not in list1 add to list2
    return z                                    #return list2(z)
#
#
#
def calculate (y):
    '''(list1)->list2
    list1 is a list where each term is a special character [ '(',')','AND','OR','NOT' ] or a list itself
    returns list(list2) equal to final answer after processing expression in list1

    Complexity-O(kn) k<n

    >>>calculate([[1,2,3],'AND',[3,4,5],'OR',[6,7,8]])
    [3,6,7,8]
    >>> calculate([[1,2,3],'OR',[3,4,5],'AND',[6,7,8]])
    [1, 2, 3]
    '''
    zval=[]                                         #list used as stack for values in expression(list1) i.e. lists in list1
    zop=[]                                          #list used as stack for operators(special characters) in expression(list1)
    i=0                                             #flag(index) to identify how much of expression(list1) has been read
    thisOp=['AND','OR','NOT']                       #list of operators
    while(i<len(y)):                                                        #while end of expression(list1) is not reached
        if type(y[i]) is list:                        
            zval.append(y[i])                                               #if type of element in expression(y) is 'list' add to zval stack and increment flag
            i+=1
        elif y[i]=='(':
            zop.append(y[i])                                                #if type of element in expression(y) is 'left bracket' add element to zop stack and increment index
            i+=1
        elif y[i]==')':
            while zop[-1]!='(':                                             #if type of element in expression(y) is 'right bracket' while top
                if(zop[-1]=='NOT'):                                         #of zop stack is not equal to 'left bracket' process loop
                    zval.append(sort_not(zval.pop()))                       #if top of zop is 'NOT' perform sort_not(popped value of zval stack)
                elif(zop[-1]=='AND'):                                       #and add it to zval. similarly if top of zop is 'AND'/'or' perform
                    zval.append(sort_and(zval.pop(),zval.pop()))            #sort_and/sort_or on two values popped from zval stack
                elif(zop[-1]=='OR'):
                    zval.append(sort_or(zval.pop(),zval.pop()))
                zop.pop()                                                   #pop the operator present in zop
            zop.pop()                                                       #pop the 'left bracket' present in zop
            i+=1                                                            #increment flag
        elif y[i] in thisOp:                                                                                                         #if element is an operator
            while (not(len(zop)==0)) and ((zop[-1]=='AND' and y[i]!='NOT') or (zop[-1]=='OR' and y[i]=='OR') or (zop[-1]=='NOT')):   #while precedence(NOT>AND>OR)
                if(zop[-1]=='NOT'):                                                                                                  #satisfied or zop stack is empty
                    zval.append(sort_not(zval.pop()))                                                                                #process loop..if top of zop is
                elif(zop[-1]=='AND'):                                                                                                #'NOT'/'AND'/'OR' perform sort_not/ 
                    zval.append(sort_and(zval.pop(),zval.pop()))                                                                     #sort_and/sort_or on popped zval
                elif(zop[-1]=='OR'):                                                                                                 #value(s) and add to zval
                    zval.append(sort_or(zval.pop(),zval.pop()))
                zop.pop()                                                                                                            #pop the operator on top of zop
            zop.append(y[i])                                                                                                         #add element to zop
            i+=1                                                                                                                     #increment flag
            #print(zop)
    while len(zop)!=0 :                                                     #while zop stack not empty use process zval items using operators in zop
        if(zop[-1]=='NOT'):
                zval.append(sort_not(zval.pop()))
        elif(zop[-1]=='AND'):
                zval.append(sort_and(zval.pop(),zval.pop()))
        elif(zop[-1]=='OR'):
                zval.append(sort_or(zval.pop(),zval.pop()))
        zop.pop()
    if len(zval)==1:
        return zval.pop()                                                       #when zop is empty final item in zval is the required answe of the expression this item is popped and returned(list2)
    else:            
        print("ERROR:INVALID EXPRESSION")
        sys.exit()

###END###            
                    
                
                
            
        
    
    
          
              
