import qrcode #pip install qrcode
import image
from PIL import Image

qr = qrcode.QRCode(
version = 10,
box_size=5,
border=5
 )

url = str(input("Enter the URL for which you want the URL : "))
# url = "https://www.youtube.com/channel/UCSGwwLS-lyrSvtcY-W510Hg"
print("Generating QR Code")
qr.add_data(url)
qr.make(fit=True)
img= qr.make_image(fill="black", back_color="white")
print("Successfully generated QR Code")
img.save("D:\\Python\\QR-Code-Generator\\QR-Code.png")
print("Successfully saved QR Code")
print("Opening the QR Code")
imgshow = Image.open("D:\\Python\\QR-Code-Generator\\QR-Code.png")
imgshow.show()




