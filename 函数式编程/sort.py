# encoding:utf-8
# 默认升序
print sorted([36,5,12,9,21])

def reversed_cmp(x,y):
	if x > y:
		return -1
	elif x < y:
		return 1
	else:
		return 0
# 通常规定，对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，则返回1。
# 也就是说，按升序排列的话,X > Y时，return的应该是1，但这里return -1，就是进行了降序的判断
# sorted函数是把cmp(x,y)返回值为-1的x排前面的

print sorted([36,5,12,9,21], reversed_cmp)