# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

#递归
class Solution:
    def jumpFloor(self, number):
        if number<=2:
            return number
        else:
            return self.jumpFloor(number - 1) + self.jumpFloor(number - 2)
 

 #迭代
class Solution1:
    def jumpFloor(self, number):
        if number<=2:
            return number
        else:
            first = 1
            second = 2
            index = 2
            while index < number:
                index +=1
                second =first + second
                first = second - first
            return second

# 一只青蛙一次可以跳上1级台阶，也可以跳上2级，也可以跳上5级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
class Solution3:
    def jumpFloorI(self, number):
        arr = [0,1,2,3,5,9]
        index = 5
        while index < number:
            index += 1
            arr.append(arr[index-1] + arr[index-2] + arr[index-5])
        return arra[number]


# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
class Solution:
    def jumpFloorII(self, number):
        acc = 0
        previouAcc= 0
        index = 0
        while index < number:
            index += 1
            acc = previouAcc + acc + 1
            previouAcc = acc - 1
        return acc
