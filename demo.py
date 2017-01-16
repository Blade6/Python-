# -*- coding:utf-8 -*-
# 九张图程序
# crop()函数接收1个参数，这个参数通常是个元组。
# 元组中包含左上角坐标，宽度，高度。
# 宽度和高度都是从被截的图的(0,0)算起，圈定的区域。
# 左上角坐标是在这个圈定区域上的一个坐标，以这个坐标为起点，
# 其右边和下方的剩余区域都被截出来。

# paste()函数接收粘贴到原图的图像，粘贴区域
# 粘贴区域：想想如果crop这个区域你会怎么写，paste同理。

# 使用说明，首先置于图片所在的目录

file = raw_input("Write the file name > ")

from PIL import Image
img = Image.open(file)
width,height = img.size
imtype = (img.format).lower()

# 判断原图是否正方形，把它处理成正方形
if width != height:
	length = max(width,height)
	Im = Image.new('RGB',(length,length),0xffffff)

	if width > height:
		Im.paste(img,(0,(length-height)/2,width,height+(length-height)/2))
	else:
 		Im.paste(img,((length-width)/2,0,width+(length-width)/2,height))
else:
	Im = img
	length = width

# 把正方形图分成九块
for i in range(1,4):
	# 每次截取原图的高度方向的1/3
	region1 = (0,(i-1)*length/3,length,i*length/3)
	im = Im.crop(region1)
	for j in range(1,4):
		# 每次截取上一步所得到的图的宽度方向的1/3
		region2 = ((j-1)*length/3,0,j*length/3,length/3)
		image = im.crop(region2)
		filename = "%d-%d.%s" % (i,j,imtype)
		image.save(filename)

print "Done!"