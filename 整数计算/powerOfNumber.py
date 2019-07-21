#给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。 较为简单

class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent ==0:
            return 1
        if exponent > 0:
            result = 1
            for i in range (0,exponent):
                result =  result*base
            return result
        else:
            result = 1
            for i in range (0,-exponent):
                result =  result*base
            return float(1/result)
