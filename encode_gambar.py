import base64
from PIL import Image
from io import BytesIO

with open("D:/UNS/UNS MADIUN/Sistem Keamanan Data/Materi_Praktikum/RSA/image_asli.jpg", "rb") as image_file:
    data = base64.b64encode(image_file.read())

print(data)
        
with open("D:/UNS/UNS MADIUN/Sistem Keamanan Data/Materi_Praktikum/RSA/encode_image_asli.txt", "w") as file:
    file.write(str(data))

im = Image.open(BytesIO(base64.b64decode(data)))
im.save('D:/UNS/UNS MADIUN/Sistem Keamanan Data/Materi_Praktikum/RSA/image1.png', 'PNG')