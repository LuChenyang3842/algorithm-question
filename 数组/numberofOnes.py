# 题目描述
# 求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、
# 10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负
# 整数区间中1出现的次数（从1 到 n 中1出现的次数）。

# -*- coding:utf-8 -*-
from collections import Counter
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        total_num = 0
        for i in range (n+1):
            temp_list = list(str(i))
            print(temp_list)
            ctr = Counter(temp_list)
            total_num +=  ctr['1']
        return total_num

