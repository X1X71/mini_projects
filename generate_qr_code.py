import qrcode

website_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

# integer from 1 to 40 that controls the size of the QR code
version = int(input("What size would you like your QR code to be? Enter a number from 1-40: "))
# integer that controls the size of each box in the QR code
box_size = int(input("How many pixels do you want each 'box' in the QR code? "))
# integer that controls the thickness of the border around the QR code
border = int(input("How many boxes thick do you want the border to be? "))

qr = qrcode.QRCode(version=version, 
                        error_correction=qrcode.constants.ERROR_CORRECT_M, 
                        box_size=box_size, 
                        border=border)
qr.add_data(website_link)
qr.make(fit=True)

img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save('youtube_qr.png')
