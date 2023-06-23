'''
当需要不同id数量超过200的时候可以考虑在IDE上for循环使用random.randint(a,b)一次性创建好id再复制粘贴到机考上
randint(a,b) 与 range(a,b)一样, 左闭右开
'''
from random import *

before_id = '123456789123456'

lst = []
count = 0
for _ in range(500):
    i, j, k = randint(1, 10), randint(1, 10), randint(1, 10)
    after_id = str(i) + str(j) + str(k)
    id = before_id + after_id
    count += 1
    if id not in lst:
        lst.append(id)
    if len(lst) == 101:
        break
    
print(count)
# print(lst)
# print(len(lst))