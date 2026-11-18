from PIL import Image

img = Image.open('cat.jpg')

def secret_text():
    text = "Dangerous script"
    bynary_text = text.encode('utf-8') + "end"
    decode = ''.join(format(b, '08b') for b in bynary_text)#to 0 && 1 from str:)

    return decode

def pic_to_bytes(img):
    img_result = (img.convert('RGB')).tobytes()
    print(img_result)

#to_bytes(img)
print(secret_text())
#function of bites mooving


#result image


