#Crop & Resize all images in directory

##This script is written with/for python2

##Description:

###This script crops the list of images from the center (both horizontally and vertically) and then resize that cropped image to given resolution

##Steps to resize the image

- hange he following variable in the code
- diroctory: this variable should contain the absolute address of the directory from where the photos will picked (and saved again).
- example: directory = '/home/nabeel/Desktop/photos/'

##Once the code is modified run following commands in terminal:
###(first change the working directory to folder with code file)

1. virtualenv -p python venv
2. source venv/bin/activate
3. pip install -r requirements.txt

Now you can run your code by giving the command

- python crop.py

####your cropped photos will be saved in the same directory with _cropped suffix.
