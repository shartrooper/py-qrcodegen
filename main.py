import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

#generation
data = "Interface demodulator"

qr= qrcode.QRCode(version = 1,box_size=10,border=4)

qr.add_data(data)

img=qr.make_image(fill_color= 'red', back_color= 'white', fit= 'True')

img.save('myqrcode.png')

#decoding generated img

img= Image.open('myqrcode.png')

result=decode(img)

print(result)