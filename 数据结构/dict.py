# encoding:utf-8
# dict字典，即其他语言的map键值对
d = {'Michael':95, 'Bob':75, 'Nancy':85}
print d['Bob']
# 75

d['Adam'] = 65
# 添加

print 'Thomas' in d
# False
# d中没有Thomas的键

print d.get('Thomas')
#如果key不存在，返回None，但交互式命令行不显示，此处是文本执行，会显示出来
print d.get('Thomas',-1)
#如果key不存在，返回指定的value

del d['Bob']
# d.pop('Bob'),功能也是删除，但是会在交互窗口输出被删除的值
# 删除键Bob
print d
# {'Michael':95, 'Adam':65, 'Nancy':85}
# dict中存放的顺序与key放入的顺序没有关系

#优点：查找和插入速度极快，与key的数目无关
#缺点：占用大量内存，用空间换时间
#list与之正相反

#dict的key必须是不可变的，所以不能是list

my_dict = {
    "Name": "Guido",
    "Age": 46,
    "BDFL": True
}
print my_dict.items()
print my_dict.keys()
print my_dict.values()