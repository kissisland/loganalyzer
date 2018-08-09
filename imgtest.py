import pytesseract
from PIL import Image
def binarizing(img,threshold):
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img
img1=Image.open("222.png")
w,h=img1.size
# region = (220*3,320*3,420*3,380*3)//两个一起
##将图片放大3倍
out=img1.resize((w*3,h*3),Image.ANTIALIAS)
region1 = (220*3,320*3,320*3,380*3)
cropImg1 = out.crop(region1)
img1= cropImg1.convert('L')
img1=binarizing(img1,200)
code1 = pytesseract.image_to_string(img1)

print ("整体搜索指数:" + str(code1).replace(".","").replace(" ",''))
