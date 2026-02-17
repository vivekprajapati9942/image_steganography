#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image

def decode_image(image_path):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()

    binary_data = ""
    decoded_message = ""

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]

            for color in (r, g, b):
                # Last bit read kar rahe hain
                binary_data += str(color & 1)

                if len(binary_data) % 8 == 0:
                    byte = binary_data[-8:]
                    decoded_message += chr(int(byte, 2))

                    if decoded_message.endswith("|||END|||"):
                        print("Decoded Message:", decoded_message[:-9])
                        return

    print("No hidden message found.")


# ---------- Run ----------
image_path = input("Enter image path to decode: ")

decode_image(image_path)


# In[ ]:




