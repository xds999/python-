"""
1、水仙花数
如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
那么问题来了，求 1000 以内的水仙花数（3 位数）
解题思路：先遍历出100-1000内的3位数数字
        再转字符串，再求和
"""
for i in range(100, 1000):
    if i == sum([int(j)**3 for j in str(i)]):
        print(i)


