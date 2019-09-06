def defineone(num):
    memory = set()
    while num not in memory:
        memory.add(num)
        num = sum(int(i)**2 for i in str(num))
    return 1 in memory


    number = input()
    inputs = []
    for i in range(int(number)):
        inputs.append(int(input()))

    for i in inputs:
        print(defineone(i))

