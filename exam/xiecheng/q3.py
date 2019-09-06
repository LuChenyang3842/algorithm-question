input_list = input().split(' ')
input_list = [int(i) for i in input_list]


# current_max = input_list[0]
# current_product = 1

# for i in range(len(input_list)):
#     if current_product * input_list[i] >  current_product:
#         current_product =   current_product * input_list[i]
#     else:
#         current_product = input_list[i]
#     if current_product > current_max:
#         current_max =  current_product

# print(current_max)
max_num = input_list[0]
min_num = input_list[0]
result = input_list[0]
for i in range(1, len(input_list)):
    temp = max_num
    max_num = max([max_num*input_list[i],min_num*input_list[i],input_list[i]])
    min_num = min([temp*input_list[i],min_num*input_list[i],input_list[i]])
    if max_num > result:
        result = max_num
print(result)

    


