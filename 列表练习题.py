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
