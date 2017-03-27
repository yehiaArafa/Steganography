# Stegnography
python script to conceal a secret image into another image.

<h4>Steganography.py</h4> takes the original cover image (RGB format) and the secret image (Black and white) and output steg.png which is the final cover image contaning the secret image.

<h4>steganography_detection.py</h4> takes steg.png as an input and output the secret (black and white) image it contain.

<h4>Steganography_colored.py</h4> takes the original cover image (RGB format) and the secret image (8 bit colored image) and output steg.png which is the final cover image contaning the secret image.

<h4>steganography_colored_detection.py</h4> takes steg.png as an input and output the secret ( 8 bit gray scale colored) image it contain.   

### Threads are used to speed up the concealing and detection. Each Image is divided into 4 parallel sections working at the same time 
