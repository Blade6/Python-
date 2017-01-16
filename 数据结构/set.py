#encoding:utf-8
s = set([1,2,3])
# 创建set需要提供一个list作为输入集合,set中不能有重复元素，有的话会自动过滤
print s
# set([1,2,3])

s.add(4)

s.remove(4)

#set可以看做数学上的集合，因此可以做交集、并集运算
s1 = set([1,2,3])
s2 = set([2,3,4])
print s1 & s2
# set([2,3])
print s1 | s2
# set([1,2,3,4])

#set中不能有可变对象，所以不能放list，理由是list是可变的，无法永久保证set内部不会有重复元素