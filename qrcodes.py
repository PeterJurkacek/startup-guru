import qrcode

links = [
    ("qr_aid.png", "https://www.aidental.ai"),
    # ("", "https://www.edu.aidental.ai"),
    ("qr_1.png", "https://www.linkedin.com/in/peter-jurkacek-a5966b209"),
]

for (name, url) in links:
    # Generate QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=2)
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="#9D79F7")

    # Save the image or display it
    img.save("slides/img/" + name)
    img.show()
