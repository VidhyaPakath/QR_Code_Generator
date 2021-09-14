import qrcode

web_link = input("Enter the link of the website for which QR Code has to be generated : ")
final_link = f'"{web_link}"'

#final_link = '"' + web_link + '"'
#print(final_link)
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border=4)

qr.add_data(final_link)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("sample.png")
