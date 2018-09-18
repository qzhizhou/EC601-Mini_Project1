import io
import os
import sys
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

a=''
c=''
b= ['bus', 'pear','and','path','AAAAAA']

# set the style of words
font = ImageFont.truetype("/Users/zhizhouqiu/Desktop/EC601/mini_project1/Arial.ttf", 50)

pic_base_dir = "/Users/zhizhouqiu/desktop/ec601/mini_project1/code"
pic_list = []

for file in os.listdir(pic_base_dir):
	if file.endswith(".jpg"):
		write_name = file #图片路径 + 图片名 + 标签
		pic_list.append(write_name)

for pic_name in range(0,len(pic_list)):


	# open images/image1
	imageFile = pic_name
	im = Image.open(imageFile)

	# draw  The text needs to be added yourself.
	draw = ImageDraw.Draw(im)
	for i in range(0,4) :
	    a = b[i] + ',' + a
	draw.text((0, 30), a, (50, 0, 0), font=font)    #word location/content/color/typeface
	for i in range(4,len(b)) :
	    c = b[i] + ',' + c
	draw.text((0, 100), c, (50, 0, 0), font=font)

	# save images
for num in range(1, 9):
	t = str(num) + 'target'
	im.save('t.jpg')
