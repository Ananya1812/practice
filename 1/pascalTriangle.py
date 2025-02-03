# https://leetcode.com/problems/pascals-triangle/description/
def pascal_Triangle(n):
    tri = [[1]*(i+1)for i in range(n)]
    for i in range(2,n):
        for j in range(1,i):
            tri[i][j] = tri[i-1][j-1] + tri[i-1][j]
            
    for row in tri:
        print(" ".join(map(str,row)))
        
n = int(input())
pascal_Triangle(n)
    
    
    