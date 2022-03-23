import qrcode

# Data for which you want to make QR code
# Here we are using the URL of the MakeUseOf website
data = "https://www.facebook.com/stories/129575584965605/UzpfSVNDOjExMzM4OTAwNDcxODI4NDY=/?bucket_count=9&source=story_tray"
# Generating the QR code
QRimage = qrcode.make(data)
# Save to
QRimage.save('myQr.png')
