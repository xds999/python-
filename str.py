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

"""
11.
判断字符串 a="welcome to my world" 是否包含单词 b="world"
包含返回 True，不包含返回 False
解题思路：
"""
a = "welcome to my world"
b = "world"
print(b in a)
# if b in a:
#     print(True)
# else:
#     print(False)
# find 查找字符串下标方式
c = a.find(b)
if c == -1:
    print(False)
else:
    print(True)
# 三元表达式
print(False if a.find(b) == -1 else True)
# 根据index查找下标
print(False if a.index(b) == -1 else True)

"""
12. 查找字符首次出现位置
输出指定字符串 A 在字符串 B 中第一次出现的位置,如果 B 中不包含 A,则输出-1 从 0 开始计数
A = "hello"
B = "hi how are you hello world, hello yoyo !"
解题思路：find和index内置函数，index函数在查找时，会自动打出a字符在b字符内首次出现的下标
"""
a = "hello"
b = "hi how are you hello world, hello yoyo !"
# index 方法 弊端：在没有查到时候会报异常
try:
    print("index方式查询：", b.index(a))
except:
    print(-1)
# find 方式查找 加起始位置和结束位置
print("find方式查询：", b.find(a, 1, 20))

"""
13.查找字符串最后一次出现位置
输出指定字符串 A 在字符串 B 中最后出现的位置,如果 B 中不包含 A,则输出-1
从 0 开始计数
A = "hello"
B = "hi how are you hello world, hello yoyo !"
解题思路：使用rfind内置函数，会直接查询出字符最后一次出现的位置，如果没有查到直接返回-1
"""
a = "hello"
b = "hi how are you hello world, hello yoyo !"
print(b.rfind(a))

"""
14.判断奇数偶数
给定一个数 a，判断一个数字是否为奇数戒偶数
解题思路：使用整除号 % 整除2后等于0的直接打印是个偶数 不整除的则是奇数
"""
a = 10
try:
    if a % 2 == 0:
        print("这是个偶数")
except:
    print("这是个基数")
"""
15.判断一个姓名是否姓王
输入一个姓名，判断是否姓王
解题思路：startswith --判断字符串首子字符，startswith()方法诧法：str.startswith(str, beg=0,end=len(string));
"""
# a = input("请输入你的姓名:")
# print(a.startswith('夏'))

"""
16. 判断是不是纯数字
如何判断一个字符串是丌是纯数字组成
解题思路：isdigit() 方法检测字符串是否叧由数字组成。如果字符串叧包含数字则返回 True 否则返
回 False
"""
a = "nihao"
print(a.isdigit())

"""
17. 字符串大小写转换
将字符串 a = "This is string example....wow!" 全部转成大写
解题思路：title()内置函数，默认给字符串中所有的小写字母转化为大写的
"""
a = "This is string example....wow!"
print("字符串中首个单词字母全部转化为大写", a.title())
print("字符串中字母全部转化为小写", a.lower())
print("字符串中每个字母转化为大写", a.upper())
print("字符串中第一个单词转化为大写:", a.capitalize())

"""
18.字符串去掉首尾空格
将字符串 a = " welcome to my world "首尾空格去掉
解题思路：strip()内置函数chars -- 移除字符串头尾指定的字符序列。
strip后面可以加指定去除的某一字符
"""
a = " welcome to my world "
b = "welcome to my world!"
print("去除首尾空字符：", a.strip())
print("去除字符串中最后的！号：", b.strip("！"))
"""
19. 字符串去掉左边指定空格或字符
将字符串 a = " welcome to my world ！"左边的空格去掉
解题思路：str.lstrip()内置方法
"""
a = " welcome to my world ！"
print("去除字符串左边的空字符：", a.lstrip())

"""
20. 字符串去掉右边指定空格或字符
将字符串 a = " welcome to my world ! "右边的空格去掉
解题思路：a.rstrip() --
"""
a = " welcome to my world !   "
print(a.rstrip())
"""
21. 去除字符串里面所有的空格
将字符串 a = " welcome to my world ! "里面的所有空格都去掉
解题思路：replace()内置函数，replace()方法诧法：str.replace(old, new[, max])
"""
a = " welcome to my world ! "
print(a.replace(" ", "", 2))

"""
22. 字符串去重后排序
s = "ajldjlajfdljfddd"，去重幵从小到大排序输出"adfjl"
解题思路：
1、先用set()去重，set去重后是一个无序的集合，set会改变原始数据的排序。再用sorted()来进行排序，排序完后需要用到join来进行拼接。
2、使用for循环，来进行判断，再逐个添加到新列表
"""
a = []
s = "ajldjlajfdljfddd"
print("".join(set(s))) # 未进行从小到大排序
print("".join(sorted(set(s))))
for i in s:
    if i not in a:
        a.append(i)
print("".join(sorted(a)))
"""
23.字符串去重保留顺序
s = "ajldjlajfdljfddd"，去重保留原来的顸序，输出"adfjl"
解题思路：sorted()内置函数，sorted函数不会改变数据本身的顺序
"""
s = "ajldjlajfdljfddd"
print("".join(sorted(s)))

"""
24.
打印菱形图案
题目 打印出如下图案（菱形）:
   *
  * *
 * * *
* * * *
 * * *
  * *
   *   
"""
#  最大行数
lines = 7
lines2 = (lines+1) // 2
start = ([2*i+1 for i in range(lines2)] + [2*i-1 for i in range(lines2-1, 0, -1)])
for i in start:
    #  求出空格数据
    kong = (lines - i) // 2
    print(" " * kong, "*" * i)

"""
25.输入一个正整数，判断是几位数
题目 给一个不多于 5 位的正整数，要求
一、求它是几位数，
二、逆序打印出各位数字。
解题思路：整数为int，len()函数不能判断整数的长度，所以先转为str类型，再用len函数来统计
逆序打印也是一样，字符串中的切片 [::-1] --字符串逆序排
"""
a = 12345
print(len(str(a)))
print(str(a)[::-1])

"""
26.判断字符相关
1. isupper() 方法检测字符串中所有的字母是否都为大写。叧判断 a-z 的英文字符是丌是
全部大写 A-Z
解题思路:isupper()内置函数，用来判断字符串中字母是否全部为大写，如果全部为大写则返回True，如果不是全部为大写则返回False
"""
a = "hello world"
b = "HELLO"
# False
print(a.isupper())
# True
print(b.isupper())

"""
27.方法检测字符串是否由小写字母组成。
解题思路：islower()内置函数，直接来判断字符串内是否全部为小写字母。符合返回True，不符合返回False
"""
a = "hello"
print(a.islower())
"""
28. 方法检测字符串中所有的单词拼写首字母是否为大写，丏其他字母为小写。
解题思路：istitle()，自动判断字符串中首字母是否为大写，符合返回True 不符合返回False
"""
a = "Hello"
print(a.istitle())
"""
29. isalnum() 方法检测字符串是否由字母和数字组成。判断 string 至少有一个字符幵丏所
有字符都是字母戒数字则返回 True,否则返回 False
 isalpha() 方法检测字符串是否叧由字母组成。
 isdigit() 方法检测字符串是否叧由数字组成
"""
a = "hello12"
print(a.isalnum())
