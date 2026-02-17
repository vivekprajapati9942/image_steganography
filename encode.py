#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image

def encode_image(image_path, message):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()

    # End marker add kar rahe hain
    message += "|||END|||"

    # Message ko binary me convert kar rahe hain
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    data_index = 0
    data_length = len(binary_message)

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]

            new_colors = []
            for color in (r, g, b):
                if data_index < data_length:
                    # Last bit replace kar rahe hain
                    new_color = (color & ~1) | int(binary_message[data_index])
                    data_index += 1
                else:
                    new_color = color
                new_colors.append(new_color)

            pixels[x, y] = tuple(new_colors)

            if data_index >= data_length:
                break
        if data_index >= data_length:
            break

    img.save("output.png")
    print("Message Stored Successfully in output.png")


# ---------- Run ----------
image_path = input("Enter PNG image path: ")
message = input("Enter message to hide: ")

encode_image(image_path, message)


# In[ ]:




