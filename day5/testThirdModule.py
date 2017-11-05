# 测试安装的第三方模块

from PIL import Image

image = Image.open('test.png')
print(image.format, image.size, image.mode)
image.thumbnail((200, 100))
image.save('thumb.jpg', 'jpeg')

