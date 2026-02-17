# Image Steganography using LSB Technique (Python)

This project implements Least Significant Bit (LSB) steganography 
to hide and retrieve secret messages inside PNG images using Python.

## Overview
This system embeds secret text inside PNG images by modifying 
the least significant bits of pixel values without visibly 
changing the image.

## Features
- Hide secret message inside PNG image
- Extract hidden message from image
- Pixel-level LSB manipulation
- Simple command-line execution

## Technologies Used
- Python
- Pillow (PIL Library)

## Installation

Install required library:

pip install pillow

## How to Run

Step 1: Run the encode script  
python encode.py  

Enter:
- PNG image path
- Message to hide  

This will generate:
output.png (image containing hidden message)

Step 2: Run the decode script  
python decode.py  

Enter:
- Path of encoded image (output.png)  

The hidden message will be displayed on screen.

## Important Notes
- Use only PNG images.
- Do not compress the encoded image.
- Image size should be sufficient to store the message.

## Concept
This project uses the Least Significant Bit (LSB) technique 
to embed binary message data into RGB pixel values.

## Author
Developed for academic and cybersecurity learning purposes.
