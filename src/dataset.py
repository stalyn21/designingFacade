#install cv2 with this command $ pip install opencv-python (21,21),0
import cv2 
b=34
c=5
f=80
for i in range(b):
    image = cv2.imread(f'ImagesDataSet/barcelona_0{i}.png')
    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(grey_img)
    blur = cv2.GaussianBlur(invert, (31,31),6)
    invertedblur = cv2.bitwise_not(blur)
    sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
    cv2.imwrite(f'ImagesDataSet/barcelonaEdited/barcelona_0{i}.png', sketch)

"""for i in range(c):
    image = cv2.imread(f'in/Cuenca{i}.png')
    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(grey_img)
    blur = cv2.GaussianBlur(invert, (31,31),4)
    invertedblur = cv2.bitwise_not(blur)
    sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
    cv2.imwrite(f'ImagesDataSet/cuencaEdited/cuenca{i}.png', sketch)"""

for i in range(1,f):
    image = cv2.imread(f'ImagesDataSet/facade_{i}.png')
    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(grey_img)
    blur = cv2.GaussianBlur(invert, (31,31),6)
    invertedblur = cv2.bitwise_not(blur)
    sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
    cv2.imwrite(f'ImagesDataSet/facadeEdited/facade_{i}.png', sketch)
