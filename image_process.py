import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# set the style of words
font = ImageFont.truetype("/Users/zhizhouqiu/Desktop/EC601/mini_project1/Arial.ttf", 50)

# open images/image1
imageFile = "1.jpg"
im = Image.open(imageFile)
# draw  The text needs to be added yourself.
draw = ImageDraw.Draw(im)
draw.text((0, 30), 'green grass football lawn pallone artificial turf', (50, 0, 0), font=font)    #word location/content/color/typeface
# save images
im.save("1_target.jpg")

#image2
imageFile = "2.jpg"
im = Image.open(imageFile)
draw = ImageDraw.Draw(im)
draw.text((0, 30), 'hand finger fashion accessory joint arm wrist girl', (50, 0, 0), font=font)
im.save("2_target.jpg")

#image3
imageFile = "3.jpg"
im = Image.open(imageFile)
draw = ImageDraw.Draw(im)
draw.text((0, 30), 'sport gridiron,football,player,tackle', (50, 0, 0), font=font)
draw.text((0, 100), 'protective equipment in gridiron football', (50, 0, 0), font=font)
im.save("3_target.jpg")

#image4
imageFile = "4.jpg"
im = Image.open(imageFile)
draw = ImageDraw.Draw(im)
draw.text((0, 30), 'baseball,player,bat ball games', (50, 0, 0), font=font)
draw.text((0, 100), 'baseball equipment,college baseball,baseball positions', (50, 0, 0), font=font)
im.save("4_target.jpg")

#image5
imageFile = "5.jpg"
im = Image.open(imageFile)
draw = ImageDraw.Draw(im)
draw.text((0, 30), 'ski pole,mountain range,skiing,freestyle skiing', (50, 0, 0), font=font)
draw.text((0, 100), 'piste,extreme sport,winter sport,ski equipment', (50, 0, 0), font=font)
im.save("5_target.jpg")

#image6
imageFile = "6.jpg"
im = Image.open(imageFile)
draw = ImageDraw.Draw(im)
draw.text((0, 30), 'sky,cloud,extreme sport,adventure,sunrise,rock', (50, 0, 0), font=font)
draw.text((0, 100), 'sport climbing,jumping,recreation,silhouette', (50, 0, 0), font=font)
im.save("6_target.jpg")

#image7
imageFile = "7.jpg"
im = Image.open(imageFile)
draw = ImageDraw.Draw(im)
draw.text((0, 30), 'blue,figure skating,figure skate,ice skating,skating', (50, 0, 0), font=font)
draw.text((0, 100), 'figure skater,gymnast,winter sport,recreation,girl', (50, 0, 0), font=font)
im.save("7_target.jpg")

#image8
imageFile = "8.jpg"
im = Image.open(imageFile)
draw = ImageDraw.Draw(im)
draw.text((0, 30), 'player,football player,sport venue,soccer player', (50, 0, 0), font=font)
draw.text((0, 100), 'grass,competition event,ball game,forward,team sport', (50, 0, 0), font=font)
im.save("8_target.jpg")

#image9
imageFile = "9.jpg"
im = Image.open(imageFile)
draw = ImageDraw.Draw(im)
draw.text((0, 30), 'trophy,award,close up,macro photography', (50, 0, 0), font=font)
draw.text((0, 100), 'computer wallpaper', (50, 0, 0), font=font)
im.save("9_target.jpg")
