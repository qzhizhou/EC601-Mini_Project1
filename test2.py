import io
import os
import sys
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

a=''
c=''
b= ['figure skater', 'figure skate', 'figure skating', 'ice skating', 'gymnast', 'competition', 'winter sport', 'dancer']

# set the style of words
font = ImageFont.truetype("/Users/zhizhouqiu/Desktop/EC601/mini_project1/Arial.ttf", 50)

pic_base_dir = "/Users/zhizhouqiu/desktop/ec601/mini_project1/code"
pic_list = []

for file in os.listdir(pic_base_dir):
	if file.endswith(".jpg"):
		write_name = file #图片路径 + 图片名 + 标签
		pic_list.append(write_name)
print(pic_list)

for pic_name in pic_list:
	# open images/image1
	imageFile = pic_name
	im = Image.open(imageFile)

	# draw  The text needs to be added yourself.
	draw = ImageDraw.Draw(im)
	if len(label_list)<7:
		for i in range(0,len(label_list)):
			a = label_list[i] + ',' + a
		draw.text((0, 30), a, (50, 0, 0), font=font)
	else:
	    for i in range(0, 7):
		    a = label_list[i] + ',' + a
	        draw.text((0, 30), a, (50, 0, 0), font=font)  # word location/content/color/typeface
	    for i in range(7, len(label_list)):
		    c = label_list[i] + ',' + c
	        draw.text((0, 100), c, (50, 0, 0), font=font)
	im.save(pic_name)

