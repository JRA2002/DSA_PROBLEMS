import pyqrcode


text = input("Enter a text to convert a QR")
qr_code = pyqrcode.create(text)

qr_code.svg('qr_code.svg', scale = 8)