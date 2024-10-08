import qrcode

links = [
    ("qr_aid.png", "https://www.aidental.ai"),
    # ("", "https://www.edu.aidental.ai"),
    ("qr_1.png", "https://www.linkedin.com/in/peter-jurkacek-a5966b209"),
    ("qr_form_intro.png", "https://aidental.typeform.com/to/MLtakqKO"),
    ("qr_form_feedback.png", "https://aidental.typeform.com/to/VKpVamog")
]

for (name, url) in links:
    # Generate QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=2)
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="#FFFFFF")

    # Save the image or display it
    img.save("slides/img/" + name)
    img.show()
