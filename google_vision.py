import io
import os
import sys
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

class GoogleVision():
    def __init__(self):
        pass

    def getNumOfImages(self):
        count = 0
        for file in os.listdir():
            if file.endswith(".jpg"):
                count = count + 1
        return count

    def getLabels(self):
        # Instantiates a client
        client = vision.ImageAnnotatorClient()

        # set the style of words
        font = ImageFont.truetype("/Users/zhizhouqiu/Desktop/EC601/mini_project1/Arial.ttf", 30)

        label_list = [] # creat a list to store labels 
        for file in os.listdir(): #file is the image name of current_dir
            if file.endswith(".jpg"):
                pic = file #image path + name +label
                file_name = os.path.join(os.path.dirname(__file__), pic)

                # Loads the image into memory
                with io.open(file_name, 'rb') as image_file:
                    content = image_file.read()

                image = types.Image(content=content)

                # Performs label detection on the image file
                response = client.label_detection(image=image)
                labels = response.label_annotations
                #templist = []
                # print labels in every picture
                #print(pic)
                # for i in range(0,3):
                #     #print(label.description)
                #     templist.append(labels[i].description)
                label_list.append(labels[0].description)
                # print('\n')
                # print(label_list)
                # print('\n')
        return label_list
                # start to draw
                # a=''
                # c=''
                # imageFile = pic
                # im = Image.open(imageFile)

                # # draw
                # draw = ImageDraw.Draw(im)
                # if len(label_list) < 6:
                #     for i in range(0, len(label_list)):
                #         a = label_list[i] + a + '/ '
                #     draw.text((0, 30), a, (50, 0, 0), font=font)
                # else:
                #     for i in range(0, 6):
                #         a = label_list[i] + '/ ' + a
                #     draw.text((0, 30), a, (50, 0, 0), font=font)  # word location/content/color/typeface
                #     for i in range(7, len(label_list)):
                #         c = label_list[i] + '/ ' + c
                #     draw.text((0, 100), c, (50, 0, 0), font=font)
                # im.save(pic)

        #Rename all the .jpg files
        # class ImageRename():
        #     def __init__(self):
        #         self.path = '/Users/zhizhouqiu/Desktop/EC601/mini_project3/Test/EC601-Mini_Project1'
            
        #     def rename(self):
        #         filelist = os.listdir(self.path)
        #         total_num = len(filelist)
                
        #         i = 0
                
        #         for item in filelist:
        #             if item.endswith('.jpg'):
        #                 src = os.path.join(os.path.abspath(self.path), item)
        #                 dst = os.path.join(str(i) + '.jpg')
        #                 os.rename(src, dst)
                        
        #                 i = i + 1
                #print(i)


# if __name__ == '__main__':
    # newname = ImageRename()
    # newname.rename()
    # twitterAnalysis = GoogleVision()
    # twitterAnalysis.getLabels()
    # print()
