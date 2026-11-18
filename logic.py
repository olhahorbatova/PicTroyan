from PIL import Image

img = Image.open('cat.jpg')

def secret_text():
    text = "Dangerous script#END#"
    bynary_text = text.encode('utf-8')
    decode = ''.join(format(b, '08b') for b in bynary_text)#to 0 && 1 from str:)

    return decode

#delete

def injection(img, secret_text):

    pass


print(img.size)

#result image


