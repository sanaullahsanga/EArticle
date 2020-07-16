seen, result = set(), []
Content=['hy i am here','hy i am here','hy','i','hy i am here']
for idx, item in enumerate(Content):
            if item not in seen:
                print(item)
                seen.add(item)  # First time seeing the element
            else:
                result.append(idx)  # Already seen, add the index to the result
n=(len(result))
for i in range(n):
    j=result[i]
    print(j)
    if i==0:
        Content.pop(j)
    if i==1:
        Content.pop(j - 1)
    if i==2:
        Content.pop(j - 2)
    if i==3:
        Content.pop(j - 3)
    if i==4:
        Content.pop(j - 4)
    if i==5:
        Content.pop(j - 5)
    if i==6:
        Content.pop(j - 6)
    if i==7:
        Content.pop(j - 7)
    if i==8:
        Content.pop(j - 8)
    if i==9:
        Content.pop(j - 9)
    if i==10:
        Content.pop(j - 10)
    #print(result[i])

print(Content)
