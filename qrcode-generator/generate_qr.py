import os
import time
import qrcode
import platform
import subprocess

def generate_qrcode():
    user_data = input("Enter information for QR code: ")
    if user_data == "":
        print("Invalid input, please try again.")
        return

    # Create instance of qrcode class
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5,
    )

    # Generate unique filename
    timestamp = int(time.time())
    filename = "qrcode" + str(timestamp) + ".png"

    def create_qrcode():
        qr.add_data(user_data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename, "PNG")

    def open_qrcode():
        """Open qrcode file with default application"""
        if platform.system() == "Windows":
            subprocess.run(['start', filename], shell=True)
        elif platform.system() == "Darwin":
            os.system(f"open {filename}")
        elif platform.system() == "Linux":
            subprocess.run(['xdg-open', filename])
        else:
            return

    create_qrcode()
    open_qrcode()

generate_qrcode()