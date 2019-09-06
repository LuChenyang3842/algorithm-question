number = int(input())
inputs = []


def convert2Int(data):
    int_list=[]
    for i in data:
        int_list.append(int(i))
    return int_list

for _ in range(number):
    versions = input().split(' ')
    inputs.append(versions)

def compareVersion(line):
    v1 = line[0].split('.')
    v2 = line[1].split('.')
    v1 = convert2Int(v1)
    v2 = convert2Int(v2)
    length = max(len(v1),len(v2))
    if (len(v1)-len(v2))>0:
        for _ in range(len(v1)-len(v2)):
            v2.append(0)
    else:
        for _ in range(len(v2)-len(v1)):
            v1.append(0)
    if v1 == v2:
        print('false')
        return 
    for i in range(length):
        if v2[i] > v1[i]:
            print('true')
            return
        if v2[i] < v1[i]:
            print('false')
            return
    print('false')

for i in inputs:
    compareVersion(i)