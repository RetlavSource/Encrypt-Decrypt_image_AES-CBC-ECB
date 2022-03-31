import sys
import cv2
from Cryptodome.Cipher import AES
import aes_cbc_encryption
import aes_ecb_encryption


def show_original_image(header_name, file_path):
    # Load original image from "images/original/imageToCypher.jpeg"
    image_orig = cv2.imread(file_path)
    row_orig, column_orig, depth_orig = image_orig.shape

    min_width = (AES.block_size + AES.block_size) // depth_orig + 1
    if column_orig < min_width:
        print(f'The minimum width of the image must be {min_width} pixels, so that IV and padding can be stored in a single additional row!')
        sys.exit()

    # Display original image
    cv2.imshow(header_name, image_orig)
    cv2.waitKey()
    return image_orig


def get_input_filepath():
    path_file = input("""
    Enter the path with the name of the file to encrypt:
    """)
    if len(path_file) < 1:
        print('The file must have at least 1 character long.')
        sys.exit()
    return path_file
    

def get_input_key():
    key = input("""
    Enter the secret key to use as the cipher:
    """)
    if len(key) < 1:
        print('The secret key must be at least 1 character long.')
        sys.exit()
    return key


if __name__ == '__main__':
    print('Encryption images using AES algorithm.')
    encMode = int(input("""
    Select the Encryption mode:

    1. ENCRYPT image using AES_CBC
    2. DECRYPT image using AES_CBC

    3. ENCRYPT image using AES_ECB
    4. DECRYPT image using AES_ECB

    """))

    if encMode == 1:
        print('\nEncrypting image using AES_CBC...')

        path_file = get_input_filepath()
        key = get_input_key()
        
        image = show_original_image("Original Image", path_file)
        print('\nEncrypting...')
        aes_cbc_encryption.encrypt(image, key)

    elif encMode == 2:
        print('\nDecrypting image using AES_CBC...')

        path_file = get_input_filepath()
        key = get_input_key()

        image = show_original_image("Encrypted Image", path_file)
        print('\nDecrypting...')
        aes_cbc_encryption.decrypt(image, key)

    elif encMode == 3:
        print('\nEncrypting image using AES_ECB...')

        path_file = get_input_filepath()
        key = get_input_key()
        
        image = show_original_image("Original Image", path_file)
        print('\nEncrypting...')
        aes_ecb_encryption.encrypt(image, key)

    elif encMode == 4:
        print('\nDecrypting image using AES_ECB...')

        path_file = get_input_filepath()
        key = get_input_key()
        
        image = show_original_image("Encrypted Image", path_file)
        print('\nDecrypting...')
        aes_ecb_encryption.decrypt(image, key)

    else:
        print('!!!WRONG OPTION SELECTED!!!')
        sys.exit()