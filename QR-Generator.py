import qrcode #pip install qrcode
import image

qr = qrcode.QRCode(
version = 10,
box_size=5,
border=5
 )

url = "https://www.youtube.com/channel/UCSGwwLS-lyrSvtcY-W510Hg"

qr.add_data(url)
qr.make(fit=True)
img= qr.make_image(fill="black", back_color="white")
img.save("D:\\Python\\QR-Code-Generator\\qr-code.png")




