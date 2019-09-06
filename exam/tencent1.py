first_input = input().split(" ")
a_num = int(first_input[0])
b_num = int(first_input[1])

a = [int(i) for i in  input().split(" ")]
b = [int(i) for i in  input().split(" ")]


a_odd = []
a_even = []
b_odd = []
b_even = []
for item in a:
    if item %2 == 0:
        a_even.append(item)
    else:
        a_odd.append(item)

for item in b:
    if item%2 == 0:
        b_even.append(item)
    else:
        b_odd.append(item)


print(min(len(a_even), len(b_odd))+ min( len(a_odd), len(b_even)))