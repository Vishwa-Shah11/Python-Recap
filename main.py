
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

    #print(mydict)
        
    for key,val in mydict.items():
        if val==1:
            return key
            

print(odd_one(eval(input().strip())))    