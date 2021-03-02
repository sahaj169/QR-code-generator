import qrcode

qr = qrcode.QRCode(
    version=5,
    box_size=25,
    border=5,
    )

data = str(input("Enter the string which you want to convert into QR Code: "))

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill='black',back_color = 'white')

try:
    img.save(f"{data}.png")
except :
    img.save("qrcode.png")
