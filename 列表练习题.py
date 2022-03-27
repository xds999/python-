"""
1、反转（判断对称）
如何判断一个数组是对称数组：
要求：判断数组元素是否对称。例如[1，2，0，2，1]，[1，2，3，3，2，1]这样的都是对
称数组
用 Python 代码判断，是对称数组打印 True，丌是打印 False,如：
x = [1, "a", 0, "2", 0, "a", 1]
解题思路：
1、切片反转列表内的字符，再来做比较。或者用reversed函数处理后来做比较
2、reversed函数调用后，返回的是一个object 对象，需要在前面转list //reversed只适用于list
3、深拷贝方式来处理
"""
# 切片判断
x = [1, "a", 0, "2", 0, "a", 1]
print(x == x[::-1])
# reversed函数处理
print(x == list(reversed(x)))
# 深拷贝
import copy
b = copy.deepcopy(x)
b.reverse()
print(x == b)

"""
2、列表切片
如果有一个列表 a=[1,3,5,7,11]
问题：1 如何让它反转成[11,7,5,3,1]
2.取到奇数位值的数字，如[1,5,11]
"""
a = [1, 3, 5, 7, 11]
# 反转后的结果
print(sorted(a, reverse=True))
# 切片
print(a[0:5:2])

"""
3.对列表 a 中的数字从小到大排序
a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
解题思路：python 的排序有两个方法，一个是 list 对象的 sort 方法，另外一个是 builtin 函数里面
sorted，主要区别：
sort 仅针对于 list 对象排序，无返回值, 会改变原来队列顸序
sorted 是一个单独函数，可以对可迭代（iteration）对象排序，不局限于 list，它不改变原
生数据，重新生成一个新的队列
"""
a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
print(sorted(a))
a.sort()
print(a)

"""
4.取出最大值最小值
L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
"""
L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
print(min(L1))
print(max(L1))

"""
5.找出列表中单词最长的一个 和 单词最短的一个
a = ["hello", "world", "yoyo", "congratulations"]
解题思路：通过匿名函数来统计每个字符的长度，再调用min方法来判断哪个字符串最短
        通过匿名函数来统计每个字符的长度，再调用max方法来判断哪个字符串最短
"""
a = ["hello", "world", "yoyo", "congratulations"]
print(min(a, key=lambda x: len(x)))
print(max(a, key=lambda x: len(x)))

"""
6.切片取出列表中最大的三个数
取出列表中最大的三个值
L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
解题思路：sorted函数排序后进行切片，逆序排列取前面三个数[:3]  or  升序排列取最后三个数 [-3:]
"""
L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
print(sorted(L1)[-3:])
print(sorted(L1, reverse=True)[:3])

"""
7. 列表按绝对值排序
a = [1, -6, 2, -5, 9, 4, 20, -3] 按列表中的数字绝对值从小到大排序
解题思路：sorted()参数说明
iterable 可迭代对象，如：str、list、tuple、dict 都是可迭代对象（这里不局限于 list
了）
key 用列表元素的某个属性戒函数进行作为关键字（此函数叧能有一个参数）
reverse 排序规则. reverse = True 降序戒者 reverse = False 升序，默认升序
return 有返回值值，返回新的队列
"""
a = [1, -6, 2, -5, 9, 4, 20, -3]
a.sort(key=lambda x:abs(x))
print(a)
print(sorted(a, key=lambda x: abs(x)))

"""
8.按字符串长度排序
b = ["hello", "helloworld", "he", "hao", "good"]
按 list 里面单词长度倒叙
解题死里：sort 或 sorted函数搭配lambda函数使用，lambda函数输出每个单词的长度，外层再使用sort或 sorted函数来进行排序。reverse为True
的话，只降序排列的
"""
b = ["hello", "helloworld", "he", "hao", "good"]
print(sorted(b, key=lambda x: len(x), reverse=True))
b.sort(key=lambda x:len(x), reverse=True)
print(b)

"""
9. 去重不排序
L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
如何用一行代码得出[1, 2, 3, 5, 11, 33, 88]
L2 = [1, 2, 3, 4, 5] ,L[10:]结果是多少（报错？还是 None，还是[]）
"""
L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
L2 = [1, 2, 3, 4, 5]
print(list(set(L1)))
print(L2[10:])

"""
10.去重保留顺序
将列表中的重复值取出(仅保留第一个)，要求保留原始列表顸序
如 a=[3, 2, 1, 4, 2, 6, 1] 输出[3, 2, 1, 4, 6]
"""
a = [3, 2, 1, 4, 2, 6, 1]
s = []
for i in a:
    if i not in s:
        s.append(i)
print(s)
# 一行代码解决
print(sorted(set(a), key=lambda x: a.index(x)))
