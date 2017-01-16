# -*- coding:utf-8 -*-
# 使用第三方模块

from PIL import Image
im = Image.open('test.png')
print im.format, im.size, im.mode

# im.thumbnail((200,100))
# im.save('thumb.jpg', 'JPEG')