from itertools import combinations
transactions = [
[1,3],
[2],
[1,4,5],
[3,5],
[1,2,4],
[5],
[2,3,4,5],
[1],
[3,4],
[1,2,3],
[2,5],
[4],
[1,3,5],
[2,4],
[1,2],
[3],
[4,5],
[1,4],
[2,3],
[1,2,3,4,5]
]


LKM1 ={}
c ={}
for t in transactions :
    for i in t :
        key = frozenset([i])
        if key in c:
            c[key]+= 1
        else :
            c[key] = 1
print(c);

minsup = 3
numiters = min(len(c.keys()),max([len(t) for t in transactions]))

L = { iteamset:count for iteamset,count in c.items() if count >= minsup}
LKM1 = L

for k in range( 2,numiters+1):
    ck={}
    for item1,count in LKM1.items():
        for item2,count2 in LKM1.items():
            l1 = list(sorted(item1))
            l2 = list(sorted(item2))
            joinable = True
            for l in range(k-2):
                if l1[l] != l2[l] :
                    joinable = False
                    break
            if joinable :
                newset = frozenset(set(l1).union(set(l2)))
                if len(newset) == k:
                    ck[newset] = 0
    for t in transactions:
        if len(t) >= k :
            for itemset in combinations(t,k):
                itemset = frozenset(itemset)
                if itemset in ck :
                    ck[itemset] += 1
    L.update(LKM1)
    LKM1 = { iteam:count for iteam,count in ck.items() if count >= minsup}
    
print(L);
