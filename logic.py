from PIL import Image

img = Image.open('cat.jpg')

def secret_text():
    text = "Dangerous script"
    bynary_text = text.encode('utf-8')
    return str(bynary_text.hex())

def to_bytes(img):
    img_result = (img.convert('RGB')).tobytes()
    print(img_result)

#to_bytes(img)
print(secret_text())
#function of bites mooving


#result image


