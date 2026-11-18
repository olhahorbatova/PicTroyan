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
    secret_text_len = len(datas)

    for x in range(width):
        for y in range(height):
            if pointer >= secret_text_len:
                break
            r,g,b = pixels[x,y]
            print(r,g,b)
            if pointer < secret_text_len:
                r = (r & ~1) | int(datas[pointer])
                pointer += 1
            if pointer < secret_text_len:
                g = (g & ~1) | int(datas[pointer])
                pointer += 1
            if pointer < secret_text_len:
                b = (b & ~1) | int(datas[pointer])
                pointer += 1

            pixels[x,y] = (r,g,b)
            print("-----------------------")
            print(r,g,b)
    img_rgb.save('cat_secret.png')
    return img_rgb
print(injection(img, st))
