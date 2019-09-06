num = int(input())
input_list = input().split(" ")


length = len(input_list)
i = 0

for j in range(length):
    if input_list[j].isdigit():
        input_list[j] = int(input_list[j])
i= 0
while i < length:
# if input_list[i].isdigit():
    if i + 1 < length and  input_list[i + 1] == '*':
        index_list = [i, i + 2]
        value_list = [input_list[i], input_list[i+2]]
        i = i + 1
        while i + 2 < length:
            i = i + 2
            if input_list[i] == '*':
                index_list.append(i+1)
                value_list.append(input_list[i+1])
            else:
                break
        value_list.sort()
        for j in range(len(index_list)):
            input_list[index_list[j]] = value_list[j]
    i = i +1  
      
input_list = [str(x) for x in input_list] 

print(" ".join(input_list))