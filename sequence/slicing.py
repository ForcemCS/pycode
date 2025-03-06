l = [ [0, 0, 0, 0], [1, 1, 1], [2, 2, 2]]

#由l的前两个元素组成的新list,元素指向的相同的内存地址
sub = l[0:2]
print(sub)

print(sub[0] is l[0])

print(sub is l )

##这个新的lits，index 0 指向了新的位置。不会改变l[0]
sub[0] = "Python"

print(sub)
print(l)

sub[1][0] = 100
print(sub)
print(l)

##-------------------
l1 = [1, 2, 3, 4]

l2 = l1[:]

print(l1 is l2)

##浅副本，与上边的不同
l2[0] = 100
print(l1,l2)

##---------
s = "hello world"

##start省略，表示从-1开始，end省略，默认值是0
print(s[::-1])
print(s[1:6:1])
print(s[1:6])

print(s[:-4:-1])
print(s[2::-1])
print(repr(s[:4:-1]))

## 判断是不是关于e对称

a = "racecar"

print(a == a[::-1])