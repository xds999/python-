"""
1、水仙花数
如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
那么问题来了，求 1000 以内的水仙花数（3 位数）
解题思路：先遍历出100-1000内的3位数数字
        再转字符串，再求和
"""
for i in range(100, 101):
    if i == sum([int(j)**3 for j in str(i)]):
        print(i)

"""
2、100以内的累加和
"""
a = 0
for i in range(101):
    a += i
print(a)
"""
3.如果一个正整数等于除它本身之外其他所有除数之和，就称之为完全数。
例如：6 是完全数，因为 6 = 1+2+3；
下一个完全数是 28 = 14+7+4+2+1。 求 1000 以下的完全数
解题思路：两个for循环，两个for循环先遍历出1000以内的所有数字，再用第二个for循环当作除数，如果能整除i的数字，添加到列表中
再判断列表中的数字和是否等于i本身如果等于i本身打印出结果
"""
# 常规解法
for i in range(1, 1001):
    s = []
    for j in range(1, i):
        if i % j == 0:
            s.append(j)
    if sum(s) == i:
        print("常规解题思路输出完整数：", i, end="")
        print()
# 简洁解题方式
for a in range(1, 1001):
    if a == sum([b for b in range(1, a)if a % b == 0]):
        print("列表推导式输出完全数：", a, end=" ")
        print()
"""
4.数字 1+2+3…+100 求和
求 1+2+3…+100 和
"""
a = 0
for i in range(1, 101):
    a += i
print(a)
# 一行代码解决 sum函数求和，range函数生成1-100以内的数字
print(sum([i for i in range(1, 101)]))
print(sum(range(101)))
"""
5.计算求 1-2+3-4+5-…-100 的值
奇数相加，偶数相减
"""
a = 0
for i in range(1, 101):
    if i % 2 == 0:
        a -= i
    else:
        a += i
print(a)
# 一行代码解决
print(sum([i if i % 2 != 0 else -1*i for i in range(1, 101)]))

"""
6.计算求 1+2-3+4-5... ...100 的值
这一题有点需要注意的是第一个数字 1 是正数，后面的数都是奇数相减，偶数相加
"""
a = 0
for i in range(1, 101):
    if i % 2 == 0 or i == 1:
        a += i
    else:
        a -= i
print(a)
