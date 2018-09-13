
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# set the style of words
font = ImageFont.truetype("/Users/zhizhouqiu/Desktop/EC601/mini_project1/Arial.ttf", 50)

# open images
imageFile = "1.jpg"
im1 = Image.open(imageFile)

# draw
draw = ImageDraw.Draw(im1)
draw.text((0, 30), 'green grass football lawn pallone artificial turf', (50, 0, 0), font=font)    #设置文字位置/内容/颜色/字体
                        #Just draw it!

# save images
im1.save("target.jpg")
