# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
# 如果有多对数字的和等于S，输出两个数的乘积最小的。

# -*- coding:utf-8 -*-
# bruteforce, 最简单的解法
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        list = []
        array.sort()
        for i in range(len(array) - 1):
            for j in range(i+1,len(array)):
                if array[j] == tsum - array[i]:
                    list.append((array[i],array[j] ))
        if not list:
            return
        print(list)
        first = list[0][0]
        second = list[0][1]
        for i in list:
            if i[0]*i[1] > first*second:
                first = i[0]
                second = i[1]
        return first, second


# -*- coding:utf-8 -*-
#在一个soted array里，离的越远，乘积越小
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        list = []
        array.sort()
        i = 0
        j = len(array) - 1
        while i <j:
            if array[i]+ array[j] == tsum:
                list.append(array[i])
                list.append(array[j])
                return list

                i = i +1
                j = j -1
            elif array[i] + array[j] < tsum:
                i = i+1
            else:
                j = j -1
        return list
test = Solution2()
print(test.FindNumbersWithSum([1,2,4,7,11,15],15))