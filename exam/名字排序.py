# 时间限制：C/C++语言 3000MS；其他语言 5000MS
# 内存限制：C/C++语言 131072KB；其他语言 655360KB
# 题目描述：
# 马上就要开学了，教务处的老师拿到了新生的名单，现在他需要根据考生的姓名录入一个拼音版的新名单。

# 老师录入时，需要输入姓和名(例如：ZHANG SAN，字母均为大写，姓名以空格隔开)，并且要将这些人按一定规则排序。

# 排序的方式如下：

# 首先，按照该姓的出现次数排序，即：姓出现次数多的人先排序

# 其次，若两个人的姓出现的次数一样多（或者是同一个姓），按照原名单的顺序。



# ZHANG SAN
# LI SI
# WANG WU
# WANG LIU
# WANG QI
# ZHANG WU
# LI WU

# WANG WU
# WANG LIU
# WANG QI
# ZHANG SAN
# LI SI
# ZHANG WU
# LI WU

from collections import Counter
import sys

name_list = []

while 1:
  s = input()
  if s != "":
      name_list.append(s)  
  else:
    break
    

def rankName(name_list):
    ctr = Counter()
    for name in name_list:
        full_name = name.split(" ")
        ctr[full_name[0]] += 1
    temp_counter = ctr.most_common(len(list(ctr)))
    name_ranking = []
    # for key in items 
    temp_value = 0
    temp_list = []
    for item in temp_counter:
        if temp_value == item[1]:
            temp_list.append(item[0])
        else:
            temp_value = item[1]
            name_ranking.append(temp_list)
            temp_list = []
            temp_list.append(item[0])
    name_ranking.append(temp_list)

    res = []
    for last_name in name_ranking:
        for name in name_list:
            temp_last_name = name.split(" ")[0]
            if temp_last_name in last_name:
                res.append(name)
    for name in res:
        sys.stdout.write(name +"\n")


# rankName(["zhang san", "si li", "lu san"])
rankName(name_list)