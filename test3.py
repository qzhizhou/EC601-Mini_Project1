import os

class ImageRename():
    def __init__(self):
        self.path = '/Users/zhizhouqiu/desktop/ec601/mini_project1/code/ffmpeg'

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)

        i = 0

        for item in filelist:
            if item.endswith('.jpg'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(str(i) + '.jpg')
                os.rename(src, dst)

                i = i + 1


if __name__ == '__main__':
    newname = ImageRename()
    newname.rename()