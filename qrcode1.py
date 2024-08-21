import qrcode

# Data to encode
data = "https://www.facebook.com"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # Size of the QR Code: 1 is the smallest
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Thickness of the border (minimum is 4)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)  # Adjust the QR code size automatically based on the data

# Create an image from the QR code instance
img = qr.make_image(fill="black", back_color="white")

# Save the image
img.save("qrcode_example1.png")
