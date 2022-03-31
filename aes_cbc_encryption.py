import time
import cv2
import hashlib
import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Set sizes
keySize = 32
initialization_vector_size = AES.block_size

def encrypt(image_original, password):
    # This program encrypts a jpg With AES-256. The encrypted image contains more data than the original image (e.g. because of 
    # padding, IV etc.). Therefore the encrypted image has one row more. Supported are CBC and ECB mode.

    # Load original image
    rowOrig, columnOrig, depthOrig = image_original.shape

    # Convert original image data to bytes
    imageOrigBytes = image_original.tobytes()

    # encrypt password
    # password = "ThisisAPasswordVaryGoodAndEvenBetterOne"
    hash = hashlib.sha256(password.encode())
    digested = hash.digest()
    key = digested
    iv = digested.ljust(initialization_vector_size)[:initialization_vector_size]



    # Encrypt
    cipher = AES.new(key, AES.MODE_CBC, iv)
    imageOrigBytesPadded = pad(imageOrigBytes, AES.block_size)
    ciphertext = cipher.encrypt(imageOrigBytesPadded)

    # Convert ciphertext bytes to encrypted image data
    #    The additional row contains columnOrig * DepthOrig bytes. Of this, ivSize + paddedSize bytes are used 
    #    and void = columnOrig * DepthOrig - ivSize - paddedSize bytes unused
    paddedSize = len(imageOrigBytesPadded) - len(imageOrigBytes)
    void = columnOrig * depthOrig - initialization_vector_size - paddedSize
    ivCiphertextVoid = iv + ciphertext + bytes(void)
    imageEncrypted = np.frombuffer(ivCiphertextVoid, dtype = image_original.dtype).reshape(rowOrig + 1, columnOrig, depthOrig)

    # Saving encrypted image
    image_name = f"img_AES_CBC_ENCRYPTED_{str(int(time.time()))}.bmp"
    cv2.imwrite(f"images/encrypted/{image_name}", imageEncrypted)
    print(f"Image saved in 'images/encrypted/' folder, with name: {image_name}")

    # Display encrypted image
    cv2.imshow("Encrypted image", imageEncrypted)
    cv2.waitKey()

    # Save the encrypted image (optional)
    #    If the encrypted image is to be stored, a format must be chosen that does not change the data. Otherwise, 
    #    decryption is not possible after loading the encrypted image. bmp does not change the data, but jpg does. 
    #    When saving with imwrite, the format is controlled by the extension (.jpg, .bmp). The following works:
    #    cv2.imwrite("topsecretEnc.bmp", imageEncrypted)
    #    imageEncrypted = cv2.imread("topsecretEnc.bmp")

    # Close all windows
    cv2.destroyAllWindows()


def decrypt(imageEncrypted, password):
    # encrypt password
    # password = "ThisisAPasswordVaryGoodAndEvenBetterOne"
    hash = hashlib.sha256(password.encode())
    key = hash.digest()

    # Convert encrypted image data to ciphertext bytes
    rowEncrypted, columnOrig, depthOrig = imageEncrypted.shape 
    rowOrig = rowEncrypted - 1
    encryptedBytes = imageEncrypted.tobytes()
    iv = encryptedBytes[:initialization_vector_size]
    imageOrigBytesSize = rowOrig * columnOrig * depthOrig
    paddedSize = (imageOrigBytesSize // AES.block_size + 1) * AES.block_size - imageOrigBytesSize
    encrypted = encryptedBytes[initialization_vector_size : initialization_vector_size + imageOrigBytesSize + paddedSize]

    # Decrypt
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decryptedImageBytesPadded = cipher.decrypt(encrypted)
    decryptedImageBytes = unpad(decryptedImageBytesPadded, AES.block_size)

    # Convert bytes to decrypted image data
    decryptedImage = np.frombuffer(decryptedImageBytes, imageEncrypted.dtype).reshape(rowOrig, columnOrig, depthOrig)

    # Saving decrypted image
    image_name = f"img_AES_CBC_DECRYPTED_{str(int(time.time()))}.jpg"
    cv2.imwrite(f"images/decrypted/{image_name}", decryptedImage)
    print(f"Image saved in 'images/decrypted/' folder, with name: {image_name}")

    # Display decrypted image
    cv2.imshow("Decrypted Image", decryptedImage)
    cv2.waitKey()

    # Close all windows
    cv2.destroyAllWindows()

