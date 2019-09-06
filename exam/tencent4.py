n = int(input())
input_arr = []
res = 0

for i in range(n):
    temp = input().split(" ")
    a = int(temp[0])
    b = int(temp[1])
    input_arr.append(b-a)
    res += n*b -a

input_arr.sort()
for index,value in enumerate(input_arr):
    res += -value*(index+1)

print(res)