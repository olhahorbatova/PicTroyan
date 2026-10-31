from PIL import Image

img = Image.open('cat.jpg')

def to_bytes(img):
    img_result = img.convert('RGB')
    print(img_result)

to_bytes(img)
#function of bites mooving


#result image


