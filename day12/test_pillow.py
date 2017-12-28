# Python常用第三方模块---pillow

from PIL import  Image,ImageFilter,ImageDraw,ImageFont,ImageFilter
import random

def thumbnail():

    #打开一个jpg图像文件
    im=Image.open('test.jpg')
    # 获取图像的尺寸
    w,h=im.size
    print('Original image size:%sx%s' %(w,h))

    #缩放至50%
    im.thumbnail((w//2,h//2))

    print("Resize image to:%sx%s" %(w//2,h//2))

    #把缩放后的图像用jpeg格式保存
    im.save('thumbnail.jpg','jpeg');

#其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全

#thumbnail()

def filter():
    # 打开一个jpg图像文件
    im = Image.open('test.jpg')
    # 应用模糊滤镜
    im2=im.filter(ImageFilter.BLUR)
    im2.save('blur.jpg','jpeg')

#filter()





