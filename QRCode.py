import qrcode

data = 'https://github.com/ViniCaetano'

img = qrcode.make(data)

img.save('D:/Python/Projetos/QR Code/GitHub.png')