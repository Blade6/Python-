执行单元测试的方法(推荐二)：
一
最简单的运行方式是在mydict_test.py的最后加上两行代码：
if __name__ == '__main__':
    unittest.main()
然后命令行$ python mydict_test.py

二
在命令行通过参数-m unittest直接运行单元测试
$ python -m unittest mydict_test