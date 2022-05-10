def odd_one(L):
    d1={}
    for i in L:
        if type(i) not in d1.keys():
            d1.update({type(i):1})
        else:
            d1.update({type(i):d1[type(i)]+1})
    
    for key,val in d1.items():
        if val==1:
            return key.__name__
    
print(odd_one(eval(input().strip())))


'''
My working copy:


def odd_one(L):
    mydict = {}
    t = ''
    for i in L:
        t = type(i).__name__
        #print(t)
        if t in mydict.keys():
            count = mydict[t]+1
            mydict.update({t:count})
        else:
            mydict.update({t:1})

    print(mydict)
        
    for key,val in mydict.items():
        if val==1:
            return key
            

print(odd_one(eval(input().strip())))    


'''