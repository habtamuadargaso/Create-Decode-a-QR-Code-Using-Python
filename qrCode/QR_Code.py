import qrcode

# Data for which you want to make QR code
# Here we are using the URL of the MakeUseOf website
data = "https://www.google.com/"
# Generating the QR code
QRimage = qrcode.make(data)
# Save to
QRimage.save('myQr')
