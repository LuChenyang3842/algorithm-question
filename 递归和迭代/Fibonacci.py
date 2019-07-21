##斐波那契数列计算

##use array to store the value
#Time complexity O(n)
#space complexity O(n)
def Fibonacci_arr(n):
    if n == 0:
        return 0
    if n < 3:
        return 1
    arr = [1,1]
    index = 2
    
    while index < n:
        next = arr[index-1]+ arr[index-2]
        arr.append(next)
        index += 1
    return arr[n-1]


##iteration
#使用两个指针
#Time complexity O(n)
#space complexity 0
def Fibonacci_Iteration(n):
    if n == 0:
        return 0
    if n < 3:
        return 1
    first = 1
    second = 1
    index = 2
    while index < n:
        index +=1
        temp = second
        second = first + second
        first = temp
    return second


##recursive 递归
#Time complexity O(2^n): 考虑树状分叉结构
def Fibonacci_recursion(n):
    if n<=1:
        return n
    else:
        return Fibonacci_recursion(n-1) + Fibonacci_recursion(n-2)



