class Solution:
    def LeftRotateString(self, s, n):
        s_list = list(s)
        move = len(s_list) % n
        if move == 0:
            return s
        s_left = ''.join(s_list[])
        s_left = ''.join(s_list[move:])
        return s_left + s_right