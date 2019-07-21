# @question: 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

#关于补码的解释和原理： https://blog.csdn.net/gaoshuang5678/article/details/50554143

#python 位移运算符：

#  << 左移 高位溢出，低位补0， 没有溢出的情况下，数学意义：左移n位等于乘以2的n次方
# >> 右移 低位溢出，高位补符号位（整数补0，负数补1），
# |  位或： 两个1才为1
# & 位与：只要有一个1就是1
# ^ 位异或： 位加法
# ~ 非： 取反


#用与操作，和1对比，从右移0位开始，最后一次右移31位，计算共有几个1.
class Solution:
    def NumberOf1(self, n):
        # write code here
        return sum([(n >> i & 1) for i in range(0,32)])
