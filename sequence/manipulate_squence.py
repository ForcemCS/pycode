my_list = [1,2,3,4,5]
print(my_list[0:2])
#----------------
l = [10, 20, 3, 40, 50]

l[2] = 30
print(l)

#---------------
l = [1, 20, 30, 5, 6]

l[1:3] = (2, 3, 4)
print(l)

#替换为右边任何可迭代对象（如列表、元组、字符串等）中的元素
l[1:3] = "python"
print(l)

#当间隔是正数的时候，需要注意
l = [1, 2, 3, 4, 5, 6, 7, 8]
print(l[1::2])

l[1::2] = 20, 40, 60, 80
print(l)

#---------
#---------
l = [1, 2, 3, 4, 5, 6, 7, 8]
print(l[1::2])

#l[1::2] = 20, 40, 60  四个元数用三个代替是错误的  
print(l)

#---------
l = [1, 2, 3, 4, 5, 6, 7, 8]

l[:-3:-1] = 'py'
print(l)

#---------
l = [1, 2, 3, 4, 5, 6]

print(l[::2])

##对原始list进行操作,删除列表中的切片部分
del l[::2]
print(l)

##扩展list
l = [1, 2, 3, 4, 5, 6]

l.append(7)
print(l)

l.append("python")
print(l)

l.append((1, 2, 3))
print(l)

l = [1, 2, 3, 4]

l.extend(["py"])
print(l)

l = [1, 2, 3, 4]

l.extend(["py"])
print(l)

l = [1, 2, 3, 4]

l.extend("py")
print(l)

###insert的使用,第二个元素后边插入ay
l = [1, 2, 3, 4]

l.insert(2, 'ay')
print(l)
