# image-encryption
Encryption / decryption of images with AES in Python 3 (CBC and ECB mode supported)
The same as the [user163](https://github.com/user163/image-encryption), but with some more tweeks, like:

 - option to select the encryption / decryption method from AES.MODE_CBC or AES.MODE_ECB

 - encrypted / decrypted file is saved
  
 - user provides the key

 - key is used as an SHA256

### Dependencies

- opencv (s. https://github.com/skvark/opencv-python)

- pycryptodome (s. https://www.pycryptodome.org/en/latest/)

- numpy (s. https://numpy.org/doc/)

### Image formats

- The images to be encrypted can be in one of the common formats (jpg, bmp, etc.). 

- Encrypted images are saved in .bmp, a lossless format for maintaining the headers.

### Program execution and flow

- Start the program under Windows / Mac in the comand prompt / terminal with: python3 main.py (or just python, but ensure it is +v3)

- Once the program is started, select the desired options. The images to encrypt / decrypt are presented. To proceed, press ENTER, with the presented window selected.

### Example

Original image

![Alt text](images/original/imageToCypher.jpeg?raw=true "Title")

Encrypted image (CBC mode)

![Alt text](images/encrypted/img_AES_CBC_ENCRYPTED_1648753699.bmp?raw=true "Title")

Encrypted image (ECB mode)

![Alt text](images/encrypted/img_AES_ECB_ENCRYPTED_1648753559.bmp?raw=true "Title")

Decrypted image

![Alt text](images/decrypted/img_AES_CBC_DECRYPTED_1648753739.jpg?raw=true "Title")

### Credits

All credits goes to [user163](https://github.com/user163), for the starting of this work.
