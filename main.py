import os
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from PIL import Image

def capture_and_decode(image):
    # Carrega a imagem e converte para um array numpy
    img = Image.open(image)
    img_np = np.array(img)
    
    # Decodifica o QR code
    qr_codes = decode(img_np)
    for qr_code in qr_codes:
        data = qr_code.data.decode("utf-8")
        print("QR Code data:", data)
    
    # Exibe a imagem capturada (opcional)
    cv2.imshow("Screenshot", img_np)
    cv2.waitKey(2000)  # Exibe por 2 segundos
    cv2.destroyAllWindows()


image = input('image > ')
capture_and_decode(image)
