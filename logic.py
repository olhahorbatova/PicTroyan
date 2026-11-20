from base64 import decode
from PIL import Image
img = Image.open('cat.jpg')
def secret_text(text):
    bynary_text = text.encode('utf-8')
    decodes = ''.join(format(b, '08b') for b in bynary_text)#to 0 && 1 from str:)
    return decodes#len chranit` v secret_text_len


st = secret_text("Dangerous script")#rozpakouka def
secret_text_len = len(st)
#print(len(st))
#print(f'My secret text {st}')
def injection(img, datas):
    width, height = img.size
    img_rgb = img.convert('RGB')
    pixels = img_rgb.load()
    secret_text_len = len(datas)
    pointer = 0
    pointer_len = 0
    list = []
    list32byt = []
    bynary_len = format(secret_text_len, '032b')
    print(bynary_len)
    for x in range(width):#cycle dlia zapisi 32 bit v nachale stroki
        for y in range(height):
            if pointer_len >= 32:
                break
            r, g, b = pixels[x, y]
            if pointer_len < 32:
                r = (r & ~1) | int(bynary_len[pointer_len])
                pointer_len += 1
            if pointer_len < 32:
                g = (g & ~1) | int(bynary_len[pointer_len])
                pointer_len += 1
            if pointer_len < 32:
                b = (b & ~1) | int(bynary_len[pointer_len])
                pointer_len += 1

            pixels[x, y] = (r, g, b)
            list32byt.append((r, g, b))
    print(list32byt)

    img_rgb.save('cat_secret.png')

    for x in range(width):
        for y in range(height):
            if pointer >= secret_text_len:
                break
            r,g,b = pixels[x,y]
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
            list.append((r, g, b))

    #img_rgb.save('cat_secret.png')
    return img_rgb, len(list)

cat, lenlist = injection(img, st)

def extractor(img, lenght_extract):
    pointer = 0
    li = []
    img = Image.open(img)
    img_rgb = img.convert('RGB')
    pixels = img_rgb.load()

    for x in range(0, 43):
        for y in range(0, 43):
            if pointer >= lenght_extract:
                break
            if pointer < lenght_extract:
                li.append(pixels[x,y])
                pointer += 1

    #print(f'dlinna spiska dlia deshifratora (RGB) {len(li)}')
    li_bit = []
    for i in range(0, len(li)):
        for j in range(0, len(li[i])):
            if li[i][j] % 2 == 0:
                li_bit.append(0)
            if  li[i][j] % 2 == 1:
                li_bit.append(1)
            if len(li_bit) == secret_text_len:
                break

    lenlibit = len(li_bit)
    #print(li_bit)
    str_bit = "".join(map(str, li_bit))
    #print(str_bit)
    litera = lenlibit // 8

    for i in range(0, len(str_bit), 8):
        s = str_bit[i:i+8]
        print(chr(int(s, 2)), end='')




extractor('cat_secret.png', 43)
