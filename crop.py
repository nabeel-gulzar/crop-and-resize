#Python 2.7

from PIL import Image
import glob
import os

def resize_aspect(im, res):
    return im.resize((res,res),Image.ANTIALIAS)

directory = '/home/in01-nbk-570/Desktop/photos/'
files_address_list = "{directory}*.png".format(directory=directory)
imgList=glob.glob(files_address_list)
resolution = 1024
for img in imgList:
    im = Image.open(img)
    w,h = im.size
    smaller_side = min(w,h)
    center = [int(w/2.0),int(h/2.0)]
    half = smaller_side/2
    box = (center[0]-half, center[1]-half, center[0]+half, center[1]+half)

    cropped_image = im.crop(box)
    w,h = cropped_image.size
 
    resized_image=resize_aspect(cropped_image,resolution)
    w,h = resized_image.size

    file_name, file_extension=os.path.splitext(img)
    cropped_file_name = "{file_name}_cropped.png".format(file_name=file_name)
    resized_image.save(cropped_file_name, "PNG")
