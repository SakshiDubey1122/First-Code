import qrcode
data = "Sakshi Dubey"
qr = qrcode.make(data)
qr.save("qrcode.png")
print("QR Code Genetrated Successfully")
