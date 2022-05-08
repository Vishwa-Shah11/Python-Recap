import itertools

def find_Min_Difference(L,P):
    l1 = list(itertools.combinations(L,P))
    #print(len(l1))
    l2 = []
    for i in l1:
        diff = max(i)-min(i)
        l2.append(diff)
    min_value = min(l2)
    return min_value
    
L=eval(input().strip())
P=int(input())
print(find_Min_Difference(L,P))