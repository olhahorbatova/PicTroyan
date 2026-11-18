from base64 import decode

from PIL import Image

img = Image.open('cat.jpg')

def secret_text():
    text = "Dangerous script"
    bynary_text = text.encode('utf-8')
    decode = ''.join(format(b, '08b') for b in bynary_text)#to 0 && 1 from str:)

    return decode#len128

st = secret_text()
def injection(img, datas):
    width, height = img.size
    img_rgb = img.convert('RGB')
    pixels = img_rgb.load()

    pointer = 0
    secret_text_len = len(secret_text())

    for x in range(width):
        for y in range(height):
            if pointer >= secret_text_len:
                break
            r,g,b = pixels[x,y]
            print(r,g,b)

    return pixels


print(injection(img, st))




