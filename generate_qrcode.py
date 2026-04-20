import qrcode

# Data to encode
data = "https://ruslylove.github.io/AI-workshop"

# Create QR Code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
# To use 'make_image', you need the Pillow library installed (pip install pillow)
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("public/qrcode_slides.png")

print("QR code generated and saved to public/qrcode_slides.png")
