L=["a","b","c","a","b","d","e","a"]
NL = L
for i in range(len(NL)-1):
    count = 0
    for j in range(i+1,len(NL)):
        if L[i]==L[j]:
            count +=1
            L.remove(L[j])
    print(L)
    print(i+"-->"+str(count))


    