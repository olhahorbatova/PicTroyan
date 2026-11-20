from base64 import decode
from PIL import Image
img = Image.open('cat.jpg')
def secret_text(text):
    bynary_text = text.encode('utf-8')
    decodes = ''.join(format(b, '08b') for b in bynary_text)#to 0 && 1 from str:)
    return decodes#len chranit` v secret_text_len


st = secret_text("Dangerous script")#rozpakouka def
secret_text_len = len(st)
def injection(img, datas):
    width, height = img.size
    img_rgb = img.convert('RGB')
    pixels = img_rgb.load()
    secret_text_len = len(datas)
    pointer = 0
    list1 = []
    header = format(secret_text_len, '032b')
    all_len = header + datas
    sum = len(all_len)
    for x in range(width):
        for y in range(height):
            if pointer >= sum:
                break
            r, g, b = pixels[x, y]
            if pointer < sum:
                r = (r & ~1) | int(all_len[pointer])
                pointer += 1
            if pointer < sum:
                g = (g & ~1) | int(all_len[pointer])
                pointer += 1
            if pointer < sum:
                b = (b & ~1) | int(all_len[pointer])
                pointer += 1

            pixels[x, y] = (r, g, b)
            list1.append((r, g, b))
    img_rgb.save('cat_secret.png')
    return img_rgb, list1#160

cat, list1 = injection(img, st)
print(len(list1))#160

def header_extract(list_header):
    li_32 = []
    for i in range(0, len(list_header)):
        for j in range(0, len(list_header[i])):
            if list_header[i][j] % 2 == 0:
                li_32.append(0)
            if  list_header[i][j] % 2 == 1:
                li_32.append(1)
            if len(li_32) == 32:
                break
    header2 = li_32[0:32]
    str_header = ''.join(map(str, header2))
    int_header = int(str_header, 2)
    return int_header

int_header = header_extract(list1)

def extractor(img, lenght_extract, header):
    pointer = 0
    li = []
    li1 = []
    img = Image.open(img)
    img_rgb = img.convert('RGB')
    pixels = img_rgb.load()
    for x in range(0, 54):
        for y in range(0, 54):
            if pointer >= lenght_extract:
                break
            if pointer < lenght_extract:
                li.append(pixels[x,y])
                pointer += 1

    li_bit = []
    print(li)
    for i in range(0, len(li)):
        for j in range(0, len(li[i])):
            if li[i][j] % 2 == 0:
                li_bit.append(0)
            if  li[i][j] % 2 == 1:
                li_bit.append(1)
            if len(li_bit) == secret_text_len:
                break

    lenlibit = len(li_bit)
    str_bit = "".join(map(str, li_bit))
    litera = lenlibit // 8
    for i in range(0, len(str_bit), 8):
        s = str_bit[i:i+8]
        print(chr(int(s, 2)), end='')

#extractor('cat_secret.png', 54)
