import pyotp
import qrcode
import os

def get_stored_key(filename='chave.txt'):
    if os.path.exists(filename):
        # Se o arquivo existir, leia e retorne o segredo armazenado
        with open(filename, 'r') as file:
            return file.read().strip()
    else:
        # Se o arquivo não existir, gere um novo segredo Base32 e salve-o
        key = pyotp.random_base32()
        with open(filename, 'w') as file:
            file.write(key)
        return key

chave = get_stored_key()

link = pyotp.TOTP(chave).provisioning_uri(name="Teste", issuer_name="Autenticador")
img_qrcode = qrcode.make(link)
img_qrcode.save("qrcode.png")

class Autenticador():
    codigo = pyotp.TOTP(chave)
    print(codigo.now())
