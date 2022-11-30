#Método Pillow deve estar instalado.
import qrcode

data = 'https://youtu.be/kdQvRo-0KkQ'

img = qrcode.make(data)

img.save('D:/Python/Projetos/QR Code/temquerespeitar.png')