# 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
# 但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，
# 机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
# 请问该机器人能够达到多少个格子？

class Solution:
    def __init__(self):
        self.max = 0
    def movingCount(self, threshold, rows, cols):
        if threshold <= 0:
            return 1
        matrix = [0]*(cols*rows)
        self.findPath(0,0,threshold,rows,cols,matrix)
        return self.max
    
    def findPath(self,i,j,k,rows,cols,matrix):
        matrix[i*cols + j] = 1
        self.max =  self.max + 1
        if i + 1 < rows and self.largeThanThreshold(i + 1, j,k) and matrix[(i+1)*cols+j] == 0:
            return self.findPath(i +1,j,k,rows,cols,matrix)
        if j + 1 < cols and  self.largeThanThreshold(i, j+1,k)and matrix[i*cols+j+1] == 0:
            return self.findPath(i,j+1,k,rows,cols,matrix)
        if i -1 >= 0 and  self.largeThanThreshold(i - 1, j,k) and matrix[(i-1)*cols+j] == 0:
            return self.findPath(i -1,j,k,rows,cols,matrix)
        if j - 1 >= 0 and  self.largeThanThreshold(i + 1, j,k) and matrix[i*cols+j-1] == 0:
            return self.findPath(i,j-1,k,rows,cols,matrix)
    
    
    def largeThanThreshold(self,i,j,k):
        tempList = map(int,list(str(i) + str(j)))
        # print(sum(tempList))
        return sum(tempList) <= k


test = Solution()
print(test.movingCount(5,10,10))

# Below are correct solution

class Solution:
    def movingCount(self, threshold, rows, cols):
         
        matrix=[[ False for j in range(cols)] for i in range(rows)]
        def moving(threshold,rows,cols,i,j,matrix):
            if (i < 0 or i >= rows or j < 0 or j >= cols or self.threshhold_check(i,j) > threshold or matrix[i][j] == 1):
                return 0
            matrix[i][j]=True
            return moving(threshold,rows,cols,i,j-1,matrix)+moving(threshold,rows,cols,i-1,j,matrix)+moving(threshold,rows,cols,i+1,j,matrix)+moving(threshold,rows,cols,i,j+1,matrix)+1
          
        return moving(threshold,rows,cols,0,0,matrix)  
                 
         
         
    def threshhold_check(self,i,j):
        sum_result=0
        while i>0:
            sum_result+=i%10
            i/=10
        while j>0:
            sum_result+=j%10
            j/=10
        return sum_result