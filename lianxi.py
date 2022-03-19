"""
水仙花束
"""

a = 1
b = 0
while a <= 100:
    if a % 2 == 0 or a == 1:
        b += a
    else:
        b -= a
    a += 1
print(b)
