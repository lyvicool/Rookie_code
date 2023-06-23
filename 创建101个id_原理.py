'''
1. 将复杂的18位字符串转换成3位字符串的操作 ----- 字符串拼接
2. 字符串不好操作,转换为列表思维 ----- 位数少时可以直接创建列表,位数多时可以用extend点方法但是记得赋值
3. 假设ijk是三位数的十进制数字,k = 9时 k+1 -> k = 0, j += 1 ; j = 9时,j + 1 -> j = 0, i += 1

涉及的方法:
①join点方法前面是以什么进行拼接,后面是拼接的迭代对象,拼出来的是字符串
②extend点方法,将迭代对象拆成元素添加到列表中: 将字符串拆成字符元素添加到列表中;将列表拆成元素添加到列表中;
int类型不是迭代对象,拆不了
'''

before_id = '123456789123456'
idlist = []
i,j,k = 0,0,0

for _ in range(101):
    if k == 10:
        j += 1
        k = 0
    if j == 10:
        i += 1
        j = 0

    after_id = [str(i) ,str(j) ,str(k)]
    id = before_id + ''.join(after_id)
    idlist.append(id)
    k += 1

print(idlist)
print(len(idlist))

