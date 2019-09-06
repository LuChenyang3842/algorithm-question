n =  int(input()) #竞拍次数
auctions = []
for i in range(n):
    temp = [int(i) for i in input().split(" ")]
    auctions.append(temp)

q =int(input())
queries = []
for i in range(q):
    temp = [int(i) for i in input().split(" ")]
    temp.pop(0)
    queries.append(temp)

res = []

for eachQuery in queries:
    if len(eachQuery) == len(auctions):
        res.append([0,0])
        continue
    # for company in eachQuery:
    for i in range(len(auctions)-1, -1, -1):
        if i ==0  and auctions[i][0] in eachQuery:
            res.append([0,0])
            break
        if auctions[i][0] in eachQuery:
            continue
        else:
            res.append(auctions[i])
            break
    # if auctions_copy:
    #     res.append(auctions_copy[-1])
    # else:
    #     res.append([0,0])


for i in res:
    print(str(i[0])+" " + str(i[1]))