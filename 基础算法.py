"""
1、水仙花数
如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
那么问题来了，求 1000 以内的水仙花数（3 位数）
解题思路：先遍历出100-1000内的3位数数字
        再转字符串，再求和
"""
for i in range(100, 1001):
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
# 列表推导式
print(sum([i if i % 2 == 0 or i == 1 else -1*i for i in range(1, 101)]))
"""
7.计算 1-n 之间的所有 5 的倍数之和
定义一个函数：计算 1-n 之间的所有 5 的倍数之和，默认计算 1-100 （ n 是 一个整数)
解题思路：for循环从1-100， 如果能整除5的数字，添加到一个新的列表当中，再用sun求和
"""
a = 5
s = []
for i in range(1, 101):
    if i % 5 == 0:
        s.append(i)
print(sum(s))
# 列表推导式，快速生成一个列表，当i能整除5的时候，输出i再使用sum函数求和
print(sum([i for i in range(1, 101) if i % 5 == 0]))


def case_1(n):
    response = sum([i for i in range(1, n)if i % 5 == 0])
    return response


result = case_1(101)
print("封装函数后的输出：{}".format(result))


"""
8. n 个自然数的立方和
计算公式 1**3 + 2**3 + 3**3 + 4**3 + …….+ n**3
实现要求：
输入 : n = 5
输出 : 225
对应的公式 : 1**3 + 2**3 + 3**3 + 4**3 + 5**3 = 225
解题思路：列表推导式 / 给一个变量赋个空值，然后累加i**3
pow函数，pow(数据源, 乘以几次方)
"""
b = 1
c = 5
s = 0
while b <= c:
    s += b ** 3
    b += 1
print("while循环求出：{}".format(s))
d = 0
for i in range(1, 6):
    d += i**3
print("for循环求出：", d)
# 列表推导式，循环遍历，生成一个快速的可迭代的list，再返回三次方的i， 再用sum进行求和
print("列表推导式求出：", sum([int(i) ** 3for i in range(1, 6)]))
print("列表推导式求出：", sum([i**3 for i in range(1, 6)]))
print("pow函数解决：", sum([pow(i, 3) for i in range(1, 6)]))
# n = input("请输入一个整数：")
# print("pow函数求出：", sum([pow(i, 3)for i in range(1, int(n)+1)]))

"""
9.求出10的阶乘
阶乘的意思: 10!=10x9x8x7x6x5x4x3x2x1
"""
a = 1
s = 1
d = 1
while a <= 10:
    s *= a
    a += 1
print(s)
for i in range(1, 11):
    d *= i
print(d)
print(sum([i*j for i in range(1, 11) for j in range(1, 11)]))
"""
10. 求 1+2!+3!+...+10!的和
跟上面一题思路差不多，多一个累加求和
"""
a = 1
s = 0
# for循环
for i in range(1, 11):
    # 求出10到1的阶乘
    a *= i
    # 再累加每个数的阶乘
    s += a
print(s)
# while循环
b = 1
f = 1
d = 0
while b < 11:
    f *= b
    d += f
    b += 1
print(d)

"""
11.求 s=a+aa+aaa+aaaa+aa...a 的值
如 n = 5  a = 3
解题思路：
"""
a = 0
s = 0
for i in range(5):
    a += 3*10**i
    s += a
print(s)

print(sum([int('3' * i)for i in range(1, 6)]))

"""
12.斐波那契数列
已知一个数列：1、1、2、3、5、8、13、。。。。的规律为从 3 开始的每一项都等于其前两
项的和，这是斐波那契数列。
求满足规律的 100 以内的所有数据
"""
num = 100
a = 0
b = 1
n = 1
while n <= 100:
    n = a+b
    a, b = b, n
    if n >= 100:
        break
    else:
        print(n, end=" ")



