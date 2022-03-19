"""
一：字符串切片
1.
已知 a 的值为"hello"，b 的值为"world"，如何交换 a 和 b 的值？
得到 a 的值为"world"，b 的值为"hello"
"""
a = "hello"
b = "world"
a, b = b, a
print(a, b)

"""
2.
回文的定义："回文" 就是正读倒读都一样的。
如奇数个："98789"，这个数字正读是"98789" 倒读也是"98789"。
偶数个数字"3223"也是回文数。
字母 "abcba" 也是回文。
判断一个字符串是否是回文字符串，是打印 True， 丌是打印 False
解题思路：切片 ::-1全部反转字符串
        迭代器 --reversed
reversed：将其元素从后向前颠倒构建成一个新的迭代器        
"""
c = "abcba"
print(c == c[::-1])
print(reversed(c))  # 返回一个object
print(c == "".join(reversed(c)))

"""
3.
已知一个字符串为 "hello_world_yoyo", 如何得到一个队列 ["hello","world","yoyo"]
split 切割
"""
d = "hello_world_yoyo"
print(d.split("_"))

"""
4.
让用户输入任意的用户名不密码，然后将他输入的用户名与密码打印出来，如用户输入
abc/123 ，则打印
"""
# e = input("请输入用户名和密码（格式username/password）")
# f = e.split('/')
# print('用户名：{}'.format(f[0]))
# print('密码：{}'.format(f[1]))

"""
5.
有个列表 ["hello", "world", "yoyo"]如何把把列表里面的字符串联起来，
得到字符串 "hello_world_yoyo"
'sep'.join(iterable)语法 sep是分隔符，iterable是一个可迭代对象
"""
g = ["hello", "world", "yoyo"]
print("_".join(g))

"""
6.
把字符串 s 中的每个空格替换成"%20"
输入：s = "We are happy."
输出："We%20are%20happy."
replace 替换 replace("替换的元素", "替换后的元素")
"""
h = "We are happy"
print(h.replace(" ", "%20"))

"""
7. 九九乘法表
"""
# for循环
for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j} * {i} = {i*j}', end="\t")
    print("")
# while循环
q = 0
while q < 10:
    j = 1
    while j <= q:
        print(f'{j} * {q} = {j*q}', end='\t')
        j += 1
    print()
    q += 1

"""
8.找出单词 "welcome" 在 字符串"Hello, welcome to my world." 中出现的位置，找丌到
返回-1
"""
e = "Hello, welcome to my world."
print(e.index('welcome'))
print(e.find('welcome'))

"""
9.统计字符串“Hello, welcome to my world.” 中字母 w 出现的次数
统计单词 my 出现的次数
可迭代对象.count统计函数
"""
print(e.count('w'))

"""
10.统计每个字符出现的次数
题目:输入一个字符串 str, 输出第 m 个叧出现过 n 次的字符，如在字符串 gbgkkdehh 中,
找出第 2 个叧出现 1 次的字符，输出结果：d
解决思路：
利用 collections 库的 Counter 方法统计字符串每个单词出现的次数
Counter 方法对字符串\列表\元祖\字典迚行计数,返回一个字典类型的数据,键是元素,值是
元素出现的次数
"""
# 常规解决方式
from collections import Counter
a = "gbgkkdehh"
c = []
for i in dict(Counter(a)).items():
    if i[1] == 1:
        c.append(i[0])
print(c[1])
# 列表推导式

print([i[0] for i in dict(Counter(a)).items() if i[1] == 1][1])
