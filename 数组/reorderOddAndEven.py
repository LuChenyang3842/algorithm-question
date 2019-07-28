#输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
# 所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

#@方法一：
#使用python deque数据类型， list分别从左往右和从右往左遍历
# 从左往右遍历，找到奇数,deque.appendlef
# 从左往右遍历，找到偶数，deque,append
from collections import deque
class Solution:
    def reOrderArray(self, array):
        dq = deque()
        x= len(array)
        for i in range(x):
            if not self.isEven(array[x-i-1]):
                dq.appendleft(array[x-i-1])
            if self.isEven(array[i]):
                dq.append(array[i])
        return list(dq)
            
        # write code here
    def isEven(self, num):
        if num%2 == 0:
            return True
        else:
            return False

#@方法二：
#创建两个数组， 第一个数组储存奇数，第二个数组储存偶数，最后合并两个数组

class Solution2:
    def reOrderArray(self, array):
        odd = []
        even = []
        for num in array:
            if num%2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return odd + even
test = Solution2()
print(test.reOrderArray([1,2,3,4,5]))