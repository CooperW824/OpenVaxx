
"""# Importing library
import qrcode
  
# Data to encode
data = "12345678901234567890"
  
# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 5)
  
# Adding data to the instance 'qr'
qr.add_data(data)
  
qr.make(fit = True)
img = qr.make_image(fill_color = 'black',
                    back_color = 'white')

from pathlib import Path
str_path = "OpenVaxxDB/qrcode.png"
path = Path(str_path)

img.save(path)"""

"""import shutil
import os
src_path = os.getcwd() + '\\OpenVaxxDB\\qrcode.png'
shutil.copy(src_path, r"C:/Users/coope/Documents/GitHub/OpenVaxx")"""
